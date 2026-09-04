JS = r"""
(function(){
'use strict';
var LS=window.localStorage;
function ls(k,d){try{var v=LS.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function ss(k,v){try{LS.setItem(k,JSON.stringify(v))}catch(e){}}
var CART=ls('gc_cart',[]), WISH=ls('gc_wish',[]);
var FREE=999;
function P(h){for(var i=0;i<DATA.length;i++){if(DATA[i].h===h)return DATA[i]}return null}
function inr(n){return '₹'+Number(n).toLocaleString('en-IN')}
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;')}
function stars(r){var f=Math.round(r),s='';for(var i=0;i<5;i++)s+=(i<f?'★':'☆');return s}
window.stars=stars;window.gcInr=inr;

var TO;
function toast(m){var t=$('#toast');if(!t)return;t.textContent=m;t.classList.add('on');
  clearTimeout(TO);TO=setTimeout(function(){t.classList.remove('on')},2200)}

function counts(){
  var c=CART.reduce(function(a,b){return a+b.q},0);
  $$('[data-cartcount]').forEach(function(e){e.textContent=c;e.style.display=c?'grid':'none'});
  $$('[data-wishcount]').forEach(function(e){e.textContent=WISH.length;e.style.display=WISH.length?'grid':'none'});
  $$('[data-wtog]').forEach(function(e){
    var h=e.getAttribute('data-wtog'),on=WISH.indexOf(h)>-1;
    e.classList.toggle('on',on);
    var s=e.querySelector('svg');if(s)s.setAttribute('fill',on?'currentColor':'none');
  });
}
window.counts=counts;window.gcToast=toast;
function toggleWish(h){
  var i=WISH.indexOf(h);
  if(i>-1){WISH.splice(i,1);toast('Removed from wishlist')}
  else{WISH.push(h);toast('Saved to wishlist')}
  ss('gc_wish',WISH);counts();renderWish();
  if(window.RENDER_WISHLIST)window.RENDER_WISHLIST();
}

/* ---------------- cart ---------------- */
function swImg(p,name){var r='';(p.sw||[]).forEach(function(x){if(x[0]===name)r=x[1]});return r}
function lineImg(c,p){return c.c?(swImg(p,c.c)||p.i[0]):p.i[0]}
function subtotal(){return CART.reduce(function(a,b){var p=P(b.h);return a+b.q*(p?p.p:0)},0)}
function mrpTotal(){return CART.reduce(function(a,b){var p=P(b.h);return a+b.q*((p&&p.cp)?p.cp:(p?p.p:0))},0)}
function addCart(h,size,color,q){
  var key=h+'|'+size+'|'+(color||'');
  var f=null;CART.forEach(function(c){if(c.k===key)f=c});
  if(f)f.q+=(q||1);else CART.push({k:key,h:h,s:size,c:color||'',q:q||1});
  ss('gc_cart',CART);counts();renderCart();
  var qm=$('#quickMod');if(qm)qm.classList.remove('on');
  openCart();
}
window.GC_ADD=function(h,s,c,q){addCart(h,s,c,q||1);toast('Added to bag')};
function renderCart(){
  var b=$('#cartBody');if(!b)return;
  if(!CART.length){
    b.innerHTML='<div class="side-empty"><p style="font-size:15px;font-weight:700;color:#1a1a1a">Your bag is empty</p>'+
      '<p style="margin:8px 0 20px">Add a few comfort-first bottoms and they will show up here.</p>'+
      '<a class="btn btn-d" href="collection.html">Start shopping</a></div>';
  }else{
    b.innerHTML=CART.map(function(c,i){var p=P(c.h);if(!p)return '';
      var sizes=p.sz.map(function(s){return '<option'+(s===c.s?' selected':'')+'>'+esc(s)+'</option>'}).join('');
      return '<div class="ci"><img src="'+lineImg(c,p)+'" alt="'+esc(p.t)+'" loading="lazy">'+
        '<div class="bd"><div class="n">'+esc(p.t)+'</div>'+
        '<div class="p">'+(p.cp?'<s>'+inr(p.cp)+'</s>':'')+inr(p.p)+'</div>'+
        '<div class="rowb">'+
          (c.c?'<span class="szsel">'+esc(c.c)+'</span>':'')+
          '<select class="szsel" data-size="'+i+'">'+sizes+'</select>'+
          '<span class="qty"><button data-q="'+i+'|-1">−</button><span>'+c.q+
          '</span><button data-q="'+i+'|1">+</button></span></div>'+
        '<div class="ret">30 days return available</div>'+
        '<div class="rowb"><a class="lnk" data-save="'+i+'">Save for later</a>'+
        '<a class="lnk" data-edit="'+i+'">Change style</a></div></div>'+
        '<button class="rm" data-del="'+i+'" aria-label="Remove">×</button></div>';
    }).join('');
  }
  var t=subtotal(), mrp=mrpTotal(), rem=Math.max(0,FREE-t), pct=Math.min(100,t/FREE*100);
  var s=$('#shipTxt');
  if(s)s.innerHTML = rem>0 ? 'Add <b>'+inr(rem)+'</b> more for free express delivery'
                           : '<b>Free express delivery unlocked</b>';
  var bar=$('#shipBar');if(bar)bar.style.width=pct+'%';
  var os=$('#osum');
  if(os){
    os.style.display=CART.length?'':'none';
    var sv=$('#osSave');
    $('#osMrp').textContent=inr(mrp);
    $('#osTot').textContent=inr(t);
    if(sv)sv.textContent='−'+inr(mrp-t);
    var svr=$('#osSaveRow');if(svr)svr.style.display=(mrp-t)>0?'':'none';
  }
  var co=$('#coBtn');
  if(co){co.textContent = CART.length ? ('Checkout @ '+inr(t)) : 'Checkout';
         co.style.opacity=CART.length?1:.45;co.style.pointerEvents=CART.length?'auto':'none';}
}
window.renderCart=renderCart;

/* ---------------- wishlist drawer ---------------- */
function renderWish(){
  var b=$('#wishBody');if(!b)return;
  var items=DATA.filter(function(p){return WISH.indexOf(p.h)>-1});
  if(!items.length){
    b.innerHTML='<div class="side-empty"><p style="font-size:15px;font-weight:700;color:#1a1a1a">Nothing saved yet</p>'+
      '<p style="margin:8px 0 20px">Tap the heart on any style and it waits for you here.</p>'+
      '<a class="btn btn-d" href="collection.html">Browse bottomwear</a></div>';
  }else{
    b.innerHTML=items.map(function(p){
      return '<div class="ci"><img src="'+p.i[0]+'" alt="'+esc(p.t)+'" loading="lazy">'+
        '<div class="bd"><div class="n">'+esc(p.t)+'</div>'+
        '<div class="ret">'+esc(p.sz[1]||p.sz[0])+'</div>'+
        '<div class="p">'+(p.cp?'<s>'+inr(p.cp)+'</s>':'')+inr(p.p)+'</div>'+
        '<div class="rowb"><a class="lnk" data-quick="'+p.h+'">Add to bag</a></div></div>'+
        '<button class="rm" data-wtog="'+p.h+'" aria-label="Remove" style="background:none;color:#6b6b6b;font-size:15px">✕</button></div>';
    }).join('');
  }
  var n=$('#wlDrwCount');if(n)n.textContent=items.length?(items.length+' item'+(items.length>1?'s':'')):'';
}
window.renderWish=renderWish;

/* ---------------- open / close ---------------- */
function openCart(){$('#cartDrw').classList.add('on');$('#ovl').classList.add('on');document.body.style.overflow='hidden'}
function openWish(){renderWish();$('#wishDrw').classList.add('on');$('#ovl').classList.add('on');document.body.style.overflow='hidden'}
function closeAll(){
  ['#cartDrw','#wishDrw','#navDrw','#searchOvl','#filterSheet'].forEach(function(s){var e=$(s);if(e)e.classList.remove('on')});
  $('#ovl').classList.remove('on');
  var m=$('#quickMod');if(m)m.classList.remove('on');
  var st=$('#stories');if(st){st.classList.remove('on');stopStory()}
  document.body.style.overflow='';
}
window.openCart=openCart;window.closeAll=closeAll;

/* ---------------- variant modal ---------------- */
var QP=null,QC=null,QS=null;
function openQuick(h){
  var p=P(h);if(!p)return;QP=p;QS=null;QC=p.sw.length?p.sw[0][0]:null;
  var m=$('#quickMod');
  var disc=p.cp?Math.round((1-p.p/p.cp)*100):0;
  var swHTML=p.sw.length?('<div class="opt"><div class="lb"><span>Colour — <b id="qcName" style="color:#1a1a1a">'+esc(QC)+'</b></span></div>'+
      '<div class="cdotsm" id="qSw">'+p.sw.map(function(x,i){
        return '<button data-qc="'+esc(x[0])+'" class="'+(i===0?'on':'')+'" style="background:'+(x[2]||'#ccc')+'" title="'+esc(x[0])+'"></button>'
      }).join('')+'</div></div>'):'';
  m.querySelector('.mod-box').innerHTML=
    '<button class="x" data-close>×</button>'+
    '<img class="hero" id="qImg" src="'+p.i[0]+'" alt="'+esc(p.t)+'">'+
    '<div class="mod-body">'+
      '<h3>'+esc(p.t)+'</h3>'+
      '<div class="pdp-rt" style="margin-top:8px"><span class="stars">'+stars(p.r)+'</span> <b style="color:#1a1a1a">'+p.r.toFixed(1)+'</b> | ('+p.rc+')</div>'+
      '<div class="pr"><b>'+inr(p.p)+'</b>'+(p.cp?'<s>'+inr(p.cp)+'</s><em>'+disc+'% Off</em>':'')+'</div>'+
      '<div style="font-size:11px;color:#6b6b6b;font-weight:600">Inclusive of all taxes</div>'+
      swHTML+
      '<div class="opt"><div class="lb"><span>Select size</span><a href="#" data-sizeguide>Size guide ›</a></div>'+
        '<div class="szrow" id="qSz">'+p.sz.map(function(s,i){
          return '<button data-qs="'+esc(s)+'"'+(i===p.sz.length-1?' class="oos"':'')+'>'+esc(s)+'</button>'}).join('')+
        '</div><div class="err" id="qErr">Please pick a size to continue</div></div>'+
      '<div class="trustline"><span>✓ Free delivery</span><span>✓ 30-day returns</span><span>✓ Free COD</span></div>'+
      '<button class="btn btn-d btn-blk" style="margin-top:18px;border-radius:5px" data-qadd>Add to bag</button>'+
      '<a class="full" href="product.html?p='+p.h+'">View full product details</a>'+
    '</div>';
  m.classList.add('on');$('#ovl').classList.add('on');document.body.style.overflow='hidden';
}
window.openQuick=openQuick;

/* ---------------- product card ---------------- */
function card(p){
  var disc=p.cp?Math.round((1-p.p/p.cp)*100):0;
  var dots=p.sw.length?('<div class="dots-c">'+p.sw.slice(0,5).map(function(x,i){
      return '<i data-cs="'+p.h+'|'+i+'" class="'+(i===0?'on':'')+'" style="background:'+(x[2]||'#ccc')+'" title="'+esc(x[0])+'"></i>'
    }).join('')+(p.sw.length>5?'<i class="plus">+'+(p.sw.length-5)+'</i>':'')+'</div>'):'';
  var tag = p.bs ? '<span class="tag">Bestseller</span>'
          : (p.nw ? '<span class="tag dk">New in</span>'
          : (disc>=40 ? '<span class="tag">'+disc+'% Off</span>' : ''));
  return '<article class="card" data-h="'+p.h+'">'+
    '<div class="imgwrap">'+
      '<a href="product.html?p='+p.h+'"><img src="'+p.i[0]+'" alt="'+esc(p.t)+'" loading="lazy" data-hero>'+
      (p.i[1]?'<img class="alt" src="'+p.i[1]+'" alt="" loading="lazy">':'')+'</a>'+
      tag+
      '<button class="wish" data-wtog="'+p.h+'" aria-label="Save to wishlist">'+heart()+'</button>'+
      '<span class="rate"><span class="st">\u2605</span>'+p.r.toFixed(1)+' <i>('+p.rc+')</i></span>'+
    '</div>'+
    '<div class="meta">'+
      '<a href="product.html?p='+p.h+'"><div class="nm">'+esc(p.t)+'</div></a>'+
      dots+
      '<div class="pr"><b>'+inr(p.p)+'</b>'+(p.cp?'<s>'+inr(p.cp)+'</s><em>'+disc+'% Off</em>':'')+'</div>'+
      (p.nudge?'<div class="nudge">'+esc(p.nudge)+'</div>':'')+
      '<button class="atcbtn" data-quick="'+p.h+'">Add to cart</button>'+
    '</div></article>';
}
window.card=card;
function heart(){return '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1L12 21l7.7-7.7 1.1-1a5.5 5.5 0 0 0 0-7.7z"/></svg>'}
function eye(){return '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="2.8"/></svg>'}
window.heart=heart;

/* ---------------- stories ---------------- */
var SIDX=0,STIM=null,SPROD=null;
var CAPS=['Made for all-day comfort','Holds its shape wash after wash','Styled by 8 million+ women','120+ colours to choose from'];
function openStories(h){
  var p=P(h);if(!p)return;SPROD=p;SIDX=0;
  var el=$('#stories');
  el.querySelector('.st-bars').innerHTML=p.i.map(function(){return '<i><b></b></i>'}).join('');
  el.querySelector('#stName').textContent=p.ty;
  el.querySelector('#stFtImg').src=p.i[0];
  el.querySelector('#stFtName').textContent=p.t;
  el.querySelector('#stFtPrice').textContent=inr(p.p);
  el.querySelector('#stFtBtn').setAttribute('data-quick',p.h);
  el.classList.add('on');document.body.style.overflow='hidden';
  showStory(0);
}
window.openStories=openStories;
function showStory(i){
  if(!SPROD)return;
  if(i>=SPROD.i.length){closeAll();return}
  if(i<0)i=0;
  SIDX=i;
  var el=$('#stories');
  el.querySelector('#stImg').src=SPROD.i[i];
  el.querySelector('#stCap').textContent=CAPS[i%CAPS.length];
  var bars=$$('.st-bars i b',el);
  bars.forEach(function(b,n){b.style.transition='none';b.style.width=n<i?'100%':'0'});
  var cur=bars[i];if(!cur)return;
  requestAnimationFrame(function(){cur.style.transition='width 3.6s linear';cur.style.width='100%'});
  clearTimeout(STIM);STIM=setTimeout(function(){showStory(i+1)},3700);
}
function stopStory(){clearTimeout(STIM)}

/* ---------------- drawer drill-down ---------------- */
function drwOpen(){$('#navDrw').classList.add('on');$('#ovl').classList.add('on');document.body.style.overflow='hidden';drwRoot()}
function drwRoot(){$$('#navDrw .drw-view').forEach(function(v){v.classList.toggle('on',v.classList.contains('root'))})}
function drwGo(id){$$('#navDrw .drw-view').forEach(function(v){v.classList.remove('on')});
  var t=$('#dv-'+id);if(t)t.classList.add('on')}

/* ---------------- coverflow ---------------- */
function initCover(){
  var c=$('#cover');if(!c)return;
  var tr=$('.cover-tr',c),slides=$$('.cover-tr>a',c),n=slides.length,idx=1;
  var dots=$('#coverDots');
  if(dots)dots.innerHTML=slides.map(function(_,i){return '<i data-cd="'+i+'"></i>'}).join('');
  function draw(){
    if(idx<0)idx=n-1;if(idx>=n)idx=0;
    var per=100/3;
    tr.style.transform='translateX('+(-(idx-1)*per)+'%)';
    slides.forEach(function(s,i){s.classList.toggle('mid',i===idx)});
    if(dots)$$('#coverDots i').forEach(function(d,i){d.classList.toggle('on',i===idx)});
  }
  c.addEventListener('click',function(e){
    var a=e.target.closest('[data-cv]');
    if(a){idx+= (a.getAttribute('data-cv')==='n'?1:-1);draw();return}
    var d=e.target.closest('[data-cd]');
    if(d){idx=+d.getAttribute('data-cd');draw()}
  });
  draw();
  setInterval(function(){idx++;draw()},6000);
}

/* ---------------- shade spectrum ---------------- */
function initSpectrum(){
  var r=$('#shadeRange');if(!r)return;
  function upd(){
    var s=SHADELIST[Math.min(SHADELIST.length-1,Math.round(r.value/100*(SHADELIST.length-1)))];
    $('#shadeChipName').textContent=s[0];
    $('#shadeChipDot').style.background=s[1];
  }
  r.addEventListener('input',upd);upd();
}

/* ---------------- delegated events ---------------- */
document.addEventListener('click',function(e){
  var t=e.target,a;
  function up(sel){return t.closest?t.closest(sel):null}

  if(up('[data-close]')||t.id==='ovl'){e.preventDefault();closeAll();return}
  if((a=up('[data-quick]'))){e.preventDefault();closeAll();
     var qh=a.getAttribute('data-quick');setTimeout(function(){openQuick(qh)},70);return}
  if((a=up('[data-wtog]'))){e.preventDefault();toggleWish(a.getAttribute('data-wtog'));return}
  if(up('[data-opencart]')){e.preventDefault();openCart();return}
  if(up('[data-openwish]')){e.preventDefault();openWish();return}
  if(up('[data-burger]')){e.preventDefault();drwOpen();return}
  if((a=up('[data-drw]'))){e.preventDefault();drwGo(a.getAttribute('data-drw'));return}
  if(up('[data-drwback]')){e.preventDefault();drwRoot();return}
  if(up('[data-search]')){e.preventDefault();$('#searchOvl').classList.add('on');$('#ovl').classList.add('on');
     setTimeout(function(){var i=$('#searchInput');if(i)i.focus()},220);return}
  if((a=up('[data-stories]'))){e.preventDefault();openStories(a.getAttribute('data-stories'));return}
  if(up('[data-sizeguide]')){e.preventDefault();toast('Size guide: waist 26–44 in · XS to 4X · petite-plus 2P–4P');return}
  if(up('[data-appclose]')){var st2=$('#appstrip');if(st2)st2.classList.add('gone');return}

  if((a=up('[data-cs]'))){
    var parts=a.getAttribute('data-cs').split('|'),p=P(parts[0]),n=+parts[1];
    var cardEl=a.closest('.card'),img=cardEl.querySelector('[data-hero]');
    if(img&&p.sw[n])img.src=p.sw[n][1];
    $$('.dots-c i',cardEl).forEach(function(x){x.classList.remove('on')});a.classList.add('on');
    return;
  }
  if((a=up('[data-qc]'))){
    QC=a.getAttribute('data-qc');
    $$('#qSw button').forEach(function(x){x.classList.remove('on')});a.classList.add('on');
    var im=$('#qImg'),u=swImg(QP,QC);if(im&&u)im.src=u;
    var nm=$('#qcName');if(nm)nm.textContent=QC;
    return;
  }
  if((a=up('[data-qs]'))){
    if(a.classList.contains('oos')){toast('That size is out of stock — notify me?');return}
    QS=a.getAttribute('data-qs');
    $$('#qSz button').forEach(function(x){x.classList.remove('on')});a.classList.add('on');
    var er=$('#qErr');if(er)er.classList.remove('on');
    return;
  }
  if(up('[data-qadd]')){
    if(!QS){var er2=$('#qErr');if(er2)er2.classList.add('on');return}
    addCart(QP.h,QS,QC,1);toast('Added to bag');return;
  }
  if((a=up('[data-q]'))){
    var pr=a.getAttribute('data-q').split('|'),i=+pr[0],d=+pr[1];
    CART[i].q+=d;if(CART[i].q<1)CART.splice(i,1);
    ss('gc_cart',CART);counts();renderCart();return;
  }
  if((a=up('[data-del]'))){CART.splice(+a.getAttribute('data-del'),1);ss('gc_cart',CART);counts();renderCart();toast('Removed from bag');return}
  if((a=up('[data-save]'))){
    var it=CART[+a.getAttribute('data-save')];
    if(WISH.indexOf(it.h)<0){WISH.push(it.h);ss('gc_wish',WISH)}
    CART.splice(+a.getAttribute('data-save'),1);ss('gc_cart',CART);counts();renderCart();toast('Moved to wishlist');return;
  }
  if((a=up('[data-edit]'))){var it2=CART[+a.getAttribute('data-edit')];closeAll();
    setTimeout(function(){openQuick(it2.h)},240);return}
  if(up('#coBtn')){toast('Demo mockup — checkout is not connected');return}
  if(up('[data-addall]')){
    var items=DATA.filter(function(p){return WISH.indexOf(p.h)>-1});
    if(!items.length){toast('Your wishlist is empty');return}
    items.forEach(function(p){addCart(p.h,p.sz[1]||p.sz[0],p.sw.length?p.sw[0][0]:'',1)});
    toast(items.length+' item'+(items.length>1?'s':'')+' added to bag');return;
  }
  if(up('[data-coupon]')){
    var v=($('#coupIn')||{}).value||'';
    toast(v.trim()?('Coupon '+v.toUpperCase()+' will apply at checkout'):'Enter a coupon code');return;
  }
  if(up('[data-pin]')){
    var pv=($('#pinIn')||{}).value||'';
    var r2=$('#pinRes');
    if(/^\d{6}$/.test(pv.trim())){r2.textContent='Delivers by '+delivDate()+' · Free shipping · COD available';r2.classList.add('on')}
    else toast('Enter a valid 6-digit pincode');
    return;
  }
  if(up('[data-stprev]')){showStory(SIDX-1);return}
  if(up('[data-stnext]')){showStory(SIDX+1);return}
  if((a=up('[data-rail]'))){
    var wrap=a.closest('.carou'),row=$('.railrow',wrap)||$('.bsrail',wrap);
    if(row)row.scrollLeft += (a.getAttribute('data-rail')==='n'?1:-1)*(row.clientWidth||420);return;
  }
  if((a=up('[data-cats]'))){
    var cw=a.closest('.catwrap'),tr=$('.cats',cw);
    tr.scrollLeft += (a.getAttribute('data-cats')==='n'?1:-1)*tr.clientWidth;return;
  }
},false);

document.addEventListener('change',function(e){
  var s=e.target.closest('[data-size]');
  if(s){var i=+s.getAttribute('data-size');CART[i].s=s.value;
    CART[i].k=CART[i].h+'|'+s.value+'|'+CART[i].c;ss('gc_cart',CART);toast('Size updated to '+s.value)}
});

function delivDate(){var d=new Date();d.setDate(d.getDate()+3);
  return d.toLocaleDateString('en-IN',{weekday:'short',day:'numeric',month:'short'})}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeAll()});

window.setVp=function(m){
  document.body.classList.toggle('mobile',m==='m');
  $$('.pbar .tg button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-vp')===m)});
  try{LS.setItem('gc_vp',m)}catch(e){}
  window.dispatchEvent(new Event('resize'));
};

document.addEventListener('DOMContentLoaded',function(){
  try{if((LS.getItem('gc_vp')||'').indexOf('m')>-1)window.setVp('m')}catch(e){}
  counts();renderCart();renderWish();
  $$('[data-tabgroup]').forEach(function(g){
    g.addEventListener('click',function(e){
      var b=e.target.closest('button[data-tab]');if(!b)return;
      var name=b.getAttribute('data-tab'),grp=g.getAttribute('data-tabgroup');
      $$('button[data-tab]',g).forEach(function(x){x.classList.toggle('on',x===b)});
      $$('[data-panel][data-group="'+grp+'"]').forEach(function(p){
        p.style.display=p.getAttribute('data-panel')===name?'':'none'});
    });
  });
  $$('[data-cards]').forEach(function(g){
    g.innerHTML=Array.prototype.map.call(g.children,function(c){
      var h=c.getAttribute('data-p');var p=P(h);return p?card(p):''}).join('');
  });
  function catArrows(){
    $$('.catwrap').forEach(function(w){
      var tr=$('.cats',w);if(!tr)return;
      w.classList.toggle('scrollable', tr.scrollWidth - tr.clientWidth > 4);
    });
    $$('.carou').forEach(function(w){
      var tr=$('.bsrail',w)||$('.railrow',w);if(!tr)return;
      w.classList.toggle('scrollable', tr.scrollWidth - tr.clientWidth > 4);
    });
  }
  window.gcCatArrows=catArrows;
  catArrows();
  window.addEventListener('resize',catArrows);
  setTimeout(catArrows,600);
  $$('[data-tabgroup]').forEach(function(g){g.addEventListener('click',function(){setTimeout(catArrows,60)})});
  initCover();initSpectrum();counts();
});
})();
"""

JS_PLP = r"""
(function(){
var SHOWN=12,SORT='rel',MAXP=2299;
var F={whom:[],cl:[],ty:[],sz:[],disc:[],len:[],fit:[],pat:[],fab:[],rise:[]};
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
var LABEL={whom:'',cl:'',ty:'',sz:'Size ',disc:'',len:'',fit:'',pat:'',fab:'',rise:''};
function pass(p){
  if(p.p>MAXP)return false;
  if(F.whom.length&&F.whom.indexOf(p.whom)<0)return false;
  if(F.ty.length&&F.ty.indexOf(p.ty)<0)return false;
  if(F.len.length&&F.len.indexOf(p.len)<0)return false;
  if(F.fit.length&&F.fit.indexOf(p.fit)<0)return false;
  if(F.pat.length&&F.pat.indexOf(p.pat)<0)return false;
  if(F.fab.length&&F.fab.indexOf(p.fab)<0)return false;
  if(F.rise.length&&F.rise.indexOf(p.rise)<0)return false;
  if(F.sz.length&&!F.sz.some(function(s){return p.sz.indexOf(s)>-1}))return false;
  if(F.cl.length&&!F.cl.some(function(c){return p.cols.indexOf(c)>-1}))return false;
  if(F.disc.length){var d=p.cp?(1-p.p/p.cp)*100:0;if(d<20)return false}
  return true;
}
function sorted(l){
  l=l.slice();
  if(SORT==='lh')l.sort(function(a,b){return a.p-b.p});
  if(SORT==='hl')l.sort(function(a,b){return b.p-a.p});
  if(SORT==='rt')l.sort(function(a,b){return b.r-a.r});
  if(SORT==='dis')l.sort(function(a,b){return (b.cp?1-b.p/b.cp:0)-(a.cp?1-a.p/a.cp:0)});
  return l;
}
window.RENDER_PLP=function(){
  var list=sorted(DATA.filter(pass));
  $('#plpGrid').innerHTML=list.slice(0,SHOWN).map(card).join('')||
    '<p style="grid-column:1/-1;padding:40px 0;color:#6b6b6b">No products match these filters. '+
    '<button style="text-decoration:underline;font-weight:800" data-clearf>Clear all</button></p>';
  $('#plpCount').textContent=list.length+' styles';
  $('#loadWrap').style.display=list.length>SHOWN?'':'none';
  $('#loadLeft').textContent=Math.max(0,list.length-SHOWN);
  var chips=[];
  Object.keys(F).forEach(function(k){F[k].forEach(function(v){chips.push([k,v,(LABEL[k]||'')+v])})});
  if(MAXP<2299)chips.push(['price','max','Under ₹'+MAXP]);
  $('#chips').innerHTML=chips.length?chips.map(function(c){
    return '<span class="c">'+c[2]+' <button data-unf="'+c[0]+'|'+c[1]+'">×</button></span>'
  }).join('')+'<button class="clr" data-clearf>Clear all</button>':'';
  if(window.counts)window.counts();
};
function syncUI(){
  $$('[data-f]').forEach(function(el){
    var pr=el.getAttribute('data-f').split('|'),on=F[pr[0]]&&F[pr[0]].indexOf(pr[1])>-1;
    el.classList.toggle('on',on);
    var cb=el.querySelector('input[type=checkbox]');if(cb)cb.checked=on;
  });
}
document.addEventListener('click',function(e){
  var t=e.target,a;
  if((a=t.closest('[data-f]'))){
    var pr=a.getAttribute('data-f').split('|'),k=pr[0],v=pr[1],i=F[k].indexOf(v);
    if(i>-1)F[k].splice(i,1);else F[k].push(v);
    if(t.tagName!=='INPUT')e.preventDefault();
    SHOWN=12;syncUI();window.RENDER_PLP();return;
  }
  if((a=t.closest('[data-unf]'))){
    var p2=a.getAttribute('data-unf').split('|');
    if(p2[0]==='price'){MAXP=2299;var r=document.querySelector('#priceRange');if(r){r.value=2299;
      document.querySelector('#priceMax').textContent='₹2,299'}}
    else{var j=F[p2[0]].indexOf(p2[1]);if(j>-1)F[p2[0]].splice(j,1)}
    syncUI();window.RENDER_PLP();return;
  }
  if(t.closest('[data-clearf]')){
    Object.keys(F).forEach(function(k){F[k]=[]});MAXP=2299;
    var r2=document.querySelector('#priceRange');
    if(r2){r2.value=2299;document.querySelector('#priceMax').textContent='₹2,299'}
    SHOWN=12;syncUI();window.RENDER_PLP();return;
  }
  if(t.closest('[data-more]')){SHOWN+=12;window.RENDER_PLP();return}
  if(t.closest('[data-filtersheet]')){document.querySelector('#filterSheet').classList.add('on');
    document.querySelector('#ovl').classList.add('on');return}
  if(t.closest('[data-sortsheet]')){document.querySelector('#sortSel').focus();
    document.querySelector('#sortSel').click();return}
},false);
document.addEventListener('DOMContentLoaded',function(){
  var s=document.querySelector('#sortSel');
  if(s)s.addEventListener('change',function(){SORT=s.value;window.RENDER_PLP()});
  var r=document.querySelector('#priceRange');
  if(r)r.addEventListener('input',function(){
    MAXP=+r.value;document.querySelector('#priceMax').textContent='₹'+MAXP.toLocaleString('en-IN');
    window.RENDER_PLP();
  });
  window.RENDER_PLP();
});
})();
"""

JS_PDP = r"""
(function(){
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
document.addEventListener('DOMContentLoaded',function(){
  var qty=1;
  $$('[data-pq]').forEach(function(b){
    b.addEventListener('click',function(){
      qty=Math.max(1,qty+(+b.getAttribute('data-pq')));$('#pQty').textContent=qty;
    });
  });
  $$('[data-pc]').forEach(function(b){
    b.addEventListener('click',function(){
      $$('[data-pc]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
      var u=b.getAttribute('data-img');
      if(u){var g=$$('#pgal img');if(g[0])g[0].src=u;var sb=$('#satcImg');if(sb)sb.src=u}
      var n=$('#pcName');if(n)n.textContent=b.getAttribute('data-pc');
    });
  });
  $$('[data-ps]').forEach(function(b){
    b.addEventListener('click',function(){
      if(b.classList.contains('oos')){window.gcToast&&window.gcToast('Out of stock');return}
      $$('[data-ps]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
      var e=$('#pErr');if(e)e.classList.remove('on');
    });
  });
  var addBtn=$('#pdpAdd');
  if(addBtn)addBtn.addEventListener('click',function(){
    var s=$('[data-ps].on'),c=$('[data-pc].on');
    if(!s){var e=$('#pErr');if(e)e.classList.add('on');return}
    window.GC_ADD(HANDLE,s.getAttribute('data-ps'),c?c.getAttribute('data-pc'):'',qty);
  });

  var bar=$('#satc'),atcRow=$('.atc');
  if(bar&&atcRow){
    var onScroll=function(){
      var r=atcRow.getBoundingClientRect();
      bar.classList.toggle('on', r.bottom < 0 || r.top > window.innerHeight);
    };
    window.addEventListener('scroll',onScroll,{passive:true});
    window.addEventListener('resize',onScroll);onScroll();
  }
  var nav=$('#subnav');
  if(nav){
    function place(){
      var h=$('.hdr'),bh=parseInt(getComputedStyle(document.body).paddingTop)||0;
      var top=(h?h.offsetHeight:70)+bh;
      nav.style.top=top+'px';
      return top+nav.offsetHeight;
    }
    var off=place();window.addEventListener('resize',function(){off=place()});
    var secs=$$('.pdp-sec');
    $$('#subnav button').forEach(function(b){
      b.addEventListener('click',function(){
        var el=document.getElementById(b.getAttribute('data-go'));if(!el)return;
        window.scrollTo({top:el.getBoundingClientRect().top+window.scrollY-off-8,behavior:'smooth'});
      });
    });
    window.addEventListener('scroll',function(){
      var first=secs[0];
      if(first)nav.classList.toggle('show',first.getBoundingClientRect().top<off+40);
      var cur=null;
      secs.forEach(function(s){if(s.getBoundingClientRect().top<=off+70)cur=s.id});
      $$('#subnav button').forEach(function(b){
        var on=b.getAttribute('data-go')===cur;b.classList.toggle('on',on);
        if(on&&b.offsetParent){var st=b.closest('.in');
          st.scrollTo({left:b.offsetLeft-st.clientWidth/2+b.clientWidth/2,behavior:'smooth'})}
      });
    },{passive:true});
  }
});
})();
"""

JS_WISH = r"""
(function(){
function ls(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
window.RENDER_WISHLIST=function(){
  var W=ls('gc_wish',[]),g=document.querySelector('#wlGrid'),e=document.querySelector('#wlEmpty');
  if(!g)return;
  var items=DATA.filter(function(p){return W.indexOf(p.h)>-1});
  document.querySelector('#wlCount').textContent=items.length+(items.length===1?' saved style':' saved styles');
  if(!items.length){g.innerHTML='';e.style.display='';return}
  e.style.display='none';g.innerHTML=items.map(card).join('');
  if(window.counts)window.counts();
};
document.addEventListener('DOMContentLoaded',window.RENDER_WISHLIST);
})();
"""
