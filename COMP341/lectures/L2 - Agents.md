We want to make **rational** agents, which acts to maximize its utility.
**Agent:** An autonomous entity that exists in some kind of *environment* and that *perceives* and *acts*.
## How do we formulate an AI problem?
- Performance/Utility
- Environment
- Actions
- Sensors


# Agent Types

## Simple Reflex
![[Pasted image 20240315205042.png]]
```python
if dirty:
	suck()
else:
	move()
```

They do not consider the aftermath of their actions, they just reflex.

## Model Based Reflex Agent
Model-Based Reflex Agents improve upon simple reflex agents by maintaining some form of internal state that depends on the percept history, allowing them to make better-informed decisions. This internal state is a model of the world, which, combined with the current percept, can help the agent determine the impact of its actions. This model includes knowledge about how the world works (the "laws" of the environment) and the current state of the world.

The structure of a Model-Based Reflex Agent can be described as follows:

1. **Update State:** Based on the current state, action taken, and current percept, update the internal model/state of the world.
2. **Rule Match:** Use the internal state and current percept to decide the action by matching against a set of rules.
3. **Action:** Execute the chosen action.

**Pacman:** is a model-based reflex agent. (in the Projects)


**Evaluation Function:** Gets a state and returns a number, indicating the "goodness" of a state.

## Goal Based Agent

## Utility Based Agent