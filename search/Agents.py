from game import Agent, Directions
import random
import numpy as np

class DumbAgent(Agent):
    "An agent that goes WEST until it can't otherwise stand at the same di"
    def getAction(self, state):
        "The agent always goes WEST"
        "The agent receives a GameState (defined in pacman.py)."
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        print("State: ", state.getPacmanState())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP

class RandomAgent(Agent):
    "An agent that can go random with possible direction."
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        print ("Legal moves: ", legalActions)
        nextDir = legalActions[random.randint(0, len(legalActions) - 1)]
        if nextDir == 'Stop': print("Stopping")
        else: print("Go", nextDir)
        return nextDir

class BetterRandomAgent(Agent):
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        print ("Legal moves: ", legalActions)
        
        if 'Stop' in legalActions: legalActions.remove('Stop')
        nextDir = legalActions[random.randint(0, len(legalActions) - 1)]
        if nextDir == 'Stop': print("Stopping")
        else: print("Go", nextDir)
        return nextDir

class ReflexAgent(Agent):
    def getAction(self, state):
        print("Current location of Pacman: ", state.getPacmanPosition())
        legalActions = state.getLegalPacmanActions()
        print ("Legal moves: ", legalActions)
        if 'Stop' in legalActions: legalActions.remove('Stop')
        scores = [self.evaluationAction(state, action) for action in legalActions]
        bestscore = max(scores)
        print("Scores : ", scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestscore]
        chosenIndex = random.choice(bestIndices)  
        print("Go", legalActions[chosenIndex])
        return legalActions[chosenIndex]

    def evaluationAction(self, state, action):
        successorGameState = state.generatePacmanSuccessor(action)
        return successorGameState.getScore()