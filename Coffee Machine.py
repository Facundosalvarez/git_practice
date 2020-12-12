class Coffe():
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550


    def __init__(self):
        self.action = input("Write action (buy, fill, take, remaining, exit):\n")
        if self.action == "buy":
            self.type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            self.buy()
        if self.action == "fill":
            self.fill()
        if self.action == "take":
            self.take()
        if self.action == "remaining":
            print("""\nThe coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money\n""".format(self.water, self.milk, self.coffee_beans, self.cups, self.money))

            self.__init__()
        if self.action == "exit":
            exit()

    def recipe(self):
        if self.type == "1":
            return {"water": 250, "milk": 0, "coffee beans": 16, "cost": 4}
        elif self.type == "2":
            return {"water": 350, "milk": 75, "coffee beans": 20, "cost": 7}
        elif self.type == "3":
            return {"water": 200, "milk": 100, "coffee beans": 12, "cost": 6}

    def buy(self):
        if self.type == "back":
            print("\n")
            self.__init__()
        elif self.water > self.recipe()["water"] and self.milk > self.recipe()["milk"] and self.coffee_beans > self.recipe()["coffee beans"] and self.cups > 1:
            self.water -= self.recipe()["water"]
            self.milk -= self.recipe()["milk"]
            self.coffee_beans -= self.recipe()["coffee beans"]
            self.cups -= 1
            self.money += self.recipe()["cost"]
            print("I have enough resources, making you a coffee!\n")
            self.__init__()
        elif self.water < self.recipe()["water"]:
            print("Sorry, not enough water!\n")
            self.__init__()
        elif self.milk < self.recipe()["milk"]:
            print("Sorry, not enough milk!\n")
            self.__init__()
        elif self.coffee_beans < self.recipe()["coffee beans"]:
            print("Sorry, not enough coffe beans!\n")
            self.__init__()
        elif self.cups < 1:
            print("Sorry, not enough cups!\n")
            self.__init__()



    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

        self.__init__()
    def take(self):
        print("I gave you ${}\n".format(self.money))
        self.money = 0
        self.__init__()
Coffe()