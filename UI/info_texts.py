from UI.ANSI_terminal_operators import *


def explain_object_recognition(screen_width: int):
    title = "Reconhecimento de Objetos\n"
    explanation = r"""
    Reconhecimento de objetos, ou também reconhecimento de padrões,
    é uma área da visão computacional baseada em identificar e cla-
    ssificar um objeto dentro de uma imagem específica, ou de um
    frame em um vídeo.
    Essa ação é útil em diversos campos e já faz parte do nosso co-
    tidiano, por exemplo, ao mostrar nossos rostos em uma câmera
    para abrir o portão de um condomínio. Existem várias formas de
    se realizar esse processo, o OpenCV faz uso de técnicas como 
    os métodos-eigen, Hidden Markov Models (HMM).
    """
    steps_title = "Principais Etapas\n"
    steps = r"""
    1. Pré-processamento: Filtrar a imagem e remover ruídos.
    2. Extração de Características: Encontrar contornos, cores, etc.
    3. Classificação: Dadas as características, classificar o objeto.
    4. Pós-processamento: Refinar o resultado, não-máximos.
    """
    references_title = "Referências\n"
    references = r"""
    Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). Imagenet 
    classification with deep convolutional neural networks. In Advances
    in neural information processing systems (pp. 1097-1105).

    Simonyan, K., & Zisserman, A. (2014). Very deep convolutional 
    networks for large-scale image recognition. arXiv preprint arXiv:1409.1556.

    LIMA, João et al. Reconhecimento de Padrões em Tempo Real Utilizando a 
    Biblioteca OpenCV. 1. ed. Pernambuco, 2008. Disponível em:
    <https://www.gprt.ufpe.br/grvm/wp-content/uploads/Publication/Tutorials/
    2008/WRVA2008_ApostilaTutorialReconhecimentoPadroesTempoReal.pdf>. 
    """
    print(title)
    move_cursor_backward(screen_width)

    lines = explanation.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(steps_title)
    move_cursor_backward(screen_width)

    lines = steps.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(references_title)
    move_cursor_backward(screen_width)

    lines = references.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print ("[q] - quit")
    move_cursor_backward(screen_width)
    print("[m] - go back to menu")
    move_cursor_backward(screen_width)

def explain_object_tracking(screen_width: int):
    title = "Rastreamento de Objetos\n"
    explanation = r"""
    Rastreamento de objetos é uma técnica de visão computacional 
    em que seguimos a posição e o movimento de um ou vários objetos 
    ao longo de um ou vários vídeos. OpenCV constrói essa técnica 
    usando algoritmos como: Boosting, MIL, KCF, TLD, MedianFlow,
    GOTURN, MOSSE e CSRT. Essa técnica é importante em aplicações 
    como vigilância, análise de tráfego e atividades esportivas.
    """
    steps_title = "Principais Etapas\n"
    steps = r"""
    1. Detecção de Objetos: Objetos são identificados e localizados em imagens.
    2  Associação de Objetos: Formar a trajetória do objeto.
    3. Modelo de Movimento: Prever a posição do objeto.
    """
    references_title = "Referências\n"
    references = r"""
    BELO, Felipe; FERREIRA, Paulo. Visão computacional: rastreamento de objetos em movimento.
    2019. Disponível em: https://www.ufjf.br/lapav/files/2019/09/Vis%C3%A3o-Computacional-
    Rastreamento-de-Objetos-em-Movimento.pdf.

    YILMAZ, A.; JAVED, O.; SHAH, M. Object tracking: A survey. ACM Computing Surveys (CSUR),
    v. 38, n. 4, p. 1-45, 2006.
    BERG, T. L.; FORSYTH, D. A. Background subtraction in highly dynamic scenes. IEEE 
    Conference on Computer Vision and Pattern Recognition, 2000.

    SANTOS, Paulo; SILVA, Rodrigo. Rastreamento de objetos em vídeo usando aprendizado 
    profundo. 2021. Disponível em: https://www.researchgate.net/publication/342342323_Ras
    treamento_de_Objetos_em_Video_usando_Aprendizado_Profundo.
    """
    print(title)
    move_cursor_backward(screen_width)

    lines = explanation.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(steps_title)
    move_cursor_backward(screen_width)

    lines = steps.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(references_title)
    move_cursor_backward(screen_width)

    lines = references.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print ("[q] - quit")
    move_cursor_backward(screen_width)
    print("[m] - go back to menu")
    move_cursor_backward(screen_width)

def explain_object_reconstruction(screen_width: int):
    title = "Reconstrução 3D\n"
    explanation = r"""
    Reconstrução 3D é a técnica de transformar objetos reais em 
    modelos digitais tridimensionais, este processo pode ser feito
    de várias maneiras, uma delas é utilizando visão computacional. 
    OpenCV utiliza algoritmos como Algoritmo de Zhang, Block Matching e 
    Triangulação de Delaunay. Essa técnica é útil em diversas áreas, como 
    na modelagem de cenários para filmes, arqueologia, simulação, etc.
    """
    steps_title = "Principais Etapas\n"
    steps = r"""
    1. Calibração da Câmera: Calibrar parâmetros, como foco e orientação.
    2. Stereo Matching: Correspondência entre pixels de um objeto em diferentes perspectivas.
    3. Criação de Nuvens de Pontos: Mapeamento dos pontos da superfície do objeto.
    4. Triangulação: Converter pontos em malhas de superfícies.
    """
    references_title = "Referências\n"
    references = r"""
    CERONI, Alessandro. Introdução à visão computacional com OpenCV. 
    São Paulo: Novatec Editora, 2018.

    KAELBLI, G.; ZABIH, R. Computação visual: conceitos e aplicações.
    Porto Alegre: Bookman Editora, 2021.

    MA, Y.; SOATTO, S.; KOSECKA, J.; SASSELOV, S. An Invitation to 3-D Vision: 
    From Images to Geometric Models. New York: Springer, 2012.

    SARAGIH, J. M. Machine Learning for Vision-Based Motion Capture. 
    New York: Springer, 2011.

    ZISSERMAN, A.; HARTLEY, R. I. Multiple View Geometry in Computer Vision.
    Cambridge: Cambridge University Press, 2003.
    """
    print(title)
    move_cursor_backward(screen_width)

    lines = explanation.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(steps_title)
    move_cursor_backward(screen_width)

    lines = steps.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(references_title)
    move_cursor_backward(screen_width)

    lines = references.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print ("[q] - quit")
    move_cursor_backward(screen_width)
    print("[m] - go back to menu")
    move_cursor_backward(screen_width)

def explain_image_segmentation(screen_width: int):
    title = "Segmentação de Imagem\n"
    explanation = r"""
    A segmentação de imagem é a técnica de dividir uma imagem
    em diferentes regiões ou segmentos que compartilham características
    semelhantes, como cor, intensidade ou textura. Este processo é crucial 
    em diversas aplicações de visão computacional, como reconhecimento de 
    objetos, detecção de bordas e rastreamento de movimento. 
    O OpenCV oferece diversas ferramentas e algoritmos para segmentação 
    de imagem, como limiarização (thresholding), segmentação baseada em cor,
    e técnicas mais avançadas como o algoritmo de Watershed.
    """
    steps_title = "Principais Etapas\n"
    steps = r"""
    1. Pré-processamento: Aplicação de filtros para redução de ruído e suavização da imagem.
    2. Limiarização: Converter a imagem para escala de cinza ou aplicar um método de 
    limiarização, como a limiarização global ou adaptativa.
    3. Operações Morfológicas: Uso de operações como erosão e dilatação para refinar 
    os segmentos.
    4. Detecção de Contornos: Identificar os contornos dos objetos segmentados na imagem.
    5. Segmentação Avançada: Aplicação de algoritmos mais sofisticados, como Watershed, 
    para melhorar a segmentação.
    """
    references_title = "Referências\n"
    references = r"""
    MA, Y.; SOATTO, S.; KOSECKA, J.; SASSELOV, S. An Invitation to 3-D Vision: 
    From Images to Geometric Models. New York: Springer, 2012.

    SARAGIH, J. M. Machine Learning for Vision-Based Motion Capture. New York: 
    Springer, 2011.

    ZISSERMAN, A.; HARTLEY, R. I. Multiple View Geometry in Computer Vision. 
    Cambridge: Cambridge University Press, 2003.
    """
    print(title)
    move_cursor_backward(screen_width)

    lines = explanation.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(steps_title)
    move_cursor_backward(screen_width)

    lines = steps.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print(references_title)
    move_cursor_backward(screen_width)

    lines = references.split("\n")[1:]
    width = max([len(line) for line in lines])
    for line in lines:
        print(line)
        move_cursor_backward(width)

    print ("[q] - quit")
    move_cursor_backward(screen_width)
    print("[m] - go back to menu")
    move_cursor_backward(screen_width)
