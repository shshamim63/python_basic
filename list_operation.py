command_number=int(input())
L=[]
for i in range (command_number):
    command=input().split()
    if command[0]=='insert':
        L.insert(int(float(command[1])),int(float(command[2])))
    elif command[0]=='print':
        print(L)
    elif command[0]=='remove':
        L.remove(int(float(command[1])))
    elif command[0]=='append':
        L.append(int(float(command[1])))
    elif command[0]=='sort':
        L.sort()
    elif command[0]=='pop':
        L.pop()
    elif command[0]=='reverse':
        L.reverse()