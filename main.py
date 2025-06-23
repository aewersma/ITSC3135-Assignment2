import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break

        elif choice == "report":
            for item, amount in sandwich_maker_instance.machine_resources.items():
                unit = "ounce(s)" if item == "cheese" else "slice(s)"
                print(f"{item.capitalize()}: {amount} {unit}")

        elif choice in recipes:
            recipe = recipes[choice]
            ingredients = recipe["ingredients"]
            cost = recipe["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)

        else:
            print("Invalid choice. Please select small, medium, large, report, or off.")


if __name__ == "__main__":
    main()
