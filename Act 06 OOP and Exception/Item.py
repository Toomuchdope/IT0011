class Item:
    def __init__(self, item_id, name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}
    
    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                print("Error: Item ID already exists.")
                return
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item successfully added!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_item(self, item_id):
        item = self.items.get(item_id)
        if item:
            print(item)
        else:
            print("Error: Item not found.")
    
    def update_item(self, item_id, name=None, description=None, price=None):
        item = self.items.get(item_id)
        if item:
            if name:
                item.name = name
            if description:
                item.description = description
            if price is not None:
                try:
                    if price < 0:
                        raise ValueError("Price cannot be negative.")
                    item.price = price
                except ValueError as e:
                    print(f"Error: {e}")
                    return
            print("Item successfully updated!")
        else:
            print("Error: Item not found.")
    
    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item successfully deleted!")
        else:
            print("Error: Item not found.")
    
    def list_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

def main():
    manager = ItemManager()
    
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List All Items")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                item_id = input("Enter Item ID: ")
                name = input("Enter Item Name: ")
                description = input("Enter Item Description: ")
                price = float(input("Enter Item Price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid price input.")
        elif choice == '2':
            item_id = input("Enter Item ID to View: ")
            manager.read_item(item_id)
        elif choice == '3':
            item_id = input("Enter Item ID to Update: ")
            name = input("Enter New Name (leave blank to keep unchanged): ") or None
            description = input("Enter New Description (leave blank to keep unchanged): ") or None
            try:
                price_input = input("Enter New Price (leave blank to keep unchanged): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid price input.")
        elif choice == '4':
            item_id = input("Enter Item ID to Delete: ")
            manager.delete_item(item_id)
        elif choice == '5':
            manager.list_items()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()