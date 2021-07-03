import nltk
from .Word import Word

class Sentence:
    def __init__(self, text: str) -> None:
        self._text = text
        self._tokens = nltk.word_tokenize(text)
        self._words = [Word(w) for w in self._tokens if w.isalpha()]
    @property
    def words(self):
        return [w for w in self._words]
    def remove_all_punctuation(self): # example of long method name
        return Sentence(' '.join([str(w) for w in self.words]))
    def __str__(self):
        return self._text