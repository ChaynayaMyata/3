
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(7, 'rat', False)
print_params(b=25, )
print_params(c=[1, 2, 3])

values_list = ('zero', (1, 9, 1), False)
values_dict = {'a': 'Opps', 'b': 666, 'c': ['o', 'p', 's']}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('zero', False)
print_params(*values_list_2, 42)