# # Последовательно печатаем каждую модель до конца списка
# # После печати каждая модель перемещается в список completed_models
#
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # Печатаем модель
#     print("Printing model: {}".format(current_design))
#     completed_models.append(current_design)
#
# # Вывод всех готовых моделей
#
# print("Выводим готовые модели:")
# for model in completed_models:
#     print(model)
def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Печатаем модель
        print("Printing model: {}".format(current_design))
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Вывод всех готовых моделей"""
    print("\nМы напечатали: ")
    for model in completed_models:
        print(model)

unprinted_designs = ['iphone case', 'robot pedant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)
