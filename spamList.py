def spamList(listItems):
    """This function loops through items in a list and generates a comma separated string, with an oxford comma."""
    stringOutput = ', '.join(map(str, listItems[:-1])) + ', and ' + listItems[-1]
    return stringOutput

spam = ['apples', 'bananas', 'tofu', 'cats']
print(spamList(spam))
