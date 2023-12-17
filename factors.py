import sys
import factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorizations = factors.factorize_numbers(file_path)

    for factorization in factorizations:
        print(factorization)
