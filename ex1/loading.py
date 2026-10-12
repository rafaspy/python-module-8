import importlib


def check_package(package_name: str) -> bool:
    """Check if a Python package is installed."""
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False


def get_package_version(package_name: str) -> str:
    """Return the installed version of a package."""
    module = importlib.import_module(package_name)
    return getattr(module, "__version__", "unknown")


def check_dependencies() -> bool:
    """Check required packages and display their versions."""
    packages = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }

    all_available = True

    print("Checking dependencies:")

    for package, description in packages.items():
        if check_package(package):
            version = get_package_version(package)
            print(f"[OK] {package} ({version}) - {description} ready")
        else:
            print(f"[MISSING] {package} - {description} unavailable")
            all_available = False

    return all_available


def compare_package_versions() -> None:
    """Display the versions of the installed packages."""
    packages = ["pandas", "numpy", "matplotlib"]

    print("\nPackage versions:")

    for package in packages:
        version = get_package_version(package)
        print(f"{package}: {version}")


def analyze_matrix_data() -> None:
    """Generate and analyze simulated Matrix data."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = np.random.randn(1000)

    df = pd.DataFrame({
        "matrix_value": data
    })

    print(f"Processing {len(df)} data points...")

    print("Generating visualization...")

    plt.plot(df["matrix_value"])
    plt.title("Matrix Data")
    plt.xlabel("Data Point")
    plt.ylabel("Matrix Value")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("Loading Programs")
    print("LOADING STATUS: Loading programs...\n")

    dependencies_available = check_dependencies()

    if not dependencies_available:
        print("\nSome dependencies are missing.")
        print("Install them with pip:")
        print("pip install -r requirements.txt")
        print("\nOr install them with Poetry:")
        print("poetry install")
        return

    compare_package_versions()
    analyze_matrix_data()


if __name__ == "__main__":
    main()
