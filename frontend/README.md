# CareerVerse Frontend

React + Vite + plain CSS frontend for CareerVerse.

## Local Setup

```bash
cd frontend
npm install
cp .env.example .env      # set VITE_API_BASE_URL to your backend URL
npm run dev
```

Visit `http://localhost:5173`.

## Project Structure

```
frontend/
  src/
    components/     # Navbar, CareerCard, Icon, ProtectedRoute, etc.
    pages/          # one file per route
    context/        # AuthContext, ThemeContext, ToastContext
    services/api.js # Axios instance with JWT + auto-refresh interceptors
    styles/theme.css # design system (colors, spacing, components)
```

## Build

```bash
npm run build   # outputs to dist/
npm run preview # preview the production build locally
```

## Deployment (Vercel)

1. Push this repo to GitHub.
2. On Vercel: **New Project**, import the repo, set root directory to `frontend`.
3. Framework preset: Vite. Build command: `npm run build`. Output directory: `dist`.
4. Add environment variable `VITE_API_BASE_URL` pointing to your deployed Render backend URL.
5. Deploy.

## Notes

- Auth tokens are stored in `localStorage` (`cv_access_token` / `cv_refresh_token`); the Axios interceptor auto-refreshes on 401s.
- Dark mode toggles a `data-theme` attribute on `<html>`; all colors are CSS variables in `src/styles/theme.css`.
- No component library / Tailwind is used, per the project spec - all styling is plain CSS co-located per page/component.
