def delete_even_elements_lower_than_x(numbers, x):
    if len(numbers) > 0:
        other = []
        for number in numbers:
            if number != x  and number % 2 != 0:
                other.append(number)
        return other
    
    else:
        raise ValueError('Input lists cannot be empty')


