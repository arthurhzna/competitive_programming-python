from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        res = []

        def dfs(num_str):
            if num_str:
                num = int(num_str)
                # batasi supaya tidak terlalu besar (misal 10^7 cukup)
                if num > 0 and num <= 10**7:
                    count = Counter(num_str)
                    if all(int(d) == c for d, c in count.items()):
                        res.append(num)
            # jangan lebih dari 7 digit (karena 10^7)
            if len(num_str) >= 7:
                return
            for d in '123456789':  # digit 1-9
                dfs(num_str + d)

        dfs('')

        # urutkan hasil
        res.sort()

        # cari smallest number > n
        for x in res:
            if x > n:
                return x
