import HW6 as P1

print("In a large number of trials, the true mean for the expected reward "
      "will fall within the range", P1.allGames.get_reward_CI(0.05), "95% of the time")

print("In a large number of trials, the true mean for the probability of loss "
      "will fall within the range", P1.allGames.get_probloss_CI(0.05), "95% of the time")
