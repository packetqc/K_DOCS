# MPLIB

## Harvest Metadata
| Field | Value |
|-------|-------|
| Repo | [packetqc/MPLIB](https://github.com/packetqc/MPLIB) |
| Last harvest | 2026-02-22 |
| Branches scanned | main |

### Branch Cursors
| Branch | Last harvested SHA | Date |
|--------|-------------------|------|
| main | 69ab56868726826cd171efaac988eae201e079df | 2026-02-21 |

---

## Knowledge Version
| Field | Value |
|-------|-------|
| Satellite version | v31 |
| Core version | v35 |
| Drift | 4 🟠 |
| Missing features | v32 recall + contextual help, v33 PAT access levels, v34 secure textarea delivery, v35 project entity model |
| Last remediated | 2026-02-21 (critical-subset CLAUDE.md deployed) |

---

## Knowledge Status
| Check | Status | Detail |
|-------|--------|--------|
| Bootstrap | 🟢 **active** | CLAUDE.md with critical-subset template (v31), knowledge pointer active |
| Session persistence | 🟢 **active** | notes/ folder with 2 session files |
| Live tooling | 🟢 **deployed** | live/ fully synced — beacon (`knowledge_beacon.py`), scanner (`knowledge_scanner.py`), capture (`stream_capture.py`), `dynamic/`, `static/`, README.md |
| Own knowledge | 🟢 **structured** | README.md + key-exchange.md + pqc-sizes.md + STM32N6570-dk.md, all with YAML frontmatter |
| Publications | ⚪ **scaffold** | docs/ structure created (GitHub Pages scaffold), no publication content yet |
| GitHub Pages | ⚪ **pending** | docs/ scaffold deployed, user needs to enable Pages in repo Settings |

---

## Claude Instructions

Critical-subset CLAUDE.md (v31) deployed with:
- Auto-wakeup protocol
- Session lifecycle (wakeup → work → save)
- Save protocol (semi-automatic, PR-based)
- Branch protocol (proxy reality)
- Human bridge principle
- Context loss recovery ladder
- 17-command reference table
- Project-specific section (architecture, hardware, conventions)

---

## Evolved Patterns

### Multi-RTOS abstraction — **PROMOTION CANDIDATE**
The same codebase compiles against both FreeRTOS and ThreadX using `#if defined(FREERTOS)` / `#elif defined(AZRTOS)` preprocessor guards. Includes an RTOS equivalence table. Proven pattern for hardware library portability across RTOS platforms.

### Library-as-static-archive
MPLIB compiles to `libMPLIB_STM32_MCU.a`, linked by application frameworks. Clean separation of library from app framework enables multi-target builds from one source.

### Thread/Singleton architecture (7 dedicated threads)
default, GUI, Data, System, Display, Secure, SDCard, Network — each with visual LED heartbeats for runtime health monitoring. **Already captured** in core patterns/rtos-integration.md as singleton module pattern.

### Dual cryptography (ECC + PQC)
System supports both ECC KEM for current key exchange and ML-KEM (post-quantum) for future-proofing. Both coexist during transition period. ML-KEM grades 512/768/1024 documented with key sizes.

### Queue/Mutex communication model
Explicit separation: queues for event/message passing (gui_msg, logs_msg, sd_msg), mutexes for shared state (canLog). Documented per-asset with clear ownership.

### TouchGFX Model-Presenter-View with backend services
C starts the thread, C++ enters the RTOS, Model handles queues, Presenter translates via modelListener, View binds to screen. Full sequence documented in mermaid. **Extends** core patterns/ui-backend-separation.md.

---

## New Pitfalls

### STM32N6570-DK CubeMX limitation — **PROMOTION CANDIDATE**
Creating project from CubeMX is impossible for the N6570-DK. Must start from TouchGFX Designer project or existing .ioc. Linker files are lost during code regeneration and must be restored manually.

### TouchGFX project structure mismatch
TouchGFX has a different project folder structure than standard CubeMX outputs. Requires manual include path and linker script adjustments.

### Binary signing requirement for N6
STM32N6 requires signed binaries (FSBL + application) before flashing. Specific flash addresses: FSBL at 0x70000000, secure app at 0x70100000, non-secure at 0x70200000.

### MPU configuration for UID memory
Reading STM32 UID requires MPU region config for 0x08FFF800-0x08FFFFFF as read-only with `MPU_DEVICE_nGnRnE` attributes.

### USB BSP power requires TCPP0203
USB power control on STM32H573I-DK needs BSP USBPD files manually copied (CubeMX does not provide them), plus TCPP0203_SUPPORT symbol, plus EXTI1 IRQ handler.

---

## Methodology Progress

- **UART printf for clearing terminal**: `printf("\x1B[2J"); printf("%c[0;0H", 0x1b);` — small but useful diagnostic trick.
- **ThreadX thread staggered startup**: Default thread resumes other threads with `tx_thread_sleep(30)` gaps between them, preventing boot race conditions.
- **Iterative staging bootstrap** (new): 3-round satellite deployment completed in single session — Round 1 scaffold, Round 2 intel/normalize, Round 3 GitHub Pages. Progressive commits per round with human bridge staging.
- **Doc normalization intel** (new): Pre-publication audit identifying 17 orphan assets, 3 placeholder sections, 1 content duplication, and asset naming inconsistencies — documented before acting.

---

## Publications Detected
| Title | Path (in satellite) | Status |
|-------|---------------------|--------|
| (none yet) | docs/publications/ scaffold ready | Hub pages created, no content pages |

---

## Promotion Candidates

1. **Multi-RTOS abstraction** — FreeRTOS/ThreadX dual support with preprocessor guards + equivalence table. Generally applicable to any cross-RTOS library. → `patterns/rtos-integration.md`
2. **CubeMX N6570-DK limitation** — Cannot create project from CubeMX, must start from TouchGFX Designer. → `lessons/pitfalls.md`
3. **TouchGFX MVP with backend services** — Extends the existing UI/backend separation pattern with concrete sequence diagrams. → `patterns/ui-backend-separation.md`
