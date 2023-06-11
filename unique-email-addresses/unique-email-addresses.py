class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sol = set()
        for each in emails:
            local,domain = each.split('@')
            curr = local.split('+')[0].replace('.','') + '@' + domain
            sol.add(curr)
        return len(sol)
