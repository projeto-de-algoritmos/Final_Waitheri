<!-- Adicionar Foto da logo aqui Deivid -->
# Waitheri

**Número da Lista**: X<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0026758 |  Deivid Alves de Carvalho  |
| 19/0030879 |  João Pedro Moura Oliveira |

## Sobre 
Descreva os objetivos do seu projeto e como ele funciona. 

## Screenshots

## Instalação 
**Linguagem**: python<br>
**Framework**: pyxel<br>

### Pré-requisitos
```
# Instalação do Pyxel
pip install pyxel

# Clonagem do repositório
git clone git@github.com:projeto-de-algoritmos/PD_O-ultimo-moedeiro.git

# Entre na pasta
cd PD_O-ultimo-moedeiro
```

## Uso 
- Após a instalação dos pré-requisitos é necessário rodar o seguinte comando:
```
python app.py
```

# Customização e Configuração
- Muitas funções do projeto Waitheri foram feitas pensando em possíveis customizações, por esse motivo o arquivo `utils.py` contem uma série de variáveis que podem ser alteradas de forma a alterar a geração, loja, probabilidades e dinâmicas do jogo.
- Dentro do próprio arquivo existem comentários que norteiam as configurações, porém algumas serão melhor explicadas nessa seção:

- [Não Recomendado] Por traz do jogo existe uma matriz que controla várias informações. O seu tamanho pode ser alterado pelas seguintes variáveis:
```python
COLUMS = 15
ROWS = 13
```

- Dentro da geração das salas pequenos quartos são pré-criados de maneira a dar forma ao quarto final. Seus tamanhos (largura e espessura) máximos e mínimos podem ser alterados pelas seguintes variáveis:
```python
MAX_WIDTH_ROOM = 2
MAX_HEIGHT_ROOM = 2
MIN_WIDTH_ROOM = 2
MIN_HEIGHT_ROOM = 2
```

- Ainda em relação a pré-criação dos quartos é possível alterar a quantidade de salas geradas através da seguinte variável
```python
QTD_ROOMS = 8
```

- [Recomendado] Na geração dos pesos de cada quarto, é possível setar diferentes valores. Para isso deve-se utilizar as variáveis abaixo seguindo o formato esperado: (porcentagem desejada, valor na matriz)
####ps.: Apenas as porcentagens de WALL e SPIKE devem ser alteradas, pois o cálculo é feito da seguinte forma: SPIKE <= valor, valor >= WALL > PER\_SPIKE e valor >= FLOOR > PER\_WALL.
```python
PER_FLOOR = (100, 1)
PER_WALL = (49, 2)
PER_SPIKE = (7, 3)
```

- [Recomendado] Ao quebrar uma caixa existe a probabilidade de ser dropada uma moeda. Esse valor é setado na seguinte variável:
```python
PER_COIN = 30
```


```python
```
