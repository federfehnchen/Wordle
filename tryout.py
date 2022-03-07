import requests, json


class WordleGetWord:
    def __init__(self):
        self.url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def isvalid(self, word: str) -> bool:
        trueurl = self.url+word
        r = requests.get(trueurl)
        data = json.loads(r.text)
        try:
            data[0]['word']
            return True
        except:
            return False



