import streamlit as st

st.set_page_config(page_title="YouTube TV · Discover", page_icon="▶", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{--bg:#0c0d10;--panel:#17191e;--line:#2b2d33;--muted:#9da1aa;--ink:#f5f6f8;--red:#ff3f55;--mint:#b6f0d0;--focus:#f7f8fa}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;color:var(--ink)}
.stApp{background:radial-gradient(ellipse at 68% 0%,#25212a 0%,#0c0d10 44%);color:var(--ink)}
#MainMenu,footer,header{visibility:hidden}.block-container{max-width:1600px;padding:1.2rem 3.1rem 3rem}
h1,h2,h3{font-family:'Space Grotesk',sans-serif;letter-spacing:-.045em}h1{font-size:3rem!important;line-height:1.03!important;margin:.55rem 0 .7rem!important}h2{font-size:1.55rem!important;margin:.2rem 0 .3rem!important}h3{font-size:1.14rem!important}
.brand{font-family:'Space Grotesk';font-size:1.2rem;font-weight:700;letter-spacing:-.04em}.brand span{color:var(--red)}
.top{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding:0 0 1rem;margin-bottom:1.35rem}
.eyebrow{color:#c9cbd1;font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase}.muted{color:var(--muted);font-size:.92rem;line-height:1.5}
.hero{min-height:340px;border:1px solid #42404a;border-radius:23px;padding:35px 42px;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden;background:radial-gradient(ellipse at 78% 30%,#ec796855,transparent 26%),radial-gradient(ellipse at 86% 20%,#63559c88,transparent 48%),linear-gradient(110deg,#24212a,#211923 45%,#38202d);}
.hero:after{content:'✦';font-size:11rem;color:#ffffff0c;position:absolute;right:7%;top:1%;font-family:'Space Grotesk';transform:rotate(-12deg)}
.hero-content{position:relative;z-index:1;max-width:680px}.hero-title{font-family:'Space Grotesk';font-size:3.1rem;font-weight:700;letter-spacing:-.06em;line-height:1.02;margin:.5rem 0}.hero-copy{max-width:570px;color:#d2cfd5;font-size:1rem;line-height:1.55}
.tag{display:inline-block;color:#eee;background:#ffffff1b;border:1px solid #ffffff27;border-radius:100px;padding:6px 11px;font-size:.75rem;margin-right:6px}
.section-head{display:flex;align-items:end;justify-content:space-between;margin:27px 0 12px}.poster{height:160px;border-radius:14px;padding:13px;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;position:relative;border:1px solid #ffffff16}
.poster:before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 20%,#050609d9 100%)}.poster-body{position:relative;z-index:1}.poster-icon{font-size:2.15rem;position:absolute;left:14px;top:10px;filter:drop-shadow(0 4px 12px #0008)}.title{font-weight:700;font-size:.96rem;line-height:1.2}.meta{color:#b8bbc2;font-size:.76rem;margin-top:5px}
.p0{background:radial-gradient(ellipse at 70% 25%,#b75f55,#3d2741 58%,#171824)}.p1{background:radial-gradient(ellipse at 32% 24%,#dfac60,#6a3f35 55%,#1c2028)}.p2{background:radial-gradient(ellipse at 67% 25%,#6fb5ae,#2d5470 56%,#17222d)}.p3{background:radial-gradient(ellipse at 68% 28%,#aa87c7,#63426e 57%,#242139)}.p4{background:radial-gradient(ellipse at 30% 24%,#e7834a,#824a43 55%,#24202a)}.p5{background:radial-gradient(ellipse at 68% 28%,#8db35b,#49633c 56%,#1f282b)}.p6{background:radial-gradient(ellipse at 70% 30%,#749ccf,#3a4d79 55%,#151c2d)}.p7{background:radial-gradient(ellipse at 68% 25%,#d5877e,#8a4c6b 55%,#211c2a)}
div[data-testid="stButton"]>button{border-radius:12px;min-height:3.2rem;background:#1b1d22;border:1px solid #3a3d44;color:#f6f7f9;font-size:1rem;font-weight:600}
div[data-testid="stButton"]>button:hover{border-color:#f5f6f8;color:#fff;background:#292b31;transform:translateY(-1px)}
div[data-testid="stButton"]>button:focus{outline:3px solid #f6f7fa!important;outline-offset:2px}
button[kind="primary"]{background:var(--red)!important;border-color:var(--red)!important;color:white!important}
div[data-testid="stTextInput"]>div>div,div[data-testid="stSelectbox"]>div{background:#181a1f;border-color:#373941;color:#f5f6f8}
div[role="radiogroup"]{gap:.6rem}div[role="radiogroup"] label{background:#181a1f;border:1px solid #353840;border-radius:100px;padding:.45rem 1rem!important;font-size:1rem}
.remote{border:1px solid #32343a;background:#15171b;border-radius:14px;padding:12px 16px;color:#c8cad0;font-size:.83rem}
.spotlight{background:linear-gradient(130deg,#1c2027,#18191f);border:1px solid #30323a;border-radius:17px;padding:18px 20px}
@media(max-width:900px){.block-container{padding-left:1rem;padding-right:1rem}h1{font-size:2.15rem!important}.hero{min-height:300px;padding:24px}.hero-title{font-size:2.3rem}.poster{height:130px}}
</style>
""", unsafe_allow_html=True)

SHOWS=[
 {"title":"The Last Lightkeepers","genre":"Adventure","year":"2025","duration":"1h 48m","icon":"🌅","poster":"p0","desc":"On a far northern island, one family keeps an old lighthouse burning through the longest winter."},
 {"title":"Kitchen, Together","genre":"Food","year":"New episodes","duration":"42 min","icon":"🍋","poster":"p1","desc":"Two friends travel home kitchens to find the recipes that bring everyone to the table."},
 {"title":"Blue Planet: Deep","genre":"Nature","year":"2025","duration":"52 min","icon":"🌊","poster":"p2","desc":"A closer look at the strange, beautiful life hidden in the deepest parts of the ocean."},
 {"title":"Small Town Sounds","genre":"Music","year":"2024","duration":"1h 12m","icon":"🎸","poster":"p3","desc":"A road trip through intimate live sessions and the people who make them unforgettable."},
 {"title":"Orbit Seven","genre":"Sci-fi","year":"New","duration":"8 episodes","icon":"🚀","poster":"p4","desc":"A quiet research mission becomes humanity's first contact with a distant intelligence."},
 {"title":"Wild Neighbors","genre":"Nature","year":"2025","duration":"6 episodes","icon":"🦊","poster":"p5","desc":"A neighborhood learns to share its streets and gardens with the wild creatures nearby."},
 {"title":"The Art of Nothing","genre":"Documentary","year":"2024","duration":"38 min","icon":"🎨","poster":"p6","desc":"Artists make room for boredom, curiosity, and the unexpected things that follow."},
 {"title":"Weekend in Kyoto","genre":"Travel","year":"2025","duration":"29 min","icon":"🏮","poster":"p7","desc":"A gentle guide to backstreets, tea houses, and early mornings in Kyoto."},
]
if "saved" not in st.session_state: st.session_state.saved=[]
if "selected" not in st.session_state: st.session_state.selected=0

top1,top2=st.columns([1,2.4])
with top1: st.markdown('<div class="brand">▶ YouTube <span>TV</span></div>',unsafe_allow_html=True)
with top2: page=st.radio("TV navigation",["Home","Search","My List","Settings"],horizontal=True,label_visibility="collapsed",key="tv_page")

if page=="Home":
 featured=SHOWS[st.session_state.selected]
 st.markdown('<div class="eyebrow">A little something for tonight</div>',unsafe_allow_html=True)
 st.markdown(f'<div class="hero"><div class="hero-content"><span class="tag">{featured["genre"]}</span><span class="tag">{featured["year"]}</span><div class="hero-title">{featured["title"]}</div><div class="hero-copy">{featured["desc"]}</div></div></div>',unsafe_allow_html=True)
 c1,c2,c3=st.columns([1,1,3])
 with c1:
  if st.button("▶  Play",type="primary",use_container_width=True): st.toast(f"Playing {featured['title']}")
 with c2:
  label="✓  In My List" if st.session_state.selected in st.session_state.saved else "＋  My List"
  if st.button(label,use_container_width=True):
   if st.session_state.selected in st.session_state.saved: st.session_state.saved.remove(st.session_state.selected)
   else: st.session_state.saved.append(st.session_state.selected)
   st.rerun()
 with c3: st.markdown('<div class="remote">Remote: use Tab / arrow keys to move · Enter to select · Search to find a title · My List keeps your picks together</div>',unsafe_allow_html=True)
 st.markdown('<div class="section-head"><div><h2>Picked for your household</h2><div class="muted">Because you watched nature and adventure</div></div><span class="muted">1 / 8</span></div>',unsafe_allow_html=True)
 cols=st.columns(4,gap="medium")
 for i,item in enumerate(SHOWS[:4]):
  with cols[i]:
   st.markdown(f'<div class="poster {item["poster"]}"><div class="poster-icon">{item["icon"]}</div><div class="poster-body"><div class="title">{item["title"]}</div><div class="meta">{item["genre"]} · {item["year"]} · {item["duration"]}</div></div></div>',unsafe_allow_html=True)
   if st.button("Select",key=f"home{i}",use_container_width=True): st.session_state.selected=i; st.rerun()
 st.markdown('<div class="section-head"><div><h2>Continue watching</h2><div class="muted">Pick up right where you left off</div></div></div>',unsafe_allow_html=True)
 cols=st.columns(4,gap="medium")
 for i,item in enumerate(SHOWS[4:8],start=4):
  with cols[i-4]:
   st.markdown(f'<div class="poster {item["poster"]}"><div class="poster-icon">{item["icon"]}</div><div class="poster-body"><div class="title">{item["title"]}</div><div class="meta">{item["genre"]} · {item["duration"]}</div></div></div>',unsafe_allow_html=True)
   st.progress([.42,.7,.26,.84][i-4],text="Continue")
   if st.button("Watch",key=f"watch{i}",use_container_width=True): st.session_state.selected=i; st.toast(f"Playing {item['title']}")

elif page=="Search":
 st.markdown('<div class="eyebrow">Search your way</div><h1>Find something good.</h1><div class="muted">Search by title or browse a genre. No tiny keyboard needed.</div>',unsafe_allow_html=True)
 query=st.text_input("Search titles and genres",placeholder="Try ‘nature’, ‘Kyoto’, or ‘music’")
 genre=st.selectbox("Browse by genre",["All genres"]+sorted({x["genre"] for x in SHOWS}))
 results=[(i,x) for i,x in enumerate(SHOWS) if (not query or query.lower() in (x["title"]+x["genre"]+x["desc"]).lower()) and (genre=="All genres" or x["genre"]==genre)]
 st.markdown(f'<div class="section-head"><div><h2>{len(results)} picks for you</h2></div><div class="muted">Use the remote to choose a card</div></div>',unsafe_allow_html=True)
 for row in range(0,len(results),4):
  cols=st.columns(4,gap="medium")
  for col,(i,item) in zip(cols,results[row:row+4]):
   with col:
    st.markdown(f'<div class="poster {item["poster"]}"><div class="poster-icon">{item["icon"]}</div><div class="poster-body"><div class="title">{item["title"]}</div><div class="meta">{item["genre"]} · {item["year"]}</div></div></div>',unsafe_allow_html=True)
    if st.button("View details",key=f"search{i}",use_container_width=True): st.session_state.selected=i; st.toast(item["desc"])

elif page=="My List":
 st.markdown('<div class="eyebrow">Saved across your devices</div><h1>Your watch list.</h1><div class="muted">Keep movie night simple. Your picks stay together here.</div>',unsafe_allow_html=True)
 if not st.session_state.saved: st.info("Your list is ready. Choose ＋ My List on a title to save it for later.")
 else:
  results=[(i,SHOWS[i]) for i in st.session_state.saved]
  cols=st.columns(4,gap="medium")
  for col,(i,item) in zip(cols,results):
   with col:
    st.markdown(f'<div class="poster {item["poster"]}"><div class="poster-icon">{item["icon"]}</div><div class="poster-body"><div class="title">{item["title"]}</div><div class="meta">{item["genre"]} · {item["duration"]}</div></div></div>',unsafe_allow_html=True)
    if st.button("Remove",key=f"remove{i}",use_container_width=True): st.session_state.saved.remove(i); st.rerun()
 st.markdown('<div class="spotlight"><b>Across your devices</b><div class="muted" style="margin-top:5px">Your list is designed to stay in sync between TV and mobile. This demo stores picks for the current session.</div></div>',unsafe_allow_html=True)

else:
 st.markdown('<div class="eyebrow">Comfort for everyone</div><h1>Make TV feel right.</h1><div class="muted">A few simple choices to make discovery and watching easier.</div>',unsafe_allow_html=True)
 left,right=st.columns(2,gap="large")
 with left:
  st.markdown('<div class="spotlight"><h2>Household recommendations</h2><div class="muted">Tune the mix shown on your home screen.</div>',unsafe_allow_html=True)
  st.multiselect("Interests",["Nature","Adventure","Food","Music","Travel","Documentary","Sci-fi"],default=["Nature","Adventure","Food"])
  st.selectbox("Who is watching?",["Everyone","Kids","Adults"])
  st.markdown('</div>',unsafe_allow_html=True)
 with right:
  st.markdown('<div class="spotlight"><h2>Remote & display</h2><div class="muted">Keep controls clear from across the room.</div>',unsafe_allow_html=True)
  st.toggle("High contrast focus highlight",value=True)
  st.toggle("Reduce motion",value=False)
  st.selectbox("Text size",["Standard","Large","Extra large"])
  st.markdown('</div>',unsafe_allow_html=True)
 st.button("Save preferences",type="primary")

st.markdown('<div style="border-top:1px solid #2b2d33;margin-top:30px;padding-top:14px" class="muted">A Smart TV discovery concept · Sample titles and session-only lists · Not affiliated with YouTube</div>',unsafe_allow_html=True)
