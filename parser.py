in_back = {}

a = [0, 1, 2, 3, 4, 5, 6, 7]
b = ['0','1','2','3,','4','5','6','7']


for i in range(7):
    in_back.update({a[i+1]: b[i+1]})

print(in_back)
