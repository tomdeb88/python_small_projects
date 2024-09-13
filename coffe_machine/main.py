from data import MENU

off=False
budget=0
resources={
    'water':100,
    'milk':50,
    'coffee':76,
}

def show_resources():
    return f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nBudget: ${budget}"

def processing_coins(drink,money,MENU):
    print("Please insert coins")
    quartes=int(input("How many quarters: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    total=(quartes*0.25+dimes*0.10+nickles*0.05+pennies*0.01)+money
    if MENU[drink]['cost']>total:
        print('Not enough money',total,budget)
    else:
        print(total,budget)
        return round(total - MENU[drink]['cost'],2)
        



while not off:
    response=input("What would you like? (espresso/latte/cappuccino): ").lower()

    if response=='report':
        print(show_resources())
    elif response=='off':
        off=True
    elif response=="espresso":
        if resources['water']>=50 and resources['coffee']>=18:
            resources['water']-=50
            resources['coffee']-=18
            budget=processing_coins(response,budget,MENU)
            print("there is your drink")
        else:
            print("Not enough ingredients")




               

               
