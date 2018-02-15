def remove_smallest_item(numbers):
    if len(numbers) == 0:
        return []

    response = numbers[:]  # clone the list as we do not want to change the i/p
    response.pop(response.index(min(response)))
    return response
