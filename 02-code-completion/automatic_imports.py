# With syntax highlighting
import nltk
import shoestring

def example1():
    s = Sentence('This sentence is made up of words.') # Ctrl+Space to auto-import Sentence class
    for i, w in enumerate(s.words):
        print(f'word {i}: {w}')
    print(s)

if __name__ == '__main__':
    nltk.download('punkt')
    example1()

# need to do this so that shoestring package is in pylance scope I think
word1 = shoestring.Word('hello')