def pig_it(text):
    out_list =[]
    words_list = text.split()

    for word in word_list:
        if word.isalpha():

            pig_word = f"{word[1:]}{word[0]}ay"

            out_list.append(pig_word)
        
        else:
            out_list.append(word)

    out_string =" ".join(out_list)
    return out_string