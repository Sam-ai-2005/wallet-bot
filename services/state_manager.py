user_states = {}

def set_state(chat_id,state):
    user_states[chat_id] = state

def get_state(chat_id):
    return user_states.get(chat_id)    


def clear_state(chat_id):
    user_states.pop(chat_id, None)