# Level-3 ______________________________________________________________________
# 5. Print the factors of a given number.


factors=int(input("Enter The Number     :"))
temp=1
while temp<=factors:
    temp_2=factors%temp
    if temp_2==0:
        print("Given Number Factors :",factors,'%',temp,"=",temp_2)
    temp+=1
    








# Example 
# print(5%1) = 0
# print(5%2) = 1
# print(5%3) = 2
# print(5%4) = 1
# print(5%5) = 0
