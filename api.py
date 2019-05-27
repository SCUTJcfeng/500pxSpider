
MAIN_URL = 'https://500px.com'
POPULAR_URL = 'https://500px.com/popular'
PHOTO_URL = 'https://api.500px.com/v1/photos?feature={}&only={}&page={}&image_size[]=16384&image_size[]=8192&image_size[]=2048&image_size[]=4096&include_states=true&include_licensing=true&formats=jpeg,lytro'

FEATURE_LIST = ['popular', 'upcoming', 'fresh', 'editors', 'galleries', 'directory', 'groups', 'perks']
# only = Night, Film, ...

CATEGORY_NAMES_MAP = {
    "10": "Abstract",
    "29": "Aerial",
    "11": "Animals",
    "5": "Black and White",
    "31": "Boudoir",
    "1": "Celebrities",
    "9": "City & Architecture",
    "15": "Commercial",
    "16": "Concert",
    "20": "Family",
    "14": "Fashion",
    "2": "Film",
    "24": "Fine Art",
    "23": "Food",
    "3": "Journalism",
    "8": "Landscapes",
    "12": "Macro",
    "18": "Nature",
    "30": "Night",
    "4": "Nude",
    "7": "People",
    "19": "Performing Arts",
    "17": "Sport",
    "6": "Still Life",
    "21": "Street",
    "26": "Transportation",
    "13": "Travel",
    "22": "Underwater",
    "27": "Urban Exploration",
    "25": "Wedding",
    "0": "Uncategorized"
}

CATEGORY_LIST = list(CATEGORY_NAMES_MAP.values())
