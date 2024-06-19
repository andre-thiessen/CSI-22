# Interface Component
class PizzaComponent:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost

# Concrete Component
class BasePizza(PizzaComponent):
    def get_description(self):
        return "Base Pizza"

    def get_cost(self):
        return 8.00 

# Decorator
class IngredientDecorator(PizzaComponent):
    def __init__(self, pizza):
        self.component = pizza

    def get_description(self):
        return self.component.get_description() + ' ' + PizzaComponent.get_description(self)

    def get_cost(self):
        return self.component.get_cost() + PizzaComponent.get_cost(self)

# Concrete Decorators
class Cheese(IngredientDecorator):
    cost = 2.00

    def __init__(self, pizza):
        IngredientDecorator.__init__(self, pizza)

class Tomato(IngredientDecorator):
    cost = 1.50

    def __init__(self, pizza):
        IngredientDecorator.__init__(self, pizza)

class Pepperoni(IngredientDecorator):
    cost = 2.50

    def __init__(self, pizza):
        IngredientDecorator.__init__(self, pizza)

class Mushroom(IngredientDecorator):
    cost = 1.75

    def __init__(self, pizza):
        IngredientDecorator.__init__(self, pizza)

class Ham(IngredientDecorator):
    cost = 1.00

    def __init__(self, pizza):
        IngredientDecorator.__init__(self, pizza)


# Usage
def main():
    pizza = BasePizza()
    print(f"Plain Pizza: {pizza.get_description()} - Cost: ${pizza.get_cost():.2f}")

    pizza_with_mozzarella = Cheese(pizza)
    print(f"Pizza with Cheese: {pizza_with_mozzarella.get_description()} - Cost: ${pizza_with_mozzarella.get_cost():.2f}")

    pizza_with_pepperoni = Pepperoni(pizza_with_mozzarella)
    print(f"Pizza with Cheese and Pepperoni: {pizza_with_pepperoni.get_description()} - Cost: ${pizza_with_pepperoni.get_cost():.2f}")

    pizza_with_everything = Mushroom(pizza_with_pepperoni)
    print(f"Pizza with Cheese, Pepperoni, and Mushroom: {pizza_with_everything.get_description()} - Cost: ${pizza_with_everything.get_cost():.2f}")

if __name__ == "__main__":
    main()