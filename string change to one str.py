# Define a function to check if a character is a vowel
def is_vowel(char):
    return char in ['A', 'E', 'I', 'O', 'U']

# Define a function to determine if Chef can reach CODETOWN from the given town
def can_reach_codetown(s):
    codetown = "CODETOWN"
    # Compare each character in the town with CODETOWN
    for i in range(8):
        # Check if characters are both vowels or both consonants
        if (is_vowel(s[i]) and not is_vowel(codetown[i])) or (not is_vowel(s[i]) and is_vowel(codetown[i])):
            return "NO"  # Chef can't reach CODETOWN if there's a mismatch
    return "YES"  # Chef can reach CODETOWN if all characters match

# Define the main function for input and output
def main():
    # Read the number of test cases
    t = int(input())
    # Loop through each test case
    for _ in range(t):
        # Read the town name for the current test case
        s = input().strip()
        # Check if Chef can reach CODETOWN and print the result
        result = can_reach_codetown(s)
        print(result)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
