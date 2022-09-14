import items
   
def additional_item(split_items):
    added_item =[]
    get_items = list(items.items.keys())
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
         cart_item = items.items.get(values)
         print (f' {values} ->  Rs.{cart_item}')
         print('-----------------------------------------')
         amt = amt + int(cart_item)
    print(f'Total Amount : Rs.{amt}')


  