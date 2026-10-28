list1=[1,2,3,4,5]
list2=[2,4,6,8]
print("Element in list one is:",list1)
print("Element in list two is:",list2)
if len(list1)==len(list2):
    printf("lists have same length")
else:
    print("lists have different length")
s1=0
s2=0
for i in range(len(list1)):
    s1=s1+list1[i]
print("The sum of list 1 is:",s1)
for i in range(len(list2)):
    s2=s2+list2[1]
print("The sum of list 2 is:",s2)
if s1==s2:
    print("The sum of lists are same")
else:
    print("The sum of lists are different")
print("the common element in list is:")
for i in list1:
    for j in list2:
     if i==j:
        print(i)