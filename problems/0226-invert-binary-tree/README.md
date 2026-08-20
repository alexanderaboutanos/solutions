# 226. Invert Binary Tree

**Difficulty:** Easy  
**Tags:** `binary-tree`, `breadth-first-search`, `depth-first-search`, `tree`  
**LeetCode:** [invert-binary-tree](https://leetcode.com/problems/invert-binary-tree/)

## Solution

[solution.py](./solution.py)

## Approach

### What the problem does *not* guarantee

Two assumptions are easy to import from the examples and both are wrong.

The tree is **not complete**. *Complete* is a precise property — every level filled except possibly the last, which fills left-to-right — and it is what lets a heap live in a flat array with children at `2i+1` / `2i+2`. Nothing here promises it. A node may have one child, no children, or the whole tree may be a degenerate chain of depth *n*. Follow pointers; never compute positions.

The tree is **not sorted**. The headline example `[4,2,7,1,3,6,9]` happens to be a valid BST, which is incidental. `[1,3,2]` and `[1,1,1]` are equally legal. So there is no comparison-driven descent available and no way to prune — every node must be visited, which is what makes this O(n) rather than O(log n). Contrast with [#235](../0235-lowest-common-ancestor-of-a-binary-search-tree), where a BST *is* guaranteed and the entire trick is exploiting it.

A pleasant corollary: if the input does happen to be a BST, the inverted tree is ordered largest-to-smallest and is therefore *no longer* a BST. Inversion doesn't preserve the search property, it reverses it.

### Solution 1 — recursive DFS

The whole algorithm is one line of work — swap a node's two children — wrapped in a recursion that applies it everywhere.

The base case `if root is None: return None` does double duty, and that is the point. It absorbs the empty-tree input (`[]`, which the constraints allow) *and* it absorbs arriving at a missing child, so the recursive calls need no guards of their own. One check at the top replaces a check at every call site.

The swap must be **unconditional**. The tempting bug is:

```python
if root.left and root.right:   # wrong
```

which silently skips any node with exactly one child and leaves that subtree un-mirrored. Swapping a `None` into place is well-defined — you are moving an absence from one side to the other — so there is nothing to defend against.

Note the recursion here is driven by mutation rather than by return value: the calls modify nodes in place and their results are discarded. `root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)` folds the swap and the recursion into a single statement and is equally correct; the version here separates them because the swap is easier to see on its own line. The order of the two recursive calls is irrelevant — the subtrees are disjoint.

### Solution 2 — iterative BFS

Same swap, but a `deque` carries the frontier instead of the call stack. Pop a node, swap its children, push both children, repeat. The `if node:` check is the queue's equivalent of the base case — `None`s get enqueued freely and are discarded on the way out, which is cheaper than checking before every append.

Worth having because it removes the recursion depth entirely. At *n* ≤ 100 the recursive version is in no danger, but a degenerate chain makes stack depth equal to node count, and that is the first thing an interviewer raises the bound to probe.

### On the `null`s in the expected output

`invertTree` receives a `TreeNode` and returns a `TreeNode`. The bracketed lists are the judge's *serialization* — how it writes a tree down to print it — and nothing in the solution constructs or consumes them. There is no `null` handling to implement.

The wrinkle is worth understanding anyway, because it looks like a bug when the shapes are compared by eye. Level-order serialization is positional: the reader consumes two slots per node, left then right, so empty spots in the interior must be marked to keep later nodes aligned with the right parent. Given `[4,2,7,1,3]`:

```
      4                              4
     / \        invert              / \
    2   7       ------>            7   2
   / \                                / \
  1   3                              3   1
```

the input needed no interior `null`s — the populated node `2` came first at its level and consumed slots 4–5 naturally. After inverting, the leaf `7` is first at that level, so its two empty slots must be written out before `3` and `1` can reach node `2`: `[4,7,2,null,null,3,1]`. Same node count, longer serialization. Dropping those two placeholders yields `[4,7,2,3,1]`, which is a genuinely different tree — one where `3` and `1` hang off `7`.

The rule: trailing `null`s are trimmed, interior `null`s never are.

## Complexity

| | Time | Space |
|---|---|---|
| Solution 1 — recursive DFS | O(n) — every node visited once | O(h) call stack, degrading to O(n) on a degenerate chain |
| Solution 2 — iterative BFS | O(n) | O(w) for the queue, where *w* is the widest level — up to O(n/2) on a full tree |

Neither can do better than O(n) time: with no ordering to exploit, every node has to be reached.
