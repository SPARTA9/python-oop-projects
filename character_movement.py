#Part a(i):
class Character:
    def __init__(self, PName, pXPosition, pYPosition):
        self.Name = PName
        self.XPosition = pXPosition
        self.YPosition = pYPosition

    #Part a(ii):
    def GetXPosition(self):
        return self.XPosition
    def GetYPosition(self):
        return self.YPosition
    
    #Part a(iii):
    def SetXPosition(self, value):
        self.XPosition = self.XPosition + value
        if self.XPosition > 10000:
            self.XPosition = 10000
        if self.XPosition < 0:
            self.XPosition = 0
    def SetYPosition(self, value):
        self.YPosition = self.YPosition + value
        if self.YPosition > 10000:
            self.YPosition = 10000
        if self.YPosition < 0:
            self.YPosition = 0
    
    #Part a(iv):
    def Move(self, direction):
        if direction == "up":
            self.SetYPosition(10)
        if direction == "down":
            self.SetYPosition(-10)
        if direction == "left":
            self.SetXPosition(-10)
        if direction == "right":
            self.SetXPosition(10)

#Part b):
Jack = Character("Jack",50,50)

#Part c):
class BikeCharacter(Character):
    def __init__(self, PName, pXPosition, pYPosition):
        super().__init__(PName, pXPosition, pYPosition)

    #Part c(ii):
    def Move(self, direction):
        if direction == "up":
            super().SetYPosition(20)
        if direction == "down":
            super().SetYPosition(-20)
        if direction == "left":
            super().SetXPosition(-20)
        if direction == "right":
            super().SetXPosition(20)
#Part d):
Karla = BikeCharacter("Karla", 100, 50)

#Part e(i):
Char = input("Which character would you like to move (Karla or Jack): ").lower()
while Char != "karla" and Char != "jack":
    Char = input("Invalid Character, try again: ").lower()
direction = input("What direction do yo want the character to move (up,down,left,right): ")
while direction != "up" and direction != "down" and direction !="left" and direction != "right":
    direction = input("Invalid direction, try again: ")
if Char == "jack":
    Jack.Move(direction)
    print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
else:
    Karla.Move(direction)
    print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")

               
