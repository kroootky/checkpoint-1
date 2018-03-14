import common
import average
import delete




def common_elements():
    first = [1,2,3,4,5,6,7]
    second = []
    print(common.get_common_odd_elements(first,second))

def average_elements():
    print(average.average_of_first_x_odd_numbers(5,start=0))

def delete_lower():
    numbers = [1,2,2,2,3,4,4,5,6,7,8]
    x = 3
    print(delete.delete_even_elements_lower_than_x(numbers, x))

common_elements()
average_elements()
delete_lower()