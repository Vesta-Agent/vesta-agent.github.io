// Lazy WebGL hero: glowing faceted form in brand blue->violet. Static CSS fallback stays underneath.
export async function start(canvas){
  const THREE=await import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.min.js');
  const r=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true,powerPreference:'high-performance'});
  const dpr=Math.min(devicePixelRatio,window.innerWidth<700?1.5:2);r.setPixelRatio(dpr);
  const scene=new THREE.Scene(),cam=new THREE.PerspectiveCamera(40,1,.1,100);cam.position.z=7;cam.position.y=-0.2;
  const uni={t:{value:0}};
  const mat=new THREE.ShaderMaterial({uniforms:uni,transparent:true,vertexShader:`varying vec3 n;varying vec3 p;uniform float t;
   void main(){n=normalize(normalMatrix*normal);vec3 q=position;q+=normal*0.12*sin(q.y*2.2+t*.8)*cos(q.x*1.7+t*.6);p=q;gl_Position=projectionMatrix*modelViewMatrix*vec4(q,1.);}`,
   fragmentShader:`varying vec3 n;varying vec3 p;uniform float t;void main(){float f=pow(1.-abs(n.z),2.2);vec3 a=vec3(.22,.45,1.),b=vec3(.58,.3,.98);vec3 c=mix(a,b,clamp(p.y*.35+.5+.15*sin(t*.4),0.,1.));gl_FragColor=vec4(c*(.12+1.3*f),.12+.6*f);}`});
  const g=new THREE.IcosahedronGeometry(1.25,24);const mesh=new THREE.Mesh(g,mat);scene.add(mesh);
  const wire=new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(1.7,2)),new THREE.LineBasicMaterial({color:0x6f7dff,transparent:true,opacity:.12}));scene.add(wire);
  const pts=new THREE.BufferGeometry(),N=window.innerWidth<700?500:1100,arr=new Float32Array(N*3);
  for(let i=0;i<N;i++){const r0=2.8+Math.random()*2.6,th=Math.random()*6.283,ph=Math.acos(2*Math.random()-1);arr.set([r0*Math.sin(ph)*Math.cos(th),r0*Math.sin(ph)*Math.sin(th),r0*Math.cos(ph)],i*3)}
  pts.setAttribute('position',new THREE.BufferAttribute(arr,3));
  const dust=new THREE.Points(pts,new THREE.PointsMaterial({color:0x9fb0ff,size:.025,transparent:true,opacity:.7}));scene.add(dust);
  let mx=0,my=0,vis=true,raf=0,last=performance.now();
  addEventListener('pointermove',e=>{mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5},{passive:true});
  function size(){const w=canvas.clientWidth,h=canvas.clientHeight;r.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix()}
  size();addEventListener('resize',size);
  function loop(now){const dt=Math.min(.05,(now-last)/1000);last=now;uni.t.value+=dt;
    mesh.rotation.y+=dt*.12;mesh.rotation.x+=dt*.05;wire.rotation.y-=dt*.04;dust.rotation.y+=dt*.02;
    scene.rotation.y+=(mx*.4-scene.rotation.y)*.04;scene.rotation.x+=(my*.25-scene.rotation.x)*.04;
    r.render(scene,cam);raf=requestAnimationFrame(loop)}
  new IntersectionObserver(es=>{const v=es[0].isIntersecting;if(v&&!vis){last=performance.now();raf=requestAnimationFrame(loop)}if(!v)cancelAnimationFrame(raf);vis=v}).observe(canvas);
  document.addEventListener('visibilitychange',()=>{if(document.hidden)cancelAnimationFrame(raf);else if(vis){last=performance.now();raf=requestAnimationFrame(loop)}});
  raf=requestAnimationFrame(loop);canvas.classList.add('on');
}
