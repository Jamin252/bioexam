import copy, time

NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def numberdifference(numfrom, numto):
    numberfrom = copy.deepcopy(numfrom)
    numberto = copy.deepcopy(numto)
    tempto = copy.deepcopy(numberto)
    tempfrom = copy.deepcopy(numberfrom)
    for i in tempto:
        for k in tempfrom:
            if i == k:
                numberto.remove(i)
                numberfrom.remove(k)
                tempfrom.remove(k)
                break
    return len(numberto) + len(numberfrom)

def translate(i):
    number = []
    for k in str(i):
        for n in NUMBERS[int(k)]:
            number.append(n)
    return number

x= translate(0)
y = translate(00)
print(x, y)
print(numberdifference(x,y))