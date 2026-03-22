def generate_fibonacci_sequence(n):
    """
    Generates a Fibonacci sequence containing 'n' terms.
    A Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers.
    """
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        sequence.append(0)
        return sequence
    
    # Starting values for the sequence
    sequence = [0, 1]
    
    # Generate the remaining terms
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

def main():
    print("=" * 45)
    print("           FIBONACCI SEQUENCE GENERATOR")
    print("=" * 45)
    print("Welcome! This tool will generate a Fibonacci ")
    print("series based on the number of terms you specify.\n")
    
    while True:
        try:
            terms = int(input("Enter the number of terms to generate: "))
            if terms <= 0:
                print("⚠️ Please enter a positive integer greater than 0.\n")
            else:
                break
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number.\n")
            
    # Generate the series
    fib_series = generate_fibonacci_sequence(terms)
    
    # Display the result
    print(f"\n✅ The Fibonacci sequence with {terms} terms is:")
    print(" -> ".join(map(str, fib_series)))
    print("-" * 45)
    print("Thank you for using the Fibonacci Generator!")

if __name__ == "__main__":
    main()
