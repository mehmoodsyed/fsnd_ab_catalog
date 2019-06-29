#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Audiobook, Author, Narrator, Link

from oauth2client.contrib.flask_util import UserOAuth2
import json
import httplib2

app = Flask(__name__)

oauth2 = UserOAuth2()
# Connect to Database and create database session
engine = create_engine('sqlite:///audiobookcatalog.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


'''
 Rubrics - API Endpoints
 The project implements a JSON endpoint that serves the same
 information as displayed in the HTML endpoints for an arbitrary
 item in the catalog.
 '''


''' display the JSON output for all the books in the catalog '''
@app.route('/audiobooks/JSON')
def audiobooksJSON():
    audiobook = session.query(Audiobook).all()
    return jsonify(audiobook=[ab.serialize for ab in audiobook])


''' display the JSON output for the genres in the catalog '''


@app.route('/genre/JSON')
def genreJSON():
    genre = session.query(Genre).all()
    return jsonify(genre=[g.serialize for g in genre])


''' Show JSOM output for Book details '''
@app.route('/audiobooks/<int:audiobook_id>/JSON')
def showBookDetailsJSON(audiobook_id):
    audiobook = session.query(Audiobook).filter_by(id=audiobook_id).one()
    author = session.query(Author).filter_by(audiobook_id=audiobook_id).one()
    narrator =\
        session.query(Narrator).filter_by(audiobook_id=audiobook_id).one()
    link = session.query(Link).filter_by(audiobook_id=audiobook_id).one()
    return jsonify(audiobook.title, author.name, narrator.name,
                   audiobook.duration, audiobook.price, link.url,
                   audiobook.recordOwner)


'''
End Rubrics - API Endpoints
'''

'''
Rubrics - CRUD Read
'''


''' Show all audio books '''
@app.route('/')
@app.route('/audiobooks/')
def showAudioBooks():
    audiobook = session.query(Audiobook).order_by(asc(Audiobook.title))
    return render_template('audiobooks.html', audiobook=audiobook)


''' Show Book details '''
@app.route('/audiobooks/<int:audiobook_id>/')
def showBookDetails(audiobook_id):
    audiobook = session.query(Audiobook).filter_by(id=audiobook_id).one()
    author = session.query(Author).filter_by(audiobook_id=audiobook_id).one()
    narrator =\
        session.query(Narrator).filter_by(audiobook_id=audiobook_id).one()
    link = session.query(Link).filter_by(audiobook_id=audiobook_id).one()
    return render_template('book.html', audiobook=audiobook,
                           author=author, narrator=narrator, link=link)


'''
End Rubrics - CRUD Read
'''

''' Show genre '''
@app.route('/genre')
@oauth2.required
def showGenre():
    genre = session.query(Genre).order_by(asc(Genre.name))
    return render_template('genre.html', genre=genre)


''' Show Book in a genre '''
@app.route('/genre/<int:genre_id>/')
@oauth2.required
def showGenreBooks(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    book_items = session.query(Audiobook).filter_by(genre_id=genre_id).all()
    return render_template('collection.html', book_items=book_items,
                           genre=genre)


'''
Rubrics - CRUD Create + Authentication & Authorization
'''


''' Create a new Genre '''
@app.route('/genre/new/', methods=['GET', 'POST'])
@oauth2.required
def newGenre():
    if request.method == 'POST':
        newGenre = Genre(name=request.form['name'])
        newGenre.recordOwner = login_session['profile']['email']
        session.add(newGenre)
        flash('New Genre %s Successfully Created.' % newGenre.name)
        session.commit()
        return redirect(url_for('showGenre'))
    else:
        return render_template('newgenre.html')


''' Create a new title and all its information '''
@app.route('/audiobooks/new/<int:genre_id>', methods=['GET', 'POST'])
@oauth2.required
def newTitle(genre_id):
    if request.method == 'POST':
        if request.form['title']:
            audiobook = Audiobook(title=request.form['title'],
                                  duration=request.form['duration'],
                                  price=request.form['price'],
                                  genre_id=genre_id)
            audiobook.recordOwner = login_session['profile']['email']
            session.add(audiobook)
            session.commit()

            book = \
                session.query(Audiobook).filter_by(title=audiobook.title).one()

            author = Author(name=request.form['author'],
                            audiobook_id=book.id)
            session.add(author)
            session.commit()

            narrator = Narrator(name=request.form['narrator'],
                                audiobook_id=book.id)
            session.add(narrator)
            session.commit()

            link = Link(url=request.form['url'],
                        audiobook_id=book.id)
            session.add(link)
            session.commit()

            flash('New Audiobook %s Successfully Added' % book.title)

            return redirect(url_for('showGenreBooks', genre_id=genre_id))
        else:
            flash('Title of the book is a required field')
            return render_template('addtitle.html')
    else:
        return render_template('addtitle.html')


'''
End Rubrics - CRUD Create + Authentication & Authorization
'''


'''
Rubrics - CRUD Delete + Authentication & Authorization
'''


''' Delete a genre '''
@app.route('/genre/<int:genre_id>/delete/', methods=['GET', 'POST'])
@oauth2.required
def deleteGenre(genre_id):
    genreToDelete = session.query(Genre).filter_by(id=genre_id).one()
    if genreToDelete.recordOwner == login_session['profile']['email']:
        if request.method == 'POST':
            book_items = \
                session.query(Audiobook).filter_by(genre_id=genre_id).all()
            if len(book_items) > 0:
                flash('Genre not empty. Please delete books associated with\
                     it.')
                return redirect(url_for('showGenre'))
            else:
                session.delete(genreToDelete)
                flash('%s Successfully Deleted' % genreToDelete.name)
                session.commit()
                return redirect(url_for('showGenre'))
        else:
            flash('This action requires that no books are associated with\
                this genre.')
            return render_template('deletegenre.html', genre=genreToDelete)
    else:
        flash('%s not authorized for this \
                acction.' % login_session['profile']['email'])
        return render_template('deletegenre.html', genre=genreToDelete)


''' Delete a title alongwith Author, Narrator and the Link Entry
 in the corresponding tables. '''


@app.route('/audiobooks/<int:audiobook_id>/delete/', methods=['GET', 'POST'])
@oauth2.required
def deleteTitle(audiobook_id):
    bookToDelete = \
        session.query(Audiobook).filter_by(id=audiobook_id).one()
    authorToDelete = \
        session.query(Author).filter_by(audiobook_id=audiobook_id).one()
    narratorToDelete = \
        session.query(Narrator).filter_by(audiobook_id=audiobook_id).one()
    linkToDelete = \
        session.query(Link).filter_by(audiobook_id=audiobook_id).one()
    if request.method == 'POST':
        if bookToDelete.recordOwner == login_session['profile']['email']:
            session.delete(bookToDelete)
            session.commit()
            session.delete(authorToDelete)
            session.commit()
            session.delete(narratorToDelete)
            session.commit()
            session.delete(linkToDelete)
            session.commit()
            flash('%s Successfully Deleted' % bookToDelete.title)

            return redirect(
              url_for('showGenreBooks', genre_id=bookToDelete.genre_id))
        else:
            flash('%s not authorized for this \
                acction.' % login_session['profile']['email'])
            return redirect(
              url_for('showGenreBooks', genre_id=bookToDelete.genre_id))
    else:
        return render_template('deletetitle.html', book=bookToDelete)


'''
End Rubrics - CRUD Delete + Authentication & Authorization
'''


'''
Rubrics - CRUD Update + Authentication & Authorization
'''

''' Edit a title alongwith Author, Narrator and the Link Entry
 in the corresponding tables. '''


@app.route('/audiobooks/<int:audiobook_id>/edit/', methods=['GET', 'POST'])
@oauth2.required
def editTitle(audiobook_id):
    bookToEdit = \
        session.query(Audiobook).filter_by(id=audiobook_id).one()
    authorToEdit = \
        session.query(Author).filter_by(audiobook_id=audiobook_id).one()
    narratorToEdit = \
        session.query(Narrator).filter_by(audiobook_id=audiobook_id).one()
    linkToEdit = \
        session.query(Link).filter_by(audiobook_id=audiobook_id).one()
    if request.method == 'POST':
        if bookToEdit.recordOwner == login_session['profile']['email']:
            if request.form['title']:
                bookToEdit.title = request.form['title']
                session.add(bookToEdit)
                session.commit()

            if request.form['duration']:
                bookToEdit.duration = request.form['duration']
                session.add(bookToEdit)
                session.commit()

            if request.form['price']:
                bookToEdit.price = request.form['price']
                session.add(bookToEdit)
                session.commit()

            if request.form['author']:
                authorToEdit.name = request.form['author']
                session.add(authorToEdit)
                session.commit()

            if request.form['narrator']:
                narratorToEdit.name = request.form['narrator']
                session.add(narratorToEdit)
                session.commit()

            if request.form['url']:
                linkToEdit.url = request.form['url']
                session.add(linkToEdit)
                session.commit()

            flash('%s Successfully Edited' % bookToEdit.title)

            return redirect(
                url_for('showGenreBooks', genre_id=bookToEdit.genre_id))
        else:
            flash('%s not authorized for this \
                acction.' % login_session['profile']['email'])
            return redirect(
                url_for('showGenreBooks', genre_id=bookToEdit.genre_id))

    else:
        return render_template('edittitle.html', book=bookToEdit,
                               author=authorToEdit,
                               narrator=narratorToEdit,
                               link=linkToEdit)


'''
End Rubrics - CRUD Update + Authentication & Authorization
'''
'''
Rubrics - Authentication & Authorization
'''


''' Add a logout handler. '''
@app.route('/logout')
def logout():
    # Delete the user's profile and the credentials stored by oauth2.
    del login_session['profile']
    login_session.modified = True
    oauth2.storage.delete()
    login_session.pop('profile', None)
    login_session.pop('email', None)
    return redirect(url_for('showAudioBooks'))


def _request_user_info(credentials):
    """
    Makes an HTTP request to the Google OAuth2 API to retrieve the user's basic
    profile information, including full name and photo, and stores it in the
    Flask session.
    reference:
    https://oauth2client.readthedocs.io/en/latest/source/oauth2client.contrib.flask_util.html
    """
    http = httplib2.Http()
    credentials.authorize(http)
    resp, content = http.request(
        'https://www.googleapis.com/oauth2/v3/userinfo')
    if resp.status == 200:
        login_session['profile'] = json.loads(content.decode('utf-8'))
    else:
        # some error handling need to be done
        return None


app.config['SECRET_KEY'] = 'super_secret_key'  # ok for non-production servers

app.config['GOOGLE_OAUTH2_CLIENT_SECRETS_FILE'] = 'client_secrets.json'

oauth2.init_app(
        app,
        scopes=['email', 'profile'],
        authorize_callback=_request_user_info)


'''
End Rubrics - Authentication & Authorization
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
