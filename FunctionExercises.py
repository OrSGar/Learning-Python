# Exercise 39
#
# def generate_evens():
#     list_of_evens = [num for num in range(1, 51) if num % 2 == 0]
#     return list_of_evens
#
#
# print(generate_evens())

# Exercise 40
#
# def speak(animal="dog"):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#
#     return "?"
#
#
# print(speak())
# print(speak("Flizzy"))

# Exercise 44

# def return_day(num):
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#
#     if 0 < num < 8:
#         return days[num - 1]
#
#     return None
#
#
# print(return_day(5))
# print(return_day(10))
# print(return_day(0))
# print(return_day(1))

# Exercise 45

# def last_element(my_list):
#     if len(my_list) != 0:
#         return my_list[len(my_list) - 1]
#
#     return None
#
#
# list1 = [1, 2, 3]
# list2 = []
#
# print(last_element(list1))
# print(last_element(list2))
#
# # Better solution
# # Using truthy approach
# def last_element2(l):
#     if l:
#         return l[-1]
#
#     return None

# Exercise 46

# def number_compare(num1, num2):
#     if num1 > num2:
#         return "First is greater"
#     elif num1 < num2:
#         return "Second is greater"
#
#     return "Numbers are equal"
#
#
# print(number_compare(1, 2))
# print(number_compare(2, 1))
# print(number_compare(1, 1))

# Exercise 47

# def single_letter_count(word, letter):
#     if letter in word.lower():
#         return word.lower().count(letter)
#
#     return 0
#
#
# print(single_letter_count("Hello World", "h"))
# print(single_letter_count("Hello World", "z"))
# print(single_letter_count("Hello World", "l"))
#
# # Can be simplified to:
# # Will return 0 regardless
#
#
# def single_letter_count2(word, letter):
#     return word.lower().count(letter.lower())

# Exercise 48

# # Need more descriptive var names
# def multi_letter_count(word):
#     return {k: word.count(k) for k in word}
#
#
# print(multi_letter_count("awesome"))

# Exercise 49

# def list_manipulation(list, cmd, loc, num=0):
#     if cmd == "remove" and loc == "end":
#         return list.pop()
#
#     if cmd == "remove" and loc == "beginning":
#         return list.pop(0)
#
#     if cmd == "add" and loc == "end":
#         list.append(num)
#         return list
#
#     if cmd == "add" and loc == "beginning":
#         list.insert(0, num)
#         return list
#
#
# print(list_manipulation([1,2,3], "remove", "end"))
# print(list_manipulation([1,2,3], "remove", "beginning"))
# print(list_manipulation([1,2,3], "add", "beginning", 20))
# print(list_manipulation([1,2,3], "add", "end", 30))

# Exercise 50

# def is_palindrome2(word):
#     if " " in word:
#         return False
#
#     reverse = word[::-1]
#
#     for i in range(0, len(word)):
#         print(f"{word[i]} - {reverse[i]}")
#         if word[i] != reverse[i]:
#             return False
#
#     return True
#
# # == Operator will already return true or false which is what we want, so return true and return false is redundant
# # in this case
#
# def is_palindrome(word):
#     reverse = word[::-1]
#
#     reverse = reverse.replace(" ", "").lower()
#     word = word.replace(" ", "").lower()
#
#     if word == reverse:
#         return True
#
#     return False
#
# def is_palindrome3(word):
#     stripped = word.replace(" ", "")
#
#     return stripped[::-1] == stripped
#
# print(is_palindrome("testing"))
# print(is_palindrome("tacocat"))
# print(is_palindrome("hannah"))
# print(is_palindrome("robert"))
# print(is_palindrome("a man a plan a canal Panama"))

# Exercise 51

# def frequency(my_list, item):
#     return my_list.count(item)
#
#
# new_list = [0, 2, 3, 3, 3, 4, 5, True]
# bool_list = [True, False, True, True]
#
# print(frequency(new_list, True))
# print(frequency(bool_list, False))

# Exercise 52

# def multiply_even_numbers(list_of_nums):
#     even_product = 1
#     for num in list_of_nums:
#         if num % 2 == 0 and num != 0:
#             even_product = num * even_product
#
#     return even_product
#
#
# nums = [num for num in range(0, 10)]
#
# print(nums)
#
# print(multiply_even_numbers(nums))

# Exercise 53

# List slice will not throw an error
# Indexing will throw an error
# SLICES WILL NOT THROW ERRORS LIKE INDEXING DOES IN PYTHON
# def my_capitalize(word):
#     return word[0].upper() + word[1::1]
#
#
# def my_capitalize_short(word):
#     return word[:1].upper() + word[1:]
#
#
# print(my_capitalize("hello"))
# print(my_capitalize("ligma"))
# print(my_capitalize("Ligma"))
#
# my_string = ""
# # print(my_string[0])
# print(my_string[:1])
#
# print(my_string)

# Exercise 54

# def compact(my_list):
#     return [element for element in my_list if element]
#
#
# new_list = [0, 1, 2, "", [], False, {}, None, "All Done"]
#
# print(compact(new_list))

# Exercise 55
# Can also be done using sets
# def intersection(list1, list2):
#     return [element for element in list1 if element in list2]
#
#
# my_list1 = [1, 2, 3]
# my_list2 = [2, 3, 4]
#
# my_list3 = ["a", "b", "z"]
# my_list4 = ["x", "y", "z"]
#
# print(intersection(my_list1, my_list2))
# print(intersection(my_list3, my_list4))

# Exercise 56

# def is_even(num):
#     return num % 2 == 0
#
#
# def partition(new_list, fn):
#     truthy_list = []
#     falsy_list = []
#
#     for element in new_list:
#         if fn(element):
#             truthy_list.append(element)
#         else:
#             falsy_list.append(element)
#
#     return [truthy_list, falsy_list]
#
#
# #
# def partition_v2(new_list, fn):
#     return [[element for element in new_list if fn(element)], [element for element in new_list if not fn(element)]]
#
#
# my_list = [1, 2, 3, 4]
#
# print(partition(my_list, is_even))
# print(partition_v2(my_list, is_even))

# Exercise 57

# def contains_purple(*args):
#     if "purple" in args:
#         return True
#
#     return False
#
#
# my_list = [1, 2, "a", True, "headass"]
# my_list2 = [1, 2, "a", True, "headass", "purple"]
#
# print(contains_purple(*my_list))
# print(contains_purple(*my_list2))

# # Exercise 58
# # Do not need keys() function just need the dict name
# def combine_words(word, **kwargs):
#     if "prefix" in kwargs.keys():
#         return kwargs["prefix"] + word
#
#     if "suffix" in kwargs.keys():
#         return word + kwargs["suffix"]
#
#     return word
#
#
# print(combine_words("child", prefix="man"))
# print(combine_words("child", suffix="ish"))
# print(combine_words("child"))

# Exercise 59
# args is a tuple
# Can use built in tuple functions when doing these kinds of things
#
# def count_sevens_2(*args):
#     return args.count(7)
#
#
# def count_sevens(*args):
#     sevens_counter = 0
#     for num in args:
#         if num == 7:
#             sevens_counter += 1
#
#     return sevens_counter
#
#
# nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23, 34,
#         45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17, 11, 7, 11, 8, 4, 6,
#         2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8,
#         7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]
#
# result_1 = count_sevens(1, 4, 7)
# result_2 = count_sevens(*nums)
#
# print(f"R1 {result_1}, R2 {result_2}")

# Exercise 60
# # get(key, value) -> value returned if the key does not exist
# def calculate(**kwargs):
#     result = None
#     if kwargs["operation"] == "add":
#         result = kwargs["first"] + kwargs["second"]
#     elif kwargs["operation"] == "subtract":
#         result = kwargs["first"] - kwargs["second"]
#     elif kwargs["operation"] == "multiply":
#         result = kwargs["first"] * kwargs["second"]
#     elif kwargs["operation"] == "divide":
#         result = kwargs["first"] / kwargs["second"]
#
#     if kwargs["make_float"] is True:
#         return f"{kwargs.get('message', 'The result is')} {float(result)}"
#     else:
#         return f"{kwargs.get('message', 'The result is')} {int(result)}"
#
#
# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6")
#
# print(calculate(make_float=True, operation='divide', first=3.5, second=5))  # "The result is 0.7"

# #Exercise 61
#
# cube = lambda x: x**3
#
# print(cube(2))
# print(cube(3))
# print(cube(8))

# Exercise 62

# def decrement_list(l):
#     return list(map(lambda x: x - 1), l)
#
#
# new_list = list(map(lambda x: x - 1, [1, 2, 3]))
# new_list = list(map(lambda x: x - 1, [20, 14, 11]))
#
# print(new_list)

# Exercise 63
#
# def remove_negatives(l):
#     return list(filter(lambda x: x > -1, l))
#
#
# print(remove_negatives([-1, 3, 4, -99]))
# print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
# print(remove_negatives([50, 60, 70]))

# Exercise 64
#
# def is_all_strings(l):
#     return all(isinstance(element, str) for element in l)
#
#
# print(is_all_strings(['a', 'b', 'c']))
# print(is_all_strings([2, 'a', 'b', 'c']))
# print(is_all_strings(['hello', 'goodbye']))

# Exercise 65
# Double round brackets are needed to make a tuple using the constructor
# def extremes(itr):
#     return min(itr), max(itr)
#
#
# print(extremes([1, 2, 3, 4, 5]))
# print(extremes((99, 25, 30, -7)))
# print(extremes("alcatraz"))

# Exercise 66
#
# def max_magnitude(nums):
#     return max(abs(num) for num in nums)
#
#
# print(max_magnitude([300, 20, -900]))
# print(max_magnitude([10, 11, 12]))
# print(max_magnitude([-5, -1, -89]))

# # Exercise 67
#
# def sum_even_values(*args):
#     return sum(num for num in args if num % 2 == 0)
#
#
# print(sum_even_values(1, 2, 3, 4, 5, 6))
# print(sum_even_values(4, 2, 1, 10))
# print(sum_even_values(1))

# Exercise 68
# type(var) == type
#
# def sum_floats(*args):
#     return sum(arg for arg in args if isinstance(arg, float))
#
#
# print(sum_floats(1.5, 2.4, 'awesome', [], 1))
# print(sum_floats(1, 2, 3, 4, 5))

# Exercise 69
#
# def interleave_2(str_1, str_2):
#     return "".join("".join(x) for x in zip(str_1, str_2))
#
#
# def interleave(str_1, str_2):
#     return "".join([char_tuple[0] + char_tuple[1] for char_tuple in zip(str_1, str_2)])
#
#
# print(interleave_2("lzr", "iad"))
# print(interleave("aaa", "zzz"))
# print(interleave("hi", "ha"))

# Exercise 70

# def triple_and_filter(l):
#     return list(
#                 map(
#                     lambda x: x * 3,
#                     filter(
#                         lambda x: x % 4 == 0,
#                         l
#                     )
#                 )
#             )
#
#
# print(triple_and_filter([1, 2, 3, 4]))
# print(triple_and_filter([6, 8, 10, 12]))

# # Exercise 71
#
# def extract_full_name(name_list):
#     return [f"{name['first']} {name['last']}" for name in names]
#
#
# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
#
# print(extract_full_name(names))

