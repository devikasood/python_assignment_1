def insert_element(lst):
    element = input("Enter the element to insert: ")
    position = int(input("Enter the position to insert (0-based index): "))
    lst.insert(position, element)
    print("Element inserted successfully!")

def delete_by_value(lst):
    element = input("Enter the element to delete: ")
    if element in lst:
        lst.remove(element)
        print("Element deleted successfully!")
    else:
        print("Element not found in the list.")

def delete_by_position(lst):
    position = int(input("Enter the position to delete (0-based index): "))
    if 0 <= position < len(lst):
        del lst[position]
        print("Element deleted successfully!")
    else:
        print("Invalid position. Element not deleted.")

def delete_slice(lst):
    start = int(input("Enter the start position for the slice (0-based index): "))
    end = int(input("Enter the end position for the slice (0-based index): "))
    if 0 <= start < len(lst) and 0 <= end < len(lst) and start <= end:
        del lst[start:end+1]
        print("Slice deleted successfully!")
    else:
        print("Invalid slice range. Slice not deleted.")

def main():
    my_list = []  # Create an empty list

    while True:
        print("\nMenu:")
        print("1. Insert element")
        print("2. Delete by value")
        print("3. Delete by position")
        print("4. Delete a slice")
        print("5. Print the list")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_element(my_list)
        elif choice == '2':
            delete_by_value(my_list)
        elif choice == '3':
            delete_by_position(my_list)
        elif choice == '4':
            delete_slice(my_list)
        elif choice == '5':
            print("Current list:", my_list)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
