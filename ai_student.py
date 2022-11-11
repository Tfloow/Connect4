import numpy as np

def ai_student(board, player):
  board = np.copy(board)
  nonfull_cols = np.where(board[0] == 0)[0]
  colonne_choisie = nonfull_cols[0]

  return colonne_choisie


