import speech_recognition as sr
r = sr.Recognizer()
while True:
	with sr.Microphone(device_index=1) as source:
			print("Скажите что-нибудь..")
			audio = r.listen(source)

	query = r.recognize_google(audio, language ="ru-RU")
	print("Вы сказали: " + query.lower())
	voice = query.lower()
	print(voice)
