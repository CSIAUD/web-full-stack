# @Name Tri et Comptage des températures du mois

def tp6() :
    tabTemp = [
        20,13,17,15,18,19,20,
        17,17,17,18,10,22,18,
        17,21,15,16,16,14,19,
        18,15,11,12,12,16,15,
        16,19
    ]

    dictTemp = {}
    for temp in tabTemp :
        if temp in dictTemp.keys() :
            dictTemp[temp] = dictTemp[temp] + 1
        else :
            dictTemp[temp] = 1


    keys = sorted(dictTemp.keys())
    for key in keys :
        print(f"{key}°C: {dictTemp[key]}")