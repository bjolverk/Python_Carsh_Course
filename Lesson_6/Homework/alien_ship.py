import random
colors = ['green', 'yellow', 'red', 'black']
scores_list= []
for i in range(10000):
    alien_color = random.choice(colors)
    scores = 0
    if alien_color == 'green':
        scores = 5
    elif alien_color == 'yellow':
        scores = 10
    elif alien_color == 'red':
        scores = 15
    else:
        scores = 3
    scores_list.append(scores)
    #print('You gain {} scores'.format(scores))

score_stat={}
for i in scores_list:
    if i not in score_stat.keys():
        score_stat[i] = 0
    else:
        score_stat[i]+=1
for key, value in score_stat.items():
    print("Значение {} встречалось {} раз".format(key, value))

favorite = max(score_stat.values())
print('Чаще всего выпадало {}'.format(list(score_stat.keys())[list(score_stat.values()).index(favorite)]))
