print("Here you have our quiz !")
print("\n-------")

# --- Question 1 ---
question_1 = "Quelle est la racine carré de 4 ? "
reponse_1 = "2"
tentatives = 0
max_tentatives = 3


print(f"Question 1 : {question_1}")

while tentatives < max_tentatives:
    # 1. On demande la réponse et on compte l'essai
    reponse_utilisateur_1 = input(f"Tentative {tentatives + 1}/{max_tentatives}. Votre réponse : ")
    print(f"Your answer : {reponse_utilisateur_1}")
    
    # 2. Vérification de la réponse
    if reponse_utilisateur_1 == reponse_1:
        print("Good job! This is the right answer")
        break  # Sort de la boucle si la réponse est correcte
    else:
        print("Too bad! That is not the correct answer")
        tentatives += 1  # Incrémente le compteur seulement si la réponse est fausse

# Message si le joueur a échoué (uniquement si le compteur est à 3)
if tentatives == max_tentatives and reponse_utilisateur_1 != reponse_1:
    print(f"Dommage ! La bonne réponse était {reponse_1}.")


# --- Question 2 ---
print("\n-------")
question_2 = "Année de création d'Apple ? "
reponse_2 = "1976"
tentatives = 0
max_tentatives = 3

print(f"Question 2 : {question_2}")

while tentatives < max_tentatives:
    reponse_utilisateur_2 = input(f"Tentative {tentatives + 1}/{max_tentatives}. Votre réponse : ")
    print(f"Your answer : {reponse_utilisateur_2}")

    if reponse_utilisateur_2 == reponse_2:
        print("Good job! This is the right answer")
        break
    else:
        print("Too bad! That is not the correct answer")
        tentatives += 1

if tentatives == max_tentatives and reponse_utilisateur_2 != reponse_2:
    print(f"Dommage ! La bonne réponse était {reponse_2}.")


# --- Question 3 ---

print("\n-------")
question_3 = "Quel est le nom du créateur principal de TESLA? "
reponse_3 = "elon musk"
tentatives = 0
max_tentatives = 3

print(f"Question 3 : {question_3}")

while tentatives < max_tentatives:
    reponse_utilisateur_3 = input(f"Tentative {tentatives + 1}/{max_tentatives}. Votre réponse : ")
    reponse_utilisateur_3_lower = reponse_utilisateur_3.lower()
    print(f"Your answer : {reponse_utilisateur_3_lower}")

    # Vérification avec .lower() et OR pour deux réponses possibles
    if reponse_utilisateur_3_lower == reponse_3:
        print("Good job! This is the right answer")
        break
    else:
        print("Too bad! That is not the correct answer")
        tentatives += 1

if tentatives == max_tentatives and reponse_utilisateur_3_lower != reponse_3:
    print(f"Dommage ! La bonne réponse était {reponse_3}.")

print("\n-------")
print("Congratulations! You have completed the quiz!")