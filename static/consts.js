export const PER_PAGE_OPTIONS = [20, 40, 100];

export const CATEGORY_SETS = {
  Movies: new Set([
    'movies',
    'movies_bd_full',
    'movies_bd_remux',
    'movies_x264',
    'movies_x264_3d',
    'movies_x264_4k',
    'movies_x264_720',
    'movies_x265',
    'movies_x265_4k',
    'movies_x265_4k_hdr',
    'movies_xvid',
    'movies_xvid_720',
  ]),
  TV: new Set(['tv', 'tv_sd', 'tv_uhd']),
  Games: new Set(['games_pc_iso', 'games_pc_rip', 'games_ps3', 'games_ps4', 'games_xbox360']),
  Music: new Set(['music_flac', 'music_mp3']),
  Books: new Set(['ebooks']),
  Software: new Set(['software_pc_iso']),
  Adult: new Set(['xxx']),
};

export const CATEGORY_ICNOS = {
  Movies: '<i class="bi bi-film" title="Movies"></i>',
  TV: '<i class="bi bi-tv" title="TV"></i>',
  Games: '<i class="bi bi-controller" title="Games"></i>',
  Music: '<i class="bi bi-music-note-beamed" title="Music"></i>',
  Books: '<i class="bi bi-book" title="Books"></i>',
  Software: '<i class="bi bi-cpu" title="Software"></i>',
  Adult: '<i class="bi bi-person-video" title="Adult"></i>',
  Other: '<i class="bi bi-folder" title="Other"></i>',
};

export const SORT_ICONS = {
  asc: '▲',
  desc: '▼',
  none: '',
};
