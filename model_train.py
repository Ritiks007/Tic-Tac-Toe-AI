import pygame
import matplotlib.pyplot as plt
import numpy as np
import pickle
if __name__ =='__main__':
    from Gridlines import Grid
    grid = Grid()

class AI:
    
    def __init__(self,exp_rate = 0.2,number=2):
        self.exp_rate = exp_rate
        self.states = []
        self.lr = 0.2
        self.decay_gamma = 0.9
        self.states_values = {}
        self.number = number
        # self.load_policy(mode)

    def choose_action(self,board):
        positions = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == -1:
                    positions.append((i,j))
        if np.random.uniform(0,1) <= self.exp_rate:
            action = positions[np.random.choice(len(positions))]
        else:
            value_max = -999
            for x,y in positions:
                next_state = [row[:] for row in board]
                next_state[x][y] = self.number
                next_state_hash = get_hash(next_state)
                value = 0
                if self.states_values.get(next_state_hash) != None:
                    value = self.states_values.get(next_state_hash)
                if value >= value_max:
                    value_max = value
                    action = (x,y)
        return action

    def add_State(self,state):
        self.states.append(state)

    def feedReward(self, reward):
        for st in reversed(self.states):
            if self.states_values.get(st) is None:
                self.states_values[st] = 0
            self.states_values[st] += self.lr * (self.decay_gamma * reward - self.states_values[st])
            reward = self.states_values[st]
    
    def reset(self):
        self.states = []

    def save_policy(self,mode=3):
        f = open('q_table_'+str(mode)+'_player'+str(self.number),'wb')
        pickle.dump(self.states_values,f)
        f.close()

    def load_policy(self,mode=3):
        f = open('q_table_'+str(mode)+'_player'+str(self.number),'rb')
        self.states_values = pickle.load(f)
        f.close()

def get_hash(board):
    ans = sum(board,[])
    return ','.join(map(str,ans))

def update_state(action,turn):
    (x,y) = action
    grid.update(x,y,turn)

def giveReward(p1,p2,winner):
    if winner == 1:
        p1.feedReward(1)
        p2.feedReward(0)
    elif winner == 2:
        p1.feedReward(0)
        p2.feedReward(1)
    else:
        p1.feedReward(0.1)
        p2.feedReward(0.5)

def train(mode,rounds=10000):
    p1 = AI(0.2,1)
    p2 = AI(0.2,2)
    win_1 = np.zeros(rounds//1000)
    win_2 = np.zeros(rounds//1000)
    draw = np.zeros(rounds//1000)
    wins_1 = 0
    wins_2 = 0
    draws = 0
    for i in range(rounds):
        if i%1000 == 0:
            print("Episode {}: {}".format(i//1000,p1.exp_rate))
            win_1[i//1000] = wins_1
            win_2[i//1000] = wins_2
            draw[i//1000] = draws
            wins_1 = 0
            wins_2 = 0
            draws = 0
        winner = 0
        turn = 0
        while winner == 0:
            if turn == 0:
                action = p1.choose_action(grid.CheckGrid)
                update_state(action,turn)
                p1.add_State(get_hash(grid.CheckGrid))

            else:
                action = p2.choose_action(grid.CheckGrid)
                update_state(action,turn)
                p2.add_State(get_hash(grid.CheckGrid))
            (x,y) = action

            winner = grid.checkwin(x,y,turn)
            if winner == 1:
                wins_1 +=1
            elif winner == 2:
                wins_2 +=1
            elif winner == 3:
                draws +=1
            turn = 1 - turn
        giveReward(p1,p2,winner)
        p1.reset()
        p2.reset()
        grid.reset()
    p1.save_policy(mode)
    p2.save_policy(mode)
    episodes = np.arange(0,rounds//1000)
    plt.plot(episodes,win_1,'r^',episodes,win_2,'bs',episodes,draw,'g--')
    plt.show()

# To train a new model, change the mode 
# and also change N and win_condition in params.py else there will be errors
if __name__ =='__main__':
    episodes = 50
    mode = 3
    train(mode,episodes*1000)