from os import read, remove
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        
    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        file = open(self.filename)
        file.readline()
        file = str(self).split(" ")
        print(file)
        return file 
        
      

class WordList:
    def __init__(self, text):
        
        self.text = file
        pass


    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        
        punctuation = ['.' , ',' , ':', "'" , '"']
        for occurance in punctuation:
            file = str(self.text.remove(occurance,""))
        return file
        pass

   
    

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        pass
        STOP_WORDS = [
     '—', ' an ', ' and ', ' are ', ' as ', ' at ', ' be ', ' by ', ' for ', ' from ', ' has ', ' he ',
    ' i ', ' in ', ' is ', ' it ', ' its ', ' of ', ' on ', ' that ', ' the ', ' to ', ' were ',
     ' will ' , ' with ' , ' a ' ]
        for word in STOP_WORDS:
            file = str(self.text).replace(word," ")
        return file
    
 

    
    
        
    
    


    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        wordcount = {};
        for single_word in file: 
        wordcount[single_word] = wordcount.get(single_word, 0) + 1
        
        
        pass


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        pass
        wordcount = {};
        for single_word in file: 
            wordcount[single_word] = wordcount.get(single_word, 0) + 1
        sorted_wordcount = sorted(wordcount.items(), key=lambda seq: seq[1], reverse=True)
        for x in sorted_wordcount:
            print(x[0], x[1], "*"*(x[1]))


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        print(FileReader(file))
        word_list = WordList(reader.read_contents())
        print(word_list)
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
