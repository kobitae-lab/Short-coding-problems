import check


def num_2_by_N_tiles(N):
  '''
  Returns the number of ways to fill a 2 by N grid
  with the horizontal, vertical, and square tiles
  
  num_2_by_N_tiles: Nat -> Nat
  
  Examples:
      num_2_by_N_tiles(0) => 0
      num_2_by_N_tiles(2) => 5
  '''

  if N == 0:
    return 0
  if N == 1:
    return 1
  
  y = 1 ## result when N = 1
  x = 3 ## result when N = 2
  unique_ways = x
  
  for i in range(3, N + 1):
    unique_ways = x + (y * 2)
    y = x
    x = unique_ways
  
  return unique_ways
  
##Examples as tests:
check.expect("Example 1", num_2_by_N_tiles(0), 0)
check.expect("Example 2", num_2_by_N_tiles(2), 3)

##Tests:
check.expect("MarkUs Basic Test", 
            num_2_by_N_tiles(3),5)
check.expect("1", num_2_by_N_tiles(1), 1)
check.expect("4", num_2_by_N_tiles(4), 11)
check.expect("5", num_2_by_N_tiles(5), 21)