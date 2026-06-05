N=int(input())
A=int(input())
for i in range(N):
 op,B=input().split()
 B=int(B)
 
 if op == "+":
    print(i+1,A+B)
    A=A+B
 elif op == "-":
    print(i+1,A-B)
    A=A-B
 elif op == "*":
    print(i+1,A*B)
    A=A*B
 elif op=="/":
      if B==0:
         print("error")
         break
      
      else:
        print(i+1,A//B)
        A=A//B