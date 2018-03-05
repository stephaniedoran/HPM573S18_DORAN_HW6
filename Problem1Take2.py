import HW6 as HW6

print("The average expected reward is", HW6.allGames.get_mean_reward())
print ("The 95% confidence interval for expected rewards is", HW6.allGames.get_reward_CI(0.05))
print ("The 95% confidence interval for the probability of loss is", HW6.allGames.get_probloss_CI(0.05))
