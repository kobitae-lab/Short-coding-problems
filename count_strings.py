import check


def count_strings(L, prefix):
  '''
  Returns the number of strings 
  in L that start with prefix
  
  count_strings: (listof Str) Str -> Nat
  Requires:
      strings in L are all lowercase english 
          letters, sorted alphabetically
      prefix is all lowercase string
  
  Examples:
      count_strings(L, "") => 5
      count_strings(L, "a") => 3
  '''
  ## find first appearance of prefix
  ## find last appearance of prefix
  ## calculate the range
  length_p = len(prefix)
  
  left = 0
  right = len(L) - 1
  
  first_index = -1
  last_index = -1
  
  if prefix == "":
    return len(L)
    
  while left <= right:
    mid = (left + right) // 2
    mid_prefix = L[mid][:length_p] if len(L[mid]) >= length_p else L[mid]
    
    if mid_prefix == prefix and (mid == 0 or L[mid-1][:length_p] != prefix):
      first_index = mid
      left = right + 1
    elif mid_prefix < prefix:
      left = mid + 1
    else:
      right = mid - 1
  
  left = 0
  right = len(L) - 1
  while left <= right:
    mid = (left + right) // 2
    mid_prefix = L[mid][:length_p] if len(L[mid]) >= length_p else L[mid]

    if mid_prefix == prefix and (mid == len(L)-1 or L[mid+1][:length_p] != prefix):
      last_index = mid
      left = right + 1
    elif mid_prefix < prefix:
      left = mid + 1
    else:
      right = mid - 1
      
  if last_index == -1 or first_index == -1:
    return 0
  else:
    return last_index - first_index + 1

## Examples as Tests:
L = ["apart", "apple", "apply", "banana", "berry"]
check.expect("Example 1", count_strings(L, ""), 5)
check.expect("Example 2", count_strings(L, "a"), 3)

## Tests:
check.expect("MarkUs Basic Test", count_strings(L, "app"), 2)