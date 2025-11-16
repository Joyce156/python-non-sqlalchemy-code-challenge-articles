# article.py
# Beginner-friendly version

class Article:

    # Store all Article instances
    all = []

    def __init__(self, author, magazine, title):
        # Validate author
        from .author import Author
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance.")

        # Validate magazine
        from .magazine import Magazine
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")

        # Validate title
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be 5–50 characters.")

        # Store values
        self._title = title
        self._author = author
        self._magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    # No setter: title cannot change after creation

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise TypeError("Author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")
        self._magazine = value
