def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

secret_word_1 = 'apple'
letters_guessed_1 = ['a', 'e', 'i', 'k', 'p', 'r', 's']
print(is_word_guessed(secret_word_1, letters_guessed_1))  
