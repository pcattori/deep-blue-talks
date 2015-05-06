6.xxx Project

If Deep Blue could talk
=======================

Installation
------------
Requires the [chess python package][python-chess]

```bash
$ pip install python-chess
```

Download:
```bash
git clone https://github.com/pcattori/deep-blue.git
```

Then in the `deep-blue` directory:

```bash
chmod +x play
```

Run
---
```bash
$ ./play
```
or
```bash
$ python play
```

Results in:
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


With a GM mind provided by [Stockfish][stockfish]

[python-chess]: https://github.com/niklasf/python-chess
[nb]: http://en.wikipedia.org/wiki/Nota_bene
[scholars mate]: http://en.wikipedia.org/wiki/Scholar%27s_mate
[stockfish]: http://stockfishchess.org/
