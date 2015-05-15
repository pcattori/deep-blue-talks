6.xxx Project

If Deep Blue could talk
=======================
[![PyPI version](https://badge.fury.io/py/deep-blue-talks.svg)](http://badge.fury.io/py/deep-blue-talks)

With a GM mind provided by [Stockfish][stockfish].

Built with the [chess python package][python-chess].

Installation
------------
```bash
$ pip install deep-blue-talks
```

Run
---
```bash
$ deep-blue-talks
```

#### Output
If you enter
```bash
> board
```

then you should see
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
>
```
[Nota Bene][nb]: Depending on your terminal, the colors of the pieces may be inverted. To correct this, toggle the boolean value of the `inverted` setting inside `/usr/local/bin/deep-blue-talks` with `vim` (or any lesser text editor of your choosing). This should be fixed for the 0.3 release.

Play
----
Enter moves in [SAN][san]

eg. [The Scholar's Mate][scholars mate]
```bash
> move e4
> move e5
> move Qh5
> move Nc6
> move Bc4
> move Nf6
> move Qxf7
```

Commands
--------
- **help**: see available commands
- **resign**: ends the game
- **fen**: get or set FEN
- **move**: move a piece on the board using SAN
- **ask**: ask about a particular move
- **advice**: get advice for what to play next
- **board**: display the chess board
- **engine**: configure [UCI][uci] options for backend chess engine

Example Usage
-------------

Interesting [FEN][fen]
```bash
$ ./play
$ fen "r1b1kb1r/ppq2ppp/2n2n2/1Bpp4/3pP3/2N2N1P/PPP2PP1/R1BQR1K1 w kq - 0 9"
$ board
$ engine MultiPv 5
$ advice
$ ask Nh4
```

[HEAD]: footnote

[stockfish]: http://stockfishchess.org/
[python-chess]: https://github.com/niklasf/python-chess
[nb]: http://en.wikipedia.org/wiki/Nota_bene
[san]: http://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29
[scholars mate]: http://en.wikipedia.org/wiki/Scholar%27s_mate
[uci]: http://wbec-ridderkerk.nl/html/UCIProtocol.html
[fen]: http://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
