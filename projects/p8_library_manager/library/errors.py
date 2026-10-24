class LibraryError(Exception):
    pass


class UnknownItemError(LibraryError):
    pass


class NotAvailableError(LibraryError):
    pass


class LimitReachedError(LibraryError):
    pass
