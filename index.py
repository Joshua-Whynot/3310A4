# CS3310 Fall 2024 Assignment 4
# Author: Joshua Whynot
# Date: 12/3/24
# Updated: 12/5/24

#Data structure imports
from gamesList import gamesLinkedList
from game import Game 
from node import node
#search algorithm imports
from linearSearch import linearSearch
from binarySearch import binarySearch
#library imports
import random
import time
import csv #need this for csv file reading because there is , inside the data
import sys
#sorting algorithm imports
from insertionSort import insertionSort
from quickSort import quickSort
#set recursion limit, we have a lot of inputs
sys.setrecursionlimit(1000000)

#main function
def main():
    #open file
    file = open("games.csv", "r")
    #create linked list
    gamesList = gamesLinkedList()
    #read file
    #skip first line
    file.readline()
    with open('games.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line
        for row in reader:
            # Check if name already exists in linked list
            x = linearSearch(gamesList, row[1])
            if x is not None:
                # Check if user rating count is higher
                if x.game.userRatingCount < row[3]:
                    # Delete game from linked list
                    gamesList.deleteGame(x)
                else:
                    continue
            # Create game
            game = Game(row[0], row[1], row[2], row[3], row[4], row[5])
            # Create node
            newnode = node(game)
            # Add node to linked list
            gamesList.addGame(newnode)
    #print first five games
    gamecount = gamesList.length
    print(f"There are {gamecount} games in the list.")
    print("Before sorting:")
    print_first_five(gamesList)
    print('')
    #test linear search
    for i in range(3):
        print(f"Search number {i + 1}:")
        time_elapsed_a, time_elapsed_b = linear_search_test(gamesList)
        print(f"Single search time: {round(time_elapsed_a)} nanoseconds.")
        print(f"Average search time: {round(time_elapsed_b)} nanoseconds.")
        print('')
    #sort linked list by name with insertion sort and quick sort
    gamesList1 = gamesList
    gamesList2 = gamesList
    start = time.time()
    insertionSort(gamesList1)
    end = time.time()
    startb = time.time()
    quickSort(gamesList2)
    endb = time.time()

    
    print('After Sorting:')
    print_first_five(gamesList1)
    print('')
    print(f"Time for insertion sort: {round((end - start) * 1000000000)} nanoseconds.")
    print(f"Time for quick sort: {round((endb - startb) * 1000000000)} nanoseconds.")

    #test binary search
    for i in range(3):
        print(f"Search number {i + 1}:")
        time_elapsed_a, time_elapsed_b = binary_search_test(gamesList1)
        print(f"Single search time: {round(time_elapsed_a)} nanoseconds.")
        print(f"Average search time: {round(time_elapsed_b)} nanoseconds.")
        print('')
    
    
    


#returns a random game name from the linked list
def get_random_game(gamesList):
    random_index = random.randint(0, gamesList.length - 1)
    current = gamesList.head
    for i in range(random_index):
        current = current.next
    return current.game.name

#print first five of game list
def print_first_five(gamesList):
    current = gamesList.head
    for i in range(5):
        if current is None:
            break
        ID = current.game.ID
        name = current.game.name
        avgUserRating = current.game.avgUserRating
        userRatingCount = current.game.userRatingCount
        developer = current.game.developer
        size = current.game.size
        print(f"{ID}, {name}, {avgUserRating}, {userRatingCount}, {developer}, {size}")
        current = current.next

#master function for linear search test. allows calling the whole test multiple times easily
def linear_search_test(gamesList):
    #get random game
    name = get_random_game(gamesList)
    print("Searching for...", name)
    start = time.time() #start precise timer
    x = linearSearch(gamesList, name)
    end = time.time() #end precise timer
    #convert to nanoseconds
    time_elapsed_a = (end - start) * 1000000000
    #search 10 more times and get average
    time_elapsed_b = 0
    for i in range(10):
        start = time.time()
        x = linearSearch(gamesList, name)
        end = time.time()
        time_elapsed_b += (end - start) * 1000000000
    return time_elapsed_a, time_elapsed_b / 10

#master function for binary search test. allows calling the whole test multiple times easily
def binary_search_test(gamesList):
    #get random game
    name = get_random_game(gamesList)
    print("Searching for...", name)
    start = time.time() #start precise timer
    x = binarySearch(gamesList, name)
    end = time.time() #end precise timer
    #convert to nanoseconds
    time_elapsed_a = (end - start) * 1000000000
    #search 10 more times and get average
    time_elapsed_b = 0
    for i in range(10):
        start = time.time()
        x = binarySearch(gamesList, name)
        end = time.time()
        time_elapsed_b += (end - start) * 1000000000
    return time_elapsed_a, time_elapsed_b / 10

if __name__ == "__main__":
    main()

