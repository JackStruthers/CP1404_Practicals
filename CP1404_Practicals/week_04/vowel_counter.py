vowels = "aeiou"
name = input("Name: ")
vowel_count = 0
for char in name:
    if char.lower() in vowels:
        vowel_count += 1

print("Out of {} letters, {} has {} vowels".format(len(name), name, vowel_count))
