class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        res = []
        for d in dirs:
            if not res and d == '..':
                continue
            elif d == '.':
                continue
            elif d == '..':
                res.pop()
            elif d == '':
                continue
            else:
                res.append(d)
        return '/' + '/'.join(res)


s = Solution()
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/a/./b/../../c/"))
