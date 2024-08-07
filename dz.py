import string
import os


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            if os.path.isfile(file_name):
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    content = content.lower()
                    content = content.translate(str.maketrans('', '', string.punctuation + ' -'))
                    words = content.split()
                    all_words[file_name] = words
            else:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}

        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                result[file_name] = position

        return result

    def count(self, word):
        word = word.lower()
        result = {}

        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))