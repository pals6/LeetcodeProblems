class Solution:
    def decodeString(self, s: str) -> str:
        count_stack=[]
        str_stack=[]
        num=0
        curr=""
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch) #handle multiple digits
            elif ch=="[":
                count_stack.append(num)
                str_stack.append(curr)
                num=0
                curr=""
            elif ch=="]":
                rep=count_stack.pop()
                prev=str_stack.pop()
                curr=prev+(curr*rep)
            else: #for letters
                curr+=ch
        return curr
      #Time: O(n) (each char processed once). Space: O(n) for stacks/output.
