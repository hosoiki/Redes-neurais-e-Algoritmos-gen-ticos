import random

def funcao_objetivo(individuo):
    '''Computa a função objetivo para o problema cb.
    
        Argumentos:
            Individuo: lista contendo os genes das caixas binárias
        
        Return:
            Um valor representando a soma dos genes do indivíduo
    '''
    return sum(individuo)
    # pass 

def gene_cb():
    '''Gera um gene válido para o problema das caixas binários, assim como visto no primeiro experimento
    
    Return:
        Ou retorna zero ou retona um
    '''
    lista = [0, 1] # lá no início dissemos que os genes poderiam assumir dois valores
    gene = random.choice(lista) # pedirei que a função escolha aleatóriamnte um valor para o gene dentro da lista
    return gene # peço que ele retorne a escolha aleatória
    #pass
    
def individuo_cb(n):
    '''Gera um indivíduo para o problema das caixas binárias (um indivíduo tem 4 genes)
    
    Argumentos:
        n: número de genes do indivíduo (ou seja, número de caixas)
        
    Return:
        Uma lista com n genes (caixas). Cada gene é um valor zero ou um.
    '''
    individuo = [] # importante lembrar: o indivíduo corresponde ao conjunto de 4 genes, ou seja, ele será uma lista desses 4 valores
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo
    #pass

    
def populacao_cb(tamanho, n):
    ''' cria uma população para o problema das caixas binárias
    
    Argumentos:
        tamanho: tamanho da população
        n: número de genes
    Returns:
        uma lista onde cada item é um indivíduo, sendo ele uma lista com n genes
    '''
    
    populacao = []
    for _ in range(tamanho): # o underline no python armazena o último comando que você fez (apenas um item) - é uma variável que já existe na natureza do python
        populacao.append(individuo_cb(n))
    return populacao


def selecao_roleta_max(populacao, fitness):
    ''' Seleciona indivíduos de uma população usando o método da roleta
    
    Nota: apenas funciona para problemas de maximização
    
    Argumentos:
        população: lista com todos os indivíduos da população
        fitness: lista com o valor da função objetivo dos indivíduos selecionados
    
    Returns:
        população dos indivíduos selecionados
    
    '''
    
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def funcao_objetivo_pop_cb(populacao):
    ''' Calcula a função objetivo para todos os membros de uma população
    
    Argumentos:
        população: lista com todos os indivíduos da população
    
    Returns:
        lista de valores representando a fitness de cada individuo da população
    '''
    
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo(individuo)
        fitness.append(fobj)
    return fitness

def cruzamento_ponto_simples(mae, pai):
    ''' operador de cruzamento de ponto simples
    
    Argumentos:
        mae: uma lista representando um individuo
        pai: uma lista representando um individuo
    
    Returns:
        duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    '''
    
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    cria1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    cria2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return cria1, cria2

def mutacao_cb(individuo):
    ''' Realiza a mutação de um gene no problema das caixas binárias
    
    Argumentos: 
        individuo: uma lista representando um individuo no problema das caixas binarias
        
    Return: 
        um individuo com um gene mutado
    '''
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo



###############################################################################
#           A partir daqui, faremos as funções utilizadas no exp. 4           #
###############################################################################



def gene_cnb(valor_max_caixa):
    ''' Gera um gene válido para o problema das caixas não-binárias
    
    Argumentos:
        valor_max_caixa: Valor máximo que a caixa pode assumir
        
    Return:
        um valor de 0 a 'valor_max_caixa' (incluso)
    '''
    
    gene = random.randint(0, valor_max_caixa)
    return gene

def individuo_cnb(numero_genes, valor_max_caixa):
    ''' Gera um indivíduo válido para o problema das caixas não-binárias
    
    Args:
        numero_genes: número de genes na lista que representa o indivíduo
        valor_max_caixa: Valor máximo que a caixa pode assumir
    
    Returns:
        Uma lista que representa um indivíduo para o problema das cas CNB
    '''
    
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    ''' Cria uma população de indivíduos para o problema das caixas não-binárias
    
    Args:
        tamanho_população: número de indivíduos da população
        numero_genes: numero de genes do indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        uma lista onde cada item representa um indivíduo
    '''
    
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao

def funcao_objetivo_cnb(individuo):
    ''' Calcula o fitness do indivíduo para o problema das caixas não-binárias
    
    Args:
        individuo: lista que representa um individuo dentro do problema das CNB
        
    Returns: 
        um valor que representa o fitness do individuo
    '''
    
    fitness = sum(individuo)
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    ''' Calcula o fitness da população completa
    
    Args: 
        populacao: lista com todos os individuos da população
        
    Returns:
        uma lista com o fitness de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop

def mutacao_cnb(individuo, valor_max_caixa):
    ''' Realiza a mutação do indivíduo
    
    Args: 
        individuo: individuo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        individuo que sofreu a mutação
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo



######################################################################################
#       A partir daqui, realizarei as funções a serem utilizadas no exp. 5           #
######################################################################################


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha

    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha

    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.

    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado



#######################################################################################
#                A partir deste ponto, colocarei as funções do exp. 6                 #
#######################################################################################



# Funções Suporte:

def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.

    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


#####################################################################################
# Funções "técnicas":



def individuo_cv(cidades):
    
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys()) #Retorna uma lista com o nome das cidades geradas
    random.shuffle(nomes) #Reorganiza a ordem das cidades de forma aleatória
    return nomes
    
    #pass

def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.

    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


def cruzamento_ordenado(pai, mae): 
    
    # Nesse caso, o cruzamento de ponto simples não funciona, pois não queremos que os genes repitam
    # Usaremos dois pontos de corte (podem ser nos limites da lista dessa vez) - Cruzamento ordenado
        # Para gerar os filhos, primeiramente os genes dentre os cortes são diretamente passados para os filhos, enquanto o restante dos genes serão completos com os genes ainda não existentes do outro pai.
    
    """Operador de cruzamento ordenado.

    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    # Estabelecendo os cortes
    corte1 = random.randint(0, len(pai) - 2)
    corte2 = random.randint(corte1 + 1, len(pai) - 1) # Se o segundo passo for baseado no primeiro, os dois nunca serão os mesmos
    
    filho1 = pai[corte1:corte2] # Pega os genes entre os cortes
    for gene in mae: #Para cada gene da mãe
        if gene not in filho1: # Se o gene ainda não estiver presente no filho
            filho1.append(gene) # Herda o gene
            
    filho2 = mae[corte1:corte2] # Pega os genes entre os cortes
    for gene in pai: #Para cada gene do pai
        if gene not in filho2: # Se o gene ainda não estiver presente no filho
            filho2.append(gene) # Herda o gene
            
    return filho1, filho2
    
    #pass


def mutacao_de_troca(individuo): #É um operador específico para esse problema, uma vez que uma mutação aleatória teria o risco de repetir uma cidade, tornando o individuo inválido
    """Troca o valor de dois genes.

    Args:
      individuo: uma lista representado um individuo.

    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    indice1 = lista_sorteada[0] # O índice é a posição do elemento na lista
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1] # Trocando dois valores sem precisar criar uma nova função
    
    return individuo

    #pass


def funcao_objetivo_cv(individuo, cidades):
    
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.

    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    
    for posicao in range(len(individuo) - 1):
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
        
    # Calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso

    return distancia


def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.

    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado