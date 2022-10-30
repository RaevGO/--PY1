def get_count_char(str_):
    str_ = str_.lower()
    dict_alpha = {}
    for i in range(len(str_)):
        if str_[i].isalpha():
            if str_[i] in dict_alpha.keys():
                dict_alpha[str_[i]] += 1
            else:
                dict_alpha.update({str_[i] : 1})
    return dict_alpha

def frequency(dict_):#частота вхождения символа в словаре
    sum_alpha = sum(dict_.values())
    for i in dict_.keys():
        dict_[i] = dict_[i]/sum_alpha
    return dict_ #зачем эта функция, если под проверку она не попадает и ответ это количество, а не процент?

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
