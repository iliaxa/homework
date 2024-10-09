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
            with open(file_name, 'r') as file:
                file_without_p = remove_punctuation(file.read().lower())
                result = file_without_p.split() # бахнуть множеством
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



finder2 = WordsFinder('sample.txt', 'test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
