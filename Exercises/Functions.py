# Exercise 39
def generate_evens():
    """
    Generate a list of even numbers

    :return: List of even numbers
    """
    list_of_evens = [num for num in range(1, 51) if num % 2 == 0]
    return list_of_evens


# Exercise 40
def speak(animal="dog"):
    """
    Print the sound a specific animal makes

    :param animal: Animal either pig, dog, duck, cat, default dog
    :return: The sound the animal makes, else '?'
    """
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"

    return "?"


# Exercise 44
def return_day(num):
    """
    Return a the name of the day given the day of the week

    :param num: Number of the day of the week 1-7
    :return: The name of the day of the week
    """
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if 0 < num < 8:
        return days[num - 1]

    return None


# Exercise 45
def last_element(my_list):
    """
    Return the last element in a list

    :param my_list: List to be evaluted
    :return: The last element else None
    """
    if len(my_list) != 0:
        return my_list[len(my_list) - 1]

    return None


# Better solution
# Using truthy approach
def last_element2(my_list):
    """
    Another version of last_element
    """
    if my_list:
        return my_list[-1]

    return None


# Exercise 46
def number_compare(num1, num2):
    """
    Compare two numbers and print which is greater

    :param num1: First number
    :param num2: Seconds number
    :return: The number that is greater or if the numbers are equal
    """
    if num1 > num2:
        return "First is greater"
    elif num1 < num2:
        return "Second is greater"

    return "Numbers are equal"


# Exercise 47
def single_letter_count(word, letter):
    """
    Count the number a time a letter in is a word

    :param word: Word to be evaluated
    :param letter: Target letter
    :return: A count of the number of times the letter appears in the word
    """
    if letter in word.lower():
        return word.lower().count(letter)

    return 0


# Can be simplified to:
# Will return 0 regardless
def single_letter_count2(word, letter):
    """
    Another version of single_letter_count
    """
    return word.lower().count(letter.lower())


# Exercise 48
# Need more descriptive var names
def multi_letter_count(word):
    """
    Return a dictionary of all occurrences of a letter in a word

    :param word: Word to be evaluated
    :return: A dictionary with the # of times a letter appears in the word
    """
    return {k: word.count(k) for k in word}


# Exercise 49
def list_manipulation(list, cmd, loc, num=0):
    """
    Perform a function on a list given a command

    :param list: List used to perform operations on
    :param cmd: Type of command, either remove or add
    :param loc: Location of the list, either end or beginning
    :param num: Element to be added to the list in the case of add
    :return: Returns the list after operations have been completed
    """
    if cmd == "remove" and loc == "end":
        return list.pop()

    if cmd == "remove" and loc == "beginning":
        return list.pop(0)

    if cmd == "add" and loc == "end":
        list.append(num)
        return list

    if cmd == "add" and loc == "beginning":
        list.insert(0, num)
        return list


# Exercise 50
def is_palindrome2(word):
    """
    Checks if a word is a palindrome or not

    :param word: Word to be evaluated
    :return: True if it is a palindrome, else False
    """
    if " " in word:
        return False

    reverse = word[::-1]

    for i in range(0, len(word)):
        print(f"{word[i]} - {reverse[i]}")
        if word[i] != reverse[i]:
            return False

    return True


# == Operator will already return true or false which is what we want, so return true and return false is redundant
# in this case
def is_palindrome(word):
    """
    Another version of is_palindrome2
    """
    reverse = word[::-1]

    reverse = reverse.replace(" ", "").lower()
    word = word.replace(" ", "").lower()

    if word == reverse:
        return True

    return False


def is_palindrome3(word):
    """ Another version of is_palindrome2 """
    stripped = word.replace(" ", "")

    return stripped[::-1] == stripped


# Exercise 51
def frequency(my_list, item):
    """
    Determine the number of times an item appears in a list

    :param my_list: List to check items in
    :param item: Target item (str, int, float, etc)
    :return: The # of times the item appears in the list
    """
    return my_list.count(item)


# Exercise 52
def multiply_even_numbers(list_of_nums):
    """
    The result of multiplying all the even numbers in a list
    :param list_of_nums: List to be evaluated
    :return: The product of all even numbers (non-zero) in a list
    """
    even_product = 1
    for num in list_of_nums:
        if num % 2 == 0 and num != 0:
            even_product = num * even_product

    return even_product


# Exercise 53
#
# List slice will not throw an error
# Indexing will throw an error
# SLICES WILL NOT THROW ERRORS LIKE INDEXING DOES IN PYTHON
def my_capitalize(word):
    """
    Capitalize the first letter in a word

    :param word: Word to be capitalized
    :return: The capitalized word
    """
    return word[0].upper() + word[1::1]


def my_capitalize_short(word):
    """ Short version of my_capitalize """
    return word[:1].upper() + word[1:]


# Exercise 54
def compact(my_list):
    """
    Remove all falsy values from a list

    :param my_list: List to be evaluated
    :return: A list of all truthy values in my_list-
    """
    return [element for element in my_list if element]


# Exercise 55
# Can also be done using sets
def intersection(list1, list2):
    """
    Find the intersection of two lists
    :param list1: First list to be evaluated
    :param list2: Second list to be evaluated
    :return: A list of all common elements in both lists (set intersection)
    """
    return [element for element in list1 if element in list2]


# Exercise 56
def is_even(num):
    return num % 2 == 0


def partition(new_list, fn):
    """
    Separates all true and false evaluations based of results of a function
    :param new_list: List to be evaluated
    :param fn: Function used to determine True or False
    :return: A list of a the list of true values and false values based on the results of the function
    """
    truthy_list = []
    falsy_list = []

    for element in new_list:
        if fn(element):
            truthy_list.append(element)
        else:
            falsy_list.append(element)

    return [truthy_list, falsy_list]


def partition_v2(new_list, fn):
    """ Shortened version of partition """
    return [[element for element in new_list if fn(element)], [element for element in new_list if not fn(element)]]


# Exercise 57
def contains_purple(*args):
    """ Determine if input arguements contain the word 'purple' """
    if "purple" in args:
        return True

    return False


# Exercise 58
# Do not need keys() function just need the dict name
def combine_words(word, **kwargs):
    """
    Append a prefix or suffix to a word
    :param word: Word to be appended
    :param kwargs: Key args, suffix or prefix with their respective values
    :return: The word after it has been appended
    """
    if "prefix" in kwargs.keys():
        return kwargs["prefix"] + word

    if "suffix" in kwargs.keys():
        return word + kwargs["suffix"]

    return word


# Exercise 59
# args is a tuple
# Can use built in tuple functions when doing these kinds of things
def count_sevens_2(*args):
    """
    Return the number of occurrences of the number 7
    :param args: Numbers to be evaluated
    :return: The # of times the number 7 appears in args
    """
    return args.count(7)


def count_sevens(*args):
    """ Another version of count_sevens """
    sevens_counter = 0
    for num in args:
        if num == 7:
            sevens_counter += 1

    return sevens_counter


# Exercise 60
# get(key, value) -> value returned if the key does not exist
def calculate(**kwargs):
    """
    Calculator using keyword args
    :param kwargs:
    :return:
    """
    result = None
    if kwargs["operation"] == "add":
        result = kwargs["first"] + kwargs["second"]
    elif kwargs["operation"] == "subtract":
        result = kwargs["first"] - kwargs["second"]
    elif kwargs["operation"] == "multiply":
        result = kwargs["first"] * kwargs["second"]
    elif kwargs["operation"] == "divide":
        result = kwargs["first"] / kwargs["second"]

    if kwargs["make_float"] is True:
        return f"{kwargs.get('message', 'The result is')} {float(result)}"
    else:
        return f"{kwargs.get('message', 'The result is')} {int(result)}"


# Exercise 62
def decrement_list(my_list):
    return list(map(lambda x: x - 1), my_list)


# Exercise 63
def remove_negatives(l):
    """
     Remove all negative values from a list

    :param l: List to be evaluated
    :return: List with negatives removed
    """
    return list(filter(lambda x: x > -1, l))


# Exercise 64
def is_all_strings(l):
    """
    Check whether a list contains all strings

    :param l: List to be evaluated
    :return: True if list contains all string else False
    """
    return all(isinstance(element, str) for element in l)


# Exercise 65
# Double round brackets are needed to make a tuple using the constructor
def extremes(itr):
    """
    Get the min and max of a list (or any iterator possibly)

    :param itr: Iterable object
    :return: Tuple, min and max of the iterable object
    """
    return min(itr), max(itr)


# Exercise 66
def max_magnitude(nums):
    """
    Get the max number regardless of sign

    :param nums: List of numbers to be evaluated
    :return: The max number
    """
    return max(abs(num) for num in nums)


# Exercise 67
def sum_even_values(*args):
    """
    Sum all even values

    :param args:
    :return: The some of all even values
    """
    return sum(num for num in args if num % 2 == 0)


# Exercise 68
def sum_floats(*args):
    """
    Sum all floats

    :param args:
    :return: Sum of all floats
    """
    return sum(arg for arg in args if isinstance(arg, float))

# Exercise 69
def interleave_2(str_1, str_2):
    return "".join("".join(x) for x in zip(str_1, str_2))


def interleave(str_1, str_2):
    return "".join([char_tuple[0] + char_tuple[1] for char_tuple in zip(str_1, str_2)])


# Exercise 70
def triple_and_filter(l):
    """
    Triple all the elements in a list and filter by mod 4

    :param l: List to be evaluated
    :return: The list after tripling and filtering
    """
    return list(
        map(
            lambda x: x * 3,
            filter(
                lambda x: x % 4 == 0,
                l
            )
        )
    )

# Exercise 71
def extract_full_name(name_list):
    """
    Extracting the full name from a list of name dictionaries
    :param name_list: List of name dictionaries containing first and last name key:values
    :return: The list of all first and last names not in dictionary format
    """
    return [f"{name['first']} {name['last']}" for name in name_list]



