# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp_domains = defaultdict(int)
        ans = []
        for domain in cpdomains:
            freq, domain = domain.split()
            freq = int(freq)
            name = domain.split(".")
            for i in range(len(name)):
                dm = ".".join(name[i:])
                cp_domains[dm] += freq
        for j in cp_domains:
            ans.append(f"{cp_domains[j]} {j}")
        return ans