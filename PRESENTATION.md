# Haven: AI‑Guided Group Matching
## Mentra Bounty Challenge Presentation

---

## Slide 1: Cover
**Haven**  
*A warm space for your mind to rest*

AI‑Guided Group Matching & Coordination

Team: Mani  
Mentra Bounty Challenge 2026

---

## Slide 2: The Problem

**Individual therapy is expensive and inaccessible**
- Average cost: $100–200 per session
- Long waitlists
- Many people never make it past intake

**Group therapy offers a solution, BUT…**
- Manual matching is slow and inconsistent
- Scheduling coordination is complex
- Cold intake forms turn people away

**The friction point**: Clinical intake workflows don’t feel human

---

## Slide 3: Why Group Matching Matters

**For Users**
- Lower cost
- Peer support and shared experience
- Reduced isolation

**For Therapists**
- Less admin work
- Better prepared sessions
- Higher quality matching

**The challenge**
Get the right people into the right group at the right time

---

## Slide 4: Our Solution — Haven

**Philosophy**: “A late‑night chat with a wise friend, not an intake form.”

**Stealth assessment**
- Warm conversation + playful reflection
- No cold forms
- Higher completion, better data

**Result**
- Users feel understood
- Therapists receive clearer context
- Matching becomes fast and scalable

---

## Slide 5: The Haven Journey

1) Google sign‑in (Firebase)
2) Calm AI chat (Gemini)
3) Bubble stressors + mood slider
4) Group match + insight card
5) Pick a time slot
6) Booking confirmation + calendar (.ics)
7) Client “My Group” page

Total time: ~8–10 minutes

---

## Slide 6: AI Approach — Conversational Analysis

**Gemini‑powered slot filling**

Critical fields:
1. Primary complaint
2. Duration
3. Severity
4. Goal

**Rules**
- Validation before questions
- No clinical jargon
- Short, calm responses
- AI is supportive, not medical

Structured responses validated with Pydantic for reliability.

---

## Slide 7: Group Matching

**5 archetype groups**
- Navigators (career/academic stress)
- Anchors (grief/loss)
- Mirrors (social anxiety/relationships)
- Balancers (burnout/boundaries)
- Explorers (identity/self‑esteem)

**Matching flow**
Conversation + reflections → structured data → group + insight

---

## Slide 8: End‑to‑End Workflow

```
Landing → Chat → Bubble Game → Mood Slider →
Insight → Match → Schedule → Booking → Confirmation
```

**Services**
- Firebase Auth + Firestore
- Gemini (google‑genai)
- Resend transactional email
- Calendar (.ics)

---

## Slide 9: Privacy & Safety

- Minimal data collection
- Clear consent + transparency
- Not a medical provider
- Crisis resources recommended for emergencies

---

## Slide 10: Technical Architecture

```
Frontend (Flask templates + JS)
  - Landing, chat, games, booking
  - Client “My Group” page

Backend (Flask API)
  - /api/chat/* (chat, assessments, match, booking)
  - /api/auth/* (Firebase sync)
  - /api/chat/session/* (summary + calendar)

Services
  - Firebase Auth + Firestore
  - Gemini (google‑genai)
  - Resend (email)
```

---

## Slide 11: Therapist Handoff

Therapists receive:
- Group overview + mood summary
- Participant summaries (from Firestore)
- Focus themes and stressors
- Download brief (mock)

Result: Session starts with context, not paperwork.

---

## Slide 12: Business Model (Projection)

- Per‑session fee (group model)
- Therapist subscription
- Enterprise wellness partnerships

---

## Slide 13: Demo Walkthrough

1) Landing page
2) Google sign‑in
3) AI chat
4) Bubble + mood
5) Insight + match
6) Schedule + confirm
7) Confirmation email + calendar
8) My Group page
9) Therapist dashboard

---

## Slide 14: What We Built

✅ Full frontend with warm, calming UI  
✅ Flask backend with REST API  
✅ Firebase Auth + Firestore storage  
✅ Gemini‑powered AI chat  
✅ Resend email + .ics calendar  
✅ Client “My Group” page  
✅ Therapist dashboard (role‑based)

---

## Slide 15: Competitive Advantage

- Warmer intake than traditional forms
- Lower friction than other mental health apps
- Group‑first matching with clear handoff
- Automated admin workflows

---

## Slide 16: Roadmap

**Next**
- Real payments (Stripe)
- Session reminders + follow‑ups
- Live calendar integrations
- Therapist role management UI

**Later**
- Multi‑language
- Video sessions
- Advanced outcome tracking

---

## Slide 17: Team & Ask

**Team**
- Mani — Full‑stack developer

**Ask**
- Mentorship + clinical feedback
- Early therapist partners
- Beta users

---

## Slide 18: Thank You

**Haven** — *A warm space for your mind to rest*

Contact:
- GitHub: github.com/yourname/haven
- Email: support@haven.mathengeinc.com
- Demo: haven.mathengeinc.com
