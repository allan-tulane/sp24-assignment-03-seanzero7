# CMPS 2200 Assignment 3
## Answers

**Name:**______Sean Hall___________________


Place all written answers from `assignment-03.md` here for easier grading.
1a) Given a $N$ dollars, state a greedy algorithm for producing as few coins as possible that sum to $N$.

Assuming 2**k is the highest currency we have and k does not go below 0, we can use

def getGeometrica(N,k):
  if N < 1: 
    return
  elif  N < 2**k:
    getGeometrica(N,k-1)
  else：
    GiveCoin(2**k)
    getGeometrica(N - 2**k, k)

1b) Prove that this algorithm is optimal by proving the greedy choice and optimal substructure properties.

-- This algorithm is optimal by greedy choice as the algorithm always picks the largest possible coin that doesn't exceed the amount to give (N). By taking out the biggest chunks out of the amount due, we rapidly reduce the number of times needed to pick a coin. 
The algorithm follows the optimal substructure properties as it ensures that each greedy step leads to a new problem of size N-2**k. Itself being solved by the same strategy, guaranteeing the overall optimality. 


1c) Because each recursive call divides N by 2^k, reducing it by a substantial fraction with large values of k, the number of calls is logarithmic. The number of times k is decremented is logarithmic with respect to N. 
Thus, total work is O(log(n)^2).
The span would be determined by the depth of the recursion. Thus Span is O(log(n))


2a). Counterexample showing that the greedy algorithm does not produce fewest number of coins:

Denominations:
D0 = 1
D1 = 3
D2 = 4

N = 6

Greedy: Takes largest D2, remaining N is 2. Fulfilled by taking 2 denominations of D0. Total 3 coins:

From common sense, we know that 2 coins is the minimum number. 

2b). The optimal subsctircture property of this problem will be the mininum ammount of coins needed from 0 to n dollars. If we can use a bottom up algorithm to get the value that will be much easlier.


2c). we can store a list of all the denominators we have. And having a table of size n+1 * num_denominators. And we just need to fill the table with minium coins needed to get potimal solution.
So the work will be O(N * number of demoninators) and the span will be the longest run in the chart will will be O(n)
