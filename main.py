import re

def main():
    with open("books/frankenstein.txt") as frankensteinText:
        contents = frankensteinText.read()
    # print(len(contents.split()))
    # print(character_count(contents))
    print(get_title(contents))

def character_count(string):
    results = {}
    lowerCaseCharacters = string.lower()
    for character in lowerCaseCharacters:
        if character in results:
            results[character] += 1
        else:
            results[character] = 1
    return results

def get_title(txt):
    searchResult = compiled_regex = re.compile(r'Title: (.*?)Author', re.DOTALL)
    return searchResult.findall(txt)[0]

def print_report(text):
    title = get_title(text)
    print("Report on " + title)

main()