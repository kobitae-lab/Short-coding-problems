import check
def merge(L1,L2):
  '''
  Returns a new list where it merges L1 and L2 
  in increasing order of their first index
  
  merge(L1, L2): (list Nat Nat) (list Nat Nat) -> (listof Nat)
  '''
  T = []
  pos1 = 0
  pos2 = 0
  while (pos1 < len(L1)) and (pos2 < len(L2)):
    if L1[pos1][0] <= L2[pos2][0]:
      T.append(L1[pos1])
      pos1 += 1
    else:
      T.append(L2[pos2])
      pos2 += 1
  while (pos1 < len(L1)):
    T.append(L1[pos1])
    pos1 += 1
  while (pos2 < len(L2)):
    T.append(L2[pos2])
    pos2 += 1
  
  return T
  
def merge_sort(L):
  '''
  Returns a new list which is like
  L but in increasing order
  
  merge_sort: (listof (list Nat Nat)) -> (listof (list Nat Nat))
  '''
  if len(L) >= 2: 
    mid = len(L)//2
    L1 = L[:mid]
    L2 = L[mid:]
    L1_copy = merge_sort(L1)
    L2_copy = merge_sort(L2)
    return merge(L1_copy,L2_copy)
  else:
    return L[:]

def merge_intervals(L):
  '''
  Returns a new list that is like L except 
  is sorted in ascending order on start time
  and overlapping intervals are merged
  
  merge_intervals: (listof (list Nat Nat)) -> (listof (list Nat Nat))
  Requires:
      the inner list follows the format [start, end]
          where start <= end
  
  Examples:
      merge_intervals([[1,2], [4, 7], [5, 8]]) =>
                      [[1,2], [4, 8]]
      merge_intervals([[3, 5], [5, 7], [8, 8]]) =>
                      [[3, 5], [5, 7], [8, 8]]
  '''
  
  start_sorted = merge_sort(L)
  i = 0
  N = []
  while i < len(start_sorted):
    if i == len(start_sorted)-1:
      N.append(start_sorted[i])
      i += 1
        
    elif start_sorted[i][1] > start_sorted[i+1][0]:
      merge = [start_sorted[i][0], max(start_sorted[i][1], start_sorted[i+1][1])]
      start_sorted[i+1] = merge
      i += 1
    else:
      N.append(start_sorted[i])
      i += 1
  return N

## Examples as Tests:
check.expect("Example 1", merge_intervals([[1,2], [4,7], [5,8]]),
                                          [[1,2], [4,8]])
check.expect("Example 2", merge_intervals([[3, 5], [5, 7], [8, 8]]),
                                          [[3, 5], [5, 7], [8, 8]])
## Tests:
L = [[1, 3], [5, 7], [2, 4], [8, 10]]
check.expect("MarkUs Basic Test", merge_intervals(L), [[1, 4], [5, 7], [8, 10]])