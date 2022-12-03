# day_2.py

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
translate = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

# A = Rock, B = Paper, C = Scissors
# X = loss, Y = draw, Z = win
translate_inverse = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win',
}

# first is opponent, second is me
game_guide = {
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
game_guide_inverse = {
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
# Loss = 0 points, Draw = 3 points, Win = 6 points

score_guide = {
    'R': 1,
    'P': 2,
    'S': 3,
    'loss': 0,
    'draw': 3,
    'win': 6,
}


def get_score(play):
    me = play[2]
    points = score_guide[me] + score_guide[game_guide[play]]
    return points


def get_play(line_stripped):
    opponent = line_stripped[0]
    me = line_stripped[2]
    play = translate[opponent] + ' ' + translate[me]
    return play


def get_play_inverse(line_stripped):
    opponent = line_stripped[0]
    outcome = line_stripped[2]
    play_inverse = translate_inverse[opponent] + ' ' + translate_inverse[outcome]
    play = translate[opponent] + ' ' + game_guide_inverse[play_inverse]
    return play


def main(input):

    total_points = 0

    with open(input) as f:
        for line in f:
            line_stripped = line.strip()
            if line_stripped:  # check if not empty
                # play = get_play(line_stripped)
                play = get_play_inverse(line_stripped)
                total_points += get_score(play)

    print(total_points)


if __name__ == '__main__':
    input = 'input/day_2_full.txt'
    main(input)
