import random

# use 16 players for example
players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kevin', 'Linda', 'Mike', 'Nancy', 'Oscar', 'Pamela']
MAX_LEN = max(map(len, players))

def generatePairings(players):
    # Generate pairings
    temp = players.copy()
    random.shuffle(temp)
    # Make a list of 2-tuple pairings
    pairings = list(map(lambda p: (p[0], p[1]), zip(temp[::2], temp[1::2]))) # Make a list of 2-tuple pairs
    if len(players) % 2 == 1:
        pairings.append((temp[-1], None))
    return pairings

def playMatch(player1, player2):
    # Play a match and return the winner
    if player2 == None:
        return player1
    else:
        winner = None
        while winner not in ['1', '2']:
            if winner != None:
                print('Invalid input')
            # winner = input('{:s} (1) vs. {:s} (2). Who won? (1/2): '.format(player1, player2))
            winner = random.choice(['1', '2'])
        return player1 if winner == '1' else player2
    
def playRound(pairings):
    # Play a round and return the next bracket
    nextPairings = []
    newMatch = []
    for match in pairings[::-1]:
        winner = playMatch(match[0], match[1])
        newMatch.insert(0, winner)
        if len(newMatch) == 2:
            nextPairings.append(tuple(newMatch))
            newMatch.clear()
    if len(newMatch) == 1:
        newMatch.append(None)
        nextPairings.append(tuple(newMatch))
    nextPairings.reverse()
    return nextPairings

history = [generatePairings(players)]
while len(history[-1]) > 1 or history[-1][0][1] is not None:
    print(history[-1])
    history.append(playRound(history[-1]))
print('Winner:', history[-1][0][0])

def printNameLine(name, r, m, p, NUM_ROUNDS):
    # Print a line of a name
    for r in range(r):
        print((' '*(MAX_LEN+4))+'|', end='')
        if r == r-1:
            print('_'*3, end='')
        else:
            print(' '*3, end='')
    print((('{:s}')+'_'*3).format(name+' '+(MAX_LEN-len(name))*'_'))

def printBracket(history):
    # Print the full bracket
    NUM_ROUNDS = len(history)
    # print(('{:>'+str(MAX_LEN)+'}').format(history[i][0][0]))
    draw = lambda r, m, p : printNameLine(history[r][m][p], r, m, p, NUM_ROUNDS)
    sequence = [
        '000', '100', '001', '200', '010', '101', '011', '300',
        '020', '110', '021', '201', '030', '111', '031', '400',
        '040', '120', '041', '210', '050', '121', '051', '301',
        '060', '130', '061', '211', '070', '131', '071'
    ]
    indices = []
    for s in sequence:
        r, m, p = map(int, s)
        indices.append((r, m, p))
    for i in indices:
        draw(i[0], i[1], i[2])
    

printBracket(history)


# def generateBracket(players):
#     # Generate starting bracket
#     temp = players.copy()
#     random.shuffle(temp)
#     # Make a list of 2-tuple pairings
#     bracket = list(map(lambda p: (p[0], p[1]), zip(temp[::2], temp[1::2]))) # Make a list of 2-tuple pairs
#     if len(players) % 2 == 1:
#         bracket.append((temp[-1], None))
#     return bracket

# def generateNameLine(name, end=''):
#     return name+' '+'_'*(MAX_NAME_LENGTH-len(name))+end

# # Print the full bracket
# def printHistory(history):
#     # for index in range(len(history)-1, -1, -1):
#     index = 0
#     round = history[index]
#     remaining = len(history)-index-1
#     print('Round', index + 1)
#     for match_index in range(len(round)):
#         match = round[match_index]
#         print(generateNameLine(match[0]))
#         if (match[1] != None):
#             for _ in range(((remaining*2)+1)//2):
#                 print(' '*(MAX_NAME_LENGTH), '|')
#             if index+1 < len(history):
#                 print(' '*(MAX_NAME_LENGTH), '|', history[index+1][(match_index+1)//2][0])
#             print(' '*(MAX_NAME_LENGTH), '|')
#             if index+1 < len(history):
#                 print(' '*(MAX_NAME_LENGTH), '|', history[index+1][(match_index+1)//2][1])
#             for _ in range(((remaining*2)-1)//2):
#                 print(' '*(MAX_NAME_LENGTH), '|')
#             print(generateNameLine(match[1], end='|'))
#         print()
#     print()

# def playMatch(player1, player2):
#     # Play a match and return the winner
#     if player2 == None:
#         return player1
#     else:
#         winner = None
#         while winner not in ['1', '2']:
#             if winner != None:
#                 print('Invalid input')
#             winner = input('{:s} (1) vs. {:s} (2). Who won? (1/2): '.format(player1, player2))
#         return player1 if winner == '1' else player2

# def playRound(bracket):
#     # Play a round and return the next bracket
#     nextBracket = []
#     newMatch = []
#     for match in bracket[::-1]:
#         winner = playMatch(match[0], match[1])
#         newMatch.append(winner)
#         if len(newMatch) == 2:
#             nextBracket.append(tuple(newMatch))
#             newMatch.clear()
#     if len(newMatch) == 1:
#         newMatch.append(None)
#         nextBracket.append(tuple(newMatch))
#     nextBracket.reverse()
#     return nextBracket

# def startTournament(players):
#     # Generate starting bracket
#     bracket = generateBracket(players)
#     history = [bracket]
#     printHistory(history)
#     # Start tournament
#     print('Starting tournament...')
#     history.append(playRound(bracket))
#     printHistory(history)
#     return history

# # Start the program
# startTournament(players)
