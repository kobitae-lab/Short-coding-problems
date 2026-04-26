import check


## A SeatStatus is a Bool
## Where: False represents an empty (i.e. unoccupied) seat, True represents an occupied seat

## A RowLabel is a Str
## Requires:
##   The string is one of 'A','B', ... 'Z'
##   (i.e. a single uppercase alphabetic character)

## A SeatRow is a (list RowLabel (listof SeatStatus))

## A Theatre is a (listof SeatRow)
## Requires:
##   Rows are distinct (no two rows have the same RowLabel).
##   Rows are in alphabetical order without skipping any letters.
##   The first row will always start with 'A' (assuming at least 1 row exists).
##   A row may be closed in which case it will be stored with a RowLabel and an empty list.
##   It is possible for rows to stop before reaching 'Z'.

## a Request is a Str
## Requires:
##   The format is 'L#' where L is an uppercase letter and # is a natural number greater than 0.
##   e.g., 'A1' means Row A, Seat index 1 (the first seat) and 'C3' means Row C, Seat index 3.

def check_row(cinema, reqs, i, rejections): # mutates cinema
  '''
  Returns the number of rejections after mutating the list cinema 
  given the reqs, i to go through the whole list and rejections 
  to keep track of the amount of reqs failed
  
  Effects:
      Mutates cinema
  
  check_row: Theatre (listof Request) Nat Nat -> Nat
  '''
  
  if reqs == []:
    return rejections
  if i >= len(cinema):
    rejections += 1
    return check_row(cinema, reqs[1:], 0, rejections)
  
  elif cinema[i][0] == reqs[0][0]: 
    if check_valid(cinema, int(reqs[0][1:]), i):
      cinema[i][1][int(reqs[0][1:]) - 1] = True
      return check_row(cinema, reqs[1:], 0, rejections)
    else:
      rejections += 1
      return check_row(cinema, reqs[1:], 0, rejections)
      
  else:
    return check_row(cinema, reqs, i+1, rejections)

def check_valid(cinema, req, i):
  '''
  Returns True if the given request req is valid in a 
  Theatre cinema, i is given as the row req is found in
  
  check_valid: Theatre Nat Nat -> Bool
  '''
  
  if len(cinema[i][1]) >= req:
    if cinema[i][1][req - 1]:
      return False
    else:
      return True
  else:
    return False

def print_theatre(cinema, i):
  '''
  Prints the theatre cinema, given i as an index
  
  Effects:
      Prints to the screen
  
  print_theatre: Theatre, Nat -> None
  '''
  if i >= len(cinema):
    return
  else:
    print('Row ' + cinema[i][0] + ':', end='')
    seats(cinema, i, 0)
    print()
    print_theatre(cinema, i+1)

def seats(cinema, i, k):
  '''
  Prints the row i in a theatre cinema, given k as an index
  
  Effects:
      Prints to the screen
  
  seats: Theatre, Nat, Nat -> None
  '''
  if len(cinema[i][1]) == 0:
    print(' ', end='')
    return
  if k >= len(cinema[i][1]):
    return
  if cinema[i][1][k]:
    print(' [X]', end='')
    seats(cinema, i, k+1)
  else:
    print(' [_]', end='')
    seats(cinema, i, k+1)

def process_bookings(cinema, reqs):
  '''
  Returns the number of invalid requests in reqs, given a Theatre, cinema
  
  Effects:
    Prints to the screen,
    Mutates cinema
  
  process_bookings: Theatre (listof Request) -> Nat
  
  Examples:
      process_bookings(example_theatre_1, requests_2) => 2
      process_bookings(example_theatre_2, requests_3) => 0
  '''
  
  rejections = check_row(cinema, reqs, 0, 0) 
  print_theatre(cinema, 0)
  return rejections


test_theatre_1 = [
                 ['A', [False, False, False]], 
                 ['B', [False, True, True, False, False]],
                 ['C', [True, False ,False, True, True]],
                 ['D', []],
                 ['E', [False]]
                ]
example_theatre_1 = [
  ['A', [False, True]],
  ['B', []],
  ['C', [True, True, False]],
  ['D', [False, True, True]]]

example_theatre_2 = [
  ['A', [False]],
  ['B', [True, True, False]],
  ['C', [False, False, True]]]

test_theatre_2 = [
  ['A', [True, False, False, False, False, False,
  True, False, False, False, False]],
  ['B', [False, True, False]],
  ['C', [False, False]]]

requests_1 = ['A1', 'C5','B6','E1', 'A1','G3']
requests_2 = ['A3', 'A1', 'D2']
requests_3 = ['A1', 'C1']
requests_4 = ['A11', 'C1', 'C2']

expected_theatre_1 = [
    ['A', [True, False, False]],               
    ['B', [False, True, True, False, False]],  
    ['C', [True, False, False, True, True]],   
    ['D', []],                                 
    ['E', [True]]                              
]

expected_theatre_2 = [
  ['A', [True, True]],
  ['B', []],
  ['C', [True, True, False]],
  ['D', [False, True, True]]]
  
expected_theatre_3 = [
  ['A', [True]],
  ['B', [True, True, False]],
  ['C', [True, False, True]]]

expected_theatre_4 = [
  ['A', [True, False, False, False, False, False,
  True, False, False, False, True]],
  ['B', [False, True, False]],
  ['C', [True, True]]]

EX1_ROW_A = "Row A: [X] [_] [_]"
EX1_ROW_B = "Row B: [_] [X] [X] [_] [_]"
EX1_ROW_C = "Row C: [X] [_] [_] [X] [X]"
EX1_ROW_D = "Row D: "
EX1_ROW_E = "Row E: [X]"

EX2_ROW_A = "Row A: [X] [X]"
EX2_ROW_B = "Row B: "
EX2_ROW_C = "Row C: [X] [X] [_]"
EX2_ROW_D = "Row D: [_] [X] [X]"

EX3_ROW_A = "Row A: [X]"
EX3_ROW_B = "Row B: [X] [X] [_]"
EX3_ROW_C = "Row C: [X] [_] [X]"

EX4_ROW_A = "Row A: [X] [_] [_] [_] [_] [_] [X] [_] [_] [_] [X]"
EX4_ROW_B = "Row B: [_] [X] [_]"
EX4_ROW_C = "Row C: [X] [X]"


## Examples:
check.set_print_exact(EX2_ROW_A, EX2_ROW_B, EX2_ROW_C, EX2_ROW_D)
check.expect("Example 1", 
              process_bookings(example_theatre_1, requests_2), 2)
check.expect("Example 1 Mutation", example_theatre_1, expected_theatre_2)

check.set_print_exact(EX3_ROW_A, EX3_ROW_B, EX3_ROW_C)
check.expect("Example 2",
              process_bookings(example_theatre_2, requests_3), 0)
check.expect("Example 2 Mutation", example_theatre_2, expected_theatre_3)        

## Tests:
check.set_print_exact(EX1_ROW_A, EX1_ROW_B, EX1_ROW_C, EX1_ROW_D, EX1_ROW_E)

check.expect("Basic Test", 
             process_bookings(test_theatre_1, requests_1), 4)

check.expect("Basic Mutation Test", test_theatre_1, expected_theatre_1)

check.set_print_exact(EX4_ROW_A, EX4_ROW_B, EX4_ROW_C)

check.expect("Double Digit Test", 
              process_bookings(test_theatre_2, requests_4), 0)
check.expect("Double Digit Mutation Test", test_theatre_2, expected_theatre_4)
