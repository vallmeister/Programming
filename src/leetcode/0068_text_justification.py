from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        widths = []
        curr_line = []
        curr_width = 0
        curr_words = 0
        for word in words:
            n = len(word)
            if curr_width + n >= maxWidth:
                lines.append(curr_line)
                curr_line = []
                widths.append(curr_width - curr_words + 1)
                curr_width = 0
                curr_words = 0
            if curr_width == 0:
                curr_line.append(word)
                curr_width = n
            elif curr_width + n < maxWidth:
                curr_line.append(word)
                curr_width += n + 1
            curr_words += 1
        else:
            lines.append(curr_line)
            widths.append(curr_width)
        ans = []
        m = len(lines)
        for i in range(m - 1):
            curr_line = lines[i]
            curr_width = widths[i]
            n = len(curr_line)
            if n == 0:
                continue
            elif n == 1:
                ans.append(curr_line[0].ljust(maxWidth))
            else:
                tmp = ''
                spaces = (maxWidth - curr_width) // (n - 1)
                extra_indices = (maxWidth - curr_width) % (len(curr_line) - 1)
                for j in range(n - 1):
                    tmp += curr_line[j]
                    tmp += ' ' * spaces
                    if j < extra_indices:
                        tmp += ' '
                tmp += curr_line[-1]
                ans.append(tmp)
        ans.append(' '.join(lines[-1]).ljust(maxWidth))
        return ans


s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
print(s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(s.fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], maxWidth=20))
print(s.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
