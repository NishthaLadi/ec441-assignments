"""
HTTP Protocol Behavior Lab
Topic 10: Application Layer

This script measures:
1. Status code behavior
2. Request latency with and without persistent sessions
3. Head-of-line blocking behavior using sequential vs parallel delayed requests

Outputs are saved in the outputs/ folder.
"""

from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import statistics

import requests
import pandas as pd
import matplotlib.pyplot as plt


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

BASE_URL = "https://example.com"
STATUS_URLS = {
    200: "https://httpbin.org/status/200",
    301: "https://httpbin.org/status/301",
    404: "https://httpbin.org/status/404",
    500: "https://httpbin.org/status/500",
}
DELAY_URL = "https://httpbin.org/delay/2"


def timed_get(url: str, session=None, timeout: int = 10):
    """Send GET request and return latency and status code."""
    client = session if session is not None else requests
    start = time.perf_counter()

    try:
        response = client.get(url, timeout=timeout)
        elapsed = time.perf_counter() - start
        return {
            "url": url,
            "status_code": response.status_code,
            "latency_seconds": elapsed,
            "error": None,
        }
    except Exception as exc:
        elapsed = time.perf_counter() - start
        return {
            "url": url,
            "status_code": None,
            "latency_seconds": elapsed,
            "error": str(exc),
        }


def experiment_status_codes():
    """Test representative status code categories."""
    rows = []

    for expected_code, url in STATUS_URLS.items():
        result = timed_get(url)
        result["experiment"] = "status_code"
        result["expected_status"] = expected_code
        rows.append(result)

    return rows


def experiment_keep_alive(num_requests: int = 10):
    """Compare repeated requests with and without a persistent session."""
    rows = []

    for i in range(num_requests):
        result = timed_get(BASE_URL)
        result["experiment"] = "no_session"
        result["request_number"] = i + 1
        rows.append(result)

    with requests.Session() as session:
        for i in range(num_requests):
            result = timed_get(BASE_URL, session=session)
            result["experiment"] = "session_keep_alive"
            result["request_number"] = i + 1
            rows.append(result)

    return rows


def experiment_hol_blocking(num_requests: int = 5):
    """Compare sequential delayed requests against parallel delayed requests."""
    rows = []

    start = time.perf_counter()
    for i in range(num_requests):
        result = timed_get(DELAY_URL, timeout=15)
        result["experiment"] = "hol_sequential"
        result["request_number"] = i + 1
        result["total_experiment_time"] = time.perf_counter() - start
        rows.append(result)

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(timed_get, DELAY_URL, None, 15) for _ in range(num_requests)]

        for i, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            result["experiment"] = "hol_parallel"
            result["request_number"] = i
            result["total_experiment_time"] = time.perf_counter() - start
            rows.append(result)

    return rows


def plot_latency_comparison(df: pd.DataFrame):
    """Plot latency distributions for session vs no session."""
    subset = df[df["experiment"].isin(["no_session", "session_keep_alive"])].copy()

    groups = [
        subset[subset["experiment"] == "no_session"]["latency_seconds"].dropna(),
        subset[subset["experiment"] == "session_keep_alive"]["latency_seconds"].dropna(),
    ]

    plt.figure(figsize=(8, 5))
    plt.boxplot(groups, labels=["No Session", "Session / Keep-Alive"])
    plt.ylabel("Latency (seconds)")
    plt.title("HTTP Request Latency: No Session vs Keep-Alive Session")
    plt.grid(True, axis="y")
    plt.savefig(OUTPUT_DIR / "latency_comparison.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_status_codes(df: pd.DataFrame):
    """Plot observed status code counts."""
    subset = df[df["experiment"] == "status_code"].copy()
    counts = subset["status_code"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))
    plt.bar([str(int(x)) for x in counts.index], counts.values)
    plt.xlabel("HTTP Status Code")
    plt.ylabel("Count")
    plt.title("Observed HTTP Status Code Distribution")
    plt.grid(True, axis="y")
    plt.savefig(OUTPUT_DIR / "status_code_distribution.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_hol_blocking(df: pd.DataFrame):
    """Plot cumulative completion time for sequential vs parallel delayed requests."""
    subset = df[df["experiment"].isin(["hol_sequential", "hol_parallel"])].copy()

    plt.figure(figsize=(8, 5))

    for experiment_name, label in [
        ("hol_sequential", "Sequential requests"),
        ("hol_parallel", "Parallel requests"),
    ]:
        group = subset[subset["experiment"] == experiment_name].sort_values("request_number")
        plt.plot(
            group["request_number"],
            group["total_experiment_time"],
            marker="o",
            label=label,
        )

    plt.xlabel("Completed Request Number")
    plt.ylabel("Cumulative Experiment Time (seconds)")
    plt.title("Head-of-Line Blocking: Sequential vs Parallel Requests")
    plt.grid(True)
    plt.legend()
    plt.savefig(OUTPUT_DIR / "hol_blocking.png", dpi=300, bbox_inches="tight")
    plt.close()


def print_summary(df: pd.DataFrame):
    """Print a concise summary of measured results."""
    print("\n=== HTTP Lab Summary ===")

    for experiment in ["no_session", "session_keep_alive"]:
        latencies = df[df["experiment"] == experiment]["latency_seconds"].dropna().tolist()
        if latencies:
            print(f"{experiment}: mean={statistics.mean(latencies):.4f}s, "
                  f"min={min(latencies):.4f}s, max={max(latencies):.4f}s")

    for experiment in ["hol_sequential", "hol_parallel"]:
        subset = df[df["experiment"] == experiment]
        if not subset.empty:
            total_time = subset["total_experiment_time"].max()
            print(f"{experiment}: total_time={total_time:.4f}s")

    print("\nGenerated files:")
    print(f"- {OUTPUT_DIR / 'latency_comparison.png'}")
    print(f"- {OUTPUT_DIR / 'status_code_distribution.png'}")
    print(f"- {OUTPUT_DIR / 'hol_blocking.png'}")
    print(f"- {OUTPUT_DIR / 'http_lab_results.csv'}")


def main():
    rows = []
    rows.extend(experiment_status_codes())
    rows.extend(experiment_keep_alive(num_requests=10))
    rows.extend(experiment_hol_blocking(num_requests=5))

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_DIR / "http_lab_results.csv", index=False)

    plot_latency_comparison(df)
    plot_status_codes(df)
    plot_hol_blocking(df)

    print_summary(df)


if __name__ == "__main__":
    main()
