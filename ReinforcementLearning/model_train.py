"""
model_train.py
"""

import matplotlib.pyplot as plt
import numpy as np
import torch
from context_bandit import ContextBandit

print(torch.__version__)
print(torch.cuda.get_device_name(0))
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
print(f"device: {DEVICE}")


def build_model(device, arms=10):
    """build_model"""
    dim_in, hidden, dim_out = arms, 100, arms
    model = torch.nn.Sequential(
        torch.nn.Linear(dim_in, hidden),
        torch.nn.ReLU(),
        torch.nn.Linear(hidden, dim_out),
        torch.nn.ReLU(),
    )
    model.to(device)
    loss_fn = torch.nn.MSELoss()
    return model, loss_fn


def get_one_hot(dim, pos, val=1):
    """get_one_hot"""
    one_hot_vec = np.zeros(dim)
    one_hot_vec[pos] = val
    return one_hot_vec


def softmax(x, tau=1.12):
    """softmax"""
    softm = np.exp(x / tau) / np.sum(np.exp(x / tau))
    return softm


def train(device, model, loss_fn, arms, env):  # pylint: disable=too-many-locals
    """train"""
    epochs = 5000
    learning_rate = 1e-2
    cur_state = torch.Tensor(get_one_hot(arms, env.get_state())).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    rewards = []
    for i in range(epochs):
        y_pred = model(cur_state)
        av_softmax = softmax(y_pred.data.cpu().numpy(), tau=2.0)
        av_softmax /= np.sum(av_softmax)
        choice = np.random.choice(arms, p=av_softmax)
        cur_reward = env.choose_arm(choice)
        one_hot_reward = y_pred.data.cpu().numpy().copy()
        one_hot_reward[choice] = cur_reward
        reward = torch.Tensor(one_hot_reward).to(device)
        rewards.append(cur_reward)
        loss = loss_fn(reward, y_pred)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        cur_state = torch.Tensor(get_one_hot(arms, env.get_state())).to(device)
        if i % 100 == 0:
            print(f"epoch: {i}, loss: {loss.item()}")
    return np.array(rewards)


def running_mean(x, num=50):
    """running_mean"""
    length = x.shape[0] - num
    y = np.zeros(length)
    conv = np.ones(num)
    for i in range(length):
        y[i] = (x[i : i + num] @ conv) / num
    return y


def main(device):
    """main"""
    arms = 10
    env = ContextBandit(bandits=arms)
    model, loss_fn = build_model(device, arms)
    rewards = train(device, model, loss_fn, arms, env)
    plt.plot(running_mean(rewards, num=500))
    plt.show()


if __name__ == "__main__":
    main(DEVICE)
    print("done")
