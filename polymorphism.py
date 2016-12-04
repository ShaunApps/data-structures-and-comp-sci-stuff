class Character(object):  # remove 'object' argument for Python 3

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender


class Paladin(Character):

    # # Python 3 syntax
    # def __init__(self, name, gender, weapon_type):
    #     super().__init__(name, gender)
    #     self.__weapon_type = weapon_type

    # Python 2 syntax
    def __init__(self, name, gender, weapon_type):
        super(Paladin, self).__init__(name, gender)
        self.__weapon_type = weapon_type

    def getDescription(self):
        return self.getGender() + " Paladin " + self.getName() + " with " + self.__weapon_type + "-type weapon."


c = Paladin("Tim", "Male", "Defensive")
print c.getDescription()
print c.getName()
