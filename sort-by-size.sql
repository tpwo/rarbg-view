SELECT magnet_links.size,
       magnetLink
FROM magnet_links
INNER JOIN items ON items.id = magnet_links.id
WHERE items.cat IS NOT 'xxx'
  AND items.title LIKE '%twin%peaks%'
ORDER BY items.size ASC;
