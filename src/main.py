import matplotlib.pyplot as plt
from utilities import generate_random_integers, measure_runtime, save_to_file
from no_privacy_computation import compute_average_without_privacy
from paillier import compute_average_with_paillier
from shamir_secret_sharing import compute_average_with_shamir
from differential_privacy import differentially_private_average

if __name__ == "__main__":
    # List of different values of n
    n_values = [5, 10, 20, 50, 100]  

    # Lists to store runtimes for plotting
    runtimes_without_privacy = []
    runtimes_with_paillier = []
    runtimes_with_shamir = []
    runtimes_with_dp = []
    # Lists to store accuracy for plotting
    accuracies_without_privacy = []
    accuracies_with_paillier = []
    accuracies_with_shamir = []
    accuracies_with_dp = []
    accuracies = []  # List to store accuracy results
    runtime_results = ""

    for n in n_values:
        print(f"Running computations for n = {n}")
        print("-----------------------")

        # Generate random data
        data = generate_random_integers(n)
        save_to_file(data, f"data/random_integers_{n}.txt")
        
        # True average
        true_average = sum(data) / len(data)
        
        # Compute average without privacy
        average_np, runtime = measure_runtime(compute_average_without_privacy)(data)
        runtimes_without_privacy.append(runtime)
        accuracies.append(abs(true_average - average_np))
        
        # Compute with paillier 
        average_p, runtime = measure_runtime(compute_average_with_paillier)(data)
        runtimes_with_paillier.append(runtime)
        accuracies.append(abs(true_average - average_p))

        # Compute with shamir 
        average_s, runtime = measure_runtime(compute_average_with_shamir)(data)
        runtimes_with_shamir.append(runtime)
        accuracies.append(abs(true_average - average_s))

        # Compute with differential privacy
        average_dp, runtime = measure_runtime(differentially_private_average)(data)
        runtimes_with_dp.append(runtime)
        accuracies.append(abs(true_average - average_dp))

        # Append the runtime and accuracy results to the string
        runtime_results += f"n = {n}\n"
        runtime_results += f"Runtime without privacy: {runtimes_without_privacy[-1]} seconds, Accuracy: {accuracies[0]}\n"
        runtime_results += f"Runtime with Paillier: {runtimes_with_paillier[-1]} seconds, Accuracy: {accuracies[1]}\n"
        runtime_results += f"Runtime with Shamir: {runtimes_with_shamir[-1]} seconds, Accuracy: {accuracies[2]}\n"
        runtime_results += f"Runtime with Differential Privacy: {runtimes_with_dp[-1]} seconds, Accuracy: {accuracies[3]}\n"
        runtime_results += "-----------------------\n"
        accuracies.clear()  # Clear the accuracies list for the next iteration

    with open("results/runtime_results.txt", "w") as file:
        file.write(runtime_results)
    
    # Plotting the results
    plt.figure(figsize=(10, 6))

    plt.plot(n_values, runtimes_without_privacy, marker='o', label='Without Privacy')
    plt.plot(n_values, runtimes_with_paillier, marker='o', label='With Paillier')
    plt.plot(n_values, runtimes_with_shamir, marker='o', label='With Shamir')
    plt.plot(n_values, runtimes_with_dp, marker='o', label='With Differential Privacy')
    
    plt.xlabel('Number of Integers (n)')
    plt.ylabel('Runtime (seconds)')
    plt.yscale('log')  # Setting y-axis to logarithmic scale
    plt.title('Comparison of Runtimes')
    plt.legend()
    plt.grid(True, which="both", ls="--", c='0.7')  # Adjusting grid for log scale
    plt.tight_layout()
    plt.savefig('results/graphs/comparison_graph.png')