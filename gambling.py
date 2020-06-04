import random

def gambling(stake,goal,trials):
    bet=0
    win=0
    lose=0

    for counter in range(1,trials+1):
        money=stake

        while money>0 and money<goal:
            bet=+1
            if random.random()<0.5:
                money+=1
            else:
                money-=1
        if money==goal:
            win+=1
        else:
            lose+=1    

    print(("{0} win and {1} lose of {2} trials").format(win,lose,trials))
    wining_percentage=(win/trials)*100
    losing_percentage=(lose/trials)*100
    print("Wining percentage {0}".format(wining_percentage))
    print("Losing percentage {0}".format(losing_percentage))

#main
stake=int(input("Enter stake "))
goal=int(input("Enter goal "))
trials=int(input("Enter trials "))
gambling(stake,goal,trials)
