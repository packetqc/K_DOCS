---
name: read conventions before render
description: Always read mindmap convention nodes from mind_memory.md before rendering — never rely on cached memory. Apply every node as a checklist.
type: feedback
---

Before every mindmap render, READ the mermaid convention nodes from mind_memory.md (lines under conventions > mermaid > mind map). Apply each one as a checklist item:

- display_layout nodes: depth, omissions, session structure, near memory categories
- theme_default nodes: init directive, useMaxWidth true, auto colors
- node_text_rules: human readable, no IDs, no reserved words

The mindmap IS the operating memory. Rendering from cached context causes convention drift (e.g., repeatedly losing useMaxWidth). The fix is mechanical: read the nodes, check them off, then render.
