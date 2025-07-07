def wordct(text):
    words = text.split()
    nwords = len(words)
    return nwords

def charct(text):
    text = text.lower()
    chardict = {}
    for char in text:
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict