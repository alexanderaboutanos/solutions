# 238. Product of Array Except Self

**Difficulty:** Medium  
**Tags:** `array`, `prefix-sum`  
**LeetCode:** [product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self/)

## Solution

[solution.py](./solution.py)

## Approach

### Split "everything except me" into two halves

The product of every element except `nums[i]` is the product of everything *left* of `i` times the product of everything *right* of `i`. Neither half contains `nums[i]`, so the exclusion falls out of the decomposition for free, with no division anywhere.

The obvious approach, multiply everything then divide by `nums[i]`, is banned by the statement and would be wrong anyway: a single zero in the input turns the total product into `0`, and `0 / 0` is undefined for the one position whose answer should be the product of the rest.

### Prefix products, the running-sum trick with `*`

`left[i]` is a running product over `nums[:i]`. It is the same shape as the running sum in [#53](../0053-maximum-subarray) and the prefix-sum family generally: carry one accumulator, record it *before* folding in the current element, then fold. The pre-fold write is what makes `left[i]` exclusive of `nums[i]`.

```
nums  = [ 1,  2, 3, 4]
left  = [ 1,  1, 2, 6]    accumulator written, then multiplied
right = [24, 12, 4, 1]    same walk, right to left
ans   = [24, 12, 8, 6]    left[i] * right[i]
```

The empty product is `1`, so both accumulators start there. That is also why the ends come out right without special cases: `left[0]` is "the product of nothing," which is `1`.

### Zeros need no branch

With one zero at index `k`, every `left[i]` for `i > k` and every `right[i]` for `i < k` is `0`, so every position but `k` gets `0`, and position `k` gets the product of everything else. Two zeros push `0` into every slot. The decomposition handles it with no counting of zeros, which the division approach has to do by hand.

### What the first attempt got wrong

The first attempt is kept commented in `solution.py`. It built `right` in the correct order by walking `reversed(nums)` and calling `right.insert(0, ...)` each step. Inserting at the front of a Python list shifts every existing element one slot, so each insert is O(n) and the loop is O(n²): at the constraint's n = 10⁵ that is on the order of 10¹⁰ element moves, which times out.

The fix is to append in the order the walk produces and `reverse()` once at the end. A single reversal is O(n), and the overall pass stays linear. The general rule: never `insert(0, x)` in a loop; build backwards and flip, or index into a preallocated list.

### Unused loop variables

The draft used `enumerate` in both passes but never read the index, since `append` tracks position implicitly. Iterating the values directly, `for number in nums`, says exactly what the loop needs and nothing more.

### The follow-up: fold `right` into the answer

The three lists `left`, `right`, and `output` can collapse to one. Write the left pass straight into `answer`, then walk back from the end with a single running right-product and multiply it into `answer[i]` in place. The second pass never needs to *store* the right products, only the current one. That is O(1) extra space, with the output array excluded as the problem allows, and it is the trade an interviewer will ask for after the two-array version. It is kept commented at the bottom of `solution.py`.

## Complexity

| | Time | Space |
|---|---|---|
| Prefix and suffix arrays (this solution) | O(n) — three linear passes, one `reverse()` | O(n) — `left` and `right`, plus the output |
| Suffix folded into the output (follow-up) | O(n) — two passes | O(1) extra — one running accumulator |
| First attempt, `insert(0, ...)` | O(n²) — each insert shifts the list | O(n) |
| Division by `nums[i]` | O(n) | O(1) extra, but banned and breaks on zeros |

The two-array version is the one to reach for first because it makes the decomposition visible. The follow-up is the same algorithm with the storage squeezed out, not a different idea.
