import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def envio_notificacion(moneda: str, precio: int, cantidades: int):

   # Iniciamos los parámetros del script
   remitente = 'ymc20250@gmail.com'
   destinatarios = ['yonihermelendez@gmail.com']
   asunto = f'Es hora de vender {moneda}'
   cuerpo = f'Hola Yoniher! Es hora de vender {moneda}, tiene un precio actual de: {precio}. La venta seria de: {cantidades} modenas.'

   # Creamos el objeto mensaje
   mensaje = MIMEMultipart()
   
   # Establecemos los atributos del mensaje
   mensaje['From'] = remitente
   mensaje['To'] = ", ".join(destinatarios)
   mensaje['Subject'] = asunto
   
   # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
   mensaje.attach(MIMEText(cuerpo, 'plain'))

   # Creamos la conexión con el servidor
   sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
   
   # Ciframos la conexión
   sesion_smtp.starttls()

   # Iniciamos sesión en el servidor
   sesion_smtp.login('ymc2050@gmail.com','glnu omau rkcq tbca')  

   # Convertimos el objeto mensaje a texto
   texto = mensaje.as_string()

   # Enviamos el mensaje
   sesion_smtp.sendmail(remitente, destinatarios, texto)

   # Cerramos la conexión
   sesion_smtp.quit()