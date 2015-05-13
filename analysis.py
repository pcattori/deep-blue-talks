import chess
from chess import SquareSet

class MoveAnalyzer():
  def __init__(self, board):
    self.board = board

  def controls(self, move):
    '''Returns a set of attacked/defended squares'''
    to_move = self.board.turn
    analysis_board = chess.Board(self.board.fen())
    analysis_board.push(move)
    squares = 0
    for square in chess.SQUARES:
      if move.to_square in analysis_board.attackers(to_move, square):
        squares |= chess.BB_SQUARES[square]
    return SquareSet(squares)

  # medium
  def protected(move):
    '''Cannot be taken at all or may be exchanged for piece of >= value'''
    # if defended return not attacked by pieces of lesser value
    pass

  # medium
  def unprotected(move):
    '''Moved piece can be taken'''
    pass

  # easy
  def comes_to_defense(move):
    '''Adds defender to equalize control of a square'''
    pass

  def develops(self, move):
    to_move = self.board.turn
    piece_type = self.board.piece_type_at(move.from_square)
    if piece_type == chess.PAWN or piece_type == chess.KING:
      return False
    if to_move == chess.WHITE:
      return move.to_square not in SquareSet(chess.BB_RANK_1)
    elif to_move == chess.BLACK:
      return move.to_square not in SquareSet(chess.BB_RANK_8)
    return False

  def absolutely_pinned(self, square):
    return pinned(square, chess.KING)

  def pinned(self, square, piece_type):
    color = self.board.piece_at_square(square).color
    target_squares = self.board.pieces(piece_type, color)
    if len(target_squares) == 0:
      return False
    for target_square in target_squares:
      analysis_board = chess.Board(self.board.fen())
      original_target_attackers = self.board.attackers(not color, target_square)
      analysis_board.remove_piece_at(square)
      new_target_attackers = analysis_board.attackers(not color, target_square)
      if original_target_attackers ^ (original_target_attackers & new_target_attackers):
        return True
    return False

  def discovered_attack(self, move, square):
    analysis_board = chess.Board(self.board.fen())
    original_target_attackers = self.board.attackers(not color, target_square)
    analysis_board.remove_piece_at(square)
    new_target_attackers = analysis_board.attackers(not color, target_square)
    new_target_attackers_not_me = new_target_attackers & (~ chess.BB_SQUARES[move.to_square])
    return original_target_attackers ^ (original_target_attackers & new_target_attackers_not_me)

  def dims_knight(self, move):
    '''Knight on the rim is dim'''
    if self.board.piece_type_at(move.from_square) == chess.KNIGHT:
      rim = SquareSet(
          chess.BB_RANK_1 | \
          chess.BB_RANK_8 | \
          chess.BB_FILE_A | \
          chess.BB_FILE_H)
      return move.to_square in rim

  # easy
  def chains_pawns(self, move):
    pass

  # easy
  def doubles_pawns(self, move):
    pass

  # easy
  def isolates_pawns(self, move):
    pass

  # medium
  def attacks_along_file(self, move):
    pass

  # medium
  def attacks_along_diagonal(self, move):
    pass

  def pins(self, move, square, piece_type):
    analysis_board = chess.Board(self.board.fen())
    analysis_board.push(move)
    analyzer = MoveAnalyzer(analysis_board)
    return analyzer.pinned(square, piece_type)

  def unpins(self, move, square, piece_type):
    return not pins(move, square, piece_type)

  # medium
  def skewers(move):
    pass

  # medium
  def increases_king_safety(move):
    pass

  # medium
  def decreases_king_safety(move):
    pass

  # hard
  def gains_tempo(move):
    pass

  # hard
  def loses_tempo(move):
    pass

  def controls_center(self, move):
    center = SquareSet(chess.BB_D4 | chess.BB_D5 | chess.BB_E4 | chess.BB_E5)
    for square in self.controls(move):
      if square in center:
        return True
    return False

  # medium
  def counterattacks(move):
    pass

  # hard
  def wins_material(move):
    pass

  # hard
  def loses_material(move):
    pass

  # hard
  def maintains_tension(move):
    pass

  # easy
  def opens_position(self, move):
    to_move = self.board.turn
    if self.board.piece_type_at(move.from_square) == chess.PAWN:
      if move.to_square not in SquareSet(chess.BB_RANK_1 | chess.BB_RANK_8):
        num_pawns_before = len(self.board.pieces(chess.PAWN, not to_move))
        analysis_board = chess.Board(self.board.fen())
        analysis_board.push(move)
        num_pawns_after = len(analysis_board.pieces(chess.PAWN, not to_move))
        return num_pawns_before != num_pawns_after
    return False

  def closes_position(self, move):
    piece = self.board.piece_at(move.from_square)
    if piece and piece.piece_type == chess.PAWN:
      if not self.opens_position(move):
        from_bb_square = chess.BB_SQUARES[move.from_square]
        pawn_attack = 0
        if piece.color == chess.WHITE:
          pawn_attack |= chess.shift_up_left(from_bb_square)
          pawn_attack |=  chess.shift_up_right(from_bb_square)
        elif piece.color == chess.BLACK:
          pawn_attack |= chess.shift_down_left(from_bb_square)
          pawn_attack |= chess.shift_down_right(from_bb_square)
        for square in SquareSet(pawn_attack):
          if self.board.piece_type_at(square) == chess.PAWN:
            return True
    return False

  def offers_trade(move):
    pass

  # medium
  def stalls_development(move):
    # usually only applies to bishops, unless pawns move to 4 knight positions
    pass

# terminology
  def exchanges(move):
    pass

  def fiancchettos(move):
    pass

  def castles(move):
    pass

  def artificially_castles(move):
    pass

  def gambits(move):
    pass

  def sacrifices(move):
    pass

  def traps(move):
    pass

class BoardAnalyzer():
  def __init__(self, board):
    self.board = board

  def weaknesses():
    '''targets, outposts, etc'''
    pass
