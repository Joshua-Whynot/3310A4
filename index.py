from gamesList import gamesLinkedList
from game import Game
from node import node
from linearSearch import linearSearch


def main():
    #open file
    file = open("games.csv", "r")
    #create linked list
    gamesList = gamesLinkedList()
    #read file
    #skip first line
    file.readline()
    duplicatecounter = 0
    for line in file:
        #split line
        data = line.split(",")
        #check if name already exists in linked list
        x = linearSearch(gamesList, data[1])
        if x != None:
            duplicatecounter += 1
            #check if user rating count is higher
            if x.game.userRatingCount < data[3]:
                #delete game from linked list
                gamesList.deleteGame(x)
            else:
                continue
            #increment duplicate counter
            
        #create game
        game = Game(data[0], data[1], data[2], data[3], data[4], data[5])
        
        #create node
        newnode = node(game)
        #add node to linked list
        gamesList.addGame(newnode)
    #close file
    file.close()
    print('Gamecount:', gamesList.length)
    print('Duplicatecount:', duplicatecounter)


if __name__ == "__main__":
    main()