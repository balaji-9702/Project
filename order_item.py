items = {
        "chocalate" : "10",
        "Sugar": "25",
        "cool_Drinks" : "40"
    }

iscomplete = False

def list_of_items():
    
   #
 try:  
    values = list(items.keys())
    print('LIST OF ITEMS')
    print(values)
    selected_items = input("> Enter the required items  from the list : ")
    split_items = list(selected_items.split(','))
    calac_amt(split_items)
    add_items = input('Type add to add items / remove  to remove items from selected list / Enter to finish  ').lower()
    if add_items == 'add':
       added_item=additional_item(split_items)
       split_items = split_items + added_item
       print(f'Purchased Items {split_items}')
       print('-----------------------------------------') 
       calac_amt(split_items)
       """
    elif add_items == 'remove':
        remove_item=removal_item(split_items)
        """

    else:
        print("Happy Shopping ! Welcome back :)")

 except TypeError:
    print("Invalid value : Please Enter the proper value")     
      
   
def additional_item(split_items):
    added_item =[]
    get_items = list(items.keys())
    print(get_items)
    new_item= input("Select the item : ")
    seg_item = list(new_item.split(','))        
    added_item = seg_item
    return added_item

"""
def removal_item(split_items):
    print(split_items)
    rm_itm =[]
    rm_items = input (f'Type the item to be removed from the selected list :')
    rm_itm = rm_items
    print(rm_itm)
    for rm in split_items:
        if rm == rm_itm:
         split_items = split_items-rm_itm
         print(split_items)    
"""

def calac_amt(split_items):
    amt = 0
    for values in split_items:
         cart_item = items.get(values)
         print (f' {values} ->  Rs.{cart_item}')
         print('-----------------------------------------')
         amt = amt + int(cart_item)
    print(f'Total Amount : Rs.{amt}')


list_of_items()    