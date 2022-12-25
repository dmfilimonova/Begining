from random import *
l = [ i for i in range(1, 76)]
l_ = [i for i in sample(l, 25)]
l_[12] = 0
for i in range(len(l_)):
    if i in [4, 9, 14, 19]:
        print(l_[i], end='\n')
    else:
        print(str(l_[i]).ljust(3), end= ' ')



