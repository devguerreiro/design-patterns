from typing import List


class Pizza:
    def __init__(self) -> None:
        self.dough: str | None = None
        self.sauce: str | None = None
        self.ingredients: List[str] = []

    def __str__(self) -> str:
        dough = f"Dough: {self.dough}"
        sauce = f"Sauce: {self.sauce}"
        ingredients = f"Ingredients: {', '.join(self.ingredients)}"
        return " | ".join([dough, sauce, ingredients])


class PizzaBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza()

    def choose_dough(self, dough: str):
        self.pizza.dough = dough
        return self

    def choose_sauce(self, sauce: str):
        self.pizza.sauce = sauce
        return self

    def add_ingredient(self, ingredient: str):
        self.pizza.ingredients.append(ingredient)
        return self

    def build(self):
        return self.pizza


class PizzaMaker:
    def prepare_margherita(self):
        return (
            PizzaBuilder()
            .choose_dough("thin")
            .choose_sauce("tomato")
            .add_ingredient("mozzarella")
            .add_ingredient("basil")
            .build()
        )


pizza_maker = PizzaMaker()
pizza = pizza_maker.prepare_margherita()

assert str(pizza) == "Dough: thin | Sauce: tomato | Ingredients: mozzarella, basil"

pizza = (
    PizzaBuilder()
    .choose_dough("thick")
    .choose_sauce("white")
    .add_ingredient("chicken")
    .add_ingredient("cream cheese")
    .build()
)

assert str(pizza) == "Dough: thick | Sauce: white | Ingredients: chicken, cream cheese"
