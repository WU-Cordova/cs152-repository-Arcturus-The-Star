# Bistro Ordering System
Hello, and welcome to the Bistro Ordering System ReadMe!

Requirements:
* Pwinput (pip install pwinput)
# Important Note!!!
The password input is finicky! Make sure you're using the vscode option to run the files in a dedicated terminal or it will not work properly. You'll know it works if it masks your password with asterisks.
# Directory of important files:
* program.py - Run this to enter the usual system
* menu_editor.py - Edit the menu
* Reports/0_report_viewer.bat - Drag reports onto this to view them
* manage_users.py - Allows for the addition and removal of users

Any other files can probably be ignored. 

To log into anything with a login, use the username "admin" and the password "password123"

When program.py is run, it should bring up a login screen, and then a dashboard. Be careful to only run from an IDE, as the imports are far too messed up to work from the terminal (sorry, if I keep the mandated folder structure there's no way around it). The rest should be self-explanatory.

### Sample Run:
>Welcome to the Bistro Authentication System
> 
>Please log in
> 
>Username: admin    
> 
>Password: ***********
> 
>Login successful
>
>Welcome to the Bistro Ordering System
>
>Dashboard:
>
>1. Display Menu
>2. Take New Order
>3. View Open Orders
>4. Mark Next Order as Complete
>5. View End-of-Day Report
>6. Exit
>
> \>1
> 
>Menu:
>
>Mocha- \$7.5 small, \$8.25 large
>
>Latte- \$6.25 small, \$6.88 large
>
>Espresso- \$3.75 small, \$4.12 large
>
>Americano- \$5.25 small, \$5.78 large
>
>Cappuccino- \$5.75 small, \$6.33 large
>
>Press enter to return
> 
> Dashboard:
>
>1. Display Menu
>2. Take New Order
>3. View Open Orders
>4. Mark Next Order as Complete
>5. View End-of-Day Report
>6. Exit
>
>\>2
> 
>Enter the name of the desired drink
>
>\>latte
> 
>1. Small
>2. Large
>
>\>1
>
>Enter any other customization
> 
>\>lavender syrup
>1. Add more items
>2. Continue to name selection
>
>\>2
>
>Enter the name of the customer
>
>\>Bob
> 
>Order for Bob:
> 
>Small latte: \$6.25 - lavender syrup
> 
>Total price: \$6.25
>1. Confirm order
>2. Start over
>
>\>1
> 
>Dashboard:
>
>1. Display Menu
>2. Take New Order
>3. View Open Orders
>4. Mark Next Order as Complete
>5. View End-of-Day Report
>6. Exit
>
>\>3
> 
>Open Orders:
> 
>\--------------------------------------------
> 
>1. Order for Bob:
>
>Small latte: \$6.25 - lavender syrup
> 
>Total price: \$6.25
> 
>\--------------------------------------------
> 
>Press enter to return
> 
> Dashboard:
>
>1. Display Menu
>2. Take New Order
>3. View Open Orders
>4. Mark Next Order as Complete
>5. View End-of-Day Report
>6. Exit
>
>\>4
> 
>The next order is:
> 
>Order for Bob:
> 
>Small latte: \$6.25 - lavender syrup
> 
>Total price: \$6.25
> 
>1. Confirm completion
>2. Cancel and return
>3. 
>\>1
> 
>Dashboard:
>
>1. Display Menu
>2. Take New Order
>3. View Open Orders
>4. Mark Next Order as Complete
>5. View End-of-Day Report
>6. Exit
>
>\>5
> 
>Report for 04-16-2025 14-23:
> 
>Drink - Total Sold - Total Revenue
> 
>Mocha - 0 - 0
> 
>Latte - 1 - 6.25
>
>Espresso - 0 - 0
>
>Americano - 0 - 0
>
>Cappuccino - 0 - 0
>
>Total revenue: $6.25
>
>1. Save to file
>2. Return without saving
>
>\>1
> 
>Dashboard:
>
>1. Display Menu
>2. Take New Order
>3. View Open Orders
>4. Mark Next Order as Complete
>5. View End-of-Day Report
>6. Exit
>
>\>6
> 
The menu editor, as the name implies, edits the menu.

## Sample run:
>Welcome to the Bistro Authentication System
> 
>Please log in
>
>Username: admin
>
>Password: ***********
>
>Login successful
>
>Welcome to the Bistro Menu Editor
>
>Dashboard:
>
>1. Add a new item
>2. Remove an old item
>3. Exit
>
>\>1
> 
>Enter the name of the new item
> 
>\>cheese
> 
>Enter the price of the new item
> 
>\>5000000
> 
>Dashboard:
>
>1. Add a new item
>2. Remove an old item
>3. Exit
>
>\>2
> 
>Menu:
>
>mocha: 7.5
>
>latte: 6.25
>
>espresso: 3.75
>
>americano: 5.25
>
>cappuccino: 5.75
>
>cheese: 5000000.0
>
>Enter the name of the item to remove or cancel to leave
>
>\>cheese
> 
>Dashboard:
> 
>1. Add a new item
>2. Remove an old item
>3. Exit
>
>\>3


Drag report files (any .json file in the reports folder) onto 0_report_viewer.bat to view them.

## Sample run:

>Report for 04-16-2025 at 14-23:
> 
>Drink - Total Sold - Total Revenue
>
>Mocha - 0 - 0
>
>Latte - 1 - 6.25
>
>Espresso - 0 - 0
>
>Americano - 0 - 0
>
>Cappuccino - 0 - 0
>
>Total revenue: $6.25
>
>Press any key to continue . . .

The user management system does exactly what it says, use this to add or remove users.

## Sample run:

>Welcome to the Bistro Authentication System
> 
>Please log in
>
>Username: admin
>
>Password: ***********
>
>Login successful
>
>Welcome to the Bistro User Management System
>
>Dashboard:
>
>1. Add User
>2. Remove User
>3. Exit
>
>\>1
>
>Adding New User:
>
>Username:steve
>
>Password: *****
>
>User successfully added
>
>Dashboard:
>
>1. Add User
>2. Remove User
>3. Exit
>
>\>2
>
>Removing a User:
>
>Username:steve
>
>User successfully removed
>
>Dashboard:
>
>1. Add User
>2. Remove User
>3. Exit
>
>\>3


# Datastructure Choices:
* **Menu** - Dictionary: I used a dictionary for the menu because it is the easiest to translate to and from JSON files, and it made lookup easier. I did not use HashMap because it cannot be dumped into JSON. Dictionaries also have a lookup of O(1), versus the O(n) of an array, however it was mostly for the ease of being able to store the name of a menu item as a key and the Drink object as the value.
* **CustomerOrder** - CustomerOrder is a dataclass that stores the OrderItems in a LinkedList. This is because I need it to be resizable and iterable, and lookup is not important. 
* **Order Confirmation** - I used the string method of CustomerOrder to translate the stored data (order array and name) into a properly formatted order summary. This is for ease of simply printing the order object to the screen without having to create anything or store and update a confirmation value. The only trade-off for this method is that it requires re-calculating the total price each time the order is printed, which has a complexity of O(n).
* **Open Orders** - I used a Deque to store the open orders. This is not due to the double-endedness but simply because it is not restricted in size like a CircularQueue. A queue is useful because a FIFO system for retrieving orders is ideal, the first order should be completed before others. Using a LinkedList based queue has the tradeoff of making lookup very expensive, but luckily lookup is not required of a queue so this is not important.
* **Completed Orders** - I used a LinkedList to store completed orders. This is because I would like to store them in a resizable data structure (as to not take up unnecessary space) and iterate over them when compiling an end of day report. LinkedList has these features, and is relatively lightweight, so it seems ideal for this scenario. LinkedList has the advantage over Array by not being dependent on an outside library, and avoids the complexity of resizing.

# Bugs / Limitations:

The largest limitation of this program is the lack of security. Yes, it uses a cryptographically secure hash system with proper salting, but it's a limitation of storing the files locally that the login system can be easily bypassed. Other than that, the biggest limitation is the console interface versus a proper GUI, but this is unavoidable and outside the scope of the project. I have not encountered any bugs in the current version of the program.

# What I Would Add:

I feel as though I have run up to the ends of my knowledge, not time. There are many features (such as a GUI or hosting files on a server) that I am simply not capable of doing yet. 