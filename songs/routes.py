from flask import current_app as app
from flask import request, render_template, make_response, json

from .models import *
# flask.request.json


@app.route('/')
def index():
    return 'Index Page with all'


@app.route('/create',methods=['POST'])
def create():
    audioFileType = request.args.get('audio_file_type')
    if audioFileType:
        if audioFileType.lower() == "song":
            name_of_the_song = request.args.get('name_of_the_song')
            duration = request.args.get('duration')
            try:
                song = Song(name_of_the_song=name_of_the_song,duration=int(duration))
                db.session.add(song)
                db.session.commit()
                # data = dict(name_of_the_song=name_of_the_song,duration=duration)
                # response = app.response_class(response=json.dumps(song),
                # status=200,
                # mimetype='application/json')
                return "song created!. song id = {} and  audio file type = {}".format(song.id,"Song"),200
            except Exception as e:
                return(str(e)),400
        elif audioFileType.lower() == "podcast":
            name_of_the_song = request.args.get('name_of_the_song')
            duration = request.args.get('duration')
            host = request.args.get('host')
            try:
                podcast = Podcast(name_of_the_song=name_of_the_song,duration=int(duration),host=host)
                db.session.add(podcast)
                db.session.commit()
                return "song created!. song id = {} and  audio file type = {}".format(podcast.id,"Podcast"),200
            except Exception as e:
                return str(e),400
        elif audioFileType.lower() == "audiobook":
            title_of_the_audiobook = request.args.get('title_of_the_audiobook')
            author_of_the_title = request.args.get('author_of_the_title')
            narrator = request.args.get('narrator')
            duration = request.args.get('duration')
            try:
                audiobook = Audiobook(title_of_the_audiobook=title_of_the_audiobook,author_of_the_title=author_of_the_title,narrator=narrator,duration=int(duration))
                db.session.add(audiobook)
                db.session.commit()
                return "song created!. song id = {} and  audio file type = {}".format(audiobook.id,"Audiobook"),200
            except Exception as e:
                return (str(e)),400
        else:
            return "Not a valid file type",400
    else:
        return "<h3>Non file not valid</h3>", 500


@app.route('/delete/<audio_file_type>/<int:_id>',methods=['DELETE'])
def delete(audio_file_type,_id):
    if audio_file_type.lower() == "song":
        try:
            song = Song.query.get(_id)
            db.session.delete(song)
            db.session.commit()
            # data = dict(name_of_the_song=name_of_the_song,duration=duration)
            # response = app.response_class(response=json.dumps(song),
            # status=200,
            # mimetype='application/json')
            return "song deleted!. song id = {} and  audio file type = {}".format(song.id,"Song"),200
        except Exception as e:
            return(str(e)),400
    elif audio_file_type.lower() == "podcast":
        try:
            podcast = Podcast.query.get(_id)
            db.session.delete(podcast)
            db.session.commit()
            return "song deleted!. song id = {} and  audio file type = {}".format(podcast.id,"Podcast"),200
        except Exception as e:
            return str(e),400
    elif audio_file_type.lower() == "audiobook":
        try:
            audiobook = Audiobook.query.get(_id)
            db.session.delete(audiobook)
            db.session.commit()
            return "song deleted!. song id = {} and  audio file type = {}".format(audiobook.id,"Audiobook"),200
        except Exception as e:
            return (str(e)),400
    else:
        return "Not a valid file type",400





@app.route('/update/<audio_file_type>/<int:_id>',methods=['PUT'])
def update(audio_file_type,_id):
    if audio_file_type.lower() == "song":
        try:
            song = Song.query.filter_by(id=_id).update(dict(request.json))
            db.session.commit()
            # data = dict(name_of_the_song=name_of_the_song,duration=duration)
            # response = app.response_class(response=json.dumps(song),
            # status=200,
            # mimetype='application/json')
            return "song updated!. song id = {} and  audio file type = {}".format(_id,"Song"),200
        except Exception as e:
            return(str(e)),400
    elif audio_file_type.lower() == "podcast":
        try:
            podcast = Podcast.query.filter_by(id=_id).update(dict(request.json))
            db.session.commit()
            return "song updated!. song id = {} and  audio file type = {}".format(_id,"Podcast"),200
        except Exception as e:
            return str(e),400
    elif audio_file_type.lower() == "audiobook":
        try:
            audiobook = Audiobook.query.filter_by(id=_id).update(dict(request.json))
            db.session.commit()
            return "song updated!. song id = {} and  audio file type = {}".format(_id,"Audiobook"),200
        except Exception as e:
            return (str(e)),400
    else:
        return "Not a valid file type",400


@app.route('/get/<audio_file_type>',methods=['GET'])
@app.route('/get/<audio_file_type>/<int:_id>',methods=['GET'])
def get(audio_file_type,_id=None):
    if _id:
        if audio_file_type.lower() == "song":
            try:
                song = Song.query.get(_id)
                data = dict(song.serialize())
                data['uploaded'] = data['uploaded'].strftime("%Y-%m-%d %I:%M:%S %p")
                db.session.commit()
                return "data: {}".format(data),200
            except Exception as e:
                return(str(e)),400
        elif audio_file_type.lower() == "podcast":
            try:
                podcast = Podcast.query.get(_id)
                data = dict(podcast.serialize())
                data['uploaded'] = data['uploaded'].strftime("%Y-%m-%d %I:%M:%S %p")
                db.session.commit()
                return "data: {}".format(data),200
            except Exception as e:
                return str(e),400
        elif audio_file_type.lower() == "audiobook":
            try:
                audiobook = Audiobook.query.get(_id)
                data = dict(audiobook.serialize())
                data['uploaded'] = data['uploaded'].strftime("%Y-%m-%d %I:%M:%S %p")
                db.session.commit()
                return "data: {}".format(data),200
            except Exception as e:
                return (str(e)),400
        else:
            return "Not a valid file type",400
    else:
        if audio_file_type.lower() == "song":
            songs_details = []
            try:
                songs = Song.query.all()
                for i in songs:
                    id = i.id
                    single = Song.query.get(id)
                    songs_details.append(single.serialize())
                return "data: {}".format(songs_details),200
            except Exception as e:
                return (str(e)),400
        elif audio_file_type.lower() == "podcast":
            podcasts_details = []
            try:
                podcasts = Podcast.query.all()
                for i in podcasts:
                    id = i.id
                    single = Podcast.query.get(id)
                    podcasts_details.append(single.serialize())
                return "data: {}".format(podcasts_details),200
            except Exception as e:
                return (str(e)),400
        
        elif audio_file_type.lower() == "audiobook":
            audiobooks_details = []
            try:
                audiobooks = Audiobook.query.all()
                for i in audiobooks:
                    id = i.id
                    single = Audiobook.query.get(id)
                    audiobooks_details.append(single.serialize())
                return "data: {}".format(audiobooks_details),200
            except Exception as e:
                return (str(e)),400
        else:
            return "Not a valid file type",400