import json
#lib that will check the letter sequence and check close matches
from difflib import SequenceMatcher, get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w=w.lower()
    near = get_close_matches(w, data.keys())
    
    if w in data:
        return data[w]
        #returns the word if it is in the dictionary
    elif w.title() in data:
        return data[w.title()]
        #returns the word if it starts with a capital
    elif w.upper() in data:
        return data[w.upper()]
        #returns the word if it is in all capitals
    elif len(near) > 0:
        #checks the length, how close a match and if it was what was looked for 
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % near[0])
        if yn == "Y":
            return data[near[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    
word = input("Enter word: ")

#prints the output in a line unlike json format
output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)