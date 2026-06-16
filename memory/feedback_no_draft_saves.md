---
name: feedback_no_draft_saves
description: Don't save drafts to files during refinement — show them in chat instead
metadata:
  type: feedback
---

Don't write drafts to the filesystem during the writing/refinement phase. Show the draft directly in the conversation so the user can refine it inline.

**Why:** User wants to iterate on drafts in chat, not in files. Saving to disk mid-refinement interrupts the flow and is premature.

**How to apply:** Only save to `clients/[client]/drafts/` after the user is satisfied with the draft and explicitly says to save it (or asks for it to be filed).
