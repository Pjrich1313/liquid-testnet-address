#!/usr/bin/env python3
"""
Simple Chaum Blind Signature Demo (RSA-based)
For educational purposes only - NOT production secure.
"""

import hashlib
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import secrets

def generate_rsa_keys(bits=2048):
    key = RSA.generate(bits)
    return key.publickey(), key  # pubkey, privatekey

def blind_message(message: bytes, pubkey):
    """Blind the message"""
    m = bytes_to_long(hashlib.sha256(message).digest())
    r = secrets.randbelow(pubkey.n)  # random blinding factor
    while gcd(r, pubkey.n) != 1:
        r = secrets.randbelow(pubkey.n)
    blinded = (m * pow(r, pubkey.e, pubkey.n)) % pubkey.n
    return blinded, r

def blind_sign(blinded_msg: int, privkey):
    """Signer signs blinded message"""
    signature = pow(blinded_msg, privkey.d, privkey.n)
    return signature

def unblind(signature: int, r: int, pubkey):
    """Remove blinding factor"""
    r_inv = pow(r, -1, pubkey.n)
    unblinded = (signature * r_inv) % pubkey.n
    return unblinded

def verify_signature(message: bytes, signature: int, pubkey):
    """Verify RSA signature"""
    m = bytes_to_long(hashlib.sha256(message).digest())
    return pow(signature, pubkey.e, pubkey.n) == m

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print("=== Chaum Blind Signature Demo ===\n")
    
    # Setup
    pubkey, privkey = generate_rsa_keys(1024)  # small for demo
    
    message = b"My secret vote or coin serial number"
    print(f"Original message: {message.decode()}")
    
    # Blind
    blinded, r = blind_message(message, pubkey)
    print("Message blinded and sent to signer.")
    
    # Sign
    blind_sig = blind_sign(blinded, privkey)
    print("Signer produced blind signature.")
    
    # Unblind
    signature = unblind(blind_sig, r, pubkey)
    print("Signature unblinded.")
    
    # Verify
    if verify_signature(message, signature, pubkey):
        print("✅ Signature verified successfully!")
    else:
        print("❌ Verification failed.")