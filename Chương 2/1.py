a, b = map(int, input().split())
if(a!=0):
    x = -b/a;
    print(x)
elif(a==0 and b==0):
    print("VSN")
else:
    print("VN")