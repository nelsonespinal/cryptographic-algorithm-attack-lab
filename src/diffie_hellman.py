import random

def generate_private_key(p):
    return random.randint(2, p - 2)


def generate_public_key(g, private_key, p):
    return pow(g, private_key, p)


def generate_shared_secret(other_public_key, private_key, p):
    return pow(other_public_key, private_key, p)

