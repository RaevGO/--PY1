import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file, separator=',', new_line='\n'):
    list_ = []
    json_form = []
    with open(input_file, 'r') as f:
        while True:  # переделываем csv в list[list]
            line = f.readline()
            list_.append(line.replace(new_line, '').split(separator))
            if not line:
                break

        for i in range(1, len(list_[:-1])):  # добавляем словарей в json_format
            dict_ = {}
            for j in range(len(list_[i])):
                dict_.update({list_[0][j]: list_[i][j]})
            json_form.append(dict_)

    return json_form


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))