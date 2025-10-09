# class Solution:
#     def minTime(self, skill: list[int], mana: list[int]) -> int:
#         n = len(skill)
#         m = len(mana)
        
#         start = [0] * m
#         start[0] = 0
        
#         for j in range(1, m):
#             max_start = 0
            
#             prefix_sum_curr = 0
#             prefix_sum_prev = 0
            
#             for i in range(n):
#                 prefix_sum_prev += skill[i] * mana[j-1]
                
#                 prev_finish = start[j-1] + prefix_sum_prev
                
#                 needed_start = prev_finish - prefix_sum_curr
#                 max_start = max(max_start, needed_start)
                
#                 prefix_sum_curr += skill[i] * mana[j]
            
#             start[j] = max_start
        
#         total_time_last_potion = sum(skill[i] * mana[m-1] for i in range(n))
#         return start[m-1] + total_time_last_potion
    
class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n = len(skill)
        m = len(mana)
        start = [0] * m
        skill_prefix = [0] * (n + 1)
        for i in range(n):
            skill_prefix[i + 1] = skill_prefix[i] + skill[i]
        for j in range(1, m):
            max_start = 0
            for i in range(n):
                prev_finish = start[j-1] + skill_prefix[i + 1] * mana[j-1]
                needed_start = prev_finish - skill_prefix[i] * mana[j]
                max_start = max(max_start, needed_start)
            start[j] = max_start
        return start[m-1] + skill_prefix[n] * mana[m-1] #