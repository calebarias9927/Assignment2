import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Create instances of SandwichMaker and Cashier
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            # Show the current resources report
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice in recipes:
            sandwich = recipes[choice]
            # Check if there are enough resources for the chosen sandwich
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                # Process payment
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich["cost"]):
                    # Make the sandwich if the transaction was successful
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
                    print(f"{choice.capitalize()} Sandwich is ready. Bon appetit!")

if __name__ == "__main__":
    main()
