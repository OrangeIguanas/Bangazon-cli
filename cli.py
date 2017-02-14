from Methods.CreateCustomer import *
# This is the CLI for interacting with our DB
print("""\
.----.   .--.  .-. .-. .---.   .--.  .---.  .----. .-. .-.
| {}  } / {} \ |  `| |/   __} / {} \{_   / /  {}  \|  `| |
| {}  }/  /\  \| |\  |\  {_ }/  /\  \/    }\      /| |\  |
`----' `-'  `-'`-' `-' `---' `-'  `-'`---'  `----' `-' `-'
                                                      """) 
print("""                    
      	    =*===
           $.  . $$$
           $ <    D$$
           $ __  $$$
     ,     $$$$  |
    ///; ,---' _ |----.
     \ )(           /  )
     | \/ \.   '  _.|  \              $
     |  \ /(   /    /\_ \          $$$$$
      \ /  (       / /  )         $$$ $$$
           (  ,   /_/ ,`_,-----.,$$  $$$
           |   <----|  \---##     \   $$
           /         \\\           |    $
          '   '                    |
          |                 \      /
          /  \_|    /______,/     /
         /   / |   /    |   |    /
        (   /--|  /.     \  (\  (_
         `----,( ( _\     \ / / ,/
               | /        /,_/,/
              _|/        / / (
             / (        ^-/, |
            /, |          ^-   
 """)
firstPage = input("Hello client developer! I am Bangazon the Centaur. I will be your virtual guide.")
nextPage = input("Press Enter to begin your journey.")

# Initiate a loop 
while True: 

  print(""" Enter a Number: 

      ******************************
         WELCOME TO BANGAZON API
      ******************************
      1.     Create a customer account
      2.     Choose active customer
      3.     Create Payment Option
      4.     Add a product to shopping cart 
      5.     Complete an Order
      6.     See product Popularity
      7.     Leave Bangazon
      """)
  # Store input values to pass as parameters in a new Customer argument 
  try:

    choice = int(input(">"))

    if choice == 1: 

      Customer.add_new()
      
    elif choice == 2:

      Customer.change_status()


        





  except ValueError: 
      print("ERROR")



                                                            
                                                            
                                                            