class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        self.add_song_to_count()

        # Add genre and artist
        self.add_to_genres(genre)
        self.add_to_artists(artist)

        # Update genre and artist counts
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Create a Song instance
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)         # "99 Problems"
print(ninety_nine_problems.artist)       # "Jay-Z"
print(ninety_nine_problems.genre)        # "Rap"
print(Song.count)                        # 1
print(Song.genres)                       # ["Rap"]
print(Song.artists)                      # ["Jay-Z"]
print(Song.genre_count)                  # {"Rap": 1}
print(Song.artist_count)                 # {"Jay-Z": 1}
