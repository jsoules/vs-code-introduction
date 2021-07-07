import nltk
import shoestring

# Comments have their own color too
def example1():
    s = shoestring.Sentence('This sentence is made up of words.')
    for i, w in enumerate(s.words):
        print(f'word {i}: {w}')
    print(s)
    if False:
        print("This code can never be reached")
        print("So it's less bright than the rest of the code.")

if __name__ == '__main__':
    nltk.download('punkt')
    example1()