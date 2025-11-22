class Article:
    # keep every Article instance here (single source of truth for articles)
    all = []

    def __init__(self, author, magazine, title):
        # validate author lazily to avoid circular import at module import time
        from .author import Author
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance.")
        # validate magazine lazily
        from .magazine import Magazine
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        # validate title (string and length 5..50)
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be 5–50 characters.")

        # internal attributes (underscore = private)
        self.title = title      # title is read-only (no setter)
        self.author = author     # uses property setter to validate
        self.magazine = magazine # uses property setter to validate

        # save instance to the global list
        Article.all.append(self)

    # read-only title property
    @property
    def title(self):
        return self._title

    # author property (read/write)
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise TypeError("Author must be an Author instance.")
        self._author = value

    # magazine property (read/write)
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        self._magazine = value
