# import time
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# another_list = [11 , 12, 13, 14, 15, 16, 17, 18, 19, 20]
# my_iterator = iter(my_list)
# another_iterator = iter(another_list)
#
# #
# # print(next(my_iterator)) #[2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(next(my_iterator)) #[3, 4, 5, 6, 7, 8, 9, 10]
# # print(next(my_iterator)) #[4, 5, 6, 7, 8, 9, 10]
# # print(next(my_iterator)) #[5, 6, 7, 8, 9, 10]
# # print(next(my_iterator)) #[6, 7, 8, 9, 10]
# # print(next(my_iterator)) #[7, 8, 9, 10]
# # print(next(my_iterator)) #[8, 9, 10]
# # print(next(my_iterator)) #[9, 10]
# # print(next(my_iterator)) #[10]
# # print(next(my_iterator), list(my_iterator))# []
#
# for e1, e2 in zip(my_iterator, another_iterator):
#     print(e1, e2)
# print(list(my_iterator), list(another_iterator))
#
#
# my_iterator = iter(my_list)
# another_iterator = iter(another_list)
# while True:
#     try:
#         print(next(my_iterator), next(another_iterator))
#         time.sleep(1)
#     except StopIteration:
#         print("Am terminat de iterat")
#         break

def require_login(functia_originala):
    @wraps
    def wrapper(self, *args, **kwargs):
        if seld.__este_logat == True:
            result = functia_originala(*args, **kwargs)
            return result
        else:
            print("Userul nu este logat")

class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.__parola = parola  #atribut privat: self.__parola = parola; se pun doua __ pentru a-l face privat
        self.__data_nasterii = data_nasterii
        self.__este_logat = False

    def login(self, email, parola):
        """
        o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
        :param email: 
        :param parola: 
        :return: 
        """

        if email == self.email and parola == self.__parola:
            self.__este_logat == True
            print("Userul nu este logat")

    def logout(self):
        self.__este_logat = False

    def get_info(self):
        if self.__este_logat == True:
            print(self.nume, self.email, self.__data_nasterii)
        else:
            print("userul nu este logat")

''' valorile date ca parametru clasei se vor duce in "self-ul" fiecarei instante (user1, user2)'''
user1 = User("asd", "asd@email.com", "asddd", "2 ianuarie 1991")
user2 = User("ert", "ert@email.com", "erttt", "2 ianuarie 1991")
user1.login("asd@email.com", "asddd")

import time
from functools import wraps

def logger(functia_originala):
    @wraps(functia_originala)
    def wrapper(args, **kwargs):
        result = functia_originala(args, kwargs)
        return result, args, kwargs
    return wrapper

def timeit(functia_originala):
    @wraps(functia_originala)
    def wrapper(*args, kwargs):
        t1 = time.time()
        result = functia_originala(*args, **kwargs)
        t2 = time.time() - t1
        print(t2)
        return result
    return wrapper

@logger
def calculate(a, b):
    return a + b

print(calculate(2,4))