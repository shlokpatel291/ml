x=input("enter numbers together")
list1=x.split()
oddlist=[]
evenlist=[]


l=len(list1)
print(l)
for i in range(0,l):
    no=eval(list1[i])
    if (no%2==0):
        evenlist.append(no)
    else:
        oddlist.append(no)

print("list",list1)
print("odd no",oddlist)
print("even no",evenlist)