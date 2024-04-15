def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    name, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found!")
        return None, None
    except Exception as e:
        print('Error while opening file')
        return None, None


    average = total // count if count else 0
    return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"