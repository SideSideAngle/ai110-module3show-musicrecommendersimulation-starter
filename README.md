# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

This recommender is **content-based**: it compares each song's attributes to a user's taste profile and ranks songs by how well they match. It uses no listening history or other users' behavior.

### Data

**Song** (one row of `data/songs.csv`, 19 songs):
`id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness`

**UserProfile** (the taste profile):
`favorite_genre, favorite_mood, target_energy`, plus `target_valence` and `target_acousticness`, which are stored but not scored in the first version.

### Algorithm Recipe

Every song gets a score from three rules, and a higher score means a better match:

| Signal | Rule | Points |
|---|---|---|
| Genre | `song.genre == user.favorite_genre` | +2.0 |
| Mood | `song.mood == user.favorite_mood` | +1.0 |
| Energy | `1.0 - abs(song.energy - user.target_energy)` | 0.0 to +1.0 |

```
score = genre_points + mood_points + energy_points      (maximum 4.0)
```

**Why these weights**
- Genre is worth the most because it is the strongest, most specific taste signal.
- Mood is worth half as much because it is a vibe, not a category, and it overlaps across genres (`chill` appears in lofi and ambient).
- Energy is continuous, so every song earns some credit. It breaks ties and keeps results sensible when no genre or mood matches.
- Genre and mood are exact string matches, and most values appear on only one or two songs. A match is therefore a strong but rare signal.

The weights are named constants (`GENRE_WEIGHT`, `MOOD_WEIGHT`, `ENERGY_WEIGHT`) in `src/recommender.py`, so the experiments below are one-line changes.

### How a Song Becomes a Recommendation

1. **Load**: `load_songs` reads `data/songs.csv` and turns each row into a dictionary, converting numeric fields from text to numbers.
2. **Score**: `score_song(user_prefs, song)` applies the three rules to one song and returns `(score, reasons)`. The reasons are short strings such as `"genre match: lofi (+2.0)"`.
3. **Rank**: `recommend_songs` scores every song, sorts by score from highest to lowest, and keeps the top `k`.
4. **Explain**: each result is returned as `(song, score, explanation)`, and `src/main.py` prints the "Because: ..." line.

The `Recommender` class (`recommend`, `explain_recommendation`) reuses `score_song`, so the class and the functions follow the same rules.

**Scoring is separate from ranking.** The scoring rule judges one song in isolation. The ranking rule compares the scores and decides what the user sees. A recommender needs both.

### Planned Experiments and Known Weaknesses

- Try genre = 1.0 with energy weight doubled, and compare the top 5.
- Try adding valence and acousticness closeness to the score.
- Exact string matching means `indie pop` does not count as `pop`, and `chill` gets no partial credit for `relaxed`.
- With only 19 songs, lower-ranked results can be weak matches that only earn energy points.
- Genre dominance can bury a song with a great mood and energy match.

### Real-World Context

Real world recommendation systems combine several signals in a pipeline. Signals like plays, skips, replays, watch or listen time, saves, time of day, device, location, genre, lyrics, other users' who listen to similar songs.
They also utilize collaborative filtering, which draws on activity and behavior from other users, and content-based filtering, which draws on the content itself. Both have their own pros and cons and requirements to get up and running.
Lastly, they also need a scoring rule to answer "how good is this song for this user" and a ranking rule to answer "which songs do we display". Both work at different levels and a recommender needs both
The scoring rule judges one song in isolation, the ranking rule would decide what the user sees.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

## Sample Recommendation Output
Loaded songs: 19

Top recommendations:

Library Rain - Score: 4.00
Because: genre match: lofi (+2.0); mood match: chill (+1.0); energy 0.35 vs target 0.35 (+1.00)

Midnight Coding - Score: 3.93
Because: genre match: lofi (+2.0); mood match: chill (+1.0); energy 0.42 vs target 0.35 (+0.93)

Focus Flow - Score: 2.95
Because: genre match: lofi (+2.0); energy 0.40 vs target 0.35 (+0.95)

Spacewalk Thoughts - Score: 1.93
Because: mood match: chill (+1.0); energy 0.28 vs target 0.35 (+0.93)

Coffee Shop Stories - Score: 0.98
Because: energy 0.37 vs target 0.35 (+0.98)


```
Loaded songs: 19

=== High-Energy Pop: top recommendations ===

Sunrise City - Score: 3.92
Because: genre match: pop (+2.0); mood match: happy (+1.0); energy 0.82 vs target 0.90 (+0.92)

Gym Hero - Score: 2.97
Because: genre match: pop (+2.0); energy 0.93 vs target 0.90 (+0.97)

Rooftop Lights - Score: 1.86
Because: mood match: happy (+1.0); energy 0.76 vs target 0.90 (+0.86)

Storm Runner - Score: 0.99
Because: energy 0.91 vs target 0.90 (+0.99)

Iron Cathedral - Score: 0.94
Because: energy 0.96 vs target 0.90 (+0.94)


=== Chill Lofi: top recommendations ===

Library Rain - Score: 4.00
Because: genre match: lofi (+2.0); mood match: chill (+1.0); energy 0.35 vs target 0.35 (+1.00)

Midnight Coding - Score: 3.93
Because: genre match: lofi (+2.0); mood match: chill (+1.0); energy 0.42 vs target 0.35 (+0.93)

Focus Flow - Score: 2.95
Because: genre match: lofi (+2.0); energy 0.40 vs target 0.35 (+0.95)

Spacewalk Thoughts - Score: 1.93
Because: mood match: chill (+1.0); energy 0.28 vs target 0.35 (+0.93)

Coffee Shop Stories - Score: 0.98
Because: energy 0.37 vs target 0.35 (+0.98)


=== Deep Intense Rock: top recommendations ===

Storm Runner - Score: 3.99
Because: genre match: rock (+2.0); mood match: intense (+1.0); energy 0.91 vs target 0.92 (+0.99)

Gym Hero - Score: 1.99
Because: mood match: intense (+1.0); energy 0.93 vs target 0.92 (+0.99)

Iron Cathedral - Score: 0.96
Because: energy 0.96 vs target 0.92 (+0.96)

Neon Pulse - Score: 0.95
Because: energy 0.97 vs target 0.92 (+0.95)

Sunrise City - Score: 0.90
Because: energy 0.82 vs target 0.92 (+0.90)
```

