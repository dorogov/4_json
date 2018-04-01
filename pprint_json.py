import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def make_pretty_json(json_content):
    return json.dumps(json_content, ensure_ascii=False, indent=4, sort_keys=True)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        metavar='ФАЙЛ',
        help='Путь до файла .json')
    return parser.parse_args()


if __name__ == '__main__':
    try:
        json_data = load_data(get_args().file)
    except IndexError:
        print('Ошибка! Вы не указали путь к файлу JSON.')
        print('Сработает, если написать "python pprint_json.py <путь к файлу>"')
    except FileNotFoundError:
        print('Ошибка! Система не нашла такой файл.')
        print('Пробуйте указать полный путь к файлу.')
    except ValueError:
        print('Ошибка. Файл должен быть в формате JSON.')
    else:
        print(make_pretty_json(json_data))
