# GCD, LCM

## Greatest Common Divisor
최대 공약수

```python
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
```

## Least Common Multiple
최소 공배수

```python
def lcm(a, b):
    return a * b / gcd(a, b)
```
