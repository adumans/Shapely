import json

def load():
    with open('test.json') as json_file:
        data = json.load(json_file)
        return data

if __name__ == "__main__":
    data = load()
    print (data['2'])