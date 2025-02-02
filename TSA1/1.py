def count_characters(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = consonant_count = space_count = other_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print(f"Vowels: {vowel_count}, Consonants: {consonant_count}, Spaces: {space_count}, Others: {other_count}")

input_string = input("Enter a string: ")
count_characters(input_string)