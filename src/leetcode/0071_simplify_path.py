class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for element in path:
            if element == '..' and stack:
                stack.pop()
            elif element in {'', '.', '/', '..'}:
                continue
            else:
                stack.append(element)
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/a/./b/../../c/"))
