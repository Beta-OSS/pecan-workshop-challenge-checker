flags = {
    "challenge1": "flag{secret1}",
    "challenge2": "flag{secret2}",
}

def check_flag(challenge_id, submitted_flag):
    if challenge_id not in flags:
        return False
    return flags[challenge_id] == submitted_flag
