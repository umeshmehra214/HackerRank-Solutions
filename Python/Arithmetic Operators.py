# Task:- 
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
  
# -> The first line contains the sum of the two numbers.
# -> The second line contains the difference of the two numbers (first - second).
# -> The third line contains the product of the two numbers.

# Solutions ------->

if __name__ == '__main__':
  
    a = int(input())
    b = int(input())
    
    sum = (a + b)
    diff = (a - b)
    product = (a*b)
    
    print(sum)
    print(diff)
    print(product)

