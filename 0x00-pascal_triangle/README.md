# Pascal's Triangle

This script provides a function, `pascal_triangle(n)`, that generates Pascal's triangle up to the specified level `n`. Pascal's triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

## Function Signature

```python
def pascal_triangle(n)
```

## Parameters

- `n` (int): The desired level of Pascal's triangle.

## Returns

- `res` (list of lists): A list of lists of integers representing Pascal's triangle up to level `n`.

## Example Usage

```python
pascal_triangle(5)
```

### Output

```
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

The function `pascal_triangle(5)` generates Pascal's triangle up to level 5 and returns a list of lists representing the triangle. The output shows the resulting triangle with each level displayed as a separate list.
