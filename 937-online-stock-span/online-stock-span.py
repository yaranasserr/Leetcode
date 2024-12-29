class StockSpanner:

    def __init__(self):
        # Initialize a stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # Start with a span of 1 for the current price
        # While the stack is not empty and the current price is greater than or equal to the price at the top of the stack
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]  # Add the span of the top element to the current span
        # Push the current price and its span to the stack
        self.stack.append((price, span))
        return span
