# Level-3 ______________________________________________________________________
# 5. Print the factors of a given number.

fact_num=int(input("Enter The Number    :"))
temp=1
sum=temp
while temp<=fact_num:
    sum=sum*temp
    temp+=1

print("Your Factors Number :",sum,sep="")


#Example code Run Type
#   sum=sum*temp
#    1 =  1*1    
#    2 =  1*2  
#    6 =  2*3   
#    24=  6*4   
#   120=  24*5    
