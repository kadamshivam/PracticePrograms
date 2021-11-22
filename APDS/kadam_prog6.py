#Written by Shivam Sanjay Kadam
#Date: 11/19/2021

class Book:
    
    book_File_Name = "BookShop.txt"                       #Class Variable called book_File_Name
      
    def __init__(self, title = "", authorLastName = "", publicationDate = "", price = 0.0):
                                                         #Set the book details
        self._title = title
        self._authorLastName = authorLastName
        self._publicationDate = publicationDate
        self._price = price 
                
   
    def getTitle(self):                                 #Get the title of the book
        return self._title
    
   
    def getAuthorsLastName(self):                        #To get the Author last name
        return self._authorLastName
    
   
    def getPublicationDate(self):                       #To know the publication date
        return self._publicationDate
    
    
    def getPrice(self):                                 #Get the price of the book
        return str(self._price)

    #Print the string        
    def __str__(self):
        printLine = self.getTitle() + ", " + self.getAuthorsLastName() + ", " + self.getPublicationDate() + ", " + self.getPrice()
        return printLine
    
                                                    
    def write_To_File(self, fileName):
        bookFile = open(fileName, 'a')
                                                      
        bookFile.write(self.__str__() + "\n")
        bookFile.close()
    
                                                     
    def read_From_File(self, fileName):
        bookList = []
        try:
            file = open(fileName, "r")
                            
            lines = file.read().splitlines()
            for line in lines:                
                self._title, self._authorLastName, self._publicationDate, self._price, bookType = line.split(",")
                bookList.append([self._title, self._authorLastName, self._publicationDate, self._price, bookType])
            return bookList
                                                   
        except FileNotFoundError:        
            print("{} NOT FOUND!".format(fileName))
            print("Kindly ensure the input file is in the same location where the Python program is running and try again")
            return []
        except Exception as ex:
            print("File open error")       
            print(ex)
            print("Kindly ensure the input file is in the same location where the Python program is running and try again")
            print("Exiting the program - Execution Terminated !!!")
            return []

                                      #Hardcover book class
class Hardcover(Book):
    def __init__(self, title = "", authorLastName = "", publicationDate = "", price = 0.0):
                                      
        self.bookType = "Hardcover"
        
                                      #Call the Book constructor
        super().__init__(title, authorLastName, publicationDate, price)                
    
                                         #String representation for Hardcover class object
    def __str__(self):
        printLine = super().__str__() + ", " + self.bookType
        return printLine
        

class Softcover(Book):
    def __init__(self, title = "", authorLastName = "", publicationDate = "", price = 0.0):
                                            #Set the bookType
        self.bookType = "Softcover"
        
                                         #Call the Book constructor
        super().__init__(title, authorLastName, publicationDate, price)
        
    
                                         #String representation for Hardcover class object
    def __str__(self):
        printLine = super().__str__() + ", " + self.bookType
        return printLine
        
                    
                                        #Function to check if number is valid 
def isValidNumber(number):
    try:
        number = float(number)
        if number < 0:
            print("Only positive numbers are allowed")
            return False
        else:                        
            return True
    except ValueError:
        print("Entered value is not a valid number")
        return False
    
#Add a book
def addBook():    
    title = input("Enter the book title: ")
    lastName = input("Enter the author last name: ")
    publicationDate = input("Enter the publication date: ")
    validPrice = False
    while (validPrice == False):
        price = input("Enter the price of the book: ")
        if isValidNumber(price):
            validPrice = True
        else:
            validPrice = False
    bookType = input("1 - For Hardcover book\n2 - Softcover book\nEnter your choice: ")
    if bookType not in ["1", "2"]:
        print("Invalid book type entered.Defaulting the book type to Hardcover book")
        bookType = "1"
    if bookType == "1":
        hcBook1 = Hardcover(title, lastName, publicationDate, price)
        hcBook1.write_To_File(Book.book_File_Name)
        print("Book added successfully")
    elif bookType == "2":
        scBook1 = Softcover(title, lastName, publicationDate, price)
        scBook1.write_To_File(Book.book_File_Name)
        print("Book added successfully")

#View a book
def viewBook():    
                                                
    book = Book()
                                                
    bookList = book.read_From_File(Book.book_File_Name)
    bookFound = False
                                                #Get the authors name from the user
    searchLastName = input("Enter the author last name: ")
                                            
    for bookDetail in bookList:        
        title = bookDetail[0]
        authorLastName = bookDetail[1]
        publicationDate = bookDetail[2]
        price = bookDetail[3]
        bookType = bookDetail[4]
        if searchLastName.lower() in authorLastName.lower():
            bookFound = True
            print("Title: {}, Author Name: {}, Publication Date: {}, Price: {}, Book Type: {}".format(title, authorLastName, publicationDate, price, bookType))
    if bookFound == False:
        print("Book with author name {} not found".format(searchLastName))
            
def main():
    exitProcessing = False
    
    while (exitProcessing == False):                
        userChoice = input("\n1 - Add a book\n2 - View a book\n3 - Exit\nEnter your choice: ")
        if (userChoice == "1"):
                                                    
            addBook()
            exitProcessing = False
        elif (userChoice == "2"):
           
            viewBook()                              
            exitProcessing = False
        elif (userChoice == "3"):
            print("You choose to exit. Good Bye have a nive day!!!")
            exitProcessing = True
        else:
            print("Invalid choice entered. Enter a valid choice")
            exitProcessing = False


if __name__ == '__main__':        
    main()





