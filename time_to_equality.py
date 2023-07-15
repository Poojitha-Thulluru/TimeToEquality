def time_to_equality_array(num_array: list) -> int:
    max_element = max(num_array)
    num_array.remove(max_element)
    new_array = []
    for val in num_array:
        new_array.append(max_element - val)
    return sum(new_array)


try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    print("The minimum time required to make the elements of an array equal is : ", time_to_equality_array(nums_array))
except ValueError:
    print("Invalid input. Enter Only Integers")
