def duplicate_count(text):
    # Your code goes here
    n = 0
    #convert to lower characters
    text = text.lower()
    for i in text:
        if text.count(i) > 1:
            # when characters exist more than onece in text, increment n
            n += 1
            # for characters appear more than once, remove from string
            text = text.replace(i,'')
    return n
