# week05-4.py 與 724. Find Pivot Index 相似
# Leetcode 3546. Equal Sum Grid Partition I
# 是否可以一刀切，讓上、下，或左、右，相加一樣
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        # 將每個 row 內的值進行相加
        row_up_sum = [0]
        row_down_sum = [0]
        for i in range(m):
            row_up_sum.append(row_up_sum[-1] + sum(grid[i]))
            row_down_sum.append(row_down_sum[-1] + sum(grid[m-i-1]))
        row_down_sum = list(reversed(row_down_sum))
        # 將每個 col 內的值進行相加
        col_left_sum = [0]
        col_right_sum = [0]
        grid2 = list(zip(*grid)) # 轉置
        for j in range(n):
            col_left_sum.append(col_left_sum[-1] + sum(grid2[j]))
            col_right_sum.append(col_right_sum[-1] + sum(grid2[n-j-1]))
        col_right_sum = list(reversed(col_right_sum))
        # 觀察是否有相加一樣的值
        for i in range(1, m):
            if row_up_sum[i] == row_down_sum[i]:
                return True
        for j in range(1, n):
            if col_left_sum[j] == col_right_sum[j]:
                return True
        return False