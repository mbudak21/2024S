# Heuristic
Measures how far away from the goal is a state.
Becomes 0 if the state is a goal state.

## Greedy Search
choose the next state based on the sole heuristic value
## A* Search
Choose the next state based on heuristic + actual cost

- Not optimal if the heuristic is not admissable.

### Admissability
We need the heuristic to be less than actual costs
Example: Manhattan Distance

