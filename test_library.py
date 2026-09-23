from library_system import Book, Magazine, Library
print("\n=== TEST 1: Duplicate detection ===")
test_lib1 = Library()
book_a = Book("Dune", "Frank Herbert", 1965, 5)
book_b = Book("Dune", "Frank Herbert", 1965, 5)  
test_lib1.addBook(book_a)
before_len = len(test_lib1.Books)
test_lib1.addBook(book_b)  
after_len = len(test_lib1.Books)
assert before_len == after_len == 1, "FAIL: a duplicate book was added — check your __eq__ method"
print("PASS: duplicate correctly rejected")
 
 
print("\n=== TEST 2: Bubble sort integrity ===")
test_lib2 = Library()
test_lib2.addBook(Book("Zebra", "Author Z", 2000, 3))
test_lib2.addBook(Book("Apple", "Author A", 1990, 4))
test_lib2.addBook(Book("Mango", "Author M", 2010, 2))
before_map2 = {b.title: b.year for b in test_lib2.Books}
test_lib2.title_bubbleSort()
after_titles2 = [b.title for b in test_lib2.Books]
assert after_titles2 == sorted(after_titles2), "FAIL: titles are not in alphabetical order"
for b in test_lib2.Books:
    assert b.year == before_map2[b.title], f"FAIL: {b.title}'s year got separated from it during sorting"
print("PASS: titles sorted correctly and each book's data stayed together:", after_titles2)
 
 
print("\n=== TEST 3: Insertion sort integrity ===")
test_lib3 = Library()
test_lib3.addBook(Book("Book C", "Author C", 2015, 3))
test_lib3.addBook(Book("Book A", "Author A", 1980, 5))
test_lib3.addBook(Book("Book B", "Author B", 1999, 4))
before_map3 = {b.title: b.author for b in test_lib3.Books}
test_lib3.year_insertionSort()
years3 = [b.year for b in test_lib3.Books]
assert years3 == sorted(years3), "FAIL: years are not in ascending order"
for b in test_lib3.Books:
    assert b.author == before_map3[b.title], f"FAIL: {b.title}'s author got separated from it during sorting"
print("PASS: years sorted correctly and each book's data stayed together:", years3)
 
 
print("\n=== TEST 4: Linear search, including edges ===")
test_lib4 = Library()
test_lib4.addBook(Book("First Book", "Author 1", 2001, 3))
test_lib4.addBook(Book("Middle Book", "Author 2", 2002, 4))
test_lib4.addBook(Book("Last Book", "Author 3", 2003, 5))
 
result_first = test_lib4.title_linearSearch("First Book")
assert result_first == 0, "FAIL: the first book was not found at index 0"
 
result_last = test_lib4.title_linearSearch("Last Book")
assert result_last == 2, "FAIL: the last book was not found — an off-by-one bug may still be present"
 
result_missing = test_lib4.title_linearSearch("Nonexistent Book")
assert result_missing is None, "FAIL: a book that was never added was somehow 'found'"
 
print("PASS: first, last, and missing titles all handled correctly")
 
 
print("\n=== TEST 5: Binary search, including edges ===")
test_lib5 = Library()
test_lib5.addBook(Book("Old Book", "Author X", 1950, 3))
test_lib5.addBook(Book("New Book", "Author Y", 2020, 4))
test_lib5.addBook(Book("Mid Book", "Author Z", 1985, 5))
test_lib5.year_insertionSort()  
years5 = sorted(b.year for b in test_lib5.Books)
print("Library sorted by year:", years5)
 
result_smallest = test_lib5.year_binarySearch(years5[0])
assert result_smallest != -1, "FAIL: the smallest year was not found"
 
result_largest = test_lib5.year_binarySearch(years5[-1])
assert result_largest != -1, "FAIL: the largest year was not found"
 
result_middle = test_lib5.year_binarySearch(years5[1])
assert result_middle != -1, "FAIL: the middle year was not found"
 
result_missing_year = test_lib5.year_binarySearch(1899)  
assert result_missing_year == -1, "FAIL: a year that doesn't exist was somehow 'found'"
 
print("PASS: smallest, largest, middle, and missing years all handled correctly")
 
 
print("\n=== TEST 6: Magazine polymorphism ===")
test_lib6 = Library()
mag = Magazine("National Geographic", "Various", 2023, 5, issue=145)
test_lib6.addBook(mag)
mag_str = str(mag)
assert "145" in mag_str, "FAIL: the issue number is missing from Magazine's printed output — add a __str__ override to Magazine"
print("PASS: Magazine's issue number appears in its printed output")
print(mag_str)
 
 
print("\n=== TEST 7: Remove ===")
test_lib7 = Library()
book_to_remove = Book("Removable Book", "Author R", 2005, 3)
test_lib7.addBook(book_to_remove)
before_remove_len = len(test_lib7.Books)
test_lib7.removeBook(book_to_remove)  
after_remove_len = len(test_lib7.Books)
assert after_remove_len == before_remove_len - 1, "FAIL: an existing book was not removed"
 
fake_book = Book("Never Added", "Nobody", 1900, 1)
before_fake_len = len(test_lib7.Books)
test_lib7.removeBook(fake_book)  
after_fake_len = len(test_lib7.Books)
assert after_fake_len == before_fake_len, "FAIL: removing a nonexistent book changed the library size"
print("PASS: remove works correctly for both existing and nonexistent books")
 
 
print("\n=== TEST 8: Edge cases — empty and single-item library ===")
empty_lib = Library()
empty_lib.title_bubbleSort()
empty_lib.year_insertionSort()
result_empty_binary = empty_lib.year_binarySearch(2000)
assert result_empty_binary == -1, "FAIL: binary search on an empty library should return -1, not crash or find something"
print("PASS: sorting and binary search handle an empty library without crashing")
 
single_lib = Library()
single_lib.addBook(Book("Only Book", "Solo Author", 2010, 5))
single_lib.title_bubbleSort()
single_lib.year_insertionSort()
result_single_binary = single_lib.year_binarySearch(2010)
assert result_single_binary == 0, "FAIL: binary search on a single-item library failed"
print("PASS: sorting and binary search handle a single-item library correctly")
 
print("\nNOTE: title_linearSearch and inputBook were not covered for the empty-library")
print("case here because they call input() interactively.")
 
print("\nAll automated checks finished. If no AssertionError appeared above, everything passed.")
