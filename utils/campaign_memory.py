campaign_memory = {}

def save_message(company, persona, step, message):
    campaign_memory.setdefault((company, persona), {})[step] = message

def get_campaign_history(company, persona):
    return campaign_memory.get((company, persona), {})
