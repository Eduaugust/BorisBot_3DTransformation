# Alunos envolvidos
- [149349] [Pedro Edom Nunes]
- [149382] [Eduardo Augusto Duarte Evangelista]
- [137913] [Bryan Umpierre Moreira]

# BorisBot_3DTransformation

Este repositório contém o projeto chamado BorisBot_3DTransformation, que implementa transformações 3D em OpenGL, a fim de gerar uma representação
que lembre as formas presentes no robo Doris da equipe de robótica FBOT.

## Descrição

O objetivo deste projeto é demonstrar como realizar transformações 3D utilizando OpenGL, fazendo com que o aluno tenho maior contato prático com aluno
parte de computação gráfica da adisciplina de sistemasa gráficos. O projeto foi desenvolvido em Python e utiliza a biblioteca PyOpenGL, para tornar a 
adaptação dos alunos mais fácil.

## Funcionalidades
No arquivo reimplementation.py, você encontrará as seguintes funcionalidades:
- Transformações de rotação em torno dos eixos X, Y e Z.
- Transformações de translação nos eixos X, Y e Z.
- Transformações de escala nos eixos X, Y e Z.

Este arquivo contém a reimplementação de algumas funções de transformação 3D, que já existem na biblioteca. As funções reimplementadas são:

glTranslatef(x, y, z): Esta função cria uma matriz de translação e a multiplica pela matriz de modelagem atual.
glScalef(sx, sy, sz): Esta função cria uma matriz de escala e a multiplica pela matriz de modelagem atual.
glRotatef(angle, x, y, z): Esta função cria uma matriz de rotação com base em um ângulo e um vetor de eixo, e a multiplica pela matriz de modelagem atual.
glFrustum(left, right, bottom, top, near, far): Esta função cria uma matriz de projeção ortográfica e a multiplica pela matriz atual.
glOrtho(left, right, bottom, top, near, far): Esta função cria uma matriz de projeção ortográfica e a multiplica pela matriz atual.


No arquivo utils.py, são definidas várias funções para desenhar formas geométricas em um ambiente gráfico 3D usando a biblioteca OpenGL. As funções incluem:
drawRectangle: Desenha um retângulo usando cubos menores.
drawRectanglePoints: Desenha um retângulo usando pontos.
drawOctagon: Desenha um octógono usando retângulos.
keyboard: Manipula eventos de teclado para controlar a posição da câmera.

Além disso, o código define variáveis globais para controlar a posição da câmera e um loop que anima a cena.

Os demais arquivos utilizam as funções definidas nos arquivos reimplementation.py e utils.py para criar as diferentes partes do robo: Braço, Base e Corpo.
Foi feita a separação de cada parte do robo em um arquivo diferente para facilitar a visualização e compreensão do código.
## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.8
- Biblioteca PyOpenGL 
- Biblioteca Numpy

## Como usar

1. Clone este repositório em sua máquina local.
2. Instale as dependências necessárias
3. Execute o arquivo main.py para ver as transformações 3D em ação.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
