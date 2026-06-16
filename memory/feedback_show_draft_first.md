---
name: feedback-show-draft-first
description: Always show the draft in chat before saving to any file
metadata:
  type: feedback
---

Always show the post draft in the conversation first before writing it to any file.

**Why:** User interrupted a file write mid-session — they want to review and approve the draft in chat before it gets saved anywhere.

**How to apply:** After the Writer produces a draft, output it in the conversation. Only save to `clients/[client]/drafts/` after the user has seen it and given the go-ahead (explicit or implicit).
