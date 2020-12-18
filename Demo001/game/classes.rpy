init python:

    import os
    import base64

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
            self.end_flag = 0

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

        def check_savefile(self, savefile):
            return os.path.isfile("{}/{}".format(config.gamedir,savefile))

        def create_file(self, savefile):
            with open("{}/{}".format(config.gamedir,savefile), 'w') as fp: 
                pass
            return True

    class game_core(base_class):
        ''' Game Core class
        '''

        def __init__(self):
            ''' Init game Core
            '''
            self.item_list = self.load_data("gamedata.save")            
            self.items = {}
            self.initItems()
            #private
            self.url = "http://localhost"

        def initItems(self):
            for i in self.getItems():
                self.items[i["name"]]={"name":i["name"],"type":i["type"], "value":i["default_value"],"image":i["image"]}

        def getItems(self):
            return self.item_list["Inventory"]

        def getItemNames(self):
            names = []
            for i in self.getItems():
                names.append(i["name"])
            return names

        def getItemAttribute(self,iname,attribute):
            return self.items[iname][attribute]

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