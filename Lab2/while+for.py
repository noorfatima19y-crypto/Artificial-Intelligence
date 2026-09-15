count=0
while(count<=3):
    
    print("hye!")
    count=count+1

s="greeks"
for i in s:
    print(i)

#iterating by index of the sequences

list=["geeks","for","geeks"]
for index in range(len(list)):
    print (list[index])


# continue statement
list="geeksforgeeks"
for letter in list:
    if letter=='e' or letter=='s':
        continue
    print ("Current Letter: ",letter)


##break statement 
for letter in "geeksforgeeks":
    if letter=='e' or letter=='s':
     break
print ("Current Letter:",letter)