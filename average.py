def average_of_first_x_odd_numbers(x,start=0):
    passes = 0 
    items_sum = 0
    items_count = 0
    numbers = [1,3,5,7,9,25]
    
    if x > 0:
        for item in numbers[start:]:
            if passes < x:
                passes += 1
                items_sum += item
                items_count += 1
                avg = items_sum / items_count
        return avg
    else:
        raise ValueError('Numbers count parameter must be greather than zero')
