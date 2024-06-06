import json
import re
from copy import deepcopy

from bs4 import BeautifulSoup
from dateutil.parser import parse

from .abstract_extractor import AbstractExtractor

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from markdownify import markdownify as md


class MarkdownExtractor(AbstractExtractor):
    def __init__(self):
        self.name = "markdown_extractor"

    def _markdown(self, item):
        """Returns the converted markdown of the extracted article."""

        url = item["url"]
        html = deepcopy(item["spider_response"].body)

        markdown = ""
        try:
            if html is None:
                request = urllib2.Request(url)
                # Using a browser user agent, decreases the change of sites blocking this request - just a suggestion
                # request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)
                # Chrome/41.0.2228.0 Safari/537.36')
                html = urllib2.build_opener().open(request).read()

            #html = BeautifulSoup(html, "lxml")
            markdown = md(html, strip=['a', 'nav'])
        except Exception as e:
            pass

        return markdown
