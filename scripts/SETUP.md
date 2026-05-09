# Scripts Setup

## sync-posts.py — Google Sheet → published posts

### Your Google Sheet format

One tab, one row per post:

| A: Date | B: Post text | C: Funnel | D: Notes |
|---|---|---|---|
| 2025-03-14 | I've been running this agency for 3 years... | top | high engagement |
| 2025-03-10 | We just closed our biggest deal ever... | bottom | |

- **Date**: YYYY-MM-DD preferred, MM/DD/YYYY also works
- **Post text**: full post, line breaks included — just paste it in
- **Funnel**: top / mid / bottom (optional but helps the Idea Scout avoid repeating topics)
- **Notes**: anything useful — "high engagement", "low reach", "client loved this" (optional)

---

### One-time setup

**1. Install dependencies**
```bash
pip install gspread google-auth
```

**2. Create Google Cloud credentials**
- Go to [console.cloud.google.com](https://console.cloud.google.com)
- Create a new project (or use existing)
- Enable the **Google Sheets API**
- Go to IAM & Admin → Service Accounts → Create Service Account
- Give it a name (e.g. `linkedin-content-sync`)
- Click the service account → Keys tab → Add Key → JSON
- Download the JSON file → rename it `credentials.json` → put it in `scripts/`

**3. Share your sheet**
- Open your Google Sheet
- Click Share
- Add the service account email (looks like `name@project.iam.gserviceaccount.com`)
- Viewer access is enough

**4. Get your Sheet ID**
From the URL: `https://docs.google.com/spreadsheets/d/**THIS_PART**/edit`

---

### Running the sync

From the repo root:

```bash
# First client
python3 scripts/sync-posts.py --client acme-corp --sheet-id 1BxiMVs0XRA...

# Second client (different sheet)
python3 scripts/sync-posts.py --client other-client --sheet-id 2CyiNWt1YSB...
```

Run this weekly after you update the sheet. It skips posts that already exist — safe to run multiple times.

---

### What it creates

Each post becomes a `.md` file in `clients/[client]/posts/published/`:

```
clients/
  acme-corp/
    posts/
      published/
        2025-03-14-ive-been-running-this-agency.md
        2025-03-10-we-just-closed-our-biggest-deal.md
```

Claude Code reads these automatically at the start of every session to learn voice, style, and topic history.
