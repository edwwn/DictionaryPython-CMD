import json
from difflib import get_close_matches

data =json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
         return data[w]
    elif len(get_close_matches(w, data.keys())) >0:
        yn = input("Did you Mean %s instead? Enter Y for Yes, or N for No:  " % get_close_matches(w, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The Word %s Doesnt Exist, Please Double Check it" % w
        else:
            return "We Didn't Understand your Entry"
    else:
        return "The Word  %s Doesnt Exists  Double Check It." % w

word = input ("Enter Word: ")
output=translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
     print(output)