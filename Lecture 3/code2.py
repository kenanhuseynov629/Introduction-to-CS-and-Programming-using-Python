where=input("go left or right? ")
k=0
while where=="right":
    k=k+1
    print(k)
    if k>2:
            print(":(")
    where=input("go left or right? ")
print("you got out")
