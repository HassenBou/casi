import os,sys
sys.path.insert(0,os.path.dirname(__file__))
from data import *
os.chdir(os.path.join(os.path.dirname(__file__),'..'))
CHD={c[0]:c for c in CH}
KEY='<svg viewBox="0 0 24 48" fill="currentColor" aria-hidden="true"><path d="M12 0a8 8 0 0 0-2 15.7V44l2 4 2-4-2-2 3-2-3-2 3-2-3-2V15.7A8 8 0 0 0 12 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Z"/></svg>'
def head(t,d,body=''):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><meta name="theme-color" content="#0B0E14">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/tokens.css"><link rel="stylesheet" href="css/styles.css"><link rel="stylesheet" href="css/pages.css"></head>
<body{body}><canvas id="fx" aria-hidden="true"></canvas>
<header class="nav"><div class="wrap"><a href="index.html" aria-label="CaSi home"><img src="assets/logo.png" alt="CaSi"></a>
<nav><ul id="menu">{"".join(f'<li><a href="{h}">{n}</a></li>' for n,h in NAV)}</ul></nav>
<a class="btn sm" href="index.html#premiere">Watch trailer</a><button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu">☰</button></div></header>
<main id="top">'''
SOC=["Instagram","YouTube","TikTok","Facebook","X"]
def tail():
    return f'''</main>
<section class="pre"><div class="wrap pre-g">
<div><img class="pre-logo" src="assets/logo.png" alt="CaSi: The Secret Key Holder"><p class="hl">Inside Grandma’s sewing box, a crocheted cactus holds ten hidden Star Keys. Thirty midnights. One Shadow King. One house to protect.</p>
<a class="btn gold sm" href="index.html#premiere">Episode 01 · 14 April 2027</a></div>
<div><h4>Explore</h4><ul>{"".join(f'<li><a href="{h}">{n}</a></li>' for n,h in NAV)}</ul></div>
<div><h4>Follow the story</h4><ul class="soc">{"".join(f'<li><a href="#" aria-label="{s}">{s}</a></li>' for s in SOC)}</ul></div></div></section>
<footer><div class="wrap"><p>© 2027 CaSi Animation Series. All Rights Reserved.</p><ul><li><a href="privacy.html">Privacy Policy</a></li><li><a href="press-kit.html">Press Kit</a></li><li><a href="production-bible.html">Production Bible</a></li><li><a href="index.html#contact">Social Channels</a></li></ul></div></footer>
<script src="js/particles.js"></script><script src="js/main.js"></script></body></html>'''
def w(n,s): open(n,'w').write(s)
def ep(i):return f'ep-{i:02d}.html'
def card_ep(i):
    t=EPS[i-1][0];return f'<a class="mini" href="{ep(i)}"><img src="assets/eps/ep{i:02d}.jpg" alt="" loading="lazy"><span>Ep {i:02d}</span><b>{t}</b></a>'
# ---------- INDEX
slides="".join(f'''<article class="slide" id="s{i}"><img src="assets/eps/ep{i:02d}.jpg" alt="Episode {i} still: {t}" {'' if i==1 else 'loading="lazy"'} draggable="false"><div class="sh"></div>
<div class="st"><span class="big" aria-hidden="true">{i:02d}</span><h3>{t}</h3><p>{d}</p><a class="btn gold" href="{ep(i)}">Read episode {i:02d}</a></div></article>''' for i,(t,d,*_) in enumerate(EPS,1))
ticks="".join(f'<button aria-label="Episode {i}" data-i="{i-1}"></button>' for i in range(1,11))
cards="".join(f'''<a class="card" style="--c:{c}" href="char-{k}.html" data-r><img src="{'assets/chars/casi.jpg' if k=='casi' else img}" alt="{n}, {tg}" loading="lazy"><div class="tx"><h3>{n}</h3><div class="role">{r}</div><div class="tag">{tg}</div><p class="d">{d}</p><span class="more">Meet {n}</span></div></a>''' for k,n,r,tg,d,_b,c,_a,img in CH)
needles="".join(f'<line x1="{x}" y1="{y}" x2="{x+60}" y2="{y+900}" stroke="url(#ng)" stroke-width="2"/>' for x,y in [(80,-100),(330,-300),(980,-200),(1240,-80),(1500,-260)])
keys="".join(f'<span class="key" style="left:{x}%;top:{y}%;animation-delay:{d}s;scale:{s}">{KEY}</span>' for x,y,d,s in [(55,18,0,.8),(72,52,-2,1),(86,22,-4,.6),(48,66,-5,.7)])
tend='<path d="M-50 700C200 500 300 800 600 560S900 200 1200 420 1500 300 1700 120" fill="none" stroke="#6a3fb5" stroke-width="26" stroke-linecap="round" opacity=".6"/><path d="M-50 860C300 700 520 960 860 760S1300 560 1700 700" fill="none" stroke="#2b1b52" stroke-width="40" stroke-linecap="round"/>'
lore=[("The midnight pact","Every night at 12:00 the yarn wakes. Thirty nights is all CaSi has to train her allies and gather the keys.",1),("The Star Keys","Ten keys, each one holding a memory of the house. Each is hidden behind a trial of needle, thread or shadow.",4),("The Shadow King","He does not steal objects. He consumes memories, and the house forgets itself a little more each night.",7),("The 30th night","A clock with thirty notches guards the front door lock. When the last notch strikes, the lock opens or stays shut forever.",10)]
loreh="".join(f'<article class="lc" data-r><img src="assets/eps/ep{n:02d}.jpg" alt="" loading="lazy"><div><h3>{t}</h3><p>{d}</p><a href="{ep(n)}">See episode {n:02d}</a></div></article>' for t,d,n in lore)
ring="".join(f'<line x1="200" y1="6" x2="200" y2="{22 if k%5 else 36}" transform="rotate({k*12} 200 200)"/>' for k in range(30))
idx=head("CaSi: The Secret Key Holder | Season 1","A handcrafted hero. A 30-night pact. Ten hidden keys to protect the house from the Shadow King.")+f'''
<section class="hero" aria-label="CaSi hero"><div class="layer l-bg" data-speed=".2"></div>
<div class="layer l-tendril" data-speed=".35"><svg viewBox="0 0 1600 1000" preserveAspectRatio="none">{tend}</svg></div><div class="layer l-shade"></div>
<div class="layer l-needles" data-speed=".5"><svg viewBox="0 0 1600 1000" preserveAspectRatio="none"><defs><linearGradient id="ng" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>{needles}</svg>{keys}</div>
<div class="wrap hero-copy" data-speed="1"><span class="pill">Episode 01 arrives 14 April 2027</span><h1>When the clock strikes midnight, <span>the yarn awakens.</span></h1>
<p>A handcrafted hero. A 30-night pact. Ten hidden keys to protect the house from the Shadow King.</p>
<div class="cta"><a class="btn gold" href="#premiere">Watch teaser trailer</a><a class="btn green" href="#episodes">Discover Season 1</a></div></div><div class="hand" aria-hidden="true"><i>12</i></div></section>
<section class="sec legend" id="story"><div class="wrap"><div data-r><p class="kicker">The legend</p><h2>The 30-night midnight pact</h2>
<div class="pact"><div><strong>30</strong>nights of training</div><div><strong>10</strong>hidden Star Keys</div><div><strong>1</strong>Shadow King</div></div></div>
<div data-r><p>Tucked inside Grandma’s wooden sewing box lies a secret smaller than a thimble, yet stronger than iron. <b>CaSi</b>, a small crocheted cactus holding magical keys in her yellow yarn pot, must lead her sewing box allies through midnight training to recover the hidden Star Keys before the Shadow King consumes the home’s memories.</p></div></div></section>
<section class="sec champs" id="champions"><div class="wrap"><div class="head" data-r><p class="kicker">Meet the squad</p><h2>The sewing box champions</h2></div><div class="cards">{cards}</div></div></section>
<section class="reel" id="episodes" aria-roledescription="carousel" aria-label="Season 1 episodes"><div class="rhead"><p class="kicker">Ten episodes, ten keys</p><h2>Season 1: the revelation of the keys</h2></div>
<div class="rtrack" tabindex="0">{slides}</div>
<div class="rctrl"><div class="ticks">{ticks}</div><span class="cnt"><b>01</b> / 10</span><button id="prev" aria-label="Previous episode">←</button><button id="next" aria-label="Next episode">→</button></div></section>
<section class="sec lore" id="lore"><div class="wrap"><div class="lore-top"><div class="poster" data-r><img src="assets/poster.jpg" alt="CaSi: The Secret Key Holder poster, Season 1 coming soon" loading="lazy"></div>
<div data-r><p class="kicker">Key lore</p><h2>One key. A thousand secrets.</h2><p class="lead">Every door in the house hides a world, and every world is guarded by something that wants to keep it shut. CaSi does not carry keys to open doors. She carries them to remember what lives behind them.</p>
<blockquote>Every door hides a world.</blockquote></div></div><div class="lgrid">{loreh}</div></div></section>
<section class="sec prem" id="premiere"><div class="pbg"></div><div class="glow"></div>
<svg class="clock" viewBox="0 0 400 400" aria-hidden="true"><circle cx="200" cy="200" r="190" fill="none" stroke="currentColor" opacity=".35"/>{ring}</svg>
<div class="wrap"><p class="kicker">Season 1 · Episode 01: The Midnight Pact</p><h2 data-r>The midnight lock opens soon</h2><p class="date">Premiere: 14 April 2027</p>
<div class="timer" data-target="2027-04-14T00:00:00" role="timer" aria-label="Countdown to premiere"><div><b>00</b><span>Days</span></div><div><b>00</b><span>Hours</span></div><div><b>00</b><span>Mins</span></div><div><b>00</b><span>Secs</span></div></div>
<form class="vip js-form" novalidate><input type="email" required placeholder="Enter your email for episode stills and key lore" aria-label="Email address"><button class="btn gold" type="submit">Unlock exclusives</button></form><p class="note" role="status"></p></div></section>
<section class="sec contact" id="contact"><div class="wrap cg"><div data-r><p class="kicker">Contact</p><h2>Talk to Labinat Studio</h2><p class="lead">Press, partnerships, licensing or a message for the team behind CaSi. Tell us what you have in mind and we will reply.</p>
<p class="studio">Labinat Studio<br><span>Production company of CaSi: The Secret Key Holder</span></p></div>
<form class="cf js-form" novalidate data-r><label>Your name<input name="n" required autocomplete="name"></label><label>Email<input type="email" name="e" required autocomplete="email"></label>
<label class="full">Subject<select name="s"><option>Press and media</option><option>Partnership</option><option>Licensing and merchandise</option><option>Message for the team</option></select></label>
<label class="full">Message<textarea name="m" rows="5" required></textarea></label><button class="btn gold" type="submit">Send message</button><p class="note full" role="status"></p></form></div></section>'''+tail()
w('index.html',idx)
# ---------- EPISODES
for i,(t,d,syn,beats,chs,key) in enumerate(EPS,1):
    prev=card_ep(i-1) if i>1 else '<span></span>';nxt=card_ep(i+1) if i<10 else '<span></span>'
    date='Premiere: 14 April 2027' if i==1 else 'Release date coming soon'
    p=head(f"Episode {i:02d}: {t} | CaSi",d)+f'''<section class="phero" style="--bg:url(assets/eps/ep{i:02d}.jpg)"><div class="wrap"><a class="back" href="index.html#episodes">All episodes</a><span class="big" aria-hidden="true">{i:02d}</span><p class="kicker">Season 1 · Episode {i:02d}</p><h1>{t}</h1><p class="lead">{d}</p><span class="pill">{date}</span></div></section>
<section class="sec"><div class="wrap pg"><div data-r><h2>The story</h2><p class="lead">{syn}</p></div>
<aside data-r><h3>Key beats</h3><ul class="beats">{"".join(f"<li>{b}</li>" for b in beats)}</ul><h3>Champions in this episode</h3><div class="chips">{"".join(f'<a href="char-{c}.html">{CHD[c][1]}</a>' for c in chs)}</div><h3>Key recovered</h3><p class="keyf">{KEY}{key}</p></aside></div></section>
<section class="sec nxt"><div class="wrap nx">{prev}{nxt}</div></section>'''+tail()
    w(ep(i),p)
# ---------- CHARACTERS
for k,n,r,tg,d,bio,c,ab,img in CH:
    ap=[i for i,e in enumerate(EPS,1) if k in e[4]]
    others="".join(f'<a class="chip-l" href="char-{o[0]}.html" style="--c:{o[6]}">{o[1]}<span>{o[2]}</span></a>' for o in CH if o[0]!=k)
    cut=' class="cut"' if k=='casi' else ''
    p=head(f"{n}: {r} | CaSi",d)+f'''<section class="chero" style="--c:{c}"><div class="wrap cg2"><div><a class="back" href="index.html#champions">All champions</a><p class="kicker">{tg}</p><h1>{n}</h1><p class="role">{r}</p><p class="lead">{bio}</p></div>
<div class="portrait"><img{cut} src="{img}" alt="{n}, {tg}"></div></div></section>
<section class="sec"><div class="wrap"><h2 data-r>Signature abilities</h2><div class="abil">{"".join(f'<div class="ab" data-r><h3>{a}</h3><p>{b}</p></div>' for a,b in ab)}</div></div></section>
<section class="sec"><div class="wrap"><h2 data-r>Appears in</h2><div class="minis">{"".join(card_ep(i) for i in ap)}</div></div></section>
<section class="sec"><div class="wrap"><h2 data-r>Fellow champions</h2><div class="others">{others}</div></div></section>'''+tail()
    w(f'char-{k}.html',p)
# ---------- INFO PAGES
def info(f,t,sub,body):
    w(f,head(f"{t} | CaSi",sub)+f'<section class="phero small"><div class="wrap"><a class="back" href="index.html">Home</a><h1>{t}</h1><p class="lead">{sub}</p></div></section><section class="sec"><div class="wrap doc">{body}</div></section>'+tail())
info('privacy.html','Privacy Policy','How the CaSi website handles your information.','<h2>What we collect</h2><p>When you join the VIP list or write to Labinat Studio, we receive the details you enter: your name, email address and message.</p><h2>How we use it</h2><p>We use your email to send episode stills and key lore, and to answer your messages. We do not sell your information.</p><h2>Your choices</h2><p>You can ask us to remove your details at any time through the contact form.</p>')
info('press-kit.html','Press Kit','Facts and assets for media covering CaSi.','<h2>Logline</h2><p>A handcrafted hero. A 30-night pact. Ten hidden keys to protect the house from the Shadow King.</p><h2>Quick facts</h2><ul class="beats"><li>Title: CaSi: The Secret Key Holder</li><li>Production company: Labinat Studio</li><li>Season 1: ten episodes, “The Revelation of the Keys”</li><li>Episode 01 premiere: 14 April 2027</li></ul><h2>Assets</h2><div class="chips"><a href="assets/poster.jpg" download>Poster</a><a href="assets/logo.png" download>Logo</a><a href="assets/hero.jpg" download>Key art</a></div><h2>Press contact</h2><p>Use the <a href="index.html#contact">contact form</a> and choose “Press and media”.</p>')
info('production-bible.html','Production Bible','The rules of the world of CaSi.','<h2>The world</h2><p>Grandma’s wooden sewing box. At midnight its tools come alive and the house’s memories become something worth protecting.</p><h2>The structure</h2><p>Thirty nights, ten Star Keys, one Shadow King. Season 1 follows one key per episode, ending on the thirtieth night at the front door lock.</p><h2>Tone</h2><p>Handcrafted and warm at the centre, dark and mysterious at the edges. Yarn, thread and gold light against deep midnight blue.</p><h2>Palette</h2><div class="chips"><a>Midnight Abyss #0B0E14</a><a>Starlight Gold #FFD700</a><a>Cactus Green #2E7D32</a><a>Pot Yellow #F4C430</a><a>Pin Red #E53935</a></div>')
print('built')
