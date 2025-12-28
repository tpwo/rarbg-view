import { CATEGORY_SETS } from './consts.js';

export function show(el) {
  if (!el) return;
  try {
    el.classList.remove('hidden');
  } catch (_e) {}
  try {
    el.style.display = '';
  } catch (_e) {}
}

export function hide(el) {
  if (!el) return;
  try {
    el.classList.add('hidden');
  } catch (_e) {}
  try {
    el.style.display = 'none';
  } catch (_e) {}
}

export function getTopLevelCategory(cat) {
  for (const [top, subs] of Object.entries(CATEGORY_SETS)) {
    if (subs.has(cat)) return top;
  }
  return 'Other';
}

export function humanReadableSize(size) {
  if (typeof size !== 'number' || Number.isNaN(size) || size === 0) return 'N/A';
  if (size < 1000) return `${size} B`;
  const units = ['KB', 'MB', 'GB', 'TB'];
  let unit = -1;
  do {
    size = size / 1000;
    unit++;
  } while (size >= 1000 && unit < units.length - 1);
  return `${size.toFixed(2)} ${units[unit]}`;
}

export function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
