# Q-Learning

## Introdução

Este programa implementa o algoritmo de **Q-Learning** para o aprendizado de políticas de decisão em ambientes de busca. Ele pode ser utilizado em três modos de operação e oferece a opção de imprimir estatísticas sobre o tempo de execução e a quantidade de atualizações realizadas na matriz \( Q \).

## Modos de Execução

O programa pode ser executado em três modos:

1. **Padrão** (`standard`):  
   Este modo realiza a busca utilizando Q-Learning com exploração e atualização padrão. O agente aprende a política determinística, de forma mais eficiente, sem introduzir aleatoriedade nas ações.

2. **Positivo** (`positive`):  
   Neste modo, o agente recebe apenas recompensas positivas ao tomar ações. Este modo tem como objetivo observar o impacto de um ambiente onde não há penalizações, o que pode resultar em um aprendizado ineficiente e mais demorado.

3. **Estocástico** (`stochastic`):  
   O agente recebe recompensas tanto positivas quanto negativas, o que permite uma exploração mais diversificada do ambiente. A aleatoriedade nas ações introduz incerteza, o que leva a uma busca mais exploratória e, geralmente, a um tempo de execução maior.

## Pré-requisitos

### Compilador necessário
- **Python 3.x**

### Instalando dependências

Use o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como Executar

Para executar o programa, utilize o seguinte comando no terminal:

```bash
python3 qlearning.py [filename] [mode] [xi] [yi] [iterations] [stats]
```

O programa requer no mínimo 6 parâmetros de entrada:

1. **Diretório do Mapa**: O arquivo de mapa a ser utilizado.
2. **Algoritmo**: O metódo do Q-Learning
    - **standar** (Padrão)
    - **positive** (Recompensas Positivas)
    - **stochastic** (Estocástico)

3. **Coordenada Inicial**: As coordenadas X e Y do ponto inicial.
4. **Coordenada Final**: As coordenadas X e Y do ponto final.
5. **stats(parametro opcional)**: Esse parametro indica que queremos as métricas do algoritimo

### Comportamento da Saída

1. **Sem o parâmetro `stats`:**  
   A saída será:
   - **Política de execução:** Uma matriz que representa as melhores decissõs que o agente pode tomar para alcançar o objetivo 

2. **Com o parâmetro `stats`:**  
   A saída será composta de:
   - **Política de execução:** Uma matriz que representa as melhores decissõs que o agente pode tomar para alcançar o objetivo 
   - **Tempo de Execução:** O tempo total de execução (em segundos, como um número flutuante).
   - **Quantidade de atualizações:** A quantidade total de atualizações feitas na matriz Q.