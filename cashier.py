class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickels + pennies
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True if payment is accepted, False if insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False