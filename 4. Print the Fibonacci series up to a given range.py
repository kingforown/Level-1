#Level-3 ______________________________________________________________________
# 4. Print the Fibonacci series up to a given range.

fib=int(input("Enter The Number :"))
plus=1
A=1     
B=1     
temp=0
while plus<=fib:     
    temp=A+B
    if temp <= fib:
        print(temp)
        A=B
        B=temp
    plus+=1


    
# Example 
#A   B
# 1=2
# 2=3
# 3=5
# 5=8
# 8=13
