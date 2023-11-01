class Game:
    all = []
    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title"):
            self._title = title


    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        return sum([result.score for result in self.results()]) / len(self.results())

class Player(Game):
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username


    def results(self):
        return [result for result in Result.all if result.player is self]
    

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        played = [result.game for result in self.results()]
        return played.count(game)
    
    @classmethod
    def highest_scored(cls, game):
        players = [player for player in cls.all if player.played_game(game)]

        if not players:
            return None
        
        high_score = max(players, key = lambda player: player.average_score(game))

        return high_score

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
    
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game


    

