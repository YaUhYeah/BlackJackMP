class Game:
    def __init__(self, id, player, player2):
        self.p1Went = False
        self.player = player
        self.player2 = player2
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moved = [None,None]

    def get_player_moved(self,p):
        return self.moved[p]

    def play(self, player, move):
        self.moved[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
