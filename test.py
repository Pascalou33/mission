import os
import unittest
from unittest.mock import patch
import questionnaire


class TestQuestion(unittest.TestCase):
    def test_bonne_mauvaise_reponse(self):
        choix =("choix1", "choix2", "choix3")
        q = questionnaire.Question("titre_question", choix, "choix2")
        with patch("builtins.input", return_value="1"):
            self.assertFalse(q.poser(1, 1)) 
        with patch("builtins.input", return_value="2"):
            self.assertTrue(q.poser(1, 1))
        with patch("builtins.input", return_value="3"):
            self.assertFalse(q.poser(1, 1)) 


class TestQuestionnaire(unittest.TestCase):
    def test_questionnaire_lancer_alien_debutant(self):
        filename = os.path.join("test_data", "cinema_alien_debutant.json")
        q =questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNotNone(q)
        # Nombre de questions
        self.assertEqual(len(q.questions),10)
        # titre, categorie, difficulte
        self.assertEqual(q.titre, "Alien")
        self.assertEqual(q.categorie, "Cinéma")
        self.assertEqual(q.difficulte, "débutant")
        # patcher le input => forcer de répondre toujours à 1 score = 4
        with patch("builtins.input", return_value="1"):
            self.assertEqual(q.lancer(), 1)
    
    def test_questionnaire_format_invalide(self):
        filename = os.path.join("test_data", "format_invalide1.json")
        q =questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNotNone(q)
        self.assertEqual(q.categorie, "inconnue")
        self.assertEqual(q.difficulte, "inconnue")
        self.assertIsNotNone(q.questions)

        filename = os.path.join("test_data", "format_invalide2.json")
        q =questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNone(q)

        filename = os.path.join("test_data", "format_invalide3.json")
        q =questionnaire.Questionnaire.from_json_file(filename)
        self.assertIsNone(q)       
               

unittest.main()






