from bge import logic as GL
import puntuacio
action = own.actuators['porta1']
cont = GL.getCurrentController()
sensor = cont.sensors['Mouse1']

if sensor.positive :
       seleccionat = sensor.hitObject
       if seleccionat.name == 'Solució_1-1a':
		action.action = 'porta1'
		cont.activate(action)
       elif seleccionat.name == 'Solució_1-2':
		puntuacio.fails = puntuacio.fails + 1
       elif seleccionat.name == 'Solució_1-3':
		puntuacio.fails = puntuacio.fails + 1
       elif seleccionat.name == 'Solució_1-4':
		puntuacio.fails = puntuacio.fails + 1

	
