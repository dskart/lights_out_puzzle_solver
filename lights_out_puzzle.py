import random
import copy
import queue


class LightsOutPuzzle(object):

    def __init__(self, board):
        self._board = board
        self._xdim = len(board[0])
        self._ydim = len(board)

    def get_board(self):
        return self._board.copy()

    def perform_move(self, row, col):
        self._board[row][col] ^= True

        if row + 1 <= self._ydim - 1:
            self._board[row+1][col] ^= True
        if row - 1 >= 0:
            self._board[row-1][col] ^= True
        if col + 1 <= self._xdim - 1:
            self._board[row][col+1] ^= True
        if col - 1 >= 0:
            self._board[row][col-1] ^= True

    def scramble(self):
        for row in range(self._ydim):
            for col in range(self._xdim):
                if random.random() < 0.5:
                    self.perform_move(row, col)

    def is_solved(self):
        for row in range(self._ydim):
            for col in range(self._xdim):
                if self._board[row][col]:
                    return False
        return True

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for row in range(self._ydim):
            for col in range(self._xdim):
                puzzle = self.copy()
                puzzle.perform_move(row, col)
                move = (row, col)
                yield (move, puzzle.copy())

    def find_solution(self):
        frontier = queue.Queue()

        frontier.put(self)
        start = tuple(map(tuple, self._board))
        visited = {}
        visited[start] = [None, None]

        while not frontier.empty():
            current = frontier.get()
            current_board = current.get_board()
            current_board_tuple = tuple(map(tuple, current_board))
            if current.is_solved():
                return []

            for move, new_puzzle in current.successors():
                new_board = new_puzzle.get_board()
                new_board_tuple = tuple(map(tuple, new_board))
                if new_board_tuple not in visited:
                    if new_puzzle.is_solved():
                        visited[new_board_tuple] = (current_board_tuple, move)
                        moves = self.BacktrackMoves(visited, new_board_tuple)
                        return moves

                    frontier.put(new_puzzle)
                    visited[new_board_tuple] = [current_board_tuple, move]

        return None

    def BacktrackMoves(self, visited, goal):
        current = [goal, None]
        start = tuple(map(tuple, self._board))
        path = []
        while current[0] != start:
            current = visited[current[0]]
            path.append(current[1])

        return path

    def PrintBoard(self):
        for row in self._board:
            print(row)


def create_puzzle(rows, cols):
    one_row = [False for col in range(cols)]
    board = [one_row.copy() for row in range(rows)]
    return LightsOutPuzzle(board)
