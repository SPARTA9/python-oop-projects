#Part a(i):
from datetime import date
class Character:
    # self.CharacterName = String
    # self.DateOfBirth = DATE
    # self.Intelligence = REAL
    # self.Speed = INTEGER
    def __init__(self, pCharacterName, pDateOfBirth, pIntelligence, pSpeed):
        self.CharacterName = pCharacterName
        self.DateOfBirth = pDateOfBirth
        self.Intelligence = pIntelligence
        self.Speed = pSpeed

    #Part a(ii):
    def GetIntelligence(self):
        return self.Intelligence
    def GetName(self):
        return self.CharacterName
    
    #Part a(iii):
    def SetIntelligence(self, value):
        self.Intelligence = value

    #Part a(iv):
    def Learn(self):
        self.Intelligence = self.Intelligence + (self.Intelligence * (10/100))

    #Part a(v):
    def ReturnAge(self):
        age = 2023 - self.DateOfBirth.year
        return age
    
#Part b(i):
FirstCharacter = Character("Royal", date(2019,1,1), 70, 30)

#Part b(ii):
FirstCharacter.Learn()
print(f"Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()}, Intelligence: {FirstCharacter.GetIntelligence()}")

#Part c):
class MagicCharacter(Character):
    # self.Element : STRING
    def __init__(self, pCharacterName, pDateOfBirth, pIntelligence, pSpeed, pElement):
        super().__init__(pCharacterName, pDateOfBirth, pIntelligence, pSpeed)
        self.Element = pElement

    #Part c(ii):
    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
            super().SetIntelligence(self.GetIntelligence() * 1.2)
        if self.Intelligence == "earth":
            super().SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            super().Learn()
    
#Part d(i):
FirstMagic = MagicCharacter("Light", date(2018,3,3),75,22,"fire")

#Part d(ii):
FirstMagic.Learn()
print(f"Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()}, Intelligence: {FirstMagic.GetIntelligence()}")
