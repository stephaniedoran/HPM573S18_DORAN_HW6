import HW6 as pOne

print ("A casino owner who gets to play the game many times "
       "would be most interested in the confidence interval, "
       "as for the casino owner with a large number of "
       "observations, this would be a steady state simulation "
       "in which a confidence interval is most appropriate. "
       "The many observations allow the law of large numbers to "
       "apply and be used to make an inference about the expected "
       "values.")
print ("The 95% confidence interval for expected rewards is",
       pOne.trial.get_reward_CI(0.05),
       "When the game is played a large number of times, the true mean "
       "will fall within this range 95% of the time")


print ("A gambler who only plays the game 10 times would be most "
       "interested in a prediction interval. The gambler would "
       "not have enough observations to apply the law of large "
       "numbers in making an inference about the expected value, "
       "making this a transient state simulation,  "
       "and would be more interested in the probable distribution of X "
       "to make an estimate about what might happen in the next "
       "trial.")
print("The 95% projection interval for expected rewards is",
      pOne.gamblertrial.get_reward_PI(0.05),
      "The next realization of the expected reward will fall in this "
      "projection interval with the probability 0.95")
