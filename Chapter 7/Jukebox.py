# Jukebox: Design a musical jukebox using object-oriented principles
# Assumption: Digital version of a jukebox, which is free to use.
# Objects: Jukebox Main Object, CD, Song, Artist, Playlist, Display
# Actions: Playlist CRUD, CD Selection, Song Selection, Play Queue, Play Next, Possibly Users

from collections import deque

class Jukebox:
    def __init__(self, cd_player: CDPlayer, user: User, cd_collection: set(), track: Song):
        self.cd_player = cd_player
        self.user = user
        self.cd_collection = cd_collection
        self.track = track

    def get_current_song(self):
        return self.track.get_current_song()

    def set_user(self, u: User):
        self.user = u

class CDPlayer:
    def __init__(self, playlist: Playlist = None, cd: CD = None):
        self.playlist = playlist
        self.cd = cd

    def play_song(self,song: Song):
        if song in self.playlist:
            self.track = song
    
    def get_playlist(self):
        return self.playlist
    
    def set_playlist(self, playlist: Playlist):
        self.playlist = playlist

    def get_cd(self):
        return self.cd
    
    def set_cd(self, cd:CD):
        self.cd = cd

class Playlist:
    def __init__(self, song: Song = None, new_playlist = None):
        self.song = song
        self.playlist_queue = new_playlist()

    def play_next(self):
        return self.playlist_queue.popleft()
    
    def add_to_queue(self, song: Song):
        self.playlist_queue.append(song)


# Simple classes with getters and setters
class Song:
    def __init__(self):
        pass

class CD:
    def __init__(self):
        pass
    
class User:
    def __init__(self):
        pass
