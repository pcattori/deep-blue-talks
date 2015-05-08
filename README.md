6.xxx Project

If Deep Blue could talk
=======================

With a GM mind provided by [Stockfish][stockfish].

Built with the [chess python package][python-chess].

Installation
------------
Download
```bash
git clone https://github.com/pcattori/deep-blue.git
```

Move to project
```bash
$ cd deep-blue
```

Install requirements
```bash
$ pip install -r requirements.txt
```

Run
---
```bash
$ python play
```

### Alternative
make `play` executable
```bash
chmod +x play
```
then run like this
```bash
$ ./play
```

### Output
You should see
```bash
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 
6 · · · · · · · · 
5 · · · · · · · · 
4 · · · · · · · · 
3 · · · · · · · · 
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 
  a b c d e f g h
!
```
[Nota Bene][nb]: Designed for dark background terminals where black pieces show up as white and white pieces show up as black. I have switched the pieces to that the board shows up correctly on dark background terminals. The pieces are *actually* switched and will appear incorrect in light background terminals

Play
----
Enter moves in SAN

eg. [The Scholar's Mate][scholars mate]
```bash
! e4
! e5
! Qh5
! Nc6
! Bc4
! Nf6
! Qxf7
```

Commands
--------
- **moves**: displays all moves made so far
- **resign**: ends the game
- **advice**: ask about which move you should make and which move you should watch out for next
- **board**: print out the board

[HEAD]: footnote

[stockfish]: http://stockfishchess.org/
[python-chess]: https://github.com/niklasf/python-chess
[nb]: http://en.wikipedia.org/wiki/Nota_bene
[scholars mate]: http://en.wikipedia.org/wiki/Scholar%27s_mate
