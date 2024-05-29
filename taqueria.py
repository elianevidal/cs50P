def main():
    cardapio = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    bill = 0.0
    while True:
        try:
            choice = input("Item: ")
            item =  choice.title()
            bill += cardapio[item]
            print("Total: $", bill)
        except (KeyError,ValueError, ZeroDivisionError):
            print(end="")
        except (EOFError):
            break

main()