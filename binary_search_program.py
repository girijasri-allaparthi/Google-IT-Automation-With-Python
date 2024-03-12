#!/usr/bin/env python3

def find_item(inputlist, item):
 #Returns True if the item is in the list, False if not.
  l=sorted(inputlist)
  if len(inputlist) == 0:
   return False


 #Is the item in the center of the list?
  middle = len(inputlist)//2
  if inputlist[middle] == item:
   return True


 #Is the item in the first half of the list?
  if item < inputlist[middle-1]:
   #Call the function with the first half of the list
   return find_item(inputlist[:middle], item)
  else:
   #Call the function with the second half of the list
   return find_item(inputlist[middle:], item)


  return False


list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]
list_of_names.sort()
#####for binary search need to give the sorted input######

print(find_item(sorted(list_of_names), "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False

