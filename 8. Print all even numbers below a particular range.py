# Level-3 ______________________________________________________________________
# 8. Print all even numbers below a particular range.

even_num=int(input("Enter The Number :"))
addnum=1
while addnum<=even_num:
    temp_2=2*addnum
    if temp_2<=even_num:
        print("Even Number :",temp_2)
    addnum+=1
