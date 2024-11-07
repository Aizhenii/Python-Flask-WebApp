import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


# database connection
def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn


def get_post(post_id):
  conn = get_db_connection()
  post = conn.execute('SELECT * FROM clubs WHERE id = ?',
                      (post_id, )).fetchone()
  conn.close()
  if post is None:
    abort(404)
  return post


def get_postb(post_idb):
  conn = get_db_connection()
  post = conn.execute('SELECT * FROM businesses WHERE id = ?',
                      (post_idb, )).fetchone()
  conn.close()
  if post is None:
    abort(404)
  return post


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'hwejhk23u4uhw23Deh8'


@app.route('/')
def index():
  return render_template('index.html')


# For Clubs
@app.route('/questions', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    club = request.form['club']
    category = request.form.getlist('category')
    category_list = '-'.join(category)
    location = request.form['location']
    provide = request.form['provide']
    looking = request.form['looking']
    description = request.form['description']
    contact = request.form['contact']

    if not club:
      flash('Club Name is required!')
    else:
      conn = get_db_connection()
      conn.execute(
        'INSERT INTO clubs (club, category, location, provide, looking, description, contact) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (club, category_list, location, provide, looking, description,
         contact))
      conn.commit()
      conn.close()
      return redirect(url_for('index'))

  return render_template('questions.html')


# For businesses
@app.route('/questionsb', methods=('GET', 'POST'))
def createb():
  if request.method == 'POST':
    business = request.form['business']
    location = request.form['location']
    provide = request.form['provide']
    looking = request.form['looking']
    description = request.form['description']
    contact = request.form['contact']

    if not business:
      flash('Business Name is required!')
    else:
      conn = get_db_connection()
      conn.execute(
        'INSERT INTO businesses (business, location, provide, looking, description, contact) VALUES (?, ?, ?, ?, ?, ?)',
        (business, location, provide, looking, description, contact))
      conn.commit()
      conn.close()
      return redirect(url_for('index'))

  return render_template('questionsb.html')


@app.route('/team')
def teams():
  return render_template('team.html')


@app.route('/clubs')
def clubs():
  conn = get_db_connection()
  clubs = conn.execute('SELECT * FROM clubs').fetchall()
  conn.close()
  return render_template('clubs.html', clubs=clubs)


@app.route('/businesses')
def businesses():
  conn = get_db_connection()
  businesses = conn.execute('SELECT * FROM businesses').fetchall()
  conn.close()
  return render_template('businesses.html', businesses=businesses)


@app.route('/signup')
def signup():
  return render_template('signup.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
  post = get_post(id)

  if request.method == 'POST':
    club = request.form['club']
    category = request.form.getlist('category')
    category_list = ' - '.join(category)
    location = request.form['location']
    provide = request.form['provide']
    looking = request.form['looking']
    description = request.form['description']
    contact = request.form['contact']

    if not club:
      flash('Club Name is required!')
    else:
      conn = get_db_connection()
      conn.execute(
        'UPDATE clubs SET club = ?, category = ?, location = ?, provide = ?, looking = ?, description = ?, contact = ?'
        ' WHERE id = ?', (club, category_list, location, provide, looking,
                          description, contact, id))
      conn.commit()
      conn.close()
      return redirect(url_for('clubs'))

  return render_template('edit.html', post=post)


@app.route('/<int:idb>/editb', methods=('GET', 'POST'))
def editb(idb):
  post = get_postb(idb)

  if request.method == 'POST':
    business = request.form['business']
    location = request.form['location']
    provide = request.form['provide']
    looking = request.form['looking']
    description = request.form['description']
    contact = request.form['contact']

    if not business:
      flash('Business Name is required!')
    else:
      conn = get_db_connection()
      conn.execute(
        'UPDATE businesses SET business = ?, location = ?, provide = ?, looking = ?, description = ?, contact = ?'
        ' WHERE id = ?',
        (business, location, provide, looking, description, contact, idb))
      conn.commit()
      conn.close()
      return redirect(url_for('businesses'))

  return render_template('editb.html', post=post)


@app.route('/<int:id>/delete', methods=('POST', ))
def delete(id):
  post = get_post(id)
  conn = get_db_connection()
  conn.execute('DELETE FROM clubs WHERE id = ?', (id, ))
  conn.commit()
  conn.close()
  flash('"{}" was successfully deleted!'.format(post['club']))
  return redirect(url_for('clubs'))


@app.route('/<int:idb>/deleteb', methods=('POST', ))
def deleteb(idb):
  post = get_postb(idb)
  conn = get_db_connection()
  conn.execute('DELETE FROM businesses WHERE id = ?', (idb, ))
  conn.commit()
  conn.close()
  flash('"{}" was successfully deleted!'.format(post['business']))
  return redirect(url_for('businesses'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=8080)
