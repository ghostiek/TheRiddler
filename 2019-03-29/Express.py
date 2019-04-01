import numpy as np

#p = 6/30, so q = 24/30
#Exact solution
print((24/30)*(23/29)*(22/28)) 

#Prob we get a card we haven't seen yet is 0.49852216748768474
#Therefore, we are more likely to see a duplicate card when pulling out 3 more when playing again!

#Through simulation (just for fun)
#This follows a hypergeometric distribution
n = 100000000
print(np.sum(np.random.hypergeometric(24, 6, 3, n) == 3)/n)

#Prob we get a card we haven't seen yet is 0.49852216748768474
#This concurs with our previous result.
