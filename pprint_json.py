import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def make_pretty_json(json_content):
    return json.dumps(json_content, ensure_ascii=False, indent=4, sort_keys=True)


def parsed_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        metavar='ФАЙЛ',
        help='Путь до файла .json')
    return parser.parse_args()


if __name__ == '__main__':
    dict_data = load_data(parsed_file_name().file)
    print(make_pretty_json(dict_data))
