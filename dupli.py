items=input("Enter elements separated by spaces:").split()
unique_items=[]
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print("List after removing duplicates:",unique_items)
