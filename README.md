# Vocabulary Richness Calculator



This Python script calculates and compares the vocabulary richness of two text files. It can be used to determine which text has a richer vocabulary based on the ratio of unique words to the total number of words.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Customization](#customization)
- [Example](#example)
- [Author](#author)
- [License](#license)

## Prerequisites

- Python 3.x
- NLTK library (Natural Language Toolkit)

You can install NLTK using pip:
```bash
pip install nltk
```




## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Place Text Files**: Place the text files you want to analyze in the same directory as this script.
   
3. **Run the Script**: Open your terminal or command prompt, navigate to the project directory, and execute the following command:

   ```bash
   python vocabulary_richness.py
   ```

## Customization
   You can easily modify this script to work with other text files by changing the file names in the read_book1 and read_book2 functions.

Feel free to adjust the lemmatization or tokenization methods to suit your specific requirements.

## Example
Suppose you have two text files, "dorian.txt" and "jekyll.txt," containing the text of "The Portrait of Dorian Gray" and "The Strange Case Of Dr. Jekyll And Mr. Hyde," respectively. Running this script will tell you which book has a richer vocabulary.

## Author
Cristina Matacuta

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

License
This project is licensed under the MIT License - see the LICENSE.md file for details
