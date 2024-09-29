import os
import pymysql
from fuzzywuzzy import process
import sys
import multiprocessing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

# Taalconfiguratie laden
lang_settings = config.get_language(config.CONFIG['language'])

# Databaseconfiguratie
db_config = config.CONFIG['db']

def process_item(item_name, available_images):
    result = process.extractOne(item_name, available_images)
    if result:
        match = result[0]
        score = result[1]
        return (item_name, match + '.png', score)
    return (item_name, None, 0)

def main():
    # Verbinding maken met de database
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            print(lang_settings['fetching_items'])
            cursor.execute("SELECT item FROM items")
            items = [row['item'] for row in cursor.fetchall()]

        print(lang_settings['total_items_fetched'].format(len(items)))

        # Lijst van beschikbare afbeeldingen in de map
        available_images = [f.split('.')[0] for f in os.listdir(config.CONFIG['paths']['images_path']) if f.endswith('.png')]
        print(lang_settings['total_available_images'].format(len(available_images)))

        # Maak een set van beschikbare afbeeldingen voor snellere zoekacties
        available_images_set = set(available_images)

        # Controleren of plaatjes bestaan en fuzzy matchen
        matched_images = {}
        missing_images = []
        used_images = set()

        print(lang_settings['matching_images'])
        
        # Gebruik multiprocessing pool voor parallel verwerking
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = pool.starmap(process_item, [(item, available_images) for item in items])
        
        # Verwerk de resultaten
        for index, (item_name, matched, score) in enumerate(results):
            if matched and score > config.CONFIG['fuzzy_match_threshold']:
                matched_images[item_name] = matched
                used_images.add(matched.split('.')[0])
            else:
                missing_images.append(item_name)

            if index % 100 == 0:
                print(lang_settings['processing_item'].format(index, len(items)))

        pool.close()
        pool.join()

        # Ongebruikte afbeeldingen bepalen
        unused_images = available_images_set - used_images

        # Logdirectory instellen
        log_directory = os.path.join(os.path.dirname(__file__), '../log')
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Gedetailleerde ontbrekende plaatjes loggen
        detailed_log_path = os.path.join(log_directory, 'detailed_missing_images_log.txt')
        with open(detailed_log_path, 'w', encoding='utf-8') as detailed_log_file:
            detailed_log_file.write(lang_settings['detailed_missing_header'] + "\n")
            for item in missing_images:
                detailed_log_file.write(f"{item}\n")
        print(lang_settings['detailed_log_written'])

        # Simpele ontbrekende plaatjes loggen
        missing_log_path = os.path.join(log_directory, 'missing_images_log.txt')
        with open(missing_log_path, 'w', encoding='utf-8') as missing_log_file:
            missing_log_file.write(lang_settings['missing_images_header'] + "\n")
            for item in missing_images:
                missing_log_file.write(f"{item}\n")
        print(lang_settings['missing_log_written'])

        # Loggen van ongebruikte afbeeldingen
        unused_log_path = os.path.join(log_directory, 'unused_images_log.txt')
        with open(unused_log_path, 'w', encoding='utf-8') as unused_log_file:
            unused_log_file.write(lang_settings['unused_images_header'] + "\n")
            for image in unused_images:
                unused_log_file.write(f"{image}.png\n")
        print(lang_settings['unused_log_written'])

    finally:
        connection.close()
        print(lang_settings['connection_closed'])

if __name__ == "__main__":
    main()
