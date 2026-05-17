class Solution:
    """
    1.count s
    2.count t
    3.compare exact name
    """
    def isAnagram(self, s: str, t: str) -> bool:
        # if not s or not t:
        #     return False
        # if len(s) != len(t):
        #     return False
        # s_dic = {}
        # t_dic = {}
        # for i in s:
        #     s_dic[i] = s_dic.get(i,0) + 1
        # for j in t:
        #     t_dic[j] = t_dic.get(j,0) + 1
        # for ele in t_dic:
        #     if ele not in s_dic:
        #         return False
        #     if s_dic[ele] != t_dic[ele]:
        #         return False
        # return True
        dict_s = {}
        for i in s:
            dict_s[i] = dict_s.get(i,0) + 1
        
        for j in t:
            if j not in dict_s:
                return False
            dict_s[j] -= 1
        
        return not any(dict_s.values())
        



