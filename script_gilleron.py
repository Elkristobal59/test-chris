import sys # Utile pour quitter proprement en cas de succès

class Question:
    """Représente une seule question de quiz avec sa logique de tentatives."""

    def __init__(self, texte, reponse_attendue, max_tentatives=3):
        """Initialise la question avec son texte et sa réponse."""
        self.texte = texte
        self.reponse_attendue = reponse_attendue.lower()
        self.max_tentatives = max_tentatives
        self.tentatives_actuelles = 0
        self.reussie = False

    def poser(self, numero_question):
        """Pose la question à l'utilisateur et gère les tentatives."""
        print(f"\n--- Question {numero_question} ---")
        print(f"Question {numero_question} : {self.texte}")
        
        while self.tentatives_actuelles < self.max_tentatives:
            # 1. Demande la réponse
            reponse_utilisateur = input(
                f"Tentative {self.tentatives_actuelles + 1}/{self.max_tentatives}. Votre réponse : "
            )
            print(f"Your answer : {reponse_utilisateur}")
            
            # Normalise la réponse pour la vérification (comme dans votre question 3)
            reponse_utilisateur_normalisee = reponse_utilisateur.lower()

            # 2. Vérifie la réponse
            if reponse_utilisateur_normalisee == self.reponse_attendue:
                print("Good job! This is the right answer")
                self.reussie = True
                return True # Réponse correcte
            else:
                print("Too bad! That is not the correct answer")
                self.tentatives_actuelles += 1

        # Si la boucle est terminée sans succès (tentatives épuisées)
        print(f"Dommage ! La bonne réponse était {self.reponse_attendue.capitalize()}.")
        return False # Échec de la question

class Quiz:
    """Gère l'ensemble du quiz et la séquence des questions."""

    def __init__(self, titre="Notre super Quiz !"):
        """Initialise le quiz avec une liste de questions vide."""
        self.titre = titre
        self.questions = []
        self.score = 0

    def ajouter_question(self, question):
        """Ajoute un objet Question à la liste du quiz."""
        self.questions.append(question)

    def demarrer(self):
        """Exécute toutes les questions du quiz."""
        print(f"Here you have {self.titre}")
        
        for i, question in enumerate(self.questions):
            # i est l'index (commence à 0), donc on utilise i + 1 pour le numéro de question
            if question.poser(i + 1):
                self.score += 1
        
        # Affichage du résultat final
        print("\n" + "="*20)
        print("Congratulations! You have completed the quiz!")
        print(f"Votre score final est de {self.score} sur {len(self.questions)}.")
        print("="*20)

# --- Création du Quiz et des Questions ---

# 1. Créer une instance du Quiz
mon_quiz = Quiz()

# 2. Créer les instances des Questions
# Note : Nous n'avons plus besoin de répéter le même code pour chaque question.
q1 = Question("Quelle est la racine carré de 4 ?", "2")
q2 = Question("Année de création d'Apple ?", "1976")
q3 = Question("Quel est le nom du créateur principal de TESLA? ", "elon musk") # La gestion de la casse est faite dans la classe Question

# 3. Ajouter les questions au Quiz
mon_quiz.ajouter_question(q1)
mon_quiz.ajouter_question(q2)
mon_quiz.ajouter_question(q3)

# 4. Démarrer le Quiz
mon_quiz.demarrer()