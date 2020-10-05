class Solution:
    
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        new_path = []
        for _dir in dirs:
            if _dir == '.' or _dir == '':
                continue
            elif _dir == '..':
                try:
                    del new_path[-1]
                except IndexError:
                    pass
            else:
                new_path.append(_dir)
            
        return '/' + '/'.join(new_path)