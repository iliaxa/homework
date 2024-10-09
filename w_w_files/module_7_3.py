def remove_punctuation(text):
    punctuation_for_replace = (',', '.', '=', '!', '?', ';', ':', ' - ')
    for p in punctuation_for_replace:
        text = text.replace(p, '')
    return text


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_without_p = remove_punctuation(file.read().lower())
                result = file_without_p.split()  # бахнуть множеством
                all_words[file_name] = result
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, file_words in all_words.items():
            if word.lower() in file_words:
                result[file_name] = file_words.index(word.lower()) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, file_words in all_words.items():
            if word.lower() in file_words:
                result[file_name] = file_words.count(word.lower())
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
