def process_numbers(numbers: list) -> list:
    numbers = list(set(numbers))
    new_list = []
    for i in numbers:
        if i >= 10:
            new_list.append(i)
    new_list.sort(reverse=True)

    return new_list