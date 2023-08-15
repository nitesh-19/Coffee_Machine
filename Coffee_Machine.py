### Commands available ###
# 'off' to turn off the machine
# 'report' to print all the resources currently available in the coffee machine

import numpy as np
import logo
# Resources currently available in the coffee machine
resources = {
    "Water": 5000,
    "Milk": 2000,
    "Coffee": 500,
    "Money": 0.0,
}
# Choices of coffee available to the user with its requirements and cost
choices = [
    {
        "ESPRESSO": {
            "Water": 100,
            "Milk": 60,
            "Coffee": 20,
            "Money": 1.0,
        }},
    {
        "LATTE": {
            "Water": 80,
            "Milk": 100,
            "Coffee": 35,
            "Money": 2.0,
        }},
    {
        "CAPPUCCINO": {
            "Water": 50,
            "Milk": 200,
            "Coffee": 45,
            "Money": 2.5,
        }}]


def find_index(choice_of_coffee):
    """
    Searches through a list of dictionaries and returns the index of the search term.
    :param choice_of_coffee: String of coffee name
    :return: integer index of the input
    """
    choice_of_coffee = choice_of_coffee.upper()
    for index in range(0, len(choices)):
        for choice_itr in choices[index]:
            if choice_itr == choice_of_coffee:
                return index
            else:
                continue


def get_report():
    """
    prints the current resources available in the coffee machine
    :return: None
    """
    units = ["ml", "ml", "g", "$"]
    index = 0
    for resource in resources:
        print(f"{resource}: {resources[resource]}{units[index]}")
        index += 1


def process_coins():
    """
    Asks the user to input various types of coins, calculates the total of all the coins
    :return: Total Dollar value of the coins as a float
    """
    coins = ["quarters", "dimes", "nickels", "pennies"]
    for index in range(0, 4):
        no_of_coins = int(input(f"Input number of {coins[index]}: "))
        coins[index] = no_of_coins
    value = np.array(coins) * np.array([0.25, 0.10, 0.05, 0.01])
    return round(value.sum(), 2)


def make_coffee(choice_of_coffee):
    """
    Checks if the resources are sufficient to make the type of coffee requested
    :param choice_of_coffee: String of coffee name
    :return: None
    """
    choice_of_coffee = choice_of_coffee.upper()
    if resource_sufficient(choice_of_coffee, resources):
        for resource in resources:
            if resource == "Money":
                continue
            resources[resource] -= choices[find_index(choice_of_coffee=choice_of_coffee)][choice_of_coffee][resource]
        print(logo.coffee_cup)
        print(f"Here is your {choice_of_coffee.title()}. Enjoy!.")

    else:
        pass


def resource_sufficient(choice_of_coffee, available_resources):
    """
    Checks if the coffee machine has the resources to make the requested type of coffee and updates the resources
    after using them. Also keeps track of the money inserted
    :param choice_of_coffee: String of coffee name
    :param available_resources: Resources currently available in the machine in a form of dictionary
    :return: True if all requirements met, False if not
    """
    choice_of_coffee = choice_of_coffee.upper()
    for ingredient in choices[find_index(choice_of_coffee=choice_of_coffee)][
        choice_of_coffee]:  # Loop through the list of dictionary to process particular ingredients.
        if ingredient == "Money":
            money_inserted = process_coins()
            money_index = find_index(choice_of_coffee=choice_of_coffee)
            if money_inserted == choices[money_index][choice_of_coffee][
                ingredient]:
                resources["Money"] += money_inserted
                continue
            elif money_inserted > choices[money_index][choice_of_coffee][
                ingredient]:
                change = money_inserted - choices[money_index][choice_of_coffee][
                    ingredient]
                money_inserted -= change
                resources["Money"] += money_inserted
                print(f"Here is ${round(change, 2)} dollars in change.")

            else:
                print("Sorry that's not enough money. Money refunded.")
                return False
        return_val = choices[find_index(choice_of_coffee=choice_of_coffee)][choice_of_coffee.upper()][ingredient]
        if return_val is not None:
            if return_val <= available_resources[ingredient]:
                continue
            else:
                print(f"Sorry there is not enough {ingredient.lower()}.")
                return False
    return True


turn_off = 0

while turn_off == 0:
    print(logo.logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        turn_off = 1
        break
    if choice == "report":
        get_report()
    else:
        make_coffee(choice_of_coffee=choice.lower())
