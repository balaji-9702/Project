items = {
        "chocalate" : "10",
        "Sugar": "25",
        "cool_Drinks" : "40"
    }


def list_of_items():
    
    
    values = list(items.keys())
    print('LIST OF ITEMS')
    print(values)
    selected_items = input("> Enter the required items  from the list : ")
    split_items = list(selected_items.split(','))
    print (type(split_items))
    calac_amt(split_items)
    
    add_items = input('Type YES if additional items needed ? ').lower()
    if add_items == 'yes':
       added_item=additional_item(split_items)
       split_items = split_items + added_item
       print(f'Purchased Items {split_items}')
       print('----------------------------') 
       calac_amt(split_items)
    else:
        print("Happy Shopping ! Welcome back :)")   
      
   
def additional_item(split_items):
    added_item =[]
    get_items = list(items.keys())
    print(get_items)
    new_item= input("Select the item : ")
    seg_item = list(new_item.split(','))        
    added_item = seg_item
    return added_item


def calac_amt(split_items):
    amt = 0
    for values in split_items:
         cart_item = items.get(values)
         print (f' {values} ->  Rs.{cart_item}')
         print('-----------------------------------------')
         amt = amt + int(cart_item)
    print(f'Total Amount : Rs.{amt}')


list_of_items()    