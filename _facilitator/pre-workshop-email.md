# Pre-Workshop Email

> Send 5 days before. English. Plain text or simple HTML.

---

**Subject:** Vibecoding Workshop — please do these 3 things before we meet

Hi everyone,

Looking forward to seeing you on **<date>** for the Vibecoding Workshop. To make sure we can start on time, please do the three things below **before** you arrive.

**1. Bring a laptop with admin rights.**
You will install software. If your laptop is locked down by IT, please sort it out this week — we can't wait for it on the day.

**2. Install the tools (10 minutes).**
- **Node.js 20 or newer:** https://nodejs.org
- **git:** https://git-scm.com (Mac/Linux usually already have it)
- **Claude Code:**
  ```
  npm install -g @anthropic-ai/claude-code
  ```

**3. Create a free Anthropic account.**
Go to https://claude.ai and sign up. The free tier is enough for the workshop. You do **not** need a paid plan.

**4. Run the pre-flight check.**
Clone the workshop repo and run the check script:
```
git clone https://github.com/quershifttechnologiesgmbh/vibecoding-workshop-2026.git vibecoding-workshop
cd vibecoding-workshop
bash check.sh
```

If `check.sh` says "All good", you're set. If it complains, reply to this email and we'll fix it before the day.

---

**A note on data**

We will use only synthetic data in this workshop. Please do **not** bring real client data, real API keys, or anything covered by an NDA. Use your personal Anthropic account, not a work one.

---

**Format**

- 4 hours, on-site, English
- One 15-min break in the middle
- You will be paired with a buddy on arrival — heterogeneous pairs by design
- Bring water and snacks; we'll have coffee

See you on **<date>**.

Best,
Elias
