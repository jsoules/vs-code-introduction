# Demo automatic imports

import nltk

def example1():
    # Ctrl+Space to auto-import Sentence class
    s = Sentence('This sentence is made up of words.')
    for i, w in enumerate(s.words):
        print(f'word {i}: {w}')
    print(s)

if __name__ == '__main__':
    nltk.download('punkt')
    example1()

word1 = shoestring.Word('hello')