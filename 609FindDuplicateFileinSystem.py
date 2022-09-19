class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup = []
        dic = {}
        
        path = ''
        for directory in paths:
            for string in directory.split():
                if not '(' in string:
                    path = string
                else:
                    x = string.split('(')
                    file = x[0]
                    content = x[1][:-1]
                    file = path + "/" + file
                    if content in dic:
                        dic[content].append(file)
                    else:
                        dic[content] = [file]
        
        for content in dic.keys():
            if len(dic[content]) > 1:
                dup.append(dic[content])
            
        return dup
