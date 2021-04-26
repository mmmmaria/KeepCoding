import sms

mensaje = input('escribe tu mensaje: ')

salida = sms.traduce(mensaje)
#salida = sms.traduce(mensaje.upper())

print("{} es -{}-".format(mensaje,salida))