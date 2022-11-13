import matplotlib.pyplot as plt
import numpy as np

nb_games = [10,100,1000,10000]
N = 10

win1 = [[80,   65,  62.1,  63,72],
 [60,   60,   64,8 , 63.75],
 [80,   59,   64.6 ,63.79],
 [60,   54,   65.7,  64.03],
 [80,   68,   64.2,  64.65],
 [40,   62,   65.6,  64.03],
 [30,   62,   61.7,  63.58],
 [80,   66,   62.1,  63.93],
 [40,   65,   66.1,  64.13],
 [60,   63,   63.9,  63.72]]
win1_mean = [61,    62.4,   64.08,  63.933]

draw = [[ 0. ,   2.  ,  2.2  , 2.01],
 [ 0.  ,  5.   , 2.   , 1.79],
 [ 0. ,   0.  ,  1.7 ,  1.78],
 [10. ,   2.  ,  1.8 ,  1.56],
 [ 0. ,   1.   , 0.9 ,  2.02],
 [ 0. ,   2.  ,  2.2  , 1.71],
 [ 0. ,   2. ,   2.   , 1.67],
 [ 0.   , 4.  ,  2.3  , 1.66],
 [ 0.   , 2.  ,  1.8 ,  1.8 ],
 [10.  ,  2.  ,  2.3 ,  1.62]]
draw_mean = [2.,    2.2,   1.92,  1.762]

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
plt.show()

plt.savefig('MCplot.png', format='png')