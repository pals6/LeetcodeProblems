#Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      #sliding window
        left=0
        right=0
        seen=set()
        max_len=0
        while right!=len(s):
            ch=s[right]
            while ch in seen: 
                seen.remove(s[left]) #shrink the window if char already oresent in the set
                left+=1
            seen.add(s[right])
            
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len
#time complexity O(n) to add/remove element from the set
