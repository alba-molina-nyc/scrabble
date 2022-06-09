# Scrabble

### Board Grid

How to render 225 squares any one square that could be accessed at anytime

- consider using nested arrays, for each row, create an empty array and then push in 15 arrays
- into each of these nested array, render a div that most importantly contains a unique identifier we use to play the game

### Keeping track of tiles

- what happens when a tile is being moved from one place to another, or when a player decides to back track and start over
  - need to keep stock of the tiles (consider using stacks?)
  - the stacks keep track of tiles in a move and are cleared after the end of a turn

### API Calls

- give player the option for it to automatically check the api when placing a word OR let the players decide when to call b.s. and challenge a word?

### Rules to keep in mind

1. Official scrabble tile number, and each letter value tied to each
2. Official scrabble board score for each square
   -- from rules 1 and 2 be able to loop through the letter value tied to each tile and also for each square where those tiles are placed in order to do the math and get how much the word placed is worth
   -- figure out a way to figure out adjacency i.e) if a word ends up creating more than one word, how to calculate that
3. Words must build on another word

- if they do then do 1,2 above
- if not the send error and maybe little pop up "sorry, words must build on another word"
