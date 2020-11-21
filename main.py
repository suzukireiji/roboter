import csv
import os.path

from termcolor import colored

text = """
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

こんにちは！わたしはRobokoです！あなたの名前はなんですか？

＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
"""

text2 = """
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

{}さん。あなたの好きなレストランはどこですか？

＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
"""

text3 = """
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

{}さん。ありがとうございました！
良い一日を！さようなら。

＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
"""

text4 = """
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

わたしのオススメのレストランは{}です。
このレストランは好きですか？[Yes/No]

＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
"""

if __name__ == '__main__':
    print(colored(text, 'green'))
    name = input()
    if os.path.exists('amamama.csv'):
        with open('amamama.csv', 'r') as amamama:
            reader = csv.DictReader(amamama)
            for i in reader:
                print(i)
                print(colored(text4.format(i['NAME']), 'green'))
                x = input()
                x = x.capitalize()
                if x == 'Yes':
                    break
    print(colored(text2.format(name), 'green'))
    resutaurant = input()
    resutaurant = resutaurant.capitalize()
    print(colored(text3.format(name), 'green'))

    if os.path.exists('amamama.csv'):
        with open('amamama.csv', 'r') as d:
            reader = csv.DictReader(d)
            for i in reader:
                if i['NAME'] in resutaurant:
                    with open('amamama.csv', 'a') as d:
                        fieldnames = ['NAME', 'COUNT']
                        writer = csv.DictWriter(d, fieldnames=fieldnames)
                        writer.writerow({'NAME': resutaurant,
                                         'COUNT': 1})

            with open('amamama.csv', 'a') as d:
                fieldnames = ['NAME', 'COUNT']
                writer = csv.DictWriter(d, fieldnames=fieldnames)
                writer.writerow({'NAME': resutaurant,
                                 'COUNT': 1})
    else:
        with open('amamama.csv', 'w') as fr:
            fieldnames = ['NAME', 'COUNT']
            writer = csv.DictWriter(fr, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'NAME': resutaurant, 'COUNT': 1})

