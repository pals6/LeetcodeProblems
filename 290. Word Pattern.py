class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        p2w={}
        w2p={}
        for key, value in zip(pattern,words):
            if key in p2w and p2w[key]!=value:
                return False
            if value in w2p and w2p[value]!=key:
                return False
            p2w[key]=value
            w2p[value]=key
        return True
