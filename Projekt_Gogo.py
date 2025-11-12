## Author: Gogo
# Date: 12.11.2025

import random  # import random module
import time    # import time module

# German words
words = [
    "Katze", "Haus", "Blume", "Schule", "Fenster", "Auto", "Buch", "Tischtennis", "Stuhl", "Lampe",
    "Baum", "Wasser", "Feuer", "Luft", "Erde", "Mensch", "Tier", "Vogel", "Fisch", "Hund",
    "Apfel", "Banane", "Orange", "Traube", "Melone", "Kirsche", "Birne", "Pfirsich", "Zitrone", "Mango",
    "Sommer", "Winter", "Herbst", "Frühling", "Regen", "Sonne", "Mond", "Stern", "Wolke", "Himmel",
    "Berg", "Tal", "Fluss", "See", "Meer", "Insel", "Stadt", "Dorf", "Land", "Wald",
    "Brot", "Käse", "Milch", "Butter", "Eisen", "Fleisch", "Gemüse", "Obst", "Salat", "Zucker",
    "Salz", "Pfeffer", "Erdölraffinerie", "Essig", "Reis", "Nudel", "Pizza", "Burger", "Pommes", "Suppenlöffel",
    "Kuchen", "Torte", "Schokolade", "Bonbon", "Keks", "Eisberg", "Joghurt", "Quark", "Marmelade", "Honig",
    "Glas", "Tasse", "Becher", "Flasche", "Dose", "Topf", "Pfanne", "Löffel", "Gabel", "Messer",
    "Fensterbank", "Schreibtisch", "Computer", "Laptop", "Handy", "Tablet", "Bildschirm", "Tastatur", "Maus", "Drucker",
    "Bleistift", "Kugelschreiber", "Radiergummi", "Lineal", "Heft", "Buch", "Papier", "Ordner", "Mappe", "Stift",
    "Lehrer", "Schüler", "Klasse", "Schule", "Pause", "Stunde", "Fach", "Mathe", "Deutsch", "Englisch",
    "Sport", "Kunst", "Musik", "Biologie", "Chemie", "Physik", "Geschichte", "Geografie", "Religion", "Ethik",
    "Zug", "Bus", "Auto", "Fahrrad", "Roller", "Motorrad", "Flugzeug", "Schiff", "T-Rex", "Straßenbahn",
    "Ampel", "Strasse", "Kreuzung", "Brücke", "Tunnel", "Park", "Spielplatz", "Zoo", "Museum", "Bibliothek",
    "Bett", "Schrank", "Kommode", "Regal", "Spiegel", "Teppich", "Vorhang", "Kissen", "Decke", "Matratze",
    "Tür", "Fenster", "Wand", "Boden", "Decke", "Licht", "Steckdose", "Schalter", "Heizung", "Ventilator",
    "Uhr", "Kalender", "Foto", "Bild", "Poster", "Plakat", "Karte", "Reiseführer", "Broschüre", "Flyer", 
    "Donaudampfschifffahrtselektrizitätenhauptbetriebswerkbauunterbeamtengesellschaft", "Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz",
    "Jugendherberge", "Informatik", "Fussball", "Weltmeisterschaft", "Schifffahrt", "Radar"
]

# ask for player name
name = input("Wie heisst du? ")  # get player name
 
score = 0  # initialize score and updates it throughout game
used_words = []  # list to store used words, so they don't repeat

print("\nWillkommen zum Wort-Scramble Spiel,", name + "!")
print("Du hast 60 Sekunden pro Wort und 3 Versuche.\n")

# play 5 rounds
for round_num in range(1, 6): #loop for 5 rounds
    print("Runde", round_num)

    # choose random a new word
    word = random.choice(words)
    while word in used_words:
        word = random.choice(words)
    used_words.append(word)

    # scramble the word
    letters = list(word)
    random.shuffle(letters) # shuffle the letters
    scrambled = ''.join(letters)

    print("Dein Wort:", scrambled)

    tries = 3  # number of tries
    start_time = time.time()  # start timer

    while tries > 0:
        guess = input("Deine Antwort: ")

        # check time
        elapsed = time.time() - start_time
        if elapsed > 60: # when time is up the game ends
            print("Zeit abgelaufen!") 
            break

        if guess.lower() == word.lower():
            if tries == 3:
                score += 6  # first try
            elif tries == 2:
                score += 4  # second try
            else:
                score += 2  # third try
            print("Richtig!")
            break
        else:
            tries -= 1
            if tries > 0:
                print("Falsch! Versuche übrig:", tries) # tries it's a variable that says how many tries are left
            else:
                print("Verloren. Das Wort war:", word) # if no tries left the game ends

    print("Aktueller Punktestand:", score) # update score after every round
    print("-" * 30)

# show final score
print("\nSpiel beendet!")
print("Spieler:", name)
print("Gesamtpunktzahl:", score)

# simple leaderboard
leaderboard = {name: score}
print("\n Rangliste:")
for player, points in leaderboard.items():
    print(player + ":", points, "Punkte")
    