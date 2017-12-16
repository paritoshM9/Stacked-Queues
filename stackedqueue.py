def enqueue(stack1,stack2,x):
    top1=len(stack1)-1
    while(len(stack1)!=0):
        stack2.append(stack1[top1])
        stack1.remove(stack1[top1])
        top1-=1
    stack1.append(x)
    top2=len(stack2)-1
    while(len(stack2)!=0):
        stack1.append(stack2[top2])
        stack2.remove(stack2[top2])
        top2-=1
    return
def dequeue(stack1):
    top1=len(stack1)-1
    if(len(stack1)==0):
        return(-1)
    else:
        print(stack1[top1])
        stack1.remove(stack1[top1])
        top1-=1
    return
print("Enter the number of instructions: ")
n=int(input().strip())
stack1=[]
stack2=[]

for i in range(n):
    choice=int(input().strip())
    if(choice==1):
        x=input().strip()
        enqueue(stack1,stack2,x)
    elif(choice==2):
        dequeue(stack1)
        
        
