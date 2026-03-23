import numpy as np
from base import Agent, MultiArmedBandit
import matplotlib.pyplot as plt


class ThompsonSamplingAgent(Agent):
    reward_memory=np.array
    count_memory=np.array
    success_mem=np.array
    fail_mem=np.array
    def __init__(self, time_horizon, bandit:MultiArmedBandit): 
        # Add fields
        super().__init__(time_horizon, bandit)
        self.bandit: MultiArmedBandit =bandit
        self.reward_memory=np.zeros(len(bandit.arms))
        self.count_memory=np.zeros(len(bandit.arms))
        self.time_count=0
        self.success_mem=np.zeros(len(bandit.arms))
        self.fail_mem=np.zeros(len(bandit.arms))
    def give_pull(self):
        thompson_sample=np.zeros(len(self.bandit.arms))
        for a in range(len(self.bandit.arms)):
            thompson_sample[a]=np.random.beta(self.success_mem[a]+1,self.fail_mem[a]+1)

        arm = np.argmax(thompson_sample)
        reward=self.bandit.pull(arm)
        self.reinforce(reward,arm) 
        

    def reinforce(self, reward, arm):
        self.time_count+=1
        self.count_memory[arm]+=1
        self.reward_memory[arm]+=reward
        self.rewards.append(reward) 
        if(reward==1):
            self.success_mem[arm]+=1
        else:
            self.fail_mem[arm]+=1
           

        
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
    agent = ThompsonSamplingAgent(TIME_HORIZON,bandit)

    # Loop
    for i in range(TIME_HORIZON):
        agent.give_pull()

    # Plot curves
    agent.plot_reward_vs_time_curve()
    agent.plot_arm_graph()
    bandit.plot_cumulative_regret()
