# Library Management System

A command-line library catalog written in Python, built to practice and demonstrate object-oriented programming and fundamental sorting/searching algorithms — implemented from scratch rather than relying on Python's built-in `sort()` or `in` operator.

## Intention

This program was created for me to practice my self-taught object-oriented programming and sorting/searching algorithms. I had prior experience with Python and basic data structures, but no formal background in OOP or these algorithms before building this — so this project was my way of learning them hands-on rather than being satisfied with just watching tutorials.

## What this project does

The program models a small library of books (and magazines) as objects, and lets you add, remove, sort, and search that collection. The point of the project wasn't just to get a working catalog — it was to implement the underlying algorithms manually, so the logic is visible and understood rather than hidden behind a library call.

## Features

- **`Book` class** — stores title, author, year, and rating, with a custom `__str__` for readable printing and a custom `__eq__` so two separately created `Book` objects with the same title and author are treated as duplicates.
- **`Magazine` class** — a subclass of `Book` that adds an `issue` number and overrides `__str__` to include it, demonstrating inheritance and polymorphism.
- **`Library` class** — holds a list of `Book`/`Magazine` objects and provides:
  - `addBook()` / `removeBook()`, with duplicate detection on add
  - `title_bubbleSort()` — sorts the catalog alphabetically by title
  - `year_insertionSort()` — sorts the catalog chronologically by year
  - `title_linearSearch(target)` — scans the catalog for a title, no ordering required
  - `year_binarySearch(target)` — searches for a year in O(log n) time, requires the catalog to already be sorted by year
  - `printLib()` — prints the full catalog
  - `inputBook()` — prompts the user to enter a new book's details

## Algorithms implemented

| Algorithm       | Used for          |
|-----------------|-------------------|
| Bubble sort     | Sort by title     | 
| Insertion sort  | Sort by year      |
| Linear search   | Find by title     | 
| Binary search   | Find by year      | 

Binary search only works correctly once the catalog has been sorted by the field being searched — `year_binarySearch` assumes `year_insertionSort()` has already been called. This precondition is intentional and mirrors why binary search is faster than linear search in the first place: it trades a one-time sorting cost for much faster lookups afterward.

## OOP concepts demonstrated

- **Encapsulation** — each `Book`/`Magazine` manages its own data; the `Library` manages the collection and the operations on it.
- **Inheritance** — `Magazine` extends `Book`, reusing its constructor via `super().__init__()` and adding only what's new (`issue`).
- **Polymorphism** — `Magazine.__str__()` overrides `Book.__str__()`, so printing a magazine automatically includes its issue number without the `Library` code needing to know the difference between a `Book` and a `Magazine`.
- **Operator overloading** — `Book.__eq__()` defines what "equal" means for two books, which is what makes duplicate detection in `addBook()` actually work.

## Project structure

```
.
├── library_system.py     # Book, Magazine, and Library classes, plus a demo run
├── test_library.py       # Automated tests covering sorts, searches, edge cases
└── README.md
```


## How to run

```
python library_system.py
```

This will populate the library with a handful of sample books, sort and search the catalog, and print the results.

## How to test

```
python test_library.py
```

Each test prints `PASS` if the behavior is correct, or raises an `AssertionError` describing exactly what went wrong. The suite covers:

- Duplicate detection
- Sort correctness (including that a book's title/author/year/rating stay together after sorting — an early version of this project had a bug where only the title field was swapped)
- Linear and binary search, including first/last/middle/missing-item edge cases
- Polymorphism (that `Magazine` actually prints its issue number)
- Removing existing and non-existing books
- Empty and single-item library edge cases

## Possible future improvements

- Generalize sorting to accept any field via a `key` function, rather than one method per field
- Add a `title_binarySearch()` to match `year_binarySearch()`
- Persist the catalog to a file (JSON/CSV) between runs
- Build a proper CLI menu instead of a linear demo script

## Author

Abdulmajeed Alsulimani
