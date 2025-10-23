def processStates(initial_state, events, transitions):
    current_state = initial_state

    for event in events:
        key = (current_state, event)
        if key in transitions:
            current_state = transitions[key]

    return current_state
