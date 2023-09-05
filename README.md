# Manipulação de Imagem/Video com Python OpenCV

Este é um projeto que utiliza a biblioteca OpenCV em Python para manipulação de imagens e vídeos. Neste trabalho, irei demonstrar como realizar a captura de uma imagem de um vídeo, apresentar a cor quando o mouse for clicado na imagem original, criar duas trackbars que disparam dois filtros passa-baixa em uma das bandas da imagem convertida, aplicar um filtro passa-alta, binarizar a imagem e, por fim, apresentar a imagem resultante.

# Sobre o trabalho:
- Disciplina: OP63I-CC8 - Processamento de Imagens e Reconhecimento de Padrões
- Turma: 2023/2 - 8° Periodo
- Professor: Pedro Luiz de Paula Filho
## Pré-requisitos e Instalação no Linux

### Python (versão recomendada: 3.11 ou superior)

A maioria das distribuições Linux já vem com o Python instalado. Para verificar se o Python está instalado, abra o terminal e digite:

```bash
python3 --version
```

Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install python3
```

No Arch Linux:

```bash
sudo pacman -Sy python
```

### PyCharm (ou qualquer outra IDE de sua escolha)

Você pode baixar o PyCharm diretamente do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/) ou, se preferir, pode usar o gerenciador de pacotes da sua distribuição para instalar a versão Community:

#### Ubuntu/Debian:

```bash
sudo snap install pycharm-community --classic
```

#### Arch Linux:

```bash
sudo pacman -Sy pycharm-community
```

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes de pacotes Python:

```bash
pip install opencv-python
```

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

```bash
pip install numpy
```

---

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

```bash
pip install opencv-python
```

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

```bash
pip install numpy
```

## Executando o Projeto

1. Clone este repositório em seu sistema:

```bash
git clone https://github.com/seuusuario/python-opencv-trabalho.git
```

2. Abra o projeto no PyCharm (ou sua IDE preferida).

3. Execute o script `captura_imagem.py` para capturar uma imagem de um vídeo em execução. Este script abrirá uma janela de vídeo e você pode clicar em qualquer ponto da imagem para ver a cor correspondente.

4. Execute o script `filtro_passa_baixa.py` para aplicar dois filtros passa-baixa à imagem capturada. Duas trackbars permitirão ajustar os parâmetros desses filtros.

5. Execute o script `filtro_passa_alta.py` para aplicar um filtro passa-alta à imagem.

6. Execute o script `binarizacao.py` para binarizar a imagem resultante.

7. Os resultados finais serão exibidos em janelas separadas para cada etapa do processamento.

## Autores

- Amoz Emanuel

## Referências

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python.org](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
