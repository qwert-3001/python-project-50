
def generate_diff(file1, file2):
    
    first_file = file1
    second_file = file2

    sorted_keys = sorted(set(first_file.keys() | set(second_file.keys())))
    diff_file = []

    for item in sorted_keys:
        if item not in second_file:
            #print(f'Во втором файле нету {item}')
            diff_file.append(f' - {item}: {first_file[item]}')
        elif item not in first_file:
            #print(f'Добавился файл {item}, со значение {second_file[item]}')
            diff_file.append(f' + {item}: {second_file[item]}')
        elif item in second_file and first_file[item] == second_file[item]:
            #print(f'Повторяется {item, first_file[item]} и {item, second_file[item]}')
            diff_file.append(f'   {item}: {first_file[item]}')
        else:
            #print(f'Айтем {item, first_file[item]} остался, но поменялся: {item, second_file[item]}')
            diff_file.append(f' - {item}: {first_file[item]}')
            diff_file.append(f' + {item}: {second_file[item]}')

    resualt = '{\n' + '\n'.join(diff_file) + '\n}'

    return resualt

