
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True if all ingredients are available, False if not."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
