from collections import OrderedDict


favorite_languge = OrderedDict()

favorite_languge['jen'] = 'python'
favorite_languge['sarah'] = 'c'
favorite_languge['edward'] = 'ruby'
favorite_languge['phil'] = 'python'

for name, languge in favorite_languge.items():
    print(name.title() + "'s favorite languge is " + languge.title())
