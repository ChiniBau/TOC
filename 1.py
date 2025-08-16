def list_prefixes(s):
    for i in range(1, len(s) + 1):
        print(s[:i])

def list_suffixes(s):
    for i in range(len(s)):
        print(s[i:])

def list_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    for sub in sorted(substrings):
        print(sub)

def main():
    s = input("Enter a string: ")
    print("Menu:\n1. Prefixes\n2. Suffixes\n3. Substrings\n4. Exit")

    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice == '1':
            list_prefixes(s)
        elif choice == '2':
            list_suffixes(s)
        elif choice == '3':
            list_substrings(s)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
