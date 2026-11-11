# Liquid Testnet Address

**Address:** `vjTwFjtVE7Fy9gjwQSxas9FkrqcnK1SeobPkdD9tghdNmCvxoXhSeCjpgD3ponKJukkD2BNPX25dZL48`

This is a testnet address on the [Liquid Network](https://liquid.network/).

Useful for testing Liquid transactions, peg-ins/peg-outs, or other features on testnet.

## Installation

### Prerequisites
- Git
- A Liquid wallet or tool (e.g., Elements or Liquid-specific libraries)

### Clone the repo
```bash
git clone https://github.com/Pjrich1313/liquid-testnet-address.git
cd liquid-testnet-address
```

### Usage
- Use the address in your Liquid testnet applications or scripts.
- Monitor balance via [Liquid Testnet Explorer](https://blockstream.info/liquidtestnet/address/vjTwFjtVE7Fy9gjwQSxas9FkrqcnK1SeobPkdD9tghdNmCvxoXhSeCjpgD3ponKJukkD2BNPX25dZL48)

## Elements Core Installation

**Elements Core** is the reference implementation for running a Liquid Network node.

### Quick Install (Binary)

**Linux (Ubuntu/Debian)**
```bash
wget https://github.com/ElementsProject/elements/releases/download/elements-23.3.0/elements-23.3.0-x86_64-linux-gnu.tar.gz
tar -xzf elements-23.3.0-x86_64-linux-gnu.tar.gz
cd elements-23.3.0
sudo install -m 0755 bin/* /usr/local/bin/
```

**macOS**
```bash
brew install elements
```

Download latest: https://github.com/ElementsProject/elements/releases

## RPC Authentication

### Recommended: Use `rpcauth` (hashed password)

Keep real RPC credentials in a local `elements.conf` (typically `~/.elements/elements.conf`). Do not commit that file. This repository ignores `elements.conf`, other `*.conf` files that can hold secrets (including `rpcauth.local.conf` written by `generate_rpcauth.py`), and `.env`. The tracked `rpcauth.conf` file is a placeholder only.

Add this to your local `elements.conf` (testnet), using your own generated values:

```conf
testnet=1
server=1
daemon=1
txindex=1
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
rpcport=18884

# Generated rpcauth — replace with your own; never commit the real line:
rpcauth=<your-rpc-username>:<your-rpcauth-salt>$<your-rpcauth-hash>
```

**Credentials** (placeholders only; store the real values in local `elements.conf`):
- Username: `<your-rpc-username>`
- Password: `<your-rpc-password>`

**Full rpcauth line:**
`rpcauth=<your-rpc-username>:<your-rpcauth-salt>$<your-rpcauth-hash>`

Generate a line with this repo's script (a random password is used unless you pass `-p`):

```bash
python3 generate_rpcauth.py -u <your-rpc-username>
```

Copy the printed `rpcauth=` line into the node's local `elements.conf`. The script also writes `rpcauth.local.conf` in the working directory; that file is gitignored and must stay uncommitted.

### Rotate your RPC password

1. Generate a new `rpcauth` line with `python3 generate_rpcauth.py` (or pass a strong random password with `-p`).
2. Put that line in the node's `elements.conf`, replacing any previous `rpcauth` or `rpcpassword` entry. Keep `elements.conf` local and uncommitted.
3. Restart `elementsd`.
4. Update any clients so they use the new username and password.

### Test
```bash
elements-cli -rpcuser=<your-rpc-username> -rpcpassword=<your-rpc-password> getblockchaininfo
```

---

More tools coming soon!