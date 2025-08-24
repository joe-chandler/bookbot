def count_book_words(book_text):
    return len(book_text.split())

def count_book_characters(book_text):
    char_counts = {}
    for char in book_text:
        val = char.lower()
        if val in char_counts:
            char_counts[val] += 1
        else:
            char_counts[val] = 1

    return char_counts

def sort_char_dict(char_dict):
    list_dict = []
    for c in char_dict:
        list_dict.append(
            {
                "char": c,
                "num": char_dict[c]
            }
        )
    list_dict.sort(reverse=True, key=lambda x: x['num'])

    return list_dict
