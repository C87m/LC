# 929 Unique Email Addresses
# 実際に送信するメールは何通か

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_email = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".","")
            set_email.add(local+"@"+domain)
        return len(set_email)