# Factorial For Loop Function - Dry Run for factorial(3)

## Function Overview

The `factorial_for_loop` function calculates the factorial of a number using an iterative approach with a for loop, rather than recursion.

```python
def factorial_for_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

## How It Works

1. Initialize `result` to 1
2. Loop from 2 to n (inclusive)
3. Multiply `result` by each number in the range
4. Return the final result

## Dry Run: factorial(3)

### Initial State
- Input: `n = 3`
- `result = 1`
- Loop range: `range(2, 4)` → [2, 3]

### Iteration 1
- `i = 2`
- `result *= 2` → `result = 1 * 2 = 2`

### Iteration 2
- `i = 3`
- `result *= 3` → `result = 2 * 3 = 6`

### Loop Ends
- No more values in range(2, 4)

### Return
- `return result` → **6**

## Result

**factorial(3) = 6** ✓

This is correct because 3! = 1 × 2 × 3 = 6
