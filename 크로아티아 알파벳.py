c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj' , 's=', 'z=']

data = input()
count = 0

while len(data) > 0:
    if len(data) >= 3 and data[:3] in c:
        data = data[3:]
        count += 1
    elif len(data) >=2 and data[:2] in c:
        data = data[2:]
        count += 1
    else:
        data = data[1:]
        count += 1
print(count)