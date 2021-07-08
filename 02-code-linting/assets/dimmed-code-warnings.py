import nltk
import shoestring
import numpy # import dimmed if unused

def example1():
    s = shoestring.Sentence('This sentence is made up of words.')
    w1 = s.words[0] # variable is dimmed if unused
    for i, w in enumerate(s.words):
        print(f'word {i}: {w}')
    if False:
        # Code is dimmed if unreachable
        print('code is dimmed if unreachable')

# function dimmed if unused
def _example2():
    print('unused example')

if __name__ == '__main__':
    nltk.download('punkt')
    example1()