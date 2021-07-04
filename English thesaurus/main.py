import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definicija(beseda):
    beseda = beseda.lower()
    if beseda in data:
        return data[beseda]
    elif beseda.upper() in data:
        return data[beseda.upper()]
    elif beseda.title() in data:
        return data[beseda.title()]
    elif len(get_close_matches(beseda, data.keys()))>0:
        odgovor = input("Ste mislili %s ? y/n" % get_close_matches(beseda,data.keys())[0])
        if odgovor == "y":
            return data[get_close_matches(beseda,data.keys())[0]]
        elif odgovor == "n":
            return "Ni razumljivo"
    else:
        return "Not found"

beseda = input("Vnos: ")
output = definicija(beseda)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)