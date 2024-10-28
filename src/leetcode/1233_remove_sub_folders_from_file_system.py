from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(reverse=True)
        ans = []
        parent_folder = folder.pop()
        while folder:
            curr_folder = folder.pop()
            if curr_folder.startswith(parent_folder) and curr_folder[len(parent_folder)] == '/':
                continue
            ans.append(parent_folder)
            parent_folder = curr_folder
        ans.append(parent_folder)
        return ans


s = Solution()
print(s.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(s.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
print(s.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))
