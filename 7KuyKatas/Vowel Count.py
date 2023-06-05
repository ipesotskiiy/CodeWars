def get_count(sentence):
    count_vowel = 0
    for char in sentence:
        if char in 'aeiou':
            count_vowel += 1
    return count_vowel