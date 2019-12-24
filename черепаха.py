import turtle
import random
from collections import Counter

def diagram_data(languages):
    # languages = input()
    # languages = languages.split()
    # n_languages = set(languages)
    # unique_list = dict()
    # for languages_item in languages:
    #     unique_list[languages_item] = languages.count(languages_item)
    # res = dict()
    # dct = {x:x for x in range(5)}
    languagesnew = Counter(languages)
    for language in languagesnew:
        languagesnew[language] *= (360 / len(languages))
    return languagesnew
    # for i in unique_list:
    #     res[i] = 360 / len(languages) * unique_list[i]
    # return res


def paint_diagram(data, radius=150):
    tr = turtle.Pen()
    colors = ('red', 'blue', 'green', 'blue', 'orange')
    for language in data:
        tr.color(random.choices(colors), random.choices(colors))
        tr.begin_fill()
        tr.forward(radius)
        tr.left(90)
        tr.circle(radius, data[language])
        tr.left(90)
        tr.forward(radius)
        tr.left(180)
        tr.end_fill()

if __name__ == '__main__':
    languages = input()
    languages = languages.split()
    data = diagram_data(languages)
    paint_diagram(data)

turtle.mainloop()


# lst = [2**i for i in range(5)]