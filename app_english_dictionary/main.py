import json
from difflib import get_close_matches

data = json.load(open("app_english_dictionary/data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        w_match = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if w_match == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif w_match == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)