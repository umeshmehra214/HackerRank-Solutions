# Task :-
  
# Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Input Format :- 

# A single line containing a positive integer,n.

# Output Format : - 

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Solutions:-------------------->

n = int(input())
if(n%2==1) or n in range (5,21):
    print("Weird")
else:
    print("Not Weird")
