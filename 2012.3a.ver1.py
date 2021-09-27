import copy

NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def numberdifference(numfrom, numto):
    numberfrom = copy.deepcopy(numfrom)
    numberto = copy.deepcopy(numto)
    tempto = copy.deepcopy(numberto)
    tempfrom = copy.deepcopy(numberfrom)
    for i in tempto:
        br = False
        for k in tempfrom:
            if i == k:
                numberto.remove(i)
                numberfrom.remove(k)
                tempfrom.remove(k)
                br = True
                break
    return len(numberto) + len(numberfrom)

class Node():
    def __init__(self, value):
        self.action_made = 0
        result = []
        for k in str(value):
            for n in NUMBERS[int(k)]:
                result.append(n)
        self.value = result
        self.number = value

    def neighbour(self):
        result = []
        for i in range(1000):
            if i == self.number:
                continue
            numberto = []
            for k in str(i):
                for n in NUMBERS[int(k)]:
                    numberto.append(n)
            if numberdifference(self.value, numberto) <= 5:
                result.append(i)
        return result

class Frontier():
    def __init__(self):
        self.frontier = []

    def remove(self):
        if len(self.frontier) == 0:
            return None
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

    def contain(self, number):
        for node in self.frontier:
            if node.number == number:
                return True
        return False

def main():
    temp = input("numbers: ")
    temp1 = temp.split(" ")
    number = int(temp1[0])
    target = int(temp1[1])
    frontier = Frontier()
    start = Node(number)
    frontier.frontier.append(start)

    explored = []
    while True:
        if len(frontier.frontier) == 0:
            return "no solution"

        if frontier.contain(target):
            for node1 in frontier.frontier:
                if node1.number == target:
                    return node1.action_made

        node = frontier.remove()

        if frontier.contain(target):
            for node1 in frontier.frontier:
                if node1.number == target:
                    return node1.action_made

        explored.append(node.number)
        for num in node.neighbour():
            if num not in explored and not frontier.contain(num):
                child = Node(num)
                child.action_made = node.action_made + 1
                frontier.frontier.append(child)





if __name__ == "__main__":
    num1 = main()
    num2 = main()
    num3 = main()
    print(num1)
    print(num2)
    print(num3)