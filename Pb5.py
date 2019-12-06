f = open("date3.txt", "r")
date = f.readline()
n = int (date)
list = []
profit =[]
prev = []
for i in range( n ):
    date = f.readline().split()
    date = [int(j) for j in date]
    list.append(date)
list.sort(key=lambda x: x[1])
for i in range( n ):
    profit.append(list[i][2])
    prev.append(-1)
print(list)
print()
maxval = 0
maxi = 0
for i in range( 1, n):
    for j in range( i ):
        if (list[j][1] <= list[i][0]):
            if (profit[j] + list[i][2] > profit[i]):
                profit[i] = profit[j] + list[i][2]
                prev[i] = j
            if (maxval < profit[i]):
                maxi = i
                maxval = profit[i]
afis = []
while (prev[i] != -1):
    afis.append(list[i])
    i = prev[i]
afis.append(list[i])
print(maxval)
print(afis)