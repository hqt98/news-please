class ComparerMarkdown:
    """Implements a compare method for markdown"""

    def extract(self, item, list_article_candidate):
        for article_candidate in list_article_candidate:
            if article_candidate.markdown != None:
                return article_candidate.markdown
