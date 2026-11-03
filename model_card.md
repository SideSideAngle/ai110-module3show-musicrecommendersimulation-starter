# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

The recommender looks at each song one at a time and asks, "How well does this fit what the listener likes?" It answers with a score, and the songs with the highest scores are the ones shown.

The listener tells the system three things: a favorite genre, a favorite mood, and how energetic they want the music to feel (a number from 0, very calm, to 1, very intense). The system then gives every song points:

- **Genre:** if the song's genre is exactly the listener's favorite, it earns 2 points. This is the biggest reward because genre is the clearest sign of taste.
- **Mood:** if the song's mood is exactly the listener's favorite, it earns 1 point. Mood counts for less because the same mood shows up across many genres.
- **Energy:** every song earns up to 1 point depending on how close its energy is to what the listener wants. A perfect match earns the full point, and the further away it is, the fewer points it earns. Because every song gets some credit here, this also breaks ties between songs that match equally on genre and mood.

A song's score is the sum of these points, so the best possible score is 4. Once every song has a score, the system sorts them from highest to lowest and keeps the top five.

Each recommendation also comes with its reasons, such as "genre match: lofi (+2.0)", so the listener can see exactly why a song was picked rather than just trusting the ranking.

The system doesn't use listening history or other people's behavior. It only compares a song's own attributes to the listener's stated preferences. Genre and mood must match exactly, so "indie pop" gets no credit as "pop", and "relaxed" gets no credit as "chill".

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
