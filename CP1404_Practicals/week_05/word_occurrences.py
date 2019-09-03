word_occurrences = {}
user_text = input("Text: ")
split_text = user_text.split(" ")
split_text.sort()

for word in split_text:
    try:
        word_occurrences[word] += 1
    except KeyError:
        word_occurrences[word] = 1

longest_count = 0
for word in split_text:
    if longest_count < len(word):
        longest_count = len(word)

for word, occurrence in word_occurrences.items():
    print("{:<{}} : {}".format(word, longest_count, occurrence))
