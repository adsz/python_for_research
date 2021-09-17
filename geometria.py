import math
import random

def distance(x, y):
    dist = math.sqrt((x[0] - y[0])**2 + (x[1] - y[0])**2)
    return dist

def in_circle(x, origin = [0,0]):
   # print(distance(x,origin))
   if distance(x,origin) < 1:
       return True
   else:
       return False

def rand():
   return(random.uniform(-1,1))

random.seed(1)
inside = []
points = []
R=10000
for i in range(R):
    point = (rand(),rand())
    points.append(point)
for j in points:
    inside.append(in_circle(j))
my_dict = {i:inside.count(i) for i in inside}
proportion = my_dict[True]/R
print(proportion)

print(math.pi/4-proportion)


