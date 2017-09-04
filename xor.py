# Page 174-166, formula (6.3)'s code
import numpy as np
def relu(x):
    return np.where(x>0,x,0)
 
X=np.array([[0,0],[0,1],[1,0],[1,1]])
W=np.array([[1,1],[1,1]])
c=np.array([[0,-1]])
w=np.array([[1],[-2]])
b=0
print(np.dot(relu(np.dot(X,W)+c),w)+b)
