// Pre-renders the 120 prompts into 120-prompts.html as static HTML, so search engines
// and AI crawlers that don't run JavaScript can read them. Run after editing PROMPT_DATA:
//   node _tools/render_120_prompts.js
const fs = require('fs'), path = require('path');
const file = path.join(__dirname, '..', '120-prompts.html');
let src = fs.readFileSync(file, 'utf8');
const m = src.match(/var PROMPT_DATA = (\[[\s\S]*?\n\]);/);
if (!m) throw new Error('PROMPT_DATA not found');
const data = Function('"use strict"; return ' + m[1])();
let html = '', total = 0;
for (const cat of data) {
  total += cat.prompts.length;
  const items = cat.prompts.map(p => '<div class="prompt-item"><div class="prompt-title">' + p[0] + '</div><div class="prompt-text">' + p[1] + '</div></div>').join('');
  html += '<div class="cat-card" id="cat-' + cat.id + '">' +
    '<button class="cat-header" data-cat="' + cat.id + '">' +
      '<div class="cat-icon">' + cat.icon + '</div>' +
      '<div><div class="cat-title">' + cat.title + '</div><div class="cat-count">' + cat.prompts.length + ' prompts</div></div>' +
      '<div class="cat-chevron">⌄</div>' +
    '</button>' +
    '<div class="cat-body">' + items + '</div>' +
  '</div>\n';
}
const re = /<div class="cat-grid" id="cat-grid">[\s\S]*?<!-- \/cat-grid -->|<div class="cat-grid" id="cat-grid"><\/div>/;
if (!re.test(src)) throw new Error('cat-grid container not found');
src = src.replace(re, () => '<div class="cat-grid" id="cat-grid">\n' + html + '</div><!-- /cat-grid -->');
// Keep the static markup on load instead of re-rendering it (no flicker, same DOM).
src = src.replace("  grid.innerHTML = html;", "  if (!grid.querySelector('.cat-card')) grid.innerHTML = html;");
fs.writeFileSync(file, src);
console.log('rendered', data.length, 'categories,', total, 'prompts');
