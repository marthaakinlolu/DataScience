import csv

def load_data(filename):
    file = " "
    with open(filename, 'r') as csv_file:
        csv_reader = csv_file.readlines()
        for row in csv_reader:
            values = row.split('|')
            for i in values:
                if len(i) > 1:
                    file += i

def analyse_nba_game(play_by_play_moves):
    for moves in play_by_play_moves:
        print(moves)
        


play_by_play_moves = load_data("nba_game_warriors_thunder_20181016.txt")
print(analyse_nba_game(play_by_play_moves))