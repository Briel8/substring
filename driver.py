

def substring(word, list_of_words):
    substrings = {}
    for element in list_of_words:
        if element in word:
            if element not in substrings:
                substrings[element] = 0
            substrings[element] += 1
    return substrings

dictionary = ["below","down","go","going","horn","how","howdy","it","i","low","own","part","partner","sit"]


print(substring("Howdy partner, sit down! How's it going", dictionary))