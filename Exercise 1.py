class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print("This is a publication.")

class Book(Publication):
    def __init__(self, name, author, page_count):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Book Name: " + self.name)
        print("Author: " + self.author)
        print("Page Count: " + str(self.page_count))
        print()

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        Publication.__init__(self, name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine Name: " + self.name)
        print("Chief Editor: " + self.chief_editor)
        print()

if __name__ == "__main__":
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    # Print information of both publications
    donald_duck.print_information()
    compartment_no_6.print_information()
