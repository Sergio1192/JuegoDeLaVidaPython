class Constants:
    NUMBER_MIN_KEEP_ALIVE = 2
    NUMBER_MAX_KEEP_ALIVE = 3
    NUMBER_RETURN_ALIVE = 3

class Rules:
    @staticmethod
    def born(numberNeighbours):
        return numberNeighbours == Constants.NUMBER_RETURN_ALIVE

    @staticmethod
    def kill(numberNeighbours):
        return numberNeighbours < Constants.NUMBER_MIN_KEEP_ALIVE or numberNeighbours > Constants.NUMBER_MAX_KEEP_ALIVE