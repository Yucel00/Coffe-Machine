from Menu import MENU,resources

# our profit
case=0

# the part where we compare the order sources with our sources
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]<=resources[item]:
            return True
        else:
            return False

# the part where we update the source
def resources_update(order_ingredients):
    for item in order_ingredients:
        resources[item]=resources[item]-order_ingredients[item]


# the part where we show our resources
def report():
    for i in resources:
        print(f"{i}:{resources[i]}")
    print(f"Case: {case}")

# the part where we receive money input
def input_money():
    total=int(input("How Many Quarters>>"))*0.25
    total+=int(input("How Many dimes>>"))*0.1
    total+=int(input("How Many nickels>>"))*0.05
    total+=int(input("How Many pennies>>"))*0.01
    return total

# the part where we control money
def money_control(order_cost):
    total_money=input_money()
    if total_money==order_cost:
        return True
    elif total_money>order_cost:
        change=round(total_money-order_cost),2
        print(f"Here is ${change} in change.")
        global case
        case+=order_cost
        return True
    else:
        print("Not Enough Money")
        return False
def game():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice=="off":
            break
        elif choice=="report":
            report()
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                if money_control(drink["cost"]):
                    print("Your Coffe Is Here Thank You For Prefer Us")
                    resources_update(drink["ingredients"])
                else:
                    print("Sorry")
            else:
                print("Sory We Don't Have Enough ingredient Right Now")
game()
