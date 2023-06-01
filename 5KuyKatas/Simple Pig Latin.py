def pig_it(text):
    words = text.split(' ')
    pigLatin = ' '

    for word in words:
        if word in '!.%&?':
            pigLatin = pigLatin + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pigLatin = pigLatin + pig_word + ' '
    return pigLatin.strip(' ')
