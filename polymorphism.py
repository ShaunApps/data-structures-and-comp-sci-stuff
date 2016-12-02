class Character():

    def __init__(self, name, gender):
        self.__name = name
        self.gender = gender

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender


class Warrior(Character):

    def __init__(self, name, gender, weapon_type):
        # Python 3 syntax
        super().__init__(name, gender)
        self.__weapon_type = weapon_type

    def getDescription(self):
        return self.getGender() + " Warrior " + self.getName() + " with " + self.__weapon_type + " weapon."



s = Warrior("Jim", "Male", "Offensive")
print(s.getDescription())
