items = {
        "chocalate" : "10",
        "Sugar": "25",
        "cool_Drinks" : "40"
    }


def list_of_items():
    
    
    values = list(items.keys())
    print('LIST OF ITEMS')
    print(values)
    selected_items = input("> Enter the required items  from the list ")
    split_items = list(selected_items.split(','))
    print (split_items)
    calac_amt(split_items)
    """
    add_items = input('Type YES if additional items needed ? ').lower()
    if add_items == 'yes':
       to_be_added = additional_item(split_items)
       count = count(to_be_added)
       if count <= 1:
            append_comm = list(to_be_added.add(','))
            print(append_comm)
       print(count)
       print(to_be_added)
       print(split_items)
       result=split_items.extend(to_be_added)
       print(result)
      """
   
def additional_item(split_items):
    added_item =''
    get_items = list(items.keys())
    for lst1 in get_items:
        for lst2 in split_items:
            if lst1 != lst2:
                added_item = lst1
    #print(added_item)
    return added_item


def calac_amt(split_items):
    amt = 0
    for values in split_items:
         cart_item = items.get(values)
         print (f'{values} -> {cart_item}')
         amt = amt + int(cart_item)
    print(f'Total Amount {amt}')


list_of_items()    