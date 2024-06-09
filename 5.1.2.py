n=[]
a=int(input("Enter the size : "))
print("Enter the",a,"elements: ")
for i in range(0,a):
      a=int(input())
      n.append(a)
b=int(input("Enter the search key: "))
x=0
l=len(n)
for i in range(l):
    if n[i]==b:
        print(b,"found at position",i)
        x=1
        break
if x==0:
    print(b,"not found")
