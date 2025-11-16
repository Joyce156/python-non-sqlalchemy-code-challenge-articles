# author.py
# Very simple beginner-friendly version

from .article import Article

class Author:
    def __init__(self, name):
        # Validate the name
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 1:
            raise ValueError("Name must have at least 1 character.")

        # Once set, name cannot change, so we use a normal variable
        self._name = name

    @property
    def name(self):
        return self._name

    # Do NOT allow changing the name, so no setter

    def articles(self):
        # Return all articles written by this author
        result = []
        for article in Article.all:
            if article.author == self:
                result.append(article)
        return result

    def magazines(self):
        # Return list of unique magazines
        mags = []
        for article in self.articles():
            if article.magazine not in mags:
                mags.append(article.magazine)
        return mags

    def add_article(self, magazine, title):
        # Create and return a new Article
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if len(mags) == 0:
            return None

        categories = []
        for mag in mags:
            if mag.category not in categories:
                categories.append(mag.category)
        return categories
