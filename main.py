from Data import MENU

def report(ingredients):
    a = 0
    for i in ingredients:
        if a <=1:
            print(f"{i}: {ingredients[i]}ml")
        if a == 2:
             print(f"{i}: {ingredients[i]}g")
        if a > 2:
             print(f"{i}: ${ingredients[i]}")
        a+=1
def enoughMaterial(OnOfF, ingredientsMachine):
    general_data = MENU.get(OnOfF)
    ingredients = general_data.get("ingredients")
    #print(f"Ingridients of the coffee: {ingredients}")
    #print(f"Ingridientes necessaries{ingredientsMachine}")
    #ingredientsMachine_JustInCase = ingredientsMachine.copy()
    
    MaterialReady = True
    for i in ingredients:
        for j in ingredientsMachine:
            if i == j.lower():
                if ingredientsMachine[j] - ingredients[i] < 0:
                    MaterialReady = False
                    print(f"No enough: {i}")
                #else:
                 #   ingredientsMachine[j] = ingredientsMachine[j] - ingredients[i]
    #if MaterialReady == False:
     #   ingredientsMachine = ingredientsMachine_JustInCase
    #print(MaterialReady)
    return ingredientsMachine, MaterialReady
    #print(f"Then of validate materials: {ingredientsMachine}")

def InsertCoin(product, ingredientsMachine):
    general_data = MENU.get(product)
    cost = general_data.get("cost")

    print("Please, insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    totalCoins = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies  * 0.01)
    
    if totalCoins > 0 and totalCoins>=cost:
        buy = True
        change = totalCoins-cost
        ingredientsMachine["Money"] = ingredientsMachine["Money"] + cost
        return buy , change
    else:
        buy = False
        change = 0
        return buy , change
    
def FinishingBuy(Change, OnOfF):
    if Change > 0:
        print(f"Here is ${round(Change,2)} in change")
    print(f"Here is your {OnOfF}, enjoy")

    general_data = MENU.get(OnOfF)
    ingredients = general_data.get("ingredients")
    for i in ingredients:
        for j in ingredientsMachine:
            if i == j.lower():
                ingredientsMachine[j] = ingredientsMachine[j] - ingredients[i]
        

ingredientsMachine = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money" : 0
}
OnOfF = "On"
while(OnOfF!="Off"):
    OnOfF = input("What would you like? (espresso/latte/capuccino): ")
    if (OnOfF) == "Off":
        break
    elif OnOfF == "Report":
        report(ingredientsMachine)
    elif OnOfF == "espresso" or OnOfF == "latte" or OnOfF == "cappuccino":
        ingredientsMachine, ReadyMaterial = enoughMaterial(OnOfF, ingredientsMachine)
        if ReadyMaterial == True:
            #print(f"Im out {ReadyMaterial}")
            BuyAcepted, change = InsertCoin(OnOfF, ingredientsMachine)
            if BuyAcepted == True:
                FinishingBuy(change, OnOfF)
    else:
        print("Value error")
