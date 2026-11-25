/* Drifting golden dust and yarn-coloured fireflies, shared by every page */
(()=>{
  const c=document.getElementById('fx');if(!c||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  const x=c.getContext('2d'),cols=['255,215,0','255,215,0','255,235,150','244,196,48','123,209,127','229,57,53','232,127,162'];
  let W,H,P=[],m={x:-999,y:-999},run=true;
  const mk=(init)=>({x:Math.random()*W,y:init?Math.random()*H:H+10,r:Math.random()*2.2+.5,v:Math.random()*.4+.12,s:Math.random()*6.28,k:Math.random()*.02+.005,c:cols[Math.random()*cols.length|0],a:Math.random()*.6+.25,dx:0});
  function size(){const d=Math.min(devicePixelRatio||1,2);W=innerWidth;H=innerHeight;c.width=W*d;c.height=H*d;x.setTransform(d,0,0,d,0,0);P=Array.from({length:Math.min(80,W*H/16000|0)},()=>mk(true))}
  addEventListener('resize',size);addEventListener('pointermove',e=>{m.x=e.clientX;m.y=e.clientY},{passive:true});
  document.addEventListener('visibilitychange',()=>{run=!document.hidden;run&&loop()});
  function loop(){
    if(!run)return;x.clearRect(0,0,W,H);
    for(const p of P){
      p.s+=p.k;p.y-=p.v;p.x+=Math.sin(p.s)*.35+p.dx;
      const ddx=p.x-m.x,ddy=p.y-m.y,d=Math.hypot(ddx,ddy);if(d<110){p.dx+=ddx/d*.08}p.dx*=.96;
      if(p.y<-10||p.x<-20||p.x>W+20)Object.assign(p,mk(false));
      const al=p.a*(.55+.45*Math.sin(p.s*3));
      x.fillStyle=`rgba(${p.c},${al*.18})`;x.beginPath();x.arc(p.x,p.y,p.r*4,0,6.28);x.fill();
      x.fillStyle=`rgba(${p.c},${al})`;x.beginPath();x.arc(p.x,p.y,p.r,0,6.28);x.fill();
    }
    requestAnimationFrame(loop);
  }
  size();loop();
})();
