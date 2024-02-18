# Blackjack Strategy Simulation

## Overview
This repository contains a Python-based simulation for analyzing different Blackjack strategies, focusing on "standing" at various values under "hard" or "soft" approaches, comparing these against the "basic" strategy. The aim is to identify the most effective stand value and approach, with the simulation providing insights into which strategy parameters yield the highest winning percentage.

## Features
- **Strategy Evaluation**: Simulates "standing" strategies and compares them with the "basic" Blackjack strategy.
- **Parameter Optimization**: Finds the best parameters for "standing" strategies using leave-one-out cross-validation.
- **Visualization**: Plots the performance of different strategies over a range of conditions for easy comparison.
- **Customization**: Allows users to change simulation conditions (e.g., number of decks, dealer rules) and compare outcomes.

## Dependencies
- `random`: For generating random numbers to simulate card shuffling and dealing.
- `seaborn` (`sns`): For creating visually appealing statistical graphics.
- `matplotlib.pyplot` (`plt`): For plotting simulation results and comparisons.
- `math`: Provides access to mathematical functions like floor and ceiling, used in calculations.
- `re`: For regular expression operations, useful in parsing strategy names and conditions.
- `classes`: Custom classes used for simulating rounds and implementing the Linear Congruential Generator (LCG) for shuffling.

## Main Components
- `spawn_deck()`: Generates a standard deck of cards.
- `shuffle_deck(deck, seed, deck_num=1)`: Shuffles the deck using a seed for reproducibility.
- `deal_hand(shuffled_deck)`: Deals cards to the player and dealer.
- `cumulative_average(numbers)`: Calculates cumulative averages for simulation results.
- `niceWatch_runIt(conditions_dict)`: Orchestrates the simulation based on specified conditions.
- `line_chart(conditions_dict, sim_dict)`: Generates line charts to visualize the simulation outcomes.

## Usage
1. Ensure all dependencies are installed.
2. Customize simulation parameters in the `conditions_dict` within `niceWatch_runIt` function as needed.
3. Run the simulation to evaluate different strategies and visualize the outcomes using `line_chart`.

## Simulation Classes
- `simulate_round`: Manages the simulation of a single round of Blackjack, evaluating different strategies.
- `LCG`: Implements a Linear Congruential Generator for pseudo-random number generation, used in card shuffling.

## Running the Simulation
To run the simulation, execute the main script after setting your desired conditions. The script will automatically simulate the specified strategies, perform analyses, and generate visualizations of the results.

## Customizing the Simulation
Adjust the `conditions_dict` in the `niceWatch_runIt` function to explore different scenarios. You can vary the number of decks, the trials, the strategies tested, and when to stand.

## Visualization
The `line_chart` function plots the performance of each strategy across the simulations, highlighting the winning percentages and providing a clear comparison of their effectiveness.

