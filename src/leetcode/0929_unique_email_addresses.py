from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            local = local.split('+')[0]
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)


s = Solution()
print(s.numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(s.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
