#2 Monte Carlo Simulation Solution

total = 0
n = 10000
for i in range(0,n):
    cards = np.arange(0,144) #0-143
    counter = 0
    numberofunique = 0
    cardsowned = []
    while True:
        counter = counter + 1
        cardbought = np.random.choice(cards)
        if not cardbought in cardsowned:
            numberofunique = numberofunique + 1
            cardsowned.append(cardbought)
            if numberofunique == 144:
                break
    total = total + counter
    if i %1000 == 0:
        print(f"{100*i/n}%")
    
print(total*5/n) #About 4000$
