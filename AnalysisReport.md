# <center> Analysis Report </center>
### <center> by Alexa Fisher </center>
<br>

 This report outlines the analysis for randomized quicksort algorithms and hashing with chaining. The analysis includes the average-case time complexity for randomized quicksort and a comparison of differences between deterministic and randomized quicksort algorithms. The report provides a robust explanation of randomized quicksort algorithm’s average-case time complexity and its reason for being <em>O</em>(<em>n</em> log <em>n</em>) with the use of concepts such as recurrence relations. The latter sections of the report include an analysis of hashing with chaining and how low factor affects the performance of insert, search, and delete operations. In addition to the performance analysis, the report includes various strategies for maintaining a low load factor and minimizing collisions.

## <center> Randomized Quick Sort Analysis </center>
### Average-Case Time Complexity

Randomized quicksort is highly efficient due to its average-case time complexity. The average-case time complexity was proven to be <em>O</em>(<em>n</em> log <em>n</em>). This efficiency was due to its approach to its pivot selection. The randomization ensures that the selection of a poor pivot choices are lowered and unlikely. The recurrence relation of average-case time complexity can provide an adequate explanation. The Figure 1 provides a detailed explanation.
<br>
<strong>Figure 1
<br>
Recurrence Relation Randomized Quicksort
<br>
</strong>
<br>
![recurrence relation](https://github.com/alexaryanfisher/MSCS532_Assignment3/blob/main/images/recurrencerelation.png))

This simplified form often reflects the balanced split scenario that randomized quicksort achieves on average which mimics the behavior of the balanced divide-and-conquer algorithm that results in <em>O(n log n)</em> based on the Master Theorem (Cormen et al., 2022).


### Comparison

The empirical comparison between deterministic quick sort via the first element and randomized quicksort showcases their practical differences. The randomly generated arrays both show similar <em>O(n log n)</em> behavior with similar execution times. However, there are noticeable differences between the already sorted, reversed-sorted, and repeated elements array.

In these use cases, the deterministic quick sort’s performance lessens to <em>O(n2)</em> time complexity. The deterministic quicksort is using the first element as the pivot, which leads to unbalanced partitions. One of the subarrays would be a size <em>(n – 1)</em> and the other would be size 0. This imbalance would result in a linear chain of recursive calls. A visualization of this is found in Figure 2.
<br>
<strong>Figure 2
<br>
Deterministic Quicksort, Recursive Tree Visualization
</strong>
<br>
![deterministic recursive tree](https://github.com/alexaryanfisher/MSCS532_Assignment3/blob/main/images/deterministic.png)

This linear chain translates into a large increase in execution time. This is especially prominent in larger input arrays. On the other hand, randomized quicksort maintains its <em>O(n log n)</em> performance regardless of the varying inputs.

## <center> Hashing with Chaining Analysis </center>
### Performance
In hashing with chaining, the load factor is a critical determinant of performance for search, insert, and delete operations. Under the assumption of simple uniform hashing, the expected length of a chain is the load factor. The expected time for the operations is <em>O</em>(1 + <em>α</em>), where <em>α</em> is the load factor. As the load factor <em>α</em> increases, the average chain length also increases. The increase causes the operations to approach <em>O(n)</em> time complexity, which decreases the performance.
### Strategies
Dynamic resizing of the hash table is a crucial strategy for maintaining a low load factor and minimizing collisions. When a load factor exceeds the predefined threshold, the hash table is resized to a larger capacity, which increases the number of buckets. All the existing key value pairings are re-hashed and re-inserted into the new larger table. Although the re-hashing operation does take  <em>O(n)</em> time complexity, the process occurs so infrequently keeping the time complexity at <em>O(1)</em> (Jung, 2024).

Another strategy includes choosing a prime number for the table capacity to improve the hash distribution. This is a direct result of the behavior of the modulo operator (Bhullar et al., 2016). In a hash table, a key is mapped to a bucket index using the modulo operation. Using a prime number ensures that it shares no common factors with the hash values. It helps the hash values to spread out more evenly across the available buckets
## <center> References </center>
Bhullar, R. K., Pawar, L. , and Kumar, V. (2016). A novel prime numbers based hashing technique for minimizing collisions.<em> 2016 2nd International Conference on Next Generation Computing Technologies (NGCT),</em> pp. 522-527, doi: 10.1109/NGCT.2016.7877471

Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. (2022). Introduction to Algorithms, 4th edition. Cambridge. The MIT Press.

Jung, Terrence.(2024 August 16). Hash Tables 1010: Collisions, Resizing, Hashing. Dev. https://dev.to/jihoonj/implementing-a-hash-table-3pa7

