init python:

################################################################################
## System Vars and imports
################################################################################

    #Developer Mode
    config.developer = True
    #Regular Imports
    import logging
    import requests
    import json
    import sys
    import os.path
    import base64

    logging.basicConfig(filename=f"{config.gamedir}/gamelog.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S',
                    level=logging.DEBUG)

    logging.info("INIT VARS")

################################################################################
## Game Classes
################################################################################

    class base_class(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()
        
        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    class GameCore(base_class):
        ''' Game Core Class where we can init the game
        '''

        def __init__(self):
            """ init Core Class

            """
            self.config_file = f"{config.gamedir}/data.json"
            self.do_login = True
            self.local_data = None
            self.player_name = "MyPlayer"
            self.player_energy = 0
            self.player_money = 0
            self.player_xp = 0
            self.player_level = 1
            self.load_ref()

        def load_ref(self):
            if os.path.exists(self.config_file):
                with open(self.config_file) as json_file:
                    self.local_data = json.load(json_file)
                    return True
            else:
                return False

        def json_request(r_url, r_params, r_json):
            return requests.post(r_url, params=r_params, json=r_json)

        def login(passcode):
            login_url = self.local_data["services"]["login"]["url"]
            params = self.local_data["services"]["login"]["params"]
            login_key = self.dec_data(self.local_data["services"]["login"]["key"])
            login_input = {"key":login_key, "passcode":passcode}
            response = self.json_request(login_url, params, login_input)
            if response.status_code == 200:
                logging.info(response.text)
                return response.text
            else:
                logging.info(f"Fail to Login: {response}")
                return False

        def enc_data(self,inputData):
            return base64.b64encode(inputData)

        def dec_data(self,inputData):
            return base64.b64decode(inputData)


        def do_request(self, r_url, r_params, r_json):
            return requests.post(r_url, params=r_params, json=r_json)

        def get_daytime(self):
            return self.daytime_ref[self.daytime]

        def next_daytime(self):
            self.daytime += 1
            if self.daytime > 3:
                self.daytime = 0
                self.days += 1

        def get_missions(self):
            rank = self.get_attr("rank")
            missions_byrank = []
            for i in self.missions:
                if int(i["rank"]) == rank:
                    missions_byrank.append(i)
            return missions_byrank

        def get_mission_members(self,mission):
            return self.mission["members"]

        def get_required_npc(self,mission):
            return self.mission["required_npc"]

        def get_consumption(self,mission):
            return self.get_consumption_byid(mission["consumption_id"])

        def get_mission_reward(self,mission,stats):
            for m_attr, m_value in mission["stats"].items():
                if m_attr in stats:
                    if m_value <= stats[m_attr]:
                        stats_ok = True
                    else:
                        stats_ok = False
                else:
                    stats_ok = False
                    break
            if stats_ok:
                return mission["gold"],mission["stars"]
            else:
                return None

        def get_consumption_byid(self,consumption_id):
            return self.consumption[consumption_id]

        def get_npc(self,npc_id):
            return self.npc_list[npc_id]

        def get_nextnpc(self,npc_id):
            npc_id += 1
            if len(self.npc_list) == npc_id:
                npc_id = 0
            return npc_id

        def get_prevnpc(self,npc_id):
            npc_id -= 1
            if npc_id < 0:
                npc_id = (len(self.npc_list)-1)
            return npc_id

        def consume_energy(self, energy):
            energy_status = self.attributes["energy"] - energy
            if energy_status >= 0:
                self.attributes["energy"] = energy_status
                return True
            else:
                return False

        def depart(self, mission):
            if self.consume_energy(int(mission["consumption_id"])):
                self.running_quests.append(mission)
                self.quest_status = "Success"
            else:
                self.quest_status = "Energy"

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

################################################################################
## Game Objects
################################################################################

    logging.info("INIT GAME OBJECTS")
    logging.info("Creating Game Core")
    game_core = GameCore()
    logging.info("VARIABLES")
    pref_menu = False
    help_menu = False

################################################################################
## Functions
################################################################################

    logging.info("INIT FUNCTION")


################################################################################
## IMAGES and Videos
################################################################################


#Main Video Launch
image main_video = Movie(play="videos/oa4_launch.webm", pos=(0, 0), anchor=(0, 0), size=(1900, 1080), channel='movie')

################################################################################
## Transformation
################################################################################

transform zoom1:
    ease 1.0 zoom 1.04 rotate -3
    ease 1.0 zoom 1.0 rotate 3
    repeat
transform zoom2:
    ease 0.7 zoom 1.07 rotate -2
    ease 0.7 zoom 1.0 rotate 2
    repeat
transform zoom3:
    ease 0.7 zoom 1.07 rotate 1
    ease 0.7 zoom 1.0 rotate -1
    repeat
