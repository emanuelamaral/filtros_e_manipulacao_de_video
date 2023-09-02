import cv2

imagem_capturada = None


def capturar_cor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cor_pixel = imagem_capturada[y, x]
        print(f"Cor no ponto ({x}, {y}): {cor_pixel}")


def rodar_video():
    global imagem_capturada

    video = cv2.VideoCapture("sunset.mp4")
    cv2.namedWindow('Video', 1)

    tecla = 0

    while tecla != 27:
        ret, frame_video = video.read()

        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        cv2.imshow("Video", frame_video)
        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('c'):
            imagem_capturada = frame_video.copy()
            cv2.imshow("Imagem Capturada", imagem_capturada)

            # Configurar o evento de clique do mouse para a imagem capturada
            cv2.setMouseCallback("Imagem Capturada", capturar_cor)

            while True:
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    rodar_video()
