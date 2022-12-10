# day_2.py

class ProblemDefinition():
    def __init__(self):
        # A = Rock, B = Paper, C = Scissors
        # X = Rock, Y = Paper, Z = Scissors
        self.translate = {
            'A': 'R',
            'B': 'P',
            'C': 'S',
            'X': 'R',
            'Y': 'P',
            'Z': 'S',
        }
        # A = Rock, B = Paper, C = Scissors
        # X = loss, Y = draw, Z = win
        self.translate_inverse = {
            'A': 'R',
            'B': 'P',
            'C': 'S',
            'X': 'loss',
            'Y': 'draw',
            'Z': 'win',
        }
        # first is opponent, second is me
        self.game_guide = {
            'R R': 'draw',
            'R P': 'win',
            'R S': 'loss',
            'P R': 'loss',
            'P P': 'draw',
            'P S': 'win',
            'S R': 'win',
            'S P': 'loss',
            'S S': 'draw',
        }
        # first is opponent, second is outcome
        self.game_guide_inverse = {
            'R draw': 'R',
            'R win': 'P',
            'R loss': 'S',
            'P loss': 'R',
            'P draw': 'P',
            'P win': 'S',
            'S win': 'R',
            'S loss': 'P',
            'S draw': 'S',
        }
        # Rock = 1 points, Paper = 2 points, Scissors = 3 points
        # loss = 0 points, draw = 3 points, win = 6 points
        self.score_guide = {
            'R': 1,
            'P': 2,
            'S': 3,
            'loss': 0,
            'draw': 3,
            'win': 6,
        }


def get_score(play, pd):
    me = play[2]
    points = pd.score_guide[me] + pd.score_guide[pd.game_guide[play]]
    return points


def get_play(line, pd):
    opponent = line[0]
    me = line[2]
    play = pd.translate[opponent] + ' ' + pd.translate[me]
    return play


def get_play_inverse(line, pd):
    opponent = line[0]
    outcome = line[2]
    play_inverse = pd.translate_inverse[opponent] + ' ' + pd.translate_inverse[outcome]
    play = pd.translate[opponent] + ' ' + pd.game_guide_inverse[play_inverse]
    return play


def main(input, part):

    pd = ProblemDefinition()

    total_points_1 = 0
    total_points_2 = 0

    with open(input) as f:
        for line in f:
            line = line.strip()
            if line:  # check if not empty
                play_1 = get_play(line, pd)  # for part 1
                play_2 = get_play_inverse(line, pd)  # for part 2
                total_points_1 += get_score(play_1, pd)
                total_points_2 += get_score(play_2, pd)

    if part == 0:
        return total_points_1, total_points_2
    elif part == 1:
        return total_points_1
    elif part == 2:
        return total_points_2


if __name__ == '__main__':
    input = 'input_test/day_2.txt'
    part = 0
    print(main(input, part))
