def capitalize_words(sentence):
    words = sentence.split()
    
    capitalized_sentence = ' '.join([word.capitalize() for word in words])
    
    return capitalized_sentence

def main():
    input_sentence = input("Enter a sentence: ")
    result = capitalize_words(input_sentence)
    print("Capitalized sentence:", result)

if __name__ == "__main__":
    main()
