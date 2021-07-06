import array as arr



size=int(input("Enter size of the stack : "))
queue = arr.array('i',[ ])
rear =-1

print("1. Enqueue  2. Dequeue  3. Display  4. Exit")

while(True):
    opt=int(input(("Enter your option : ")))
    if(opt==1):
        if (rear == size - 1):
            print("Queue overflow.")
        else:
            ele = int(input("Enter element : "))
            rear=rear+1
            queue.append(ele)

    elif(opt==2):
        if(rear==-1):
            print("Queue is Underflow")
        else:
            print("Deleting element :",queue[0])
            rear=rear-1
            queue.pop(0)

    elif(opt==3):
        if (rear == -1):
            print("Queue is empty.")
        else:
            print(queue)
    elif(opt==4):
        break
    else:
        print("Invalid option.")
