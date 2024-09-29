# DCR Image Matcher

The DCR Image Matcher is a tool designed to verify if images for items used in your server are present in your inventory. It connects to your database to retrieve a list of item names and compares them to the available image files.

## Features
- Retrieves item names from your database
- Matches item names with image files using fuzzy matching
- Generates logs for missing images, detailed missing items, and unused images

## Requirements
- Python 3.x
- Required Python libraries (install using `pip install -r requirements.txt`)

## Setup

1. Place the DCR-ImageMatcher folder in your desired location.
2. Edit the `config.py` file to configure your database settings and file paths.
3. Add your language settings in `lang.lua`. Choose between English (`en`) and Dutch (`nl`).
4. Make sure you have placed all required Python libraries (see `requirements.txt`).

## Running the Script
Navigate to the `scripts` folder and run:

```bash
python logboek.py
```

## License
This project is licensed under the MIT License.




-----------------------------------------------------------------------------------------------------------------------------------------------------------
# NEDERLANDS!

# DCR Image Matcher

De DCR Image Matcher is een hulpmiddel ontworpen om te controleren of afbeeldingen voor items die in je server worden gebruikt, aanwezig zijn in je inventory. Het maakt verbinding met je database om een lijst met itemnamen op te halen en vergelijkt deze met de beschikbare afbeeldingsbestanden.

## Functies
- Haalt itemnamen op uit je database
- Vergelijkt itemnamen met afbeeldingsbestanden met behulp van fuzzy matching
- Genereert logs voor ontbrekende afbeeldingen, gedetailleerde ontbrekende items en ongebruikte afbeeldingen

## Vereisten
- Python 3.x
- Vereiste Python-bibliotheken (installeer met `pip install -r requirements.txt`)

## Installatie

1. Plaats de DCR-ImageMatcher map op de gewenste locatie.
2. Bewerk het `config.py` bestand om je database-instellingen en bestandslocaties in te stellen.
3. Voeg je taalinstellingen toe in `lang.lua`. Kies tussen Engels (`en`) en Nederlands (`nl`).
4. Zorg ervoor dat je alle vereiste Python-bibliotheken hebt geïnstalleerd (zie `requirements.txt`).

## Script Uitvoeren
Navigeer naar de `scripts` map en voer uit:

```bash
python logboek.py
```

## Licentie
Dit project valt onder de MIT-licentie.
