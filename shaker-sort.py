import check
f_msg = "Forward Pass {0}: {1}"
b_msg = "Backward Pass {0}: {1}"

def forward_pass(L, i, right, pass_number):
  '''
  Mutates L by going from the front to 
  the back of the list L and swaps whenever
  the left is greater than the right element
  
  Effects:
      Mutates L
      Prints to the screen
  
  forward_pass: (listof Int) Nat Nat Nat -> None
  '''
  while i < right:
    if L[i] > L[i+1]:
      temp = L[i]
      L[i] = L[i+1]
      L[i+1] = temp
      i += 1
    else:
      i += 1
  print(f_msg.format(pass_number, L))
  
def backward_pass(L, k, left, pass_number):
  '''
  Mutates L by going from the back 
  to the front of the list L
  and swaps whenever the left is 
  greater than the right element
  
  Effects:
      Mutates L
      Prints to the screen
  
  backward_pass: (listof Int) Nat Nat Nat -> None
  '''
  while k > left:
    if L[k] < L[k-1]:
      temp = L[k]
      L[k] = L[k-1]
      L[k-1] = temp
      k -= 1
    else:
      k -= 1
  print(b_msg.format(pass_number, L))

def shaker_sort(L):
  '''
  Mutates the list L so that it is 
  sorted in increasing order
  
  Effects: 
      Mutates L
      Prints to the screen
      
  shaker_sort: (listof Int) -> (listof Int)
  
  Examples:
      shaker_sort([4, 3, 2, 5]) => None
          Final list printed: [2, 3, 4, 5]
      shaker_sort([1, 2, 3, 4, 5, 6]) => None
          Final list printed: [1, 2, 3, 4, 5, 6]
  '''
  
  pass_number = 1
  left = 0
  right = len(L) - 1
  while left < right:
    forward_pass(L, left, right, pass_number)
    left += 1
    backward_pass(L, right, left, pass_number)
    right -= 1
    pass_number += 1

## Examples as Tests:
check.set_print_exact("Forward Pass 1: [3, 2, 4, 5]",
"Backward Pass 1: [2, 3, 4, 5]",
"Forward Pass 2: [2, 3, 4, 5]",
"Backward Pass 2: [2, 3, 4, 5]")
check.expect("Example 1", shaker_sort([4, 3, 2, 5]), None)
check.set_print_exact("Forward Pass 1: [1, 2, 3, 4, 5, 6]",
"Backward Pass 1: [1, 2, 3, 4, 5, 6]",
"Forward Pass 2: [1, 2, 3, 4, 5, 6]",
"Backward Pass 2: [1, 2, 3, 4, 5, 6]",
"Forward Pass 3: [1, 2, 3, 4, 5, 6]",
"Backward Pass 3: [1, 2, 3, 4, 5, 6]")
check.expect("Example 2", shaker_sort([1, 2, 3, 4, 5, 6]), None)
## Tests:
L = [6, 3, 8, 2, 7, 4, 5]
check.set_print_exact(f_msg.format(1, [3, 6, 2, 7, 4, 5, 8]),
                      b_msg.format(1, [2, 3, 6, 4, 7, 5, 8]),
                      f_msg.format(2, [2, 3, 4, 6, 5, 7, 8]),
                      b_msg.format(2, [2, 3, 4, 5, 6, 7, 8]),
                      f_msg.format(3, [2, 3, 4, 5, 6, 7, 8]),
                      b_msg.format(3, [2, 3, 4, 5, 6, 7, 8]))
check.expect("MarkUs Basic Test", shaker_sort(L), None)
check.expect("MarkUs Basic Test Mutation", L, [2, 3, 4, 5, 6, 7, 8])