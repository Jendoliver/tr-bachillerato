from bge import logic as GL
import puntuacio
import correctes2 as a
action = own.actuators['porta2']
cont = GL.getCurrentController()
sensor = cont.sensors['Mouse2']


if sensor.positive and a == 0:
       seleccionat = sensor.hitObject
       if seleccionat.name == 'Solució_2-1a':
		a =+ 1
       elif seleccionat.name == 'Solució_2-2b':
		puntuacio.fails = puntuacio.fails + 1
       elif seleccionat.name == 'Solució_2-3':
		puntuacio.fails = puntuacio.fails + 1
       elif seleccionat.name == 'Solució_2-4':
		puntuacio.fails = puntuacio.fails + 1

if sensor.positive and a == 1:
	seleccionat = sensor.hitObject
	if seleccionat.name == 'Solució_2-1a':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
	elif seleccionat.name == 'Solució_2-2b':
		action.action = 'porta2'
		cont.activate(action)
	elif seleccionat.name == 'Solució_2-3':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
	elif seleccionat.name == 'Solució_2-4':
		puntuacio.fails = puntuacio.fails + 1
		a = 0
		
