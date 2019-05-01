import numpy as np
data = np.array([[15,3.78],
[29,2.0],
[10,2.5],
[25,2.85],
[30,3.96]])
logit_pi = (data*np.array([0.2, 0.5])).sum(axis=1) - 3.98
p_xi = 1.0/(np.exp(logit_pi*-1) + 1)
n = int(input())
if not (1 <= n <= 5):
    print('Error')
elif p_xi[n - 1] > 0.5:
    print('True')
else:
    print('False')