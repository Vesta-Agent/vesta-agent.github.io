(function(){
var R='https://github.com/Vesta-Agent/vesta-agent-releases/releases/latest/download/';
var A={win:'VestaAgent-1.4.0-windows-x64-setup.exe',win7:'VestaAgent-1.4.0-windows7-8-legacy-setup.exe',android:'VestaAgent-1.4.0-android.apk',deb:'VestaAgent-1.4.0-linux-amd64.deb',appimage:'VestaAgent-1.4.0-linux-x86_64.AppImage'};
var ver='1.4.0';
function apply(){document.querySelectorAll('[data-asset]').forEach(function(a){a.href=R+A[a.dataset.asset]});
 document.querySelectorAll('[data-ver]').forEach(function(e){e.textContent=ver});
 var u=navigator.userAgent,k='win',d=document.documentElement.lang=='fa';
 var n={win:d?'ویندوز':'Windows',win7:d?'ویندوز ۷/۸':'Windows 7/8',android:d?'اندروید':'Android',deb:d?'لینوکس':'Linux',appimage:'Linux'};
 if(/Android/i.test(u))k='android';else if(/Windows NT (6\.[0-3])/.test(u))k='win7';else if(/Windows/.test(u))k='win';else if(/Linux|X11/.test(u))k='deb';else if(/iPhone|iPad|Mac/.test(u))k=null;
 var b=document.getElementById('dlbtn'),t=document.getElementById('dlos');
 if(k){b.href=R+A[k];t.textContent=n[k]}else{b.href='#download';t.textContent=d?'':''}}
apply();
fetch('https://api.github.com/repos/Vesta-Agent/vesta-agent-releases/releases/latest').then(function(r){return r.ok?r.json():null}).then(function(j){if(!j)return;ver=j.tag_name.replace(/^v/,'');
 (j.assets||[]).forEach(function(x){var m=x.name;if(/windows-x64-setup\.exe$/.test(m))A.win=m;else if(/windows7-8.*\.exe$/.test(m))A.win7=m;else if(/\.apk$/.test(m))A.android=m;else if(/\.deb$/.test(m))A.deb=m;else if(/\.AppImage$/.test(m))A.appimage=m});apply()}).catch(function(){});
if('IntersectionObserver' in window){var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');o.unobserve(e.target)}})},{threshold:.12});document.querySelectorAll('.rv').forEach(function(e){o.observe(e)})}else document.querySelectorAll('.rv').forEach(function(e){e.classList.add('in')});
})();
