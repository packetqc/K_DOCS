# Session 2026-02-21 — PQC Intel + knowledge-live Project Scoping

## Status
- Branch: claude/wakeup-functionality-6Drqy
- Focus: PQC capability evolution + knowledge-live satellite project scoping

## #0:pqc — Knowledge System PQC Intel

### OpenSSL 3.5+ as Installable Asset
- OpenSSL 3.5+ must be available as an installable asset in the knowledge system
- The `scripts/pqc_envelope.py` auto-detection ladder (Level 3: ML-KEM-1024) requires OpenSSL 3.5+ or oqs-provider
- Currently falling back to Level 2 (X25519) because container OpenSSL < 3.5
- **Action**: Include OpenSSL 3.5+ build/install script as a knowledge asset (like `live/` tooling)

### OWASP Top 10 — Ephemeral Token Considerations
- Review OWASP guidance on ephemeral/short-lived token management
- Current ephemeral token protocol (v27) aligns with OWASP principles:
  - No credential storage at rest
  - Session-scoped lifetime
  - Minimum privilege (read-only Contents scope)
  - Explicit cleanup (image files deleted after extraction)
- **TODO**: Cross-reference against OWASP Top 10 2021 (A07: Identification and Authentication Failures) and validate compliance

### PQC Industry Migration — Multi-Algorithm Support
- The PQC era requires supporting/testing multiple concurrent algorithms
- Current: ML-KEM-1024 (FIPS 203) only — single algorithm
- Evolution needed: test and support multiple PQC candidates as industry standardizes
- Rationale: different vendors/platforms may adopt different PQC algorithms during transition
- The auto-detection ladder pattern (already in pqc_envelope.py) naturally extends to multiple PQC algorithms
- **Candidate algorithms to evaluate**:
  - ML-KEM-1024 (FIPS 203) — current, lattice-based KEM
  - ML-DSA (FIPS 204) — lattice-based digital signatures (for beacon authentication)
  - SLH-DSA (FIPS 205) — hash-based signatures (stateless, conservative fallback)
  - BIKE, HQC — code-based KEMs (NIST round 4 candidates)

## knowledge-live — New Satellite Project (Pre-Scoping)

### Purpose
Dedicated satellite project for the live knowledge network — PQC-secured communications between core and satellite minds. Separates the network infrastructure from the knowledge system itself.

### Architecture Requirements
1. **wolfSSL on Ubuntu** — primary TLS/crypto library
   - wolfSSL has native PQC support (via liboqs integration)
   - wolfCrypt provides the crypto primitives
   - Compile wolfSSL with `--enable-pqc` flag
2. **wolfSSL-powered curl** — for GitHub API and external HTTPS communications
   - Build curl linked against wolfSSL instead of OpenSSL
   - Enables PQC-secured HTTPS connections to GitHub
   - Replace system curl with wolfSSL-backed build for all external comms
3. **Minimal user interaction for PQC key generation**
   - No certificates required — generate PQC keys programmatically
   - Self-contained key generation (no CA, no CSR, no manual steps)
   - Keys generated on first beacon start, rotated per session
4. **Multi-solution PQC support**
   - Start with wolfSSL as primary
   - Support OpenSSL 3.5+ as alternative (when available)
   - Auto-detect which crypto library is available (same ladder pattern as pqc_envelope.py)
5. **Network communications between core and satellite minds**
   - Beacon-to-beacon encrypted channels
   - PQC key exchange for session establishment
   - Mutual authentication without traditional PKI
   - Support harvest data transfer over encrypted channels

### Claude/Anthropic PQC Guidance
- Research what Claude/Anthropic recommends for PQC key usage in TLS
- How to implement PQC with minimal user interaction
- Best practices for certificate-less PQC deployments
- Hybrid mode: classical + PQC during transition period

### wolfSSL + curl Build Chain (Ubuntu)
```
# wolfSSL with PQC
git clone https://github.com/wolfSSL/wolfssl.git
cd wolfssl && ./autogen.sh
./configure --enable-pqc --enable-tls13 --enable-all
make && sudo make install

# curl with wolfSSL backend
git clone https://github.com/curl/curl.git
cd curl && autoreconf -fi
./configure --with-wolfssl
make && sudo make install
```

### Integration with Knowledge System
- knowledge-live reads packetqc/knowledge on wakeup (standard satellite)
- Provides wolfSSL-backed secure transport layer
- Replaces Python-only pqc_envelope.py with native C crypto (performance)
- Python wrapper around wolfSSL for beacon integration
- knowledge-live assets synced to satellites that need PQC network comms

## Platform Test Results — OpenSSL 3.0.13 on Ubuntu (Container)

### Confirmed Working
| Capability | Algorithm | OpenSSL CLI command | Status |
|-----------|-----------|---------------------|--------|
| Key exchange | X25519 (Curve25519 ECDH) | `openssl genpkey -algorithm X25519` | WORKING |
| Encryption | AES-256-CBC | `openssl enc -aes-256-cbc` | WORKING |
| Key derivation | HKDF-SHA256 | `openssl kdf ... HKDF` | WORKING |
| Signatures | ED25519 (`-rawin` mandatory) | `openssl pkeyutl -sign -rawin` | WORKING |

### Not Available (needs OpenSSL 3.5+ or oqs-provider)
- ML-KEM-1024 (FIPS 203) — post-quantum KEM
- ML-DSA (FIPS 204) — post-quantum digital signatures
- SLH-DSA (FIPS 205) — hash-based signatures

### Python cryptography library
- **BROKEN** on this container — `ModuleNotFoundError: No module named '_cffi_backend'`
- Workaround: use OpenSSL CLI directly (all operations confirmed working)
- Fix for knowledge-live: `pip install cffi` or use wolfSSL Python bindings

### Key Insight: Token-as-Key-Seed
- GitHub PAT token can seed PQC key generation via HKDF
- One user action (create PAT) enables both repo access AND encrypted comms
- `HKDF(PAT, salt="knowledge-live", info="session-keys") → X25519 private key`
- No certificates, no CA, no CSR — minimal interaction design

### Proven Recipes (all tested on this platform)
1. X25519 key pair generation → `/dev/shm/` (RAM only)
2. Two-party key exchange → identical shared secrets confirmed
3. AES-256-CBC encrypt/decrypt with derived key → round-trip successful
4. ED25519 sign/verify with `-rawin` flag → verified successfully
5. Zero-overwrite cleanup → `dd if=/dev/zero` before `rm`

## Decisions
- [ ] OpenSSL 3.5+ install script → knowledge asset
- [ ] OWASP compliance audit on ephemeral token protocol
- [ ] knowledge-live satellite creation (project create knowledge-live)
- [ ] wolfSSL + curl build automation for Ubuntu
- [ ] PQC multi-algorithm testing framework
- [x] Platform crypto capabilities tested and documented
- [ ] Token-as-key-seed implementation in pqc_envelope.py
