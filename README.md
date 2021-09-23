# Task

> Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression.
> Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right.
> Additions and subtractions have a lower priority and should also be performed left-to-right.
 
## parse()
 - This method is used to translate a string into an array, separating numbers, signs, brackets.

## pr()
 - This is necessary to determine the priority of the symbol.


## evaluete()
 - Used to solve the example using [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

```
// Example:
Calculator().evaluate("2 / 2 + 3 * 4 - 6")
//Output: 7

// Example:
Calculator().evaluate("3 * 4 + 3 * 7 - 6")
// Output: 27

// Example:
Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )")
// Output: 16
 ```
