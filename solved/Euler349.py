#!/usr/bin/env python

# Find the number of black squares given the path of an ant who flips the colours
# of squares in a grid.

# At first, the pattern seems chaotic and difficult to analyze. So, we run a
# simulation and see what happens. We notice that after around ~10000 moves,
# a repeating pattern emerges, so we can use that to determine the total number
# of flipped squares.

import operator

# Variables used to run the simulation
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

dirs = {
  LEFT : (-1, 0),
  UP : (0, 1),
  RIGHT: (1, 0),
  DOWN: (0, -1),
}

facing = UP
curr_pos = (0,0)
blacks = set([])

target = 10**18

# Given a list of items, returns a list of the differences between
# adjacent items in the list
def differences(lis) :
  return map(operator.sub, lis[1:], lis[:-1])

# Run the simulation until we observe a repeating period
step = 0
history = []
while True :
  if curr_pos in blacks :
    facing = (facing - 1) % 4
    blacks.discard(curr_pos)
  else :
    facing = (facing + 1) % 4
    blacks.add(curr_pos)
  curr_pos = (curr_pos[0] + dirs[facing][0], curr_pos[1] + dirs[facing][1])

  # Print the grid. This is what we use to visually see the pattern. It is turned
  # off in order to actually compute the answer
  if False :
    biggest = max(max(map(abs, x)) for x in blacks)
    print biggest, step
    for i in xrange(-biggest, biggest+1) :
      for j in xrange(-biggest, biggest+1) :
        if (i,j) == curr_pos :
          print 'O'
        elif (i,j) in blacks :
          print 'x',
        else :
          print ' ',
      print
    raw_input('Next?')

  # Check to see if a repeating pattern has emerged. Empirically we observed it
  # does not show up until around 10000 steps. Also, we do not want to get false
  # positives so we only check for decently long periods.
  if step >= 11000 :
    history.append(len(blacks))
    if len(history) % 2 == 0 and len(history) >= 20 :
      first = history[:len(history)/2]
      last = history[len(history)/2:]
      if (differences(first) == differences(last)) :
        # We have found the repeating period (probably). So do the math and figure out
        # our answer

        step += 1  # Make sure we count the move we just made
        count_of_blacks = len(blacks)

        period_length = len(history)/2
        effect_of_period = (history[-1] - history[0])/2

        steps_left = target - step - 2  # There is an off-by-one error somewhere
        full_periods_left = steps_left / period_length
        count_of_blacks += full_periods_left * effect_of_period

        steps_remaining = steps_left % period_length
        count_of_blacks += history[steps_remaining] - history[0]

        print 'Period length is', period_length
        print 'Increase in count is', effect_of_period
        print 'Full periods left is', full_periods_left
        print 'Number of leftover steps is', steps_remaining
        print 'Total black squares:', count_of_blacks
        exit(0)

  step += 1

  # If we run the simulation to completion (obviously for values < 10^18),
  # output the simulated value
  if step == target :
    print 'Simulated value:', len(blacks)
    exit(0)

