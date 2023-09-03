import cv2
import numpy as np

imagem_capturada = None
brilho_atual = 0  # Define o valor inicial do brilho
sigma_atual = 0  # Define o valor inicial do Sigma
kernel_size_atual = 1  # Define o valor inicial do kernel como sendo 1
limiar_inferior_canny = 50  # Define o valor do threshold1 em 50
limiar_superior_canny = 150  # Define o valor do threshold2 em 150


def capturar_cor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cor_pixel = imagem_capturada[y, x]
        print(f"Cor no ponto ({x}, {y}): {cor_pixel}")


def aplicar_filtros(valor):
    global imagem_capturada
    global brilho_atual
    global sigma_atual

    # Divide o canal de cores em 3 (B, G, R)
    canais_de_cor = cv2.split(imagem_capturada)

    brilho_atual = valor

    # Aplica o filtro Gaussian Blur com sigma_atual no canal de cor 0
    imagem_gaussian = cv2.GaussianBlur(canais_de_cor[0], (5, 5), sigma_atual)

    # Aplica o filtro Median Blur com kernel_size_atual no canal de cor 0
    imagem_median = cv2.medianBlur(canais_de_cor[0], kernel_size_atual)

    imagem_resultante = cv2.addWeighted(imagem_gaussian, 0.7, imagem_median, 0.3, 0)
    imagem_modificada = cv2.add(imagem_resultante, np.ones_like(canais_de_cor[0]) * brilho_atual)

    cv2.imshow("Imagem Capturada", imagem_modificada)


def gaussian_blur(valor):
    global sigma_atual
    sigma_atual = valor
    aplicar_filtros(brilho_atual)


def median_blur(valor):
    global kernel_size_atual
    kernel_size_atual = valor if valor % 2 == 1 else valor + 1
    aplicar_filtros(brilho_atual)


def alterar_limiar_superior(valor):
    global limiar_superior_canny
    limiar_superior_canny = valor
    atualizar_filtro_canny()


def alterar_limiar_inferior(valor):
    global limiar_inferior_canny
    limiar_inferior_canny = valor
    atualizar_filtro_canny()


def atualizar_filtro_canny():
    edges = cv2.Canny(imagem_capturada, limiar_inferior_canny, limiar_superior_canny, apertureSize=3, L2gradient=False)
    cv2.imshow("Imagem Capturada", edges)


def processa_frame(imagem):
    cv2.imshow("Imagem Capturada", imagem)
    cv2.imwrite("captura_do_frame.png", imagem)

    # Configurar o evento de clique do mouse para a imagem capturada
    cv2.setMouseCallback("Imagem Capturada", capturar_cor)

    # Cria uma trackbar para ajustar o Sigma na imagem captura e aplicar o filtro Gaussian Blur
    cv2.createTrackbar("Sigma", "Imagem Capturada", sigma_atual, 50, gaussian_blur)

    # Cria um trackbar para ajusatar o valor do kernel size do filtro Median Blur
    cv2.createTrackbar("Kernel Size", "Imagem Capturada", kernel_size_atual, 50, median_blur)

    # Cria dois trackbars: um para threshold1 (lower) e o outro para threshold2 (upper)
    cv2.createTrackbar("Limiar Inferior Canny", "Imagem Capturada", limiar_inferior_canny, 255, alterar_limiar_inferior)
    cv2.createTrackbar("Limiar Superior Canny", "Imagem Capturada", limiar_superior_canny, 255, alterar_limiar_superior)


def rodar_video():
    global imagem_capturada

    video = cv2.VideoCapture("sunset.mp4")
    cv2.namedWindow('Video', 1)

    tecla = 0

    # Deixa o video em um loop infinito até a tecla 'ESC' ser pressionada

    while tecla != 27:
        ret, frame_video = video.read()

        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        cv2.imshow("Video", frame_video)
        tecla = cv2.waitKey(1) & 0xFF

        # Ao pressionar a tecla 'c' é feito uma captura do video e salvando o frame em um arquivo .png

        if tecla == ord('c'):
            imagem_capturada = frame_video.copy()
            processa_frame(imagem_capturada)

            # Pausa o video de fundo até a tecla 'q' ser pressionada
            #
            # while True:
            #     key = cv2.waitKey(1) & 0xFF
            #     if key == ord('q'):
            #         break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    rodar_video()
