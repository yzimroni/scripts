import random
import os

LIMIT_SEASON = True
SEASON_MIN = 1
SEASON_MAX = 10

BASE_DIR = os.getcwd()


def run():
    season = None
    if LIMIT_SEASON:
        season = str(random.randint(SEASON_MIN, SEASON_MAX))
    else:
        while season is None or not os.path.isdir(BASE_DIR + "/" + season):
            season = random.choice(os.listdir(BASE_DIR))

    season_dir = BASE_DIR + "/" + season
    if not os.path.isdir(season_dir):
        raise AssertionError("season_dir (" + season_dir + ") is not a directory!")

    episode = random.choice(os.listdir(season_dir))
    print("Playing " + episode)
    os.startfile(season_dir + "/" + episode)


if __name__ == "__main__":
    run()
