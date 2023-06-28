def consonant_count(s):
    count = 0
    for i in s:
        if i.lower() not in 'aeiou' and i.isalpha():
            count += 1
    return count