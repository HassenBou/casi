const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const calm=matchMedia('(prefers-reduced-motion:reduce)').matches;

/* nav, parallax, midnight hand */
const nav=$('.nav'),layers=$$('[data-speed]'),hand=$('.hand'),hero=$('.hero');let tk=false;
function frame(){const y=scrollY;nav.classList.toggle('stuck',y>40);
  if(!calm&&hero&&y<innerHeight*1.4)layers.forEach(l=>l.style.transform=`translate3d(0,${y*l.dataset.speed*.4}px,0)`);
  hand&&hero&&hand.style.setProperty('--p',Math.min(1,y/hero.offsetHeight));tk=false}
addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(frame)}},{passive:true});frame();

/* mobile menu */
const burger=$('.burger'),menu=$('#menu');
burger.onclick=()=>burger.setAttribute('aria-expanded',menu.classList.toggle('open'));
$$('#menu a').forEach(a=>a.addEventListener('click',()=>{menu.classList.remove('open');burger.setAttribute('aria-expanded',false)}));

/* reveal + active link (home page) */
const io=new IntersectionObserver(e=>e.forEach(x=>x.isIntersecting&&(x.target.classList.add('in'),io.unobserve(x.target))),{threshold:.12});
$$('[data-r]').forEach(el=>io.observe(el));
const links=$$('#menu a'),secs=$$('main section[id]');
if(secs.length){const so=new IntersectionObserver(e=>e.forEach(x=>{if(x.isIntersecting)links.forEach(l=>l.classList.toggle('on',l.getAttribute('href').endsWith('#'+x.target.id)))}),{rootMargin:'-45% 0px -50%'});secs.forEach(s=>so.observe(s))}

/* champion card tilt */
$$('.card').forEach(c=>{
  c.onmousemove=e=>{if(calm)return;const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(900px) rotateY(${x*9}deg) rotateX(${-y*9}deg) translateY(-6px)`};
  c.onmouseleave=()=>c.style.transform=''});

/* full-screen episode reel */
const rt=$('.rtrack');
if(rt){
  const tick=$$('.ticks button'),cnt=$('.cnt b');let cur=0;
  const go=i=>rt.scrollTo({left:Math.max(0,Math.min(9,i))*rt.clientWidth,behavior:calm?'auto':'smooth'});
  rt.addEventListener('scroll',()=>{const i=Math.round(rt.scrollLeft/rt.clientWidth);if(i!==cur){cur=i;tick.forEach((t,k)=>t.classList.toggle('on',k===i));cnt.textContent=String(i+1).padStart(2,'0')}},{passive:true});
  tick.forEach((t,k)=>{t.onclick=()=>go(k);t.classList.toggle('on',!k)});
  $('#prev').onclick=()=>go(cur-1);$('#next').onclick=()=>go(cur+1);
  rt.onkeydown=e=>{if(e.key==='ArrowRight')go(cur+1);if(e.key==='ArrowLeft')go(cur-1)};
  let dn=false,sx=0,sl=0;
  rt.onpointerdown=e=>{if(e.pointerType==='mouse'&&!e.target.closest('a')){dn=true;sx=e.clientX;sl=rt.scrollLeft;rt.style.scrollSnapType='none'}};
  addEventListener('pointermove',e=>{if(dn)rt.scrollLeft=sl-(e.clientX-sx)});
  addEventListener('pointerup',()=>{if(dn){dn=false;rt.style.scrollSnapType='';go(Math.round(rt.scrollLeft/rt.clientWidth))}});
}

/* countdown */
const tm=$('.timer');
if(tm){const t0=new Date(tm.dataset.target).getTime(),cs=$$('b',tm),pad=n=>String(n).padStart(2,'0');
  const t=()=>{const d=Math.max(0,t0-Date.now())/1000;[d/86400,d%86400/3600,d%3600/60,d%60].forEach((v,i)=>cs[i].textContent=pad(Math.floor(v)))};t();setInterval(t,1000)}

/* forms (front-end only: connect to your email service) */
$$('.js-form').forEach(f=>f.onsubmit=e=>{e.preventDefault();const n=$('.note',f.parentElement.contains($('.note',f))?f:f.parentElement);
  const bad=$$('[required]',f).find(i=>!i.checkValidity());
  if(bad){n.style.color='#ff8a80';n.textContent=bad.type==='email'?'Enter a valid email address, like name@example.com.':'Please fill in the highlighted field.';bad.focus();return}
  n.style.color='';n.textContent=f.classList.contains('cf')?'Message sent. Labinat Studio will reply soon.':'Unlocked. Watch your inbox for the first key.';f.reset()});
