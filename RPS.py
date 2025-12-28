from random import choice

def winhand(hand):

    if hand == "R":
        return "P"
    elif hand == "P":
        return "S"
    elif hand == "S":
        return "R"  
    else:
        return choice(["R", "P", "S"])

def markov_l4(history):
    """
    Markov de orden 4.
    recive el historial de jugadas del oponente
    y predice la siguiente.
    """
    
    # si no hay suficientes datos, no predecir
    if len(history) < 5:
        return None

    transitions = {}

    # construir tabla
    for i in range(len(history) - 4):

        # crear estado de 4 jugadas
        state = "".join(history[i:i+4])
        next_move = history[i+4]

        # inicializar si no existe
        if state not in transitions:
            transitions[state] = {"R": 0, "P": 0, "S": 0}

        transitions[state][next_move] += 1

    # predecir siguiente jugada
    current_state = "".join(history[-4:])

    # si el estado no existe en la tabla, no predecir
    if current_state not in transitions:
        return None

    counts = transitions[current_state]

    # si no hay transiciones, no predecir
    if sum(counts.values()) == 0:
        return None

    # devolver la jugada más probable
    return max(counts, key=counts.get)


def player(prev_play, opponent_history=[]):

    if prev_play:
        opponent_history.append(prev_play)

    # primeros movimientos: aleatorio
    if len(opponent_history) < 5:
        return choice(["R", "P", "S"])

    prediction = markov_l4(opponent_history)

    if prediction:
        return winhand(prediction)

    return choice(["R", "P", "S"])
