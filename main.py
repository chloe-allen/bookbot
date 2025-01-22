def sort_on(dict_item):
    return dict_item["num"] 


def characters(text: str) -> dict:
    counts = {}
    for i in text:
        if i.isalpha():
            lower_text = i.lower()
            value = counts.get(lower_text, 0)
            counts[lower_text] = value + 1
    return counts


def count_words(text: str) -> int:
    words = text.split()
    count = len(words)
    return count


def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as file:
        file_contents = file.read()

        count = count_words(file_contents)
       

        char_counts = characters(file_contents)

        char_list = [{"char": key, "num": value} for key, value in char_counts.items()]

        char_list.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {path_to_file} ---")
        print(f"{count} words found in the document")

        for item in char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")
        print("--- End report ---")
    
main()