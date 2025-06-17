a = int(input())
b = int(input())
c = int(input())

g = list(map(int,str(a*b*c)))

for i in range(10):
  print(g.count(i))