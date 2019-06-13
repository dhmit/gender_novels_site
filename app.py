# python imports
import os

# 3rd party imports
from flask import Flask, render_template, abort
import markdown2


app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


# These function calls render the individual pages of the overall website so that the
# landing page is able to link to them through the navbar

@app.route('/')
def render_overview():
    return render_markdown_any('gender_novels_overview', title='Gender in Novels, 1770–1922')


@app.route('/info/team.html')
def render_team():
    return render_template('team.html')


@app.route('/info/pronoun_adjective_analysis')
def render_adjective():
    female_adjectives = [('Beautiful', -6606), ('Pretty', -4348), ('Sweet', -4119), ('Lady', -3058),
                         ('Lovely', -2205), ('Dear', -1926), ('Soft', -1922), ('Happy', -1527),
                         ('Queen', -1198), ('Girlish', -1027), ('Delicate', -987), ('Graceful',
                                                                                    -945),
                         ('Bright', -932), ('Rosy', -771), ('Alone', -755), ('Pale', -697),
                         ('Down', -665), ('Childish', -657), ('Slim', -645)]
    male_adjectives = [('Old', 53565), ('Good', 48647), ('Last', 48647), ('Great', 40234), ('First',
                                                                                    28948),
                       ('Young', 26771), ('Little', 25935), ('More', 25071), ('Few', 20510),('Much',
                                                                                      19362),
                       ('Many', 19283), ('New', 18025), ('Long', 17929), ('Big', 17520), ('Right',
                                                                                      15763),
                       ('Best', 14032), ('Dead', 12470), ('Certain', 11966), ('Better', 11782),
                       ('Sure', 11643)]
    return render_template('adjective_analysis.html',
                           female_adjectives=female_adjectives, male_adjectives=male_adjectives)


@app.route('/info/notes')
def render_notes():
    return render_template('corpus_notes.html')


@app.route('/info/subject_object_pronoun_analysis')
def render_subject_object():
    return render_template('subject_object_analysis.html')

@app.route('/info/pronoun_frequency_analysis')
def render_pronoun_frequency():
    return render_template('pronoun_frequency.html')


@app.route('/info/instance_distance_analysis')
def render_instance_distance():
    return render_template('instance_distance.html')


@app.route('/info/<filename>')
def render_markdown_any(filename, title=None):
    file_path = os.path.join('static', 'markdowns', f'{filename}.md')

    try:
        with open(file_path, encoding='utf-8') as fh:
            md_in = fh.read()
    except FileNotFoundError:
        abort(404)

    md_in = md_in.replace('(images/', '(/static/markdowns/images/')

    markdown_html = markdown2.markdown(md_in)

    if title is None:
        title_parts = filename.split('_')
        title = ' '.join([title_word.capitalize() for title_word in title_parts])
        # Gender in Novels, 1770-1922 is the desired title and this automatic naming
        # system would override that
        if title == "Gender Novels Overview":
            title = "Gender in Novels, 1770–1922"

    return render_template('blank_markdown.html', title=title, markdown_html=markdown_html)


@app.route('/markdowns/<filename>/')
def render_no_slash(filename, title=None):
    return render_markdown_any(filename, title)


if __name__ == '__main__':
    # Open a web browser on the landing page
    import webbrowser
    webbrowser.open('http://127.0.0.1:8021/', new=1)
    app.run(host='127.0.0.1', port='8021')
