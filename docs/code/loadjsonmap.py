import json

def load(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

if __name__ == "__main__":
    filename0 = 'jsonFileTest0.json'
    filename1 = 'jsonFile.json'
    data0 = load(filename0)
    data1 = load(filename1)
    print (data0[0])