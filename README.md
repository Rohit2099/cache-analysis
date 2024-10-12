# Computer Architecture: Cache Analysis

This repository contains solutions and experimental analysis of **cache memory performance**. The experiments focus on understanding the properties of cache memory such as block size, associativity, miss penalty, and TLB behavior. The analysis is based on the results obtained from running memory-intensive programs and interpreting cache behavior using graphs for a windows computer.

---

## Key Questions Addressed:

### 1. What is the overall size and block size of the second-level cache?

-   **Answer:** The size of the L2 cache was determined to be **2 MB**, and the block size was found to be **128 bytes** based on cache miss patterns and access time spikes in the graph.

### 2. What is the miss penalty of the second-level cache?

-   **Answer:** The miss penalty for the L2 cache is approximately **70 nanoseconds** as observed from access time when a miss occurs.

### 3. What is the associativity of the second-level cache?

-   **Answer:** The L2 cache was found to be **8-way set associative**, inferred from the graph by observing cache access times for strides larger than the cache size.

### 4. What is the size of the main memory?

-   **Answer:** The size of the main memory is estimated to be **greater than 256 MB**, although the exact size could not be conclusively determined from the graph.

### 5. What is the paging time if the page size is 4 KB?

-   **Answer:** The paging time and related details are analyzed based on the cache behavior and TLB access patterns.

### 6. Experimental Results Plot:

-   A plot was created with **elapsed time** on the y-axis and **memory stride** on the x-axis. **Logarithmic scales** were used for both axes, and a line was drawn for each cache size. This plot helps visualize cache and TLB performance characteristics.

---

## Additional Cache Insights:

### 1. What is the system page size?

-   **Answer:** Based on TLB miss behavior, the page size was determined to be **2 KB**.

### 2. How many entries are there in the TLB?

-   **Answer:** The **TLB** can reference **256 entries**, inferred from the graph where TLB misses start when cache size exceeds 2 MB.

### 3. What is the miss penalty for the TLB?

-   **Answer:** The TLB miss penalty is estimated to be **greater than 75 nanoseconds**, which is the time taken to access the main memory.

### 4. What is the associativity of the TLB?

-   **Answer:** The associativity of the TLB is explored based on observed memory access patterns and TLB miss behavior.

---

## How to Run the Experiments:

1. Clone this repository to your local machine.
2. Ensure that the necessary tools to measure cache performance and memory access times are installed (e.g., cache simulation software or benchmarking tools).
3. Run the programs provided to generate memory access patterns and analyze cache performance.
