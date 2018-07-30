import random
from scipy.stats import bernoulli

# Coin A: P(H) = 0.3
# Coin B: P(H) = 0.5
# Coin C: P(H) = 0.9


class BayesCoin:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.weights = {'A': 0.3, 'B': 0.5, 'C': 0.9}
        self.coins = list(self.weights.keys())
        self.priors = {coin: 1 / 3 for coin in self.coins}
    # ------------------------------------------------------------ #

    def choose_coin(self):
        # sampling from a discrete uniform distribution
        self.coin = random.choice(self.coins)
    # ------------------------------------------------------------ #

    def flip_coin(self):
        # sampling from a discrete bernoulli distribution
        rv = bernoulli(self.weights[self.coin])
        return rv.rvs(1)[0]
    # ------------------------------------------------------------ #

    def update_priors(self, side):
        denominator = list(map(lambda coin: [1 - self.weights[coin], self.weights[coin]][side] * self.priors[coin], self.coins))
        self.priors = {self.coins[i]: numerator / sum(denominator) for i, numerator in enumerate(denominator)}
        self.debug(side, denominator)
    # ------------------------------------------------------------ #

    def debug(self, side, denominator):
        print('-' * 50)
        print('coin:', self.coin, 'side:', side)
        print('denominator:', denominator)
        print('priors:', self.priors)
        print('sum of priors:', sum(self.priors.values()))
        print('sum of denominator:', sum(denominator))
    # ------------------------------------------------------------ #
