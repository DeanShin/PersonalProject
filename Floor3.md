# Floor 3

When I asked players of PP what they would want to see in Floor 3, everyone unanimously said that they wanted more mechanic-driven puzzles like The Lovers and The Hanged Man at around the same difficulty as Floor 2. I at least got half of that equation right. Floor 3 was designed to have a new mechanic in each area, and, after the initial round of playtests, a massive challenge fitting of 'endgame' for players.

## The Devil / The Crimson

Originally, The Devil was going to be an area about mythological creatures e.g. the Hydra. I forget exactly how I came up with the connection between Touhou 6 (The Embodiment of Scarlet Devil) and The Devil, but discord messages around that time seem to suggest that Arisu is to blame.

The idea for redefining bottom oranges as a cipher comes as a natural extension of top and middle oranges. I'm very surprised hasn't been put into a map before--I know that Daffa made a bottom orange that used elements as components, but I think this idea has a ton of potential in future maps (who knows, I might make one in the future).

I started with the answers for the top floor, which are locations, characters, and song titles in Touhou 6. From there, I tried to make as many of the words as possible using as few component words as I could. I think it works pretty well (although `MALE`, `FEMALE`, and `MAGIC` are definitely Walcome Buck).

## The Tower / The Spire

Funnily enough, The Tower was the second or the third area that I ideated for Personal Project and was therefore the first area that I made for floor 3. This area was designed to be a more difficult version of the Gemstone Room in LL1 and the Human tower in LL2.

The idea to obfuscate the floor number only came as I was laying out the section in the editor. Originally, each panel would only be accessible via a labyrinth of staircases, but I wasn't able to design a compelling maze that anyone (let alone I as a certified maze-hater) would've found fun. Switching to warps allowed me to not only hide the floor number (only to reveal the floor via the middle column), but also hide the orientation of each panel relative to one another, making the 'stacks' less obvious.

Two stacks ended up being changed during development. The triple letter stack originally was much more convoluted--it was words that contained the nth symbol of the periodic table twice (*H*US*H*, *HE*ARTAC*HE*, etc.). The 12 days of Christmas stack was originally the different levels of Celeste, which was removed once I finalized the theme for The Sun.

## The Star / The Asterisk

Of all of the areas, I'm probably the most proud with how this one turned out. Given that the next couple areas were `THE STAR`, `THE MOON`, and `THE SUN`, I needed some way to differentiate each area thematically so that there was no overlap between areas.

The design for the area (an asterisk) came before I fully created puzzles for the area, which necessitated that I make 12-13 puzzles times 6. This meant that I had to come up with enough puzzles and submechanics using Regex to fill the area. Luckily, Regex is extremely powerful and has tons of tools.

Also, the color name is canonically light black.

## The Moon / The Lunatic

Of the areas in Floor 3, I'm definitely the least happy with The Moon. The mechanic was inspired by an [Icely video where he played the Word Scramble Baba puzzle pack](https://youtu.be/NPXXNDIpbwc?si=Wm0ZWwXJ9lDbVE69). The theme works fine, and it's funny how each one of the panels looks like gobbledygook, but the mechanic didn't end up being that interesting to me.

However, I did need to keep the mechanic to interface with the light black regex blocks, so I tried my best to make interesting themed and mechanical puzzles. Coming up with the mechanical puzzles wasn't the easiest, as I had to manually try a bunch of short synonyms and antonyms in Qat to see what worked.

You might also say that this mechanic is very similar to dots in Icely Palace to which I'll say, "Yes, I completely forgot that Icely made this mechanic already".

## The Sun / The Celestial Body

The Celeste Area! This area contains my favorite mechanic of Floor 3. The mechanic for this area was inspired by Gl!tch's and my collab room in Perceiving is Deceiving, where colored glass increased and decreased the height of blocks. Furthermore, we had cream-colored blocks that would take the color and height of other blocks, which inspired the = mechanic. The = combined with multi-size blocks in Farewell came from me thinking: "How can I subvert people's expectations with this mechanic?" From playtests, I can definitely say that I succeeded in that.

For a while during playtesting, this area was much harder--Forsaken City didn't just contain bottom -s and +s, it contained side +s and -s as well, not to mention stacks. Furthermore, there was no "tutorial" for side +s and -s in old site like there currently is.

Would the area have been more interesting from a rule-discovery perspective the old way? Maybe, but playtesters were not having a good time figuring out the mechanic, so I think making it easier was the right choice in the end.

## Judgement / Verdict

This mechanic was a holdover from an old version of the true achievemnt reveal--originally, once you solved `THE WORLD`, the pillars would drop down, revealing blocks with an ambiguous height (using the Celeste mechanic) and an ambiguous color (using this mechanic).

I dunno how I feel about the mechanic however--I like pretty much all of the puzzles except the Phoenix Wright puzzles (I couldn't come up with many interesting ways to use 'not'), but my original idea for where the mechanic would go (complex boolean algebra) (CBA reference!) would probably not make for fun puzzling.

A funny thing is that this mechanic used to be notated with sign panels with `||`, `&&`, and `!` instead of quarter-size blocks. However, this was about when PP started to get unplayably laggy--the main culprit, according to Chris, is Godot's implementation of viewports, which each sign panel requires to render. This led me to switch to quarter-size blocks to hopefully reduce some of the lag.

## The World
