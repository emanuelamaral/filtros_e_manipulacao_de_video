# Manipulação de Imagem/Video com Python OpenCV

Este é um projeto que utiliza a biblioteca OpenCV em Python para manipulação de imagens e vídeos. Neste trabalho, irei demonstrar como realizar a captura de uma imagem de um vídeo, apresentar a cor quando o mouse for clicado na imagem original, criar trackbars que disparam dois filtros passa-baixa em uma das bandas da imagem convertida, aplicar um filtro passa-alta, binarizar a imagem e, por fim, apresentar a imagem resultante.

## Sobre o trabalho

- Disciplina: OP63I-CC8 - Processamento de Imagens e Reconhecimento de Padrões
- Turma: 2023/2 - 8° Período
- Professor: Pedro Luiz de Paula Filho

## Pré-requisitos e Instalação no Linux

### Python (versão recomendada: 3.11 ou superior)

A maioria das distribuições Linux já vem com o Python instalado. Para verificar se o Python está instalado, abra o terminal e digite:

`python3 --version`

Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu/Debian:

`
sudo apt-get update
sudo apt-get install python3
`

No Arch Linux:

`
sudo pacman -Sy python
`

### PyCharm (ou qualquer outra IDE de sua escolha)

Você pode baixar o PyCharm diretamente do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/) ou, se preferir, pode usar o gerenciador de pacotes da sua distribuição para instalar a versão Community:

#### Ubuntu/Debian:

`
sudo snap install pycharm-community --classic
`

#### Arch Linux:

`
sudo pacman -Sy pycharm-community
`

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes Python:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Pré-requisitos e Instalação no Windows

### Python (versão recomendada: 3.11 ou superior)

1. Baixe o instalador Python para Windows no site oficial (https://www.python.org/downloads/windows/).

2. Execute o instalador e marque a opção "Adicionar o Python X.Y ao PATH" durante a instalação, onde X.Y é a versão do Python (por exemplo, 3.11).

### PyCharm (ou qualquer outra IDE de sua escolha)

1. Baixe o instalador do PyCharm Community ou Professional do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/).

2. Execute o instalador e siga as instruções na tela.

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes de pacotes Python:

Abra o prompt de comando (cmd) e execute:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Executando o Projeto

1. Clone este repositório em seu sistema:

`
git clone https://github.com/seuusuario/python-opencv-trabalho.git
`

2. Abra o projeto no PyCharm (ou sua IDE preferida).

## Modo de Uso

1. **Captura de Imagem:** Pressione a tecla `c` para capturar uma imagem do vídeo. A imagem capturada será exibida em uma nova janela.

2. **Aplicação de Filtros:**

   - Utilize as trackbars para ajustar os filtros passa-baixa.
   - Para aplicar um filtro passa-alta, utilize os trackbars limiar superior e limiar inferior.
   - Para binarizar a imagem, o trackbar threshold.

3. **Mostrar Cores no Clique:**

   - Clique na imagem capturada e as cores no ponto clicado serão exibidas no console.

4. **Sair do Programa:** Pressione a tecla `Esc` para sair do programa.

## Autores

- Amoz Emanuel

## Referências

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python.org](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
```

Certifique-se de adaptar as instruções de uso para refletir a lógica específica do seu código, pois as funcionalidades de trackbars e detecção de cores no clique podem requerer uma implementação personalizada.
