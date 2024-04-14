import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  # Base cases
  if S == "":
    return len(T)
  if T == "":
    return len(S)

  # Recursive cases
  if S[0] == T[0]:
    result = fast_MED(S[1:], T[1:], MED)
  else:
    result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

  # Save in dict before returning
  MED[(S, T)] = result
  return result

def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
      return MED[(S, T)]

  # Base cases
  if S == "":
      return ("-" * len(T), T)
  if T == "":
      return (S, "-" * len(S))

  # Recursive cases
  if S[0] == T[0]:
      edited_S, edited_T = fast_align_MED(S[1:], T[1:], MED)
      result = (S[0] + edited_S, T[0] + edited_T)
  else:
      insert_S, insert_T = fast_align_MED(S, T[1:], MED)
      delete_S, delete_T = fast_align_MED(S[1:], T, MED)
    
      insert_cost = 1 + len(insert_S)
      delete_cost = 1 + len(delete_S)

      if insert_cost <= delete_cost:
        result = ("-" + insert_S, T[0] + insert_T)
      else:
         result = (S[0] + delete_S, "-" + delete_T)
  # Save in dictionary
  MED[(S, T)] = result
  return result

print(MED(test_cases[0][0], test_cases[0][1]));

print(fast_MED('book', 'back'))
print(fast_align_MED('kookaburra', 'kookybird'))
print(MED('book', 'back'))