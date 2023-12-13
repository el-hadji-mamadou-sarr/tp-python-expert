def func(a, b):
    return a if a>b else b

def func(a,b,c):
    return a if a>b else b if b>c else c

def funcA(*args):
    max = args[0]
    for i in args:
        if i > max:
            max = i
    return max

print(funcA(1,4,5,9,3,9))

m = "mississippi"

def func(m):
    for i in m:
        nbr=0
        if(i == 'i'):
            nbr+=1
    return(nbr)

def countM(m):
    count = {}
    result =[]
    for i in range(len(m)):
        nbr=0
        if m[i] not in count:
            for j in range(len(m)):
                if m[i] == m[j]:
                   nbr+=1
            count[m[i]] = nbr
            result.append((m[i], nbr))
    return result


result = countM(m)

def replace(result):
    max = 0
    letter =''
    for i in result:
        if i[1] > max:
            max = i[1]
            letter = i[0]

    new = m.replace(letter, 'a')

    return new            

print(replace(result))

