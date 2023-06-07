def good_vs_evil(good, evil):
    evil_forces = evil.split()
    good_forces = good.split()
    battle_result = 0
    good_race_raiting = [1, 2, 3, 3, 4, 10]
    evil_race_raiting = [1, 2, 2, 2, 3, 5, 10]

    for race in range(len(evil_forces)):
        if race < len(evil_forces) - 1:
            battle_result += int(good_forces[race]) * good_race_raiting[race]
            battle_result -= int(evil_forces[race]) * evil_race_raiting[race]

        elif race == len(evil_forces) - 1:
            battle_result -= int(evil_forces[race]) * evil_race_raiting[race]

    if battle_result == 0:
        return "Battle Result: No victor on this battle field"

    return "Battle Result: Good triumphs over Evil" if battle_result > 0 else "Battle Result: Evil eradicates all trace of Good"