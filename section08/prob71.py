
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords

list_stop = [x for x in stopwords.words('english')]
#print(list_stop)

def bool_stop(s):
    return s.lower() in list_stop

def test_stop():
    assert bool_stop(".") == False, 'No.1'
    assert bool_stop("a") == True, 'No.2'
    assert bool_stop("of") == True, 'No.3'
    assert bool_stop("apple") == False, 'No.4'

if __name__ == "__main__":
    print(bool_stop('a'))
    print(bool_stop('0'))
    print(bool_stop('ofteN'))

    test_stop()

    print(list_stop)