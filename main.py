import cv2


cap = cv2.VideoCapture('video.mkv')
car_cascade = cv2.CascadeClassifier('detecta_carro.xml')



while True:

	ret, img = cap.read()
	if (type(img) == type(None)):
		break
		
        img = cv2.resize(img,(0,0),None, .6,.6)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	cars = car_cascade.detectMultiScale(gray, 2, 4)

	for (x, y, w, h) in cars :
			if h > 30:
				cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2, cv2.LINE_AA)
				msg = "VEICULO DETECTADO"
				cv2.putText(img, msg, (x, y + h + 20 ), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255),2, cv2.LINE_AA)

	cv2.imshow('video', img)
	

	if cv2.waitKey(1) == ord('q'):
		break;

cv2.destroyAllWindows()
cap.release()
