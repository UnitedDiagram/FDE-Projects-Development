ticket = {
    "ticket_id": "T101",
    "text": "Production outage",
    "affected_users": 1200
}

def validate_ticket(ticket):

    if 'T' in ticket['ticket_id'] and len(ticket['ticket_id']) == 4 and isinstance(ticket['ticket_id'], str):
        if isinstance(ticket['text'], str) :
            if isinstance(ticket['affected_users'], int):
                return True
            else:
                return False

print(validate_ticket(ticket))