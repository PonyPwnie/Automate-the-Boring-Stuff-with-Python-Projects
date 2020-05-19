#!/usr/bin/env python3
import random


number_of_streaks = 0
last_experiment = random.randint(0, 1)
counter = 0
for experiment_number in range(9999):
    # Code that creates a list of 100 'heads' or 'tails' values.
    this_experiment = random.randint(0, 1)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    if this_experiment != last_experiment:
        counter = 0
    else:
        counter += 1

    if counter == 6:
        number_of_streaks += 1
        counter = 0

print('Chance of streak: %s%%' % (number_of_streaks / 100))
