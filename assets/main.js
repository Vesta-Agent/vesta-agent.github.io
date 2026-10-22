(function(){
var R='https://github.com/Vesta-Agent/vesta-agent-releases/releases/latest/download/';
var A={win:R+'VestaAgent-1.8.0-windows-x64-setup.exe',win7:R+'VestaAgent-1.8.0-windows7-8-legacy-setup.exe',android:R+'VestaAgent-1.8.0-android.apk',deb:'https://github.com/Vesta-Agent/vesta-agent-releases/releases/download/v1.4.1/VestaAgent-1.4.1-linux-amd64.deb',appimage:'https://github.com/Vesta-Agent/vesta-agent-releases/releases/download/v1.4.1/VestaAgent-1.4.1-linux-x86_64.AppImage'};
var N={win:'Windows',win7:'Windows 7/8',android:'Android',deb:'Linux',appimage:'Linux'},ver='1.8.0';
var F={en:'for {os}',fa:'برای {os}',ar:'لنظام {os}',tr:'{os} için',de:'für {os}',fr:'pour {os}',es:'para {os}',ru:'для {os}',zh:'{os} 版',hi:'{os} के लिए'};
function apply(){document.querySelectorAll('[data-asset]').forEach(function(a){a.href=A[a.dataset.asset]});
 document.querySelectorAll('[data-ver]').forEach(function(e){e.textContent=ver});
 var u=navigator.userAgent,k='win';
 if(/Android/i.test(u))k='android';else if(/Windows NT 6\.[0-3]/.test(u))k='win7';else if(/Windows/.test(u))k='win';else if(/iPhone|iPad|Macintosh/.test(u))k=null;else if(/Linux|X11/.test(u))k='deb';
 document.querySelectorAll('.dlbtn').forEach(function(b){var t=b.querySelector('.os');if(k){b.href=A[k];t.textContent=(F[(document.documentElement.lang||'en').slice(0,2)]||F.en).replace('{os}',N[k])}else{b.href='#download';t.textContent=''}})}
apply();
fetch('https://api.github.com/repos/Vesta-Agent/vesta-agent-releases/releases/latest').then(function(r){return r.ok?r.json():null}).then(function(j){if(!j)return;ver=j.tag_name.replace(/^v/,'');
 (j.assets||[]).forEach(function(x){var m=x.name;if(/windows-x64-setup\.exe$/.test(m))A.win=R+m;else if(/windows7-8.*\.exe$/.test(m))A.win7=R+m;else if(/\.apk$/.test(m))A.android=R+m;else if(/\.deb$/.test(m))A.deb=R+m;else if(/\.AppImage$/.test(m))A.appimage=R+m});apply()}).catch(function(){});
var rv=document.querySelectorAll('.rv');
if('IntersectionObserver' in window){var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');o.unobserve(e.target)}})},{threshold:.1});rv.forEach(function(e){o.observe(e)})}else rv.forEach(function(e){e.classList.add('in')});
document.querySelectorAll('.tile').forEach(function(t){t.addEventListener('pointermove',function(e){var r=t.getBoundingClientRect();t.style.setProperty('--x',(e.clientX-r.left)+'px');t.style.setProperty('--y',(e.clientY-r.top)+'px')},{passive:true})});
var tabs=document.querySelectorAll('.tabs button'),imgs=document.querySelectorAll('.scr img'),cap=document.getElementById('cap'),cur=0,timer;
function sel(i){cur=i;tabs.forEach(function(b,j){b.setAttribute('aria-selected',j==i)});imgs.forEach(function(m,j){m.classList.toggle('on',j==i);if(j==i&&m.dataset.src){m.src=m.dataset.src;m.removeAttribute('data-src')}});cap.textContent=imgs[i].alt}
tabs.forEach(function(b,i){b.addEventListener('click',function(){clearInterval(timer);sel(i)})});
var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(!rm&&tabs.length)timer=setInterval(function(){sel((cur+1)%tabs.length)},5000);
var pv=document.getElementById('pv');
if(pv){var vb=pv.dataset[matchMedia('(max-width: 640px)').matches?'v':'h'],loaded=false,sys=false;pv.poster=vb+'.webp';
 var vload=function(){if(loaded)return;loaded=true;var f=pv.firstChild;
  if(pv.canPlayType('video/webm; codecs="vp9, opus"')){var w=document.createElement('source');w.src=vb+'.webm';w.type='video/webm';pv.insertBefore(w,f)}
  var m=document.createElement('source');m.src=vb+'.mp4';m.type='video/mp4';pv.insertBefore(m,f);pv.preload='metadata';pv.load()};
 var vauto=!rm&&!(navigator.connection&&navigator.connection.saveData);
 pv.addEventListener('pause',function(){if(!sys)pv.dataset.user='1';sys=false});
 if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){vload();if(vauto&&pv.paused&&!pv.dataset.user){var p=pv.play();if(p&&p.catch)p.catch(function(){})}}else if(!pv.paused&&!pv.dataset.user){sys=true;pv.pause()}})},{rootMargin:'200px 0px',threshold:.25}).observe(pv)}else vload()}
var c=document.getElementById('gl');
if(c&&!rm&&!navigator.connection?.saveData){var go=function(){import("./hero3d.js").then(function(m){return m.start(c)}).catch(function(){})};
 if('requestIdleCallback' in window)requestIdleCallback(go,{timeout:1500});else setTimeout(go,600)}
})();
