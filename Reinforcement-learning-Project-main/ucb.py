import numpy as np
from base import Agent, MultiArmedBandit
import matplotlib.pyplot as plt


class UCBAgent(Agent):
    # Add fields 
    reward_memory=np.array
    count_memory=np.array
    def __init__(self, time_horizon, bandit:MultiArmedBandit): 
        # Add fields
        super().__init__(time_horizon, bandit)
        self.bandit: MultiArmedBandit =bandit
        self.reward_memory=np.zeros(len(bandit.arms))
        self.count_memory=np.zeros(len(bandit.arms))
        self.time_count=0
    def give_pull(self):
        with np.errstate(divide='ignore', invalid='ignore'):
            p_hat = np.divide(
                self.reward_memory,
                self.count_memory,
                out=np.zeros_like(self.reward_memory),
                where=self.count_memory != 0
            )
            exploration_terms = np.sqrt((2 * np.log(max(self.time_count, 1))) / self.count_memory)
            exploration_terms[self.count_memory == 0] = np.inf
            ucb = p_hat + exploration_terms

        arm = np.argmax(ucb)
        reward=self.bandit.pull(arm)
        self.reinforce(reward,arm) 
        

    def reinforce(self, reward, arm):
        self.time_count+=1
        self.count_memory[arm]+=1
        self.reward_memory[arm]+=reward
        self.rewards.append(reward)
        
 
    def plot_arm_graph(self):
        counts = self.count_memory
        indices = np.arange(len(counts))

        # Plot the data
        plt.figure(figsize=(12, 6))
        plt.bar(indices, counts, color='skyblue', edgecolor='black')

        # Formatting
        plt.title('Counts per Category', fontsize=16)
        plt.xlabel('Arm', fontsize=14)
        plt.ylabel('Pull Count', fontsize=14)
        plt.grid(axis='y', linestyle='-')  # Add grid lines for the y-axis
        plt.xticks(indices, [f'Category {i+1}' for i in indices], rotation=45, ha='right')
        # plt.yticks(np.arange(0, max(counts) + 2, step=2))

        # Annotate the bars with the count values
        for i, count in enumerate(counts):
            plt.text(i, count + 0.5, str(count), ha='center', va='bottom', fontsize=12, color='black')

        # Tight layout to ensure there's no clipping of labels
        plt.tight_layout()

        # Show plot
        plt.show()
    


# Code to test
if __name__ == "__main__":
    # Init Bandit
    TIME_HORIZON = 10_000
    bandit = MultiArmedBandit(np.array([0.23,0.55,0.76,0.44]))
    agent = UCBAgent(TIME_HORIZON,bandit) ## Fill with correct constructor

    
    # Loop
    for i in range(TIME_HORIZON):
        agent.give_pull()

    # Plot curves
    agent.plot_reward_vs_time_curve()
    agent.plot_arm_graph()
    bandit.plot_cumulative_regret()