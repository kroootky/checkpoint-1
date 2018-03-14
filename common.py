def get_common_odd_elements(first, second):
    if len(first) > 0 and len(second) > 0:
        
        result = []
        for element in first:
            for elem in second:
                if element == elem and element % 2 != 0:
                    result.append(element)
        return result
    
    else:
        raise ValueError('Input list cannot be empty')


                