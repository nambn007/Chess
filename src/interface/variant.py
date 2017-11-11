from abc import ABCMeta, abstractmethod
from typing import Sequence, Type, TYPE_CHECKING, Set

if TYPE_CHECKING:
    from interface.board import Board
    from interface.move import Move
    from interface.piece import Piece
    from interface.side import Side
    from interface.position import Position


class Variant(metaclass=ABCMeta):
    @property
    @abstractmethod
    def board(self) -> Type['Board']:
        pass

    @abstractmethod
    def init_board_state(self) -> str:
        """
        Sets Board init state for this game mode
        :return FEN strong of part with board only
        """
        pass

    @abstractmethod
    def assert_move(self, move: Type['Move']) -> bool:
        """
        Assert if given move in current game state and game mode is legal
        :param move: Move type
        :return: bool, positive if given move is legal
        """
        pass

    @property
    @abstractmethod
    def pieces(self) -> Sequence[Type['Piece']]:
        """
        :return: Tuple of Pieces supported with implemented GameMode
        """
        pass

    @property
    @abstractmethod
    def sides(self) -> Sequence[Type['Side']]:
        """
        :return: tuple of players sides
        """
        pass

    @abstractmethod
    def standard_moves(self, position: Type['Position']) -> Set[Type['Position']]:
        pass

    @abstractmethod
    def standard_captures(self, position: Type['Position']) -> Set[Type['Position']]:
        pass

    @abstractmethod
    def attacked_fields(self, position: Type['Position']) -> Set[Type['Position']]:
        pass

    @abstractmethod
    def attacked_fields_by_sides(self, side: Type['Side']) -> Set[Type['Position']]:
        pass
