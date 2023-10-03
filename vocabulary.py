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

#define function for TTR after lemmatization
def vocab_richness(text):
    unnique_words=set(real_words(text))
    words=real_words(text)
    ttr=len(unnique_words)/len(words) * 100
    return ttr

#define function for ttr before lemmatization
def vocab_richness2(text):
    unnique_words2=set(punctuation_removed(text))
    words2=punctuation_removed(text)
    ttr2=len(unnique_words2)/len(words2) * 100
    return ttr2


#define a function for collocation
def collocation(text):
     text_object = nltk.Text(punctuation_removed(text))
     return text_object.collocations()

def main():

    
    text1 = read_book1()
    text2 = read_book2()

    

   
   #ttr after lemmatization
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

    print()

    
    #ttr before lematization
    ttr2_text1 = vocab_richness2(text1)
    ttr2_text2 = vocab_richness2(text2)

    if ttr2_text1 > ttr2_text2:
        print("Text 1 has a greater vocab richness")
        print(ttr2_text1, ">", ttr2_text2)
    elif ttr2_text1 == ttr2_text2:
        print("Both books have equal TTR")
    else:
        print("Text 2 has a greater TTR")
        print(ttr2_text2, ">", ttr2_text1)

    collocation_text1 = collocation(text1)
    
    print()
    print()
    collocation_text2 = collocation(text2)
    

if __name__ == "__main__":
    main()
