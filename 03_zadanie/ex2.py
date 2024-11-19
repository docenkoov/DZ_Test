from book import Book

library = [
    Book("Мастер и маргарита", "Булгаков"),
    Book("Поднятая целина", "Шолохов"),
    Book("Идиот", "Достоевский")
]
for book in library:
    print(f"{book.title}: {book.author}")
