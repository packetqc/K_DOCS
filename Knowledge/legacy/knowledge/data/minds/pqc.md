# PQC

## Harvest Metadata
| Field | Value |
|-------|-------|
| Repo | [packetqc/PQC](https://github.com/packetqc/PQC) |
| Last harvest | 2026-02-21 |
| Branches scanned | master |

### Branch Cursors
| Branch | Last harvested SHA | Date |
|--------|-------------------|------|
| master | e46fd5386d7f9b37a8602ebd7b74260e9a531bb3 | 2025-09-18 (unchanged since 2026-02-19 harvest) |

---

## Knowledge Version
| Field | Value |
|-------|-------|
| Satellite version | v0 (no tag — pre-bootstrap) |
| Core version | v35 |
| Drift | 35 versions behind (complete) 🔴 |
| Missing features | All: entire knowledge system postdates this repo's last activity |
| Last remediated | never |

---

## Knowledge Status
| Check | Status | Detail |
|-------|--------|--------|
| Bootstrap | **missing** | No CLAUDE.md, no reference to packetqc/knowledge |
| Session persistence | **missing** | No notes/ folder |
| Live tooling | **missing** | No live/ folder |
| Own knowledge | **basic** | Two markdown files (README.md + TLS1.3.md), documentation only |
| Publications | **none** | No publications/ folder. Content is reference/learning material. |

---

## Claude Instructions

None. No CLAUDE.md exists. PQC is a pure documentation/reference repository. No source code. Last activity 2025-09-18.

---

## Evolved Patterns

### ML-KEM key sizing reference for embedded — **PROMOTION CANDIDATE**
Complete size tables for ML-KEM (512/768/1024) and ML-DSA (44/65/87) with private key, public key, ciphertext, and shared secret sizes. Critical for embedded memory budgeting on constrained devices.

| Grade | Private Key | Public Key | Ciphertext | Shared Secret |
|-------|-------------|------------|------------|---------------|
| ML-KEM-512 | 1,632 | 800 | 768 | 32 |
| ML-KEM-768 | 2,400 | 1,184 | 1,088 | 32 |
| ML-KEM-1024 | 3,168 | 1,568 | 1,568 | 32 |

### PQC library compliance for STM32 — **PROMOTION CANDIDATE**
| Library | ML-DSA | ML-KEM | STM32 tested |
|---------|--------|--------|-------------|
| WolfSSL v5.8.2 | yes | yes | **yes** (production choice) |
| STM32 CMOX v1.1.0 | yes | pending | yes |
| liboqs | yes | yes | no (dev only) |

### LAN PQC key exchange protocol
UDP broadcast announce → TCP unicast with ML-KEM encapsulation/decapsulation → PQC-AES encrypted data channel. Reusable protocol pattern for embedded device communication.

### Flash certificate storage pattern
`__attribute__((section(".certificates")))` with custom linker section `.certificates`. DER certificates embedded in firmware via `xxd -i` conversion pipeline.

### NetX Duo TLS 1.3 session lifecycle
Complete API workflow: TCP establish → TLS session start → `nx_secure_tls_packet_allocate` → send/receive → CloseNotify → session end. Must use TLS-specific packet allocator, not generic `nx_packet_allocate`.

---

## New Pitfalls

### liboqs not STM32-tested
liboqs builds with `gcc-arm-none-eabi` cross-compilation but is not validated on actual STM32 hardware. Dev/test environment only — do not use in production firmware.

### CMOX ML-KEM version dependency
ML-KEM support requires CMOX v1.1.0+. Earlier versions only have ML-DSA. Must verify library version before attempting ML-KEM operations.

### NetX Duo TLS packet allocator
Must use `nx_secure_tls_packet_allocate`, NOT `nx_packet_allocate`. Common mistake that causes silent failures.

### TLS session requires TCP first
`nx_secure_tls_session_start` fails if TCP connection is not already established. Ordering is mandatory: TCP connect → TLS start.

### CloseNotify required on both ends
Both ends must process CloseNotify for clean TLS session shutdown. Unilateral close can leave the peer in a broken state.

---

## Methodology Progress

- **OpenSSL 3.5.0 native PQC**: Eliminates OQS provider dependency for PQC certificate generation. Streamlined workflow: `openssl genpkey -algorithm mldsa87`.
- **Certificate-to-C pipeline**: `openssl x509 -outform DER` → `xxd -i` → C array. Proven workflow for embedding certs in firmware.

---

## Publications Detected
| Title | Path (in satellite) | Status |
|-------|---------------------|--------|
| (none) | — | No publications/ folder. Content is learning/reference material. |

---

## Promotion Candidates

1. **ML-KEM/ML-DSA size reference** — Complete sizing tables for memory budgeting on embedded. → `patterns/` (new file: pqc-embedded.md)
2. **PQC library compliance matrix** — WolfSSL = production, CMOX = pending, liboqs = dev only. → `patterns/` (new file: pqc-embedded.md)
3. **Flash certificate storage pattern** — Linker section + xxd pipeline. → `patterns/embedded-debugging.md` or new patterns file
