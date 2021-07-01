class Word:
    def __init__(self, word: str):
        self._word = word
        # todo: validate word -- must be a single alpha word
    @property
    def length(self):
        return len(self._word)
    def __str__(self):
        return self._word
    