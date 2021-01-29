import socket
import speech_recognition as sr
r = sr.Recognizer()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)

server.bind(
    ("127.0.0.2", 1234)
)

server.listen()

while True:
	user_socket, address = server.accept()
	with sr.Microphone(device_index=1) as source:
		print("Скажите что-нибудь")
		audio = r.listen(source)
	query = r.recognize_google(audio, language ="ru-RU")
	print("Вы сказали: " + query.lower())
	voice = query.lower()
	print(voice)
	user_socket.send(voice.encode("utf-8"))
