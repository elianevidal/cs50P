def main():
   time = input("What time is it? ")
   hour = int(time.split(':')[0])
   min = int(time.split(':')[1])

   meal = float(hour+(min/60))
   convert(meal)


def convert(meal):
    if (7.0 <= meal <= 8.0):
        print("breakfast time")
    elif (12.0 <= meal <= 13.0):
            print("lunch time")
    elif (18.0 < meal <= 19.0):
            print("dinner time")

main()