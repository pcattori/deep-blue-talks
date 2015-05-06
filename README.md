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
- moves: displays all moves made so far
- resign:
- advice
- board


With a GM mind provided by [Stockfish][stockfish]

[python-chess]: https://github.com/niklasf/python-chess
[scholars mate]: http://en.wikipedia.org/wiki/Scholar%27s_mate
[stockfish]: http://stockfishchess.org/
