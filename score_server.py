import socket
# keep track of all information
human_games = 0
ai_games = 0
num_of_clients = 0
x_win = 0
o_win = 0
draw = 0
address_list = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 1234))
    # keep taking information from client and unpack and decode
    # the message into score and player information
    # put them into a string and send the information back
    while True:
        s.listen(5)
        clientsocket, address = s.accept()
        if address not in address_list:
            num_of_clients += 1
            address_list.append(address)
            with clientsocket:
                message = clientsocket.recv(1024)
                if message.decode("utf-8") != '':
                    score, player = message.split()
                    score = score.decode("utf-8")
                    player = player.decode("utf-8")
                    if player == 'ai':
                        ai_games += 1
                    elif player == 'human':
                        human_games += 1
                    print("there have been {} human games and {} AI games reported from {} number of clients"\
                          .format(human_games, ai_games, num_of_clients))
                    if score == 'X':
                        x_win += 1
                    elif score == 'O':
                        o_win += 1
                    elif score == 'tie':
                        draw += 1
                    clientsocket.send(bytes("player x wins {} player o wins {} and draws {}"\
                          .format(x_win, o_win, draw), "utf-8"))
                    clientsocket.close()

