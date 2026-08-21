class Solutions:
    def maxDepth(s):
        current_depth=0
        max_depth=0
        for char in s:
            if char=='(':
                current_depth+=1
                max_depth=max(current_depth,max_depth)
            elif char==')':
                current_depth-=1
        return max_depth
    s = "(1+(2*3)+((8)/4))+1"
    print(maxDepth(s))