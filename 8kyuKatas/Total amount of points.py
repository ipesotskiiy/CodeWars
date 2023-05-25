def points(games):
    result = 0
    for game in games:
        if game[0] > game[-1]:
            result += 3
        elif game[0] == game[-1]:
            result += 1
        elif game[0] < game[-1]:
            result += 0
    return result

