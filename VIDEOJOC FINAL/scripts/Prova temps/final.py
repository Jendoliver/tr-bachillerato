import temps1
import temps2
import bge
temps = tempsfin - tempsini
print(temps)

if temps < 5:
    bge.logic.endGame
else:
    bge.logic.restartGame