# 271. Encode and Decode Strings

**Difficulty:** Medium  
**Tags:** `array`, `string`, `design`  
**LeetCode:** [encode-and-decode-strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium; solved on [NeetCode's free version](https://neetcode.io/problems/string-encode-and-decode))

## Solution

[solution.py](./solution.py)

## Approach

### Lossless, unlike the key in #49

[#49](../0049-group-anagrams) also turned strings into a string, but that key was lossy on purpose: many words collapsed onto one key, and nothing ever had to be recovered from it. Here the mapping has to be **invertible**. `decode(encode(strs))` must return the exact list, including empty strings, and the words can contain any character. That last condition rules out the obvious answer. Any delimiter you pick, like `,` or `#`, can appear inside a word, and splitting on it would cut that word in two.

### Index up front, payload after

The fix is to never search the payload for anything. `encode` writes a header of cumulative **end offsets**, then a `#`, then every word concatenated with no separators:

```
["neet","code","love","you"]  ->  "4,8,12,15#neetcodeloveyou"
```

`decode` reads the header and slices the payload between consecutive offsets. It never examines a character inside a word, so the words' contents can't confuse it. This is how file formats with an index table work: the table says where each record lives, and the records themselves are opaque bytes.

### Why the first `#` is safe

The header is written by `encode` and contains only digits and commas, so the first `#` in the string has to be the terminator. Every `#` after it belongs to the payload, and `decode` never looks past the first one. The test `["a#b", ",", "12,3#", "#"]` encodes to `3,4,9,10#a#b,12,3##` and round-trips cleanly.

### Empty list vs. list of one empty string

These are the two inputs a careless encoding merges. `[]` has no offsets and encodes to `#`. `[""]` has one offset and encodes to `0#`. The `if header:` guard is what keeps them apart. `"".split(",")` returns `[""]` rather than `[]`, and without the guard `int("")` would raise.

### What the first draft got wrong

- **`str.append`.** Both the header and the payload were built with `.append` on a `str`. Python strings are immutable and have no `append`, so this raised `AttributeError`. Collecting the pieces in a list and joining them once is the idiomatic fix, and it avoids the risk of quadratic time from `+=` in a loop.
- **Two-character brackets.** The draft wrapped the header in `_[` … `]_`. The header's alphabet already makes a single terminator unambiguous, so the opening bracket did nothing and the closing one was twice as long as it needed to be.
- **Separate `startIdx` and `endIdx`.** One running total is enough.

The draft stopped before `decode`. The algorithm was sound, and the finished version keeps it.

### The standard alternative: prefix each word with its length

NeetCode's answer interleaves the index with the data: `"4#neet4#code4#love3#you"`. You read digits up to `#`, take that many characters, and repeat. Both designs are O(n) and rely on the same insight, that a length is safer than a delimiter. The difference is **locality**. The length prefix can be written and read as a stream, one word at a time. The header version has to know every length before it writes any of the payload, but it can find the *k*-th word straight from the header without reading the words before it.

The approach to avoid is a delimiter plus escaping, which means doubling every `#` inside a word, much like CSV quoting. It works, but it's the fragile version of the same idea.

## Complexity

| | Time | Space |
|---|---|---|
| Offset header, then payload (this solution) | O(n) encode and decode | O(n) for the output, plus O(m log n) header digits |
| Length prefix per word | O(n) encode and decode | O(n) for the output, plus O(m log n) prefix digits |
| Delimiter with escaping | O(n) encode and decode | O(n), up to 2× when every character needs escaping |

Here *n* is the total number of characters across all words and *m* is the number of words. Each offset is at most *n*, so it takes O(log n) digits to write. The header and the length prefix cost the same. Choosing between them is a matter of access pattern (streaming vs. random access), not asymptotics.
