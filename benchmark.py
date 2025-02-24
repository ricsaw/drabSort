import time
import random
import statistics
import matplotlib.pyplot as plt
import numpy as nppip
from tabulate import tabulate

def benchmark(sorting_algorithms, cases):
    results = {}
    
    for name, sort_func in sorting_algorithms.items():
        results[name] = []
        
        for case_name, arr in cases:
            arr_copy = arr.copy()
            start_time = time.perf_counter()
            sorted_arr = sort_func(arr_copy)
            end_time = time.perf_counter()

            assert sorted_arr == sorted(arr), f"{name} failed sorting!"

            time_taken = (end_time - start_time) * 1e6  # Convert to microseconds
            results[name].append((case_name, time_taken))

    return results

def generate_test_cases():
    """Generate a comprehensive set of test cases to evaluate sorting algorithms"""
    sizes = [10, 100, 1_000, 10_000, 100_000]  # Different input sizes
    cases = []
    
    for size in sizes:
        # Standard test cases
        cases.append((f"Random-{size}", [random.randint(-10**6, 10**6) for _ in range(size)]))
        cases.append((f"Sorted-{size}", list(range(size))))
        cases.append((f"Reverse-{size}", list(range(size, 0, -1))))
        cases.append((f"Duplicates-{size}", [42] * size))
        cases.append((f"Float-{size}", [random.uniform(-1000, 1000) for _ in range(size)]))
        
        # Advanced test cases
        if size >= 1000:
            # Small range of values (many duplicates)
            cases.append((f"SmallRange-{size}", [random.randint(0, 50) for _ in range(size)]))
            
            # Nearly sorted (95% in order)
            nearly_sorted = list(range(size))
            swaps = int(size * 0.05)
            for _ in range(swaps):
                i, j = random.sample(range(size), 2)
                nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]
            cases.append((f"NearlySorted-{size}", nearly_sorted))
            
            # Sawtooth pattern
            cases.append((f"Sawtooth-{size}", [i % 100 for i in range(size)]))
            
            # High number of duplicates with random distribution
            cases.append((f"FewUniques-{size}", [random.randint(1, 10) for _ in range(size)]))
            
            # Random at extremes (either very small or very large)
            extremes = []
            for _ in range(size):
                if random.random() < 0.5:
                    extremes.append(random.randint(-10**6, -10**5))
                else:
                    extremes.append(random.randint(10**5, 10**6))
            cases.append((f"Extremes-{size}", extremes))
            
            # Alternating high/low values
            alternating = []
            for i in range(size):
                if i % 2 == 0:
                    alternating.append(random.randint(0, 100))
                else:
                    alternating.append(random.randint(900, 1000))
            cases.append((f"Alternating-{size}", alternating))
            
    return cases

def analyze_results(results, cases):
    """Analyze and visualize benchmark results"""
    # Group results by algorithm
    algorithm_results = {}
    for name, data in results.items():
        algorithm_results[name] = {case_name: time for case_name, time in data}
    
    # Group by test case pattern and size
    pattern_results = {}
    size_results = {}
    
    for name, data in algorithm_results.items():
        # Process by pattern
        for case_name, time in data.items():
            pattern = case_name.split('-')[0]
            if pattern not in pattern_results:
                pattern_results[pattern] = {}
            if name not in pattern_results[pattern]:
                pattern_results[pattern][name] = []
            pattern_results[pattern][name].append(time)
        
        # Process by size
        for case_name, time in data.items():
            size = int(case_name.split('-')[1])
            if size not in size_results:
                size_results[size] = {}
            if name not in size_results[size]:
                size_results[size][name] = []
            size_results[size][name].append(time)
    
    return algorithm_results, pattern_results, size_results

def generate_visualizations(algorithm_results, pattern_results, size_results):
    """Generate performance visualization plots"""
    # Configure the plots
    plt.figure(figsize=(15, 10))
    
    # 1. Overall performance comparison
    plt.subplot(2, 2, 1)
    algorithm_names = list(algorithm_results.keys())
    avg_times = [statistics.median(list(algorithm_results[name].values())) for name in algorithm_names]
    plt.barh(algorithm_names, avg_times)
    plt.xscale('log')
    plt.title('Median Performance Across All Test Cases')
    plt.xlabel('Time (microseconds, log scale)')
    
    # 2. Performance by data size
    plt.subplot(2, 2, 2)
    sizes = sorted(size_results.keys())
    for name in algorithm_results:
        medians = [statistics.median(size_results[size][name]) for size in sizes]
        plt.plot(sizes, medians, marker='o', label=name)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Scaling Performance by Data Size')
    plt.xlabel('Data Size (log scale)')
    plt.ylabel('Time (microseconds, log scale)')
    plt.legend()
    
    # 3. Performance by pattern type
    plt.subplot(2, 2, 3)
    patterns = sorted(pattern_results.keys())
    data = []
    for name in algorithm_results:
        row = [name]
        for pattern in patterns:
            if name in pattern_results[pattern]:
                row.append(statistics.median(pattern_results[pattern][name]))
            else:
                row.append(0)
        data.append(row)
    
    # Create a heatmap-style visualization
    cell_text = []
    for row in data:
        cell_text.append([row[0]] + [f"{val:.2f}" for val in row[1:]])
    
    plt.table(cellText=cell_text, 
              colLabels=['Algorithm'] + patterns,
              loc='center')
    plt.axis('off')
    plt.title('Median Performance by Pattern Type (microseconds)')
    
    # 4. Best algorithm for each pattern
    plt.subplot(2, 2, 4)
    best_algorithms = {}
    for pattern in patterns:
        best_time = float('inf')
        best_alg = None
        for name in algorithm_results:
            if name in pattern_results[pattern]:
                time = statistics.median(pattern_results[pattern][name])
                if time < best_time:
                    best_time = time
                    best_alg = name
        best_algorithms[pattern] = (best_alg, best_time)
    
    plt.bar(patterns, [time for _, time in best_algorithms.values()])
    plt.yscale('log')
    plt.xticks(rotation=45)
    plt.title('Best Algorithm Performance by Pattern')
    plt.ylabel('Time (microseconds, log scale)')
    
    # Add labels for the best algorithm names
    for i, pattern in enumerate(patterns):
        alg, time = best_algorithms[pattern]
        plt.text(i, time, alg, ha='center', va='bottom', rotation=90, fontsize=8)
    
    plt.tight_layout()
    plt.savefig('sorting_performance.png')
    return 'sorting_performance.png'

def print_detailed_results(results, cases):
    """Print detailed benchmark results in a readable format"""
    # Calculate average time for each algorithm
    case_names = [name for name, _ in cases]
    algorithm_names = list(results.keys())
    
    # Create a table with all results
    table_data = []
    for name in algorithm_names:
        row = [name]
        for i, (case_name, _) in enumerate(cases):
            row.append(f"{results[name][i][1]:.2f}")
        table_data.append(row)
    
    print("\n--- Detailed Performance Results (microseconds) ---")
    print(tabulate(table_data, headers=["Algorithm"] + [name for name, _ in cases]))
    
    # Calculate average time for each algorithm
    avg_times = {}
    for name in algorithm_names:
        avg_times[name] = sum(time for _, time in results[name]) / len(results[name])
    
    # Sort algorithms by speed (ascending order)
    sorted_algorithms = sorted(avg_times.items(), key=lambda x: x[1])
    
    # Print rankings
    print("\n--- Algorithm Rankings (Fastest to Slowest) ---")
    for rank, (name, avg_time) in enumerate(sorted_algorithms, start=1):
        print(f"{rank}. {name} - {avg_time:.2f} µs (Avg)")
    
    # Best algorithm for each case size
    print("\n--- Best Algorithm by Input Size ---")
    size_categories = sorted(set(int(name.split('-')[1]) for name, _ in cases))
    
    for size in size_categories:
        relevant_cases = [(i, case) for i, case in enumerate(cases) if int(case[0].split('-')[1]) == size]
        best_alg = None
        best_time = float('inf')
        
        for name in algorithm_names:
            times = [results[name][i][1] for i, _ in relevant_cases]
            avg_time = sum(times) / len(times)
            if avg_time < best_time:
                best_time = avg_time
                best_alg = name
        
        print(f"Size {size}: {best_alg} ({best_time:.2f} µs)")
    
    # Best algorithm for each pattern type
    print("\n--- Best Algorithm by Pattern Type ---")
    pattern_types = sorted(set(name.split('-')[0] for name, _ in cases))
    
    for pattern in pattern_types:
        relevant_cases = [(i, case) for i, case in enumerate(cases) if case[0].startswith(pattern)]
        best_alg = None
        best_time = float('inf')
        
        for name in algorithm_names:
            times = [results[name][i][1] for i, _ in relevant_cases]
            avg_time = sum(times) / len(times)
            if avg_time < best_time:
                best_time = avg_time
                best_alg = name
        
        print(f"{pattern}: {best_alg} ({best_time:.2f} µs)")

def main():
    # Create sorting algorithm dictionary
    from comparison import drab_sort, quick_sort, merge_sort, heap_sort
    
    sorting_algorithms = {
        "DrabSort": drab_sort,
        "Timsort": sorted,
        "QuickSort": quick_sort,
        "MergeSort": merge_sort,
        "HeapSort": heap_sort
    }
    
    # Generate test cases
    print("Generating test cases...")
    cases = generate_test_cases()
    print(f"Created {len(cases)} test cases across various patterns and sizes")
    
    # Run benchmarks
    print("Running benchmarks (this may take a while)...")
    results = benchmark(sorting_algorithms, cases)
    print("Benchmarks complete!")
    
    # Analyze results
    algorithm_results, pattern_results, size_results = analyze_results(results, cases)
    
    # Print detailed results
    try:
        print_detailed_results(results, cases)
    except ImportError:
        print("Could not import tabulate. Install with 'pip install tabulate' for better formatting.")
        # Fall back to simple formatting
        for name, timings in results.items():
            print(f"\n{name} Performance:")
            for (case_name, time) in timings:
                print(f"  {case_name}: {time:.2f} µs")
    
    # Generate visualizations if matplotlib is available
    try:
        chart_file = generate_visualizations(algorithm_results, pattern_results, size_results)
        print(f"Performance visualization saved as '{chart_file}'")
    except ImportError:
        print("Could not generate visualizations. Install matplotlib with 'pip install matplotlib'")
    
    print("\nBenchmark complete. Check the results to see which algorithm performs best for your data patterns.")

if __name__ == "__main__":
    main()