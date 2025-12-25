


# UI Improvement Plan for RareTide

## Goals

- Make the search form visually appealing and user-friendly
- Present search results in a modern, readable, and responsive layout
- Ensure consistent, attractive styling across all pages
- Improve usability on both desktop and mobile

## 1. Search Menu Improvements

- Place the search form in a card or panel with padding and a subtle background
- Use larger, rounded input fields and dropdowns
- Add a search icon button (SVG or Unicode) for visual clarity
- Align form elements horizontally on desktop, stack vertically on mobile
- Add spacing between form elements
- Use a modern, clean font (e.g., system-ui, Inter, Roboto)

## 2. Search Results Improvements

- Display results in a card or list group with padding and hover effects
- Show the title prominently, with category as a colored badge and date in muted text
- Use alternating row backgrounds or dividers for readability
- Add a loading spinner instead of plain text
- Make the results area responsive and easy to scan

## 3. General Styling

- Use a soft, modern color palette (light backgrounds, accent colors for buttons/badges)
- Add more whitespace and padding throughout
- Make the site fully responsive (media queries for mobile)
- Use CSS variables for easy theme adjustments
- Add subtle transitions for interactive elements (buttons, hover states)

## 4. Implementation Steps

1. **Design**: Sketch or wireframe the new UI (optional, can use Figma or pen & paper)

2. **CSS Refactor**:
	- Create or update `static/styles.css` with new styles for form, results, and layout
	- Use CSS variables for colors, spacing, and fonts
	- Add responsive breakpoints

3. **HTML Template Update**:
	- Update `templates/search.html` to use semantic HTML and new class names
	- Add structure for badges, cards, and spinner

4. **JS Update**:
	- Update `static/script.js` to render results with new HTML structure
	- Add spinner logic for loading state

5. **Testing**:
	- Test on desktop and mobile browsers
	- Adjust styles for accessibility (contrast, focus states)

6. **Polish**:
	- Refine spacing, colors, and transitions

## 5. Optional Enhancements

- Add dark mode toggle
- Animate search results on load
- Add icons for categories
- Show result count and search summary

---
This plan will guide a step-by-step UI overhaul for a modern, user-friendly RareTide experience.
