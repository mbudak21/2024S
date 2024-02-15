Mehmet Murat Budak 78940
team: Mete Yokuş, Ali Mete Sevinçli, Fırat Gümüş
## 3 Areas Of Improvement In Lectures

- Algorithm Design
	  Div & Conq, Dynamic Programming, Greedy, Incr. Impr.
- Algorithm Analysis
	  Recurrences, Amortization, Randomization ...
- Algorithm Correctness
	  Induction, copy-paste proofs ...

  
### Divide And Conquer Template:

```python

def F(problem):
	if Base.case(problem):
		return simple_answer(problem)
	pieces = Divide(problem)
	Answers = [F(p) where p in Pieces]
	return merge(Answers)
```

**Exercise 1:** Write the binary search and merge sort algos in the above template.

```python
def F(Array, number):
	# Base case
	if Array = []:
		return False
		
	l = len(Array)
	middle_element = Array[len/2]
	if middle_element > Number:
		return F(Array[:len/2], number)
	elif middle_element == Number:
		return True # Second Base Case
	elif middle_element < Number::
		return F(Array[len/2:], number)
```

**Recurrence:** 
$$
P(n) = P(\frac{n}{2}) + \Theta(1)
$$

**Recurrence:** 
$$
P(n) = \frac{1}{8}P(\frac{n}{2}) + \Theta(n^2)
$$

