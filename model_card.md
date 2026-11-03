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

with genre at 1.0, a different-genre song with matching energy and mood can now outrank a same-genre song. This helps energy-driven listeners but weakens genre loyalty. The weaknesses from earlier remain: exact string matching, silent handling of bad input, and the empty profile returning 0.00 for everything.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

### What I tested

I ran three "normal" listeners (High-Energy Pop, Chill Lofi, Deep Intense Rock) and nine deliberately tricky ones (for example someone who wants sad music at high energy, or someone whose genre isn't in the catalog). Unless I say otherwise, the numbers below use the original point values (genre 2, mood 1, energy 1). Later I ran an experiment that halves genre and doubles energy; that is called out as "after the shift".

### Why does "Gym Hero" keep showing up for people who just want Happy Pop?

Think of the system as a judge with a checklist. For a listener who wants happy pop at high energy, the judge gives:

- 2 points if the song is pop,
- 1 point if the song is happy,
- up to 1 point for how close its energy is to what the listener wants.

Gym Hero is a pop song and a very energetic one (0.93 against the 0.90 asked for), so it earns about 2.97 points. It is not a *happy* song (it is labeled "intense"), so it misses the mood point. But the only song that *is* happy and *isn't* labeled "pop" is Rooftop Lights, which is labeled "indie pop". The judge reads "indie pop" and "pop" as two unrelated words, so Rooftop Lights gets no genre points and scores only 1.86. Since genre is worth twice as much as mood, "right genre, wrong mood" beats "right mood, wrong genre". That is the whole reason Gym Hero lands in second place right behind Sunrise City. Nobody decided Gym Hero was special; it just picks up the biggest reward by luck of its label.

### Comparing the profiles side by side

**High-Energy Pop vs. Chill Lofi.** The two lists have no songs in common at all. Pop's list is all loud songs (energy 0.76 to 0.96) and lofi's list is all quiet ones (0.28 to 0.42). That makes sense: these listeners asked for opposite things, and every rule in the scoring pushes them in opposite directions. One quieter difference is that lofi gets *three* songs that match its genre (so its top 3 all score above 2.9), while pop only has *two*, so after those two the pop list drops sharply (1.86, then 0.99). The lofi listener is simply lucky that the catalog has more lofi.

**High-Energy Pop vs. Deep Intense Rock.** These two both want loud music, so their lists do overlap: Gym Hero, Storm Runner and Iron Cathedral appear in both. What is interesting is *why* Gym Hero is second in both lists. For the pop fan it is there because it is pop. For the rock fan it is there because it is "intense" (rock fans asked for the intense mood, and Gym Hero is labeled intense). The same song is recommended for two different reasons. Rock also has just one rock song in the catalog, so after Storm Runner (3.99) the next best score is 1.99. Half the score vanishes after the first pick.

**Chill Lofi vs. Deep Intense Rock.** Total opposites, and again no overlap. Both get a near-perfect first pick (4.00 and 3.99), which shows the system does work when the catalog has an exact match. The difference is the shape of what follows: the lofi fan gets a gentle slide of reasonable choices (3.93, 2.95, 1.93, 0.98) because there are several lofi, chill and low-energy songs, while the rock fan falls off a cliff because there is only one rock song.

**Each normal profile, before vs. after the weight shift.** After the shift (genre worth 1, energy worth 2) the lists are mostly the same songs, but the gaps between them shrink. For the pop fan, Rooftop Lights jumps from 1.86 to 2.72, nearly catching Gym Hero (2.94 instead of 2.97), so the "Gym Hero unfairly beats happy songs" effect gets much weaker. For the rock fan, Gym Hero goes from 1.99 to 2.98, because the energy match now counts for more than the missing genre. For the lofi fan, the "chill but not lofi" song Spacewalk Thoughts rises from 1.93 to 2.86, almost tying Focus Flow, which is lofi but not chill (2.90). It makes sense: when we say "how loud or quiet" matters more than "what label it has", songs with the right feel can overtake songs with the right label.

**Happy Pop vs. "pop but sad" (a listener with conflicting wishes).** Both listeners want pop at energy 0.9. The only difference is the mood. The sad-pop listener gets almost the same list, with Gym Hero (2.97) and Sunrise City (2.92) at the top, because there are no sad songs in the catalog at all and the mood point can never be earned. The system doesn't say "I have nothing sad for you." It quietly ignores the request and hands back pop songs. The happy listener, in contrast, sees Sunrise City clearly on top (3.92) because it earns the mood point. The lesson is that a preference nobody can satisfy doesn't change anything, and it doesn't warn you either.

**Chill Lofi vs. "calm classical who wants maximum energy" (another conflict).** The lofi listener asks for things that fit together and gets a 4.00. The classical listener asks for peaceful classical music at energy 1.0, which no song can satisfy. Moonlit Sonata still wins with 3.18, because genre plus mood (3 points) easily outweighs being very far off in energy (0.18 points). The next best songs are loud ones scoring under 1. The system treats "name matches" as more important than "sounds right". After the shift the margin shrinks (2.36 vs. 1.94), which is a healthier balance, though Moonlit Sonata still wins.

**Unknown genre and mood vs. a completely empty profile.** Neither listener earns any genre or mood points, because "k-pop" and "ecstatic" don't exist in the catalog and the empty profile asked for nothing. The first one is ranked purely by energy, so the best pick is Velvet Hours, which is an exact match (1.00) on energy. The empty profile has every song at 0.00, so the system returns the first five rows of the spreadsheet in order. Both lists look like recommendations but are not really personal. The empty one is just file order dressed up as a recommendation.

**Energy of 5.0 vs. energy of -1.0 (impossible values).** Both numbers are outside the 0-to-1 scale, so every song gets zero energy points. Now only genre and mood matter. For the lofi listener (5.0), the two lofi/chill songs tie at 3.00 and the rest of the list is sorted by genre and mood. For the metal listener (-1.0), Iron Cathedral gets 3.00 and the four remaining slots all score 0.00, filled by whichever songs come first in the file. The difference comes from the catalog: there are three lofi songs, so the lofi list still looks sensible, but there is only one metal song, so the metal list quickly turns into random filler. Neither case warns that the input was invalid.

**"Rock " and "INTENSE" vs. Deep Intense Rock.** The wishes are the same in plain English, but the first listener typed a capital letter and an extra space. To the computer "Rock " is not "rock", so Storm Runner loses both its genre and mood points and drops from 3.99 to 0.99. It still happens to come first because its energy is closest, but the margin is gone and the reasons shown to the user are wrong. A small typing difference completely changes the score, which would be a real problem for a real app.

**Pop with no mood at energy 0.5 vs. High-Energy Pop.** The mid-energy listener wants pop but doesn't care about loudness. Sunrise City (2.68) and Gym Hero (2.57) still take the top two spots even though Gym Hero is very energetic, while Velvet Hours, which matches energy 0.5 exactly, only manages 1.00. This is the same genre-over-everything effect as the Gym Hero story. After the shift, the gap closes (Gym Hero 2.14 vs. Velvet Hours 2.00), which is a more believable ranking for someone who wants middle-of-the-road music.

**Blues + happy + very high energy, before vs. after the shift.** Before the shift, a quiet, melancholic blues song (Blue Monday Rain, energy 0.30) was #1 with 2.35, simply because it is blues. The listener asked for happy, energetic music, so that pick looks wrong. After the shift it falls out of the top five and is replaced by happy, energetic songs (Sunrise City 2.74, Rooftop Lights 2.62). That is the clearest example in my tests of the shift giving a more sensible answer.

### What surprised me

The system never has to be "wrong" to give an odd result. It just adds points, and a song can collect a lot of points for the wrong reasons (right word, wrong sound). Also, how well it works depends heavily on the catalog: listeners whose taste has several songs (lofi, pop) get a good list, while listeners whose taste has only one song (rock, metal, classical) get one good pick and then filler.

### Note on the current code

The code in `src/recommender.py` is currently left on the experimental weights (genre 1, mood 1, energy 2), so Section 3 above describes the original version, not what the code does right now.

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
