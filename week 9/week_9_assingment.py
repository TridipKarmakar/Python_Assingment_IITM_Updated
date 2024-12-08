# WEEK9-GrPA 1

def reverse(L):
    if len(L) <= 1:
        return L
    # Bring the last element to the front
    # And reverse the first n - 1 elements
    return [L[-1]] + reverse(L[:-1])

# WEEK9-GrPA 2
def linear(P, Q, k):
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[0] / Q[0] != k:
        return False
    return linear(P[1: ], Q[1: ], k)

# WEEK9-GrPA 3
def collatz(n):
    # base case of the recursion
    # if n = 1, you don't need to call the function at all
    if n == 1:
        return 0
    # simple application of the piecewise defn of the
    # Collatz function
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)

# WEEK9-GrPA 4

# Basic idea behind the solution:
# The sum of all steps in a sequence should add up to n
# The last term in any sequence could be either 1, 2 or 3
# The number of sequences with last step as 1 is given by steps(n - 1)
# The number of sequences with last step as 2 is given by steps(n - 2)
# The number of sequences with last step as 3 is given by steps(n - 3)
# So, total number of sequences is steps(n - 1) + steps(n - 2) + steps(n - 3)
def steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return steps(1) + steps(2) + 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)

# WEEK9-GrPA 5
def ancestry(P, present, past):
    if present == past:
        return [past]
    return [present] + ancestry(P, P[present], past)