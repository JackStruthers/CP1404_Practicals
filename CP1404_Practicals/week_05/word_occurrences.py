word_occurrences = {}
user_input = input("Text: ")
list_of_text = user_input.split(" ")
list_of_text.sort()

for word in list_of_text:
    try:
        word_occurrences[word] += 1
    except KeyError:
        word_occurrences[word] = 1

longest_count = 0
for word in list_of_text:
    if longest_count < len(word):
        longest_count = len(word)

for word, occurrence in word_occurrences.items():
    print("{:<{}} : {}".format(word, longest_count, occurrence))
