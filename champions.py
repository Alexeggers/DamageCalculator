# Imports
import requests, json


api_key = "f374ec42-d082-4287-aaf1-7e4552aca866"
champ_request_url = "https://global.api.pvp.net/api/lol/" \
                    "static-data/euw/v1.2/champion/"
champion_list = {
    'Morgana': 25,
    'Urgot': 6,
    'Kayle': 10,
    'Volibear': 106,
    'Gragas': 79,
    'MonkeyKing': 62,
    'Jayce': 126,
    'Ezreal': 81,
    'Velkoz': 161,
    'TwistedFate': 4,
    'Amumu': 32,
    'Annie': 1,
    'Zed': 238,
    'Janna': 40,
    'Heimerdinger': 74,
    'Corki': 42,
    'Bard': 432,
    'Fiora': 114,
    'Zilean': 26,
    'JarvanIV': 59,
    'Shen': 98,
    'Ryze': 13,
    'Rammus': 33,
    'Skarner': 72,
    'Shaco': 35,
    'Nunu': 20,
    'Azir': 268,
    'FiddleSticks': 9,
    'Ekko': 245,
    'Pantheon': 80,
    'XinZhao': 5,
    'Diana': 131,
    'Ziggs': 115,
    'Udyr': 77,
    'Syndra': 134,
    'Chogath': 31,
    'Garen': 86,
    'Gnar': 150,
    'Vi': 254,
    'Nautilus': 111,
    'Taric': 44,
    'Jinx': 222,
    'Gangplank': 41,
    'Lucian': 236,
    'Kled': 240,
    'Malzahar': 90,
    'Nasus': 75,
    'AurelionSol': 136,
    'Khazix': 121,
    'Viktor': 112,
    'Vladimir': 8,
    'Cassiopeia': 69,
    'Thresh': 412,
    'Poppy': 78,
    'Lissandra': 127,
    'Akali': 84,
    'Yasuo': 157,
    'Kassadin': 38,
    'LeeSin': 64,
    'MissFortune': 21,
    'Lulu': 117,
    'Malphite': 54,
    'Taliyah': 163,
    'DrMundo': 36,
    'Trundle': 48,
    'Quinn': 133,
    'Zac': 154,
    'Shyvana': 102,
    'Kindred': 203,
    'Tristana': 18,
    'Teemo': 17,
    'Ivern': 427,
    'Nidalee': 76,
    'Riven': 92,
    'Vayne': 67,
    'Talon': 91,
    'Sivir': 15,
    'Brand': 63,
    'Draven': 119,
    'Twitch': 29,
    'Leona': 89,
    'TahmKench': 223,
    'Ashe': 22,
    'Karthus': 30,
    'Sejuani': 113,
    'Xerath': 101,
    'Darius': 122,
    'Braum': 201,
    'Karma': 43,
    'Zyra': 143,
    'MasterYi': 11,
    'Anivia': 34,
    'Galio': 3,
    'Rengar': 107,
    'Jhin': 202,
    'Elise': 60,
    'Sona': 37,
    'Ahri': 103,
    'Veigar': 45,
    'Lux': 99,
    'Sion': 14,
    'Hecarim': 120,
    'Singed': 27,
    'Irelia': 39,
    'RekSai': 421,
    'Nocturne': 56,
    'Illaoi': 420,
    'Jax': 24,
    'KogMaw': 96,
    'Kalista': 429,
    'Tryndamere': 23,
    'Soraka': 16,
    'Mordekaiser': 82,
    'Caitlyn': 51,
    'Renekton': 58,
    'Rumble': 68,
    'Kennen': 85,
    'Swain': 50,
    'Aatrox': 266,
    'Leblanc': 7,
    'Evelynn': 28,
    'Maokai': 57,
    'Orianna': 61,
    'Graves': 104,
    'Olaf': 2,
    'Varus': 110,
    'Fizz': 105,
    'Nami': 267,
    'Katarina': 55,
    'Warwick': 19,
    'Yorick': 83,
    'Alistar': 12,
    'Blitzcrank': 53}


class Champion:
    '''Represents a champion in LoL
    who has spells and stats.'''

    def __init__(self, name, level = 1):
        self.name = name
        self.id = champion_list[name]
        self.spells = self.get_spells()
        self.stats = self.get_stats()
        self.level = level

    def get_api_json(self, type):
        '''Makes a request to the RIOT api with the given type
        (usually spells or stats) and returns a json object.
        '''
        url = champ_request_url + str(self.id) + "?champData=" + type + \
              "&api_key=" + api_key
        dto = requests.get(url)
        return json.loads(dto.text)

    def get_spells(self):
        '''Gets the champion's stats from the RIOT api.'''
        # Keyword: "spells"
        json = self.get_api_json("spells")

        raise NotImplementedError

    def get_stats(self):
        '''Gets the champion's stats from the RIOT api.'''
        # Keyword: "stats"
        json = self.get_api_json("stats")

        raise NotImplementedError