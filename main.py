import re

def main():
    with open("books/frankenstein.txt") as frankensteinText:
        contents = frankensteinText.read()
        print_report(contents)

def character_count(string):
    results = {}
    lowerCaseCharacters = string.lower()
    for character in lowerCaseCharacters:
        if character.isalpha():
            if character in results:
                results[character] += 1
            else:
                results[character] = 1
    return results

def get_title(text):
    searchResult = compiled_regex = re.compile(r'Title: (.*?)Author', re.DOTALL)
    return searchResult.findall(text)[0]

def print_report(text):
    title = get_title(text)
    print(f'Total Words found: {len(text.split())}')
    print("Report on " + title)
    letter_counts = character_count(text)
    for letter in sorted(letter_counts, key=letter_counts.get, reverse=True):
        print(f'The character \'{letter}\' was found {letter_counts[letter]} times')
main()