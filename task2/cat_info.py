def cats_info(path: str) -> dict:
    dict_list = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                id, name, age = line.strip().split(',')
                dict_list.append({'id': id, 'name': name, 'age': age})
    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print('Error while opening file')
        return None

    return dict_list

