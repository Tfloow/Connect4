import itertools
import numpy as np

def ai_student(board, player):
  board = np.copy(board)
  nonfull_cols = np.where(board[0] == 0)[0]
  colonne_choisie = nonfull_cols[0]

  return colonne_choisie


def possibleMove(board, player, notFullCol):
  placePiece, placeOpp = getPlacing(board, player)
def getPlacing(board, player):
  """

  :param board: board de puissance 4
  :param player: qui on joue
  :return: retourne deux listes avec mes pièces et les pièces de l'adversaire
  """
  myPlace = []
  oppPlace = []

  # add as an index in two different list the position
  for i, j in itertools.product(range(len(board)), range(len(board[0]))):
    if board[i][j] == player:
      myPlace.append((i, j))
    elif board[i][j] == 0:
      continue
    else:
      oppPlace.append((i, j))

  return myPlace, oppPlace

def getBit(placePiece, placeOpp):
  """
  :param placePiece: liste de mes pièces
  :param placeOpp:  liste pièces adverses
  :return: un dictionnaire avec les ensembles de lignes
  """

def fallingPlace(board):
  """
  :param board: plateau de puissance 4
  :return: retourne les endroits où peut tomber notre prochaine pièce
  """
  fallingOne = [(i, len(board[0])) for i in range(len(board[0]))]

  for i in range(len(board[0])):
    for j in range(len(board)):
      if board[j][i] != 0:
        fallingOne[i] = ((i,j-1))
        break

  return fallingOne
