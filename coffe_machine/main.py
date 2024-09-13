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
            print("there is your drink")
        else:
            print("Not enough ingredients")




               

               
