menu = {}

print("""----order----
   1: Add item
   2: Remove item
   3: View order
   4: Cancel order
""")

option = int(input("Enter an option: "))

while option != 0:
   if option == 1:
       item = input("Enter an item: ")
       price = int(input("Enter the price: "))
       menu[item] = price

   elif option == 2:
       item = input("Enter an item: ")
       del(menu[item])


   elif option == 3:
       for item in menu:
           print(item, ":", menu[item])


   elif option != 0:
       print("You didn't enter a valid number.")

   option = int(input("\n\nEnter an Option: "))

else:
   print("Order canceled! Have a nice day.")
