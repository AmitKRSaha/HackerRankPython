def count_substring(string, sub_string):
    count = 0
    for x in range(0, len(string)):
        if x + len(sub_string) <= len(string) and string[x: x + len(sub_string)] == sub_string:
            count = count + 1
            
    print(count)

def string_validation(str):
    print(True) if str.isalnum() else print(False)
    print(True) if str.isalpha() else print(False)
    print(True) if str.isdigit() else print(False)
    print(True) if str.islower() else print(False)
    print(True) if str.isupper() else print(False)

def lower_score(val):
    lst = []
    scores = []
    for x in val:
        scores.append(float(x[1]))
    uniqlst = list(set(scores))
    uniqlst.sort()

    for x in val:
        if x[1] == uniqlst[1]:
            lst.append(x[0])
    print(lst)            
        


def Runners_Up(val):
    val.sort()
    print(val[1])

def List_Comprehensions(x,y,z, n):
    finallist = []
    for i in range(0,x + 1):
        for j in range(0,y + 1):
            for k in range(0,z + 1):
                if i + j + k != n:
                    lst = [i, j, k]
                    finallist.append(lst)
                    print(finallist)



def tupleHash(num, val):
    tupleN = tuple(val)
    print(hash(tupleN))
    