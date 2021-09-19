import re


def ionize(file_path: str):
    """returns a list"""
    contacts = {}
    count = 0

    with open(file_path, 'r') as file:
        files = file.readlines()
        for line in files:
            if re.search(r'^BEGIN', line):
                count += 1
                details = []
            if re.search(r'^END', line):
                details.append(line)
                contacts[count] = details
            else:
                details.append(line)

    return contacts