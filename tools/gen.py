#!/usr/bin/env python3
"""Generates index.html for vesta-agent.github.io (English only). Run from repo root: python3 tools/gen.py"""
import json
S='https://vesta-agent.github.io/'
I={'voice':'<path d="M12 3a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3z"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
'eye':'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
'phone':'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
'group':'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 1.8 6 5"/>',
'mem':'<rect x="5" y="5" width="14" height="14" rx="3"/><path d="M9 9h6v6H9zM9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
'key':'<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.7 12.3 21 2M17 6l3 3M14 9l2 2"/>',
'send':'<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>',
'globe':'<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
'off':'<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
'lock':'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'}
DL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 3v12M6 10l6 6 6-6M4 20h16"/></svg>'
title='Vesta Agent - Personal AI Assistant for Windows, Android & Linux'
desc='Vesta Agent is a free personal AI assistant for Windows, Android and Linux with voice calls, screen vision, phone control, multi-agent group chat, Telegram, proxy support and memory that stays on your device.'
F=[('voice','Voice calls','Talk naturally and hear spoken replies. Share your screen mid-call and ask what is wrong.','w3','voice','Vesta Agent voice call screen'),
('eye','Screen vision','With your permission the agent sees your screen, explains it and helps you fix it.','w3','share','Vesta Agent chat while the agent can see the screen'),
('phone','Phone control','The agent taps, types and navigates on Android, even without a computer.','',None,None),
('group','Multi-agent group chat','Put specialised agents in one room and let them split the work.','',None,None),
('mem','Memory stored locally','Smart memory that lives only on your device. View, edit or wipe it at any time.','',None,None),
('key','Multi-key failover','Add several API keys per agent. When one runs out, the next one continues the same task.','w4','keys','Vesta Agent API keys settings'),
('send','Telegram','Connect your own bot or personal account and schedule messages.','',None,None),
('globe','Proxy for Iran','Real HTTP and SOCKS5 proxy per service, with a built-in step-by-step guide.','',None,None),
('off','Offline mode','Run entirely on your computer with Ollama. Nothing leaves the machine.','',None,None),
('lock','Privacy first','No accounts and no cloud database. Keys are encrypted on your device.','',None,None)]
G=[('chat','Chat','A real assistant, not a chatbot','Vesta Agent chat with a weekly plan'),
('group','Group chat','Agents working together','Group chat where Researcher, Server Ops and Writer split a task'),
('tools','Tools','Runs commands on your machine','Agent running tools and reporting the result'),
('share','Screen sharing','The agent sees what you see','Screen sharing indicator while chatting'),
('voice','Voice call','Hands-free conversation','Voice call screen'),
('store','Agents','Ready-made specialists','Agent store with ready-made agents'),
('telegram','Telegram','Bot or personal account','Telegram settings'),
('proxy','Proxy','Works where services are blocked','Proxy settings with per-service routing')]
PH=[('m-chat','Chat'),('m-group','Group chat'),('m-side','Agents'),('m-voice','Voice call')]
P=[('win','Windows 10 / 11','64-bit installer',['Run the installer.','If SmartScreen appears, click More info, then Run anyway.','Open Vesta Agent from the Start menu.']),
('win7','Windows 7 / 8','Legacy build for older PCs',['Run the installer.','If warned, click More info, then Run anyway.','Open Vesta Agent from the Start menu.']),
('android','Android','APK for phones and tablets',['Download the APK on your phone.','Allow installing from this source when asked.','Open the app and follow setup.']),
('deb','Linux .deb','Ubuntu, Debian, Mint',['Download the .deb file.','Run <code>sudo apt install ./VestaAgent-*.deb</code>','Launch it from your apps.']),
('appimage','Linux AppImage','Any distribution',['Download the AppImage.','Run <code>chmod +x VestaAgent-*.AppImage</code>','Double-click to start.'])]
Q=[('Is Vesta Agent free?','Yes. The app is free. You use your own AI key, for example a free Gemini or OpenRouter key, or run models offline with Ollama.'),
('Where is my data stored?','Only on your own device: chats, memory, agents, settings and encrypted keys. There is no Vesta server or online database.'),
('Does it work in Iran?','Yes. Add a proxy in Settings, for example the local port from v2rayN or NekoBox, and choose which services use it. A built-in guide shows each step.'),
('Which AI models does it support?','Gemini, OpenRouter, OpenAI-compatible providers and local models through Ollama.'),
('Will it update automatically?','Yes. It checks quietly at launch and only shows a window when a new version is available.'),
('Why does Windows show a blue warning?','The installer is not yet signed with a paid certificate. Click More info, then Run anyway.')]
ld={"@context":"https://schema.org","@type":"SoftwareApplication","name":"Vesta Agent","url":S,"image":S+"assets/og-image.png","screenshot":S+"assets/shots/chat.webp","description":desc,"applicationCategory":"ProductivityApplication","operatingSystem":"Windows 7, Windows 8, Windows 10, Windows 11, Android, Linux","softwareVersion":"1.4.0","inLanguage":"en","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"author":{"@type":"Organization","name":"Persian Studio","url":"https://github.com/Vesta-Agent"},"downloadUrl":"https://github.com/Vesta-Agent/vesta-agent-releases/releases/latest"}
fq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in Q]}
def tile(i,f):
  k,h,p,w,sh,alt=f
  fig=f'<figure><img src="assets/shots/{sh}.webp" alt="{alt}" width="1440" height="900" loading="lazy" decoding="async"></figure>' if sh else ''
  return f'<article class="tile rv {w}"><span class="num">{i+1:02d}</span><div class="ic"><svg viewBox="0 0 24 24" aria-hidden="true">{I[k]}</svg></div><h3>{h}</h3><p>{p}</p>{fig}</article>'
tiles=''.join(tile(i,f) for i,f in enumerate(F))
tabs=''.join(f'<button role="tab" aria-selected="{"true" if i==0 else "false"}">{a}<span>{b}</span></button>' for i,(k,a,b,c) in enumerate(G))
imgs=''.join(f'<img {"src" if i==0 else "data-src"}="assets/shots/{k}.webp" alt="{c}" width="1440" height="900" decoding="async"{" class=on" if i==0 else ""}>' for i,(k,a,b,c) in enumerate(G))
phones=''.join(f'<figure class="phone rv"><div class="s"><img src="assets/shots/{k}.webp" alt="Vesta Agent on Android: {n}" width="412" height="915" fetchpriority="low" decoding="async"></div><p>{n}</p></figure>' for k,n in PH)
plats=''.join(f'<article class="plat rv{" rec" if k=="win" else ""}"><h3>{h}</h3><small>{s}</small><ol>{"".join("<li>"+x+"</li>" for x in st)}</ol><a class="get" data-asset="{k}" href="https://github.com/Vesta-Agent/vesta-agent-releases/releases/latest" rel="nofollow">Download</a></article>' for k,h,s,st in P)
faq=''.join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q,a in Q)
html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="Vesta Agent, AI assistant, personal AI agent, desktop AI assistant, Android AI assistant, AI agent app, Gemini, OpenRouter, Ollama, Telegram AI bot, voice AI assistant, Persian Studio">
<!-- google-site-verification: paste the Google Search Console meta tag here, e.g. <meta name="google-site-verification" content="XXXX"> -->
<link rel="canonical" href="{S}">
<meta name="theme-color" content="#04060d">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="Vesta Agent">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{S}"><meta property="og:image" content="{S}assets/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{S}assets/og-image.png">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" href="assets/favicon-32.png"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Inter:wght@400;500;600&display=swap">
<link rel="preload" as="image" href="assets/logo-256.webp">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{json.dumps(ld)}</script>
<script type="application/ld+json">{json.dumps(fq)}</script>
</head>
<body>
<div class="glow" aria-hidden="true"><i></i><i></i></div><div class="noise" aria-hidden="true"></div>
<nav aria-label="Main"><a class="brand" href="./"><img src="assets/logo-256.webp" alt="" width="28" height="28">Vesta Agent</a>
<ul><li><a href="#features">Features</a></li><li><a href="#gallery">Gallery</a></li><li><a href="#download">Download</a></li><li><a href="#faq">FAQ</a></li><li><a href="#privacy">Privacy</a></li></ul>
<a class="pill" href="#download">Get the app</a></nav>
<main>
<header class="hero">
<div class="stage" aria-hidden="true"><div class="orb"></div><canvas id="gl"></canvas></div>
<div class="inner">
<img class="mark" src="assets/logo-256.webp" srcset="assets/logo-256.webp 1x, assets/logo-512.webp 2x" alt="Vesta Agent logo" width="84" height="84" fetchpriority="high">
<span class="eyebrow"><b></b>Personal AI assistant &middot; v<span data-ver>1.4.0</span></span>
<h1>Vesta Agent<br><span class="serif">works for you.</span></h1>
<p class="lede">Your own AI agent that talks, sees your screen, controls your phone and gets things done. Everything stays on your device.</p>
<div class="cta"><a class="btn dlbtn" href="#download">{DL}<span>Download <span class="os"></span></span></a><a class="btn alt" href="#gallery">See it in action</a></div>
<span class="ver">Free for Windows, Android and Linux &middot; Version <span data-ver>1.4.0</span></span>
</div><span class="scroll" aria-hidden="true"></span>
</header>
<section id="features"><div class="wrap"><div class="head rv"><span class="eyebrow"><b></b>Capabilities</span><h2>Everything an assistant <span class="serif">should</span> do.</h2><p>One app, powerful agents, and no servers of ours in between.</p></div><div class="bento">{tiles}</div></div></section>
<section id="gallery"><div class="wrap"><div class="head c rv"><span class="eyebrow"><b></b>Inside the app</span><h2>Designed to feel <span class="serif">calm.</span></h2><p>Real screens from Vesta Agent 1.4, shown with demo content.</p></div>
<div class="gallery rv"><div class="tabs" role="tablist" aria-label="Screens">{tabs}</div><div><div class="frame"><div class="bar" aria-hidden="true"><i></i><i></i><i></i></div><div class="scr">{imgs}</div></div><p class="cap" id="cap" aria-live="polite">{G[0][3]}</p></div></div>
<div class="phones">{phones}</div></div></section>
<section id="download"><div class="wrap"><div class="head c rv"><span class="eyebrow"><b></b>Download</span><h2>Free. Pick your <span class="serif">platform.</span></h2><p>Latest version: v<span data-ver>1.4.0</span>. Installs in under a minute.</p></div><div class="dl">{plats}</div>
<p class="cap" style="margin-top:28px"><a href="https://github.com/Vesta-Agent/vesta-agent-releases/releases" style="text-decoration:underline">All releases and SHA256 checksums</a></p></div></section>
<section id="faq"><div class="wrap"><div class="head c rv"><span class="eyebrow"><b></b>FAQ</span><h2>Questions, <span class="serif">answered.</span></h2></div><div class="faq">{faq}</div></div></section>
<section id="privacy"><div class="wrap"><div class="priv rv"><div><span class="eyebrow"><b></b>Privacy</span><h2>Your data <span class="serif">never</span> leaves home.</h2></div>
<ul><li>No Vesta servers and no online database. Chats, memory and settings live on your device.</li><li>API keys are encrypted locally. Passwords, keys and card details are never saved to memory.</li><li>Only the message you send goes to the AI provider whose key you added. With Ollama, nothing leaves at all.</li><li>A visible indicator is always on while the microphone or screen sharing is active.</li></ul></div></div></section>
<section class="final"><div class="wrap rv"><h2>Meet your <span class="serif">new agent.</span></h2><a class="btn dlbtn" href="#download">{DL}<span>Download <span class="os"></span></span></a></div></section>
</main>
<footer><div class="wrap"><span>Made by Persian Studio &middot; &copy; 2026</span><span><a href="https://github.com/Vesta-Agent/vesta-agent-releases">Releases on GitHub</a></span></div></footer>
<script src="assets/main.js" defer></script>
</body>
</html>
'''
open('index.html','w').write(html)
