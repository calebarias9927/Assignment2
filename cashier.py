class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = 0
        try:
            total += int(input("how many dollars?: ")) * 1.00
            total += int(input("how many quarters?:")) * 0.25
            total += int(input("how many dimes?:")) * 0.10
            total += int(input("how many nickels?:")) * 0.05
            total += int(input("how many pennies?:")) * 0.01
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return 0
        return total

    def transaction_result(self, coins, cost):
        """Returns True when the payment is accepted, or False if money is insufficient."""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
        else:
            print("Exact amount received. No change needed.")
        return True