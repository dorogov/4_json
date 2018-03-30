import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def made_pretty_json(dict_data):
    return json.dumbs(json_file, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', 
        '--file', 
        required=True, 
        metavar='ФАЙЛ',
        help='Путь до файла .json')
    args = parser.parse_args()
    dict_data = load_data(args.file)
    print(made_pretty_json(dict_data))
