firstWord = "carte"
secondWord = "antet"
insert = 2
remove = 2
replace = 2
def Levenshtein(str1, str2, n, m):

    matrice = [[[0, 0] for x in range(m + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                matrice[i][j][0] = j * insert
                matrice[i][j][1] = j
            elif j == 0:
                matrice[i][j][0] = i * remove
                matrice[i][j][1] = i
            elif str1[i - 1] == str2[j - 1]:
                matrice[i][j] = matrice[i - 1][j - 1]
            else:
                matrice[i][j][0] = min(matrice[i][j - 1][0] + remove, matrice[i - 1][j][0] + insert, matrice[i - 1][j - 1][0] + replace)
                matrice[i][j][1] = 1 + min(matrice[i][j-1][1], matrice[i - 1][j][1], matrice[i -1][j - 1][1])
    print(matrice)
    k = matrice[n][m][1] - 1
    array = []
    i = n
    j = m
    while matrice[i][j][1] != 0:
        diag = matrice[i - 1][j - 1][1]
        left = matrice[i][j - 1][1]
        top = matrice[i - 1][j][1]
        if min(diag, left, top) == diag:
            if diag != matrice[i][j][1]:
                array.insert(k, f'{str1[i - 1]} -> {str2[j - 1]}')
            i -= 1
            j -= 1
        elif min(diag, left, top) == left:
            if left != matrice[i][j][1]:
                array.insert(k, f'inseram {str2[j - 1]}')
            j -= 1
        else:
            if top != matrice[i][j][1]:
                array.insert(k, f'stergem {str1[i - 1]}')
            i -= 1
        k -= 1
    return matrice[n][m][0], array

distance, result = Levenshtein(firstWord, secondWord, len(firstWord), len(secondWord))
print(distance)
for elem in result:
    print(elem)