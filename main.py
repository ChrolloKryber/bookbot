def main():
    filename = "books/frankenstein.txt"
    with open(filename) as file:
        content = file.read()
        content = content.lower().split()
        word_count = len(content)
        counter = {}
        for words in content:
            for char in words:
                if char not in counter and char.isalpha():
                    counter[char] = 1
                elif char.isalpha():
                    counter[char] += 1
        counter = dict(
            sorted(counter.items(), key=lambda item: item[1], reverse=True))
        print(f"--- Begin report of {filename} ---")
        print(f"{word_count} words found in the document")
        for key, value in counter.items():
            print(f"The {key} character was found {value} times")
        print("--- End report ---")


main()
