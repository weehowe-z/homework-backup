import numpy as np
import matplotlib.pyplot as plt

file = open("two_spiral_train.txt")
train = []
for line in file:
    (tmp1,tmp2,tmp3) = line.split('\t',2)
    train.append([[float(tmp1),float(tmp2)],[int(tmp3)]])
file.close()


import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

plt.axes([0.025,0.025,0.95,0.95])
plt.scatter(X,Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5,1.5), plt.xticks([])
plt.ylim(-1.5,1.5), plt.yticks([])
# savefig('../figures/scatter_ex.png',dpi=48)
plt.show()