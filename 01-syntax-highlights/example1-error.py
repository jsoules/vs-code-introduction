import nltk
import shoestring

# Comments have their own color too
def example1():
    s = shoestring.Sentence('This sentence is made up of words.')
    y = x
     s = 5
     s += 1
    for i, w in enumerate(s.words):
        print(f'word {i}: {w}')
    print(s)

if __name__ == '__main__':
    nltk.download('punkt')
    example1()