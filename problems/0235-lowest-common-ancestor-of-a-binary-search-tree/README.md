# 235. Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** Easy  
**Tags:** `binary-search-tree`, `binary-tree`, `depth-first-search`, `tree`  
**LeetCode:** [lowest-common-ancestor-of-a-binary-search-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Solution

[solution.py](./solution.py)

## Approach

### The guarantee is the whole problem

This is a **BST**, and the constraints say so. That single word is what separates this from [#236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/), its sibling problem on an unordered binary tree, which is rated Medium and needs an O(n) post-order search of *both* subtrees at every node because nothing tells you which way the targets lie.

Here the ordering tells you. At any node, every value in the left subtree is smaller and every value in the right subtree is larger, so comparing `p` and `q` against the current node discards an entire subtree per step. Contrast [#226](../0226-invert-binary-tree), where the absence of any ordering means every node must be touched — the two problems sit on opposite sides of the same distinction, and it is always the first thing to establish when reading a tree problem.

### Characterizing the answer

Walk down from the root. As long as `p` and `q` are both on the same side, the LCA is further down that side — the current node has one of them buried in a subtree that doesn't contain the other, so it can't be the common ancestor of both. The moment they stop agreeing, you have arrived.

So: **the LCA is the first node where the two search paths diverge**, which is the same as saying the first node whose value falls in the closed interval between `p.val` and `q.val`.

That gives the three-way branch directly:

| Condition | Meaning |
|---|---|
| both values greater than `node.val` | both live right — descend right |
| both values less than `node.val` | both live left — descend left |
| anything else | the paths part here — `node` is the LCA |

### The `else` absorbs three cases, not one

Worth naming them, because collapsing them is what keeps the code to three branches:

1. **A genuine split** — `p.val < node.val < q.val` or the reverse. The paths diverge at this node.
2. **`node` is `p`** — `p` is an ancestor of `q`, and the problem's definition explicitly allows a node to be a descendant of itself.
3. **`node` is `q`** — symmetric.

Cases 2 and 3 are what Example 2 exists to test. A version that treated equality as "keep going" would descend straight past the answer and return something below it.

On the sample tree:

```
            6
          /   \
         2     8
        / \   / \
       0   4 7   9
          / \
         3   5
```

`p=2, q=8` — at 6 they sit on opposite sides, so 6 is the answer immediately.
`p=2, q=4` — at 6 both are smaller, descend left to 2; now `node` *is* `p`, so 2 is the answer. One comparison decides each level.

### Why the swap isn't needed

The first attempt is kept commented at the bottom of `solution.py`. It normalizes `p` and `q` so the smaller comes first, then loops while `root.val` sits outside the pair, with a separate equality check inside for the self-ancestor case.

It works, but the ordering step is doing nothing. `p.val > node.val and q.val > node.val` is **symmetric in `p` and `q`** — a conjunction doesn't care which operand is larger, it only holds when both agree on direction. Testing both against the same side rather than testing the node against an ordered interval removes the swap and the extra equality check together.

One correction to the note preserved in that old attempt: it blames the swap on the tree, claiming "the left node might be LARGER than the right node." In a BST that cannot happen — `left < node < right` is the defining invariant, and this problem guarantees it. The actual reason a swap seemed necessary is unrelated to the tree: **`p` and `q` are handed to you in arbitrary order relative to each other**, and the interval test `p.val < root.val < q.val` is the thing that's order-sensitive. Fix the test instead of the inputs.

### Iterative rather than recursive

The natural recursion here is **tail recursive** — the recursive call's result is returned unchanged, with no work left to do on the way back up. That makes the conversion to a `while` loop mechanical, and since CPython doesn't eliminate tail calls, it's a real saving rather than a cosmetic one.

It also matters at this problem's stated size. The constraints allow 10⁵ nodes and promise nothing about balance, so a degenerate chain is legal — that's 10⁵ stack frames against CPython's default recursion limit of 1000. The recursive version doesn't merely use more memory on the worst case; it raises `RecursionError`. Descending in a loop is the version that survives.

### The unreachable `return None`

The loop exits only by falling off the bottom of the tree, and the constraints guarantee both `p` and `q` are present with `p != q`. Under those preconditions the descent always terminates on an LCA — worst case the root itself — so `while node` can never actually run out. The trailing `return None` is there so every path returns a value, and as a defined behaviour if the precondition is ever violated.

## Complexity

| | Time | Space |
|---|---|---|
| Iterative descent | O(h) — one comparison per level | O(1) — two pointers, no stack |

Where *h* is the height: O(log n) on a balanced tree, degrading to O(n) on a degenerate chain, which the constraints permit. The recursive form is identical in time but O(h) in space.

The sub-linear time is bought entirely by the BST guarantee. [#236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/), the same question without ordering, is O(n) time and O(h) space — it has to look everywhere.
