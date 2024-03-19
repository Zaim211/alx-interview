Minimum Operations:

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

Solution(explication):

Initialization:

ope is initially 0.
i starts from 2.
Loop Iteration 1:

i = 2: Since 9 % 2 != 0, 2 is not a factor of 9.
No change in ope or n.
i becomes 3.
Loop Iteration 2:

i = 3: Since 9 % 3 == 0, 3 is a factor of 9.
ope += i increments ope by 3, making ope = 3.
n //= i updates n to 3.
i becomes 1.
Loop Iteration 3:

i = 2: Since 3 % 2 != 0, 2 is not a factor of 3.
No change in ope or n.
i becomes 3.
Loop Iteration 4:

i = 3: Since 3 % 3 == 0, 3 is a factor of 3.
ope += i increments ope by 3, making ope = 6.
n //= i updates n to 1.
i becomes 1.
End of Loop:

Since i > n, the loop ends.
Result:

The minimum number of operations (ope) required to reach n = 9 characters is 6.
