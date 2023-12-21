from domain.domainFilm import Film
from domain.domainClient import Client
from random import *

def generateRandomString(length):
    '''
    Functia va genera un string random de lungime specificata
    :param length: INT
    :return: STRING
    '''
    new_string = ""
    for _ in range(length):
        random_value = randint(ord('a') , ord('z'))
        new_string += random_value

    return new_string

def generateRandomCnp(length):
    '''
    Functia va genera un cnp random de lungime data
    :param length: INT
    :return: INT
    '''

    new_cnp = ""
    for _ in range(length):
        random_value = randint(ord('0') , ord('9'))
        new_cnp += random_value

    return new_cnp
