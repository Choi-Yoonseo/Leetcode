class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - round(purchaseAmount + (0 if purchaseAmount % 5 != 0 else 1), -1)