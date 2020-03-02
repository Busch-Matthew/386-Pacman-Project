vector = pygame.math.Vector2


class Score():

    def __init__(self, text ,score, left, top):


        self.position = vector(left, top)
        self.score = score
        self.text = text
        self.output = f'{text}: {self.score}'
