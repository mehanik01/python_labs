import re
import random
from collections import UserDict


class Synonyms():

    PATTERN = re.compile(r'(?P<key>\w+)\s*[-|—](?P<vals>.+)')

    def add_row_in_file(self, key, value):
        with open(self.filename, 'a') as f:
            f.write("{} - {}\n".format(key, value))

    def add_new(self, key):
        r = input('добавить новый синоним к {} [y]es [n]o? '.format(key)).strip()
        if r.lower() == 'y' or r.lower() == 'yes':
            new_w = input('введите новый синоним => ').strip().lower()
            l = self.synonyms_dict[key]
            if new_w and (new_w not in l):
                l.append(new_w)
                self.synonyms_dict[key] = list(set(l))
                self.add_row_in_file(key, new_w)

    @property
    def make_work(self):
        while True:
            w = input('Пожалуйста, введите слово: ').strip()
            if w:
                w = w.lower()
                synonyms = self.synonyms_dict.get(w, None)
                if synonyms:
                    print('синоним: {}'.format(random.choice(synonyms)))
                    self.add_new(w)
                else:
                    print(
                        'слово для поиска синонимов в словаре не найдено\n')

    def make_values(self, val):
        return list(set([str(i).lower().strip()
            for i in val.split(self.file_sep)]))

    def __init__(self, filename='synonyms.txt', file_sep=';'):
        pattern = re.compile(r'(?P<key>\w+)\s*[-|—](?P<vals>.+)')

        self.filename = filename
        self.file_sep = file_sep
        self.synonyms_dict = UserDict()
        with open(filename, 'r') as f:
            synonyms = f.read()
            result = Synonyms.PATTERN.findall(synonyms)

        name_set = set([i[0] for i in result])
        tup_idx = [(i[0], idx) for idx, i in enumerate(result)]
        result_ = []
        for i in name_set:
            res = list(filter(lambda item: item[0] == i, tup_idx))
            all_syn = [result[idx[1]][1] for idx in res]
            result_.append((i, ''.join(all_syn)))
        self.synonyms_dict = {
            item[0].lower(): self.make_values(
                item[1]) for item in result_}


if __name__ == '__main__':
    Synonyms().make_work