# Stock Trading Bot Using Deep Reinforcement Learning 📈

## Overview

This project pioneers the development of an intelligent Stock Trading Bot utilizing Deep Q-Learning, a sophisticated Deep Reinforcement Learning approach. The implementation adheres to the principles outlined in key research papers, providing an insightful journey into the application of these advanced techniques in the dynamic world of stock trading.

## Introduction

Reinforcement Learning (RL) is an innovative machine learning domain where agents learn optimal actions through trial and error, interacting with an environment. This is particularly useful in complex real-world applications like stock trading, where conventional supervised learning might falter due to the intricacies of the task or the lack of adequately labeled data.

## Methodology

Employing Deep Q-Learning, a model-free RL technique, this project has made notable strides:

- Vanilla Deep Q-Network (DQN)
- DQN with Fixed Target Distribution
- Double DQN

The agent assesses its environment (stock market) and decides on actions (buy, sell, hold) based on the current state, represented by the n-day window stock price, modifying its strategy according to the rewards received.

## Exciting Enhancements! 🚀

The trading bot has now evolved to integrate critical market influencers:

- **Senator Trades Analysis**: Keeping an eye on the investment patterns of influential market players.
- **Insider Trades Tracking**: Leveraging insider trading data for a more informed trading strategy.
- **News Sentiment Analysis**: Currently in development, this feature aims to analyze news related to specific companies using sentiment analysis transformers, adding a layer of qualitative data assessment.
- **Inflation Data Integration**: Incorporating economic indicators like inflation to refine the accuracy of trading decisions.

## Results

Originally trained and tested on Google's 2010-2017 stock data, the bot demonstrated promising results. Future enhancements aim to elevate its market prediction capabilities further.

## Some Considerations

- The bot currently operates on a single-stock transaction basis for simplicity.
- The feature representation includes a normalized vector of Adjusted Closing price differences.
- CPU-based training is recommended due to the sequential nature of the task.

## Data Sources

Leverage Historical Financial data from [Yahoo! Finance](https://ca.finance.yahoo.com/) or explore pre-included sample datasets under `data/`.

## Getting Started 🌟

To embark on this journey, install the required Python packages:

```bash
pip3 install -r requirements.txt
```

Now you can open up a terminal and start training the agent:

```bash
python3 train.py data/GOOG.csv data/GOOG_2018.csv --strategy t-dqn
```

Once you're done training, run the evaluation script and let the agent make trading decisions:

```bash
python3 eval.py data/GOOG_2019.csv --model-name model_GOOG_50 --debug
```

Now you are all set up!

