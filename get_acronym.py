def get_acronym(text):
    text = text.split()
    final_string = ""
    for word in text:
        final_string += str(word[0].upper())
    return final_string

if __name__ == "__main__":
    output = get_acronym(input("Please input text: "))
    print(output)

