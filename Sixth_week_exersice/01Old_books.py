the_book = input()
library_capacity = int(input())
books_cheked = 0
while library_capacity > 0:
    current_book = input()
    if current_book == the_book:
        print(f"You checked {books_cheked} books and found it.")
        break
    books_cheked += 1
    if library_capacity == books_cheked:
        print(f"The book you search is not here!")
        print(f"You checked {books_cheked} books.")
        break