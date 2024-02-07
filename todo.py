# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp
# 

def add(list, item):
  # https://www.w3schools.com/python/python_lists_add.asp
 list.append(super_shop)
pass


def remove(list, index):

 list.pop(index)

pass


def clear(list):
 
 list.clear()
 

pass


def print_list(list):
  if list == 0:
    print("List is empty")
  else:
   print(list)
  pass


def show(list):
  print(list[index])
  pass

list = []
super_shop = []

print("List is empty now, what you want to do?")
while True:

  print("....")
  print("....")
  
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index "))

  if len(list) > 10:
   print("The list can't be longer than 10 elements!")
   list.clear()

   if choice == 1:
    super_shop = input("What you want to add?\n")
    list.append(super_shop)
    print(list)

  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    remove(list, index)
    print(list)

  elif choice == 3:
    clear(list)
    print(list)

  elif choice == 4:
    print(list)

  elif choice == 5:
    show(list)

  else:
    print("Invalid input")
