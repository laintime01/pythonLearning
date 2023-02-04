class Solution(object):
    def maxProfit(self,price):
        """
        :param price: List[int]
        :return: int
        """
        max_val, p_min = 0,0
        for i in range(len(price)):
            p_min = min(p_min, price[i])
            max_val = max(max_val, price[i]-p_min)
        return max_val