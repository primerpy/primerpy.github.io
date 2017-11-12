---
title: "Binary Addition"
slug: "binary-addition"
date:  2017-11-11
tags:  ["python", "algorithms"]
---

We can add binary numbers together, just like we can with base 10 numbers

In the example below:

-   `a` is in base 10 -- because we have 10 possible digits, the highest value we can represent with one digit is 9
-   When we want to represent `a` value one higher, we need to add another digit.
-   `a` now has two digits -- we incremented the invisible leading digit, which was 0 and is now 1, and set the last digit back to zero.

```python
a = 9
a += 1
a
```



When we add 1 to 19, we increment the leading 1 by 1, and then set the last digit to 0, giving us 20.

```python
a = 19
a += 1
a
```



When we add 1 to 99, we increment the last digit by 1, and add 1 to the first digit, but the first digit is now greater than 9, so we have to increment the invisible leading digit.

```python
a = 99
a += 1
a
```



Binary addition works the exact same way, except the highest value any single digit can represent is 1

-   We'll add binary values by defining a `binary_add` function that was made just for this exercise
-   It's not extremely important to know how it works at the moment

```python
b = "1"
def binary_add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

c = binary_add(b, "1")
c
```



c now equals "11"

```python
c = binary_add(c, "1")
c
```



c now equals "100"

```python
c = binary_add(c, "1")
c
```


