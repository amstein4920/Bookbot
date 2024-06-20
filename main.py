def main():
    with open("books/frankenstein.txt") as frankensteinText:
        contents = frankensteinText.read()
    print(len(contents.split()))
    print(characterCount(contents))

def characterCount(string):
    results = {}
    lowerCaseCharacters = string.lower()
    for character in lowerCaseCharacters:
        if character in results:
            results[character] += 1
        else:
            results[character] = 1
    return results
main()