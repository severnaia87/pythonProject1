import os

# # собираем текстовые файлы
# list_file = [elem for elem in os.listdir(path='pythonProject1') if elem.endswith('txt') and elem[0].isdigit()]
#
# my_dict_len = {}
# my_dict_text = {}
#
# for stroke in list_file:
#     file_slash = os.path.join('pythonProject1', stroke)
#     with open(file_slash, 'r', encoding='utf-8') as file_in:
#         read_file = file_in.read().splitlines()
#         my_dict_len[str(stroke)] = len(read_file)
#         my_dict_text[str(stroke)] = '\n'.join(read_file)
#
# my_dict_len = {key: value for key, value in sorted(my_dict_len.items(), key=lambda x: x[1])}
#
# with open('file_out.txt', 'w', encoding='utf-8') as file_out:
#     for stroke in my_dict_len:
#         print(f'Наименование файла: {stroke}', file=file_out)
#         print(f'Строки: {my_dict_len[stroke]}', file=file_out)
#         print(my_dict_text[stroke], file=file_out)
#         print(file=file_out)
def create_combined_list(file):
    file_list = os.listdir(file)
    combined_list = []

    for f in file_list:
        with open(directory + "/" + f) as cur_file:
            combined_list.append([f, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[3], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+') as newfile:
        for file in create_combined_list(file):
            newfile.write(f'File name: {file.txt[0]}\n')
            newfile.write(f'Length: {file.txt[1]} string(s)\n')
            newfile.write(f'Length1: {file.txt[1]} string(s)\n')
            for string in file[3]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')


create_file_from_directory('text', 'mytext')