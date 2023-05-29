# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class HtmlParser(object):
    def getUrls(self, url):
        """
        :type url: str
        :rtype List[str]
        """


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        urls = []

        def dfs(url):
            urls.append(url)
            for sub_url in htmlParser.getUrls(url):
                if sub_url.startswith(startUrl):
                    dfs(sub_url)

        dfs(startUrl)
        return urls


s = Solution()
