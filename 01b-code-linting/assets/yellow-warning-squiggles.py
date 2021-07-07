import nltk
import shoestring

def example1():
    s = shoestring.Sentence('This sentence is made up of words.')
    for i, w in enumerate(s.words):
        print('word {i}:\x {w}') # unsupported escape character
    
    print(s)

if __name__ == '__main__':
    nltk.download('punkt')
    example1()
    