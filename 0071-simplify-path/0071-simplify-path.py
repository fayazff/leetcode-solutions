class Solution:
    def simplifyPath(self, path: str) -> str:
        dumy=path.split("/")
        output=[]
        for ch in dumy:
            if ch == "" or ch == ".":
                continue
            elif ch == "..":
                if output:
                    output.pop()
            else:
                output.append(ch)
        return "/" + "/".join(output)

            
