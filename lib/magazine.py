# magazine.py
# Beginner-friendly simple version

from .article import Article

class Magazine:

    # Class-level list to store all magazines
    all_magazines = []

    def __init__(self, name, category):
        # Validate name
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be 2–16 characters.")
        
        # Validate category
        if not isinstance(category, str):
            raise TypeError("Category must be a string.")
        if len(category) < 1:
            raise ValueError("Category must have at least 1 character.")

        self._name = name
        self._category = category

        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be 2–16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if len(value) < 1:
            raise ValueError("Category must have at least 1 character.")
        self._category = value

    def articles(self):
        # Return all articles that belong to this magazine
        result = []
        for article in Article.all:
            if article.magazine == self:
                result.append(article)
        return result

    def contributors(self):
        # Return list of unique authors
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
        return authors

    def article_titles(self):
        my_articles = self.articles()
        if len(my_articles) == 0:
            return None
        titles = []
        for article in my_articles:
            titles.append(article.title)
        return titles

    def contributing_authors(self):
        counts = {}

        for article in self.articles():
            writer = article.author
            if writer not in counts:
                counts[writer] = 0
            counts[writer] += 1

        result = []
        for author in counts:
            if counts[author] > 2:
                result.append(author)

        if len(result) == 0:
            return None
        return result

    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None

        top_mag = None
        top_count = 0

        for magazine in cls.all_magazines:
            count = len(magazine.articles())
            if count > top_count:
                top_count = count
                top_mag = magazine

        return top_mag
