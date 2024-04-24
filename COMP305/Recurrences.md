## Substitution Method
Guess the bound and use mathematical induction to proove it.
## Recursion Tree Method
Convert the recurrence into a tree and try to understand its cost.
## Master Method
$$
T(n) = aT(\frac{n}{b}) + f(n), \text{Where } a\ge1 \text{ and } b > 1 
$$
There are the following three cases: 

- If f(n) = O(nc) where c < Logba then T(n) = Θ(nLogba) 
- If f(n) = Θ(nc) where c = Logba then T(n) = Θ(ncLog n) 
- If f(n) = Ω(nc) where c > Logba then T(n) = Θ(f(n))
