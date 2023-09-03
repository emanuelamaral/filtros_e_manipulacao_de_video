import cv2
import numpy as np


class ProcessamentoDeVideo:
    def __init__(self, video_filename):
        self.video_filename = video_filename
        self.imagem_capturada = None
        self.brilho_atual = 0
        self.sigma_atual = 0
        self.kernel_size_atual = 1
        self.limiar_inferior_canny = 50
        self.limiar_superior_canny = 150

    def capturar_cor(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cor_pixel = self.imagem_capturada[y, x]
            print(f"Cor no ponto ({x}, {y}): {cor_pixel}")

    def aplicar_filtros(self, valor):
        # Divide o canal de cores em 3 (B, G, R)
        canais_de_cor = cv2.split(self.imagem_capturada)
        self.brilho_atual = valor

        # Aplica o filtro Gaussian Blur com sigma_atual no canal de cor 0
        imagem_gaussian = cv2.GaussianBlur(canais_de_cor[0], (5, 5), self.sigma_atual)

        # Aplica o filtro Median Blur com kernel_size_atual no canal de cor 0
        imagem_median = cv2.medianBlur(canais_de_cor[0], self.kernel_size_atual)
        imagem_resultante = cv2.addWeighted(imagem_gaussian, 0.7, imagem_median, 0.3, 0)
        imagem_modificada = cv2.add(imagem_resultante, np.ones_like(canais_de_cor[0]) * self.brilho_atual)

        cv2.imshow("Imagem Capturada", imagem_modificada)

    def gaussian_blur(self, valor):
        self.sigma_atual = valor
        self.aplicar_filtros(self.brilho_atual)

    def median_blur(self, valor):
        self.kernel_size_atual = valor if valor % 2 == 1 else valor + 1
        self.aplicar_filtros(self.brilho_atual)

    def alterar_limiar_superior(self, valor):
        self.limiar_superior_canny = valor
        self.atualizar_filtro_canny()

    def alterar_limiar_inferior(self, valor):
        self.limiar_inferior_canny = valor
        self.atualizar_filtro_canny()

    def atualizar_filtro_canny(self):
        edges = cv2.Canny(self.imagem_capturada, self.limiar_inferior_canny, self.limiar_superior_canny, apertureSize=3, L2gradient=False)
        cv2.imshow("Imagem Capturada", edges)

    def rodar_video(self):
        video = cv2.VideoCapture(self.video_filename)
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
                self.imagem_capturada = frame_video.copy()
                cv2.imshow("Imagem Capturada", self.imagem_capturada)
                cv2.imwrite("captura_do_frame.png", self.imagem_capturada)

                # Configurar o evento de clique do mouse para a imagem capturada
                cv2.setMouseCallback("Imagem Capturada", self.capturar_cor)

                # Cria uma trackbar para ajustar o Sigma na imagem captura e aplicar o filtro Gaussian
                cv2.createTrackbar("Sigma", "Imagem Capturada", self.sigma_atual, 50, self.gaussian_blur)

                # Cria um trackbar para ajusatar o valor do kernel size do filtro Median Blur
                cv2.createTrackbar("Kernel Size", "Imagem Capturada", self.kernel_size_atual, 50, self.median_blur)

                # Cria dois trackbars: um para threshold1 (lower) e o outro para threshold2 (upper)
                cv2.createTrackbar("Limiar Inferior Canny", "Imagem Capturada", self.limiar_inferior_canny, 255, self.alterar_limiar_inferior)
                cv2.createTrackbar("Limiar Superior Canny", "Imagem Capturada", self.limiar_superior_canny, 255, self.alterar_limiar_superior)

                # Pausa o video de fundo até a tecla 'q' ser pressionada

                #
                # while True:
                #     key = cv2.waitKey(1) & 0xFF
                #     if key == ord('q'):
                #         break

        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    processamento_video = ProcessamentoDeVideo("sunset.mp4")
    processamento_video.rodar_video()
