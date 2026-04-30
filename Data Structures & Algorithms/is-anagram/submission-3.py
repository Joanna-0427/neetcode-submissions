class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        for i in s:
            s_dic[i] = s_dic.get(i,0) + 1
        for j in t:
            t_dic[j] = t_dic.get(j,0) + 1
        for ele in t_dic:
            if ele not in s_dic:
                return False
            if s_dic[ele] != t_dic[ele]:
                return False
        return True

