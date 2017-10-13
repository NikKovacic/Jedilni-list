print "Welcome to daily menu."

daily_menu = {}

while True:
    dish_name = raw_input("Please add a dish to daily menu: ")
    price = raw_input("Please enter dish price: ")
    daily_menu[dish_name] = price

    new = raw_input("Would you like to add new dish to daily menu?: ")

    if new.lower() == "no":
        break

print "Daily menu: %s" % daily_menu

with open("daily_menu.txt", "w+") as daily_menu_file:
    for dish in daily_menu:
        daily_menu_file.write("%s, %s EUR\n" % (dish, daily_menu[dish]))

print "Goodbye!"


