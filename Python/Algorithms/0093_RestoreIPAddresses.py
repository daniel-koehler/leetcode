class Solution:
    
    def valid_component(self, component: str) -> bool:
        return 0 <= int(component) <= 255 and (component[0] != '0' or component == '0')
    
    def backtrack(self, digits: str, ip: List[str], all_ips: List[str]):
        
        if not digits and len(ip) == 4:
            all_ips.append('.'.join(ip))
            return
        
        for i in range(min(3, len(digits))):
            
            if self.valid_component(digits[:i+1]):
                ip.append(digits[:i+1])
                self.backtrack(digits[i+1:], ip, all_ips)
                del ip[-1]
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return []
        all_ips = []
        self.backtrack(s, [], all_ips)
        return all_ips