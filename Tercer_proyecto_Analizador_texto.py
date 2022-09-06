title0 = "\t\ttext analyzer\n".title()
print(title0)
text = input("Enter any text:\n")
# print(text)

print("\nEnter 3 different letters:")
letter1 = input("Letter 1: ")
letter2 = input("Letter 2: ")
letter3 = input("Letter 3: ")
print(f"Letter {letter1} appears: {text.count(letter1)} times")
print(f"Letter {letter2} appears: {text.count(letter2)} times")
print(f"Letter {letter3} appears: {text.count(letter3)} times\n")

text_lower = text.lower()
words = text_lower.split(" ")
length_words = len(words)
# print(type(length_words))
print(f"The text has {length_words} words")

last_word = words[length_words - 1]
length_last_word = len(last_word)
# print(last_word)
# print(length_last_word)
# BETTER WAY: ultima palabra = words[-1]
fl_word = words[0]
print(f"The firs letter of the text is: {fl_word[0]}")
print(f"The last letter of the text is: {last_word[length_last_word - 1]}")

words.reverse()
# print(words)
print(f"\nThe reverse text is:\n{' '.join(words)}")


dictionary = {True: "appears in the text", False: "doesn't appears in the text"}
check_python = 'python' in words
print(f"PYTHON {dictionary[check_python]}")
