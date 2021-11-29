import json
from tovar import nounlist2
from price import nounlist1

def convertToJSON():
    with open("c:/Users/UA/Desktop/вариант 1/tovar_json.json", "w") as write_file:
        json.dump(nounlist1, write_file)
def convertInJSON():
    with open("c:/Users/UA/Desktop/вариант 1/price_json.json", "w") as write_file:
        json.dump(nounlist2, write_file)