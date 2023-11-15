from datetime import datetime, timedelta

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False
        self.due_date = None

    def display_info(self):
        return f"{self.item_id}: {self.title} by {self.author}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.now() + timedelta(days=14)
            print(f"Checked out: {self.display_info()}. Due date: {self.due_date.strftime('%Y-%m-%d')}")
        else:
            print("Item is already checked out.")

    def return_item(self):
        if self.checked_out:
            days_late = (datetime.now() - self.due_date).days
            late_fee = max(0, days_late) * 0.50
            self.checked_out = False
            self.due_date = None
            print(f"Returned: {self.display_info()}. {days_late} days late. Late fee: ${late_fee:.2f}")
        else:
            print("Item is not checked out.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        return f"{super().display_info()}, Genre: {self.genre}"

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}, Director: {self.director}, Duration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, item_id):
        super().__init__(title, "N/A", item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}, Issue Number: {self.issue_number}"

book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", item_id="1", genre="Classic")
book.check_out()
dvd = DVD(title="Inception", director="Christopher Nolan", item_id="2", duration=148)
dvd.check_out()
magazine = Magazine(title="Le Monde", issue_number=255, item_id="3")
magazine.check_out()
book.return_item()
dvd.return_item()
magazine.return_item()
