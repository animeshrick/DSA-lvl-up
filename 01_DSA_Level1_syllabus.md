# DSA Level-1 Syllabus — Python (Service/IT Coding Rounds)

**Scope:** Everything that actually shows up in TCS/Infosys/Wipro/Accenture/Cognizant coding rounds.
**Duration:** ~4 weeks at 2–3 hrs/day. **Day 1 = June 21, 2026.**
**Rule:** Learn concept → dry-run on paper → code in Python → log it in the tracker.

> Each topic lists problems in increasing difficulty. Start from the top of Week 1.
> ✅ = must-do (very common in service coding rounds).

---

## Week 1 — Basics, Math & Patterns (the bread-and-butter of coding rounds)

### Day 1 — Time/Space Complexity + I/O warm-up  ⬅️ START HERE
Concept: Big-O intuition (O(1), O(n), O(n²), O(log n)). How to read input/print output in Python for online judges (`input()`, `int(input())`, `map(int, input().split())`).
Problems:
1. ✅ Sum of first N natural numbers (loop vs formula — compare complexity)
2. ✅ Reverse a number (e.g., 1234 → 4321)
3. ✅ Count digits in a number
4. Find max & min in a list

### Day 2 — Number Theory I  ✅ (HIGH-yield for coding rounds)
Concept: modulo, divisibility.
Problems:
1. ✅ Check prime number
2. ✅ Print all primes up to N
3. ✅ Factorial of N (loop + recursion)
4. ✅ Check Armstrong number
5. ✅ Check palindrome number

### Day 3 — Number Theory II
Problems:
1. ✅ GCD / HCF (Euclidean algorithm)
2. LCM of two numbers
3. ✅ Fibonacci series up to N (loop + recursion)
4. Sum of digits / digital root
5. Count number of factors of N

### Day 4 — Pattern Printing  ✅ (asked constantly)
Concept: nested loops.
Problems:
1. ✅ Right-angled triangle of stars
2. ✅ Inverted triangle
3. ✅ Pyramid pattern
4. ✅ Floyd's triangle (numbers)
5. ✅ Pascal's triangle
6. Hollow square / diamond

### Day 5 — Arrays I  ✅
Concept: Python lists, indexing, traversal.
Problems:
1. ✅ Reverse an array
2. ✅ Find largest/smallest element
3. ✅ Sum & average of array
4. ✅ Count even/odd elements
5. Second largest element

### Day 6 — Arrays II
Problems:
1. ✅ Linear search
2. Move all zeros to end
3. ✅ Find duplicates in array
4. Rotate array by k positions
5. Find missing number (1..N)

### Day 7 — Revision + mini-test
Re-solve 5 problems you flagged. Then a 45-min timed set: 1 pattern + 1 number-theory + 1 array problem. Log score.

---

## Week 2 — Strings, Searching & Sorting

### Day 8 — Strings I  ✅
Concept: Python string methods, slicing, immutability.
Problems:
1. ✅ Reverse a string (`s[::-1]` + manual)
2. ✅ Check palindrome string
3. ✅ Count vowels and consonants
4. Count words in a sentence
5. Toggle case

### Day 9 — Strings II  ✅
Problems:
1. ✅ Check anagram (two strings)
2. ✅ Find duplicate characters
3. First non-repeating character
4. Remove duplicates from string
5. Count character frequency

### Day 10 — Strings III
Problems:
1. Reverse words in a sentence
2. Check if two strings are rotations
3. Longest word in a sentence
4. Capitalize first letter of each word
5. String compression (aaabb → a3b2)

### Day 11 — Binary Search  ✅
Concept: sorted array, divide & conquer, mid calculation.
Problems:
1. ✅ Binary search (iterative)
2. Binary search (recursive)
3. First/last occurrence of element
4. Square root of N (integer)
5. Find element in rotated sorted array (stretch)

### Day 12 — Sorting Basics
Concept: understand, don't memorize. Know complexities.
Problems (implement each once):
1. ✅ Bubble sort
2. Selection sort
3. Insertion sort
4. Know that Python's `sorted()` is O(n log n) — use it in real problems

### Day 13 — Sorting Applications
Problems:
1. ✅ Sort array of 0s, 1s, 2s
2. Merge two sorted arrays
3. Kth smallest/largest element
4. Check if array is sorted
5. Sort by frequency

### Day 14 — Revision + timed test
Re-solve flagged problems. 45-min timed: 1 string + 1 search + 1 sort.

---

## Week 3 — Hashing, Two Pointers & Recursion

### Day 15 — Hashing (dict/set)  ✅
Concept: Python `dict` and `set`, O(1) lookups.
Problems:
1. ✅ Two Sum
2. ✅ Frequency count of elements
3. Find pair with given sum
4. Find majority element
5. Longest consecutive sequence (stretch)

### Day 16 — Two Pointers
Problems:
1. ✅ Pair sum in sorted array
2. Remove duplicates from sorted array
3. Reverse array using two pointers
4. Container with most water (stretch)

### Day 17 — Sliding Window (intro)
Problems:
1. Max sum subarray of size k
2. First negative in every window of size k
3. Longest substring without repeating characters (stretch)

### Day 18 — Recursion I  ✅
Concept: base case, recursive case, call stack.
Problems:
1. ✅ Factorial (recursive)
2. ✅ Fibonacci (recursive)
3. Sum of digits (recursive)
4. Power of a number (x^n)
5. Reverse a string recursively

### Day 19 — Recursion II
Problems:
1. Print 1 to N / N to 1 recursively
2. Check palindrome recursively
3. Tower of Hanoi
4. Sum of array elements recursively

### Day 20 — Basic Backtracking (intro)
Problems:
1. Generate all subsets of a set
2. Generate all permutations of a string
3. (Stretch) N-Queens — read, don't stress

### Day 21 — Revision + timed test
Re-solve flagged. 45-min timed: 1 hashing + 1 recursion + 1 two-pointer.

---

## Week 4 — Linked Lists, Stacks/Queues & Full Revision

### Day 22 — Linked List I  ✅
Concept: nodes, pointers, traversal in Python (class Node).
Problems:
1. ✅ Create & traverse singly linked list
2. Insert at beginning/end
3. ✅ Reverse a linked list
4. Find middle of linked list

### Day 23 — Linked List II
Problems:
1. Detect loop (Floyd's cycle)
2. Delete a node
3. Merge two sorted linked lists
4. Remove duplicates

### Day 24 — Stacks  ✅
Concept: LIFO, Python list as stack.
Problems:
1. ✅ Implement stack
2. ✅ Valid parentheses (balanced brackets)
3. Reverse string using stack
4. Next greater element (stretch)

### Day 25 — Queues
Concept: FIFO, `collections.deque`.
Problems:
1. ✅ Implement queue
2. Implement stack using queues / queue using stacks
3. Circular queue (read)

### Day 26 — Trees (intro)  ✅
Concept: binary tree, BST, traversals.
Problems:
1. ✅ Inorder / Preorder / Postorder traversal
2. Height of tree
3. Count nodes / leaf nodes
4. Level order traversal (BFS)

### Day 27 — Full revision Day A
Re-solve all ✅ problems you've flagged from Weeks 1–2.

### Day 28 — Full revision Day B + Level-1 final test
Re-solve flagged from Weeks 3–4. Then a 60-min timed test: 3 mixed problems. Log final score.

---

## After Level-1
You'll be solid for service-company coding rounds. Next we build:
- **Level-2:** more trees/BST, advanced sliding window, intro to DP, basic graphs (BFS/DFS).
- **Aptitude module** (parallel from Week 2).
- **Core CS module** (DBMS, OOP, OS, CN) for technical interviews.

## Practice platforms
- **GeeksforGeeks** — best for service-company style + "must-do coding questions" list.
- **HackerRank** — used by many service companies for actual tests; do their "Problem Solving" track.
- **LeetCode** — Easy set, filter by topic.

## Daily checklist
- [ ] Read concept + watch/skim one explanation
- [ ] Dry-run 1 example on paper
- [ ] Code each problem yourself (no copy-paste)
- [ ] Narrate your approach out loud
- [ ] Log in tracker + flag anything to revise
