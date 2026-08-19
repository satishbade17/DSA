class Solution:
    def maxScore(cardPoints, k):
        left_sum = sum(cardPoints[:k])
        max_sum = left_sum

        right_sum = 0

        for i in range(1, k + 1):
            left_sum -= cardPoints[k - i]
            right_sum += cardPoints[-i]

            max_sum = max(max_sum, left_sum + right_sum)

        return max_sum