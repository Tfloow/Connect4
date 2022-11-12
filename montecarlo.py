import numpy as np
import matplotlib.pyplot as plt
import connect4
import time

t = time.time()

N = 10 # Nb repetitions
nb_games = [10, 100, 1000] # to be faster I skiped the 10 000 while testing
# Array with the percentage of success for player 1 for [10, 100, 1000, 10000] games, N times each
win1 = np.zeros((N, len(nb_games)))
# Array with the percentage of draws for player 1 for [10, 100, 1000, 10000] games, N times each
draw = np.zeros((N, len(nb_games)))

##################################
### START : To do for students ###
##################################

# To do : fill in arrays win1 and draw
# In order to do so, simulate games with the function connect4.run_game()
index =  -1

for num in nb_games:
    start = time.time()
    index += 1
    for rep in range(N):
        print(rep, index)
        for _ in range(num):
            result = connect4.run_game()
            if result == 0:
                draw[rep][index] += 1
            elif result == 1:
                win1[rep][index] += 1
        draw[rep][index]/= num
        win1[rep][index]/= num
    print(num)
    print(time.time()-start)
win1 *= 100
draw *= 100

print("____")
print(draw, win1)
print("___")

################################
### END : To do for students ###
################################

# Computes and prints de mean for each [10, 100, 1000, 10000]
win1_mean = np.mean(win1, axis=0)
draw_mean = np.mean(draw, axis=0)
print(win1_mean)
print(draw_mean)

# Plot the results in the required format.
# Please do not modify
plt.figure()
for i in range(len(nb_games)):
    plt.scatter(np.full(N, nb_games[i]), win1[:,i], c = 'blue', s = 10)
    plt.scatter(np.full(N, nb_games[i]), draw[:,i], c = 'red', s = 10)
    plt.scatter(nb_games[i], win1_mean[i], c = 'blue', marker = 'x', s = 50)
    plt.scatter(nb_games[i], draw_mean[i], c = 'red', marker = 'x', s = 50)
plt.legend(['Victoire joueur 1', 'Ex-aequo', 'Moyenne victoire joueur 1', 'Moyenne ex-aequo'])
plt.xlabel('Nombre de parties')
plt.ylabel('Probabilite en %')
plt.xscale("log")
plt.ylim((-10,100))
# plt.show()

elapsed = time.time() - t
print('Elapsed time: ', elapsed)

plt.savefig('MCplot.png', format='png')

""""[[10.    7.    4.9   5.39]
 [10.    2.    5.7   4.98]
 [10.    4.    4.5   5.44]
 [ 0.    8.    3.9   5.33]
 [10.    6.    4.7   5.09]
 [10.    5.    6.6   5.2 ]
 [20.    4.    5.1   4.87]
 [ 0.    8.    6.6   5.44]
 [ 0.    3.    3.9   5.53]
 [ 0.    3.    6.    5.57]] [[50.   41.   50.1  49.74]
 [40.   63.   47.5  50.61]
 [30.   44.   50.8  50.01]
 [60.   45.   50.9  49.78]
 [30.   55.   50.3  50.69]
 [50.   48.   50.2  50.8 ]
 [30.   57.   49.8  50.76]
 [40.   46.   47.5  49.28]
 [60.   49.   51.9  49.8 ]
 [50.   50.   48.4  49.87]]
___
[44.    49.8   49.74  50.134]
[7.    5.    5.19  5.284]
Elapsed time:  1261.640570640564"""
