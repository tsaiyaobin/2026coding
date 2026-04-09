# week07-4.py 學習計畫 Stack 第 3 題目
# Leetcode 394. Decode String
# 數字代表重複的次數
class Solution:
    def decodeString(self, ss: str) -> str:
        ans = ""
        nums = 0
        temp = []
        for s in ss:
            if s.isdigit():
                nums = nums * 10 + int(s)
            elif s == '[': # 放入數字、字串
                print('遇到 "[" ')
                print('temp加入:',(nums, ans))
                print()
                temp.append((nums, ans))
                ans = ""
                nums = 0
            elif s == ']': # 取出數字、字串
                print('遇到 "]" ,取出數字、字串')
                count, ch = temp.pop()
                print(f'數字:{count}, 以前字串:{ch}')
                print(f'現有字串:', ans)
                ans = ch + ans * count
                print('以前的字串 + 數字 * 現有字串:',ans)
                print()
            else:
                ans += s
                print('加入字串:', ans)
                print()
        return ans
