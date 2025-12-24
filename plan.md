# Search Results Pagination and Subpage Plan

## Goal
- Redirect users to `/search/{query}/{page}/` (e.g., `/search/abc/1/`) when searching.
- Display 20 results per page, fetched via JSON API.
- Populate the results page dynamically with JavaScript, not by showing raw JSON.

## Steps

### 1. Frontend Changes
- Update search button logic to redirect to `/search/{query}/1/`.
- Create a new HTML page or template for `/search/{query}/{page}/`.
- Add JavaScript to fetch results from `/results?search_query={query}&page={page}&per_page=20`.
- Render results in the DOM.
- Add pagination controls (Next/Previous) to navigate pages.
- Add a search form to the results page, with the current search term prepopulated, so users can search again directly from the results page.
- Add a category dropdown to the search form on the results page, using high-level group names (Movies, TV, Games, Music, Books, Software, Adult).
- Update search logic to include the selected category in the request and preselect the current category if set.

### 2. Backend Changes
- Add a new route `/search/{query}/{page}/` to serve the results page (HTML).
- Update `/results` API endpoint to accept `search_query`, `page`, and `per_page` parameters, and return paginated results as JSON.
- In the database query, use `LIMIT` and `OFFSET` for pagination.
- Update `/results` API endpoint to accept an optional `category` parameter (the high-level group name).
- Map the high-level category to the relevant `cat` values in the database query and filter results accordingly.

### 3. User Experience
- When visiting `/search/abc/1/`, the page loads and fetches results for `abc` page 1.
- Results are displayed dynamically.
- Pagination controls allow moving between pages.

### 4. Optional Enhancements
- Show loading indicators while fetching data.
- Display a message if no results are found.
- Highlight the current page in pagination controls.

---
This plan will be updated as progress is made or requirements change.
