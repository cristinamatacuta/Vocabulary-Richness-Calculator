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

#define a function for word tokenization
def word_fragmentation(text):
    words = [word.lower() for word in word_tokenize(text)]
    return words

#define a function to remove punctuation

def punctuation_removed(text):
    words = word_tokenize(text)  # Use NLTK's word_tokenize directly
    punctuation_removed = [re.sub(r"[^\w\s]", "", word) for word in words]
    return punctuation_removed




#define a function to lemmatize the words
def real_words(text):
    words=punctuation_removed(text)
    lematizer=nltk.stem.WordNetLemmatizer()
    real_words=[lematizer.lemmatize(word) for word in words]
    return real_words

#define function for TTR
def vocab_richness(text):
    unnique_words=set(real_words(text))
    words=real_words(text)
    ttr=len(unnique_words)/len(words)
    return ttr


#define a function for collocation
def collocation(text):
     text_object = nltk.Text(punctuation_removed(text))
     return text_object.collocations()

def main():

    
    text1 = read_book1()
    text2 = read_book2()

    #print unique words from book1
    unique_words_text1 = set(real_words(text1))
    print("Text 1 has", len(unique_words_text1), "unique words")

    #print unique words from book2
    unique_words_text2 = set(real_words(text2))
    print("Text 2 has", len(unique_words_text2), "unique words")

    #print all words from book1
    all_words1 = punctuation_removed(text1)
    print("Text 1 has", len(all_words1), "words")
    
    #print all words from book2
    all_words2 = punctuation_removed(text2)
    print("Text 2 has", len(all_words2), "words")

    ttr_text1 = vocab_richness(text1)
    ttr_text2 = vocab_richness(text2)

    if ttr_text1 > ttr_text2:
        print("Text 1 has a greater vocab richness")
        print(ttr_text1, ">", ttr_text2)
    elif ttr_text1 == ttr_text2:
        print("Both books have equal TTR")
    else:
        print("Text 2 has a greater TTR")
        print(ttr_text2, ">", ttr_text1)

    
    collocation_text1 = collocation(text1)
    

    collocation_text2 = collocation(text2)
    

if __name__ == "__main__":
    main()
