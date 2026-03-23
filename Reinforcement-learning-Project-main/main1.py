import numpy as np
import matplotlib.pyplot as plt

# Import your classes (assuming your code is saved in base.py)
from base import  Agent,MultiArmedBandit

# Import your agent implementations (assuming they are in separate files)
from epsilon_greedy import EpsilonGreedyAgent
from ucb import UCBAgent
from klucb import KLUCBAgent
from thompson import ThompsonSamplingAgent

def run_agents_and_plot():
    TIME_HORIZON = 30000
    arms = np.array([0.23, 0.55, 0.76, 0.44])

    # Initialize bandits for each agent separately
    bandit_eg = MultiArmedBandit(arms)
    bandit_ucb = MultiArmedBandit(arms)
    bandit_klucb = MultiArmedBandit(arms)
    bandit_ts = MultiArmedBandit(arms)

    # Initialize agents with your bandits
    agent_eg = EpsilonGreedyAgent(TIME_HORIZON, bandit_eg, epsilon=0.01)
    agent_ucb = UCBAgent(TIME_HORIZON, bandit_ucb)
    agent_klucb = KLUCBAgent(TIME_HORIZON, bandit_klucb, c=3)
    agent_ts = ThompsonSamplingAgent(TIME_HORIZON, bandit_ts)

    # Run simulation for all agents
    for _ in range(TIME_HORIZON):
        agent_eg.give_pull()
        agent_ucb.give_pull()
        agent_klucb.give_pull()
        agent_ts.give_pull()

    # Plot cumulative regret for all agents on one plot
    plt.figure(figsize=(10, 6))
    plt.plot(bandit_eg.cumulative_regret_array, label='Epsilon-Greedy')
    plt.plot(bandit_ucb.cumulative_regret_array, label='UCB')
    plt.plot(bandit_klucb.cumulative_regret_array, label='KL-UCB')
    plt.plot(bandit_ts.cumulative_regret_array, label='Thompson Sampling')
    plt.title('Cumulative Regret Over Time')
    plt.xlabel('Timesteps')
    plt.ylabel('Cumulative Regret')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot average reward over time for all agents on one plot
    plt.figure(figsize=(10, 6))
    timesteps = np.arange(1, TIME_HORIZON + 1)
    avg_rewards_eg = [np.mean(agent_eg.rewards[:t]) for t in timesteps]
    avg_rewards_ucb = [np.mean(agent_ucb.rewards[:t]) for t in timesteps]
    avg_rewards_klucb = [np.mean(agent_klucb.rewards[:t]) for t in timesteps]
    avg_rewards_ts = [np.mean(agent_ts.rewards[:t]) for t in timesteps]

    plt.plot(timesteps, avg_rewards_eg, label='Epsilon-Greedy')
    plt.plot(timesteps, avg_rewards_ucb, label='UCB')
    plt.plot(timesteps, avg_rewards_klucb, label='KL-UCB')
    plt.plot(timesteps, avg_rewards_ts, label='Thompson Sampling')

    plt.title('Average Reward Over Time')
    plt.xlabel('Timesteps')
    plt.ylabel('Average Reward')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bar chart: number of times each agent chose the optimal arm
    agents_names = ['Epsilon-Greedy', 'UCB', 'KL-UCB', 'Thompson Sampling']
    optimal_arm = np.argmax(arms)

    optimal_counts = [
        agent_eg.count_memory[optimal_arm],
        agent_ucb.count_memory[optimal_arm],
        agent_klucb.count_memory[optimal_arm],
        agent_ts.count_memory[optimal_arm]
    ]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(agents_names, optimal_counts, color=['blue', 'orange', 'green', 'red'])
    plt.title('Number of Times Each Agent Chose the Optimal Arm')
    plt.ylabel('Count')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 200, f'{int(height)}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()






def run_S2_experiment():
    TIME_HORIZON = 30000
    p_values = np.array([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9])
    final_regret_eg = []
    final_regret_ucb = []
    final_regret_klucb = []
    final_regret_ts = []

    for p in p_values:
        arms = np.array([p, p + 0.1])

        # Epsilon-Greedy
        bandit_eg = MultiArmedBandit(arms)
        agent_eg = EpsilonGreedyAgent(TIME_HORIZON, bandit_eg, epsilon=0.01)
        for _ in range(TIME_HORIZON):
            agent_eg.give_pull()
        final_regret_eg.append(bandit_eg.cumulative_regret_array[-1])

        # UCBs
        bandit_ucb = MultiArmedBandit(arms)
        agent_ucb = UCBAgent(TIME_HORIZON, bandit_ucb)
        for _ in range(TIME_HORIZON):
            agent_ucb.give_pull()
        final_regret_ucb.append(bandit_ucb.cumulative_regret_array[-1])

        # KL-UCB
        bandit_klucb = MultiArmedBandit(arms)
        agent_klucb = KLUCBAgent(TIME_HORIZON, bandit_klucb, c=3)
        for _ in range(TIME_HORIZON):
            agent_klucb.give_pull()
        final_regret_klucb.append(bandit_klucb.cumulative_regret_array[-1])

        # Thompson Sampling
        bandit_ts = MultiArmedBandit(arms)
        agent_ts = ThompsonSamplingAgent(TIME_HORIZON, bandit_ts)
        for _ in range(TIME_HORIZON):
            agent_ts.give_pull()
        final_regret_ts.append(bandit_ts.cumulative_regret_array[-1])

    # Plotting final regret vs p for all agents
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, final_regret_eg, marker='o', label='Epsilon-Greedy')
    plt.plot(p_values, final_regret_ucb, marker='s', label='UCB')
    plt.plot(p_values, final_regret_klucb, marker='^', label='KL-UCB')
    plt.plot(p_values, final_regret_ts, marker='d', label='Thompson Sampling')
    plt.xlabel('p (probability of lower arm)')
    plt.ylabel('Final Regret after {} steps'.format(TIME_HORIZON))
    plt.title('Final Regret vs p for Each Agent (S2)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    #run_agents_and_plot()
    run_S2_experiment()
