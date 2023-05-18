MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def recusos_suficientes(ingredientes):
    """Mostra se tem ingredientes suficientes"""
    for item in ingredientes:
        if ingredientes[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_moedas():
    """Pede pela moedas e processa elas"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successful(pagamento_rec, drink_cost):
    """Compara se o pagamento é suficente e retorna o troco."""
    if pagamento_rec >= drink_cost:
        troco = round(pagamento_rec - drink_cost, 2)
        print(f"Here is ${troco} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Reduz os ingredients dos resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    comand = input("What would you like? (espresso/latte/cappuccino): ")
    if comand == "off":
        is_on = False
    elif comand == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[comand]

        if recusos_suficientes(drink["ingredients"]):
            pagamento = process_moedas()
            if transaction_successful(pagamento, drink["cost"]):
                make_coffee(comand, drink["ingredients"])








