def make_auto(maker, model, **other_params):
    auto={'maker': maker, 'model': model}
    for key, value in other_params.items():
        auto[key] = value

    return auto

car = make_auto('subaru', 'outback', color = 'blue', tow_package = True)

for key, value in car.items():
    print(f'{key}: {value}')
