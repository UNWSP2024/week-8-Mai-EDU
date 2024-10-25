# Programmer: Mai Lillie
# Date: 10/25/2024
# Program #2: Word Separator

# Adds spaces, lowercase and uppercase, and a period
def word_separator(sentence_input):
    modified_sentence = ""

    modified_sentence = modified_sentence + sentence_input[0]
    for i in range(1, len(sentence_input)):
        char = sentence_input[i]

        if char.isupper():
            char = char.lower()
            modified_sentence = modified_sentence + " "

        modified_sentence = modified_sentence + char

    modified_sentence = modified_sentence + "."
    return modified_sentence.strip()

# Runs program with user input
sentence = input("Enter your sentence here: ")
new_sentence = word_separator(sentence)
print(new_sentence)
