n=[]
a=int(input("Enter the size : "))
print("Enter the",a,"elements: ")
for i in range(0,a):
      a=int(input())
      n.append(a)
x=n[0]
y=n[0]
l=len(n)
for i in range(1,l):
    if x>n[i]:
        x=n[i]
    if y<n[i]:
        y=n[i]
print("Smallest element :",x)
print("Largest element :",y)
        
    
