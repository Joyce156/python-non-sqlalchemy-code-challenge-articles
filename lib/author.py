
from .article import Article

class Author:
    def __init__(self, name):
        # name must be a non-empty string; once set it cannot change
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 1:
            raise ValueError("Name must have at least 1 character.")
        self._name = name

    # name is read-only
    @property
    def name(self):
        return self._name

    # Return all Article instances written by this author
    def articles(self):
        result = []
        for a in Article.all:
            if a.author == self:
                result.append(a)
        return result

    # Return unique list of Magazine instances this author wrote for
    def magazines(self):
        mags = []
        for a in self.articles():
            if a.magazine not in mags:
                mags.append(a.magazine)
        return mags

    # Create and return a new Article linked to this author and given magazine/title
    def add_article(self, magazine, title):
        self.magazine = magazine
        self.title = title

        return Article
    # Return unique list of categories (strings) for magazines this author contributed to
    # Return None if no articles (matches the assignment)
    def topic_areas(self):
        mags = self.magazines()
        if len(mags) == 0:
            return None
        categories = []
        for m in mags:
            if m.category not in categories:
                categories.append(m.category)
        return categories
