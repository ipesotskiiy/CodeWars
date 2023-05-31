def first_non_repeating_letter(s):
    s_lower = s.lower()
    for char in range(len(s_lower)):
        if s_lower.count(s_lower[char]) == 1:
            return s[char]
    return ''
