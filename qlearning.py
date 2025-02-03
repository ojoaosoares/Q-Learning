import sys
import random

alpha = 0.1  
gamma = 0.9  
epsilon = 0.1  

actions = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

action_symbols = {
    "up": "^",
    "down": "V",
    "left": "<",
    "right": ">"
}

standard_rewards = {
    '.': -0.1,  # Grama
    ';': -0.3,  # Grama Alta
    '+': -1.0,  # Água
    'x': -10.0, # Fogo
    'O': 10.0,  # Objetivo
    '@': float('-inf')   # Parede (estado inválido)
}

positive_rewards = {
    '.': 3.0,    # Grama
    ';': 1.5,    # Grama Alta
    '+': 1.0,    # Água
    'x': 0.0,    # Fogo
    'O': 10.0,   # Objetivo
    '@': float('-inf')  # Parede (estado inválido)
}

def initialize_q_table(cols, rows):
    Q = {}
    for r in range(rows):
        for c in range(cols):
            Q[(c, r)] = {a: 0.0 for a in actions}  # Inicializa todas as ações com Q=0
    return Q

def get_next_state(state, action, cols, rows):
    c, r = state
    dc, dr = actions[action]
    new_r, new_c = r + dr, c + dc

    if 0 <= new_r < rows and 0 <= new_c < cols:
        return (new_c, new_r)
    return state 

def choose_action(Q, state):
    if random.uniform(0, 1) < epsilon:
        return random.choice(list(actions.keys()))

    return max(Q[state], key=Q[state].get)
    

def qlearning(the_map, cols, rows, xi, yi, iterations, mode):

    rewards = standard_rewards
    
    if mode == 2:
        rewards = positive_rewards

    Q = initialize_q_table(cols, rows)
    it = 0

    while it < iterations:
        state = (xi, yi)

        while True:
            print(f"Estado atual: {state}")  # Debug

            # Checando se o estado é final
            if the_map[state[1]][state[0]] in "XO":
                print("Estado final atingido.")
                # reward = rewards[the_map[state[1]][state[0]]]
                break  # Fim do episódio

            action = choose_action(Q, state)
            next_state = get_next_state(state, action, cols, rows)

            print(f"Ação escolhida: {action}, Próximo estado: {next_state}")

            # Verificação para limites do mapa
            if next_state[0] < 0 or next_state[0] >= cols or next_state[1] < 0 or next_state[1] >= rows:
                print("Tentativa de sair dos limites!")
                continue  # Tente outra ação

            reward = rewards[the_map[state[1]][state[0]]]
            max_q_next = max(Q[next_state].values())

            # Verificando se o próximo estado é inválido
            if state == next_state:
                reward = rewards['@']
            

            # Obtendo a recompensa do estado atual
            

            # Atualizando a Q-table
            Q[state][action] = (1 - alpha) * Q[state][action] + gamma * (reward + max_q_next)

            if mode == 3:
                if random.uniform(0, 1) < 0.2:  # 10% de chance de mudar para uma ação perpendicular
                    if action == "up":
                        action = random.choice(["left", "right"])  # Escolhe aleatoriamente entre "left" ou "right"
                    elif action == "down":
                        action = random.choice(["left", "right"])  # Escolhe aleatoriamente entre "left" ou "right"
                    elif action == "left":
                        action = random.choice(["up", "down"])  # Escolhe aleatoriamente entre "up" ou "down"
                    elif action == "right":
                        action = random.choice(["up", "down"])
                next_state = get_next_state(state, action, cols, rows)
                    
                
            state = next_state
            

        it += 1

    return Q



def print_q_map(Q, the_map, cols, rows):
    for r in range(rows):
        line = ""
        for c in range(cols):
            if the_map[r][c] in "XO@":
                line += the_map[r][c]  # Imprime os caracteres 'X', 'O' e '@' como estão
            else:
                best_action = max(Q[(c, r)], key=Q[(c, r)].get)  # Pega a melhor ação na posição (r, c)
                simbol = action_symbols.get(best_action, "<")  # Usa o símbolo da ação
                line += simbol
        print(line)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Use: python3 qlearning.py [filename] [mode] [xi] [yi] [iterations]")
        print("Use: modes [standard, positive, stochastic]")
        sys.exit(1)

    filename, mode, x, y, iterations = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])

    with open(filename, 'r') as file:
    # Lendo as três primeiras linhas
        cols, rows = map(int, file.readline().split())

        # Lendo as próximas linhas que representam os dados das colunas
        the_map = [list(file.readline().strip()) for _ in range(rows)]

    if (mode == 'standard'):
        Q = qlearning(the_map, cols, rows, x, y, iterations, mode=1)

    elif (mode == 'positive'):
        Q = qlearning(the_map, cols, rows, x, y, iterations, mode=2)

    elif (mode == 'stochastic'):
        Q = qlearning(the_map, cols, rows, x, y, iterations, mode=3)

    else:
        sys.exit(1)

    print_q_map(Q, the_map, cols, rows)
