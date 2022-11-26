## Codigo obtenido de: https://unipython.com/juego-python-ahorcado/
## Mis aportaciones:
##      Hice que las palabras usadas las tomara del archivo words y no de la lista que venia por default
##      Lo cambie a ingles para qeu se viera mas placoson (Menos los mensajes)
##      Hice que la palabra oculta y las letras usadas se mostraran en una sola linea
##      Hice que al ganar se muestre la palabra completa en los espacios (_) antes se mostraba que ganaba, pero no la ultima letra


import random
from words import words

HANGMAN = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def ChooseRandomWord(words):
    # Funcion que regresa una palabra al azar del archivo words
    randWord = '-'
    while '-' in randWord or ' ' in randWord:
        randWord = random.choice(words)
    return randWord.lower()

def displayBoard(HANGMAN, mistakes, success, word):
    print(HANGMAN[len(mistakes)])
    print ("")
    end = " "
    print ('Letras incorrectas: ', mistakes)
    spaces = '_' * len(word) 
    for i in range(len(word)): # Remplaza los espacios en blanco por la letra bien escrita
        if word[i] in success:
            spaces = spaces[:i] + word[i] + spaces[i+1:]
    print (spaces)
    print ("")
 
def chooseLetter(anyLetter):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letter = input()
        letter = letter.lower()
        if len(letter) != 1:
            print ('Introduce una sola letra.') 
        elif letter in anyLetter:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letter
 
def start():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')
 
print ('H A N G M A N')
mistakes = ""
success = ""
word = ChooseRandomWord(words)
endgame = False
while True:
    displayBoard(HANGMAN, mistakes, success, word)
    # El usuairo elije una letra.
    letter = chooseLetter(mistakes + success)
    if letter in word:
        success = success + letter
        # Se fija si el jugador ganó
        victory = True
        for i in range(len(word)):
            if word[i] not in success:
                victory = False
                break
        if victory:
            displayBoard(HANGMAN, mistakes, success, word)
            print ('¡Muy bien! La palabra secreta es "' + word.upper() + '"! ¡Has ganado!')
            endgame = True
    else:
        mistakes = mistakes + letter
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(mistakes) == len(HANGMAN) - 1:
            displayBoard(HANGMAN, mistakes, success, word)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(mistakes)) + ' letras erroneas y ' + str(len(success)) + ' letras correctas, la palabra era "' + word.upper() + '"')
            endgame = True
    # Pregunta al jugador si quiere jugar de nuevo
    if endgame:
        if start():
            mistakes = ""
            success = ""
            endgame = False
            word = ChooseRandomWord(words)
        else:
            break