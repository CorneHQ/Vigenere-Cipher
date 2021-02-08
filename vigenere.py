from english_quadgrams import quadgram_score
import re, string, random

alphabet = string.ascii_lowercase

def quadgram_fitness(text):
    text = re.sub('[^A-Za-z]+', '', text.replace(" ", "").lower()) 

    quadgrams = [text[i:i+4] for i in range(len(text)-4+1)]

    fitness = sum([quadgram_score[quadgram] if quadgram in quadgram_score else 23 for quadgram in quadgrams])

    if "." in str(fitness) and len(str(fitness).split(".")[1]) <= 4:
        return round(fitness, 5)
        
    return fitness

def encrypt_vigenere(plaintext, key):
    outcome = ''
    count = 0
    for letter in plaintext:
        if letter == ' ':
            outcome += ' '
        elif letter.lower() in alphabet:
            if count < len(key):
                keyPosition = alphabet.index(key[count])
                letterPosition = alphabet.index(letter.lower())
                if keyPosition + letterPosition < 26:
                    outcome += alphabet[keyPosition + letterPosition].upper() if letter.isupper() else alphabet[keyPosition + letterPosition]
                else:
                    outcome += alphabet[keyPosition + letterPosition - 26].upper() if letter.isupper() else alphabet[keyPosition + letterPosition - 26]
                count += 1
            else:
                keyPosition = alphabet.index(key[0])
                letterPosition = alphabet.index(letter.lower())
                if keyPosition + letterPosition < 26:
                    outcome += alphabet[keyPosition + letterPosition].upper() if letter.isupper() else alphabet[keyPosition + letterPosition]
                else:
                    outcome += alphabet[keyPosition + letterPosition - 26].upper() if letter.isupper() else alphabet[keyPosition + letterPosition - 26]
                count = 1
        else:
            outcome += letter
    return outcome


def decrypt_vigenere(ciphertext, key):
    outcome = ''
    count = 0
    for letter in ciphertext:
        if letter == ' ':
            outcome += ' '
        elif letter.lower() in alphabet:
            if count < len(key):
                keyPosition = alphabet.index(key[count])
                letterPosition = alphabet.index(letter.lower())
                if letterPosition - keyPosition >= 0:
                    outcome += alphabet[letterPosition - keyPosition].upper() if letter.isupper() else alphabet[letterPosition - keyPosition]
                else:
                    outcome += alphabet[letterPosition - keyPosition + 26].upper() if letter.isupper() else alphabet[letterPosition - keyPosition + 26]
                count += 1
            else:
                keyPosition = alphabet.index(key[0])
                letterPosition = alphabet.index(letter.lower())
                if letterPosition - keyPosition >= 0:
                    outcome += alphabet[letterPosition - keyPosition].upper() if letter.isupper() else alphabet[letterPosition - keyPosition]
                else:
                    outcome += alphabet[letterPosition - keyPosition + 26].upper() if letter.isupper() else alphabet[letterPosition - keyPosition + 26]
                count = 1
        else:
            outcome += letter
    return outcome

def solve_vigenere(ciphertext, keylen):
    randomKey = ''.join(random.choice(alphabet) for i in range(keylen))
    currentFitness = 0
    bestFitness = 0
    bestKey = ""
    bestText = ""

    for _ in range(1000*keylen**2):
        keyList = list(randomKey)
        keyList[random.randint(0, len(keyList)-1)] = random.choice(alphabet)
        tempKey = ''.join(keyList)
        tempDecryptedText = decrypt_vigenere(ciphertext, tempKey)
        tempNewFitness = quadgram_fitness(tempDecryptedText)

        if tempNewFitness < currentFitness or random.random() < 0.01 or currentFitness == 0:
            randomKey = tempKey
            currentFitness = tempNewFitness

        if currentFitness < bestFitness or bestFitness == 0:
            bestFitness = currentFitness
            bestKey = randomKey
            bestText = tempDecryptedText

    return bestKey, bestText