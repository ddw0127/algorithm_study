import xmltodict
import json

def main():
    with open("sample.xml", "rt", encoding="UTF-8") as f:
        doc = xmltodict.parse(f.read())
        print(doc)

        json_type = json.dumps(doc)
        dict2_type = json.loads(json_type)

        print(json_type)
        print(dict2_type)

if __name__ == "__main__":
    main()