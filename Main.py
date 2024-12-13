import pandas as pd

input_file = 'web_clients_correct.csv'
output_file = 'descriptions.txt'

data = pd.read_csv(input_file)
data.columns = data.columns.str.strip()

def create_description(row, index):
    if row['sex'].lower() == 'male':
        action = 'совершил'
    elif row['sex'].lower() == 'female':
        action = 'совершила'
    else:
        action = 'совершил(а)'  # Если пол неизвестен

    # Форматирование строки в соответствии с вашим примером с нумерацией
    return (f"{index}. Пользователь {row['name']} {row['sex']} пола, "
            f"{row['age']} лет {action} покупку на {row['bill']} у.е. "
            f"с {row['device_type']} браузера {row['browser']}. "
            f"Регион, из которого совершалась покупка: {row['region']}.\n")

descriptions = []
for index, row in data.iterrows():
    description = create_description(row, index + 1)  # Нумерация с 1
    descriptions.append(description)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(descriptions)

print(f"Описание покупателей успешно записано в {output_file}.")





