# NOTE this program will allow a user to select a graph and check invariants
import numpy as np
import graphStuff as gs

def main():
    graphNum = input('Select a graph to see adjacency matrix (1-9): ')
    G = np.loadtxt('graphs/graph{0}.txt'.format(graphNum), int)
    print(G, '\n')
    menuChoice = invariantList()
    print(displayInvariant(G, menuChoice))

def invariantList():
    print('1) Order of G')
    print('2) Size of G')
    print('3) Max Degree of G')
    print('4) Min Degree of G')
    print('5) Degree Sequence of G')
    return input('Choose an invariant from the list: ')

def displayInvariant(G, userInput):
    return {
        '1': gs.order(G),
        '2': gs.size(G),
        '3': gs.maxDegree(G),
        '4': gs.minDegree(G),
        '5': gs.degreeSequence(G)
            }[userInput]

main()
