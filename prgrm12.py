n=int(input("enter the number of colours:"))
color_list=[]
for i in range(n):
    color=input("enter the colour:")
    color_list.append(color)
print(color_list)
print("The first colour is:",color_list[0])
print("The last colour is:",color_list[-1])