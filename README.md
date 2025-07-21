# Understanding Algorithm Efficiency and Scalability
This is a repository containing my third assignment for MSCS532. This is a Python implementation of Randomized Quicksort, Deterministic Quicksort, and Hashing with Chaining.

## Project Overview
This assignment was designed to show understanding of how algorithms perform under different conditions. It included an analysis of the efficiency and scalability of Quicksort and Hashing with Chaining. The project aimed to show the development of skills necessary to provide an evaluation of algorithm performance, efficiency in practical implementation, and a showcase of how to make informed decisions on algorithm selection based on theoretical and empirical analysis.

### Part 1: Quicksort Analysis
This part of the implementation focused on the implementation of the Randomized Quicksort algorithm and provided an empirical comparison against the Deterministic Quicksort algorithm.

### Part 2: Hashing with Chaining
This part of the implementation focused on the implementation of a hash table using chaining for collision resolution.

### Project Deliverables:
```RandomizedQuicksort.py``` : Python file containing implementation of Randomized Quicksort with various edge and use cases such as repeated elements, empty arrays, and already sorted arrays.

```DeterministicQuicksort.py``` : Python file containing implementation of Deterministic Quicksort using the first element of an array. The script contains the comparison logic and prints running times for both the deterministic and randomized Quicksort.

```HashingwChaining.py``` : Python file containing a hash table using chaining for collision resolution and some use cases.

```Analysis Report.md``` : Report containing analysis of average case time complexity for Randomized Quicksort and analysis of how load factor affects performance of search, insert, delete within a hash table, as well as strategies for maintaining a low load factor.

## Summary of Findings
The empirical tests and theoretical analysis completed within this project provided clear insights into the efficiency and scalability of Randomized Quicksort and Hashing with Chaining. It was shown in the following key features:
-	Randomized Quicksort Comparison Analysis: The comparison between Randomized and Deterministic Quicksort demonstrates the power of randomization. Randomized Quicksort maintained its expected <em>O(n log n)</em> performance efficiency across all tested generated arrays. Whereas Deterministic Quicksort’s performance degrades to <em>O(n2)</em>  performance on inputs that are already sorted, reverse sorted, or have repeated elements. This confirms that randomization effectively mitigates the risk of worst-case pivot selections and makes it reliable regardless of initial data order.

-	Hashing with Chaining Performance Analysis: The hashing with chaining implementation highlighted the average-case performance of hash tables. Operations like insert, search, and delete steadily performed in <em> O(1) </em>  time for the tested scenarios. The analysis highlights that while hash tables are fast, their performance is directly tied to the load factor (<em>α</em>). As <em>α</em> increases, the average chain length grows. It causes the operations’ performance to downgrade towards <em>O(n)</em> in the worst case. Maintaining a low load factor through strategies like dynamic resizing and the usage of prime numbers for table capacity is crucial for preserving the hash table's <em> O(1) </em>  amortized average-case performance and minimizing collisions.
These findings underscore that effective algorithm selection and implementation require a blend of theoretical understanding and empirical support.

### How to Run Code
* Clone the repository or save all Python files into a folder.
* Open terminal or preferred IDE.
* Navigate and open the save file.
* Run the scripts using a Python interpreter.




