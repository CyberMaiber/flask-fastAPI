from flask import Flask, render_template

app = Flask(__name__)


@app.get('/')
def root():
    return render_template('layout.html')


# @app.get('/students/')
# def students():
#     items = [
#         {
#             'name': 'Ivan',
#             'surname': 'Ivanov',
#             'age': 20,
#             'avg_mark': 4.9
#         },
#         {
#             'name': 'Ivan',
#             'surname': 'Kuznecov',
#             'age': 21,
#             'avg_mark': 5.0
#         },
#         {
#             'name': 'Ivan',
#             'surname': 'Sidorov',
#             'age': 19,
#             'avg_mark': 4.8
#         }
#     ]
#     return render_template('students.html', students=students)


@app.get('/jackets/')
def jackets():
    jackets = [
        {
            'title': 'Куртка 1',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/kur1.jpg'
        },
        {
            'title': 'Куртка 2',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/kur2.jpg'
        },
        {
            'title': 'Куртка 3',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/kur3.jpg'
        },
    ]
    return render_template('items.html', items=jackets, page_title='Куртки')

@app.get('/hats/')
def hats():
    hats = [
        {
            'title': 'Шапка 1',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/shp1.jpg'
        },
        {
            'title': 'Шапка 2',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/shp2.jpg'
        },
        {
            'title': 'Шапка 3',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/shp3.jpg'
        },
    ]
    return render_template('items.html', items=hats, page_title='Шапки')

@app.get('/boots/')
def boots():
    boots = [
        {
            'title': 'Чоботы 1',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/bot1.jpg'
        },
        {
            'title': 'Чоботы 2',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/bot2.jpg'
        },
        {
            'title': 'Чоботы 3',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'remains': '5 штук',
            'filename': 'img/bot3.jpg'
        },
    ]
    return render_template('items.html', items=boots, page_title='Боты')

if __name__ == '__main__':
    app.run(debug=True)