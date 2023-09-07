def main():
    try:
        num = int(input("Enter an integer: "))
        
        if num < 0:
            raise ValueError("Please enter a non-negative integer.")
        
        binary_representation = bin(num)
        
        print(f"The binary representation of {num} is: {binary_representation}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
if __name__ == "__main__":
    main()
