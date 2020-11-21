import csv
import os.path

from termcolor import colored

import main

class Roboter(object):
    list = []

    def list_sort(self):
        return sorted(Roboter.list, key=lambda x:x['COUNT'], reverse=True)

    def make_csv(self):
        sorted_list = self.list_sort()
        with open('favorite_resutaurant.csv', 'w') as fr:
            fieldnames = ['NAME', 'COUNT']
            writer = csv.DictWriter(fr, fieldnames=fieldnames)
            writer.writeheader()
            for i in sorted_list:
                writer.writerow(i)


    def questionnaire(self):
        print(colored(main.text, 'green'))
        name = input()
        if Roboter.list != []:
            sorted_list = self.list_sort()
            for i in sorted_list:
                print(colored(main.text4.format(i['NAME']), 'green'))
                input()
        print(colored(main.text2.format(name), 'green'))
        resutaurant = input()
        resutaurant = resutaurant.capitalize()
        if Roboter.list != []:
            for i in Roboter.list:
                if i['NAME'] == resutaurant:
                    i['COUNT'] += 1
                    break
            else:
                Roboter.list.append({'NAME': resutaurant, 'COUNT': 1})
        else:
            Roboter.list.append({'NAME': resutaurant, 'COUNT': 1})
        self.make_csv()
        print(colored(main.text3.format(name), 'green'))

if __name__ == '__main__':
    roboter = Roboter()
    roboter.questionnaire()
    roboter2 = Roboter()
    roboter2.questionnaire()
    roboter3 = Roboter()
    roboter3.questionnaire()
    roboter4 = Roboter()
    roboter4.questionnaire()
