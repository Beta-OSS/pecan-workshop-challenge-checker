#format name: [category, descritpion, flag, files]

class Challenges:
    def __init__(self, name, category, description, flag, file = None):
        self.name = name
        self.category = category
        self.description = description
        self.flag = flag
        self.file = file

def check_flag(challenge_id, submitted_flag):
    print(challenge_id)
    if challenge_id not in flags:
        return False
    return flags[challenge_id].flag == submitted_flag

flags = {
    "c1": Challenges("Challenge 1", "Cryptography", "Test Description", "pecan{flag1}"),
    "c2": Challenges("Challenge 2", "Cryptography", "Test Description", "pecan{flag2}"),
    "c3": Challenges("Challenge 3", "Steganography", "Just another test description", "pecan{flag3}"),
    "c4": Challenges("Challenge 4", "Steganography", "Just another test description", "pecan{flag4}"),
    "c5": Challenges("Challenge 5", "Forensics", "Just another test description", "pecan{flag5}"),
    "c6": Challenges("Challenge 6", "Forensics", "Just another test description", "pecan{flag6}"),
}