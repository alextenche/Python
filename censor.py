def censor(text, word):
    text = text.split()    
    for elem in text:
        if elem == word:
            loc = text.index(elem)
            text[loc] = "*"*len(word)
    finish = " ".join(text)
    return finish
        

censor("this hack is wack hack", "hack")