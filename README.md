PROJECT ITEM CATALOG (FSND):
============================
INTRODUCTION:
In this project we are required to build an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete items.

DESCRIPTION:
-- After some fumbling I decided to create an app that catalogs Audiobooks and decided to give it title Audiobook Catalog -- very original :)

-- This web app is created using Python3 and Flask framework.

-- The app uses SQLite database which was named audiobookcatalog.db. The database file was created and accessed from Python code database_setup.py and project_catalog.py respectively, using SQLAlchemy. This approach is similar to what we have learned during the course.

-- To initially fill the database, I used the Python application database_fill.py. Again this approach is similar to what we saw in the class.

-- Authentication is performed using oauth2 client. I used Google as my authentication source.

-- The application pages are styled with Bootstrap and JavaScript components. The static folder under top level contain the thumbnail image used in the application pages and the style.css file. The templates folder contains all the html files used by the application pages.


SETUP:
This program was tested under VM. Tools used to install an manage the VM are called Vagrant and VirtualBox. Virtual Box can be 
downloaded at https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 and Vagrant can be downloaded at
https://www.vagrantup.com/downloads.html
To find more detailed description on how to use the tools mentioned above please refer to following URL:
https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0

IMPLEMENTATION:
-- I started my implementation by coming up with the database

-- The classes defined in the database are: Genre, Audiobook, Author, Narrator and Link.

-- Genre is defined as:

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    recordOwner = Column(String(500))
    
-- Audiobook is defined as:

    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    duration = Column(String(8))
    price = Column(String(8))
    recordOwner = Column(String(500))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)
    
-- Author is defined as:

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    audiobook_id = Column(Integer, ForeignKey('audiobook.id'))
    audiobook = relationship(Audiobook, cascade="all, delete-orphan",\
                             single_parent=True)
    
-- Narrator is defined as:
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    audiobook_id = Column(Integer, ForeignKey('audiobook.id'))
    audiobook = relationship(Audiobook, cascade="all, delete-orphan",\
                             single_parent=True)
    
-- Link is defined as:

    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    audiobook_id = Column(Integer, ForeignKey('audiobook.id'))
    audiobook = relationship(Audiobook, cascade="all, delete-orphan",\
                             single_parent=True)
    
-- The header of the application pages display two menu items -- Titles and Genre. The right side of the header will either show a link for Login or user name if authenticated.

-- The main application page contains the list of all the books. This page requires no authentication. Clicking on any of the books will take you to the description of the title which displays all the information defined in the above classes. The title information page is the only other page that can be accessed without authentication.

-- The C, U and D operations from the CRUD are exercised through the Genre Application page(s) and all of these pages require authentication. Clicking on Genre will take you to the Genre List in the database. From here you can add or delete a genre. Clicking on any of the genre items will display the books associated with that genre. From there a new book can be added, deleted or modified. A genre can not be deleted unless there are no books associated with that genre.

-- There are two JSON APIs defined for this app. One list all the books and the other one list all the genres and are accessed at /audiobooks/JSON and /genre/JSON

-- For creating my credentials, I logged on to Google API Dashboard @ https://console.developers.google.com Click on Create Credentials and follow the prompts.

-- For the name of my OAuth Client ID I selected "Catalog Web App"

-- For restrictions I entered http://localhost:5000 for "Authorized JavaScript origins" and http://localhost:5000/oauth2callback for "Authorized redirect URIs"

-- I downloaded JSON credentials and saved in application directory as client_secrets.json.

EXECUTION:
-- To Launch Flask on my VM I used following command:

    $ virtualenv flask-env

followed by:

    $ source flask-env/bin/activate

-- To create the database file audiobookcatalog.db I used following command:

    $ python3 database_setup.py

-- I populated my database using throwaway code as follows:

    $ python3 database_fill.py

-- To launch my web app I used following command:

    $ python3 project_catalog.py


From this point on the application will be available @ http://localhost:5000


  RESOURCES USED:
  1) Instructors notes
  2) http://www.stackoverflow.com
  3) https://www.w3schools.com/bootstrap/bootstrap_typography.asp
  4) https://developers.google.com/identity/protocols/OAuth2?hl=en_US
  5) https://developers.google.com/identity/sign-in/web/sign-in
  6) https://developers.google.com/identity/protocols/OAuth2UserAgent
  7) https://cloud.google.com/python/getting-started/authenticate-users
  8) http://flask.pocoo.org/docs/1.0/patterns/appfactories/
  9) https://oauth2client.readthedocs.io/en/latest/source/oauth2client.contrib.flask_util.html
  10) https://www.w3schools.com/icons/bootstrap_icons_glyphicons.asp
  11) https://developers.google.com/api-client-library/python/auth/web-app#tokenrevoke
  12) https://docs.sqlalchemy.org
  13) https://cloud.google.com/python/getting-started/authenticate-users
  14) https://github.com/GoogleCloudPlatform/getting-started-python
  15) https://getbootstrap.com/docs/
  16) https://br3ndonland.github.io/udacity/
  17) https://docs.sqlalchemy.org/en/13/orm/cascades.html

  and probably many more

  ISSUES:
  
