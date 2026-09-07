# Import errors are explicitly allowed on this file by the subject:
# missing dependencies must be detected and reported, not crash the
# program. Loading each heavy library through importlib (instead of
# a plain "import numpy as np") is the trick that keeps mypy --strict
# happy even when a package has no type stubs installed.
import importlib
import sys
from typing import Any, Optional


def _try_import(module_name: str) -> Optional[Any]:
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


np = _try_import("numpy")
pd = _try_import("pandas")
matplotlib = _try_import("matplotlib")
requests = _try_import("requests")

plt = None
if matplotlib is not None:
    matplotlib.use("Agg")
    plt = _try_import("matplotlib.pyplot")


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_ok = True

    if np is not None:
        print(f"[OK] numpy ({np.__version__}) - "
              "Numerical computation ready")
    else:
        print("[MISSING] numpy - run: pip install numpy")
        all_ok = False

    if pd is not None:
        print(f"[OK] pandas ({pd.__version__}) - "
              "Data manipulation ready")
    else:
        print("[MISSING] pandas - run: pip install pandas")
        all_ok = False

    if requests is not None:
        version = getattr(requests, "__version__", "unknown")
        print(f"[OK] requests ({version}) - Network access ready")

    if plt is not None and matplotlib is not None:
        print(f"[OK] matplotlib ({matplotlib.__version__}) - "
              "Visualization ready")
    else:
        print("[MISSING] matplotlib - run: pip install matplotlib")
        all_ok = False

    return all_ok


def generate_matrix_data(size: int = 1000) -> Any:
    if np is None:
        raise RuntimeError("numpy is required to generate Matrix data")
    rng = np.random.default_rng(seed=42)
    return rng.normal(loc=0.0, scale=1.0, size=size)


def analyze_matrix_data(data: Any) -> Any:
    if pd is None:
        raise RuntimeError("pandas is required to analyze Matrix data")
    frame = pd.DataFrame({"signal": data})
    return frame.describe()


def plot_matrix_data(data: Any, output_path: str) -> None:
    if plt is None:
        raise RuntimeError("matplotlib is required to plot Matrix data")
    plt.figure()
    plt.plot(data)
    plt.title("Matrix Data Stream")
    plt.savefig(output_path)
    plt.close()


def compare_pip_and_poetry() -> None:
    print("\nDependency management: pip vs Poetry")
    print(
        "pip installs the flat list of packages in requirements.txt, "
        "with no automatic lock file."
    )
    print(
        "Poetry reads pyproject.toml, resolves the full dependency "
        "graph, and writes poetry.lock so installs are reproducible."
    )


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print("\nInstall missing dependencies with either:")
        print("  pip install -r requirements.txt")
        print("  poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    data = generate_matrix_data()
    print(f"Processing {len(data)} data points...")
    print(analyze_matrix_data(data))

    print("Generating visualization...")
    plot_matrix_data(data, "matrix_analysis.png")

    compare_pip_and_poetry()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
