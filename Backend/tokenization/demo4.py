word = input("Enter a word: ") or "Python"

print("word = ", word)
print("Length = ", len(word))

characters = list(word)
print("Characters in the given word:", characters)

pairs = list(zip(characters, characters[1:]))

print("Adjacent Pairs:", pairs)