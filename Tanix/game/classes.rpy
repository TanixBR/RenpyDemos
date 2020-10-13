init python:

    import json
    import os.path
    import base64
    import os

    class base_class(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()
        
        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    class player(base_class):
        ''' Player Class where we can init the player
        '''

        def __init__(self):
            """ Init of the Player

            The following attributes will be instantiated:
            iventory
            
            """
            self.player_name = "Player Name"
            self.items = []     
            self.relationships = {}
            self.winner = None

        def addRelationship(self, character):
            ''' 
            Add one relationship to list
            '''
            self.updateRelationship(character, 0)

        def increaseRelationship(self, character, value):
            '''
            Increment Relationship
            '''
            self.relationships[character] += value
            self.checkWinner()
        
        def getRelationship(self, character):
            '''
            Get Relationship
            '''
            return self.relationships[character]
        
        def updateRelationship(self, character, value):
            '''
            Update one Relationship from the list
            '''
            self.relationships[character] = value
            self.checkWinner()
        
        def checkWinner(self):
            temp = 0
            self.winner = None            
            for key, value in self.relationships.items():                
                if value >= temp:
                    self.winner = key
                temp = value

    class inventory(base_class):
            ''' Iventory Class where inventory is defined
            '''

            def __init__(self):
                ''' Init Iventory
                    set items attribute
                '''
                self.items = []

            def addItem(self, item):
                ''' Add one item to the list
                '''
                self.items.append(item)

            def useItem(self, item):
                ''' Pop one item from the list
                
                Return the item that it's pop
                Return False if there is no item in the list
                '''
                if item in self.items:
                    self.items.remove(item)
                    return True
                else:
                    return False

            def checkItems(self, item):
                ''' Pop one item from the list
                
                Return the item that it's pop
                Return False if there is no item in the list
                '''
                if item in self.items:            
                    return True
                else:
                    return False

            def listItems(self):
                ''' 
                Return All item from list
                '''
                return self.items

    class base_item(base_class):
        ''' Item Class that holds item caracteristics
        '''
        def __init__(self, name, type, default_value, image):
            ''' Init items attribute
            '''
            self.name = None
            self.type = None
            self.default_value = None
            self.image = None
            self.max = 1
            self.quantity = None
            self.value = None

        def getName():
            return self.name

        def getType():
            return self.type

    class game_core(base_class):
        ''' Game Core class
        '''

        def __init__(self):
            ''' Init game Core
            '''
            self.item_list = self.load_data("gamedata.save")            
            self.items = []
            self.initItems()

        def initItems(self):
            for i in self.getItems():
                self.items.append(base_item(i["name"], i["type"], i["default_value"], i["image"]))

        def getItems(self):
            return self.item_list["Inventory"]

        def getItemNames(self):
            names = []
            for i in self.getItems():
                names.append(i["name"])
            return names

        def enc_data(self,inputData):
            return base64.b64encode(inputData)
        
        def dec_data(self,inputData):
            return base64.b64decode(inputData)

        def load_data(self,file_name):
            with open("{}/{}".format(config.gamedir,file_name), 'rb') as f:
                fileData = f.read()
            return json.loads(self.dec_data(fileData).decode("utf-8"))
        
        def save_data(self,content):
            with open(self.save_name, 'wb') as f:
                f.write(self.enc_data(content))    


