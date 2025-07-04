import csv

class Song:
    
    def __init__(self, title, artist, top_genre, year, bpm, energy, danceability, dB, valence):
        """
        Task 5.1
            Initialize a Song object with given information
            
        Arg:
            information of the song:
                title (str)
                artist (Artist)
                top_genre (str)
                year (int)
                bpm (int)
                energy (int)
                danceability (int)
                dB (int)
                valence (int)
        """
        pass

class Artist:
    
    def __init__(self, name, songs):
        """
        Task 5.1
            Initialize an Artist object with given information
            
        Arg:
            information of the song:
                name (str)
                songs (list of Song)
        """
        pass

def parse_song_csv(filename):
    """
    Task 5.2
        Parse the given csv file and return two lists, list of songs and list of artists in order
    Arg:
        filename (str)
    Return:
        song_list (list of Song): list of Song objects present in the file
        artist_list (list of Artist): list of Artist objects present in the file
    """
    
    song_list, artist_list = [], []
    
    return song_list, artist_list

def find_similar_artist(artist, artist_list, criterion):
    """
    Task 5.3
        Find the most similar artist to the given artist for the given criterion in artist_list
        criterion is one of 'bpm', 'energy', 'danceability', 'dB', or 'valence'.
    Arg:
        artist (Artist)
        artist_list (list of Artists)
        criterion (str)
    Return:
        most_similar_artist (Artist): the most similar artist for the given criterion
    """
    
    pass

def main():
    # You can modify the main function to test your code
    
    song_list, artist_list = parse_song_csv('task2.csv')
    for song in song_list:
        print(f'Artist for {song.title} in artist_list?: {song.artist in artist_list}')
    
    for artist in artist_list:
          for song in artist.songs:
            print(f"{artist.name}'s song {song.title} in song_list?: {song in song_list}")
            
    song_list, artist_list = parse_song_csv('task3.csv')
    print(find_similar_artist(artist_list[0], artist_list[1:], 'bpm').name)
    print(find_similar_artist(artist_list[1], [artist_list[0] ,artist_list[2]], 'danceability').name)
    
    

if __name__ == "__main__":
    main()
