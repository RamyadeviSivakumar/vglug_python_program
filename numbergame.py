sum=0
print("\nWelcome for the play!!\nTwo palyers can play the game\ndon't enter number more than 10\n\nlets start")
while (sum<=100):
    while True:
        a=int(input("Player1: "))
        if a<=10 :
            sum=sum+a
            print("sum is",sum)
            if sum==100:
                print("player 1 wins")
            break
        else:
            print("Enter less than 10")
    if sum>=100:
        break

    while  True:
        b=int(input("Player2: "))
        if b<=10 :
            sum=sum+b
            print("sum is",sum)
            if sum==100:
                print("player 2 wins")
            break
        else:
            print("Enter less than 10")
    if sum>=100:
        break