from data import MENU

off=False
profit=0
resources={
    'water':300,
    'milk':200,
    'coffee':100,
}

def show_resources():
    return f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nMoney: ${profit}"

def processing_coins(drink,coffees):
    print("Please insert coins")
    quartes=int(input("How many quarters: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    total=(quartes*0.25+dimes*0.10+nickles*0.05+pennies*0.01)
    if coffees[drink]['cost']>total:
        print("Sorry that's not enough money. Money refunded","$",total)
        return 0
    elif coffees[drink]['cost']==total:
        print("There is your drink!")
        return coffees[drink]['cost']
    elif coffees[drink]['cost']<total:
        change=round(total-coffees[drink]['cost'],2)
        print(f"There is your drink! Here is ${change} dollars in change")
        return coffees[drink]['cost']
        


    

while not off:
    response=input("What would you like? (espresso/latte/cappuccino): ").lower()

    if response=='report':
        print(show_resources())
    elif response=='off':
        off=True
    elif response=="espresso":
        if resources['water']>=MENU['espresso']['ingredients']['water'] and resources['coffee']>=MENU['espresso']['ingredients']['coffee']:
            resources['water']-=MENU['espresso']['ingredients']['water'] 
            resources['coffee']-=MENU['espresso']['ingredients']['coffee']
            profit+=processing_coins(response,MENU)
        else:
            print("Not enough ingredients")
    elif response=="latte":
        if resources['water']>=MENU['latte']['ingredients']['water'] and resources['coffee']>=MENU['latte']['ingredients']['coffee'] and resources['milk']>=MENU['latte']['ingredients']['milk']:
            resources['water']-=MENU['latte']['ingredients']['water'] 
            resources['coffee']-=MENU['latte']['ingredients']['coffee']
            resources['milk']-=MENU['latte']['ingredients']['milk']
            profit+=processing_coins(response,MENU)
        else:
            print("Not enough ingredients")
    elif response=="cappuccino":
        if resources['water']>=MENU['cappuccino']['ingredients']['water'] and resources['coffee']>=MENU['cappuccino']['ingredients']['coffee'] and resources['milk']>=MENU['cappuccino']['ingredients']['milk']:
            resources['water']-=MENU['cappuccino']['ingredients']['water'] 
            resources['coffee']-=MENU['cappuccino']['ingredients']['coffee']
            resources['milk']-=MENU['cappuccino']['ingredients']['milk']
            profit+=processing_coins(response,MENU)
        else:
            print("Not enough ingredients")
            
    else:
        print("Wrong entrance")
        off=True

    




               

               
