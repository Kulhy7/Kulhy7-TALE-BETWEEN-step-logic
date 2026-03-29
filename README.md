# StepCount System

## How it works
Encounters are triggered based on player movement.

- A random value (RNG) is generated between min_value and max_value
- Each step increases a counter
- When the counter exceeds RNG, a battle starts

## Dynamic Behavior
Instead of a simple increasing chance:

- The range (min_value–max_value) **shrinks over time**
- This makes encounters more likely the longer the player walks
- RNG may be re-generated during this process based on milestones

## Special Case
- Rarely, the system delays an encounter (no_one_came mechanic), creating unpredictability

## Clean vs Normal Version
- **Normal**: Includes location and item modifiers (used in upcoming game TALE BETWEEN)
- **Clean**: Core logic only, no modifiers (for personal use in your own game)
