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