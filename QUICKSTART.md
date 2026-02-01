# 🚀 Quick Start — Haven

This is the fastest way to run the full app locally.

---

## ✅ Prereqs
- Python **3.10+** (3.11 recommended)
- Firebase Admin service account JSON
- Google AI API key (Gemini)
- Resend API key (optional)

---

## 1) Install
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 2) Add Firebase Admin key
Download a Firebase service account JSON and place it at:
```
./serviceAccountKey.json
```
Or set:
```
FIREBASE_KEY_PATH=/path/to/key.json
```

---

## 3) Set env vars
Minimal:
```bash
export FIREBASE_KEY_PATH=./serviceAccountKey.json
export GOOGLE_API_KEY=your_gemini_api_key
export APP_BASE_URL=http://localhost:5000
export MAIL_ENABLED=false
```

If you want emails:
```bash
export MAIL_ENABLED=true
export RESEND_API_KEY=your_resend_key
export MAIL_FROM="Haven <no-reply@mail.haven.mathengeinc.com>"
export MAIL_REPLY_TO=support@haven.mathengeinc.com
```

---

## 4) Run
```bash
python run.py
```
Open: `http://localhost:5000`

---

## What to test
1) Google sign‑in
2) Chat + bubble game + mood slider
3) Group match + insight card
4) Booking + confirmation email + calendar file
5) Client summary (after booking) + **/my-group** page
6) Therapist dashboard (set user role to therapist)

---

## Troubleshooting

**Port in use**
```bash
# Change the port in run.py if needed
```

**Firebase key missing**
- Set `FIREBASE_KEY_PATH` or place `serviceAccountKey.json` in the root.

**No emails**
- Set `MAIL_ENABLED=true` and provide `RESEND_API_KEY` + `MAIL_FROM`.

---

## Render deployment
Start command:
```bash
gunicorn wsgi:app --bind 0.0.0.0:$PORT
```

Use `.env.render` as your template for production env vars.
