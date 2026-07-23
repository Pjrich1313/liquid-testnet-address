#/usr/bin/env python3
"""
RPC Auth Generator for Elements Core / Bitcoin Core
Generates secure rpcauth lines for elements.conf or bitcoin.conf
"""

import hashlib
import secrets
import hmac
import argparse
import sys

def generate_rpcauth(username: str, password: str = None):
    """Generate rpcauth string and return (rpcauth_line, password)"""
    if password is None:
        password = secrets.token_hex(32)
    
    # Generate random salt
    salt = secrets.token_hex(16)
    
    # Create HMAC-SHA256 hash
    message = f"{username}:{password}".encode()
    hmac_obj = hmac.new(salt.encode(), message, hashlib.sha256)
    hashed = hmac_obj.hexdigest()
    
    rpcauth = f"rpcauth={username}:{salt}${hashed}"
    return rpcauth, password

def main():
    parser = argparse.ArgumentParser(description="Generate rpcauth for Elements/Bitcoin Core")
    parser.add_argument("-u", "--username", default="liquidtestuser", help="RPC username (default: liquidtestuser)")
    parser.add_argument("-p", "--password", help="Custom password (random if not provided)")
    
    args = parser.parse_args()
    
    rpcauth, password = generate_rpcauth(args.username, args.password)
    
    print("\n=== RPC Auth Generated ===")
    print(f"Username: {args.username}")
    print(f"Password: {password}")
    print(f"\nAdd this line to your elements.conf:")
    print(rpcauth)
    print("\nTest with:")
    print(f"elements-cli -rpcuser={args.username} -rpcpassword={password} getblockchaininfo")
    
    # Also write to file
    with open("rpcauth.conf", "w") as f:
        f.write("# Add this to ~/.elements/elements.conf\n")
        f.write(rpcauth + "\n")
    print("\nAlso saved to rpcauth.conf")

if __name__ == "__main__":
    main()