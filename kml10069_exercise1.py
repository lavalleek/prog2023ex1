def overlap (list_A, list_B):
  overlap = []
  for i in range(len(list_A)):
    for j in range(len(list_B)):
      if list_A[i] == list_B[j]:
        overlap.append(list_A[i])
  return(overlap)