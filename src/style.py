CSS = r"""
:root{
  --brand:#E6007E;
  --brand-dk:#b80065;
  --ink:#1a1a1a;
  --muted:#6b6b6b;
  --line:#e6e6e6;
  --soft:#f7f5f4;
  --soft2:#efece9;
  --ok:#0f7b47;
  --sale:#e02020;
  --font:'Montserrat',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  --maxw:1400px;
  --barh:0px;
  --hdrh:112px;
  --hdrm:62px;
  --r:10px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:var(--font);color:var(--ink);background:#fff;font-weight:500;
  font-size:14px;line-height:1.5;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button{font-family:inherit;font-weight:600;cursor:pointer;border:0;background:none;color:inherit}
input,select{font-family:inherit;font-size:14px}
h1,h2,h3,h4{margin:0;font-weight:700;letter-spacing:-.01em}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
#viewport{container-type:inline-size;margin:0 auto;transition:max-width .25s ease;background:#fff;position:relative}
body.mobile #viewport{max-width:420px;box-shadow:0 0 0 1px var(--line)}

/* ---------- preview toolbar ---------- */
.pbar{position:fixed;top:0;left:0;right:0;height:44px;background:#141414;color:#fff;z-index:999;
  display:flex;align-items:center;gap:6px;padding:0 14px;font-size:12px;font-weight:600;
  flex-wrap:nowrap;overflow-x:auto;white-space:nowrap;scrollbar-width:none}
.pbar::-webkit-scrollbar{display:none}
.pbar .pb-logo,.pbar .tg{flex:0 0 auto}
.pbar .pb-logo{font-weight:800;letter-spacing:.14em;margin-right:10px;font-size:11px;color:var(--brand)}
.pbar a{padding:6px 11px;border-radius:20px;opacity:.72}
.pbar a:hover{opacity:1;background:#262626}
.pbar a.on{background:var(--brand);opacity:1}
.pbar .spacer{margin-left:auto}
.pbar .tg{display:flex;background:#262626;border-radius:20px;padding:3px}
.pbar .tg button{padding:5px 12px;border-radius:16px;font-size:11px;color:#bbb}
.pbar .tg button.on{background:#fff;color:#111}
body.hasbar{--barh:44px;padding-top:44px}

/* ---------- app strip ---------- */
.appstrip{background:#fff;border-bottom:1px solid var(--line);display:flex;align-items:center;
  gap:14px;padding:9px 18px;font-size:12px;font-weight:600}
.appstrip .txt{flex:1;line-height:1.35}
.appstrip .cta{background:var(--brand);color:#fff;border-radius:20px;padding:7px 16px;font-size:11px;
  font-weight:800;white-space:nowrap}
.appstrip .x{color:var(--muted);font-size:17px;line-height:1;padding:2px 4px}
.appstrip.gone{display:none}
.greenline{height:6px;background:#1f3d2b}

/* ---------- header ---------- */
.hdr{position:sticky;top:var(--barh);z-index:120;background:#fff;border-bottom:1px solid var(--line)}
.hdr-in{display:flex;align-items:center;gap:16px;padding:10px 24px;max-width:var(--maxw);margin:0 auto}
.logo{order:-1;display:flex;align-items:flex-start;gap:1px;flex-shrink:0}
.logo .lg{font-size:22px;font-weight:800;font-style:italic;letter-spacing:.01em;line-height:1}
.logo .ex{color:var(--brand);font-size:22px;font-weight:800;font-style:italic;line-height:1}
.nav{display:flex;align-items:center;gap:0;margin:0 0 0 22px;padding:0}
.nav>li{list-style:none;position:static}
.nav .top{position:relative;display:flex;align-items:center;gap:5px;padding:14px 15px;font-size:13.5px;
  font-weight:600;cursor:pointer;white-space:nowrap}
.nav .top .car{font-size:9px;color:var(--muted)}
.nav .top .badge{position:absolute;top:0;left:9px;background:var(--brand);color:#fff;font-size:7.5px;
  padding:2px 5px;border-radius:3px;letter-spacing:.06em;font-weight:800}
.nav>li:hover .top{color:var(--brand)}
.nav .top::after{content:"";position:absolute;left:15px;right:15px;bottom:6px;height:2px;background:var(--brand);
  transform:scaleX(0);transition:transform .18s}
.nav>li:hover .top::after{transform:scaleX(1)}
.searchbox{flex:1;max-width:430px;margin:0 auto;position:relative}
.searchbox input{width:100%;border:1.4px solid #d9d9d9;border-radius:26px;padding:10px 16px 10px 40px;
  outline:none;background:#fff;cursor:pointer;font-size:13px}
.searchbox .si{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--muted);
  display:grid;place-items:center}
.icons{margin-left:auto;display:flex;align-items:flex-start;gap:14px}
.ico{position:relative;display:grid;justify-items:center;gap:2px;padding:4px 2px;min-width:40px}
.ico .lbl{font-size:9.5px;font-weight:600;color:#444}
.ico:hover{color:var(--brand)}
.ico .cnt{position:absolute;top:-2px;right:2px;min-width:15px;height:15px;border-radius:8px;background:var(--brand);
  color:#fff;font-size:9px;font-weight:800;display:grid;place-items:center;padding:0 4px}
.burger{display:none}

/* ---------- mega menu ---------- */
.mega{position:absolute;left:0;right:0;top:100%;background:#fff;border-top:1px solid var(--line);
  box-shadow:0 18px 40px rgba(0,0,0,.10);opacity:0;visibility:hidden;transform:translateY(-6px);
  transition:.18s;z-index:130;padding:30px 0 34px}
.nav>li:hover .mega,.nav>li:focus-within .mega{opacity:1;visibility:visible;transform:none}
.mega-in{max-width:var(--maxw);margin:0 auto;padding:12px 24px 8px;display:grid;grid-template-columns:1fr 236px;gap:44px;max-height:calc(100vh - 140px);overflow:auto}
.mcols{display:grid;grid-template-columns:repeat(6,1fr);gap:26px 30px;align-items:start}
.mcol{min-width:0}
.mhd{font-size:12.5px;font-weight:800;color:var(--brand);letter-spacing:.02em;margin:0 0 12px;
  padding-bottom:9px;border-bottom:1px solid var(--line)}
.mcol+.mcol{}
a.mlink{display:flex;align-items:center;gap:11px;padding:6px 7px 6px 4px;margin-left:-4px;
  border-radius:8px;font-size:12.5px;font-weight:600;color:#3d3d3d;line-height:1.3;transition:.14s}
a.mlink img{width:34px;height:40px;object-fit:cover;border-radius:6px;background:var(--soft);flex:0 0 34px}
a.mlink span{min-width:0}
a.mlink:hover{color:var(--brand);background:#fdf3f8}
.mega-sizes{margin-top:24px;padding-top:18px;border-top:1px solid var(--line)}
.mega-side .hd{font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);margin:10px 0 2px}
.nav .chiprow a.mega-chip{padding:6px 13px;border:1px solid var(--line);border-radius:20px;
  font-size:11.5px;font-weight:600;color:#444}
.nav .chiprow a.mega-chip:hover{border-color:var(--ink);background:var(--ink);color:#fff}
.mega-side .allbtn{display:block;text-align:center;background:var(--ink);color:#fff;font-size:12px;
  font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:11px;border-radius:7px}
.mega-side .allbtn:hover{background:var(--brand)}
.mega-side .chiprow{display:flex;flex-wrap:wrap;gap:7px}
.mega-side{display:flex;flex-direction:column;gap:12px}
.mega-promo{border-radius:8px;overflow:hidden;position:relative;background:var(--soft)}
.mega-promo img{width:100%;aspect-ratio:230/100;object-fit:cover}
.mega-promo .cap{position:absolute;left:12px;bottom:10px;color:#fff;font-size:12px;font-weight:800;
  text-shadow:0 1px 6px rgba(0,0,0,.55)}
.mega-best{display:flex;gap:10px}
.mega-best a{flex:1}
.mega-best img{width:100%;aspect-ratio:1/1.2;object-fit:cover;border-radius:8px}
.mega-best .p{font-size:11px;font-weight:700;margin-top:5px}

/* ---------- overlays ---------- */
.ovl{position:fixed;inset:0;background:rgba(15,15,15,.45);z-index:400;opacity:0;visibility:hidden;transition:.22s}
.ovl.on{opacity:1;visibility:visible}

/* search overlay */
.srch{position:fixed;top:0;left:0;right:0;background:#fff;z-index:410;transform:translateY(-100%);
  transition:transform .28s cubic-bezier(.2,.8,.2,1);max-height:92vh;overflow:auto;padding-bottom:24px}
.srch.on{transform:none}
.srch-top{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);padding:14px 20px;
  display:flex;align-items:center;gap:12px;z-index:2}
.srch-top input{flex:1;border:1.4px solid #d9d9d9;border-radius:26px;padding:11px 16px;outline:none;font-size:14px}
.srch-in{max-width:900px;margin:0 auto;padding:0 20px}
.srch .hd{font-size:12px;font-weight:800;text-transform:uppercase;color:var(--muted);margin:22px 0 4px}
.srch .row{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:13px 2px;
  border-bottom:1px solid var(--soft2);font-size:14px;font-weight:600}
.srch .row .ar{color:var(--muted);font-size:15px}
.srch .row:hover{color:var(--brand)}
.srch .row .q{color:var(--brand)}
.srch-prods{display:flex;gap:14px;overflow-x:auto;padding:6px 2px 4px;scrollbar-width:none}
.srch-prods::-webkit-scrollbar{display:none}
.srch-prods a{width:150px;flex:0 0 auto}
.srch-prods img{width:100%;aspect-ratio:1/1.3;object-fit:cover;border-radius:8px;background:var(--soft)}
.srch-prods .n{font-size:12px;font-weight:600;margin-top:7px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.srch-prods .p{font-size:13px;font-weight:800;margin-top:3px}

/* ---------- mobile drawer ---------- */
.drw{position:fixed;top:0;bottom:0;left:0;width:min(88vw,380px);background:#fff;z-index:410;
  transform:translateX(-100%);transition:transform .28s cubic-bezier(.2,.8,.2,1);display:flex;flex-direction:column}
.drw.on{transform:none}
.drw-hd{display:flex;align-items:center;justify-content:space-between;padding:16px 18px;border-bottom:1px solid var(--line)}
.drw-pills{display:flex;gap:8px;padding:12px 16px;border-bottom:1px solid var(--line);
  background:var(--soft);flex:0 0 auto}
.drw-pills button{position:relative;flex:1;padding:9px 6px;border-radius:22px;border:1px solid var(--line);
  background:#fff;font-size:13px;font-weight:700;color:#444;transition:.15s}
.drw-pills button.on{background:var(--ink);border-color:var(--ink);color:#fff}
.drw-pills .badge{position:absolute;top:-8px;left:50%;transform:translateX(-50%);background:var(--brand);
  color:#fff;font-size:8px;font-weight:800;letter-spacing:.06em;padding:2px 5px;border-radius:3px;
  font-style:normal}
.drw-body{flex:1;overflow:auto;-webkit-overflow-scrolling:touch}
.dall{display:block;margin:14px 16px 4px;text-align:center;background:var(--brand);color:#fff;
  font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:12px;border-radius:8px}
.dgrp{padding:14px 16px 4px}
.dhd{font-size:12px;font-weight:800;color:var(--brand);margin-bottom:10px}
.dgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px 10px}
.dgrid a{display:flex;align-items:center;gap:9px;font-size:12px;font-weight:600;color:#333;line-height:1.25}
.dgrid img{width:34px;height:42px;object-fit:cover;border-radius:5px;background:var(--soft);flex:0 0 34px}
.dpromo{display:flex;gap:9px;overflow-x:auto;padding:14px 16px 4px;scrollbar-width:none}
.dpromo::-webkit-scrollbar{display:none}
.dpromo a{position:relative;flex:0 0 60%;border-radius:9px;overflow:hidden;background:var(--soft)}
.dpromo img{width:100%;aspect-ratio:230/110;object-fit:cover}
.dpromo span{position:absolute;left:10px;bottom:8px;color:#fff;font-size:11px;font-weight:800;
  text-shadow:0 1px 4px rgba(0,0,0,.5)}
.drw-links{margin-top:12px;border-top:1px solid var(--line)}
.drw-links a{display:flex;align-items:center;justify-content:space-between;width:100%;
  padding:14px 18px;font-size:13.5px;font-weight:600;border-bottom:1px solid #f2efec;color:#2a2a2a}
.drw-links a span{color:#bbb}
.drw-foot{border-top:1px solid var(--line);padding:14px 18px;display:grid;gap:8px;font-size:12px;color:var(--muted)}

/* ---------- buttons ---------- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 24px;border-radius:28px;
  font-size:12.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;transition:.16s;
  border:1.5px solid transparent;cursor:pointer}
.btn-p{background:var(--brand);color:#fff}
.btn-p:hover{background:var(--brand-dk)}
.btn-d{background:var(--ink);color:#fff}
.btn-d:hover{background:#333}
.btn-o{border-color:var(--ink);color:var(--ink);background:#fff}
.btn-o:hover{background:var(--ink);color:#fff}
.btn-blk{width:100%}

/* ---------- hero ---------- */
.hero{position:relative}
.hero img{width:100%;aspect-ratio:1440/620;object-fit:cover;object-position:center 50%}
.hero .cap{position:absolute;left:0;right:0;bottom:16%;text-align:center}
.hero .cap a{display:inline-block;background:rgba(35,35,35,.82);color:#fff;font-size:12.5px;font-weight:600;
  padding:8px 20px;border-radius:4px}
.hero .cap a:hover{background:var(--brand)}

/* ---------- trust ---------- */
.trust{background:var(--soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.trust ul{display:flex;justify-content:center;margin:0;padding:0;list-style:none}
.trust li{display:flex;align-items:center;gap:11px;padding:18px 56px;font-size:13px;font-weight:600;position:relative}
.trust li+li::before{content:"";position:absolute;left:0;top:24%;bottom:24%;width:1px;background:#dcdcdc}
.trust svg{color:var(--brand);flex-shrink:0}

/* ---------- sections ---------- */
.sec{padding:42px 0}
.sec.tight{padding:28px 0}
.sec.grey{background:var(--soft)}
.sec-hd{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:18px}
.sec-hd h2{font-size:clamp(18px,2.1vw,25px)}
.sec-hd .sub{font-size:12.5px;color:var(--muted);font-weight:500;margin-top:5px}
.sec-hd a.more{font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  border-bottom:2px solid var(--brand);padding-bottom:2px;white-space:nowrap}
.tabs{display:flex;gap:26px;margin-bottom:18px;overflow:auto;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tabs button{padding:0 0 8px;font-size:13px;font-weight:600;color:var(--muted);
  border-bottom:2px solid transparent;white-space:nowrap}
.tabs button.on{color:var(--brand);border-color:var(--brand)}
.pilltabs{display:flex;gap:10px;margin-bottom:18px;overflow:auto;scrollbar-width:none}
.pilltabs::-webkit-scrollbar{display:none}
.pilltabs button{padding:8px 20px;border-radius:22px;border:1px solid var(--line);font-size:12.5px;
  font-weight:600;white-space:nowrap;background:#fff}
.pilltabs button.on{background:var(--brand);color:#fff;border-color:var(--brand)}

/* category tiles */
/* ---------- category grid ---------- */
.catsec .tabs{gap:30px}
.cat{position:relative;display:block}
.cat .ci{position:relative;overflow:hidden;border-radius:8px;background:var(--soft2);
  aspect-ratio:1/1.05}
.cat .ci img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  transition:transform .45s ease}
.cat:hover .ci img{transform:scale(1.045)}
.cat .sale{position:absolute;top:10px;left:10px;z-index:2;background:var(--sale);color:#fff;
  font-size:10px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:5px 10px;
  border-radius:4px;box-shadow:0 2px 8px rgba(0,0,0,.18);line-height:1}
.cat .sale.new{background:var(--ink)}
.cat .n{font-size:13px;font-weight:600;text-align:center;margin-top:10px;line-height:1.35;
  display:flex;align-items:center;justify-content:center;gap:5px;min-height:36px}
.cat:hover .n{color:var(--brand)}
.cat .n .ar{color:var(--muted);font-size:11px;transition:transform .2s}
.cat:hover .n .ar{transform:translateX(3px);color:var(--brand)}

.catwrap{position:relative}
.cats{display:grid;grid-auto-flow:column;grid-template-rows:repeat(2,auto);
  grid-auto-columns:calc((100% - 3*18px)/4);gap:22px 18px;overflow-x:auto;
  scroll-snap-type:x proximity;scroll-behavior:smooth;scrollbar-width:none;padding-bottom:2px}
.cats::-webkit-scrollbar{display:none}
.cats>.cat{scroll-snap-align:start}
.catwrap .arw{position:absolute;top:32%;width:38px;height:38px;border-radius:50%;
  background:#fff;box-shadow:0 2px 12px rgba(0,0,0,.18);display:none;place-items:center;
  z-index:4;font-size:17px;transform:translateY(-50%)}
.catwrap.scrollable .arw{display:grid}
.catwrap .arw.l{left:-16px}
.catwrap .arw.r{right:-16px}
@container (max-width:900px){.catwrap .arw{width:32px;height:32px;font-size:15px;top:27%}
  .catwrap .arw.l{left:-6px}.catwrap .arw.r{right:-6px}}
@media (max-width:900px){.catwrap .arw{width:32px;height:32px;font-size:15px;top:27%}
  .catwrap .arw.l{left:-6px}.catwrap .arw.r{right:-6px}}
.catwrap .arw:hover{background:var(--ink);color:#fff}

/* price bands */
.bands{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.band{background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.band img{width:100%;aspect-ratio:4/3.1;object-fit:cover}
.band .lb{padding:9px 6px;text-align:center;font-size:12px;font-weight:700}
.band:hover .lb{color:var(--brand)}

/* coverflow spotlight */
.cover{position:relative;padding:0 44px}
.cover-vp{overflow:hidden}
.cover-tr{display:flex;transition:transform .4s cubic-bezier(.2,.8,.2,1)}
.cover-tr>a{flex:0 0 33.333%;padding:10px;transition:.4s}
.cover-tr>a .im{position:relative;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,.10)}
.cover-tr>a img{width:100%;aspect-ratio:16/9.2;object-fit:cover;filter:brightness(.94)}
.cover-tr>a:not(.mid){transform:scale(.88);opacity:.72}
.cover-tr>a.mid{transform:scale(1.02);z-index:2;position:relative}
.cover .ov{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
  padding:0 28px;color:#fff}
.cover .ov b{font-size:clamp(13px,1.5vw,19px);font-weight:800;line-height:1.2;max-width:62%;
  text-shadow:0 2px 10px rgba(0,0,0,.4)}
.cover .ov span{font-size:11px;margin-top:5px;opacity:.92;text-shadow:0 1px 8px rgba(0,0,0,.5)}
.cover .ov i{margin-top:10px;background:#fff;color:#1a1a1a;font-style:normal;font-size:10.5px;font-weight:800;
  padding:7px 14px;border-radius:3px;align-self:flex-start}
.cover .arw{position:absolute;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:50%;
  background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.18);display:grid;place-items:center;z-index:5;font-size:16px}
.cover .arw.l{left:2px}
.cover .arw.r{right:2px}
.dots{display:flex;gap:7px;justify-content:center;margin-top:16px}
.dots i{width:7px;height:7px;border-radius:50%;background:#d5d5d5;cursor:pointer;display:block}
.dots i.on{background:var(--brand);width:20px;border-radius:4px}

/* stats */
.stats{display:grid;grid-template-columns:repeat(4,1fr)}
.stats>div{padding:22px 28px;position:relative}
.stats>div+div::before{content:"";position:absolute;left:0;top:26%;bottom:26%;width:1px;background:#dcdcdc}
.stats .n{font-size:clamp(17px,2vw,22px);font-weight:800}
.stats .l{font-size:12px;font-weight:500;color:var(--muted);margin-top:4px}

/* ---------- product card ---------- */
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 18px}
.grid.g5{grid-template-columns:repeat(5,1fr)}
.railrow{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;padding-bottom:4px;scroll-behavior:smooth}
.railrow::-webkit-scrollbar{display:none}
.railrow>.card{flex:0 0 calc((100% - 3*16px)/4);scroll-snap-align:start}
.carou{position:relative}
.carou .arw{position:absolute;top:34%;width:38px;height:38px;border-radius:50%;background:#fff;
  box-shadow:0 2px 12px rgba(0,0,0,.18);display:none;place-items:center;z-index:4;font-size:17px;
  transform:translateY(-50%)}
.carou.scrollable .arw{display:grid}
.carou .arw:hover{background:var(--ink);color:#fff}
.carou .arw.l{left:-16px}
.carou .arw.r{right:-16px}
@container (max-width:900px){.carou .arw{width:32px;height:32px;font-size:15px;top:30%}
  .carou .arw.l{left:-6px}.carou .arw.r{right:-6px}}
@media (max-width:900px){.carou .arw{width:32px;height:32px;font-size:15px;top:30%}
  .carou .arw.l{left:-6px}.carou .arw.r{right:-6px}}
.card{position:relative;display:flex;flex-direction:column}
.card .imgwrap{position:relative;overflow:hidden;background:var(--soft);aspect-ratio:1/1.32;border-radius:var(--r)}
.card .imgwrap img{width:100%;height:100%;object-fit:cover;transition:opacity .3s}
.card .imgwrap img.alt{position:absolute;inset:0;opacity:0}
.card:hover .imgwrap img.alt{opacity:1}
.card .tag{position:absolute;top:0;left:0;background:var(--brand);color:#fff;font-size:9px;font-weight:700;
  padding:4px 9px;border-bottom-right-radius:6px;z-index:2}
.card .tag.dk{background:var(--ink)}
.card .wish{position:absolute;top:8px;right:8px;width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,.94);
  display:grid;place-items:center;box-shadow:0 2px 8px rgba(0,0,0,.10);z-index:3}
.card .wish.on{color:var(--brand)}
.card .eye{position:absolute;right:10px;bottom:10px;width:34px;height:34px;border-radius:50%;
  background:rgba(255,255,255,.95);display:grid;place-items:center;box-shadow:0 2px 8px rgba(0,0,0,.14);z-index:3}
.card .eye:hover{background:var(--brand);color:#fff}
.card .meta{padding:9px 0 0;display:flex;flex-direction:column;flex:1}
.card .nm{font-size:13px;font-weight:600;line-height:1.35;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
  min-height:35px;margin:0}
.card .pr{display:flex;align-items:baseline;gap:7px;flex-wrap:nowrap;margin-top:7px;
  white-space:nowrap;overflow:hidden}
.card .pr b{font-size:14px;font-weight:700;flex:0 0 auto}
.card .pr s{font-size:11.5px;color:var(--muted);flex:0 0 auto}
.card .pr em{font-style:normal;font-size:9.5px;font-weight:800;color:#fff;background:var(--sale);
  padding:3px 5px;border-radius:3px;flex:0 1 auto;overflow:hidden;text-overflow:ellipsis}
.card .rt{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--muted);font-weight:600;margin-top:6px}
.card .rt .stars{color:#f0a500;letter-spacing:-1px}
.card .rt b{color:var(--ink)}
.dots-c{position:absolute;left:8px;right:auto;bottom:8px;z-index:3;display:inline-flex;gap:6px;
  width:max-content;max-width:calc(100% - 16px);
  align-items:center;flex-wrap:nowrap;overflow:hidden;padding:6px 9px;border-radius:20px;
  background:rgba(255,255,255,.82);backdrop-filter:blur(6px);
  box-shadow:0 2px 8px rgba(0,0,0,.10)}
.dots-c i{flex:0 0 auto;width:15px;height:15px;border-radius:50%;
  box-shadow:0 0 0 1px rgba(0,0,0,.18) inset;cursor:pointer;display:block}
.dots-c i.on{box-shadow:0 0 0 1.5px #fff inset,0 0 0 2.5px var(--ink)}
.dots-c .plus{flex:0 0 auto;width:auto;height:auto;font-size:10.5px;font-weight:700;
  color:var(--muted);font-style:normal;box-shadow:none;border-radius:0;cursor:default;
  margin-left:1px;white-space:nowrap}
.card .nudge{font-size:10.5px;font-weight:700;color:var(--brand);margin-top:6px;margin-bottom:10px}


.card .rate{position:absolute;right:8px;top:8px;z-index:3;background:rgba(255,255,255,.95);
  border-radius:5px;padding:4px 9px;font-size:11px;font-weight:800;display:inline-flex;
  align-items:center;gap:5px;box-shadow:0 2px 8px rgba(0,0,0,.14);line-height:1}
.card .rate .st{color:#f0a500;font-size:12px}
.card .rate i{font-style:normal;color:var(--muted);font-weight:600;font-size:10.5px}
.ctarow{display:flex;gap:8px;margin-top:11px}
.atcbtn{flex:0 0 70%;padding:10px 6px;border:1.4px solid var(--ink);border-radius:5px;
  background:#fff;color:var(--ink);font-size:11.5px;font-weight:800;letter-spacing:.04em;
  text-transform:uppercase;transition:.16s;white-space:nowrap;overflow:hidden}
.atcbtn:hover{background:var(--ink);color:#fff}
.wishbtn{flex:1 1 auto;display:grid;place-items:center;border:1.4px solid var(--line);
  border-radius:5px;background:#fff;color:#555;transition:.16s}
.wishbtn:hover{border-color:var(--ink);color:var(--ink)}
.wishbtn.on{color:var(--brand);border-color:var(--brand);background:#fff5fa}

/* bestsellers rail */
.bsrail{display:flex;gap:18px;overflow-x:auto;scroll-behavior:smooth;scrollbar-width:none;
  scroll-snap-type:x proximity;padding-bottom:2px}
.bsrail::-webkit-scrollbar{display:none}
.bsrail>.card{flex:0 0 calc((100% - 3*18px)/4);scroll-snap-align:start}

/* shade spectrum */
.spectrum{max-width:760px;margin:22px auto 0}
.spectrum input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:9px;border-radius:6px;
  outline:none;background:linear-gradient(90deg,#111,#7a4a2a,#c2185b,#e6007e,#f0a500,#d4af37,#3aa655,
    #1f7a7a,#2f5fa8,#6b4a86,#f4c2ce,#ffffff)}
.spectrum input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:20px;height:20px;border-radius:50%;
  background:#fff;box-shadow:0 1px 6px rgba(0,0,0,.35);cursor:pointer;border:2px solid #fff}
.spectrum input[type=range]::-moz-range-thumb{width:20px;height:20px;border-radius:50%;background:#fff;
  box-shadow:0 1px 6px rgba(0,0,0,.35);cursor:pointer;border:2px solid #fff}
.spectrum .chip{display:inline-flex;align-items:center;gap:7px;margin-top:12px;background:var(--soft);
  border-radius:4px;padding:5px 11px;font-size:11px;font-weight:700}
.spectrum .chip i{width:11px;height:11px;border-radius:2px;box-shadow:0 0 0 1px rgba(0,0,0,.15) inset;display:block}

/* ---------- reviews ---------- */
.revs{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.rev{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:20px}
.rev .st{color:#f0a500;font-size:14px;letter-spacing:1px}
.rev p{font-size:13px;line-height:1.6;margin:10px 0 14px;color:#333}
.rev .who{font-size:12px;font-weight:700}
.rev .who span{color:var(--muted);font-weight:500}
.rev .vf{display:inline-flex;gap:4px;font-size:10px;font-weight:800;color:var(--ok);
  text-transform:uppercase;margin-top:8px}
.revsum{display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:20px;
  font-size:12.5px;font-weight:600;color:var(--muted)}
.revsum .stars{color:#f0a500}
.revsum .vf{color:var(--ok);font-weight:800}

/* ---------- footer ---------- */
.shopbar{background:#0d0d0d;color:#e2e2e2;padding:20px 0}
.shopbar h4{font-size:12px;letter-spacing:.1em;margin-bottom:9px;color:#fff}
.shopbar .lks{font-size:12px;line-height:2;color:#b5b5b5}
.shopbar .lks a:hover{color:#fff}
.shopbar .sep{color:#5a5a5a;margin:0 7px}
.ftr{background:#fff;padding:34px 0 0;border-top:1px solid var(--line)}
.ftr-grid{display:grid;grid-template-columns:1.1fr 1fr 1fr 1.2fr;gap:30px}
.ftr h4{font-size:14px;margin-bottom:14px}
.ftr ul{list-style:none;margin:0;padding:0;display:grid;gap:9px}
.ftr a{font-size:12.5px;color:#4a4a4a}
.ftr a:hover{color:var(--brand)}
.ftr .soc{display:flex;gap:9px;margin-top:16px}
.ftr .soc a{width:28px;height:28px;border-radius:50%;border:1px solid var(--line);display:grid;
  place-items:center;font-size:10px;font-weight:800;color:#555}
.ftr .soc a:hover{background:var(--brand);border-color:var(--brand);color:#fff}
.ftr .cx{display:flex;gap:9px;align-items:flex-start;font-size:12.5px;color:#4a4a4a;line-height:1.5;margin-bottom:10px}
.ftr .cx svg{flex-shrink:0;margin-top:2px;color:var(--muted)}
.ftr .bot{border-top:1px solid var(--line);margin-top:30px;padding:16px 0;display:flex;
  justify-content:space-between;gap:14px;flex-wrap:wrap;font-size:11.5px;color:#777}
.ftr .bot a{font-size:11.5px;color:#777;margin-right:16px}
.appfab{position:fixed;left:18px;bottom:18px;background:var(--brand);color:#fff;border-radius:24px;
  padding:11px 20px;font-size:12px;font-weight:800;z-index:180;box-shadow:0 6px 20px rgba(230,0,126,.35)}

/* ---------- mobile tab bar ---------- */
.tabbar{display:none;position:fixed;left:0;right:0;bottom:0;height:58px;background:#fff;
  border-top:1px solid var(--line);z-index:200;justify-content:space-around;align-items:center}
.tabbar a{display:grid;place-items:center;color:#555;position:relative;flex:1;height:100%}
.tabbar a.on{color:var(--brand)}
.tabbar a.on::after{content:"";position:absolute;bottom:6px;width:16px;height:2px;background:var(--brand)}
.tabbar .cnt{position:absolute;top:10px;right:26%;min-width:15px;height:15px;border-radius:8px;
  background:var(--brand);color:#fff;font-size:9px;display:grid;place-items:center;font-weight:800}

/* ---------- side drawers ---------- */
.side{position:fixed;top:0;bottom:0;right:0;width:min(94vw,430px);background:#fff;z-index:420;display:flex;
  flex-direction:column;transform:translateX(100%);transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.side.on{transform:none}
.side-hd{display:flex;align-items:center;gap:12px;padding:15px 18px;border-bottom:1px solid var(--line)}
.side-hd h3{font-size:15px;flex:1;text-align:center}
.side-hd .bk{font-size:20px;line-height:1}
.steps{display:flex;align-items:center;gap:8px;padding:12px 18px;font-size:11px;font-weight:700;color:var(--muted)}
.steps .s{display:flex;align-items:center;gap:6px}
.steps .s i{width:7px;height:7px;border-radius:50%;background:#d2d2d2;display:block}
.steps .s.on{color:var(--ok)}
.steps .s.on i{background:var(--ok)}
.steps .ln{flex:1;height:1px;background:#e0e0e0}
.tchips{display:flex;justify-content:space-around;gap:8px;padding:12px 14px;border-bottom:1px solid var(--line)}
.tchips div{display:flex;align-items:center;gap:7px;font-size:10.5px;font-weight:600;line-height:1.25}
.tchips svg{color:var(--brand);flex-shrink:0}
.ship{padding:12px 18px;background:var(--soft);border-bottom:1px solid var(--line)}
.ship .t{font-size:12px;font-weight:700;margin-bottom:7px}
.ship .t b{color:var(--ok)}
.ship .bar{height:6px;border-radius:4px;background:#e0dedb;overflow:hidden}
.ship .bar i{display:block;height:100%;background:var(--ok);border-radius:4px;transition:width .35s}
.side-body{flex:1;overflow:auto;padding:4px 18px 14px}
.ci{display:flex;gap:13px;padding:15px 0;border-bottom:1px solid var(--soft2);position:relative}
.ci img{width:82px;aspect-ratio:1/1.3;object-fit:cover;border-radius:6px;background:var(--soft)}
.ci .bd{flex:1}
.ci .n{font-size:13px;font-weight:700;line-height:1.35;padding-right:22px}
.ci .p{font-size:13.5px;font-weight:800;margin-top:5px}
.ci .p s{font-size:11.5px;color:var(--muted);font-weight:600;margin-right:6px}
.ci .rowb{display:flex;align-items:center;gap:10px;margin-top:9px;flex-wrap:wrap}
.ci .szsel{border:1px solid var(--line);border-radius:5px;padding:5px 8px;font-size:11.5px;font-weight:700}
.qty{display:inline-flex;align-items:center;border:1px solid var(--line);border-radius:20px}
.qty button{width:27px;height:27px;font-size:15px;color:var(--muted)}
.qty span{min-width:22px;text-align:center;font-size:12px;font-weight:800}
.ci .rm{position:absolute;top:15px;right:0;width:20px;height:20px;border-radius:50%;background:var(--sale);
  color:#fff;font-size:12px;line-height:1;display:grid;place-items:center}
.ci .lnk{font-size:11px;font-weight:700;color:var(--muted);text-decoration:underline}
.ci .ret{font-size:10.5px;color:var(--muted);font-weight:600;margin-top:6px}
.side-empty{text-align:center;padding:60px 20px;color:var(--muted)}
.osum{padding:14px 18px;border-top:8px solid var(--soft)}
.osum h4{font-size:14px;margin-bottom:10px}
.osum .r{display:flex;justify-content:space-between;padding:7px 0;font-size:12.5px;font-weight:600;color:#444}
.osum .r b{color:var(--ink)}
.osum .r.free b{color:var(--ok)}
.osum .r.tot{border-top:1px solid var(--line);margin-top:6px;padding-top:11px;font-size:14px}
.osum .r.tot b{color:var(--brand);font-size:15px}
.rail{padding:14px 18px;border-top:8px solid var(--soft)}
.rail .hd{font-size:13px;font-weight:700;margin-bottom:10px}
.rail .r{display:flex;gap:10px;overflow:auto;scrollbar-width:none}
.rail .r::-webkit-scrollbar{display:none}
.rail .r>div{width:98px;flex-shrink:0;cursor:pointer}
.rail img{width:100%;aspect-ratio:1/1.3;object-fit:cover;border-radius:6px}
.rail .p{font-size:10.5px;font-weight:700;margin-top:5px;line-height:1.3}
.rail .a{font-size:10px;font-weight:800;color:var(--brand);margin-top:3px}
.side-ft{border-top:1px solid var(--line);padding:12px 18px 16px;background:#fff;box-shadow:0 -6px 18px rgba(0,0,0,.05)}
.coup{display:flex;gap:8px;margin-bottom:10px}
.coup input{flex:1;border:1px solid var(--line);border-radius:22px;padding:10px 15px;outline:none}
.coup button{padding:0 17px;border-radius:22px;border:1.5px solid var(--ink);font-size:11px;font-weight:800;
  letter-spacing:.05em;text-transform:uppercase}
.side-ft .note{font-size:10.5px;color:var(--muted);text-align:center;margin-top:8px;font-weight:600}
.side-ft .ok{color:var(--ok);font-weight:800;font-size:11.5px;margin-bottom:8px;text-align:center}
.side-ft .two{display:flex;gap:10px}
.side-ft .two .btn{flex:1;padding:12px 10px;font-size:11px}
.wl-sel{display:flex;gap:9px;padding:12px 18px;border-bottom:1px solid var(--line);background:var(--soft)}
.wl-sel select{flex:1;border:1px solid var(--line);border-radius:5px;padding:8px 11px;font-weight:600;background:#fff}
.wl-sel button{width:34px;background:var(--ink);color:#fff;border-radius:5px;font-size:17px}

/* ---------- modal ---------- */
.mod{position:fixed;inset:0;z-index:430;display:none;place-items:center;padding:20px}
.mod.on{display:grid}
.mod-box{background:#fff;border-radius:12px;width:min(720px,100%);max-height:88vh;overflow:auto;position:relative;
  display:grid;grid-template-columns:250px 1fr}
.mod-box img.hero{width:100%;height:100%;object-fit:cover;border-radius:12px 0 0 12px;background:var(--soft)}
.mod-body{padding:26px}
.mod .x{position:absolute;top:12px;right:14px;font-size:24px;line-height:1;color:var(--muted);z-index:2}
.mod h3{font-size:17px;line-height:1.35}
.mod .pr{display:flex;align-items:baseline;gap:9px;margin:10px 0 4px}
.mod .pr b{font-size:20px}
.mod .pr s{color:var(--muted);font-size:13px}
.mod .pr em{font-style:normal;color:#fff;background:var(--sale);font-weight:800;font-size:11px;padding:3px 7px;border-radius:3px}
.opt{margin-top:18px}
.opt .lb{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  margin-bottom:9px;display:flex;justify-content:space-between;align-items:center}
.opt .lb a{color:var(--brand);text-transform:none;letter-spacing:0;font-size:11px;text-decoration:underline}
.szrow{display:flex;flex-wrap:wrap;gap:8px}
.szrow button{min-width:40px;height:40px;padding:0 11px;border:1.4px solid var(--line);border-radius:50%;
  font-size:12px;font-weight:700}
.szrow button.on{border-color:var(--ink);background:var(--ink);color:#fff}
.szrow button.oos{opacity:.34;text-decoration:line-through}
.cdotsm{display:flex;gap:9px;flex-wrap:wrap}
.cdotsm button{width:30px;height:30px;border-radius:50%;box-shadow:0 0 0 1px rgba(0,0,0,.16) inset;padding:0}
.cdotsm button.on{box-shadow:0 0 0 2px #fff inset,0 0 0 3px var(--ink)}
.mod .trustline{display:flex;gap:14px;flex-wrap:wrap;margin-top:16px;font-size:11px;font-weight:700;color:var(--muted)}
.mod .full{display:block;text-align:center;font-size:12px;font-weight:700;text-decoration:underline;
  margin-top:14px;color:var(--muted)}
.err{color:var(--brand);font-size:11.5px;font-weight:700;margin-top:9px;display:none}
.err.on{display:block}

/* ---------- toast ---------- */
.toast{position:fixed;left:50%;bottom:26px;transform:translate(-50%,20px);background:var(--ink);color:#fff;
  padding:12px 22px;border-radius:28px;font-size:12.5px;font-weight:700;z-index:500;opacity:0;
  transition:.25s;pointer-events:none;box-shadow:0 10px 30px rgba(0,0,0,.25)}
.toast.on{opacity:1;transform:translate(-50%,0)}

/* ---------- PLP ---------- */
.crumb{font-size:11.5px;color:var(--muted);padding:12px 0;font-weight:600}
.crumb b{color:var(--brand);font-weight:700}
.plp{display:grid;grid-template-columns:230px 1fr;gap:26px;padding-bottom:40px}
.side-f{border-right:1px solid var(--line);padding-right:18px}
.side-f>h3{font-size:14px;letter-spacing:.04em;padding-bottom:12px;border-bottom:1px solid var(--line)}
.fgrp{border-bottom:1px solid var(--soft2);padding:12px 0}
.fgrp>summary{list-style:none;display:flex;align-items:center;gap:7px;font-size:12.5px;font-weight:700;cursor:pointer}
.fgrp>summary::-webkit-details-marker{display:none}
.fgrp>summary::before{content:"▾";font-size:9px;color:var(--muted);transition:transform .18s}
.fgrp:not([open])>summary::before{transform:rotate(-90deg)}
.fgrp .bd{padding:11px 0 3px;max-height:190px;overflow:auto}
.fchk{display:flex;align-items:center;gap:8px;padding:5px 0;font-size:12px;color:#444;cursor:pointer}
.fchk input{width:13px;height:13px;accent-color:var(--brand);margin:0}
.fchk .ct{margin-left:auto;color:var(--muted);font-size:11px}
.fchk:hover{color:var(--ink)}
.fcols{display:grid;grid-template-columns:repeat(5,1fr);gap:9px;padding:11px 0 3px}
.fcols i{width:20px;height:20px;border-radius:50%;box-shadow:0 0 0 1px rgba(0,0,0,.18) inset;cursor:pointer;display:block}
.fcols i.on{box-shadow:0 0 0 2px #fff inset,0 0 0 3.5px var(--ink)}
.fsz{display:flex;flex-wrap:wrap;gap:7px;padding:11px 0 3px}
.fsz button{min-width:30px;padding:6px 8px;border:1px solid var(--line);border-radius:4px;font-size:11px;font-weight:700}
.fsz button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.frange{padding:14px 2px 3px}
.frange input{width:100%;accent-color:var(--ink)}
.frange .lb{display:flex;justify-content:space-between;font-size:11px;color:var(--muted);font-weight:600;margin-top:6px}
.plp-top{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:2px 0 14px}
.plp-top .cnt{font-size:12.5px;color:var(--muted);font-weight:600}
.sortsel{border:1px solid var(--line);border-radius:4px;padding:9px 12px;font-weight:600;font-size:12.5px;
  background:#fff;outline:none;cursor:pointer}
.chips{display:flex;gap:8px;flex-wrap:wrap;padding:0 0 14px}
.chips .c{background:var(--soft);border-radius:16px;padding:6px 12px;font-size:11.5px;font-weight:700;
  display:inline-flex;align-items:center;gap:7px}
.chips .clr{font-size:11.5px;font-weight:800;color:var(--brand);text-decoration:underline;align-self:center}
.mfilter{display:none;gap:0;padding:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
  position:sticky;top:calc(var(--barh) + 60px);background:#fff;z-index:60}
.mfilter button{flex:1;padding:12px;font-size:12px;font-weight:700;display:flex;align-items:center;
  justify-content:center;gap:7px}
.mfilter button+button{border-left:1px solid var(--line)}
.loadmore{text-align:center;padding:22px 0 10px}
.sheet{position:fixed;left:0;right:0;bottom:0;background:#fff;z-index:420;border-radius:16px 16px 0 0;
  transform:translateY(100%);transition:transform .3s cubic-bezier(.2,.8,.2,1);max-height:82vh;
  display:flex;flex-direction:column}
.sheet.on{transform:none}
.sheet .hd{display:flex;align-items:center;justify-content:space-between;padding:15px 20px;border-bottom:1px solid var(--line)}
.sheet .bd{overflow:auto;padding:4px 20px 16px}
.sheet .ft{padding:12px 20px 18px;border-top:1px solid var(--line);display:flex;gap:10px}
.sheet .ft .btn{flex:1}

/* ---------- PDP ---------- */
.pdp{display:grid;grid-template-columns:1.08fr .92fr;gap:34px;padding:6px 0 10px;align-items:start}
.pgal{display:grid;grid-template-columns:1fr 1fr;gap:8px;position:relative}
.pgal img{width:100%;aspect-ratio:1/1.32;object-fit:cover;background:var(--soft)}
.pgal .tg{position:absolute;top:0;left:0;background:var(--brand);color:#fff;font-size:9.5px;font-weight:700;
  padding:4px 10px;border-bottom-right-radius:6px;z-index:3}
.pgal .tryon{position:absolute;top:10px;right:10px;background:#fff;border-radius:18px;padding:6px 13px;
  font-size:11px;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.14);z-index:3;display:flex;align-items:center;gap:6px}
.storyring{position:absolute;left:12px;top:44px;width:58px;height:58px;border-radius:50%;padding:3px;
  background:conic-gradient(var(--brand),#f0a500,var(--brand));display:grid;place-items:center;cursor:pointer;
  z-index:4;animation:pulse 2.4s ease-in-out infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(230,0,126,.42)}50%{box-shadow:0 0 0 10px rgba(230,0,126,0)}}
.storyring .in{width:100%;height:100%;border-radius:50%;background:#fff;display:grid;place-items:center;
  font-size:8px;font-weight:800;text-align:center;line-height:1.15;padding:3px}
.pdp-info h1{font-size:clamp(17px,1.9vw,21px);line-height:1.35}
.pdp-info .sku{font-size:11.5px;color:var(--muted);font-weight:600;margin-top:5px}
.pdp-rt{display:flex;align-items:center;gap:7px;margin-top:9px;font-size:12px;font-weight:700;color:var(--muted)}
.pdp-rt .stars{color:#f0a500}
.pdp-mrp{margin:12px 0 2px;font-size:13px;font-weight:600;color:#333}
.pdp-mrp b{font-size:19px;font-weight:800}
.pdp-mrp s{color:var(--muted);font-weight:600;margin-left:7px;font-size:13px}
.pdp-mrp em{font-style:normal;background:var(--sale);color:#fff;font-size:11px;font-weight:800;
  padding:3px 7px;border-radius:3px;margin-left:7px}
.pdp-tax{font-size:10.5px;color:var(--muted);font-weight:600}
.rew{background:#141414;color:#fff;border-radius:8px;overflow:hidden;margin-top:14px}
.rew .t{background:#000;padding:9px 14px;font-size:12px;font-weight:700;display:flex;align-items:center;gap:8px}
.rew .t i{background:#fff;color:#000;font-style:normal;font-size:9px;font-weight:800;padding:2px 5px;border-radius:2px}
.rew .b{padding:13px 14px}
.rew p{margin:0 0 12px;font-size:12px;color:#d6d6d6;line-height:1.5}
.rew .jb{width:100%;background:#fff;color:#000;border-radius:4px;padding:12px;font-size:11.5px;font-weight:800;
  letter-spacing:.05em;text-transform:uppercase}
.rew .fine{font-size:10.5px;color:#9a9a9a;margin:10px 0 0;text-align:center}
.rew .fine b{color:var(--brand)}
.pbox{border:1px solid var(--line);border-radius:8px;padding:14px;margin-top:14px}
.pbox .h{display:flex;align-items:center;justify-content:space-between;font-size:13px;font-weight:700;margin-bottom:11px}
.pbox .h .nav2{display:flex;gap:10px;color:var(--muted);font-size:13px}
.pbox .h a{font-size:11.5px;color:var(--brand);font-weight:700}
.cdots{display:grid;grid-template-columns:repeat(8,1fr);gap:9px}
.cdots button{width:100%;aspect-ratio:1;border-radius:50%;box-shadow:0 0 0 1px rgba(0,0,0,.16) inset;
  position:relative;padding:0}
.cdots button.on::after{content:"✓";position:absolute;inset:0;display:grid;place-items:center;color:#fff;
  font-size:11px;text-shadow:0 0 3px rgba(0,0,0,.5)}
.cdots button.on{box-shadow:0 0 0 2px #fff inset,0 0 0 3px var(--ink)}
.simw{margin-top:14px}
.simw .h{font-size:12px;font-weight:700;margin-bottom:8px}
.simc{display:flex;gap:12px}
.simc a{width:58px}
.simc img{width:100%;aspect-ratio:1/1.15;object-fit:cover;border-radius:4px;background:var(--soft)}
.simc span{display:block;font-size:9px;font-weight:600;color:var(--muted);text-align:center;margin-top:4px}
.pinbox{border:1px solid var(--line);border-radius:8px;padding:13px 14px;margin-top:14px}
.pinbox .h{font-size:12.5px;font-weight:700;margin-bottom:9px}
.pin{display:flex;align-items:center;border:1px solid var(--line);border-radius:5px;overflow:hidden}
.pin input{flex:1;border:0;padding:10px 13px;outline:none}
.pin button{padding:0 15px;color:var(--brand);font-size:12px;font-weight:800}
.pinres{font-size:11.5px;font-weight:700;color:var(--ok);margin-top:8px;display:none}
.pinres.on{display:block}
.atc{display:flex;gap:11px;margin-top:16px;align-items:center}
.atc .qty{border-radius:5px}
.atc .qty button{width:30px;height:30px}
.atc .btn{flex:1;border-radius:5px;padding:15px 20px}
.wbtn{width:48px;height:48px;border-radius:50%;border:1.4px solid var(--line);display:grid;place-items:center;flex:0 0 auto}
.wbtn.on{color:var(--brand);border-color:var(--brand)}
.usp3{display:flex;justify-content:space-between;gap:10px;margin-top:16px}
.usp3 div{display:flex;align-items:center;gap:8px;font-size:10.5px;font-weight:600;line-height:1.25}
.usp3 svg{color:var(--brand);flex-shrink:0}
.acc{margin-top:18px;border-top:1px solid var(--line)}
.acc details{border-bottom:1px solid var(--line)}
.acc summary{padding:15px 2px;font-size:13px;font-weight:600;cursor:pointer;list-style:none;
  display:flex;justify-content:space-between;align-items:center;gap:14px}
.acc summary::-webkit-details-marker{display:none}
.acc summary::after{content:"⌄";font-size:15px;color:var(--muted)}
.acc details[open] summary::after{content:"⌃"}
.acc .ab{padding:0 2px 18px;font-size:12.5px;color:#444;line-height:1.7}
.acc .ab ul{margin:10px 0 0;padding-left:18px}
.acc .dl div{display:flex;justify-content:space-between;gap:14px;padding:8px 0;border-bottom:1px solid var(--soft2)}
.acc .dl div span:first-child{color:var(--muted)}
.acc .dl div span:last-child{font-weight:700}
.subnav{position:sticky;z-index:70;background:#fff;border-bottom:1px solid var(--line);
  opacity:0;visibility:hidden;transition:opacity .2s}
.subnav.show{opacity:1;visibility:visible}
.subnav .in{display:flex;overflow-x:auto;scrollbar-width:none;max-width:var(--maxw);margin:0 auto;padding:0 24px}
.subnav .in::-webkit-scrollbar{display:none}
.subnav button{padding:14px 17px;font-size:12px;font-weight:700;color:var(--muted);
  border-bottom:2px solid transparent;white-space:nowrap}
.subnav button.on{color:var(--ink);border-color:var(--brand)}
.pdp-sec{padding:30px 0;border-top:1px solid var(--line);scroll-margin-top:180px}
.pdp-sec h2{font-size:18px;margin-bottom:14px}
.satc{position:fixed;left:0;right:0;bottom:0;background:#fff;border-top:1px solid var(--line);z-index:150;
  transform:translateY(100%);transition:transform .25s;box-shadow:0 -6px 20px rgba(0,0,0,.07)}
.satc.on{transform:none}
.satc .in{max-width:var(--maxw);margin:0 auto;padding:10px 24px;display:flex;align-items:center;gap:14px}
.satc img{width:44px;aspect-ratio:1/1.25;object-fit:cover;border-radius:5px}
.satc .n{font-size:13px;font-weight:700;line-height:1.3}
.satc .r{font-size:11px;color:var(--muted);font-weight:600;margin-top:2px}
.satc .p{margin-left:auto;font-size:16px;font-weight:800;white-space:nowrap}
.satc .btn{white-space:nowrap;border-radius:5px}

/* stories */
.stories{position:fixed;inset:0;z-index:450;background:rgba(0,0,0,.86);display:none;place-items:center}
.stories.on{display:grid}
.st-card{width:min(400px,94vw);aspect-ratio:9/16;max-height:90vh;background:#000;border-radius:14px;
  overflow:hidden;position:relative}
.st-card>img{width:100%;height:100%;object-fit:cover}
.st-bars{position:absolute;top:10px;left:10px;right:10px;display:flex;gap:4px;z-index:3}
.st-bars i{flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.34);overflow:hidden;display:block}
.st-bars i b{display:block;height:100%;width:0;background:#fff;border-radius:2px}
.st-top{position:absolute;top:24px;left:14px;right:14px;display:flex;align-items:center;gap:9px;z-index:3;color:#fff}
.st-top .av{width:30px;height:30px;border-radius:50%;background:var(--brand);display:grid;place-items:center;
  font-size:10px;font-weight:800}
.st-top .nm{font-size:12px;font-weight:700}
.st-top .x{margin-left:auto;font-size:24px;line-height:1}
.st-nav{position:absolute;inset:0;display:flex;z-index:2}
.st-nav div{flex:1}
.st-cap{position:absolute;left:14px;right:14px;bottom:88px;color:#fff;z-index:3;font-size:15px;font-weight:800;
  text-shadow:0 2px 12px rgba(0,0,0,.6);line-height:1.35}
.st-ft{position:absolute;left:0;right:0;bottom:0;background:rgba(0,0,0,.72);backdrop-filter:blur(8px);
  padding:11px 13px;display:flex;align-items:center;gap:11px;z-index:3;color:#fff}
.st-ft img{width:38px;aspect-ratio:1/1.25;border-radius:5px;flex:0 0 auto;object-fit:cover}
.st-ft .n{font-size:11.5px;font-weight:700;line-height:1.25}
.st-ft .p{font-size:12.5px;font-weight:800;margin-top:2px}
.st-ft .btn{margin-left:auto;padding:10px 17px;font-size:10.5px;border-radius:4px}

/* wishlist page */
.wl-empty{text-align:center;padding:70px 20px}
.wl-empty h2{font-size:20px;margin-bottom:10px}
.wl-empty p{color:var(--muted);margin:0 0 22px}

/* index hub */
.hub{max-width:980px;margin:0 auto;padding:50px 24px 70px}
.hub h1{font-size:29px}
.hub .lead{color:var(--muted);margin:12px 0 30px;font-size:13.5px;line-height:1.7;max-width:680px}
.hublist{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.hublist a{border:1px solid var(--line);border-radius:12px;padding:20px;transition:.18s;display:block}
.hublist a:hover{border-color:var(--ink);transform:translateY(-2px);box-shadow:0 10px 26px rgba(0,0,0,.07)}
.hublist .n{font-size:15px;font-weight:800}
.hublist .d{font-size:12.5px;color:var(--muted);margin-top:6px;line-height:1.55}
.hub .note{margin-top:34px;padding:20px;background:var(--soft);border-radius:10px;font-size:12.5px;
  color:var(--muted);line-height:1.75}
.hub .note b{color:var(--ink)}


/* ---------- L1 audience bar (desktop nav carried into mobile) ---------- */
.l1bar{display:none;background:#fff;border-bottom:1px solid var(--line);
  position:sticky;top:calc(var(--barh) + var(--hdrm));z-index:110}
.l1bar .in{display:flex;overflow-x:auto;scrollbar-width:none}
.l1bar .in::-webkit-scrollbar{display:none}
.l1bar a{flex:1 0 auto;min-width:25%;text-align:center;padding:13px 16px;font-size:13px;
  font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#3a3a3a;
  border-bottom:2px solid transparent;white-space:nowrap}
.l1bar a.on{color:var(--ink);border-color:var(--brand)}
.l1bar a:active{background:var(--soft)}

/* ---------- split banner ---------- */
.sban{display:grid;grid-template-columns:1fr 1fr;align-items:stretch;background:var(--soft);
  min-height:clamp(430px,44vw,580px)}
.sban .im{position:relative;overflow:hidden;background:var(--soft2)}
.sban .im img{width:100%;height:100%;object-fit:cover;object-position:center 20%;position:absolute;inset:0}
.sban .bd{display:flex;flex-direction:column;justify-content:center;padding:clamp(28px,3.6vw,58px);
  background:#fff}
.sban .tag{display:inline-flex;align-self:flex-start;align-items:center;gap:7px;background:#fff3f9;
  color:var(--brand);font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
  padding:7px 14px;border-radius:20px}
.sban h1{font-size:clamp(26px,3.4vw,44px);line-height:1.12;margin:18px 0 0;letter-spacing:-.02em}
.sban .sub{font-size:clamp(13px,1.15vw,15px);color:var(--muted);line-height:1.7;margin:14px 0 0;
  max-width:46ch;font-weight:500}
.sban .ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}
.sban .ctas .btn{padding:15px 30px}
.sban .disc{font-size:11px;color:#8a8a8a;line-height:1.6;margin-top:26px;padding-top:20px;
  border-top:1px solid var(--line);
  max-width:52ch;font-weight:500}
.sban .disc b{color:#6b6b6b;font-weight:700}

/* ================= responsive ================= */
@container (max-width:1180px){
  .mcols{grid-template-columns:repeat(4,1fr)}
  .grid{grid-template-columns:repeat(3,1fr)}
  .grid.g5{grid-template-columns:repeat(4,1fr)}
  .revs{grid-template-columns:repeat(2,1fr)}
  .plp{grid-template-columns:200px 1fr}
}
@container (max-width:900px){
  .l1bar{display:block}
  .sban{grid-template-columns:1fr}
  .sban{min-height:0}
  .sban .im{aspect-ratio:4/4.2}
  .sban .im img{object-position:center 16%}
  .sban .bd{padding:26px 20px 30px}
  .sban .ctas .btn{flex:1;padding:14px 18px;justify-content:center}
  .sban .disc{padding-top:22px}
  .nav,.searchbox,.mega{display:none}
  .burger{display:grid;place-items:center;width:40px;height:40px}
  .logo{order:0;position:absolute;left:50%;transform:translateX(-50%)}
  .hdr-in{position:relative;padding:11px 12px}
  .icons{margin-left:auto;gap:10px}
  .ico .lbl{display:none}
  .ico{min-width:32px}
  .hero img{aspect-ratio:3/3.4;object-fit:cover;object-position:center 46%}
  .trust li{padding:13px 16px;font-size:11px}
  .cats{grid-template-rows:repeat(3,auto);grid-auto-columns:calc((100% - 12px)/2);gap:18px 12px}
  .bands{grid-template-columns:repeat(2,1fr)}
  .stats{grid-template-columns:repeat(2,1fr)}
  .revs{grid-template-columns:1fr}
  .cover-tr>a{flex:0 0 80%}
  .cover{padding:0 10px}
  .grid,.grid.g5{grid-template-columns:repeat(2,1fr);gap:20px 12px}
  .bsrail{gap:12px}
  .bsrail>.card{flex:0 0 calc((100% - 12px)/2)}
  .plp{grid-template-columns:1fr}
  .side-f{display:none}
  .mfilter{display:flex}
  .pdp{grid-template-columns:1fr;gap:18px}
  .pgal{grid-template-columns:1fr}
  .mod-box{grid-template-columns:1fr}
  .mod-box img.hero{aspect-ratio:16/9;border-radius:12px 12px 0 0;max-height:190px}
  .ftr-grid{grid-template-columns:1fr 1fr}
  .tabbar{display:flex}
  body{padding-bottom:58px}
  .satc{bottom:58px}
  .appfab{display:none}
  .hublist{grid-template-columns:1fr}
  .cdots{grid-template-columns:repeat(9,1fr)}
}
@container (max-width:560px){
  .logo .lg,.logo .ex{font-size:18px}
  .ico{min-width:28px}
  .ftr-grid{grid-template-columns:1fr}
  .sec{padding:28px 0}
  .card .eye{display:none}
}
@media (max-width:900px){
  .l1bar{display:block}
  .sban{grid-template-columns:1fr}
  .sban{min-height:0}
  .sban .im{aspect-ratio:4/4.2}
  .sban .im img{object-position:center 16%}
  .sban .bd{padding:26px 20px 30px}
  .sban .ctas .btn{flex:1;padding:14px 18px;justify-content:center}
  .sban .disc{padding-top:22px}
  .nav,.searchbox,.mega{display:none}
  .burger{display:grid;place-items:center;width:40px;height:40px}
  .logo{order:0;position:absolute;left:50%;transform:translateX(-50%)}
  .hdr-in{position:relative;padding:11px 12px}
  .icons{margin-left:auto;gap:10px}
  .ico .lbl{display:none}
  .ico{min-width:32px}
  .hero img{aspect-ratio:3/3.4;object-fit:cover;object-position:center 46%}
  .trust li{padding:13px 16px;font-size:11px}
  .cats{grid-template-rows:repeat(3,auto);grid-auto-columns:calc((100% - 12px)/2);gap:18px 12px}
  .bands{grid-template-columns:repeat(2,1fr)}
  .stats{grid-template-columns:repeat(2,1fr)}
  .revs{grid-template-columns:1fr}
  .cover-tr>a{flex:0 0 80%}
  .cover{padding:0 10px}
  .grid,.grid.g5{grid-template-columns:repeat(2,1fr);gap:20px 12px}
  .bsrail{gap:12px}
  .bsrail>.card{flex:0 0 calc((100% - 12px)/2)}
  .plp{grid-template-columns:1fr}
  .side-f{display:none}
  .mfilter{display:flex}
  .pdp{grid-template-columns:1fr;gap:18px}
  .pgal{grid-template-columns:1fr}
  .mod-box{grid-template-columns:1fr}
  .mod-box img.hero{aspect-ratio:16/9;border-radius:12px 12px 0 0;max-height:190px}
  .ftr-grid{grid-template-columns:1fr}
  .tabbar{display:flex}
  body{padding-bottom:58px}
  .satc{bottom:58px}
  .appfab{display:none}
  .hublist{grid-template-columns:1fr}
  .cdots{grid-template-columns:repeat(9,1fr)}
  .logo .lg,.logo .ex{font-size:18px}
  .card .eye{display:none}
}

@media (max-width:900px){ .icons a[title="Store locator"]{display:none} .logo .lg,.logo .ex{font-size:19px} }
@container (max-width:900px){ .icons a[title="Store locator"]{display:none} .logo .lg,.logo .ex{font-size:19px} }

@keyframes sheetUp{from{transform:translateY(100%)}to{transform:none}}
@container (max-width:900px){
  .mod{place-items:end stretch;padding:0}
  .mod-box{width:100%;max-width:none;max-height:90vh;border-radius:18px 18px 0 0;
    animation:sheetUp .3s cubic-bezier(.2,.8,.2,1)}
  .mod-box::before{content:"";position:sticky;top:0;display:block;width:42px;height:4px;
    border-radius:3px;background:#d8d8d8;margin:10px auto 0;z-index:3}
  .mod .x{top:14px;right:16px}
  .mod-body{padding:18px 20px 26px}
}
@media (max-width:900px){
  .mod{place-items:end stretch;padding:0}
  .mod-box{width:100%;max-width:none;max-height:90vh;border-radius:18px 18px 0 0;
    animation:sheetUp .3s cubic-bezier(.2,.8,.2,1)}
  .mod-box::before{content:"";position:sticky;top:0;display:block;width:42px;height:4px;
    border-radius:3px;background:#d8d8d8;margin:10px auto 0;z-index:3}
  .mod .x{top:14px;right:16px}
  .mod-body{padding:18px 20px 26px}
}


/* category starts-at tag */
.cat .startsat{position:absolute;left:10px;bottom:10px;z-index:2;background:rgba(255,255,255,.94);
  backdrop-filter:blur(6px);color:var(--ink);font-size:11px;font-weight:800;letter-spacing:.01em;
  padding:5px 9px;border-radius:20px;box-shadow:0 1px 5px rgba(0,0,0,.12);white-space:nowrap}

/* app download */
.appdl{background:linear-gradient(105deg,#fdf1f7 0%,#f3f6ff 55%,#eef3ff 100%);
  border-top:1px solid var(--line)}
.appdl .ad-in{display:grid;grid-template-columns:220px 1fr;align-items:end;gap:30px;
  padding:30px 0 0}
.appdl .ph{position:relative;width:190px;justify-self:center;align-self:end;background:#0d0d0d;
  border-radius:26px 26px 0 0;padding:9px 9px 0;line-height:0;
  box-shadow:0 14px 30px rgba(20,30,80,.22)}
.appdl .ph .notch{position:absolute;left:50%;top:15px;transform:translateX(-50%);width:56px;
  height:5px;border-radius:6px;background:#3a3a3a;z-index:2}
.appdl .ph img{width:100%;height:230px;object-fit:cover;object-position:center 18%;
  border-radius:20px 20px 0 0}
.appdl .cp{padding-bottom:34px}
.appdl .cp h2{font-size:clamp(19px,2.4vw,29px);line-height:1.16;letter-spacing:-.01em;
  text-transform:uppercase;color:#132a63;margin:0}
.appdl .cp p{color:#4c5570;font-size:13px;line-height:1.65;margin:9px 0 16px;max-width:52ch}
.appdl .badges{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.appdl .dn{font-size:13.5px;font-weight:800;color:#132a63;letter-spacing:.02em}
.appdl .store{display:inline-flex;align-items:center;gap:9px;background:#0d0d0d;color:#fff;
  padding:8px 15px;border-radius:9px;transition:.16s}
.appdl .store:hover{transform:translateY(-2px);box-shadow:0 8px 18px rgba(0,0,0,.22)}
.appdl .store .ic{display:grid;place-items:center;line-height:0}
.appdl .store .tx{display:flex;flex-direction:column;line-height:1.15}
.appdl .store .tx i{font-style:normal;font-size:9px;letter-spacing:.06em;text-transform:uppercase;opacity:.82}
.appdl .store .tx b{font-size:14px;font-weight:700;letter-spacing:.01em}


@media (max-width:900px){
.railrow{gap:12px}
.railrow>.card{flex:0 0 calc((100% - 12px)/2)}
.cat .startsat{left:7px;bottom:7px;font-size:10px;padding:4px 7px}
.appdl .ad-in{grid-template-columns:1fr;gap:0;text-align:center;padding:22px 0 0}
.appdl .cp{padding-bottom:22px}
.appdl .cp p{margin-inline:auto}
.appdl .badges{justify-content:center;gap:9px}
.appdl .dn{flex:0 0 100%}
.appdl .store{padding:7px 12px}
.appdl .store .tx b{font-size:13px}
.appdl .ph{width:160px;margin:14px auto 0;order:2}
.appdl .ph img{height:185px}
}
@container (max-width:900px){
.railrow{gap:12px}
.railrow>.card{flex:0 0 calc((100% - 12px)/2)}
.cat .startsat{left:7px;bottom:7px;font-size:10px;padding:4px 7px}
.appdl .ad-in{grid-template-columns:1fr;gap:0;text-align:center;padding:22px 0 0}
.appdl .cp{padding-bottom:22px}
.appdl .cp p{margin-inline:auto}
.appdl .badges{justify-content:center;gap:9px}
.appdl .dn{flex:0 0 100%}
.appdl .store{padding:7px 12px}
.appdl .store .tx b{font-size:13px}
.appdl .ph{width:160px;margin:14px auto 0;order:2}
.appdl .ph img{height:185px}
}
"""