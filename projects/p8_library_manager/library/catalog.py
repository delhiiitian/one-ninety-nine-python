"""The Library class: lending rules, search and reports."""

import functools
from contextlib import contextmanager
from datetime import date

from .errors import LimitReachedError, NotAvailableError, UnknownItemError
from .items import EBook, Item, Member


def logged(action):
    """Decorator: record every successful call in the library's activity log."""
    def decorator(method):
        @functools.wraps(method)
        def wrapper(self, member_id, item_id, *args, **kwargs):
            result = method(self, member_id, item_id, *args, **kwargs)
            self.activity.append(f"{action}: {member_id}, {item_id}")
            return result
        return wrapper
    return decorator


class Library:
    def __init__(self, name):
        self.name = name
        self.items: dict[str, Item] = {}
        self.members: dict[str, Member] = {}
        self.activity: list[str] = []

    # ----- the Python data model makes a Library feel built in -----
    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(sorted(self.items.values()))

    def __contains__(self, item_id):
        return item_id in self.items

    def __getitem__(self, item_id):
        try:
            return self.items[item_id]
        except KeyError:
            raise UnknownItemError(f"no item with id {item_id}") from None

    # ----- adding things -----
    def add(self, *items):
        for item in items:
            self.items[item.item_id] = item

    def join(self, member):
        self.members[member.member_id] = member
        return member

    # ----- lending -----
    @logged("borrow")
    def borrow(self, member_id, item_id, today=None):
        today = today or date.today()
        member = self.members[member_id]
        item = self[item_id]
        if item_id in member:
            raise NotAvailableError(f"{member.name} already has {item.title}")
        if len(member) >= member.max_loans:
            raise LimitReachedError(f"{member.name} has reached {member.max_loans} loans")
        if item.available <= 0:
            raise NotAvailableError(f"all copies of {item.title} are out")
        if not isinstance(item, EBook):
            item.on_loan += 1
        due = today + item.due_in()
        member.loans[item_id] = due
        return due

    @logged("return")
    def give_back(self, member_id, item_id, today=None):
        today = today or date.today()
        member = self.members[member_id]
        due = member.loans.pop(item_id)
        item = self[item_id]
        if not isinstance(item, EBook):
            item.on_loan -= 1
        return item.late_fee((today - due).days)

    @contextmanager
    def reading_room(self, member_id, item_id):
        """Borrow for use inside the building; always returned on exit."""
        self.borrow(member_id, item_id)
        try:
            yield self[item_id]
        finally:
            self.give_back(member_id, item_id)

    # ----- searching (generators: results are produced lazily) -----
    def search(self, text):
        text = text.lower()
        for item in self:
            author = getattr(item, "author", "")
            if text in item.title.lower() or text in author.lower():
                yield item

    def overdue(self, today):
        for member in self.members.values():
            for item_id, due in member.loans.items():
                if due < today and not isinstance(self[item_id], EBook):
                    yield member.name, self[item_id].title, (today - due).days

    def stats(self):
        kinds = {}
        for item in self.items.values():
            kinds[type(item).__name__] = kinds.get(type(item).__name__, 0) + 1
        return {
            "items": len(self),
            "by_type": kinds,
            "on_loan": sum(i.on_loan for i in self.items.values()),
            "members": len(self.members),
        }
