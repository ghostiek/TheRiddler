"""
Heres my logic behind this solution:

We are trying to solve for numbers divisible by 100, clearly the only numbers that matter are the 2 first digits of each number, since the
3rd and so on can be any number and it would still be divisible by 100. 

We can also be confident in saying there is no point in accounting for values that multiply into something smaller than 100 considering how
large the set of values we can pick from is.

counter = 0
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            if i*j*k%100 == 0:
                counter = counter + 1

print(counter/(100**3)) #12.43%
