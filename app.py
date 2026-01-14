import streamlit as st
import pandas as pd
from pyxirr import xirr
from datetime import datetime, date
import random

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Financial Calculators Suite - Pro Edition", layout="wide")

# --- CUSTOM CSS FOR UI MATCHING ---
st.markdown("""
    <style>
    .main { background-color: #0E1116; color: #E5E7EB; }
    .stApp { background-color: #0E1116; }
    div[data-baseweb="tab-list"] { background-color: #0E1116; border-bottom: 1px solid #374151; }
    button[data-baseweb="tab"] { color: #9CA3AF !important; font-weight: bold !important; }
    button[aria-selected="true"] { color: #22C55E !important; border-bottom-color: #22C55E !important; }
    .input-card { background-color: #1A2233; padding: 20px; border-radius: 5px; border: 1px solid #374151; }
    .result-text { color: #22C55E; font-family: 'JetBrains Mono', monospace; font-weight: bold; }
    .quote-text { color: #22C55E; font-style: italic; font-size: 0.9em; }
    .stButton>button { background-color: #22C55E; color: white; width: 100%; border: none; }
    .stButton>button:hover { background-color: #16a34a; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA & QUOTES ---
sip_quotes = [
    "നിക്ഷേപം ഒരു ഒറ്റ തീരുമാനം അല്ല, ജീവിതകാല ശീലമാണ്.",
    "സമ്പത്ത് പെട്ടെന്ന് ഉണ്ടാകുന്നില്ല; സ്ഥിരതയോടെ വളരുന്നു.",
    "समय മാർക്കറ്റിൽ ഉണ്ടാകുന്നതാണ് ഏറ്റവും വലിയ ശക്തി.",
    "SIP ക്ഷമയെ സമ്പത്താക്കുന്ന സംവിധാനം ആണ്.",
    "ചെറിയ തുകയ്ക്കും ദീർഘകാലം വലിയ മൂല്യമുണ്ട്.",
    "നിക്ഷേപത്തിൽ വികാരങ്ങൾ കുറയുമ്പോൾ ഫലം വർധിക്കും.",
    "സ്ഥിരമായ നിക്ഷേപം അനിശ്ചിത ഭാവിയെ നിയന്ത്രിക്കും.",
    "വരുമാനം വർധിപ്പിക്കാതെ പോലും സമ്പത്ത് ഉണ്ടാക്കാം.",
    "നിക്ഷേപം ഭാവിയോട് ഉള്ള ഉത്തരവാദിത്വമാണ്.",
    "സാമ്പത്തിക വിജയത്തിന്റെ അടിസ്ഥാനം ഡിസിപ്ലിൻ ആണ്.",
    "മാർക്കറ്റ് ചാഞ്ചാട്ടം നിക്ഷേപത്തിന്റെ സ്വഭാവമാണ്.",
    "SIPയിൽ തുടർച്ച തന്നെയാണ് ഏറ്റവും വലിയ തന്ത്രം.",
    "സമ്പത്ത് ലക്ഷ്യമല്ല; സുരക്ഷയും സ്വാതന്ത്ര്യവുമാണ്.",
    "നിക്ഷേപം പഠിക്കുന്നത് നഷ്ടം ഒഴിവാക്കുന്നു.",
    "время തന്നെയാണ് ഏറ്റവും വിലയേറിയ ഇൻവെസ്റ്റ്മെന്റ്.",
    "നിക്ഷേപം ഭാഗ്യക്കളിയല്ല, ശാസ്ത്രീയ പ്രക്രിയയാണ്.",
    "ചെറിയ ശീലങ്ങൾ വലിയ സാമ്പത്തിക മാറ്റങ്ങൾ സൃഷ്ടിക്കും.",
    "SIP മാർക്കറ്റ് ഭയത്തെ നിയന്ത്രിക്കുന്നു.",
    "സ്ഥിരത ഇല്ലെങ്കിൽ കണക്കുകൾ അർത്ഥമില്ല.",
    "നിക്ഷേപം ജീവിതത്തെ ക്രമപ്പെടുത്തും.",
    "ഇന്ന് സംരക്ഷിച്ചത് നാളെയുടെ സ്വാതന്ത്ര്യം.",
    "മാർക്കറ്റിലെ ഉയർച്ചയും ഇടിവും താൽക്കാലികമാണ്.",
    "നിക്ഷേപം ക്ഷമ പഠിപ്പിക്കുന്ന ഗുരുവാണ്.",
    "SIP പണത്തെ ജോലി ചെയ്യിപ്പിക്കുന്നു.",
    "സ്ഥിരമായ നിക്ഷേപം മനസ്സിനും ശാന്തത നൽകും.",
    "വരുമാനത്തേക്കാൾ പ്രധാനമാണ് കൈകാര്യം ചെയ്യൽ.",
    "നിക്ഷേപം തീരുമാനിക്കുന്നതു മനസ്സുകൊണ്ട്, നടപ്പാക്കുന്നത് ശീലത്തിലൂടെയാണ്.",
    "സമ്പത്ത് വളരാൻ ശബ്ദം ആവശ്യമില്ല.",
    "SIP ഭാവിയിലേക്ക് നൽകുന്ന പ്രതിബദ്ധതയാണ്.",
    "നിക്ഷേപം ജീവിതത്തിന്റെ ബാക്കപ്പ് പ്ലാനാണ്.",
    "സാമ്പത്തിക അറിവ് അപകടസാധ്യത കുറയ്ക്കും.",
    "നിക്ഷേപം ദീർഘദൂര ഓട്ടമാണ്.",
    "മാർക്കറ്റ് താഴുമ്പോൾ SIP കൂടുതൽ ഫലപ്രദമാണ്.",
    "നിക്ഷേപം സ്വയം നിയന്ത്രണം പഠിപ്പിക്കും.",
    "പണം കിടക്കുമ്പോൾ മൂല്യം നഷ്ടപ്പെടും.",
    "SIP സ്ഥിരതയുള്ള വളർച്ചയുടെ വഴിയാണ്.",
    "നിക്ഷേപം ഭാവിയെ ഇപ്പോഴിൽ നിന്ന് നിർമ്മിക്കുന്നു.",
    "സാമ്പത്തിക സ്വാതന്ത്ര്യം ഭാഗ്യഫലം അല്ല.",
    "സ്ഥിരമായ പ്ലാൻ വിജയത്തിന്റെ അടയാളമാണ്.",
    "നിക്ഷേപം ആത്മവിശ്വാസം വളർത്തും.",
    "SIP ചെറുതായി തുടങ്ങി ശക്തമായി വളരും.",
    "സമ്പത്ത് തീരുമാനങ്ങളുടെ ഫലമാണ്.",
    "നിക്ഷേപത്തിൽ ഏറ്റവും വലിയ ശത്രു ഭയമാണ്.",
    "പണം സംരക്ഷിക്കുന്നത് സുരക്ഷ; നിക്ഷേപം വളർച്ച.",
    "നിക്ഷേപം ജീവിത ലക്ഷ്യങ്ങൾക്ക് ഇന്ധനം നൽകും.",
    "SIP സമയം കൊണ്ട് ശക്തിയാകും.",
    "സാമ്പത്തിക ഡിസിപ്ലിൻ ജീവിത ഡിസിപ്ലിനാണ്.",
    "നിക്ഷേപം ഒരു ശീലമാകണം, ഇടവേളയാകരുത്.",
    "സ്ഥിരതയുള്ള നിക്ഷേപം സമ്മർദ്ദം കുറക്കും.",
    "പണം നിങ്ങൾക്കായി ജോലി ചെയ്യണം.",
    "നിക്ഷേപം സ്വപ്നങ്ങൾക്ക് ദിശ നൽകും.",
    "SIP അനാവശ്യ തീരുമാനങ്ങൾ ഒഴിവാക്കുന്നു.",
    "സാമ്പത്തിക സുരക്ഷ ശമ്പളത്തിൽ മാത്രം നിന്നില്ല.",
    "നിക്ഷേപം ദീർഘകാല കാഴ്ചപ്പാട് നൽകും.",
    "സ്ഥിരമായ SIP വലിയ കണക്കുകൾ സൃഷ്ടിക്കും.",
    "നിക്ഷേപം ജീവിതത്തെ ലളിതമാക്കും.",
    "время നഷ്ടപ്പെട്ടാൽ തിриകെ കിട്ടില്ല.",
    "നിക്ഷേപം ഭാവിയുടെ അടിത്തറയാണ്.",
    "SIP സാമ്പത്തിക ശാന്തതയുടെ മാർഗമാണ്.",
    "പണം നിയന്ത്രിച്ചാൽ ജീവിതം നിയന്ത്രിക്കാം.",
    "നിക്ഷേപം പഠിക്കുന്നത് ചെലവല്ല.",
    "SIP വിപണിയിലെ ചാഞ്ചാട്ടം തുലയ്ക്കും.",
    "സാമ്പത്തിക സ്വാതന്ത്ര്യം ശീലങ്ങളുടെ ഫലമാണ്.",
    "നിക്ഷേപം ഇന്ന് കഷ്ടം, നാളെ ആശ്വാസം.",
    "സ്ഥിരത ഇല്ലെങ്കിൽ വിജയം ദൂരമാണ്.",
    "SIP പണത്തിന്റെ മൂല്യം സംരക്ഷിക്കും.",
    "നിക്ഷേപം ക്ഷമയുടെ പരീക്ഷയാണ്.",
    "സാമ്പത്തിക പ്ലാൻ ജീവിതത്തിന് ദിശ നൽകും.",
    "നിക്ഷേപം ശാന്തമായി വളരും.",
    "പണം തീരുമാനങ്ങളെ അനുസരിക്കുന്നു.",
    "SIP സ്വയം നിയന്ത്രണം വളർത്തും.",
    "നിക്ഷേപം ഭാവിക്ക് നൽകുന്ന സമ്മാനമാണ്.",
    "സാമ്പത്തിക വിജയം സ്ഥിരതയിൽ നിന്നാണ്.",
    "നിക്ഷേപം ഭാഗ്യത്തിൽ ആശ്രയിക്കില്ല.",
    "SIP ചെറുതായിട്ടാണ് ശക്തി തുടങ്ങുന്നത്.",
    "നിക്ഷേപം ഭാവിയുടെ സുരക്ഷയാണ്.",
    "സ്ഥിരമായ നിക്ഷേപം മനസ്സിന് ആശ്വാസം.",
    "പണം വളരാൻ സമയം വേണം.",
    "നിക്ഷേപം ജീവിതത്തിലെ അനിശ്ചിതത്വം കുറയ്ക്കും.",
    "SIP ദീർഘകാല ചിന്തയുടെ ഫലമാണ്.",
    "നിക്ഷേപം ലക്ഷ്യബോധം സൃഷ്ടിക്കും.",
    "സാമ്പത്തിക ഡിസിപ്ലിൻ സ്വാതന്ത്ര്യം നൽകും.",
    "SIP പണത്തിന് ദിശ നൽകും.",
    "നിക്ഷേപം ഇന്നത്തെ തീരുമാനമാണ്.",
    "സ്ഥിരതയാണ് സമ്പത്തിന്റെ ഭാഷ.",
    "നിക്ഷേപം ഭാവിയോട് ചെയ്യുന്ന കരാർ.",
    "SIP സമയത്തെ നിങ്ങളുടെ പക്ഷത്താക്കും.",
    "പണം വളരുന്നത് ശാന്തമായാണ്.",
    "നിക്ഷേപം ജീവിതത്തിന്റെ സുരക്ഷാവലയം.",
    "സ്ഥിരമായ ശീലങ്ങൾ വലിയ മാറ്റങ്ങൾ.",
    "SIP സാമ്പത്തിക ശാന്തതയുടെ അടിത്തറ.",
    "നിക്ഷേപം അറിവും ക്ഷമയും ആവശ്യപ്പെടുന്നു.",
    "സാമ്പത്തിക സ്വാതന്ത്ര്യം ഒരു യാത്രയാണ്.",
    "നിക്ഷേപം തീരുമാനങ്ങളുടെ തുടർച്ചയാണ്.",
    "SIP ഭാവിയിലേക്കുള്ള പ്രതിബദ്ധത.",
    "നിക്ഷേപം ജീവിത നിലവാരം ഉയർത്തും.",
    "время കൂടുമ്പോൾ SIP ശക്തമാകും.",
    "സാമ്പത്തിക പ്ലാൻ ഇല്ലെങ്കിൽ പണം വഴിതെറ്റും.",
    "നിക്ഷേപം സുരക്ഷയും വളർച്ചയും ഒരുമിച്ച്.",
    "സ്ഥിരതയുള്ള നിക്ഷേപം യഥാർത്ഥ സമ്പത്ത്.",
    "ഇപ്പോൾ തുടങ്ങുക!"
]

ins_quotes = [
    "Insurance is for protection; investment is for growth.",
    "Insurance covers risk, investment builds wealth.",
    "Mixing protection and growth weakens both goals.",
    "Insurance is a safety net, not a return generator.",
    "Investment needs confidence; insurance provides it.",
    "Expect returns from investments, not insurance.",
    "Insurance handles uncertainty; investment handles opportunity.",
    "Combining both increases cost and reduces efficiency.",
    "Insurance protects income; investment multiplies savings.",
    "Protection comes first, growth follows."
]

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #E5E7EB;'>FINANCIAL CALCULATORS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9CA3AF;'>Developed by SHAMSUDEEN ABDULLA</p>", unsafe_allow_html=True)

# --- TABS SETUP ---
tab_sip, tab_lumpsum, tab_cagr, tab_ins, tab_xirr, tab_rev_cagr = st.tabs([
    " SIP ", " LUMPSUM ", " CAGR ", " INSURANCE ", " XIRR PRO ", " REV CAGR "
])

# --- CALENDAR RANGE SETTINGS ---
min_date = date(1950, 1, 1)
max_date = date(2099, 12, 31)

# --- SIP TAB ---
with tab_sip:
    col1, space, col2 = st.columns([0.48, 0.04, 0.48])
    with col1:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.subheader("Target Goal (Target SIP)")
        t_amt = st.number_input("Target Goal (₹)", key="sip_t_amt", format="%0.2f")
        t_rate = st.number_input("Expected Return (%)", key="sip_t_rate")
        t_years = st.number_input("Time Period (Years)", key="sip_t_years", step=1)
        if st.button("Calculate Goal SIP"):
            try:
                annual_rate = t_rate / 100
                monthly_rate = (1 + annual_rate)**(1/12) - 1
                n = t_years * 12
                res = t_amt * (monthly_rate / (((1 + monthly_rate)**n - 1) * (1 + monthly_rate)))
                st.markdown(f'<h2 class="result-text">₹ {round(res):,}</h2>', unsafe_allow_html=True)
                st.markdown('<p style="color: #E5E7EB;">If you invest this amount in SIP for 20 years, you can achieve your goal.</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="quote-text">"{random.choice(sip_quotes)}"</p>', unsafe_allow_html=True)
            except: st.error("Check values")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.subheader("Wealth Generator (SIP)")
        w_amt = st.number_input("Monthly Investment (₹)", key="sip_w_amt")
        w_rate = st.number_input("Expected Return (%)", key="sip_w_rate")
        w_years = st.number_input("Time Period (Years)", key="sip_w_years", step=1)
        if st.button("Calculate Wealth"):
            try:
                annual_rate = w_rate / 100
                monthly_rate = (1 + annual_rate)**(1/12) - 1
                n = w_years * 12
                total = w_amt * (((1 + monthly_rate)**n - 1) / monthly_rate) * (1 + monthly_rate)
                invested = w_amt * n
                est_returns = total - invested
                st.markdown(f'<p style="color: #E5E7EB;">Invested Amount: ₹ {round(invested):,}</p>', unsafe_allow_html=True)
                st.markdown(f'<p style="color: #E5E7EB;">Estimated Returns: ₹ {round(est_returns):,}</p>', unsafe_allow_html=True)
                st.markdown(f'<h2 class="result-text">Total Wealth: ₹ {round(total):,}</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="quote-text">"{random.choice(sip_quotes)}"</p>', unsafe_allow_html=True)
            except: st.error("Check values")
        st.markdown('</div>', unsafe_allow_html=True)

# --- LUMPSUM TAB ---
with tab_lumpsum:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    l_p = st.number_input("Investment (₹)", key="l_p")
    l_r = st.number_input("Return (%)", key="l_r")
    l_n = st.number_input("Years", key="l_n")
    if st.button("Calculate Lumpsum"):
        fv = l_p * ((1 + l_r/100) ** l_n)
        invested_l = l_p
        returns_l = fv - l_p
        st.markdown(f'<p style="color: #E5E7EB;">Invested Amount: ₹ {round(invested_l):,}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #E5E7EB;">Estimated Returns: ₹ {round(returns_l):,}</p>', unsafe_allow_html=True)
        st.markdown(f'<h1 class="result-text" style="text-align:center;">Total Value: ₹ {round(fv):,}</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAGR TAB ---
with tab_cagr:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    c_i = st.number_input("Initial (₹)", key="c_i")
    c_f = st.number_input("Final (₹)", key="c_f")
    c_y = st.number_input("Years", key="c_y")
    if st.button("Calculate CAGR"):
        res = ((c_f / c_i) ** (1 / c_y) - 1) * 100
        st.markdown(f'<h1 class="result-text" style="text-align:center;">{res:.2f}%</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- INSURANCE TAB ---
with tab_ins:
    if 'ins_data' not in st.session_state: st.session_state.ins_data = []
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    i_amt = st.number_input("Amount (₹)", key="ins_amt")
    i_date = st.date_input("Select Date", key="ins_date", min_value=min_date, max_value=max_date)
    i_type = st.radio("Type", ["Premium", "Survival/MoneyBack", "Maturity Amount"], horizontal=True)
    if st.button("Add to List"):
        actual = -abs(i_amt) if i_type == "Premium" else abs(i_amt)
        st.session_state.ins_data.append({"Date": i_date, "Type": i_type, "Amount": actual})
        st.success("Added!")

    if st.session_state.ins_data:
        df = pd.DataFrame(st.session_state.ins_data)
        st.table(df)
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            if st.button("Calculate Result"):
                dates = [pd.to_datetime(d['Date']) for d in st.session_state.ins_data]
                amounts = [d['Amount'] for d in st.session_state.ins_data]
                try:
                    res = xirr(dates, amounts) * 100
                    st.markdown(f'<h3 class="result-text">Annual Return: {res:.2f}%</h3>', unsafe_allow_html=True)
                    st.markdown(f'<p class="quote-text">{random.choice(ins_quotes)}</p>', unsafe_allow_html=True)
                    if res < 6:
                        st.warning("ഇൻഫ്‌ളേഷൻ ബീറ്റ് ചെയ്യാത്ത റിട്ടേൺ ആണ്. നന്നായി പഠിച്ച ശേഷം നിക്ഷേപ തീരുമാനം എടുക്കുക")
                except: st.error("Error in data logic")
        with col_c2:
            if st.button("Clear Data"):
                st.session_state.ins_data = []
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- XIRR PRO TAB ---
with tab_xirr:
    st.error("⚠️ IMPORTANT: INVESTMENT as NEGATIVE (-10000), RETURNS as POSITIVE (25000)")
    if 'xirr_pro' not in st.session_state: 
        st.session_state.xirr_pro = [{"Date": date.today(), "Amount": 0.0} for _ in range(50)]
    for i in range(len(st.session_state.xirr_pro)):
        cols = st.columns([1, 2, 2])
        cols[0].write(f"{i+1}.")
        st.session_state.xirr_pro[i]["Date"] = cols[1].date_input(f"Date {i}", value=st.session_state.xirr_pro[i]["Date"], key=f"date_inp_{i}", label_visibility="collapsed", min_value=min_date, max_value=max_date)
        st.session_state.xirr_pro[i]["Amount"] = cols[2].number_input(f"Amt {i}", value=st.session_state.xirr_pro[i]["Amount"], key=f"amt_inp_{i}", label_visibility="collapsed")
    if st.button("Calculate XIRR PRO"):
        valid_data = [x for x in st.session_state.xirr_pro if x["Amount"] != 0]
        if len(valid_data) >= 2:
            try:
                dates = [pd.to_datetime(x["Date"]) for x in valid_data]
                amounts = [x["Amount"] for x in valid_data]
                res = xirr(dates, amounts) * 100
                st.markdown(f'<h2 class="result-text">XIRR: {res:.2f}%</h2>', unsafe_allow_html=True)
            except: st.error("Invalid calculation")

# --- REVERSE CAGR ---
with tab_rev_cagr:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    r_initial = st.number_input("Initial Amount (₹)", key="r_i")
    r_cagr = st.number_input("Expected CAGR (%)", key="r_c")
    r_years = st.number_input("Years", key="r_y", step=1)
    if st.button("Calculate Future Value"):
        res = r_initial * ((1 + r_cagr/100) ** r_years)
        st.markdown(f'<h1 class="result-text" style="text-align:center;">₹ {round(res):,}</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
