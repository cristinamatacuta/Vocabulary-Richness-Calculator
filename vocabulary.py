from __future__ import division
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# define a function to open the files
def read_book1():

    with open("dorian.txt", "r", encoding="utf-8") as file_read:
        my_file1=file_read.read()
        return my_file1
def read_book2():
    with open('jekyll.txt', "r", encoding="utf-8") as file_read2:
        my_file2=file_read2.read()
        return my_file2
    
#define function for sentence fregmentation
def sentences_fragmented(text):
    sentences_fragmented=sent_tokenize(text)
    return sentences_fragmented

#define function for word tokenization
def words(text):
    # Tokenize words from the input text and convert them to lowercase
    words = [word.lower() for word in word_tokenize(text)]
 # Tokenize words from the input text
    return words

#remove puncutation
def clean_words(text):
    words_clean=words(text)
    clean_words=[re.sub(r"[^\w\s]", "", word) for word in words_clean]
    return clean_words

#lemmatize the words
def real_words(text):
    words_real=clean_words(text)
    lematizer=nltk.stem.WordNetLemmatizer()
    real_words=[lematizer.lemmatize(word) for word in words_real]
    return real_words

# function to make a set out of the real words
def real_words_set(text):
    real_words_set=set(real_words(text))
    return real_words_set

#function for vocabulary richness
def vocab_richness(text):
    words=real_words(text)
    set_words=real_words_set(text)
    vocab_richness=len(words)/len(set_words)
    return vocab_richness

def main():
    text1=read_book1()
    text2=read_book2()

    #vocabulary richness for text1
    text1_richness=vocab_richness(text1)

    #vocabulary richness for text2
    text2_richness=vocab_richness(text2)

    #comparing which books has more unique words based on their lenght

    if text1_richness > text2_richness:
        print("The Portert of Dorian Gray has more unique words")
    elif text1_richness==text2_richness:
        print("The two books have the same number of unique words")
    elif text1_richness<text2_richness:
        print("The Strange Case Of Dr. Jekyll And Mr. Hyde has more unique words")
    else:
        print("Not enough data")


if __name__ == "__main__" :
    main()
