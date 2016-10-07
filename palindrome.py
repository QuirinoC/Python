not_aceptable_characters = [".",",","?","!","@","#","\"", "\'", \
                            "(", ")","'", " ","-",";","\n",'',"-"]
'''
    Copyright Quirino...
        jk use it as yours if you want.

    #Documenting after writing is boring
'''

#Realized classes are not that dificult, this class is realy useful
#This class makes it easier for me to do useful things with a string
'''
    I used a class because it was a pain for me naming variables
    This way i instantiate once then use the class
'''
class palindrome(object):
    #This __init__ thing creates the object itself
    '''
        Now with this class we could do something like
        Pstring = palindrome("Ana")
        And the class will make:
            -A filtered string                              (self.string)
            -A reversed string                              (self.reversed)
            -A splited string in case is not just a word    (self.listed)
            -A method that checks for palindrome string     (ispalindrome())
            -And has a method to create an filtered list    (flist())
            #NOTE:
                The methods of the class would be used as self.ispalindrome()
    '''
    def __init__(self, string):
        self.string = (filter(string, not_aceptable_characters))
        self.reversed = (self.string)[::-1]
        self.listed = string.split()
    def ispalindrome(self):
        if self.string == self.reversed:
            return True
        else:
            return False
    def flist(self):
        newList = []
        for i in self.listed:
            newList.append(filter(i,not_aceptable_characters))
        return newList

def filter(string,filter_list):
    #This function takes a string argument, and uses a filter that is a list
    #(See line 1) so the non desired character gets eliminated from the string
    new_word = ""
    for i in string:
        if i not in filter_list:
            new_word += i
    return new_word.lower()

def palindrome_(string):
    '''
        Oh boy this one was tricky.
        ---------------------------
        First we create a Pstring object using the palindrome class
        Now we can use all its variables and methods for check which kind
        Of palindrome the string is, i included 3 basic cases
    '''
    Pstring = palindrome(string)
    #First Case:
        #The Whole sentence is palindrome
    if Pstring.ispalindrome():
        print("\nThe whole string is character palindrome\n")


    ''' Thanks to the class i used above i saved myself 3 lines,
        And confusion when it comes to variable usage
        More readable code
    #IGNORE#
        Pstring = string
        FPstring = filter(Pstring,not_aceptable_characters)
        RFPstring = FPstring[::-1]
        if FPstring == RFPstring:
            print("\nThe whole thing is character palindrome\n")
    #IGNORE#
    '''

    ##########################################################
    #Second Case:
        #Show palindrome words in the string
    palindromeWords = []
    for i in Pstring.flist():
        Pword = palindrome(i)
        if i not in palindromeWords and Pword.ispalindrome():
            palindromeWords.append(i)
    ##########################################################
    if len(palindromeWords) > 0:
        print("\nThis words are palindrome:")
        for i in palindromeWords:
            print (i)
        print ()
    #Third case:
        #The string is palindrome in a words way like
        #Hola ana como te va te como ana Hola
    if Pstring.flist() == Pstring.flist()[::-1]:
        print ("This string is word palindrome\n")
    ##########################################################
def start():
    #This function takes user prompt to decide wheter the input will be a file
    #Or a user given string
    user_input = input(\
"Please input F to check a File or S to analize auser String: ")
    if user_input.upper() == "F":
        print("\n\
File must be in the same folder, \n\
Please write with extension, if the file is \n\
a .docx please write file.docx\n")
        #Since its very easy for the user to get the name of the file wrong
        #try will save the day
        try:
            file_ = open(input("Name of file: \n"),"r+")
            file_string = file_.read()
            file_.close()
            palindrome_(file_string)
        except:
            print ("There is no such file")
            start()
    elif user_input.upper() == "S":
        palindrome_(input("Please input the string to test: \n"))
    else:
        print ("Invalid Input")
        start()

start()
