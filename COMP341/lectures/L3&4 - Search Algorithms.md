# Uninformed Search
- DFS - Stack
- BFS - Queue

## ID-DFS Iterative Deepening
**Idea:** Always use DFS, but cap its depth.
- Run DFS with depth 2, if no solution..
- Run DFS with depth 3, if no sol...
- Run again, and so on.

## Uniform Cost Search f(s) = g(s)
Use a priority que based on the *cumulative* cost.
- Complete and Optimal
- Explores in every direction


# Informed Search
## Greedy Best-First Search f(s) = h(s)
![[Pasted image 20240317230043.png]]
Expand next state based on the sole heuristic value
- Complete only if cycles are prevented
- Not Optimal
- $O(b^m)$ time
- $O(b^m)$ space
## A* Search f(s) = g(s) + h(s)
Choose the next state based on heuristic + actual cost

- Not optimal if the heuristic is not admissable.
### Heuristic
Measures how far away from the goal is a state.
Becomes 0 if the state is a goal state.
### Admissability
- **Under-estimate** the cost to goal: $0 \le h(s) \le g(s)$ 
- Zero for any goal state
- Non-zero for all others
Example: Manhattan Distance

 
