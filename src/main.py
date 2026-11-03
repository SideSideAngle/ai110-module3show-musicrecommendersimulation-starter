"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


HIGH_ENERGY_POP = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.90,
    "valence": 0.80,
    "acousticness": 0.10,
}

# A calm, acoustic listener who wants chill lofi
CHILL_LOFI = {
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.35,
    "valence": 0.60,
    "acousticness": 0.80,
}

DEEP_INTENSE_ROCK = {
    "genre": "rock",
    "mood": "intense",
    "energy": 0.92,
    "valence": 0.40,
    "acousticness": 0.10,
}

PROFILES = {
    "High-Energy Pop": HIGH_ENERGY_POP,
    "Chill Lofi": CHILL_LOFI,
    "Deep Intense Rock": DEEP_INTENSE_ROCK,
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {name}: top recommendations ===\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
