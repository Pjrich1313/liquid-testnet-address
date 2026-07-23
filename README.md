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

Add to `~/.elements/elements.conf` (testnet):

```conf
testnet=1
server=1
daemon=1
txindex=1
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
rpcport=18884

# Generated rpcauth:
rpcauth=liquidtestuser:26207a38c6756066b3a0aadc5862484c$3f1a... (example - use your own)
```

**Your generated credentials** (example):
- Username: `liquidtestuser`
- Password: `41ee13dea6479e312d3fa73ffd893e1697bddc80041313c943bdb4ebcbb70c34`

**Full rpcauth line:**
`rpcauth=liquidtestuser:26207a38c6756066b3a0aadc5862484c$...`

Replace with your own generated values for security.

### Test
```bash
elements-cli getblockchaininfo
```

---

More tools coming soon!