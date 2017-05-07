# NOTE this program will allow a user to select a graph and check invariants
import numpy as np
import graphStuff as gs
import zeroForce as zf

def main():
    # graphNum = input('Select a graph to see adjacency matrix (1-9): ')
    # G = np.loadtxt('graphs/graph{0}.txt'.format(graphNum), int)
    G = np.loadtxt('graphs/dodecahedron.txt', int)
    print(G, '\n')
    while 1 < 2:
        menuChoice = invariantList()
        print('OUTPUT:\n', displayInvariant(G, menuChoice))
        print('\n')

def invariantList():
    print('1) Order of G')
    print('2) Size of G')
    print('3) Max Degree of G')
    print('4) Min Degree of G')
    print('5) Degree Sequence of G')
    print('6) Closed Neighborhood of v2')
    print('7) Open Neighborhood of v2')
    print('8) Eccentricity of v2')
    print('9) Radius of G')
    print('10) Diameter of G')
    print('11) Resiude of G')
    print('12) Independence Number of G')
    print('13) Domination Number of G')
    print('14) Total Domination Number of G')
    print('15) Clique Number of G')
    print('16) Chromatic Number of G')
    print('17) Girth of G')
    print('18) Complement of G')
    print('19) Zero Forcing Number of G')
    print('20) Annihilation Number')
    print('21) Sub Total Annihilation')
    return input('Choose an invariant from the list: ')

def displayInvariant(G, userInput):
    return {
        '1': gs.order(G),
        '2': gs.size(G),
        '3': gs.maxDegree(G),
        '4': gs.minDegree(G),
        '5': gs.degreeSequence(G),
        '6': gs.closedNeighborhood(G, 2), 
        '7': gs.openNeighborhood(G, 2),
        '8': gs.eccentricity(G, 2),
        '9': gs.radius(G),
        '10': gs.diameter(G),
        '11': gs.residue(G),
        '12': gs.indyNumber(G),
        '13': gs.domNumber(G),
        '14': gs.totalDomNumber(G),
        '15': gs.cliqueNumber(G),
        '16': gs.chromatic(G),
        '17': gs.girth(G),
        '18': gs.complement(G),
        '19': zf.zeroForceNum(G),
        '20': zf.annihilationNum(G),
        '21': zf.subTotalDom(G)
            }[userInput]

main()
