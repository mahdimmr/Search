from flask import Blueprint, render_template
import json

bp = Blueprint('search', __name__, url_prefix='/', template_folder='templates')


def search_in_lyric(file, keyWord):
    res = {}
    c = 0
    for f in file['objects']:
        if keyWord in f['lyric']:
            c = c + 1
            res[f'res{c}'] = f'{keyWord} found in {f["title"]}'
            res[f'key{c}'] = f'{f["title"]}'
    return res


@bp.route('/search')
def search():
    with open("src.json", "r") as f:
        src = f.read()
    file = json.loads(src)
    keyWord = input("input a KeyWord\n")

    print(search_in_lyric(file, keyWord))
    return render_template('search.html', s=search_in_lyric(file, keyWord))
