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
            """ Init of the Player

            The following attributes will be instantiated:
            iventory
            
            """
            self.player_name = "Player Name"     
            self.relationships = {}

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

