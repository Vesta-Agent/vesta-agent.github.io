#!/usr/bin/env python3
"""Builds translated copies of the site into /<lang>/... from tools/i18n/<lang>.txt
(one line per entry of tools/i18n/strings.json). Run from repo root after tools/gen.py:
    python3 tools/i18n.py"""
import json, os, re, sys
from bs4 import BeautifulSoup, NavigableString, Comment
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'tools', 'i18n')
SITE = 'https://vesta-agent.github.io'
LANGS = {'en':'English','fa':'فارسی','ar':'العربية','tr':'Türkçe','de':'Deutsch','fr':'Français','es':'Español','ru':'Русский','zh':'中文','hi':'हिन्दी'}
RTL = {'fa','ar'}
PAGES = ['', 'download/', 'faq/', 'features/', 'privacy/', 'screenshots/', 'support/']
ATTRS = ('alt','title','aria-label','placeholder')
SKIP_PREFIX = ('/assets', '/favicon', '/site.webmanifest', '/robots', '/sitemap')

def load():
    src = json.load(open(os.path.join(D, 'strings.json'), encoding='utf-8'))
    tr = {}
    for l in LANGS:
        if l == 'en': continue
        lines = open(os.path.join(D, l + '.txt'), encoding='utf-8').read().rstrip('\n').split('\n')
        if len(lines) != len(src):
            sys.exit(f'{l}.txt has {len(lines)} lines, expected {len(src)}')
        tr[l] = {s.strip(): t for s, t in zip(src, lines) if s.strip() and t.strip()}
    return tr

def sub(m, s):
    k = s.strip()
    if k in m:
        lead = s[:len(s) - len(s.lstrip())]; trail = s[len(s.rstrip()):]
        return lead + m[k] + trail
    return s

def local(href, lang):
    if not href.startswith('/') or href.startswith('//') or href.startswith(SKIP_PREFIX): return href
    return '/' + lang + href

def head_extras(soup, page, lang):
    head = soup.head
    for t in head.select('link[hreflang]'): t.decompose()
    for l in LANGS:
        a = soup.new_tag('link', rel='alternate', hreflang=l, href=f'{SITE}/{"" if l=="en" else l+"/"}{page}')
        head.append(a)
    head.append(soup.new_tag('link', rel='alternate', hreflang='x-default', href=f'{SITE}/{page}'))
    for t in head.select('link[rel=canonical]'):
        t['href'] = f'{SITE}/{"" if lang=="en" else lang+"/"}{page}'
    for t in head.select('meta[property="og:url"]'):
        t['content'] = f'{SITE}/{"" if lang=="en" else lang+"/"}{page}'
    for t in soup.select('#va-langs, #va-langdetect, #va-langcss'): t.decompose()
    css = soup.new_tag('style', id='va-langcss')
    css.string = ('#va-langs{position:fixed;bottom:14px;inset-inline-end:14px;z-index:60;font:13px system-ui;'
                  'background:rgba(20,22,30,.82);color:#fff;border:1px solid rgba(255,255,255,.18);border-radius:10px;'
                  'padding:6px 8px;backdrop-filter:blur(8px)}#va-langs option{color:#000}')
    head.append(css)
    if lang == 'en':
        s = soup.new_tag('script', id='va-langdetect')
        s.string = ("(function(){try{if(localStorage.getItem('va_lang'))return;var L=" + json.dumps([l for l in LANGS if l!='en']) +
                    ",n=(navigator.languages||[navigator.language||'']).map(function(x){return(x||'').slice(0,2).toLowerCase()});"
                    "localStorage.setItem('va_lang','auto');for(var i=0;i<n.length;i++){if(n[i]==='en')return;if(L.indexOf(n[i])>=0){"
                    "location.replace('/'+n[i]+location.pathname+location.search+location.hash);return}}}catch(e){}})();")
        head.insert(0, s)

def switcher(soup, page, lang):
    sel = soup.new_tag('select', id='va-langs'); sel['aria-label'] = 'Language'
    sel['onchange'] = "try{localStorage.setItem('va_lang',this.value)}catch(e){};location.href=this.selectedOptions[0].dataset.u"
    for l, name in LANGS.items():
        o = soup.new_tag('option', value=l); o['data-u'] = f'/{"" if l=="en" else l+"/"}{page}'; o.string = name
        if l == lang: o['selected'] = ''
        sel.append(o)
    soup.body.append(sel)

def build(page, lang, m):
    src = os.path.join(ROOT, page, 'index.html')
    soup = BeautifulSoup(open(src, encoding='utf-8').read(), 'html.parser')
    if lang != 'en':
        for node in soup.find_all(string=True):
            if isinstance(node, Comment) or node.parent.name in ('script', 'style'): continue
            new = sub(m, str(node))
            if new != str(node): node.replace_with(NavigableString(new))
        for t in soup.find_all(True):
            for a in ATTRS:
                if t.has_attr(a): t[a] = sub(m, t[a])
            if t.name == 'meta' and t.has_attr('content') and (t.get('name') in ('description','twitter:title','twitter:description') or (t.get('property') or '').startswith('og:')):
                t['content'] = sub(m, t['content'])
            if t.name == 'a' and t.has_attr('href'): t['href'] = local(t['href'], lang)
        soup.html['lang'] = lang
        soup.html['dir'] = 'rtl' if lang in RTL else 'ltr'
    head_extras(soup, page, lang)
    switcher(soup, page, lang)
    out = src if lang == 'en' else os.path.join(ROOT, lang, page, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    html = str(soup)
    if not html.lstrip().lower().startswith('<!doctype'): html = '<!DOCTYPE html>\n' + html
    open(out, 'w', encoding='utf-8').write(html)
    return out

def sitemap():
    rows = []
    for p in PAGES:
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}/{"" if l=="en" else l+"/"}{p}"/>' for l in LANGS)
        for l in LANGS:
            rows.append(f'<url><loc>{SITE}/{"" if l=="en" else l+"/"}{p}</loc>{alts}</url>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')

if __name__ == '__main__':
    tr = load()
    for p in PAGES:
        for l in LANGS:
            if l != 'en': build(p, l, tr[l])
    for p in PAGES: build(p, 'en', {})   # English last so translated copies read the clean source
    sitemap()
    print('ok', len(PAGES) * len(LANGS), 'pages')
