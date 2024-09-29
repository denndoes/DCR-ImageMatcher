import os
import pymysql

# Algemene instellingen
CONFIG = {
    'language': 'en',  # Verander naar 'en' voor Engels of 'nl' voor Nederlands
    'db': {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'db': 'YOUR DATABSE NAME',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    },
    'paths': {
        'images_path': "change to your path/resources/[VORP]/[vorp_essentials]/vorp_inventory/html/img/items/",
        'server_scripts_path': "change to your path/resources",  # Pad naar je serverbestanden
        'log_directory': "change to your path/resources/DCR-ImageMatcher/log",  # Correcte pad naar de log directory
        'detailed_missing_images_log': 'change to your path/resources/DCR-ImageMatcher/log/detailed_missing_images_log.txt',
        'missing_images_log': 'change to your path/resources/DCR-ImageMatcher/log/missing_images_log.txt',
        'unused_images_log': 'C:/change to your path/resources/DCR-ImageMatcher/log/unused_images_log.txt'
    },
    'fuzzy_match_threshold': 90  # Pas de drempel aan voor fuzzy matching (0-100)
}

# Functie om de taalinstellingen uit lang.lua te laden
def get_language(language_code):
    lang_file = os.path.join(os.path.dirname(__file__), 'lang.lua')
    
    if not os.path.exists(lang_file):
        print("Lang file not found!")
        return {}
    
    language_settings = {}
    
    with open(lang_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        lang_start = False
        for line in lines:
            line = line.strip()
            if line.startswith(f'{language_code} = {{'):
                lang_start = True
                continue
            
            if lang_start:
                if line.startswith('}'):
                    break
                key_value = line.split('=', 1)
                if len(key_value) == 2:
                    key = key_value[0].strip().strip('"').strip("'")
                    value = key_value[1].strip().strip('"').strip("'").strip(',')
                    language_settings[key] = value
    
    return language_settings
