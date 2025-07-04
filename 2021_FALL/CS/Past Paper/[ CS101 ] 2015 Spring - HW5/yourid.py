"""
Word class represents an word data (a piece of string).
Especially, this class supports comparison of two word objects
by implementing the 'edit distance' algorithm as the compareTo() method
"""
class Word(object) :
    """
    Internal data - an english word
    """
    data = ""
    
    """
    Constuctor (initializer) method.
    input : data (string)
    output : None
    """
    def __init__(self, word) :
        pass
        
    """
    String operator method.
    input : None
    output : a representative string of an object (string)
    """
    def __str__(self) :
        pass
    
    """
    Get an internal string data
    input : None
    output : a string which is intilaized by the constructor (string)
    """
    def getData(self) :
        pass
    
    """
    Get a difference between this and the other Word object.
    Specifically, this method returns 'the edit distiance' of
    two string data which belong to this and the other object.
    input : an other Word object
    output : a difference(edit distance) of this and the other object data
    """
    def compareTo(self, other) :
        pass
    
"""
Text class represents a collection of Word objects.
This class provides load() method that loads strings from a file and
make a list of Word objects.
"""
class Text(object) :
    """
    Internal data - Word object list
    """
    content = []
    
    """
    Constuctor (initializer) method.
    input : None
    output : None
    """    
    def __init__(self) :
        pass

    """
    String operator method.
    input : None
    output : a representative string of an object (string)
    """
    def __str__(self) :
        pass
    
    """
    Load content of a file and save them as a list of Word objects.
    input : a text file path
    output : None
    """    
    def load(self, textFilePath) :
        pass
    
    """
    Get internal content (a list of Word objects)
    input : None
    output : a list of Word objects which is loaded by the load() method.
    """
    def getContent(self) :
        pass
    
    """
    Set internal content (a list of Word objects)    
    input : a list of Word objects
    output : None
    """
    def setContent(self, words) :
        pass
    
    """
    Print internal content as plain text style.    
    input : None
    output : None
    """
    def printContent(self) :
        pass
    
"""
SpellingCorrector class represents an misspelling check algorithm.
"""
class SpellingCorrector(object) :
    
    """
    Internal data - Text Object
    """
    correctedText = Text()
    
    """
    Constuctor (initializer) method.
    In this constuctor,
    an Word object list for mispelling correction is created.    
    input : a file path of the dictionary file
    output : None
    """
    def __init__(self, dictionaryFile) :
        pass
    
    """
    Correct misspelled words using the mispelling correction
    which is intilaized by a constructor.    
    input : a Text class object
    output : new Text class object which is misspelling-corrected.
    """
    def correct(self, txt):        
        pass
    
def main() :
    
    # --------------------------------------------------------
    # Word object test code
    # --------------------------------------------------------    
    
    # Create an word object using a constructor
    w1 = Word("kaist 2014")
    w2 = Word("kiast 2015")
    
    # Test getData() method
    print w1.getData()
    print w2.getData()
    
    # Test __str__() method
    print w1
    print w2
    
    # Test compareTo() method
    print "Difference : " + str(w1.compareTo(w2))    
    
    
    # --------------------------------------------------------
    # Text object test code
    # --------------------------------------------------------
    
    # Create a text object using a constructor
    txt1 = Text()
    
    # Test load() method
    txt1.load("kaist1.txt")
    
    # Test __str__() method
    print "-------------------------------------------------"    
    print txt1
    print "-------------------------------------------------"
    
    # Test printContent() method
    txt1.printContent()
    print "-------------------------------------------------"
    
    
    # --------------------------------------------------------
    # SpellingCorrect object test code
    # --------------------------------------------------------    
    
    # Create a spelling corrector object using a constructor
    corrector = SpellingCorrector("dic.txt")
    
    # Test correct() method
    txt1_corrected = corrector.correct(txt1)
    
    print "-------------------------------------------------"    
    txt1_corrected.printContent()
    print "-------------------------------------------------"
    
    txt2 = Text()
    txt2.load("kaist2.txt")
    print "-------------------------------------------------"
    print txt2
    print "-------------------------------------------------"
    txt2.printContent()
    print "-------------------------------------------------"    
    
    txt2_corrected  = corrector.correct(txt2)
    print "-------------------------------------------------"
    txt2_corrected.printContent()
    print "-------------------------------------------------"
    
    txt3 = Text()
    txt3.load("kaist3.txt")
    print "-------------------------------------------------"
    print txt3
    print "-------------------------------------------------"
    txt3.printContent()
    print "-------------------------------------------------"    
    
    txt3_corrected  = corrector.correct(txt3)
    print "-------------------------------------------------"
    txt3_corrected.printContent()
    print "-------------------------------------------------"    
    
main()