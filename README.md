[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Aegis1916/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Aegis1916/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01 entry

A chess engine in 3,929 bytes of Python (standard library only), built for
make.fun's "Build the strongest chess engine in 4 KB of Python".

`main.py` is the whole engine: negamax search with alpha-beta pruning,
quiescence search with delta pruning and check extensions, MVV-LVA and
killer-move ordering, and a tapered evaluation with piece-square tables,
bishop-pair, rook open-file, king-tropism and pawn-structure terms. It plays
the gauntlet through the env at MAKEFUN_ENV_URL (POST /game, POST /move) with
a fixed depth and node budget, so its moves are deterministic.

MIT licensed, see LICENSE.
