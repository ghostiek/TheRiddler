import numpy as np

probs = np.linspace(0.9,0.99, 10)

def simulate_spellingbee(probabilities):
    survived = np.ones(10)
    #Keep looping 'till we meet our condition
    while True:
        for i in range(0, len(probabilities)):
            #If eliminated (aka is 0) we skip
            if not survived[i]:
                continue
            #Update survival status
            survived[i] = 0 if np.random.rand() >= probabilities[i] else 1
            #Return survival status after the competition has ended
            if np.sum(survived) == 1:
                return survived

#We go first
n_sims = 10000
prob_decreasing = list(reversed(probs))

winners = np.zeros(10)
for i in range(0, n_sims):
    winners += simulate_spellingbee(prob_decreasing)
#Prob of winning
print(winners[0]/np.sum(winners)) #0.5246

#We go last
n_sims = 10000

winners = np.zeros(10)
for i in range(0, n_sims):
    winners += simulate_spellingbee(probs)
#Prob of winning
print(winners[-1]/np.sum(winners)) #0.5315
