from . import db
import datetime

class Song(db.Model):
    __tablename__ = 'Song'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name_of_the_song = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    uploaded = db.Column(db.DateTime,default=datetime.datetime.utcnow,nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name_of_the_song': self.name_of_the_song,
            'duration': self.duration,
            'uploaded':self.uploaded
        }

class Podcast(db.Model):
    __tablename__ = 'Podcast'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name_of_the_song = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    uploaded = db.Column(db.DateTime,default=datetime.datetime.utcnow,nullable=False)
    host = db.Column(db.String(100),nullable=False)
    # participants = db.Column(db.ARRAY(db.String(100)))


    def __repr__(self):
            return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'name_of_the_song': self.name_of_the_song,
            'duration': self.duration,
            'uploaded':self.uploaded,
            'host':self.host
            # 'participants':self.participants
        }

class Audiobook(db.Model):
    __tablename__ = 'Audiobook'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title_of_the_audiobook = db.Column(db.String(100),nullable=False)
    author_of_the_title = db.Column(db.String(100),nullable=False)
    narrator = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    uploaded = db.Column(db.DateTime,default=datetime.datetime.utcnow,nullable=False)


    def __repr__(self):
            return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'title_of_the_audiobook': self.title_of_the_audiobook,
            'author_of_the_title': self.author_of_the_title,
            'narrator':self.narrator,
            'duration':self.duration,
            'uploaded':self.uploaded
        }

