import FunctionExercises as funcex
# Exercise 29
print(funcex.generate_evens())

# Exercise 40

print(funcex.speak())
print(funcex.speak("Flizzy"))

# Exercise 44

print(funcex.return_day(5))
print(funcex.return_day(10))
print(funcex.return_day(0))
print(funcex.return_day(1))

# Exercise 45

list1 = [1, 2, 3]
list2 = []

print(funcex.last_element(list1))
print(funcex.last_element(list2))

# Exercise 46

print(funcex.number_compare(1, 2))
print(funcex.number_compare(2, 1))
print(funcex.number_compare(1, 1))

# Exercise 47

print(funcex.single_letter_count("Hello World", "h"))
print(funcex.single_letter_count("Hello World", "z"))
print(funcex.single_letter_count("Hello World", "l"))

# Exercise 48

print(funcex.multi_letter_count("awesome"))

# Exercise 49

print(funcex.list_manipulation([1, 2, 3], "remove", "end"))
print(funcex.list_manipulation([1, 2, 3], "remove", "beginning"))
print(funcex.list_manipulation([1, 2, 3], "add", "beginning", 20))
print(funcex.list_manipulation([1, 2, 3], "add", "end", 30))

# Exercise 50

print(funcex.is_palindrome("testing"))
print(funcex.is_palindrome("tacocat"))
print(funcex.is_palindrome("hannah"))
print(funcex.is_palindrome("robert"))
print(funcex.is_palindrome("a man a plan a canal Panama"))

# Exercise 51

new_list = [0, 2, 3, 3, 3, 4, 5, True]
bool_list = [True, False, True, True]

print(funcex.frequency(new_list, True))
print(funcex.frequency(bool_list, False))

# Exercise 52

nums = [num for num in range(0, 10)]

print(nums)
print(funcex.multiply_even_numbers(nums))

# Exercise 53

print(funcex.my_capitalize("hello"))
print(funcex.my_capitalize("ligma"))
print(funcex.my_capitalize("Ligma"))

# Exercise 54

new_list = [0, 1, 2, "", [], False, {}, None, "All Done"]

print(funcex.compact(new_list))

# Exercise 55

my_list1 = [1, 2, 3]
my_list2 = [2, 3, 4]

my_list3 = ["a", "b", "z"]
my_list4 = ["x", "y", "z"]

print(funcex.intersection(my_list1, my_list2))
print(funcex.intersection(my_list3, my_list4))

# Exercise 56

my_list = [1, 2, 3, 4]

print(funcex.partition(my_list, funcex.is_even))
print(funcex.partition_v2(my_list, funcex.is_even))

# Exercise 57

my_list = [1, 2, "a", True, "head"]
my_list2 = [1, 2, "a", True, "head", "purple"]

print(funcex.contains_purple(*my_list))
print(funcex.contains_purple(*my_list2))

# Exercise 58

print(funcex.combine_words("child", prefix="man"))
print(funcex.combine_words("child", suffix="ish"))
print(funcex.combine_words("child"))

nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23, 34,
        45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17, 11, 7, 11, 8, 4, 6,
        2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8,
        7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]

result_1 = funcex.count_sevens(1, 4, 7)
result_2 = funcex.count_sevens(*nums)

print(f"R1 {result_1}, R2 {result_2}")

# Exercise 60

print(funcex.calculate(make_float=False, operation='add', message='You just added', first=2, second=4))  # "You just added 6")
print(funcex.calculate(make_float=True, operation='divide', first=3.5, second=5))  # "The result is 0.7"

# Exercise 61

cube = lambda x: x ** 3

print(cube(2))
print(cube(3))
print(cube(8))

# Exercise 62

new_list = list(map(lambda x: x - 1, [1, 2, 3]))
# new_list = list(map(lambda x: x - 1, [20, 14, 11]))
print(new_list)

# Exercise 63

print(funcex.remove_negatives([-1, 3, 4, -99]))
print(funcex.remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
print(funcex.remove_negatives([50, 60, 70]))

# Exercise 64

print(funcex.is_all_strings(['a', 'b', 'c']))
print(funcex.is_all_strings([2, 'a', 'b', 'c']))
print(funcex.is_all_strings(['hello', 'goodbye']))

# Exercise 65

print(funcex.extremes([1, 2, 3, 4, 5]))
print(funcex.extremes((99, 25, 30, -7)))
print(funcex.extremes("alcatraz"))

# Exercise 66

print(funcex.max_magnitude([300, 20, -900]))
print(funcex.max_magnitude([10, 11, 12]))
print(funcex.max_magnitude([-5, -1, -89]))

# Exercise 67

print(funcex.sum_even_values(1, 2, 3, 4, 5, 6))
print(funcex.sum_even_values(4, 2, 1, 10))
print(funcex.sum_even_values(1))

# Exercise 68

print(funcex.sum_floats(1.5, 2.4, 'awesome', [], 1))
print(funcex.sum_floats(1, 2, 3, 4, 5))

# Exercise 69

print(funcex.interleave_2("lzr", "iad"))
print(funcex.interleave("aaa", "zzz"))
print(funcex.interleave("hi", "ha"))

# Exercise 70

print(funcex.triple_and_filter([1, 2, 3, 4]))
print(funcex.triple_and_filter([6, 8, 10, 12]))

# Exercise 71
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(funcex.extract_full_name(names))










