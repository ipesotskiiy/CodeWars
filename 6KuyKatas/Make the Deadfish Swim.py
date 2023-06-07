def parse(data):
    number = 0
    result = []
    for command in data:
        if command == 'i':
            number += 1
        elif command == 'd':
            number -= 1
        elif command == 's':
            number *= number
        elif command == 'o':
            result.append(number)
    return result