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

- Is Complete (under some conditions)
- Optimality depends on h(s)
- Time complexity also depends on h(s)
- Space complexity is Exponential

### Bi-Directional A*
If we have access to goals, start an A* search from start and goal nodes, stop when searches meet.
- Halves the space complexity (still exponential)
## Heuristics
Measures how far away from the goal is a state.
Becomes 0 if the state is a goal state.
### Admissability
- **Under-estimate** the cost to goal: $0 \le h(s) \le g(s)$ 
- Zero for any goal state
- Non-zero for all others
Example: Manhattan Distance
![[Pasted image 20240317230721.png]]
### Consistency
A heuristic is consistent if it is monotonically decreasing along the path to the goal.


### Dominance
![[Pasted image 20240317232736.png]]
 
## Beyond A*
• Limited Space A* (aka Beam Search) 
• Pre-compute costs for certain nodes and use a version of triangle equality 
• Learning heuristics 
• Online A*
• Dynamic Environment: D*

## Local Search
Disregard the path, just focus on getting the goal state.
- Solution is the goal state itself.
- Search for a