#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, Audiobook, Link, Author, Narrator

engine = create_engine('sqlite:///audiobookcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Biography
genre1 = Genre(name="Biography")
genre1.recordOwner = "mehmood.a.syed@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="Proud: My Fight for an Unlikely American Dream",
                  duration="9h:12m", price="$29.65", genre=genre1)
book1.recordOwner = "mehmoo.a.syed@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="Ibtihaj Muhammad, Lori L. Tharps",
                 audiobook=book1)

session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Ibtihaj Muhammad", audiobook=book1)
narrator1.recordOwner = "mehmood.a.syed@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/Proud-Audiobook/B07BGDGY6C?qid=\
1557949041&sr=1-4&ref=a_search_c3_lProduct_1_4&pf_rd_p=e81b7c27-6880-467a\
-b5a7-13cef5d729fe&pf_rd_r=SQYFMKHTWT59P5GH37PZ",
             audiobook=book1)
link1.recordOwner = "mehmood.a.syed@gmail.com"
session.add(link1)
session.commit()

# Book 2
book2 = Audiobook(title="Educated",
                  duration="12h:10m", price="$29.65", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="Tara Westover", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Julia Whelan", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/Educated-Audiobook/B075F8MBMQ?\
qid=1557951135&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=e81b7c27-6880\
-467a-b5a7-13cef5d729fe&pf_rd_r=V6J90X874KMTB1ZE51K0",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()
# Fiction
genre1 = Genre(name="Fiction")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="1984",
                  duration="11h:22m", price="$20.97", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="George Orwell", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Simon Prebble", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/1984-Audiobook/B002V19RO6?qid\
=1557951886&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=e81b7c27-6880-\
467a-b5a7-13cef5d729fe&pf_rd_r=1QXE2WP9W4EGNGHQDR27",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()

# Book 2
book2 = Audiobook(title="To Kill A Mocking Bird",
                  duration="12h:17m", price="$30.79", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="Harper Lee", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Sissy Spacek", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/To-Kill-a-Mockingbird-Audiobook\
/B00K1HQVOQ?qid=1557952222&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=\
e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=W1TY2A2VQ1BTKBMV6ABW",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()
# Mystery
genre1 = Genre(name="Mystery")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()

# Book 1
book1 = Audiobook(title="Buried",
                  duration="17h:32m", price="$25.59", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="Jussi Adler-Olsen", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Steven Pacey", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/Buried-Audiobook/B00TR1E716?qid\
=1557952723&sr=1-12&ref=a_search_c3_lProduct_1_12&pf_rd_p=e81b7c27-6880\
-467a-b5a7-13cef5d729fe&pf_rd_r=5HH4EW2GZH807N0MPZK6",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()

# Book 2
book2 = Audiobook(title="The Purity of Vengeance",
                  duration="14h:6m", price="$31.50", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="Jussi Adler-Olsen", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Graeme Malcolm", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/The-Purity-of-Vengeance-Audiobook\
/B00H8XHDOS?qid=1557952906&sr=1-2&ref=a_search_c3_lProduct_1_2&pf_rd_p=\
e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=HYGR8DAMQQGDBF67DNHP",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()

# Legend
genre1 = Genre(name="Legend")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="EMPEROR: The Gods of War, Book 4",
                  duration="15h:22m", price="$22.38", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="Conn Iggulden", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Paul Blake", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/EMPEROR-The-Gods-of-War-Book-4\
-Unabridged-Audiobook/B002VA9H4C?qid=1557953176&sr=1-4&ref=a_search_c3_\
lProduct_1_4&pf_rd_p=e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=\
D1DTQ2KN3B2DRZ9KS9G7",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()

# Book 2
book2 = Audiobook(title="EMPEROR: The Death of Kings, Book 2 ",
                  duration="17h:57m", price="$22.38", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="Conn Iggulden", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Robert Glenister", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/EMPEROR-The-Death-of-Kings-Book\
-2-Unabridged-Audiobook/B002V5ISOC?qid=1557953700&sr=1-3&ref=\
a_search_c3_lProduct_1_3&pf_rd_p=e81b7c27-6880-467a-b5a7-\
13cef5d729fe&pf_rd_r=QD1JRHVXBP771R9QSFPB",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()

# Fable
genre1 = Genre(name="Fable")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="The Alchemist",
                  duration="4h", price="$23.95", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="Paulo Coelho", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Jeremy Irons", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/The-Alchemist-Audiobook\
/B002V0Q4LG?qid=1557954045&sr=1-1&ref=a_search_c3_lProduct_1_1&pf\
_rd_p=e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=\
D8J1BB4YA6PDS7EGGTEY",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()
# Fantasy
genre1 = Genre(name="Fantasy")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="Harry Potter and the Chamber of Secrets, Book 2",
                  duration="9h:24m", price="$29.99", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="J.K. Rowling", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Jim Dale", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/Harry-Potter-and-the-Chamber\
-of-Secrets-Book-2-Audiobook/B017V4IWVG?qid=1557954306&sr=1-2&ref=\
a_search_c3_lProduct_1_2&pf_rd_p=e81b7c27-6880-467a-b5a7-\
13cef5d729fe&pf_rd_r=QQC0VAKQG3ZBGC9QK192",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()
# Book 2
book2 = Audiobook(title="Harry Potter and the Prisoner of Azkaban, Book 3",
                  duration="12h:15m", price="$29.99", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="J.K. Rowling", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Jim Dale", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/Harry-Potter-and-the-Prisoner\
-of-Azkaban-Book-3-Audiobook/B017V4JA2Q?qid=1557954501&sr=1-4&ref=\
a_search_c3_lProduct_1_4&pf_rd_p=e81b7c27-6880-467a-b5a7-\
13cef5d729fe&pf_rd_r=QM2AAHSV070TDP1HCX7E",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()
# Science Fiction
genre1 = Genre(name="Science Fiction")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="The Martian",
                  duration="10h:53m", price="$29.99", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="Andy Weir", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="R. C. Bray", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/The-Martian-Audiobook/\
B00B5HZGUG?qid=1557954911&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=\
e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=S3VEPA57WHES360TTPY9",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()
# Book 2
book2 = Audiobook(title="Space Case",
                  duration="6h:28m", price="$17.00", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="Stuart Gibbs", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Gibson Frazier ", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/Space-Case-Audiobook/\
B00MX28Y2O?qid=1557955158&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p\
=e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=AKT94T1K9P0XGV1GJRH8",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()
# Nonfiction
genre1 = Genre(name="Nonfiction")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="Grit",
                  duration="9h:22m", price="$20.99", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author 1
author1 = Author(name="Angela Duckworth", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator 1
narrator1 = Narrator(name="Angela Duckworth", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link 1
link1 = Link(url="https://www.audible.com/pd/Grit-Audiobook/B01D3AC5BA?qid\
=1557955467&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=e81b7c27-6880-467a-\
b5a7-13cef5d729fe&pf_rd_r=KSSG3S7QS6Q89CP8DBKY",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()
# Book 2
book2 = Audiobook(title="An Unquiet Mind",
                  duration="2h:46m", price="$13.27", genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author 2
author2 = Author(name="Kay Redfield Jamison", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator 2
narrator2 = Narrator(name="Kay Redfield Jamison", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link 2
link2 = Link(url="https://www.audible.com/pd/An-Unquiet-Mind-Audiobook\
/B00307X1AQ?qid=1557955635&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=\
e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=T1CWD3PA4FGK5HSQHPZ7",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()

# Narrative Nonfiction
genre1 = Genre(name="Narrative Nonfiction")
genre1.recordOwner = "john.doe@gmail.com"
session.add(genre1)
session.commit()
# Book 1
book1 = Audiobook(title="Molly's Game: From Hollywood's Elite, to Wall \
Street's Billionaire Boys Club, My High-Stakes Adventure in the World of \
    Underground Poker", duration="8h:30m", price="$25.09", genre=genre1)
book1.recordOwner = "john.doe@gmail.com"
session.add(book1)
session.commit()
# Author
author1 = Author(name="Molly Bloom", audiobook=book1)
author1.recordOwner = "john.doe@gmail.com"
session.add(author1)
session.commit()
# Narrator
narrator1 = Narrator(name=" Cassandra Campbell ", audiobook=book1)
narrator1.recordOwner = "john.doe@gmail.com"
session.add(narrator1)
session.commit()
# Link
link1 = Link(url="https://www.audible.com/pd/Mollys-Game-Audiobook\
/B00JPK626C?qid=1557950490&sr=1-1&ref=a_search_c3_lProduct_1_1&pf_rd_p=\
e81b7c27-6880-467a-b5a7-13cef5d729fe&pf_rd_r=W5WPVBKYA52GFYYJN0CM",
             audiobook=book1)
link1.recordOwner = "john.doe@gmail.com"
session.add(link1)
session.commit()
# Book 2
book2 = Audiobook(title="Wild", duration="13h:2m", price="$24.95",
                  genre=genre1)
book2.recordOwner = "john.doe@gmail.com"
session.add(book2)
session.commit()
# Author
author2 = Author(name="Cheryl Strayed ", audiobook=book2)
author2.recordOwner = "john.doe@gmail.com"
session.add(author2)
session.commit()
# Narrator
narrator2 = Narrator(name="Bernadette Dunne ", audiobook=book2)
narrator2.recordOwner = "john.doe@gmail.com"
session.add(narrator2)
session.commit()
# Link
link2 = Link(url="https://www.audible.com/pd/Wild-Audiobook/B0079LB0BG?qid=\
1557950860&sr=1-2&ref=a_search_c3_lProduct_1_2&pf_rd_p=e81b7c27-6880-467a\
-b5a7-13cef5d729fe&pf_rd_r=HG926HSHSDFWEFF89MBH",
             audiobook=book2)
link2.recordOwner = "john.doe@gmail.com"
session.add(link2)
session.commit()

print("added Genres, Books, Authors, Narrators & Links")
