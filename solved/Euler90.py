# We want to find the number of ways to print the numbers 0 - 9 on the faces of
# two cubes, so that we can form all the square numbers below 100:
# 01 04 09 16 25 36 49 64 81

# To do this, we will first designate a left cube and a right cube. Then, we
# observe that for each number, it will be possible to build # it in only two
# ways: first digit on left cube, or first digit on right cube. We will try all
# possible assignments of squares to left cube or right cube, and then for each
# assignment count the number of possibilities

# We add the caveat that we can flip 6's or 9's, but they are still considered
# distinct numbers on the cube. We will solve this by identifying 6's and 9's, 
# and then at the end counting twice for each 6

# The list of squares, with 9's replaced with 6's
nums = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(6,4),(8,1)]

answers = set([])

# Utility function for changing sets with just a 6 to include
# just a 9
def change_6_to_9(se) :
  if 6 in se :
    return se.difference(set([6])).union(set([9]))
  return se

# Given a partial cube, generate all possibilitiies for that cube
def choices_for(cube_so_far) :
  if len(cube_so_far) == 6 :
    # Since the assign_nums code only generates 6's, we need to check
    # to see if the cube has just a 6, and then we need to generate
    # the corresponding cube containing a 9
    if 6 in cube_so_far and 9 not in cube_so_far :
      return [cube_so_far, change_6_to_9(cube_so_far)]
    else :
      return [cube_so_far]
  else :
    # In the recursive case, we generate all possible new entries and
    # add them to the cube
    ret = []
    for i in xrange(10) :
      if i not in cube_so_far :
        ret.extend(choices_for(cube_so_far.union(set([i]))))
    return ret

answers = set([])

# Generate all possible cube configurations and store them in an answer set
def assign_nums(num_list, left_so_far, right_so_far) :
  global answers

  if (len(left_so_far) > 6 or len(right_so_far) > 6) :
    return
  if (len(num_list) == 0) :
    # Check to see how many possibilities there are
    left_possibilities = choices_for(left_so_far)
    right_possibilities = choices_for(right_so_far)
    for lposs in left_possibilities :
      for rposs in right_possibilities :
        lposs = frozenset(lposs)
        rposs = frozenset(rposs)

        # We are very aggressive to ensure no duplicates
        if (lposs, rposs) not in answers and (rposs, lposs) not in answers :
          answers.add((lposs, rposs))
  else :
    num = num_list[0]

    # Try assigning first digit to left cube
    assign_nums(num_list[1:],
      left_so_far.union(set([num[0]])),
      right_so_far.union(set([num[1]])))
    # Try assigning first digit to right cube
    assign_nums(num_list[1:],
      left_so_far.union(set([num[1]])),
      right_so_far.union(set([num[0]])))

assign_nums(nums, set([]), set([]))

print len(answers)

