"""
context_bandit.py
"""
import random

import numpy as np


class ContextBandit:
    """ContextBandit"""

    def __init__(self, bandits=10):
        self.bandits = bandits
        self.init_distribution(bandits)
        self.update_state()

    def init_distribution(self, bandits):
        """init_distribution"""
        self.bandit_matrix = np.random.rand(bandits, bandits)

    def reward(self, prob):
        """reward"""
        reward = 0
        for _ in range(self.bandits):
            if random.random() < prob:
                reward += 1
        return reward

    def get_state(self):
        """get_state"""
        return self.state

    def update_state(self):
        """update_state"""
        self.state = np.random.randint(0, self.bandits)

    def get_reward(self, arm):
        """get_reward"""
        return self.reward(self.bandit_matrix[self.state][arm])

    def choose_arm(self, arm):
        """choose_arm"""
        reward = self.get_reward(arm)
        self.update_state()
        return reward


def main():
    """main"""
    env = ContextBandit(bandits=10)
    state = env.get_state()
    reward = env.choose_arm(1)
    print(f"state: {state}, reward: {reward}")


if __name__ == "__main__":
    main()
