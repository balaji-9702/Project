import order_item_funs
import items



iscomplete = False

def list_of_items():
    
   #
 try:  
    values = list(items.items.keys())
    print('LIST OF ITEMS')
    print(values)
    selected_items = input("> Enter the required items  from the list : ")
    split_items = list(selected_items.split(','))
    order_item_funs.calac_amt(split_items)
    add_items = input('Type add to add items / remove  to remove items from selected list / Enter to finish  ').lower()
    if add_items == 'add':
       added_item=order_item_funs.additional_item(split_items)
       split_items = split_items + added_item
       print(f'Purchased Items {split_items}')
       print('-----------------------------------------') 
       order_item_funs.calac_amt(split_items)
       """
    elif add_items == 'remove':
        remove_item=removal_item(split_items)
        """

    else:
        print("Happy Shopping ! Welcome back :)")

 except TypeError:
    print("Invalid value : Please Enter the proper value")


list_of_items()