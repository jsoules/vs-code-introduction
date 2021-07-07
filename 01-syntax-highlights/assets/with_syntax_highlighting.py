# With syntax highlighting
import nltk
import shoestring

def example1():
    s = shoestring.Sentence('This sentence is made up of words.')
    for i, w in enumerate(s.words):
        print(f'word {i}: {w}')
    print(s)

if __name__ == '__main__':
    nltk.download('punkt')
    example1()


