# Exercise 95
# In colts solution, he first read the contents of the first file with a with
# He the used another with and wrote to the new file
def copy(file1, file2):
    """
    Copy contents of one file to another
    :param file1: Path of file to be copied
    :param file2: Path of destination file
    """
    destination = open(file2, "w")

    with open(file1, "r") as source:
        destination.write(source.read())

    destination.close()


# Exercise 96
# In Colts code, he didnt save the reverse - He just reversed it when we passed it in
def copy_and_reverse(file1, file2):
    """
    Copy contents of a file to another in reverse
    :param file1: Path of file ot be copied
    :param file2: Path of destination file
    """
    with open(file1, "r") as source:
        data = source.read()

    with open(file2, "w") as destination:
        reverse_data = data[::-1]
        destination.write(reverse_data)


# Exercise 97
def statistics_2(file):
    """
    Print number of lines, words, and characters in a file
    :param file: Path of file
    """
    with open(file) as source:
        lines = source.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) for line in lines),
            # Split every line on a space and count how many elements there are
            "characters": sum(len(line) for line in lines)}  # Count number of chars in each line


def statistics(file):
    """ My original version of statistics_2 """
    num_lines = 0
    num_char = 0
    num_words = 1
    with open(file) as source:
        line = source.readlines()
        num_lines = len(line)
        source.seek(0)
        data = source.read()
        num_char = len(data)

        for char in data:
            if char == " ":
                num_words += 1

    return {"lines": num_lines, "words": num_words, "characters": num_char}


# Exercise 98
# In Colts implementation, he just read the whole thing and replaced it
def find_and_replace(file, target, replacement):
    """
    Find and replace a target word in a file
    :param file: Path to the file
    :param target: Word to be replaced
    :param replacement: Replacement word
    """
    with open(file, "r+") as source:
        for line in source:
            print(line)
            if line == "":
                break
            elif line.replace(target, replacement) != line:
                source.write(line.replace(target, replacement))


def f_n_r(file, target, replacement):
    """ Another version of find_and_replace """
    with open(file, "r+") as source:
        text = file.read()
        new_text = text.replace(target, replacement)
        file.seek(0)
        file.write(new_text)
        file.truncate()  # Delete everything after a certain position


find_and_replace("fileio.txt", "Orlando", "Ligma")
copy("fileio.txt", "fileio_copy.txt")
copy_and_reverse("fileio.txt", "fileio_copy.txt")
print(statistics_2("fileio.txt"))
