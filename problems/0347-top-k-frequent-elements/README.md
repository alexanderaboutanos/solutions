# 347. Top K Frequent Elements

**Difficulty:** Medium  
**Tags:** `array`, `hash-table`, `divide-and-conquer`, `sorting`, `heap-priority-queue`, `bucket-sort`, `counting`, `quickselect`  
**LeetCode:** [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/)

## Solution

[solution.py](./solution.py)

## Approach

### Count first, the table from #242

The first half is the frequency dict from [#242](../0242-valid-anagram), built by the same `if num not in counts: = 1 else: += 1` idiom. In #242 the table was the answer, compared whole with `==`. Here it is only an intermediate: the question is which keys have the largest values, which is a ranking problem layered on top of a counting one.

### Rank by sorting the keys on their counts

`sorted(counts, key=counts.get, reverse=True)` does the ranking in one line. Iterating a dict yields its keys, so the sort orders the distinct numbers themselves, and `key=counts.get` makes each number compare by its count rather than its own value. `reverse=True` puts the most frequent first, and `[:k]` takes the answer.

Ties are harmless. The constraints guarantee a unique answer, so no tie can straddle the cutoff at *k*, and within the top *k* the order doesn't matter.

### What the first draft got wrong

- **`if not counts[num]:`** tested for a missing key by reading it. Indexing a dict with an absent key raises `KeyError`; it doesn't return something falsy. The membership test `num not in counts` (or `counts.get(num, 0) + 1`) is the fix.
- **`key=count.get`** referred to a name that didn't exist, a `NameError` from the variable being called `counts`.

### Why the follow-up rejects this

The problem's follow-up demands better than O(n log n), and this solution is exactly O(n log n) in the worst case, when every number is distinct and the sort sees all *n* keys. It passes the tests, but it is the answer an interviewer asks you to improve. Two standard improvements:

- **Min-heap of size *k*** (`heapq.nlargest(k, counts, key=counts.get)`): O(n log k). It never holds more than *k* candidates, so it wins when *k* is small. It is the general tool, and it returns in the Heap / Priority Queue section ([#973](../0973-k-closest-points-to-origin) uses one).
- **Bucket sort by count**: O(n). A count is an integer between 1 and *n*, so it can index an array directly. Build `n + 1` empty lists, append each number to the slot for its count, then walk the slots from the top down until *k* numbers are collected. Placement *is* the sort, with no comparisons at all. The trick works only because the sort key is a small bounded integer; distances in #973 have no such bound, which is why that problem needs the heap.

## Complexity

| | Time | Space |
|---|---|---|
| Count, then sort keys by count (this solution) | O(n + u log u), which is O(n log n) when every number is distinct | O(u) for the counts and the sorted list |
| Count, then min-heap of size *k* | O(n + u log k) | O(u + k) |
| Count, then bucket by count | O(n) | O(n) for the `n + 1` buckets |

Here *n* is `len(nums)` and *u* is the number of distinct values, at most *n*. Counting is O(n) in every row; the approaches differ only in how they rank the *u* counted keys.
