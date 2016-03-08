import numpy as np
f = open('colors.data', 'r')

cols = np.zeros(3)
c = np.zeros(3)

for i in f:
    i = i.strip()
    if(len(i) != 6): continue
    c[0] = int(i[0:2], 16)
    c[1] = int(i[2:4], 16)
    c[2] = int(i[4:6], 16)
    cols = np.vstack((cols, c))

np.save('colors.npy', cols)
