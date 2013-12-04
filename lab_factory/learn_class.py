class Superhero:
    """
    To make the variables of an object, we put __ in front of variables
    """
    __superhero_count = 0
    
    def __init__(self,name = "", hungry = False, tired = False):
        self.__name = name
        self.__hungry = hungry
        self.__tired = tired
        Superhero.__superhero_count += 1
    @staticmethod                           # To declare an empty item :D
    def get_superhero_count():
        return Superhero.__superhero_count
    #instance methods
    def mowGrass(self):
        print self.__name + " is mowing the grass."
        self.__tired = True
        self.__hungry = True
    
    def nap(self):
        print self.__name + " is taking a nap."
        self.__tired = False
        
    def eat(self, food):
        print self.__name + " is eating " + food + "."
        self.__hungry = False
    
    def throwParty(self, superhero, food):
        print self.__name + " is throwing a party for " + superhero.__name + "."
        self.eat(food)
        superhero.eat(food)
        
    def fly(self):
        print self.__name + " is flying."
        self.__tired = True
    
    def __str__(self):
        if self.__tired:
            tired_s = "tired"
        else:
            tired_s = "not tired"
        if self.__hungry:
            hungry_s = "hungry"
        else:
            hungry_s = "not hungry"
        
        return "%s is %s and %s" % (self.__name, tired_s, hungry_s )

def main():
    hulk = Superhero("The Hulk", True, False)
    print hulk
    hulk.mowGrass()
    print hulk
    hulk.eat("banana")
    print hulk
    hulk.nap()
    print hulk
    hulk.fly()
    print hulk
    superman = Superhero("The Superman", False, False )
    hulk.throwParty(superman,"lemon")
    print hulk
    print superman
    
if __name__=="__main__":
    main()
