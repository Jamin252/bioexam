board = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(".")
    board.append(row)
NUMBERS = ["zero", "one", "two", "three", "four", "five"]
class player():
    def __init__(self, list):
        self.one = list[0]
        self.two = list[1]
        self.three = list[2]
        self.four = list[3]
        self.five = list[4]
        self.order = 1
temp1 = input("First player order")
temp2 = input("Second player order: ")
x = temp1.split(" ")
y = temp2.split(" ")
firstPlayer = player(x)
secondPlayer = player(y)
board[4] = x
board[0] = y
board[2][2] = "*"

def neu(y, x):
    y = int(y)
    x = int(x)
    for i in range(1, 8):
        if i == 1:
            tempx = x
            tempy = y - 1
            while board[tempy][tempx] == ".":
                tempy += 1
            return ()
while True:
