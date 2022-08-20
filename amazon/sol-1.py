class CartItem:
    def _init_(self, itemName, nextItem):
        self.itemName = itemName
        self.nextItem = nextItem

    def print(self):
        print(self.itemName)


def getShoppingCart(head, operations):
    left = head
    right = head

    while right.nextItem:
        right = right.nextItem

    for operation in operations:
        if operation[0] == "PUSH_HEAD":
            left = CartItem(operation[1], left)
        elif operation[0] == "PUSH_TAIL":
            right.nextItem = CartItem(operation[1], None)
            right = right.nextItem
        else:  # POP_HEAD
            left = left.nextItem

    return left


root = CartItem()

getShoppingCart()