def factorize_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]

        factorizations = []
        for num in numbers:
            for i in range(2, int((num ** 0.5)) + 1):
                if num % i == 0:
                    factorizations.append(f"{num}={int(num/i)}*{i}")
                    break
            else:
                factorizations.append(f"{num}={num}*1")

        return factorizations
    except Exception as e:
        return [f"Error: {e}"]
