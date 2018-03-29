import json
from sys import argv

def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def pretty_print_json(json_file):
    return json.dumbs(json_file, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == '__main__':
    try:
        print(pretty_print_json(load_data(argv[1])))
    except IOError:
        print('file not found!')
