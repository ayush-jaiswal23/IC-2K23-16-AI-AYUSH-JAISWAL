# Water Jug Problem

## Problem Statement

We are given two water jugs:

* **4-liter jug**
* **3-liter jug**

Both jugs are initially empty. We have an unlimited supply of water.

The objective is to measure exactly **2 liters of water** using these two jugs.

### Allowed Operations

We can perform the following operations:

1. Fill a jug completely.
2. Empty a jug completely.
3. Pour water from one jug into the other until either:

   * the source jug becomes empty, or
   * the destination jug becomes full.

---

## Solution

We can solve this problem using the following sequence of operations.

We represent the state as:

```text
(4L Jug, 3L Jug)
```

where the first value represents the amount of water in the 4-liter jug and the second value represents the amount of water in the 3-liter jug.

### Step 1: Initial State

Both jugs are empty.

```text
(0, 0)
```

### Step 2: Fill the 3-Liter Jug

Fill the 3-liter jug completely.

```text
(0, 3)
```

Now:

* 4L jug = 0 liters
* 3L jug = 3 liters

### Step 3: Pour the 3-Liter Jug into the 4-Liter Jug

Transfer all 3 liters into the 4-liter jug.

```text
(3, 0)
```

Now the 4-liter jug contains 3 liters.

Therefore, it has:

```text
4 - 3 = 1 liter
```

of remaining capacity.

### Step 4: Fill the 3-Liter Jug Again

Fill the 3-liter jug completely.

```text
(3, 3)
```

Now both jugs contain 3 liters.

### Step 5: Pour the 3-Liter Jug into the 4-Liter Jug

The 4-liter jug has space for only **1 liter**.

Therefore, only 1 liter can be transferred from the 3-liter jug.

Before pouring:

```text
4L Jug = 3L
3L Jug = 3L
```

After pouring:

```text
4L Jug = 4L
3L Jug = 2L
```

Final state:

```text
(4, 2)
```

Therefore, the **3-liter jug contains exactly 2 liters of water**.

---

## Solution Sequence

The complete sequence can be represented as:

```text
(0, 0)
   ↓
Fill 3L Jug
   ↓
(0, 3)
   ↓
Pour 3L → 4L
   ↓
(3, 0)
   ↓
Fill 3L Jug
   ↓
(3, 3)
   ↓
Pour 3L → 4L
   ↓
(4, 2)
```

### Final Result

```text
4-Liter Jug = 4 liters
3-Liter Jug = 2 liters
```

**Exactly 2 liters have been measured.**

---

## Algorithm

```text
1. Start with both jugs empty.
2. Fill the 3-liter jug.
3. Pour the 3-liter jug into the 4-liter jug.
4. Fill the 3-liter jug again.
5. Pour the 3-liter jug into the 4-liter jug.
6. Since the 4-liter jug has space for only 1 liter,
   only 1 liter is transferred.
7. The 3-liter jug is left with exactly 2 liters.
8. Stop.
```

---

## State Representation

Each state is represented as:

```text
(Amount in 4L Jug, Amount in 3L Jug)
```

For this solution:

| Step | Operation     | State    |
| ---- | ------------- | -------- |
| 0    | Initial state | `(0, 0)` |
| 1    | Fill 3L jug   | `(0, 3)` |
| 2    | Pour 3L → 4L  | `(3, 0)` |
| 3    | Fill 3L jug   | `(3, 3)` |
| 4    | Pour 3L → 4L  | `(4, 2)` |

The final state `(4, 2)` satisfies the goal because the 3-liter jug contains exactly **2 liters**.

---

## Key Concept

The Water Jug Problem is a classic **State Space Search** problem in Artificial Intelligence.

Each possible configuration of the two jugs can be considered a **state**.

For example:

```text
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)
```

Operations such as filling, emptying, and pouring move us from one state to another.

Therefore, the problem can be viewed as finding a path:

```text
Initial State → Intermediate States → Goal State
```

For this particular problem, the target can be reached directly using the sequence described above.

---

## Time and Space Complexity

If we solve the general Water Jug Problem using **Breadth-First Search (BFS)**, where the jug capacities are `A` and `B`, the maximum number of states is:

```text
(A + 1) × (B + 1)
```

Therefore:

### Time Complexity

```text
O(A × B)
```

### Space Complexity

```text
O(A × B)
```

For this specific 4L and 3L problem, there are only:

```text
(4 + 1) × (3 + 1) = 20
```

possible states.

---

## Conclusion

The 4-liter and 3-liter Water Jug Problem can be solved by repeatedly filling the 3-liter jug and transferring its water into the 4-liter jug.

After the second transfer, the 4-liter jug becomes full and the 3-liter jug is left with exactly **2 liters**.

### Final Answer

**2 liters are obtained in the 3-liter jug.**
