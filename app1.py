import json
from difflib import get_close_matches

word=input("ENTER THE WORD:-  ")

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.8))>0:
        ans= input("did you mean %s instead?\nenter Y/N:-" % get_close_matches(w,data.keys())[0])
        if ans.lower()=='y':
            return data[get_close_matches(w,data.keys())[0]]
        elif ans.lower() == 'n':
            return "WORD NOT IN DICTIONARY\nplease check your word again"
        else:
            return "we didn't get your query"

    else:
        print('WORD NOT IN DICTIONARY\nplease check your word again')




final_output= translate(word)

if type(final_output)==list:
    for _ in final_output:
        print (_)
else:
    print("WORD NOT IN DICTIONARY\nplease check your word again")
