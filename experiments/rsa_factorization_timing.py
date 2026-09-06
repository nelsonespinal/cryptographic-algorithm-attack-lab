import time
import statistics
import matplotlib.pyplot as plt
import csv

from src.rsa import generate_keys
from src.attacks.rsa_factorization import factor_modulus


def measure_factorization_time(bits):
    public_key, _, _, _, _ = generate_keys(bits=bits)

    _, n = public_key

    start = time.perf_counter()

    factor_modulus(n)

    end = time.perf_counter()

    return end - start


def run_experiment(bit_sizes, trials=20):
    results = []

    for bits in bit_sizes:
        times = []

        for _ in range(trials):
            elapsed = measure_factorization_time(bits)
            times.append(elapsed)

        average = statistics.mean(times)
        median = statistics.median(times)

        results.append((bits, average, median))

    return results


def save_results_to_csv(results):
    filename = "experiments/rsa_factorization_results.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Prime Bit Length",
            "Average Factorization Time (seconds)",
            "Median Factorization Time (seconds)",
        ])

        for bits, average, median in results:
            writer.writerow([
                bits,
                average,
                median,
            ])


def plot_results(results):
    bit_sizes = [bits for bits, _, _ in results]
    averages = [average for _, average, _ in results]
    medians = [median for _, _, median in results]

    plt.figure(figsize=(8, 5))

    plt.plot(
        bit_sizes,
        averages,
        marker="o",
        label="Average"
    )

    plt.plot(
        bit_sizes,
        medians,
        marker="o",
        label="Median"
    )

    plt.xlabel("Prime Bit Length")
    plt.ylabel("Factorization Time (seconds)")
    plt.title("RSA Factorization Time vs. Prime Bit Length")

    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "experiments/rsa_factorization_timing.png",
        dpi=300
    )

    plt.show()


if __name__ == "__main__":
    bit_sizes = [8, 10, 12, 14, 16]

    results = run_experiment(bit_sizes, trials=20)

    for bits, average, median in results:
        print(
            f"{bits}-bit primes | "
            f"Average: {average:.6f} s | "
            f"Median: {median:.6f} s"
        )

    save_results_to_csv(results)
    plot_results(results)

