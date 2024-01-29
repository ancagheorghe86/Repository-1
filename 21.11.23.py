'''Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba
(exemplu `input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa)
numita get_translator(language) – in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')

'''
from abc import ABC, abstractmethod


# clasa abstracta
class Translator(ABC):
    @abstractmethod
    def localize(self, ro_word):
        raise NotImplementedError


class EnglishTranslator(Translator):
    translations = {
        "masina": "car"
    }

    def localize(self, ro_word):
        """
        cauta ro_word (cheia) in dictionarul self.translations. daca exista
        returneaza valoarea corespunzatoare
        :param ro_word: cuvant in limba romana
        :return: none daca nu exista traducerea lui | traducerea lui
        """
        if ro_word in self.translations:
            return self.translations[ro_word]
        else:
            return None


class SpanishTranslator(Translator):
    translations = {
        "masina": "coce"
    }

    def localize(self, ro_word):
        if ro_word in self.translations:
            return self.translations[ro_word]
        else:
            return None


class FrenchTranslator(Translator):
    translations = {
        "masina": "voiture"
    }

    def localize(self, ro_word):
        if ro_word in self.translations:
            return self.translations[ro_word]
        else:
            return None

language = input("introdu limba: ")
if language == "en":
    en_tr = EnglishTranslator()
    response = en_tr.localize("masina")
    print(response)
elif language == "sp":
    sp_tr = SpanishTranslator()
    response = sp_tr.localize("masina")
    print(response)
elif language == "fr":
    fr_tr = FrenchTranslator()
    response = fr_tr.localize("masina")
    print(response)
else:
    print("dictionary not implemented")

class TranslatorFactory:
    @staticmethod
    def get_translator(language):
        if language == "en":
            en_tr = EnglishTranslator()
            return en_tr
        elif language == "sp":
            sp_tr = SpanishTranslator()
            return sp_tr
        elif language == "fr":
            fr_tr = FrenchTranslator()
            return fr_tr
        else:
            print("dictionary not implemented")


en_tr = TranslatorFactory.get_translator("en")
sp_tr = TranslatorFactory.get_translator("sp")
fr_tr = TranslatorFactory.get_translator("fr")
print(f'In engleza zicem {en_tr.localize("masina")}')
print(f'In spaniola zicem {sp_tr.localize("masina")}')
print(f'In franceza zicem {fr_tr.localize("masina")}')


'''HTTP. Rest APIs. Requests


Folosim Simple Books API, descris aici : https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client. Pentru testare se va crea un obiect din aceasta clasa și se vor apela metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token (fa asta in constructor, client name si email ar trebui sa fie atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.


3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.
'''


