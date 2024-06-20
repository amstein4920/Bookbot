import re

def main():
    with open("books/frankenstein.txt") as frankensteinText:
        contents = frankensteinText.read()
    # print(len(contents.split()))
    # print(character_count(contents))
    get_title(contents)

def character_count(string):
    results = {}
    lowerCaseCharacters = string.lower()
    for character in lowerCaseCharacters:
        if character in results:
            results[character] += 1
        else:
            results[character] = 1
    return results

def get_title(text):
    searchResult = re.search("^\nTitle((?:\n|.)*?)\n$", text)
    print(searchResult)

def print_report(text):
    title = get_title(text)
    print("Report on " + title)

main()