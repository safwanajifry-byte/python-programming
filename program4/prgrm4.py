n=int(input("Enter the number of element in the list:"))
num_list=[]
for x in range(n):
    x=int(input("Enter the element:"))
    if x<100:
        num_list.append(x)
    else:
        num_list.append('over')
        print(num_list)