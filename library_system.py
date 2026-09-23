def print_help():
    print("\n===== Library Management System =====")
    print("Available commands:")
    print("  inputBook()                 - Returns a book object")
    print("  addBook(book)               - Add a new book to the library")
    print("  removeBook(book)            - Remove a book from the library")
    print("  title_bubbleSort()          - Sort the library alphabetically by title (bubble sort)")
    print("  year_insertionSort()        - Sort the library chronologically by year (insertion sort)")
    print("  title_linearSearch(target)  - Search for a book by title (linear search)")
    print("  year_binarySearch(target)   - Search for a book by year (binary search)")
    print("  printLib()                  - Print the full library")
  
class Book:
  def __init__(self,title,author,year,rating):
    self.title = title
    self.author = author
    self.year = year
    self.rating = rating
  def __str__(self):
    return(
    f"Title = {self.title}\n"
    f"Author = {self.author}\n"
    f"Year = {self.year}\n"
    f"Rating = {self.rating}\n"
    )
  def __eq__(self,other):
    if not isinstance(other,Book):
      return NotImplemented
    return (self.title.strip().lower() == other.title.strip().lower() and self.author.strip().lower() == other.author.strip().lower())
    
class Magazine(Book):
  def __init__(self,title,author,year,rating,issue):
    super().__init__(title,author,year,rating)
    self.issue = issue
  def __str__(self):
    return super().__str__() + f"Issue = {self.issue}\n"
    
class Library:
  def __init__(self):
    self.Books = []

  def addBook(self,book):
    if book not in self.Books:
      self.Books.append(book)
      print("Book has been added")
    else:
      print("Duplicate, Try Again")
      
  def removeBook(self,book):
    if book in self.Books:
      self.Books.remove(book)
      print("Book has been removed")
    else:
      print("Book is not part of library")
      
  def title_bubbleSort(self):
    n = len(self.Books)
    for i in range(n - 1):
      for j in range(n - i - 1):
        if self.Books[j].title > self.Books[j+1].title:
          self.Books[j],self.Books[j+1] = self.Books[j+1],self.Books[j]
    return self.Books

  def year_insertionSort(self):
    n = len(self.Books)
    for i in range(1,n):
      value_to_sort = self.Books[i].year
      while (i > 0) and (self.Books[i-1].year > value_to_sort):
        self.Books[i-1],self.Books[i] = self.Books[i],self.Books[i-1]
        i -= 1
    return self.Books
      
  def printLib(self):
    for i,book in enumerate(self.Books):
      print("***********************\n")
      print(f"Book #{i+1}")
      print(book)
      print("***********************\n")

  def inputBook(self):
    title=input("Enter title: ")
    author=input("Enter author: ")
    year=int(input("Enter year: "))
    rating=int(input("Enter rating: "))
    newBook = Book(title,author,year,rating)
    return newBook

  def title_linearSearch(self,target):
    for i in range(len(self.Books)):
      if self.Books[i].title.lower() == target.lower():
        print(f"Book #{i+1}, index = {i}")
        return i
    else:
      print("Book is not part of library")

  def year_binarySearch(self,target,start=0,end=None):
    if end == None:
      end = len(self.Books)-1
    if start > end:
      print("Book is not part of library")
      return -1
    middle = (start + end) // 2
    if target == self.Books[middle].year:
      print(f"Book #{middle+1}, index = {middle}")
      return middle
    if target < self.Books[middle].year:
      return self.year_binarySearch(target,start,middle-1)
    if target > self.Books[middle].year:
      return self.year_binarySearch(target,middle+1,end)
    
print_help()
