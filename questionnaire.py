
import json
import sys


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def fromjsondata(data):
        # Transforme les données choix tuple (titre, bool "bonne réponse") => [choix 1, choix2...]
        choix = [i[0] for i in data["choix"]]
        # Trouve le bon choix en fonction du bool "bonne réponse"
        bonne_reponse = [i[0] for i in data["choix"] if i[1]]
        # Si aucune bonne réponse ou plusieurs bonnes réponse -> Anomalie dans les données
        if len(bonne_reponse) != 1 :
            return None
        q = Question(data["titre"], choix, bonne_reponse[0])
        return q

    def poser(self, num_question, nb_questions):
        print(f"QUESTION N° {num_question}/{nb_questions}")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions, categorie, titre, difficulte):
        self.questions = questions
        self.categorie = categorie
        self.titre = titre
        self.difficulte = difficulte
        
    def fromjsondata(data):

        # Si le fichier Json n'a pas de questions, arrêt du questionnaire par None    
        if not data.get("questions"):
            return None    

        questionnaire_data_questions = data["questions"]
        questions = [Question.fromjsondata(i) for i in questionnaire_data_questions]
        # Supprime les questions None (qui n'ont pas pu être créées)
        questions = [i for i in questions if i]
        
        # Si le fichier Json n'a pas de catégorie ou de difficulté, donnée mise à "inconnue"
        if not data.get("categorie"):
            data["categorie"] = "inconnue"
            
        if not data.get("difficulte"):
            data["difficulte"] = "inconnue"
        
        # Si le fichier Json n'a pas de titre, arrêt du questionnaire par None    
        if not data.get("titre"):
            return None    

        return Questionnaire(questions, data['categorie'], data['titre'], data['difficulte'])
        
    def from_json_file(filename):
        try:
            file = open(filename, "r")
            json_data = file.read()
            file.close()
            questionnaire_data = json.loads(json_data)
        except:
            print("ERREUR: Exception lors de l'ouverture ou la lecture du fichier")
            return None
        return Questionnaire.fromjsondata(questionnaire_data)

    def lancer(self):
        score = 0
        nb_questions = len(self.questions)
        print("Questionnaire: " + self.titre)
        print("Catégorie: " + self.categorie)
        print("Difficulté: " + self.difficulte)
        print("Nombre de questions: " + str(nb_questions))
        print()
        
        for i in range(nb_questions):
            question = self.questions[i]
            if question.poser(i+1, nb_questions):
                score += 1
        print("Score final :", score, "sur", nb_questions)
        return score

if __name__ == "__main__":
    # Questionnaire.from_json_file("animaux_leschats_debutant.json").lancer()

    if len(sys.argv) < 2:
        print("ERREUR: Vous devez spécifier le nom du fichier à charger")
        exit(0)

    json_filename = sys.argv[1]
    questionnaire = Questionnaire.from_json_file(json_filename)

    if questionnaire:
        questionnaire.lancer()

