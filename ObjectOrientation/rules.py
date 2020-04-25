class Rules:
    NUMBER_MIN_KEEP_ALIVE = 2
    NUMBER_MAX_KEEP_ALIVE = 3
    NUMBER_RETURN_ALIVE = 2

    @staticmethod
    def born(numberNeighbours):
        return numberNeighbours == Rules.NUMBER_RETURN_ALIVE

    @staticmethod
    def kill(numberNeighbours):
        return numberNeighbours < Rules.NUMBER_MIN_KEEP_ALIVE or numberNeighbours > Rules.NUMBER_MAX_KEEP_ALIVE