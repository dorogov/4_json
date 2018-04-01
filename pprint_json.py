import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def make_pretty_json(json_data):
    return json.dumbs(json_data, ensure_ascii=False, indent=4, sort_keys=True)


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', 
        '--file', 
        required=True, 
        metavar='ФАЙЛ',
        help='Путь до файла .json')
    return parser.parse_args()
   
    
if __name__ == '__main__':
    args = parser()
    dict_data = load_data(args.file)
    print(make_pretty_json(json_data))
