f = open("date1.txt", "r")
n = int(f.readline())
list = []
urmator = [-1 for x in range(n+1)]
anterior = [-1 for x in range(n+1)]
Lungime_max = [0 for x in range(n)]
for i in range( n ):
    pereche = f.readline().split()
    list.append(pereche)
    list[i][0] = int( list[i][0] )
    list[i][1] = int( list[i][1] )
    Lungime_max[i] = 1
    urmator[i] = -1
print(list)
for i in range( n-2, -1, -1):
    for j in range( i+1, n):
        if(list[i][1] == list[j][0] ):
            if( Lungime_max[i] <= Lungime_max[j]):
                Lungime_max[i] = Lungime_max[j] + 1
                urmator[i] = j
                anterior[j] = i
            else:
                anterior[j] = i
for i in range( n ):
    if( urmator[i] != -1):
        break

while ( i != -1):
    print(list[i])
    i =urmator[i]
print(urmator)
print( Lungime_max)
print(anterior)