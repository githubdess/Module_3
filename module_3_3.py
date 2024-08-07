def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [2, 'orange', 4.23]
values_list_2 = ['пост', 3.15]
values_dict = {'a': 888, 'b': 'строка', 'c': True}
print_params(False)
print_params(67, 'стрим')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
# Нельзя передать values_list и values_dict в функцию print_params, так как
# сколько элементов у нас принимает функция и сколько параметров она ожидает
print_params(*values_list_2, 42)
