def main():

    grocery = {}

    while True:
        try:
            item = input()
            update_grocery_list(grocery,item.upper())
        except EOFError:
            for i in grocery:
                print(grocery[i],i)
            break

def update_grocery_list(grocery, item):
    if item in grocery:
        ##add or update item
        grocery.update({item : grocery[item]+1})
        return True
    else:
        grocery.update({item : 1})

main ()