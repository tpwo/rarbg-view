
# Plan: Rebuild HTML Flow with Jinja2 Templates and Shared Components

## Goal
Create a maintainable, DRY HTML flow using Jinja2 templates in FastAPI, with shared components (e.g., top bar, favicon, footer) injected into all pages. Avoid copy-pasting and enable easy UI changes across the app.

## Steps

### 1. Project Structure
- Create a `templates/` directory for Jinja2 HTML templates.
- Move all HTML files (search, results, etc.) into `templates/`.
- Create shared template components:
	- `base.html`: Main layout with favicon, header/top bar (page name), and footer.
	- `header.html`, `footer.html`: For easy inclusion in multiple pages.

### 2. Template Inheritance & Includes
- Use Jinja2 `{% extends 'base.html' %}` in all page templates.
- Use `{% include 'header.html' %}` and `{% include 'footer.html' %}` for shared sections.
- Place page-specific content in `{% block content %}{% endblock %}`.

### 3. FastAPI Integration
- Install Jinja2 and use `Jinja2Templates` in FastAPI.
- Update all routes to return `TemplateResponse` with the appropriate template and context.
- Serve `/` and `/search/{query}/{page}/` using the same main template, with dynamic content based on context.

### 4. JavaScript & Dynamic Content
- Keep JS and CSS in `static/` and link in `base.html`.
- Use JS to handle search, pagination, and results rendering as before.
- Pass initial context (e.g., search term, category) from FastAPI to the template for pre-filling forms.

### 5. User Experience
- The user always sees a consistent UI, whether on the main page or search results.
- All shared elements (header, favicon, footer) are managed in one place.
- Future UI changes require editing only the shared templates.

---
This plan will be updated as progress is made or requirements change.
