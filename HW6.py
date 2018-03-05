import numpy as np
import scr.FigureSupport as figureLibrary
import scr.StatisticalClasses as Stat


class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        #self._rnd.seed(self._id)
        self._probHead = prob_head  # probability of flipping a head
        self._countWins = 0  # number of wins, set to 0 to begin

    def simulate(self, n_of_flips):

        count_tails = 0  # number of consecutive tails so far, set to 0 to begin

        # flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250


class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = [] # create an empty list where rewards will be stored
        self._probLoss = []

        # simulate the games
        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward
            self._gameRewards.append(game.get_reward())

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._gameRewards) / len(self._gameRewards)

    def get_reward_list(self):
        """ returns all the rewards from all game to later be used for creation of histogram """
        return self._gameRewards

    def get_max(self):
        """ returns maximum reward"""
        return max(self._gameRewards)

    def get_min(self):
        """ returns minimum reward"""
        return min(self._gameRewards)

    def get_probability_loss(self):
        """ returns the probability of a loss """
        count_loss = 0
        for value in self._gameRewards:
            if value < 0:
                count_loss += 1
        return float(count_loss) / len(self._gameRewards)

    def prob_loss_list(self):
        for value in self._gameRewards:
            if value < 0:
                self._probLoss.append(0)
            else: self._probLoss.append(1)
        return self._probLoss

    def get_loss_CI(self, alpha):
        sumStatLoss=Stat.SummaryStat("Prob Losses", self._probLoss)
        return sumStatLoss.get_t_CI(alpha)

    def get_reward_CI(self, alpha):
        sumStatReward=Stat.SummaryStat("Expected Reward", self._gameRewards)
        return sumStatReward.get_t_CI(alpha)

    def get_reward_PI(self, alpha):
        sumStatReward=Stat.SummaryStat("Expected Reward", self._gameRewards)
        return sumStatReward.get_PI(alpha)



class MultiSetofGames:
    def __init__(self, ids, n_games, prob_head):
        self._ids = ids
        self._nGames = n_games
        self.probHead = prob_head

        self._aveRewards = []
        self._probLosses = []
        self._sumStat_aveRewards = None
        self._sumStat_probLosses = None

        for i in range(40):
            gameA = SetOfGames(prob_head=self.probHead[i], n_games=self._nGames[i])
            self._aveRewards.append(gameA.get_ave_reward())
            self._probLosses.append(gameA.get_probability_loss())

    def get_reward_CI(self, alpha):
        sumStatReward=Stat.SummaryStat("Expected Reward", self._aveRewards)
        return sumStatReward.get_t_CI(alpha)

    def get_mean_reward(self):
        sumStatReward = Stat.SummaryStat("Expected Reward", self._aveRewards)
        return sumStatReward.get_mean()

    def get_reward_list(self):
        return self._aveRewards

    def get_probloss_CI(self, alpha):
        sumStatLoss=Stat.SummaryStat("Probability of Loss", self._probLosses)
        return sumStatLoss.get_t_CI(alpha)


# Calculate expected reward of 1000 games
trial = SetOfGames(prob_head=0.5, n_games=1000)
gamblertrial = SetOfGames(prob_head=0.5, n_games= 10)
allGames = MultiSetofGames(ids=range(40), n_games=[25]*40, prob_head=[0.5]*40)


# print("The average expected reward is:", trial.get_ave_reward())


# Create histogram of winnings
# figureLibrary.graph_histogram(
  #  observations=trial.get_reward_list(),
  #  title="Histogram of Rewards from 1000 Games",
  #  x_label="Game Rewards",
  #  y_label="Frequency")

# minimum reward is -$250 if {T, T, H} never occurs.
# maximum reward is $350 if {T, T, H} occurs 6 times (if you increase the number of games you might see this outcome).

# find minimum and maximum reward in trial
# print("In our trial, the maximum reward is:", trial.get_max())
# print("In our trial, the minimum reward is:", trial.get_min())

# Find the probability of a loss
#print("The probability of a single game yielding a loss is:", trial.get_probability_loss())

#print(allGames.simulate())
#print ("The 95% confidence interval for expected rewards is", allGames.get_reward_CI(0.05))
#print ("The 95% confidence interval for the probability of loss is", allGames.get_probloss_CI(0.05))
