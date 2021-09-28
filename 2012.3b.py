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

def main(nfrom, nto):
    number = nfrom
    target = nto
    frontier_start = Frontier()
    frontier_final = Frontier()
    start = Node(number)
    final = Node(target)
    frontier_start.frontier.append(start)
    frontier_final.frontier.append(final)

    explored = []
    explored_final = []
    while True:
        if len(frontier_start.frontier) == 0 or len(frontier_final.frontier) == 0:
            return "no solution"
        
        for tempnode in frontier_final.frontier:
            for node1 in frontier_start.frontier:
                if node1.number == tempnode.number:
                    return node1.action_made + tempnode.action_made

        node_start = frontier_start.remove()

        explored.append(node_start.number)
        for num in node_start.neighbour():
            if num not in explored and not frontier_start.contain(num):
                child = Node(num)
                child.action_made = node_start.action_made + 1
                frontier_start.frontier.append(child)

        if len(frontier_start.frontier) == 0 or len(frontier_final.frontier) == 0:
            return "no solution"

        for tempnode in frontier_final.frontier:
            for node1 in frontier_start.frontier:
                if node1.number == tempnode.number:
                    return node1.action_made + tempnode.action_made
        
        node_final = frontier_final.remove()

        explored_final.append(node_final.number)
        for num in node_final.neighbour():
            if num not in explored and not frontier_final.contain(num):
                child_final = Node(num)
                child_final.action_made = node_final.action_made + 1
                frontier_final.frontier.append(child_final)




if __name__ == "__main__":
    count = 0
    number = []
    zero = ["Z", "E", "R", "O"]
    for i in range(1, 100):
        x = main(i, 0)
        if x == 1:
            count += 1
    print(count)