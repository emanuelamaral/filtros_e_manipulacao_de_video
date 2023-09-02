import cv2
import numpy as np

imagem_capturada = None
brilho_atual = 0  # Define o valor inicial do brilho
sigma_atual = 0  # Define o valor inicial do Sigma
kernel_size_atual = 1


def capturar_cor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cor_pixel = imagem_capturada[y, x]
        print(f"Cor no ponto ({x}, {y}): {cor_pixel}")


def aplicar_filtros(valor):
    global imagem_capturada
    global brilho_atual
    global sigma_atual

    brilho_atual = valor

    # Aplica o filtro Gaussian Blur com sigma_atual
    imagem_gaussian = cv2.GaussianBlur(imagem_capturada, (5, 5), sigma_atual)

    imagem_median = cv2.medianBlur(imagem_capturada, kernel_size_atual)

    imagem_resultante = cv2.addWeighted(imagem_gaussian, 0.7, imagem_median, 0.3, 0)
    imagem_modificada = cv2.add(imagem_resultante, np.ones_like(imagem_capturada) * brilho_atual)

    cv2.imshow("Imagem Capturada", imagem_modificada)


def gaussian_blur(valor):
    global sigma_atual

    sigma_atual = valor
    aplicar_filtros(brilho_atual)


def median_blur(valor):
    global kernel_size_atual

    kernel_size_atual = valor if valor % 2 == 1 else valor + 1
    aplicar_filtros(brilho_atual)


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

            # cv2.createTrackbar("Brilho", "Imagem Capturada", brilho_atual, 100, ajustar_brilho)

            # Cria uma trackbar para ajustar o Sigma na imagem captura e aplicar o filtro Gaussian Blur
            cv2.createTrackbar("Sigma", "Imagem Capturada", sigma_atual, 50, gaussian_blur)
            cv2.createTrackbar("Kernel Size", "Imagem Capturada", kernel_size_atual, 50, median_blur)

            while True:
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    rodar_video()
