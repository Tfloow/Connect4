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