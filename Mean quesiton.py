import numpy as np

#Question 1
Screen_Time = np.array([220, 190, 260, 300, 180, 240, 270, 200, 250, 210, 230, 280])

#Question 2
mean = round(np.mean(Screen_Time))
print(f"\nThe mean of Screen time is: {mean}")

std_dev = round(np.std(Screen_Time))
print(f"\nThe stand deviation of Screen time is: {std_dev}")

#Question 3
above_240 = (np.sum(Screen_Time > 240))
print(f"\n the number of participants that more than 240 mins of screen time {above_240}")


#Question 4
lower_end = mean - std_dev
upper_end = mean + std_dev

# Count participants within one standard deviation of the mean
one_std_dev = np.sum((Screen_Time >= lower_end) & (Screen_Time <= upper_end))
print(f'\n one standard deviation of the mean {upper_end:.2f} & {lower_end:.2f}')
print(f' one standard deviation of the mean {one_std_dev}')


# 5. Count participants with screen time 20% above the mean
above_20_percent = mean * 1.2
count_20_percent = np.sum(Screen_Time > above_20_percent)
print(f"\n above the 20% mean: {above_20_percent:.2f} min")
print(f"The screen count above 20% above Mean: {count_20_percent}")