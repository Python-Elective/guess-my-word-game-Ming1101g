def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

# Test cases
secret_word_1 = 'apple'
letters_guessed_1 = ['a', 'e', 'i', 'k', 'p', 'r', 's']
print(is_word_guessed(secret_word_1, letters_guessed_1))  # Output: False

secret_word_2 = 'durian'
letters_guessed_2 = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
print(is_word_guessed(secret_word_2, letters_guessed_2))  # Output: True

# Random Test 1
print(is_word_guessed('carrot', ['b', 'g', 'd', 'z', 'w', 'y', 'v', 'm', 'i', 'k']))  # Output: False

# Random Test 2
print(is_word_guessed('lettuce', ['k', 'v', 'a', 'e', 'n', 'd', 'b', 'f', 'u', 'c']))  # Output: False

# Random Test 3
print(is_word_guessed('pineapple', []))  # Output: False

# Random Test 4
print(is_word_guessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']))  # Output: True
