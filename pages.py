# pages.py  -  Tehranzone v1.0
# شامل: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

# لوگوی NERULA (به‌صورت base64 داخلی، بدون نیاز به هاست خارجی)
LOGO_B64 = "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"

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · Tehranzone</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.44.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#000000;--card:#0d0d0d;--accent:#ffffff;--text:#ffffff;--dim:#555555;--mid:#888888;--border:rgba(255,255,255,0.06)}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px}
.bg{position:fixed;inset:0;background:var(--bg);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px);background-size:44px 44px;z-index:0}
.orb{position:fixed;border-radius:50%;filter:blur(90px);z-index:0;animation:fl 9s ease-in-out infinite}
.o1{width:380px;height:380px;background:rgba(255,255,255,0.06);top:-100px;right:-80px}
.o2{width:280px;height:280px;background:rgba(34,197,94,0.04);bottom:-60px;left:-60px;animation-delay:4s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px}
.card{background:#0d0d0d;border:1px solid rgba(255,255,255,0.06);border-radius:18px;padding:38px 34px 34px;backdrop-filter:blur(24px);box-shadow:0 20px 60px rgba(0,0,0,.7)}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px}
.brand-img{width:48px;height:48px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);flex-shrink:0;background:#111111}
.brand-img img{width:100%;height:100%;object-fit:cover}
.brand-name{font-size:16px;font-weight:800;color:var(--text)}
.brand-sub{font-size:10px;color:var(--accent);margin-top:2px}
h1{font-size:21px;font-weight:800;color:var(--text);margin-bottom:5px;letter-spacing:-.02em}
.sub{font-size:12px;color:var(--mid);margin-bottom:24px;line-height:1.6}
.hint{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:10px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--dim);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent);background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);padding:3px 11px;border-radius:7px;cursor:pointer;transition:.18s;letter-spacing:.08em}
.hint-val:hover{background:rgba(255,255,255,0.18)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--mid);margin-bottom:7px;text-transform:uppercase;letter-spacing:.06em}
.inp-wrap{position:relative}
input[type=password]{width:100%;padding:13px 44px 13px 16px;border-radius:11px;border:1px solid rgba(255,255,255,0.10);background:rgba(0,0,0,.3);color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.2s}
input[type=password]:focus{border-color:rgba(255,255,255,.5);background:rgba(0,0,0,.4);box-shadow:0 0 0 3px rgba(255,255,255,.08)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:.2s}
input:focus+.ic{color:var(--accent)}
.err{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.15);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:13px;border-radius:11px;border:none;cursor:pointer;background:#ffffff;color:#000000;font-family:inherit;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 20px rgba(255,255,255,.15);transition:.2s;position:relative;overflow:hidden}
.btn::before{content:'';position:absolute;inset:0;background:rgba(0,0,0,.08);opacity:0;transition:.2s}
.btn:hover::before{opacity:1}
.btn:disabled{opacity:.5;cursor:not-allowed}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
.footer a{color:var(--accent);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="orb o1"></div><div class="orb o2"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div style="width:48px;height:48px;border-radius:12px;background:#111111;border:1px solid rgba(255,255,255,0.08);display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:20px;font-weight:800;flex-shrink:0">T</div>
      <div><div class="brand-name">Tehranzone</div><div class="brand-sub">v1.0</div></div>
    </div>
    <h1>ورود به پنل</h1>
    <p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <div class="hint">
      <span class="hint-label">رمز پیش‌فرض سیستم</span>
      <span class="hint-val" onclick="document.getElementById('pw').value='NERULA2024';document.getElementById('pw').focus()">NERULA2024</span>
    </div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-lock ic"></i>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer">پشتیبانی <a href="https://discord.gg/PJJavvtZ7U" target="_blank"><i class="ti ti-brand-discord"></i>discord.gg/PJJavvtZ7U</a></div>
  </div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tehranzone</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.44.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#000000;--bg2:#0a0a0a;--bg3:#111111;
  --card:#0d0d0d;--card-b:rgba(255,255,255,0.06);--card-bh:rgba(255,255,255,0.12);
  --accent:#ffffff;--accent2:#cccccc;--accent-d:rgba(255,255,255,0.05);
  --green:#22c55e;--green-bg:rgba(34,197,94,0.10);--green-t:#4ade80;
  --red:#ef4444;--red-bg:rgba(239,68,68,0.10);--red-t:#f87171;
  --amber:#eab308;--amber-bg:rgba(234,179,8,0.10);--amber-t:#facc15;
  --purple:#a78bfa;--purple-bg:rgba(167,139,250,0.10);
  --t1:#ffffff;--t2:#888888;--t3:#555555;
  --sidebar-w:260px;--radius:14px;
  --shadow:0 8px 32px rgba(0,0,0,0.5);
  --glass:#0d0d0d;
}
[data-theme="light"]{
  --bg:#F0F4FA;--bg2:#E4EDF9;--bg3:#D5E3F5;
  --card:#FFFFFF;--card-b:rgba(0,0,0,0.08);--card-bh:rgba(0,0,0,0.15);
  --accent:#111111;--accent2:#333333;--accent-d:rgba(0,0,0,0.04);
  --green:#16a34a;--green-bg:rgba(22,163,74,0.08);--green-t:#166534;
  --red:#dc2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991b1b;
  --amber:#ca8a04;--amber-bg:rgba(202,138,4,0.08);--amber-t:#92400e;
  --purple:#7c3aed;--purple-bg:rgba(124,58,237,0.08);
  --t1:#0f172a;--t2:#334155;--t3:#64748b;
  --shadow:0 4px 20px rgba(0,0,0,0.08);
  --glass:#FFFFFF;
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:#050505;border-left:1px solid rgba(255,255,255,0.04);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s}
.logo{display:flex;align-items:center;gap:11px;padding:20px 16px 16px;border-bottom:1px solid rgba(255,255,255,0.04)}
.logo-icon{width:34px;height:34px;border-radius:9px;background:#ffffff;color:#000000;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:900;flex-shrink:0}
.logo-name{font-size:14px;font-weight:800;color:#ffffff;letter-spacing:.03em}
.logo-sub{font-size:8px;color:rgba(255,255,255,0.2);margin-top:1px;font-weight:500}
.sb-close{display:none;position:absolute;left:10px;top:18px;background:none;border:none;color:rgba(255,255,255,0.2);width:28px;height:28px;border-radius:7px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:12px 8px 8px}
.nav-sec{padding:14px 10px 6px;font-size:7.5px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,0.15);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 12px;color:rgba(255,255,255,0.3);font-size:12px;cursor:pointer;border-radius:9px;transition:all .15s;margin:1px 6px;position:relative}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0;transition:.15s}
.nav-it:hover{background:rgba(255,255,255,0.03);color:rgba(255,255,255,0.6)}
.nav-it.on{background:rgba(255,255,255,0.05);color:#ffffff;font-weight:700}
.nav-it.on i{color:#ffffff}
.nav-badge{margin-right:auto;background:rgba(255,255,255,0.06);color:rgba(255,255,255,0.3);font-size:8.5px;padding:2px 6px;border-radius:12px;font-weight:700}
.sb-foot{padding:10px;border-top:1px solid rgba(255,255,255,0.04)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:rgba(255,255,255,0.025);color:rgba(255,255,255,0.25);border-radius:9px;padding:8px;font-size:11px;font-weight:500;font-family:inherit;border:1px solid rgba(255,255,255,0.04);cursor:pointer;width:100%;transition:.15s;margin-bottom:5px}
.theme-btn:hover{background:rgba(255,255,255,0.05);color:rgba(255,255,255,0.5)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:rgba(239,68,68,0.04);color:rgba(239,68,68,0.4);border-radius:9px;padding:8px;font-size:11px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.05);cursor:pointer;width:100%;transition:.15s;margin-top:4px}
.logout-btn:hover{background:rgba(239,68,68,0.08);color:rgba(239,68,68,0.7)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:50px;background:rgba(5,5,5,0.95);border-bottom:1px solid rgba(255,255,255,0.04);z-index:150;align-items:center;justify-content:space-between;padding:0 12px;backdrop-filter:blur(12px)}
.mob-top .ml{display:flex;align-items:center;gap:8px}
.mob-logo{width:28px;height:28px;border-radius:7px;background:#ffffff;color:#000000;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:900}
.mob-title{color:#ffffff;font-size:12.5px;font-weight:800;letter-spacing:.03em}
.mob-right{display:flex;gap:5px}
.menu-btn,.theme-mob{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.04);color:rgba(255,255,255,0.3);width:32px;height:32px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.menu-btn:hover,.theme-mob:hover{background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.6)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 30px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:24px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:20px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:9px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:22px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:4px 12px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:var(--purple)}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.metric{background:#0d0d0d;border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 18px 15px;transition:all .22s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
/* ══════ صفحه ترافیک - ریدیزاین ══════ */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:14px;margin-bottom:18px}
.traf-main-stat{background:#0d0d0d;border:1px solid var(--card-b);border-radius:16px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,rgba(255,255,255,.06),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:#0d0d0d;border:1px solid var(--card-b);border-radius:16px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.22s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}

.traf-chart-card{background:#0d0d0d;border:1px solid var(--card-b);border-radius:16px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:9px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:7px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.18s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(255,255,255,.35)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:36px;height:36px;border-radius:10px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:#0d0d0d;border:1px solid var(--card-b);border-radius:16px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent);word-break:break-all;line-height:1.8;letter-spacing:.01em}
[data-theme="light"] .vl-code{background:rgba(0,0,0,.03)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:600;border-radius:10px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .18s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:#ffffff;color:#000000;box-shadow:0 2px 8px rgba(0,0,0,.3)}
.btn-p:hover{background:#eeeeee;transform:translateY(-1px)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(255,255,255,.25)}
.btn-g{background:var(--accent-d);color:var(--accent);border:1px solid rgba(255,255,255,0.12)}
.btn-g:hover{background:rgba(255,255,255,0.15)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.15)}
.btn-d:hover{background:rgba(239,68,68,.18)}
.btn-pur{background:var(--purple-bg);color:var(--purple);border:1px solid rgba(167,139,250,.15)}
.btn-pur:hover{background:rgba(167,139,250,.18)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(234,179,8,.15)}
.btn-amber:hover{background:rgba(234,179,8,.18)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:7px}
.card{background:#0d0d0d;border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.04);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.25);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.18s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.03)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(255,255,255,.45);background:rgba(0,0,0,.3);box-shadow:0 0 0 3px rgba(255,255,255,.08)}
.fs option{background:var(--bg2)}
[data-theme="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(234,179,8,.12);color:var(--amber-t)}
/* ══════ پنل ساخت کانفیگ - طراحی جدید ══════ */
.create-panel{background:#0d0d0d;border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:18px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,rgba(255,255,255,.03),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:12px;background:#111111;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:20px;flex-shrink:0;border:1px solid rgba(255,255,255,0.08)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.2);border:1px solid var(--card-b);border-radius:12px;padding:14px 16px}
[data-theme="light"] .cp-block{background:rgba(255,255,255,.02)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.22);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(255,255,255,.5);box-shadow:0 0 0 3px rgba(255,255,255,.08)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.18s;white-space:nowrap}
.chip:hover{background:rgba(255,255,255,0.15);color:var(--accent)}
.chip.active{background:#ffffff;color:#000000;border-color:#ffffff}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:12px;padding:13px 12px;cursor:pointer;transition:.2s;text-align:center;position:relative;background:rgba(0,0,0,.12)}
[data-theme="light"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(255,255,255,.08)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:#ffffff;color:#000000;border:none;border-radius:12px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;transition:.2s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
.cp-toggle-head{cursor:pointer;user-select:none}
.cp-toggle-head:hover{background:rgba(255,255,255,0.02)}
.cp-toggle-arrow{color:var(--t3);font-size:18px;transition:transform .25s;margin-right:8px}
.cp-toggle-head.cp-open .cp-toggle-arrow{transform:rotate(180deg)}
.cp-body-wrap{max-height:0;overflow:hidden;transition:max-height .35s cubic-bezier(.4,0,.2,1),padding .35s;padding:0 24px}
.cp-body-wrap.cp-open{max-height:2000px;padding:2px 24px 22px}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
/* ══════ پنل اطلاعات سرور ══════ */
.srv-panel{background:#0d0d0d;border:1px solid var(--card-b);border-radius:18px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(255,255,255,.03),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:#111111;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:22px;flex-shrink:0;border:1px solid rgba(255,255,255,0.08)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:12px;padding:12px 14px;transition:.2s}
[data-theme="light"] .srv-tile{background:rgba(255,255,255,.02)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}

/* ══════ پنل تغییر رمز ══════ */
.pw-panel{background:#0d0d0d;border:1px solid var(--card-b);border-radius:18px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,rgba(255,255,255,.03),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:#111111;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:22px;flex-shrink:0;border:1px solid rgba(255,255,255,0.08)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.22);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="light"] .pw-input{background:#fff}
.pw-input:focus{border-color:rgba(167,139,250,.5);box-shadow:0 0 0 3px rgba(167,139,250,.08)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:#ffffff;color:#000000;border:none;border-radius:11px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;transition:.2s}
.pw-submit:hover{transform:translateY(-2px)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* ══════ اتصالات فعال - نسخه پیشرفته ══════ */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.conn-hero-tile{background:#0d0d0d;border:1px solid var(--card-b);border-radius:14px;padding:16px 18px;position:relative;overflow:hidden;transition:.22s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:34px;height:34px;border-radius:10px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}

.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(34,197,94,.15)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}

.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:#0d0d0d;border:1px solid var(--card-b);border-radius:16px;padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(34,197,94,.08),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--green),#16a34a);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(34,197,94,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.08) 15%,rgba(255,255,255,0.08) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#4ade80);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}

.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:18px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:16px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}

@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(255,255,255,0.03);border:1px dashed rgba(255,255,255,0.12);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--purple);word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
/* ══════ گروه‌های ساب - ریدیزاین کامل ══════ */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:11px;border:1px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
.subs-search input:focus{border-color:rgba(255,255,255,.5);box-shadow:0 0 0 3px rgba(255,255,255,.08)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}

.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:#0d0d0d;border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,.24)}
.sub-card-top{background:#0d0d0d;padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(255,255,255,.03),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:13px;background:#111111;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:20px;flex-shrink:0;border:1px solid rgba(255,255,255,0.08)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}

.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:12px;overflow:hidden}
[data-theme="light"] .sub-card-stats{background:rgba(255,255,255,.02)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}

.sub-card-url-row{margin:14px 20px 0;background:rgba(255,255,255,0.03);border:1px dashed rgba(255,255,255,0.12);border-radius:10px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--purple);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.18s}
.sub-card-url-copy:hover{color:var(--accent);transform:scale(1.1)}

.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}

.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:18px;grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:16px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}

/* ══════ مودال ساخت گروه - نسخه فشرده ══════ */
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.modal-v2-head{background:#0d0d0d;padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(255,255,255,.03),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.2)}
.modal-v2-icon{width:42px;height:42px;border-radius:12px;background:#111111;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;border:1px solid rgba(255,255,255,0.08)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--accent);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.22);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .modal-v2-input{background:rgba(255,255,255,.03)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(255,255,255,.55);box-shadow:0 0 0 3px rgba(255,255,255,.08);background:rgba(0,0,0,.28)}
[data-theme="light"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--accent)}
.modal-v2-hint{background:var(--accent-d);border:1px solid rgba(255,255,255,0.12);border-radius:10px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:10px;background:#ffffff;color:#000000;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.2s}
.modal-v2-btn-submit:hover{transform:translateY(-2px)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* ══════ مودال انتخاب کانفیگ - نسخه پیشرفته ══════ */
.lmodal-head{background:#0d0d0d;padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:12px;background:#111111;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:19px;flex-shrink:0;border:1px solid rgba(255,255,255,0.08)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.22);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme="light"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:rgba(255,255,255,.5);box-shadow:0 0 0 3px rgba(255,255,255,.08)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:7px;background:var(--accent-d);color:var(--accent);border:1px solid var(--card-b);cursor:pointer;transition:.18s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(255,255,255,0.15)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}

.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.14)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}

.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}

@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(5px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 60px rgba(0,0,0,.5)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.15s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.04)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap;backdrop-filter:blur(12px)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(34,197,94,.25);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.25);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}

/* ══════ داشبورد - طراحی جدید Tehranzone ══════ */
.m4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.m-card{background:#0d0d0d;border:1px solid var(--card-b);border-radius:14px;padding:18px 16px;display:flex;align-items:center;gap:14px;transition:.22s;position:relative;overflow:hidden}
.m-card:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.m-icon{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0}
.m-i-green{background:var(--green-bg);color:var(--green)}
.m-i-blue{background:var(--accent-d);color:var(--accent)}
.m-i-white{background:rgba(255,255,255,0.06);color:#ffffff}
.m-i-red{background:var(--red-bg);color:var(--red)}
.m-text{flex:1;min-width:0}
.m-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.m-val{font-size:24px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:600;color:var(--t3);margin-right:2px}
.m-sub{font-size:9.5px;color:var(--t3);margin-top:3px}
@media(max-width:1100px){.m4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.m4{grid-template-columns:1fr}.m-val{font-size:20px}}
.n-chart-wrap{background:#0d0d0d;border:1px solid var(--card-b);border-radius:16px;padding:22px 24px 18px;margin-bottom:16px;position:relative;overflow:hidden}
.n-chart-wrap::before{content:'';position:absolute;top:-60px;right:-60px;width:180px;height:180px;background:radial-gradient(circle,rgba(255,255,255,.03),transparent 70%);pointer-events:none}
.n-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;position:relative;z-index:1}
.n-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.n-chart-title i{color:var(--accent);font-size:18px}
.n-chart-body{height:240px;position:relative;z-index:1}
@media(max-width:900px){.n-overview-hero{grid-template-columns:1fr}}
@media(max-width:520px){.n-chart-body{height:200px}.m-val{font-size:18px}}

/* ══════ کانفیگ‌ها - لایه‌بندی کاملاً جدید ══════ */
.lk-header{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-bottom:16px;flex-wrap:wrap}
.lk-header-r{display:flex;align-items:center;gap:10px}
.lk-title{font-size:20px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.lk-title i{color:var(--accent);font-size:22px}
.lk-header-l{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.lk-create-btn{background:#ffffff;color:#000000;border:none;border-radius:10px;padding:9px 18px;font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.2s;white-space:nowrap}
.lk-create-btn:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(255,255,255,.1)}
.lk-search-wrap{position:relative;margin-bottom:14px}
.lk-search-wrap i{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:16px;pointer-events:none}
.lk-search-wrap input{width:100%;padding:12px 14px 12px 40px;border-radius:12px;border:1px solid var(--card-b);background:#0d0d0d;color:var(--t1);font-family:inherit;font-size:13px;outline:none;transition:.18s}
.lk-search-wrap input:focus{border-color:rgba(255,255,255,.3)}
.lk-search-wrap input::placeholder{color:var(--t3)}
.cfg-grid{display:flex;flex-direction:column;gap:6px}
.cfg-card{background:#0d0d0d;border:1px solid var(--card-b);border-radius:12px;padding:0;transition:all .2s;position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 4px 20px rgba(0,0,0,.25);transform:translateY(-1px)}
.cfg-card.is-off{opacity:.5}
.cfg-card.is-exp{opacity:.65}
.cfg-row{display:flex;align-items:center;gap:12px;padding:12px 14px}
.cfg-select{display:flex;align-items:center;flex-shrink:0}
.cfg-select input{width:16px;height:16px;accent-color:var(--accent);cursor:pointer}
.cfg-status-dot{width:7px;height:7px;border-radius:50%;background:var(--green);flex-shrink:0}
.cfg-card.is-off .cfg-status-dot{background:var(--red)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber)}
.cfg-identity{display:flex;flex-direction:column;gap:2px;min-width:130px;flex-shrink:0}
.cfg-label{font-size:12.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:5px}
.cfg-sub-meta{display:flex;align-items:center;gap:6px;font-size:9.5px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9px;color:var(--accent2);background:rgba(255,255,255,0.04);padding:2px 6px;border-radius:4px;cursor:pointer;transition:.15s;border:1px solid transparent}
.cfg-uuid-mini:hover{background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.06)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0;opacity:.5}
.cfg-usage-col{flex:1;min-width:140px;display:flex;flex-direction:column;gap:4px}
.ubar{height:3px;border-radius:2px;background:rgba(255,255,255,0.05);overflow:hidden}
.ubar-f{height:100%;border-radius:2px;transition:width .4s ease}
.utxt{font-size:9px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:90px}
.cfg-badges-col{display:flex;flex-direction:column;gap:3px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:3px;flex-shrink:0}
.cfg-actions .btn{padding:5px 7px;font-size:10px}
.cfg-actions .btn-icon{width:28px;height:28px;padding:0;justify-content:center}
.proto-chip{font-size:8.5px;padding:3px 7px;border-radius:5px;font-weight:700;white-space:nowrap}
.pc-ws{background:rgba(255,255,255,0.06);color:var(--t2)}
.pc-xhttp{background:var(--purple-bg);color:var(--purple)}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9px;color:var(--t3);display:flex;align-items:center;gap:3px;white-space:nowrap}
.cfg-sub-tag i{color:var(--accent2);font-size:10px}
.tog{width:18px;height:28px;border-radius:18px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:12px;height:12px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:13px}
.tog.on{background:var(--green)}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
@media(max-width:880px){.cfg-row{flex-wrap:wrap}.cfg-divider-v{display:none}.cfg-usage-col{min-width:100%;order:5}}
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:10px}
  .cfg-card{border-radius:14px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:10px;padding:14px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:8px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;flex-wrap:wrap;gap:4px;align-items:center}
  .cfg-divider-v{display:none}
}

/* ══════ مودال ساخت کانفیگ ══════ */
.cfg-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:400;opacity:0;pointer-events:none;transition:opacity .25s;backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center}
.cfg-overlay.open{opacity:1;pointer-events:auto}
.cfg-drawer{position:fixed;top:50%;left:50%;width:480px;max-width:92vw;max-height:90vh;background:#0b0b0b;border:1px solid rgba(255,255,255,0.06);border-radius:20px;z-index:410;transform:translate(-50%,-50%) scale(.9);opacity:0;transition:all .3s cubic-bezier(.4,0,.2,1);display:flex;flex-direction:column;overflow:hidden;box-shadow:0 32px 100px rgba(0,0,0,.7),0 0 0 1px rgba(255,255,255,0.03)}
.cfg-drawer.open{transform:translate(-50%,-50%) scale(1);opacity:1}
.cfg-drawer-head{display:flex;align-items:center;justify-content:space-between;padding:22px 24px 18px;flex-shrink:0;border-bottom:1px solid rgba(255,255,255,0.04)}
.cfg-drawer-title{font-size:15px;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:10px}
.cfg-drawer-title i{color:#000000;font-size:18px;background:#ffffff;width:32px;height:32px;border-radius:9px;display:flex;align-items:center;justify-content:center}
.cfg-drawer-close{background:none;border:none;color:rgba(255,255,255,0.25);width:30px;height:30px;border-radius:8px;font-size:18px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.cfg-drawer-close:hover{background:rgba(255,255,255,0.06);color:#ffffff}
.cfg-drawer-body{flex:1;overflow-y:auto;padding:8px 22px 22px}
.cfg-drawer-body::-webkit-scrollbar{width:3px}
.cfg-drawer-body::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.06);border-radius:3px}
.cfg-drawer-note{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:10px;padding:10px 13px;font-size:10px;color:rgba(255,255,255,0.3);display:flex;align-items:center;gap:8px;margin-bottom:18px;line-height:1.7}
.cfg-drawer-note i{color:rgba(255,255,255,0.15);font-size:13px;flex-shrink:0}
.cfg-sec{background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:12px;padding:14px 14px 12px;margin-bottom:10px}
.cfg-sec-head{display:flex;align-items:center;gap:7px;margin-bottom:10px}
.cfg-sec-head i{color:rgba(255,255,255,0.35);font-size:14px}
.cfg-sec-head span{font-size:10.5px;font-weight:700;color:rgba(255,255,255,0.5);letter-spacing:.03em}
.cfg-fi{width:100%;padding:10px 13px;border-radius:8px;border:1px solid rgba(255,255,255,0.05);background:rgba(0,0,0,.3);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s;box-sizing:border-box}
.cfg-fi:focus{border-color:rgba(255,255,255,0.15);background:rgba(0,0,0,.45)}
.cfg-fi::placeholder{color:rgba(255,255,255,0.18)}
.cfg-fi + .cfg-fi{margin-top:7px}
.cfg-fi-row{display:flex;gap:7px}
.cfg-fi-row .cfg-fi{flex:1}
.cfg-form-row{display:flex;gap:10px}
.cfg-form-row .cfg-sec{flex:1;min-width:0}
.cfg-fs-label{font-size:9px;font-weight:700;color:rgba(255,255,255,0.25);text-transform:uppercase;letter-spacing:.06em;display:flex;align-items:center;gap:5px;margin-bottom:7px}
.cfg-fs-label i{color:rgba(255,255,255,0.15);font-size:11px}
.chip-row{display:flex;gap:5px;flex-wrap:wrap;margin-top:7px}
.chip{font-size:10px;font-weight:700;padding:4px 10px;border-radius:6px;background:rgba(255,255,255,0.03);color:rgba(255,255,255,0.3);border:1px solid rgba(255,255,255,0.04);cursor:pointer;transition:.18s;white-space:nowrap}
.chip:hover{background:rgba(255,255,255,0.06);color:rgba(255,255,255,0.7);border-color:rgba(255,255,255,0.08)}
.chip.active{background:#ffffff;color:#000000;border-color:#ffffff}
.cfg-proto-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.cfg-proto-opt{border:1px solid rgba(255,255,255,0.04);border-radius:10px;padding:13px 8px;cursor:pointer;transition:.2s;text-align:center;background:transparent}
.cfg-proto-opt:hover{border-color:rgba(255,255,255,0.1)}
.cfg-proto-opt.active{border-color:#ffffff;background:rgba(255,255,255,0.04)}
.cfg-proto-opt i{font-size:20px;color:rgba(255,255,255,0.2);margin-bottom:6px;display:block;transition:.2s}
.cfg-proto-opt.active i{color:#ffffff}
.cfg-proto-name{font-size:11px;font-weight:800;color:rgba(255,255,255,0.4);transition:.2s}
.cfg-proto-opt.active .cfg-proto-name{color:#ffffff}
.cfg-proto-desc{font-size:8.5px;color:rgba(255,255,255,0.15);margin-top:3px;line-height:1.5}
.cfg-drawer-foot{padding:14px 22px 18px;border-top:1px solid rgba(255,255,255,0.04);flex-shrink:0;background:#0b0b0b}
.cfg-submit-btn{width:100%;justify-content:center;background:#ffffff;color:#000000;border:none;border-radius:11px;padding:13px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;transition:.2s}
.cfg-submit-btn:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(255,255,255,.06)}
.cfg-submit-btn:active{transform:scale(.98)}
@media(max-width:600px){.cfg-form-row{flex-direction:column;gap:0}.cfg-form-row .cfg-sec{margin-bottom:0}.cfg-drawer{max-height:92vh;border-radius:14px}}

/* ── زیر ۷۶۸px: تبدیل کامل به کارت موبایل ── */
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}
}

/* ══════ اتصالات فعال با IP ══════ */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:#0d0d0d;border:1px solid var(--card-b);border-radius:14px;padding:15px 17px;transition:.22s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}

/* ══════ لاگ فعالیت‌ها ══════ */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,0.04);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.04)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
.cfgdash-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.cfgdash-item{background:#0d0d0d;border:1px solid var(--card-b);border-radius:12px;padding:13px 14px;cursor:pointer;transition:.18s}
.cfgdash-item:hover{border-color:var(--card-bh)}
.cfgdash-item.on{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.cfgdash-item-top{display:flex;align-items:center;gap:7px;margin-bottom:8px}
.cfgdash-item-label{font-size:12.5px;font-weight:700;color:var(--t1);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cfgdash-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.cfgdash-stat{background:var(--accent-d);border:1px solid var(--card-b);border-radius:11px;padding:12px 13px}
.cfgdash-stat-l{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.cfgdash-stat-v{font-size:16px;font-weight:800;color:var(--t1)}
.cfgdash-ip-row{display:flex;align-items:center;gap:10px;padding:9px 11px;border-radius:9px;background:var(--accent-d);border:1px solid var(--card-b);margin-bottom:6px;flex-wrap:wrap}
.cfgdash-ip-row .ip{font-family:ui-monospace,monospace;font-size:12px;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfgdash-ip-meta{display:flex;align-items:center;gap:12px;font-size:10.5px;color:var(--t3);margin-right:auto;flex-wrap:wrap}
/* Tehranzone monochrome skin: UI only, no functionality changes */
:root{--bg:#f4f4f4;--bg2:#ededed;--bg3:#dedede;--card:#fff;--card-b:rgba(0,0,0,.09);--card-bh:rgba(0,0,0,.18);--accent:#000;--accent2:#222;--accent-d:rgba(0,0,0,.055);--t1:#0a0a0a;--t2:#404040;--t3:#777;--glass:#fff;--shadow:0 8px 28px rgba(0,0,0,.08)}
html,body{background:#f4f4f4!important;color:#0a0a0a!important}.sidebar{background:#050505!important;border-left:1px solid #000!important}.logo-name{color:#fff!important}.logo-sub{color:rgba(255,255,255,.42)!important}.nav-item{color:rgba(255,255,255,.62)!important}.nav-item:hover{background:rgba(255,255,255,.08)!important;color:#fff!important}.nav-item.active{background:#fff!important;color:#000!important}.nav-item.active i{color:#000!important}.main{background:#f4f4f4!important}
.metric,.traf-main-stat,.traf-mini,.traf-chart-card,.card,.vless-box,.m-card,.n-chart-wrap,.cfg-card{background:#fff!important;border-color:rgba(0,0,0,.09)!important;box-shadow:0 6px 24px rgba(0,0,0,.055)!important}.metric:hover,.traf-mini:hover,.card:hover,.cfg-card:hover{border-color:rgba(0,0,0,.18)!important}.m-icon,.traf-mini-icon,.m-i-green,.m-i-red,.m-i-white,.m-i-blue{background:#f0f0f0!important;color:#000!important}.btn-g,.btn-o{background:#fff!important;color:#111!important;border-color:rgba(0,0,0,.14)!important}.btn-g:hover,.btn-o:hover{background:#f0f0f0!important;color:#000!important}.btn-w,.lk-create-btn{background:#000!important;color:#fff!important}.lk-search-wrap input,.fi,.fs,.cfg-drawer,.cfg-drawer-head,.modal,.toast{background:#fff!important;color:#111!important;border-color:rgba(0,0,0,.12)!important}.lk-search-wrap input::placeholder{color:#888!important}.cfg-drawer-title{color:#111!important}.cfg-drawer-title i{background:#000!important;color:#fff!important}.cfg-drawer-close{color:#666!important}.cfg-drawer-close:hover{color:#000!important;background:#f0f0f0!important}.cfg-uuid-mini{background:#f5f5f5!important;color:#333!important;border-color:#e5e5e5!important}.ubar{background:#e5e5e5!important}.proto-chip.pc-ws,.pc-ws{background:#f0f0f0!important;color:#222!important}.pc-xhttp{background:#ededed!important;color:#222!important}.cfg-link-btn{color:#555!important;border-color:#d8d8d8!important}.cfg-link-btn:hover{background:#f5f5f5!important;color:#111!important;border-color:#aaa!important}.cfg-vless,.vl-code{background:#f5f5f5!important;color:#111!important;border-color:#ddd!important}.dash-footer{border-color:#ddd!important}.df-link{color:#111!important}.topbar,.toolbar{background:#f4f4f4!important}.logout-btn{background:#fff!important;color:#555!important;border-color:#ddd!important}.logout-btn:hover{background:#000!important;color:#fff!important}.cfg-overlay{background:rgba(0,0,0,.58)!important}select option{background:#fff!important;color:#111!important}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option>
          <option value="firefox">firefox</option>
          <option value="safari">safari</option>
          <option value="ios">ios</option>
          <option value="android">android</option>
          <option value="edge">edge</option>
          <option value="360">360</option>
          <option value="qq">qq</option>
          <option value="random">random</option>
          <option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-link-chart">
  <div class="modal" style="max-width:640px">
    <button class="modal-close" onclick="closeModal('modal-link-chart')"><i class="ti ti-x"></i></button>
    <div class="modal-title" id="lc-title"><i class="ti ti-chart-line"></i> نمودار مصرف</div>
    <div style="height:280px;margin-top:10px"><canvas id="lc-canvas"></canvas></div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo">T</div>
    <span class="mob-title">Tehranzone</span>
  </div>
  <div class="mob-right">
    <a class="theme-mob" href="https://discord.gg/PJJavvtZ7U" target="_blank" style="display:flex;align-items:center;justify-content:center;text-decoration:none"><i class="ti ti-brand-discord"></i></a>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-icon">T</div>
    <div><div class="logo-name">Tehranzone</div><div class="logo-sub">v1.0</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="cfgdash"><i class="ti ti-chart-infographic"></i> داشبورد کانفیگ‌ها</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
  </div>
  <div class="sb-foot">
    <a class="theme-btn" href="https://discord.gg/PJJavvtZ7U" target="_blank" style="text-decoration:none"><i class="ti ti-brand-discord"></i> Discord</a>
    
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd"></div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
    </div>
  </div>
  <div class="m4">
    <div class="m-card"><div class="m-icon m-i-green"><i class="ti ti-plug-connected"></i></div><div class="m-text"><div class="m-label">اتصالات زنده</div><div class="m-val" id="m-conns">—</div><div class="m-sub" id="conns-live">WebSocket / XHTTP</div></div></div>
    <div class="m-card"><div class="m-icon m-i-blue"><i class="ti ti-world"></i></div><div class="m-text"><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">مصرف کل سرور</div></div></div>
    <div class="m-card"><div class="m-icon m-i-white"><i class="ti ti-link"></i></div><div class="m-text"><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div></div>
    <div class="m-card"><div class="m-icon m-i-red"><i class="ti ti-alert-triangle"></i></div><div class="m-text"><div class="m-label">خطاها</div><div class="m-val" id="m-errs">—</div><div class="m-sub">از راه‌اندازی</div></div></div>
  </div>
  <div class="n-chart-wrap">
    <div class="n-chart-head">
      <div class="n-chart-title"><i class="ti ti-chart-area"></i> نمودار ترافیک ساعتی</div>
    </div>
    <div class="n-chart-body"><canvas id="ch1"></canvas></div>
  </div>
  <div class="dash-footer">
    <span class="df-text">Tehranzone v1.0</span>
    <a class="df-link" href="https://discord.gg/PJJavvtZ7U" target="_blank"><i class="ti ti-brand-discord"></i> discord.gg/PJJavvtZ7U</a>
  </div>
</section>
</section>
<section class="pg" id="pg-links">
  <div class="lk-header">
    <div class="lk-header-r">
      <div class="lk-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div>
      <span class="badge bg-blue" id="links-pg-cnt">۰</span>
    </div>
    <div class="lk-header-l">
      <label class="bulk-selall">
        <input type="checkbox" id="links-selall" onchange="toggleSelectAllLinks(this)">
        <span>انتخاب همه</span>
      </label>
      <select id="links-sort" class="fs" onchange="renderLinksGrid()">
        <option value="newest">جدیدترین</option>
        <option value="name">نام</option>
        <option value="usage_desc">بیشترین مصرف</option>
        <option value="usage_asc">کمترین مصرف</option>
        <option value="remaining_asc">کمترین حجم</option>
        <option value="active_first">فعال‌ها اول</option>
      </select>
      <button class="lk-create-btn" onclick="openCfgCreate()"><i class="ti ti-plus"></i> ساخت کانفیگ</button>
    </div>
  </div>
  <div class="lk-search-wrap">
    <i class="ti ti-search"></i>
    <input id="links-search" placeholder="جستجو بر اساس نام، یادداشت یا UUID..." oninput="renderLinksGrid()">
  </div>
  <div class="bulk-bar" id="links-bulkbar" style="display:none">
    <span class="bulk-count"><i class="ti ti-checkbox"></i> <span id="links-selcount">۰</span> کانفیگ انتخاب شده</span>
    <div class="bulk-actions">
      <button class="btn btn-sm btn-g" onclick="bulkLinksAction('activate')"><i class="ti ti-circle-check"></i> فعال</button>
      <button class="btn btn-sm btn-g" onclick="bulkLinksAction('deactivate')"><i class="ti ti-circle-x"></i> غیرفعال</button>
      <button class="btn btn-sm btn-g" onclick="bulkLinksAction('reset')"><i class="ti ti-rotate"></i> ریست</button>
      <button class="btn btn-sm btn-d" onclick="bulkLinksAction('delete')"><i class="ti ti-trash"></i> حذف</button>
      <button class="btn btn-sm btn-o" onclick="clearLinksSelection()"><i class="ti ti-x"></i> لغو</button>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
  <div class="empty" id="links-empty-search" style="display:none"><i class="ti ti-search-off"></i><p>موردی پیدا نشد</p></div>
  <div class="dash-footer" style="margin-top:16px">
    <span class="df-text">Tehranzone v1.0</span>
    <a class="df-link" href="https://discord.gg/PJJavvtZ7U" target="_blank"><i class="ti ti-brand-discord"></i> discord.gg/PJJavvtZ7U</a>
  </div>
  <div class="cfg-overlay" id="cfg-overlay" onclick="closeCfgCreate()"></div>
  <div class="cfg-drawer" id="cfg-drawer">
    <div class="cfg-drawer-head">
      <div class="cfg-drawer-title"><i class="ti ti-square-rounded-plus"></i> ساخت کانفیگ جدید</div>
      <button class="cfg-drawer-close" onclick="closeCfgCreate()"><i class="ti ti-x"></i></button>
    </div>
    <div class="cfg-drawer-body">
      <div class="cfg-drawer-note"><i class="ti ti-info-circle"></i> UUID تصادفی تولید می‌شود · پروتکل پس از ساخت قابل تغییر نیست.</div>

      <div class="cfg-sec">
        <div class="cfg-sec-head"><i class="ti ti-user"></i><span>شناسه</span></div>
        <input class="cfg-fi" id="nl-label" placeholder="نام کانفیگ، مثلاً: کاربر علی">
        <input class="cfg-fi" id="nl-note" placeholder="یادداشت (اختیاری)">
      </div>

      <div class="cfg-form-row">
        <div class="cfg-sec">
          <div class="cfg-sec-head"><i class="ti ti-clock-hour-4"></i><span>انقضا</span></div>
          <input class="cfg-fi" id="nl-exp" type="number" min="0" step="1" placeholder="روز · 0 = نامحدود">
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
        <div class="cfg-sec">
          <div class="cfg-sec-head"><i class="ti ti-gauge"></i><span>سهمیه</span></div>
          <div class="cfg-fi-row">
            <input class="cfg-fi" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
            <select class="cfg-fi" id="nl-unit" style="flex:0 0 72px"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
          </div>
          <div class="chip-row" id="quota-chips">
            <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
            <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰M</span>
            <span class="chip active" onclick="setQuota(1,'GB',this)">۱G</span>
            <span class="chip" onclick="setQuota(5,'GB',this)">۵G</span>
            <span class="chip" onclick="setQuota(10,'GB',this)">۱۰G</span>
            <span class="chip" onclick="setQuota(50,'GB',this)">۵۰G</span>
          </div>
        </div>
      </div>

      <div class="cfg-sec">
        <div class="cfg-sec-head"><i class="ti ti-plug-connected"></i><span>پروتکل</span></div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp">XHTTP Ultra · mode: auto</option>
        </select>
        <div class="cfg-proto-grid">
          <div class="cfg-proto-opt active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <i class="ti ti-link"></i>
            <div class="cfg-proto-name">VLESS / WS</div>
            <div class="cfg-proto-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="cfg-proto-opt" data-val="xhttp" onclick="selectProto('xhttp',this)">
            <i class="ti ti-bolt"></i>
            <div class="cfg-proto-name">XHTTP · auto</div>
            <div class="cfg-proto-desc">خودکار packet-up/stream-up</div>
          </div>
        </div>
      </div>

      <div class="cfg-form-row">
        <div class="cfg-sec">
          <div class="cfg-sec-head"><i class="ti ti-fingerprint"></i><span>Fingerprint</span></div>
          <select class="cfg-fi" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="360">360</option>
            <option value="qq">qq</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cfg-sec">
          <div class="cfg-sec-head"><i class="ti ti-antenna-bars-5"></i><span>ALPN</span></div>
          <select class="cfg-fi" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">پیش‌فرض</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <input class="cfg-fi" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none;margin-top:8px">
        </div>
      </div>

      <div class="cfg-form-row">
        <div class="cfg-sec">
          <div class="cfg-sec-head"><i class="ti ti-users"></i><span>محدودیت آی‌پی</span></div>
          <input class="cfg-fi" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵</span>
          </div>
        </div>
        <div class="cfg-sec">
          <div class="cfg-sec-head"><i class="ti ti-speed"></i><span>محدودیت سرعت</span></div>
          <div class="cfg-fi-row">
            <input class="cfg-fi" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0">
            <select class="cfg-fi" id="nl-speed-unit" style="flex:0 0 80px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵</span>
          </div>
        </div>
      </div>

    </div>
    <div class="cfg-drawer-foot">
      <button class="cfg-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
    </div>
  </div>
</section>
<section class="pg" id="pg-cfgdash">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-infographic"></i> داشبورد کانفیگ‌ها</div><div class="tb-sub">آنالیز اختصاصی هر کانفیگ — وضعیت، مصرف و آی‌پی‌های متصل</div></div>
    <div class="tb-right"></div>
  </div>
  <div class="card" style="margin-bottom:16px">
    <div class="card-title"><i class="ti ti-list"></i> انتخاب کانفیگ <span class="ml-auto badge bg-blue" id="cfgdash-count">۰</span></div>
    <div class="cfgdash-grid" id="cfgdash-list"></div>
    <div class="empty" id="cfgdash-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
  </div>
  <div id="cfgdash-detail">
    <div class="card"><div class="empty"><i class="ti ti-hand-click"></i><p>یک کانفیگ را از لیست بالا انتخاب کنید تا آنالیز کامل آن نمایش داده شود</p></div></div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live-badge">—</span></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Tehranzone</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت پیش‌فرض</div><div class="srv-tile-val">443 (TLS) · قابل تغییر در هر کانفیگ</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v1.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Cloud</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>
</main>
<script>
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp':['XHTTP · auto','pc-xhttp']};
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,logs:loadActivity,cfgdash:loadCfgDash};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-errs').textContent=d.total_errors??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-badge').textContent='Tehranzone · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf;
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
let allLinksList=[];
let selectedLinks=new Set();
async function loadLinks(){
  try{
    const r=await authF('/api/links');
    const {links=[]}=await r.json();
    allLinksList=links;
    const validUuids=new Set(links.map(l=>l.uuid));
    selectedLinks.forEach(u=>{if(!validUuids.has(u))selectedLinks.delete(u)});
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    renderLinksGrid();
  }catch(e){console.error(e)}
}
function filteredLinksList(){
  const q=(document.getElementById('links-search')?.value||'').trim().toLowerCase();
  let list=!q?allLinksList:allLinksList.filter(l=>
    (l.label||'').toLowerCase().includes(q) ||
    (l.note||'').toLowerCase().includes(q) ||
    (l.uuid||'').toLowerCase().includes(q)
  );
  const sortBy=document.getElementById('links-sort')?.value||'newest';
  const remaining=l=>l.limit_bytes===0?Infinity:Math.max(0,l.limit_bytes-l.used_bytes);
  list=list.slice();
  if(sortBy==='name'){
    list.sort((a,b)=>(a.label||'').localeCompare(b.label||'','fa'));
  }else if(sortBy==='usage_desc'){
    list.sort((a,b)=>(b.used_bytes||0)-(a.used_bytes||0));
  }else if(sortBy==='usage_asc'){
    list.sort((a,b)=>(a.used_bytes||0)-(b.used_bytes||0));
  }else if(sortBy==='remaining_asc'){
    list.sort((a,b)=>remaining(a)-remaining(b));
  }else if(sortBy==='active_first'){
    list.sort((a,b)=>((b.active&&!b.expired)?1:0)-((a.active&&!a.expired)?1:0));
  }else{
    list.sort((a,b)=>(b.created_at||'').localeCompare(a.created_at||''));
  }
  return list;
}
function renderLinksGrid(){
  const links=filteredLinksList();
  const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty'),emptySearch=document.getElementById('links-empty-search');
  if(!allLinksList.length){grid.innerHTML='';empty.style.display='block';emptySearch.style.display='none';updateBulkBar();return}
  if(!links.length){grid.innerHTML='';empty.style.display='none';emptySearch.style.display='block';updateBulkBar();return}
  empty.style.display='none';emptySearch.style.display='none';
  grid.innerHTML=links.map(l=>{
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  const checked=selectedLinks.has(l.uuid)?'checked':'';
  return `<div class="cfg-card ${cardCls}">
    <div class="cfg-row">
      <span class="cfg-select"><input type="checkbox" ${checked} onchange="toggleLinkSelect('${l.uuid}',this)" title="انتخاب"></span>
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}</div>
        <div class="cfg-sub-meta">
          <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="پورت اتصال"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="آی‌پی‌های متصل / محدودیت"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="محدودیت سرعت"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود'}</span>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="window.open('${esc(l.sub_url)}','_blank')" title="باز کردن داشبورد ساب"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="openLinkChart('${l.uuid}','${esc(l.label)}')" title="نمودار مصرف ۳۰ روز اخیر"><i class="ti ti-chart-line"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
  updateBulkBar();
}
function toggleLinkSelect(uuid,el){
  if(el.checked)selectedLinks.add(uuid);else selectedLinks.delete(uuid);
  updateBulkBar();
}
function toggleSelectAllLinks(el){
  const list=filteredLinksList();
  if(el.checked)list.forEach(l=>selectedLinks.add(l.uuid));
  else list.forEach(l=>selectedLinks.delete(l.uuid));
  renderLinksGrid();
}
function clearLinksSelection(){selectedLinks.clear();renderLinksGrid();}
function openCfgCreate(){document.getElementById('cfg-overlay').classList.add('open');document.getElementById('cfg-drawer').classList.add('open')}
function closeCfgCreate(){document.getElementById('cfg-overlay').classList.remove('open');document.getElementById('cfg-drawer').classList.remove('open')}
function updateBulkBar(){
  const bar=document.getElementById('links-bulkbar');
  const selall=document.getElementById('links-selall');
  const n=selectedLinks.size;
  document.getElementById('links-selcount').textContent=toFa(n);
  bar.style.display=n>0?'flex':'none';
  const list=filteredLinksList();
  selall.checked=list.length>0&&list.every(l=>selectedLinks.has(l.uuid));
}
async function bulkLinksAction(action){
  const uuids=Array.from(selectedLinks);
  if(!uuids.length)return;
  if(action==='delete'&&!confirm(`حذف ${toFa(uuids.length)} کانفیگ انتخاب‌شده؟ این عمل غیرقابل بازگشت است.`))return;
  try{
    await Promise.all(uuids.map(uuid=>{
      if(action==='activate')return authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:true})});
      if(action==='deactivate')return authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:false})});
      if(action==='reset')return authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});
      if(action==='delete')return authF('/api/links/'+uuid,{method:'DELETE'});
    }));
    const msg={activate:'کانفیگ‌های انتخاب‌شده فعال شدند ✓',deactivate:'کانفیگ‌های انتخاب‌شده غیرفعال شدند ✓',reset:'مصرف کانفیگ‌های انتخاب‌شده ریست شد ✓',delete:'کانفیگ‌های انتخاب‌شده حذف شدند ✓'}[action];
    toast(msg,'ok');
    if(action==='delete')selectedLinks.clear();
    loadLinks();
  }catch(e){toast('خطا در اجرای عملیات گروهی','err')}
}
let linkChart=null;
async function openLinkChart(uuid,label){
  document.getElementById('lc-title').textContent='نمودار مصرف ۳۰ روز اخیر — '+label;
  openModal('modal-link-chart');
  try{
    const r=await authF('/api/links/'+uuid+'/history'),d=await r.json();
    const labels=d.days.map(x=>x.date.slice(5));
    const vals=d.days.map(x=>+(x.bytes/1024**2).toFixed(2));
    const ctx=document.getElementById('lc-canvas');
    if(linkChart)linkChart.destroy();
    linkChart=new Chart(ctx,{type:'bar',data:{labels,datasets:[{label:'مصرف (MB)',data:vals,backgroundColor:'rgba(255,255,255,.5)',borderRadius:5,maxBarThickness:22}]},
      options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{beginAtZero:true}}}});
  }catch(e){toast('خطا در دریافت تاریخچه مصرف','err')}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('کانفیگ ساخته شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ساخت','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const fingerprint=document.getElementById('el-fp').value||'chrome';
  const alpn=document.getElementById('el-alpn').value.trim();
  const port=Number(document.getElementById('el-port').value)||443;
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
let connsExpanded=new Set();
function toggleConnCard(uuid){
  if(connsExpanded.has(uuid))connsExpanded.delete(uuid);else connsExpanded.add(uuid);
  renderConnsGrid(window.__lastConfigs||[]);
}
function renderConnsGrid(configs){
  const grid=document.getElementById('conns-grid');
  grid.innerHTML=configs.map(cfg=>{
    const open=connsExpanded.has(cfg.uuid);
    const ipsHtml=(cfg.connections||[]).map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      return `<div style="display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:10px;background:var(--accent-d);border:1px solid var(--card-b);margin-top:7px">
        <div style="display:flex;align-items:center;gap:8px;min-width:0">
          <i class="ti ti-device-desktop" style="color:var(--t3)"></i>
          <span style="font-family:ui-monospace,monospace;font-size:12px;color:var(--t1)">${esc(c.ip)}</span>
          <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i></button>
        </div>
        <div style="display:flex;align-items:center;gap:12px;font-size:10.5px;color:var(--t3);flex-shrink:0">
          <span><i class="ti ti-repeat" style="font-size:10px"></i> ${toFa(c.sessions)} سشن</span>
          <span><i class="ti ti-transfer" style="font-size:10px"></i> ${esc(c.bytes_fmt)}</span>
          <span><i class="ti ti-clock" style="font-size:10px"></i> ${dur}</span>
        </div>
      </div>`;
    }).join('') || '<div style="padding:10px;color:var(--t3);font-size:11px">اتصالی نیست</div>';
    return `<div class="conn-card-v2" style="cursor:pointer" onclick="toggleConnCard('${cfg.uuid}')">
      <div class="conn-card-v2-glow"></div>
      <div class="conn-card-v2-top">
        <div class="conn-avatar"><i class="ti ti-key"></i></div>
        <div class="conn-card-v2-id">
          <div class="conn-ip-v2">${esc(cfg.label)}</div>
          <div class="conn-label-v2">${toFa(cfg.ip_count)} آی‌پی · ${toFa(cfg.sessions)} سشن</div>
        </div>
        <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
      </div>
      <div class="conn-card-v2-divider"></div>
      <div class="conn-card-v2-body">
        <div class="conn-proto-row">${protoBadge(cfg.protocol)}</div>
        <div class="conn-stat-row">
          <div class="conn-stat-box">
            <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
            <div>
              <div class="conn-stat-text-label">ترافیک</div>
              <div class="conn-stat-text-val">${esc(cfg.bytes_fmt)}</div>
            </div>
          </div>
          <div class="conn-stat-box">
            <div class="conn-stat-icon time"><i class="ti ti-users"></i></div>
            <div>
              <div class="conn-stat-text-label">آی‌پی‌های متصل</div>
              <div class="conn-stat-text-val">${toFa(cfg.ip_count)}</div>
            </div>
          </div>
        </div>
        <div style="text-align:center;font-size:10.5px;color:var(--accent2);margin-top:8px"><i class="ti ti-chevron-${open?'up':'down'}"></i> ${open?'بستن':'نمایش اتصالات'}</div>
        ${open?`<div onclick="event.stopPropagation()">${ipsHtml}</div>`:''}
      </div>
    </div>`;
  }).join('');
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live-badge').innerHTML='<span class="dot dg pulse"></span> '+d.raw_count+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.raw_count);
    const configs=d.configs||[];
    window.__lastConfigs=configs;
    if(!configs.length){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=configs.reduce((s,c)=>s+(c.bytes||0),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=configs.reduce((s,c)=>s+c.ip_count,0);
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const allDurs=[];
    configs.forEach(c=>(c.connections||[]).forEach(ip=>allDurs.push(ip.connected_at?Math.max(0,Math.floor((Date.now()-new Date(ip.connected_at).getTime())/1000)):0)));
    const avgSec=allDurs.length?Math.floor(allDurs.reduce((a,b)=>a+b,0)/allDurs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    renderConnsGrid(configs);
  }catch(e){console.error(e)}
}

// ── داشبورد کانفیگ‌ها: از داده‌ی همون /api/links و /api/connections استفاده می‌کنه ──
let cfgDashSelected=null;
async function loadCfgDash(){
  try{
    if(!allLinksList.length)await loadLinks();
    await loadConns();
    renderCfgDashList();
    if(cfgDashSelected&&allLinksList.some(l=>l.uuid===cfgDashSelected))renderCfgDashDetail(cfgDashSelected);
  }catch(e){console.error(e)}
}
function renderCfgDashList(){
  const wrap=document.getElementById('cfgdash-list'),empty=document.getElementById('cfgdash-empty');
  document.getElementById('cfgdash-count').textContent=toFa(allLinksList.length);
  if(!allLinksList.length){wrap.innerHTML='';empty.style.display='block';return}
  empty.style.display='none';
  wrap.innerHTML=allLinksList.map(l=>{
    const allowed=l.active&&!l.expired;
    const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
    const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
    return `<div class="cfgdash-item${cfgDashSelected===l.uuid?' on':''}" onclick="selectCfgDash('${l.uuid}')">
      <div class="cfgdash-item-top"><span class="cfg-status-dot ${allowed?'pulse':''}"></span><span class="cfgdash-item-label">${esc(l.label)}</span>${protoBadge(l.protocol)}</div>
      <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
      <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>${l.connected_ips||0} آی‌پی زنده</span></div>
    </div>`;
  }).join('');
}
function selectCfgDash(uuid){cfgDashSelected=uuid;renderCfgDashList();renderCfgDashDetail(uuid)}
function renderCfgDashDetail(uuid){
  const box=document.getElementById('cfgdash-detail');
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l){box.innerHTML='<div class="card"><div class="empty"><i class="ti ti-mood-empty"></i><p>این کانفیگ دیگر وجود ندارد</p></div></div>';return}
  const grp=(window.__lastConfigs||[]).find(c=>c.uuid===uuid);
  const ips=grp?grp.connections||[]:[];
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const speedTxt=l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود';
  box.innerHTML=`
    <div class="card" style="margin-bottom:14px">
      <div class="card-title"><i class="ti ti-key"></i> ${esc(l.label)} ${l.active&&!l.expired?'<span class="badge bg-green" style="margin-right:6px">فعال</span>':'<span class="badge bg-red" style="margin-right:6px">'+(l.expired?'منقضی':'غیرفعال')+'</span>'}
        <span class="ml-auto" style="display:flex;gap:6px">
          <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
          <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
          <button class="btn btn-sm btn-g btn-icon" onclick="openLinkChart('${l.uuid}','${esc(l.label)}')" title="نمودار مصرف"><i class="ti ti-chart-line"></i></button>
        </span>
      </div>
      <div class="cfgdash-stats">
        <div class="cfgdash-stat"><div class="cfgdash-stat-l">مصرف / سقف</div><div class="cfgdash-stat-v">${fmtB(l.used_bytes)}</div><div class="utxt" style="margin-top:6px"><span></span><span>از ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div><div class="ubar" style="margin-top:6px"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div></div>
        <div class="cfgdash-stat"><div class="cfgdash-stat-l">محدودیت سرعت</div><div class="cfgdash-stat-v" style="font-size:14px">${speedTxt}</div></div>
        <div class="cfgdash-stat"><div class="cfgdash-stat-l">آی‌پی زنده / محدودیت</div><div class="cfgdash-stat-v">${toFa(l.connected_ips||0)}${l.ip_limit?(' / '+toFa(l.ip_limit)):' (∞)'}</div></div>
        <div class="cfgdash-stat"><div class="cfgdash-stat-l">انقضا</div><div class="cfgdash-stat-v" style="font-size:14px">${expChip(l.expires_at,l.expired)}</div></div>
      </div>
      <div class="sr"><span class="sr-k"><i class="ti ti-route"></i> پروتکل</span><span class="sr-v">${protoBadge(l.protocol)}</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-plug"></i> پورت</span><span class="sr-v">${toFa(l.port||443)}</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">${esc(l.fingerprint||'chrome')}</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar"></i> تاریخ ساخت</span><span class="sr-v">${new Date(l.created_at).toLocaleDateString('fa-IR')}</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-map-pin"></i> آی‌پی‌های متصل هم‌اکنون <span class="ml-auto badge bg-blue">${toFa(ips.length)}</span></div>
      ${ips.length?ips.map(c=>{
        const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
        const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
        return `<div class="cfgdash-ip-row">
          <span class="ip"><span class="dot dg pulse" style="width:7px;height:7px;border-radius:50%;background:var(--green);display:inline-block"></span> ${esc(c.ip)}</span>
          <div class="cfgdash-ip-meta">
            <span><i class="ti ti-repeat"></i> ${toFa(c.sessions)} سشن</span>
            <span><i class="ti ti-transfer"></i> ${esc(c.bytes_fmt)}</span>
            <span><i class="ti ti-clock"></i> ${dur}</span>
          </div>
        </div>`;
      }).join(''):'<div class="empty"><i class="ti ti-plug-off"></i><p>در حال حاضر آی‌پی متصلی به این کانفیگ نیست</p></div>'}
    </div>
  `;
}

async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();loadLinks();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}
async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز تغییر کرد ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast('✗ '+e.message,'err')}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
  label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}
function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  const c1=document.getElementById('ch1').getContext('2d');
  const grad1=makeGradient(c1,'rgba(255,255,255,.35)','rgba(255,255,255,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(0,0,0,.96)',borderColor:'rgba(255,255,255,.1)',borderWidth:1,
        titleColor:'#f1f5f9',bodyColor:'#94a3b8',padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#64748b',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(255,255,255,.05)'},border:{display:false},ticks:{color:'#64748b',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#ffffff',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#ffffff',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,'rgba(255,255,255,.42)','rgba(255,255,255,.06)','rgba(255,255,255,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#ffffff',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#ffffff',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#eab308',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(0,0,0,.97)',borderColor:'rgba(255,255,255,.1)',borderWidth:1,
          titleColor:'#f1f5f9',bodyColor:'#94a3b8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#64748b',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(255,255,255,.04)'},border:{display:false},ticks:{color:'#64748b',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  fetchStats();loadLinks();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
    if(document.getElementById('pg-cfgdash').classList.contains('on'))loadCfgDash();
  },5000);
});
</script>
</body></html>"""


# جایگزینی نهایی لوگو در صفحات استاتیک (LOGIN_HTML / DASHBOARD_HTML)



def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب — تم سفید و مشکی، طراحی اختصاصی Tehranzone"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>Tehranzone Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.44.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#000000;--bg2:#050505;--bg3:#0a0a0a;
  --card:#0a0a0a;--card-b:rgba(255,255,255,0.06);--card-bh:rgba(255,255,255,0.12);
  --accent:#ffffff;--accent2:rgba(255,255,255,0.7);--accent-d:rgba(255,255,255,0.04);
  --green:#22c55e;--green-bg:rgba(34,197,94,0.08);--green-t:#4ade80;
  --red:#ef4444;--red-bg:rgba(239,68,68,0.08);--red-t:#f87171;
  --amber:#f59e0b;--amber-bg:rgba(245,158,11,0.08);--amber-t:#fbbf24;
  --purple:#a855f7;--purple-bg:rgba(168,85,247,0.08);--purple-t:#c084fc;
  --t1:#ffffff;--t2:rgba(255,255,255,0.55);--t3:rgba(255,255,255,0.25);
  --radius:16px;--shadow:0 12px 40px rgba(0,0,0,0.6);
  --serif:'Vazirmatn',sans-serif;
}}
html,body{{min-height:100%;background:#000000;font-family:var(--serif);color:var(--t1);font-size:14px}}
.wrap{{position:relative;z-index:10;max-width:560px;margin:0 auto;padding:20px 16px 64px}}

.top{{display:flex;align-items:center;justify-content:flex-end;margin-bottom:28px;gap:10px}}
.brand{{display:flex;align-items:center;gap:10px;min-width:0}}
.brand-icon{{width:36px;height:36px;border-radius:10px;background:#ffffff;color:#000000;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:900;flex-shrink:0}}
.brand-name{{font-size:14px;font-weight:800;color:#ffffff;letter-spacing:.04em}}
.brand-ver{{font-size:8.5px;color:var(--t3);font-weight:500;margin-top:1px}}

.sub-card{{background:#0a0a0a;border:1px solid var(--card-b);border-radius:16px;padding:20px;margin-bottom:14px;position:relative;overflow:hidden}}
.sub-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.06),transparent)}}
.sub-label{{font-size:9px;font-weight:700;color:var(--t3);text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px;display:flex;align-items:center;gap:5px}}
.sub-label i{{font-size:11px}}
.sub-name{{font-size:18px;font-weight:800;color:#ffffff;margin-bottom:4px;letter-spacing:-.01em}}
.sub-desc{{font-size:11.5px;color:var(--t2);line-height:1.7;margin-bottom:14px}}
.sub-meta{{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:5px;margin-bottom:14px}}
.sub-meta i{{font-size:11px}}
.sub-url-box{{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:10px;padding:11px 13px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.sub-url{{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--t2);word-break:break-all;flex:1;min-width:120px}}
.sub-url-copy{{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.06);color:var(--t2);border-radius:7px;padding:5px 10px;font-size:9.5px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:4px;transition:.15s;font-family:inherit;white-space:nowrap}}
.sub-url-copy:hover{{background:rgba(255,255,255,0.1);color:#ffffff}}

.stats-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}}
.stat{{background:#0a0a0a;border:1px solid var(--card-b);border-radius:12px;padding:14px 13px;text-align:center}}
.stat-lbl{{font-size:8px;font-weight:700;color:var(--t3);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}}
.stat-val{{font-size:20px;font-weight:800;color:#ffffff;line-height:1}}
.stat-sub{{font-size:8.5px;color:var(--t3);margin-top:5px}}

.copy-all{{display:flex;align-items:center;gap:12px;background:#ffffff;border-radius:14px;padding:14px 16px;margin-bottom:14px}}
.copy-all-txt{{flex:1;min-width:0}}
.copy-all-title{{font-size:12px;font-weight:800;color:#000000;display:flex;align-items:center;gap:5px}}
.copy-all-sub{{font-size:9.5px;color:rgba(0,0,0,0.4);margin-top:2px}}
.copy-all-btn{{background:#000000;color:#ffffff;border:none;border-radius:10px;padding:9px 16px;font-family:inherit;font-size:11.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:5px;transition:.15s;white-space:nowrap;flex-shrink:0}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.4)}}

.cfgs-title{{font-size:10px;font-weight:800;color:var(--t3);margin-bottom:10px;display:flex;align-items:center;gap:5px;text-transform:uppercase;letter-spacing:.08em}}
.cfgs-title i{{font-size:12px;color:var(--t2)}}

.cfg-card{{background:#0a0a0a;border:1px solid var(--card-b);border-radius:14px;transition:all .2s;overflow:hidden;margin-bottom:8px}}
.cfg-card:hover{{border-color:var(--card-bh)}}
.cfg-card.inactive{{opacity:.5}}
.cfg-card-top{{padding:14px 15px 12px;position:relative}}
.cfg-card-top::before{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-card-top::before{{background:var(--red)}}
.cfg-card-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:10px}}
.cfg-card-name{{font-size:13px;font-weight:700;color:#ffffff}}
.cfg-card-badges{{display:flex;gap:4px;flex-wrap:wrap;margin-top:4px}}
.proto-chip{{font-size:8.5px;padding:2px 7px;border-radius:5px;font-weight:700;letter-spacing:.02em}}
.pc-ws{{background:rgba(255,255,255,0.05);color:var(--t2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.conn-chip{{display:inline-flex;align-items:center;gap:3px;font-size:8.5px;padding:2px 7px;border-radius:12px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:4px;height:4px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.cfg-status{{display:flex;align-items:center;gap:4px;font-size:9px;font-weight:700;padding:3px 8px;border-radius:14px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}

.ubar{{height:3px;border-radius:2px;background:rgba(255,255,255,0.04);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:2px;transition:width .5s ease}}
.utxt{{font-size:8.5px;color:var(--t3);display:flex;justify-content:space-between}}

.cfg-card-divider{{height:0;border-top:1px dashed rgba(255,255,255,0.05);margin:0 15px}}
.cfg-card-bottom{{padding:12px 15px 14px}}
.cfg-link-btn{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:8px;background:transparent;border:1px dashed rgba(255,255,255,0.06);border-radius:9px;padding:9px 12px;cursor:pointer;font-family:inherit;color:var(--t3);font-size:10.5px;font-weight:600;transition:.15s}}
.cfg-link-btn:hover{{background:rgba(255,255,255,0.02);border-color:rgba(255,255,255,0.1);color:var(--t2)}}
.cfg-link-btn .ltl{{display:flex;align-items:center;gap:6px}}
.cfg-link-btn i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-btn.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:10px 12px;font-size:9px;font-family:ui-monospace,monospace;color:var(--t2);word-break:break-all;line-height:1.7;margin-top:8px;max-height:80px;overflow-y:auto}}
.cfg-vless::-webkit-scrollbar{{width:2px}}
.cfg-vless::-webkit-scrollbar-thumb{{background:rgba(255,255,255,0.06);border-radius:2px}}
.cfg-card-actions{{display:flex;gap:5px;flex-wrap:wrap;margin-top:10px}}
.btn{{font-family:inherit;font-size:10.5px;font-weight:700;border-radius:8px;padding:7px 12px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:12px}}
.btn-w{{background:#ffffff;color:#000000}}
.btn-w:hover{{box-shadow:0 3px 10px rgba(255,255,255,.1)}}
.btn-g{{background:rgba(255,255,255,0.04);color:var(--t2);border:1px solid rgba(255,255,255,0.06)}}
.btn-g:hover{{background:rgba(255,255,255,0.08);color:var(--t1)}}

.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:#0a0a0a;border:1px solid rgba(255,255,255,0.06);border-radius:20px;text-align:center;max-width:360px;width:100%;overflow:hidden}}
.lock-banner{{padding:36px 28px 24px;position:relative}}
.lock-shield{{width:56px;height:56px;border-radius:16px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-6px;border-radius:20px;border:1px solid rgba(255,255,255,0.04);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.06);opacity:0}}}}
.lock-shield i{{font-size:24px;color:#ffffff}}
.lock-title{{font-size:17px;font-weight:800;color:#ffffff;margin-bottom:5px}}
.lock-sub{{font-size:11.5px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:0 28px 28px}}
.lock-field{{position:relative;margin-bottom:12px}}
.lock-inp{{width:100%;padding:12px 42px;border-radius:11px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.02);color:#ffffff;font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
.lock-inp:focus{{border-color:rgba(255,255,255,0.15);background:rgba(255,255,255,0.04)}}
.lock-eye{{position:absolute;left:12px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:15px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--t2)}}
.lock-lockicon{{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11px;margin-bottom:10px;min-height:14px;display:flex;align-items:center;justify-content:center;gap:4px}}
.lock-btn{{width:100%;justify-content:center;padding:12px;font-size:12.5px;border-radius:11px}}
.lock-footer{{padding:12px 28px;border-top:1px solid rgba(255,255,255,0.04);font-size:9.5px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:5px}}

.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:34px;display:block;margin-bottom:12px}}

.toast{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(40px);background:#0a0a0a;border:1px solid rgba(255,255,255,0.08);color:#ffffff;border-radius:10px;padding:9px 18px;font-size:12px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:6px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(34,197,94,0.2);background:var(--green-bg);color:var(--green-t)}}

.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:#0a0a0a;border:1px solid rgba(255,255,255,0.06);border-radius:18px;padding:24px;text-align:center;max-width:320px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13px;font-weight:800;margin-bottom:14px;color:#ffffff}}
.qr-img{{border-radius:12px;overflow:hidden;margin-bottom:14px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:12px}}
.qr-close{{width:100%;justify-content:center}}

.footer{{text-align:center;padding-top:24px;font-size:10px;color:var(--t3)}}
.footer a{{color:var(--t2);font-weight:700}}

@media(max-width:520px){{
  .stats-row{{grid-template-columns:1fr 1fr}}
  .stats-row .stat:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:16px}}
  .copy-all{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:14px 12px 50px}}
  .lock-banner{{padding:30px 22px 20px}}
  .lock-form{{padding:0 22px 24px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
/* Tehranzone subscription monochrome skin */
html,body{{background:#f5f5f5!important;color:#111!important}}.wrap{{max-width:620px}}.brand-icon{{background:#000!important;color:#fff!important}}.brand-name{{color:#000!important}}.brand-ver{{color:#777!important}}.sub-card,.stat,.cfg-card,.lock-card,.qr-box{{background:#fff!important;border-color:#ddd!important;box-shadow:0 8px 28px rgba(0,0,0,.06)}}.sub-card::before{{background:linear-gradient(90deg,transparent,#000,transparent)!important;opacity:.08}}.sub-label,.sub-meta,.stat-lbl,.stat-sub,.cfgs-title,.utxt{{color:#777!important}}.sub-name,.cfg-card-name,.stat-val,.lock-title,.qr-title{{color:#111!important}}.sub-desc{{color:#555!important}}.sub-url-box,.cfg-vless,.cfg-link-btn,.lock-inp{{background:#f6f6f6!important;border-color:#ddd!important;color:#222!important}}.sub-url{{color:#444!important}}.sub-url-copy{{background:#fff!important;color:#222!important;border-color:#d5d5d5!important}}.sub-url-copy:hover{{background:#000!important;color:#fff!important}}.copy-all{{background:#000!important}}.copy-all-title{{color:#fff!important}}.copy-all-sub{{color:rgba(255,255,255,.58)!important}}.copy-all-btn,.btn-w{{background:#fff!important;color:#000!important}}.btn-g{{background:#fff!important;color:#111!important;border-color:#d5d5d5!important}}.btn-g:hover{{background:#000!important;color:#fff!important}}.cfg-card-top::before{{background:#000!important}}.cfg-card.inactive .cfg-card-top::before{{background:#777!important}}.pc-ws{{background:#f0f0f0!important;color:#222!important}}.ubar{{background:#e3e3e3!important}}.cfg-card-divider{{border-color:#ddd!important}}.cfg-link-btn:hover{{background:#eee!important;color:#111!important}}.cfg-vless{{color:#333!important}}.lock-shield{{background:#f3f3f3!important;border-color:#ddd!important}}.lock-shield i{{color:#000!important}}.lock-inp{{color:#111!important}}.lock-btn{{background:#000!important;color:#fff!important}}.lock-footer{{border-color:#ddd!important;color:#777!important}}.footer{{color:#777!important}}.footer a{{color:#111!important}}.qr-modal{{background:rgba(0,0,0,.62)!important}}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g qr-close" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-icon">N</div>
      <div><div class="brand-name">Tehranzone</div><div class="brand-ver">v1.0</div></div>
    </div>
  </div>
  <div id="root"></div>
  <div class="footer">Tehranzone v1.0</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp"><i class="ti ti-bolt"></i> XHTTP · auto</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/p/' + UUID_KEY);
  const subUrl = baseSubUrl;

  window._nrlSubUrl  = subUrl;
  window._nrlSubName = d.name;
  window._nrlLinks   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url,
    label : l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-card">
      <div class="sub-label"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-url-box">
        <span class="sub-url">${{esc(subUrl)}}</span>
        <button class="sub-url-copy" onclick="navigator.clipboard.writeText(window._nrlSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
          <i class="ti ti-copy"></i> کپی
        </button>
        <button class="sub-url-copy" onclick="showQR(window._nrlSubName + ' — کل گروه', window._nrlSubUrl)">
          <i class="ti ti-qrcode"></i> QR
        </button>
      </div>
    </div>

    <div class="copy-all">
      <div class="copy-all-txt">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی (${{toFa(activeCount)}})</button>
    </div>

    <div class="stats-row">
      <div class="stat">
        <div class="stat-lbl">کانفیگ فعال</div>
        <div class="stat-val">${{toFa(activeCount)}}</div>
        <div class="stat-sub">از ${{toFa(d.links.length)}}</div>
      </div>
      <div class="stat">
        <div class="stat-lbl">اتصالات</div>
        <div class="stat-val">${{toFa(d.active_connections)}}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;justify-content:center;gap:4px"><span class="dot"></span> آنلاین</div>
      </div>
      <div class="stat">
        <div class="stat-lbl">مصرف کل</div>
        <div class="stat-val" style="font-size:16px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
      </div>
    </div>

    <div class="cfgs-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}})</div>
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-card-top">
              <div class="cfg-card-head">
                <div>
                  <div class="cfg-card-name">${{esc(l.label)}}</div>
                  <div class="cfg-card-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
                  </div>
                </div>
                <span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
              </div>
              <div style="margin-top:8px">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>${{esc(l.used_fmt)}} مصرف</span><span>سهمیه: ${{lim}}</span></div>
              </div>
            </div>
            <div class="cfg-card-divider"></div>
            <div class="cfg-card-bottom">
              <button class="cfg-link-btn" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                </div>
              </div>
              <div class="cfg-card-actions">
                <button class="btn btn-w"
                  onclick="navigator.clipboard.writeText(window._nrlLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
                  <i class="ti ti-copy"></i> کپی لینک
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._nrlLinks[${{i}}].label, window._nrlLinks[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
  `;
  setTimeout(() => autoRefresh(), 30000);
}}

function copyAllConfigs(){{
  const links=window._nrlLinks||[];
  if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));
}}

async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }}
}}

init();
</script>
</body></html>"""
