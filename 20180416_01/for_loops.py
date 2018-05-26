import numpy as np

var = [4,5,6,8]
var = [var, var, var, 'Hallo Welt!']

#for i in var:
#    for j in i:
#        print(j)
        
s = 'Hallo nochmals.'

print(s[0:5])
print(s[5])

z = np.zeros((10,10))

for i in range(10):
    z[i,i] = 999
    print(i)


