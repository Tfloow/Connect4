import itertools
import numpy as np
import random

def ai_student(board, player):


  return possibleMove(board, player)

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
      myPlace.append((j,i))
    elif board[i][j] == 0:
      continue
    else:
      oppPlace.append((i, j))

  return myPlace

def getBit(placePiece):
  """
  :param placePiece: liste de mes pièces
  :return: un dictionnaire avec les ensembles de lignes
  """
  bit = {}
  sized = [1,2,3,4]
  biggestSol = []
  sizeMax = 0


  if len(placePiece) == 0:
    return None


  for indexing in placePiece:
    for i in range(-1,2):
      for j in range(-1,2):
        if i == 0 and j == 0:
          continue
        else:
          if (indexing[0]+i, indexing[1]+j) in placePiece:
              # 3 d'affilé
              if (indexing[0] + 2*i, indexing[1] + 2*j) in placePiece:
                if (indexing[0] + 3*i, indexing[1] + 3*j) in placePiece:
                  if 4 in sized:
                    sized.pop(sized.index(4))
                    bit[4] = []
                    bit[4].append([(indexing[0], indexing[1]), (indexing[0] + i, indexing[1] + j),
                                 (indexing[0] + 2 * i, indexing[1] + 2 * j),(indexing[0] + 3 * i, indexing[1] + 3 * j)])
                  else:
                    bit[4].append([(indexing[0], indexing[1]), (indexing[0] + i, indexing[1] + j),
                                   (indexing[0] + 2 * i, indexing[1] + 2 * j),
                                   (indexing[0] + 3 * i, indexing[1] + 3 * j)])

                if 3 in sized:
                  sized.pop(sized.index(3))
                  bit[3] = []
                  bit[3].append([(indexing[0], indexing[1]),(indexing[0]+i, indexing[1]+j),(indexing[0]+2*i, indexing[1]+2*j)])
                else:
                  bit[3].append([(indexing[0], indexing[1]),(indexing[0]+i, indexing[1]+j),(indexing[0]+2*i, indexing[1]+2*j)])
              # 2 d'affilé en diag
              else:
                if 2 in sized:
                  sized.pop(sized.index(2))
                  bit[2] = []
                  bit[2].append([(indexing[0], indexing[1]),(indexing[0]+i, indexing[1]+j)])
                else:
                  bit[2].append([(indexing[0], indexing[1]),(indexing[0]+i, indexing[1]+j)])
  return bit

def fallingPlace(board):
  """
  :param board: plateau de puissance 4
  :return: retourne les endroits où peut tomber notre prochaine pièce
  """
  fallingOne = [(i, len(board)-1) for i in range(len(board[0]))]

  for i in range(len(board[0])):
    for j in range(len(board)):
      if board[j][i] != 0:
        fallingOne[i] = ((i,j-1))
        break

  return fallingOne

def possibleMove(board, player):
  bitMine = getBit(getPlacing(board, player))
  opp = (player%2)+1
  bitOpp = getBit(getPlacing(board, opp))
  move = fallingPlace(board)
  moveCloned = move.copy()
  bestMove = []

  for moveCheck in move:
    if moveCheck[1] == -1:
      moveCloned.remove(moveCheck)

  if bitMine == None:
    print("i guesssss")
    return moveCloned[random.randint(0, len(moveCloned) - 1)]



  move = futureCheck(board, player)
  danger = futureCheck(board, opp)

  if danger[0] >= 1000:
    print("dangerous move")
    print(danger[1])
    return danger[1]
  elif move[0] is not None:
    print("done the best")
    print(move[1])
    if move[1] is None:
      return moveCloned[random.randint(0, len(moveCloned) - 1)] #if we are almost at a draw and everything is full
    return move[1]
  else:
    print("i guesssss")
    return moveCloned[random.randint(0,len(moveCloned)-1)]


def futureCheck(board, player):
  bitMine = getBit(getPlacing(board, player))
  move = fallingPlace(board)
  moveCloned = move.copy()
  adv = None

  for moveCheck in move:
    if moveCheck[1] == -1:
      moveCloned.remove(moveCheck)

  if bitMine is None:
    return
  maxAdv = 0

  for possibleFuture in moveCloned:
    possibleBoard = board.copy()
    possibleBoard[possibleFuture[1]][possibleFuture[0]] = player
    bitMinePossible = getBit(getPlacing(possibleBoard, player))
    newBit = (len(bitMinePossible.get(2, []))-len(bitMine.get(2,[])))*2 + (len(bitMinePossible.get(3, []))-len(bitMine.get(3,[])))*3 + (len(bitMinePossible.get(4, []))-len(bitMine.get(4,[])))*1000
    if newBit > maxAdv:
      maxAdv = newBit
      adv = possibleFuture

  return (maxAdv,adv)
