# CareerVerse API (Backend)

FastAPI backend for CareerVerse. **No external database required** - data
lives in an in-memory store that's seeded automatically on startup.

## Local Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # set a JWT_SECRET_KEY, admin credentials, etc.
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for interactive Swagger docs.

On first startup, the app automatically:
- Loads all 16 careers from `app/data/careers_data.py` into memory
- Creates an admin account using `ADMIN_EMAIL` / `ADMIN_PASSWORD` from your `.env`

You can log in immediately with those admin credentials to access `/api/admin/*`.

## How Data Storage Works

`app/database.py` implements a small in-memory data layer (`Store` /
`Collection` / `Cursor`) that mimics the handful of MongoDB/Motor operations
this app uses (`find_one`, `find`, `insert_one`, `update_one`, `delete_one`,
`count_documents`, `distinct`, `aggregate`). Router code reads almost
identically to a "real" database-backed app.

- **While the server is running**, all reads/writes happen against Python
  dicts in memory - fast, and no setup required.
- **Best-effort persistence**: after every write, the full store is dumped
  to `backend/data_store.json`. On the next `uvicorn` startup, that file is
  reloaded if present, so local restarts don't lose your data.
- **On typical free-tier hosts** (e.g. Render's free web service) the
  filesystem is ephemeral - it survives while the instance is awake and
  sleeping/waking, but resets on a redeploy or dyno restart. In practice
  that means: great for demos, evaluation, and personal use; for guaranteed
  durability at scale, see "Swapping in a real database" below.

To wipe all data and start fresh (users, saved careers, study plans, chat
history - not the seeded careers, which reload automatically):
```bash
python -m scripts.reset_data
```

## Project Structure

```
backend/
  app/
    main.py              # FastAPI app + router registration + startup seeding
    config.py             # env-based settings (JWT secret, CORS, admin creds)
    database.py            # in-memory data store (Store/Collection/Cursor)
    auth/                  # JWT + password hashing + auth dependencies
    schemas/                # Pydantic request/response models
    routers/                 # one file per resource (auth, careers, chat, admin, ...)
    data/careers_data.py      # seed content - add new careers here
    utils/                     # recommendation engine + chat engine
  scripts/reset_data.py         # wipes data_store.json for a clean slate
  requirements.txt
  .env.example
```

## Adding a New Career

Add a new dict to `CAREERS` in `app/data/careers_data.py` following the
existing schema, then restart the server (or delete `data_store.json` and
restart, if you've since made local changes you want to discard). It
immediately shows up in the explorer, guidance engine, comparison tool, and
chat assistant - no other code changes required.

Admins can also add/edit/delete careers live via `POST/PUT/DELETE
/api/admin/careers` while the server is running.

## Environment Variables

See `.env.example`:
- `JWT_SECRET_KEY` - a long random string (e.g. `openssl rand -hex 32`)
- `CORS_ORIGINS` - comma-separated list of allowed frontend origins
- `ADMIN_EMAIL` / `ADMIN_PASSWORD` - bootstrapped automatically on first run
- `ANTHROPIC_API_KEY` (optional) - enables open-ended AI Assistant conversation

## Deployment (Render)

1. Push this repo to GitHub.
2. On Render: **New → Web Service**, connect the repo, set root directory to `backend`.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add the environment variables from `.env.example` in Render's dashboard.
6. Deploy - that's it. No database provisioning step needed.

## Swapping in a Real Database Later

If you outgrow the in-memory store (need durability across redeploys,
multiple server instances, etc.), the router layer was written against a
Mongo-like interface on purpose. To move to MongoDB Atlas:
1. `pip install motor pymongo` and add them to `requirements.txt`.
2. Replace the body of `app/database.py` with a Motor-backed `Database`
   class exposing the same collection attribute names.
3. Router files won't need changes beyond removing the `Database` type hint
   import if you rename it.

## AI Assistant Notes

The `/api/chat/message` endpoint ships with a fast, free, rule-based response
engine (`app/utils/chat_engine.py`) that answers from the in-memory careers
data - no external API key required. If you set an `ANTHROPIC_API_KEY`
environment variable, it will automatically use the Anthropic API for more
open-ended conversation instead, falling back to the rule-based engine if the
call fails or the key isn't set.
