# 49. Group Anagrams

**Difficulty:** Medium  
**Tags:** `array`, `hash-table`, `sorting`, `string`  
**LeetCode:** [group-anagrams](https://leetcode.com/problems/group-anagrams/)

## Solution

[solution.py](./solution.py)

## Approach

### The frequency table from #242, applied n times

[#242](../0242-valid-anagram) settled what "anagram" means: two words have the same letter counts. That solution built a frequency dict for each word and compared the two with `==`. This problem asks the same question of every pair of words at once, so each word gets the same hand-rolled dict, and two words share a group exactly when their dicts are equal.

### Groups found by scanning

The groups live in two parallel lists. `listOfDictionaries` holds one representative table per group, and `finalOutputList` holds that group's words at the **same index**. For each word, the loop walks the representatives until one compares equal. On a match it appends the word to the group at that index and `break`s. If nothing matches, the word starts a new group, and both lists grow together so the index alignment holds.

The scan exists because a dict can't be a dict key. It's mutable, so it isn't hashable, and the table that identifies a group can't be used to *look up* that group. Scanning with `==` works around that, and it costs one comparison per existing group for every word.

### What the first draft got wrong

The draft reviewed before this one had three bugs, and each is worth naming:

- **`[newDict]` instead of `newDict`.** Wrapping the table in a list made every `dictionary == newDict` compare a list to a dict, which is never equal. Every word landed in its own group.
- **A special case for the first word.** It seeded both lists when they were empty, then the general loop ran anyway and added the first word a second time. An empty `listOfDictionaries` already falls through to "no match, start a group", so the empty case needed no branch. This is the same lesson as the length-1 input in [#217](../0217-contains-duplicate).
- **`boolean foundMatch = False`**, a Java-style declaration and a syntax error in Python.

### Accepted, but quadratic

When every word is its own group, word *i* is compared against *i* groups, which totals about n²/2 comparisons. The constraints allow 10⁴ words of length 100. With no two of them anagrams, that is 5×10⁷ dict comparisons, and this solution took 8.4 s locally against 0.14 s for the hashed version. LeetCode accepts it because dict `==` runs in C and stops at the first differing key, and because its test data doesn't hit that adversarial case. An interviewer judges against the constraints, not the test suite, so this is the part they would push on.

### What hashing would change

The fix is to **freeze the table into something hashable** and key a map with it. #242's write-up anticipated this step. Two standard keys:

- `"".join(sorted(s))`: the sorted string. It's simple and costs O(k log k) per word.
- `tuple(count)` over a `[0] * 26` array: O(k) per word, and the optimal answer. The fixed 26-slot array is safe here because the constraints promise lowercase English letters, which is the special case #242's Unicode follow-up warned about.

Then `groups[key].append(s)` into a `defaultdict(list)` and `return list(groups.values())`. The scan disappears, each word costs one O(1) average lookup, and the two parallel lists collapse into one map. There is no index invariant left to maintain.

## Complexity

| | Time | Space |
|---|---|---|
| Linear scan over group representatives (this solution) | O(n·k + n·g), which is O(n²) when every word is its own group | O(n·k) for the output, plus one table per group |
| Hashmap keyed by sorted string | O(n·k log k) | O(n·k) |
| Hashmap keyed by 26-count tuple | O(n·k) | O(n·k) |

Here *n* is the number of words, *k* is the maximum word length, and *g* is the number of groups. Each dict comparison is bounded by the 26-letter alphabet, so it is O(1). The scan's cost depends on *g*: near-linear when most words share a few groups, quadratic when none do. The hashed versions make it independent of the input's shape, which is the point of the problem.
