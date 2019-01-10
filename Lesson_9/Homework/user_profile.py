def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Антон', 'Стах', age=33, hometown='Moscow')
print(user_profile)