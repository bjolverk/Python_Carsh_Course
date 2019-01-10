def sandwich_maker(*components):
    """Функция эмулирует процесс создания сэндвича"""
    sandwich_build = ['Кусок хлеба']
    for component in components:
        sandwich_build.append(component)
    sandwich_build.append('Кусок хлеба')
    return sandwich_build


my_sandwich = sandwich_maker('кусок сыра', 'кусок ветчины', 'кусок колбасы')

print(my_sandwich)
