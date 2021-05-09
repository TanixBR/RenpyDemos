init python:

    class base_class(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()
        
        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    class player(base_class):
        ''' Player Class where we can init the player
        '''

        def __init__(self):
            self.money = 0
            self.money_max = 99999
            self.imagebase = "images/{}.png"

        def credit_money(self, amount):
            self.money += amount
            if self.money >= self.money_max:
                self.money = self.money_max
        
        def debit_money(self, amount):
            self.money -= amount
            if self.money < 0:
                self.money = 0


