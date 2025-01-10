import requests

# Your TMDB API key here
API_KEY = 'dd4699065f466230a4dc1b00c1925b88'
BASE_URL = 'https://api.themoviedb.org/3'
POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'

def get_poster_url(movie_title, release_year=None):
    """Fetch the poster URL for a given movie title with optional release year."""
    search_url = f"{BASE_URL}/search/movie"
    params = {
        'api_key': API_KEY,
        'query': movie_title,
        'include_adult': False,
    }
    if release_year:
        params['year'] = release_year  # Add year filter if provided

    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        results = response.json().get('results')
        if results:
            poster_path = results[0].get('poster_path')
            if poster_path:
                return f"{POSTER_BASE_URL}{poster_path}"
            else:
                return f"No poster found for {movie_title}"
        else:
            return f"No results found for {movie_title}"
    else:
        return f"Error: {response.status_code}"

def fetch_all_posters(movies_with_years):
    """Fetch poster URLs for all movies in the list, with optional release years."""
    movie_posters = {}
    for movie, year in movies_with_years:
        poster_url = get_poster_url(movie, release_year=year)
        movie_posters[movie] = poster_url
        print(f"{movie} ({year if year else 'N/A'}): {poster_url}")
    return movie_posters

# Example: Movies with optional release years
movies_with_years = [
    ("The Godfather", 1972),
    ("Scream", 1996),
    ("Oldboy", 2003),
    ("Parasite", 2019),
    ("Cure", 1997),
    ("WALL·E", 2008),
    ("The Hunt", 2012),
    ("Pulse", 2001),
]

# Run the script
posters = fetch_all_posters(movies_with_years)

# Save the results to a file (optional)
with open("movie_posters.txt", "w") as file:
    for movie, url in posters.items():
        file.write(f"{movie}: {url}\n")
