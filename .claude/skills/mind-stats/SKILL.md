---
name: mind-stats
description: "Show memory stats table — disk size, token counts, loaded context, and available tokens before compaction."
allowed-tools: Bash
---

## K_MIND — Memory Stats

!`cd /mnt/d/K/K_MIND && python3 scripts/memory_stats.py`

Output this table to the user. The **Loaded** column shows tokens each store occupies in context. **Available** shows approximate tokens remaining before compaction (based on 200K context window minus K_MIND loaded; actual usage includes conversation history).
