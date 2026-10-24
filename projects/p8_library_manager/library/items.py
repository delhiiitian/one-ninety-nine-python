"""The things a library holds, and the people who borrow them."""

from dataclasses import dataclass, field
from datetime import timedelta


@dataclass
class Item:
    item_id: str
    title: str
    year: int
    copies: int = 1
    on_loan: int = 0
    loan_days = 14                      # class attribute, shared by all items

    @property
    def available(self) -> int:
        return self.copies - self.on_loan

    def due_in(self) -> timedelta:
        return timedelta(days=self.loan_days)

    def late_fee(self, days_late: int) -> int:
        return max(days_late, 0) * 5

    def __str__(self):
        return f"[{self.item_id}] {self.title} ({self.year}){self.byline()} - {self.status()}"

    def byline(self) -> str:
        return ""

    def status(self) -> str:
        return f"{self.available}/{self.copies} in"

    def __lt__(self, other):            # lets sorted() order items by title
        return self.title.lower() < other.title.lower()


@dataclass
class Book(Item):
    author: str = "Unknown"
    pages: int = 0

    def byline(self) -> str:
        return f" by {self.author}"


@dataclass
class EBook(Book):
    size_mb: float = 1.0
    loan_days = 7

    @property
    def available(self) -> int:         # digital copies never run out
        return self.copies

    def late_fee(self, days_late: int) -> int:
        return 0                        # e-books simply expire

    def status(self) -> str:
        return "e-book, always in"


@dataclass
class Member:
    member_id: str
    name: str
    max_loans: int = 3
    loans: dict = field(default_factory=dict)    # item_id -> due date

    def __len__(self):
        return len(self.loans)

    def __contains__(self, item_id):
        return item_id in self.loans
