import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry, Calendar
from pyxirr import xirr
from datetime import datetime
from dateutil.relativedelta import relativedelta
import winsound
import random

class FinancialSuite:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Calculators Suite - Pro Edition")
        
        # Exact window size as requested
        self.root.geometry("1000x900") 
        
        # --- THEME COLORS ---
        self.bg_color = "#0E1116"      
        self.surface_color = "#1A2233" 
        self.accent_color = "#22C55E"  
        self.text_primary = "#E5E7EB"
        self.text_secondary = "#9CA3AF"
        self.error_color = "#EF4444"

        self.root.configure(bg=self.bg_color)

        self.sip_quotes = [
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
            "സമയം തന്നെയാണ് ഏറ്റവും വിലയേറിയ ഇൻവെസ്റ്റ്മെന്റ്.",
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
            "സമയം നഷ്ടപ്പെട്ടാൽ തിриകെ കിട്ടില്ല.",
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
            "സമയം കൂടുമ്പോൾ SIP ശക്തമാകും.",
            "സാമ്പത്തിക പ്ലാൻ ഇല്ലെങ്കിൽ പണം വഴിതെറ്റും.",
            "നിക്ഷേപം സുരക്ഷയും വളർച്ചയും ഒരുമിച്ച്.",
            "സ്ഥിരതയുള്ള നിക്ഷേപമാണ് യഥാർത്ഥ സമ്പത്ത്.",
            "ബജറ്റ് ഇല്ലാത്ത സാമ്പത്തിക ജീവിതം ദിശയറിയാത്ത കപ്പൽ പോലെയാണ്.",
            "നിങ്ങളുടെ ഓരോ ചെലവുകളെയും ട്രാക്ക് ചെയ്യുക.",
            "മറ്റുള്ളവരെ കാണിക്കാൻ കടം വാങ്ങി സാധനങ്ങൾ വാങ്ങരുത്.",
            "കടം ഒരു കെണിയാണ്, അതിൽ നിന്ന് എത്രയും വേഗം മോചിതനാകുക.",
            "ക്രെഡിറ്റ് കാർഡ് ഉപയോഗിക്കുമ്പോൾ സൂക്ഷിക്കുക.",
            "അത്യാവശ്യവും (Need) ആഗ്രഹവും (Want) തമ്മിലുള്ള വ്യത്യാസം അറിയുക.",
            "ആരോഗ്യ ഇൻഷുറൻസ് നിക്ഷേപമല്ല, അതൊരു സംരക്ഷണമാണ്.",
            "ലൈഫ് ഇൻഷുറൻസ് കുടുംബത്തിനുള്ള കരുതലാകണം.",
            "സാമ്പത്തിക സ്വാതന്ത്ര്യം എന്നത് ജോലി ഇല്ലാതെ ജീവിക്കാനുള്ള കരുത്താണ്.",
            "പണത്തെ നിയന്ത്രിക്കുക, അല്ലെങ്കിൽ പണം നിങ്ങളെ നിയന്ത്രിക്കും.",
            "ആഡംബരം എപ്പോഴും സമ്പന്നതയുടെ അടയാളമല്ല.",
            "ലാളിത്യമാണ് സാമ്പത്തിക വിജയത്തിന്റെ രഹസ്യം.",
            "ഓരോ മാസവും അക്കൗണ്ട് ബാലൻസ് പരിശോധിക്കുക.",
            "അനാവശ്യ സബ്സ്ക്രിപ്ഷനുകൾ ഒഴിവാക്കുക.",
            "വലിയ ചെലവുകൾക്ക് മുൻപ് 30 ദിവസം കാത്തിരിക്കുക.",
            "ഭക്ഷണത്തിനും വിനോദത്തിനുമുള്ള ചെലവുകളിൽ മിതത്വം പാലിക്കുക.",
            "കടം വാങ്ങി നിക്ഷേപിക്കരുത്.",
            "സാമ്പത്തിക തീരുമാനങ്ങളിൽ വികാരങ്ങൾ മാറ്റിവെക്കുക.",
            "സാമ്പത്തിക ലക്ഷ്യങ്ങൾ എഴുതി വെക്കുക.",
            "സാമ്പത്തിക സാക്ഷരത ജീവിതകാലം മുഴുവൻ നേടേണ്ട ഒന്നാണ്.",
            "സാധാരണക്കാരനെ സമ്പന്നനാക്കുന്ന മാന്ത്രിക വിദ്യയാണ് SIP.",
            "അച്ചടക്കമുള്ള നിക്ഷേപത്തിന്റെ പേരാണ് SIP.",
            "വിപണിയിലെ താഴ്ചകളിൽ കൂടുതൽ യൂണിറ്റുകൾ വാങ്ങാൻ SIP സഹായിക്കുന്നു.",
            "ചെറിയ തുകകൾ കൊണ്ട് വലിയ ലക്ഷ്യങ്ങൾ നേടാം.",
            "കോമ്പൗണ്ടിംഗിന്റെ ശക്തി (Power of Compounding) SIP വെളിപ്പെടുത്തുന്നു.",
            "സമയം നൽകിയാൽ ചെറിയ വിത്ത് വലിയ മരമാകും.",
            "വിപണിയിലെ കയറ്റിറക്കങ്ങളെ ഭയപ്പെടേണ്ട, ഉപയോഗപ്പെടുത്തുക.",
            "SIP ഒരു ശീലമാക്കുക, വികാരങ്ങൾക്ക് സ്ഥാനം നൽകരുത്.",
            "എത്ര നേരത്തെ തുടങ്ങുന്നുവോ അത്രയും വലിയ തുക ലഭിക്കും.",
            "ഓരോ വർഷവും SIP തുക വർദ്ധിപ്പിക്കുക (Step-up SIP).",
            "നിക്ഷേപത്തിന്റെ മൂല്യം കുറയുമ്പോൾ SIP നിർത്തരുത്.",
            "ദീർഘകാല ലക്ഷ്യങ്ങൾക്ക് ഇക്വിറ്റി മ്യൂച്ചൽ ഫണ്ടുകൾ മികച്ചതാണ്.",
            "ഇൻഡക്സ് ഫണ്ടുകൾ ചെലവ് കുറഞ്ഞ നിക്ഷേപ മാർഗ്ഗമാണ്.",
            "ഫണ്ട് മാനേജർ നിങ്ങളുടെ പണത്തിനായി കഠിനാധ്വാനം ചെയ്യുന്നു.",
            "കൃത്യമായ ലക്ഷ്യത്തോടെയുള്ള നിക്ഷേപം തുടങ്ങുക.",
            "വിരമിക്കൽ കാലത്തേക്ക് ഒരു വലിയ SIP ഇന്നുതന്നെ തുടങ്ങുക.",
            "കുട്ടികളുടെ വിദ്യാഭ്യാസത്തിനായി ഇന്നുതന്നെ നിക്ഷേപിച്ചു തുടങ്ങാം.",
            "നികുതി ലാഭിക്കാൻ ELSS ഫണ്ടുകൾ ഉപയോഗിക്കുക.",
            "പോർട്ട്‌ഫോളിയോ ഇടയ്ക്കിടെ പുനഃപരിശോധിക്കുക.",
            "ക്ഷമയാണ് SIP-യിലെ ഏറ്റവും വലിയ ലാഭം.",
            "സമ്പാദ്യം വരുമാനമല്ല, അത് ചെലവാക്കാത്ത പണമാണ്.",
            "പണം നിങ്ങൾക്കായി ജോലി ചെയ്യുന്ന രീതിയാണ് നിക്ഷേപം.",
            "നിക്ഷേപം തുടങ്ങാൻ ഏറ്റവും നല്ല സമയം ഇന്നലെയായിരുന്നു.",
            "രണ്ടാമത്തെ മികച്ച സമയം ഇപ്പോഴാണ്.",
            "പണപ്പെരുപ്പത്തെക്കാൾ വേഗത്തിൽ വളരുന്നതാകണം നിക്ഷേപം.",
            "സമ്പന്നനാകാൻ ഉറങ്ങുമ്പോഴും പണം വളരണം.",
            "വരുമാനത്തിൽ നിന്ന് നിക്ഷേപം കഴിഞ്ഞുള്ളത് മാത്രം ചെലവാക്കുക.",
            "അത്യാവശ്യത്തിനുള്ള പണം (Emergency Fund) ആദ്യം കരുതുക.",
            "നിക്ഷേപം ഒരു ഓട്ടമത്സരമല്ല, അതൊരു മാരത്തണാണ്.",
            "റിസ്ക് എടുക്കാതിരിക്കുന്നതാണ് ഏറ്റവും വലിയ റിസ്ക്.",
            "എല്ലാ മുട്ടകളും ഒരു കൊട്ടയിൽ ഇടരുത്.",
            "ലളിതമായ നിക്ഷേപങ്ങൾ പലപ്പോഴും മികച്ച ഫലം നൽകുന്നു.",
            "നിക്ഷേപത്തെക്കുറിച്ചുള്ള അറിവാണ് ഏറ്റവും വലിയ മൂലധനം.",
            "നിങ്ങളുടെ വരുമാന സ്രോതസ്സുകൾ വർദ്ധിപ്പിക്കുക.",
            "ദീർഘകാല നിക്ഷേപകർക്ക് വിപണിയിലെ ചാഞ്ചാട്ടം ഒരു അവസരമാണ്.",
            "സ്വർണ്ണം സുരക്ഷിതമാണ്, പക്ഷേ അത് സമ്പത്ത് സൃഷ്ടിക്കില്ല.",
            "റിയൽ എസ്റ്റേറ്റ് ക്ഷമയുള്ളവർക്കുള്ള നിക്ഷേപമാണ്.",
            "ഓഹരി വിപണി ക്ഷമയില്ലാത്തവരിൽ നിന്ന് ക്ഷമയുള്ളവരിലേക്ക് പണം മാറ്റുന്നു.",
            "ആസ്തികളും ബാധ്യതകളും തിരിച്ചറിയുക.",
            "പണം ഉണ്ടാക്കുന്ന ആസ്തികളെ (Assets) സ്വന്തമാക്കുക.",
            "\"വില നിങ്ങൾ നൽകുന്നതാണ്, മൂല്യം നിങ്ങൾക്ക് ലഭിക്കുന്നതാണ്.\" - വാറൻ ബഫറ്റ്.",
            "\"ഒരിക്കലും ഒരു വരുമാനത്തെ മാത്രം ആശ്രയിക്കരുത്.\" - വാറൻ ബഫറ്റ്.",
            "\"ഉറങ്ങുമ്പോൾ പണം സമ്പാദിക്കാൻ വഴി കണ്ടെത്തിയില്ലെങ്കിൽ, മരണം വരെ ജോലി ചെയ്യേണ്ടി വരും.\"",
            "\"കോമ്പൗണ്ട് ഇൻ്ററസ്റ്റ് ലോകത്തിലെ എട്ടാമത്തെ അത്ഭുതമാണ്.\" - ആൽബർട്ട് ഐൻസ്റ്റീൻ.",
            "\"നിക്ഷേപം കഴിഞ്ഞ ശേഷം ബാക്കിയുള്ളത് മാത്രം ചെലവാക്കുക.\"",
            "\"സമ്പന്നർ പണം നിക്ഷേപിക്കുന്നു, മറ്റുള്ളവർ ചെലവാക്കുന്നു.\" - ജിം റോൺ.",
            "\"പണം ഒരു നല്ല വേലക്കാരനാണ്, എന്നാൽ മോശം യജമാനനാണ്.\"",
            "\"വരുമാനത്തേക്കാൾ കുറഞ്ഞ ചെലവിൽ ജീവിക്കുക.\"",
            "\"അറിവിലുള്ള നിക്ഷേപം ഏറ്റവും മികച്ച പലിശ നൽകുന്നു.\" - ബെഞ്ചമിൻ ഫ്രാങ്ക്ലിൻ.",
            "\"റിസ്ക് വരുന്നത് നിങ്ങൾ എന്താണ് ചെയ്യുന്നതെന്ന് അറിയാത്തപ്പോഴാണ്.\"",
            "\"നിങ്ങളെത്തന്നെ വികസിപ്പിക്കുക, അതാണ് ഏറ്റവും മികച്ച നിക്ഷേപം.\"",
            "\"ഭാഗ്യമല്ല, തന്ത്രമാണ് നിങ്ങളെ സമ്പന്നനാക്കുന്നത്.\"",
            "\"പണത്തേക്കാൾ മൂല്യം സമയത്തിനുണ്ടെന്ന് മനസ്സിലാക്കുക.\"",
            "\"പരാജയങ്ങളെ ഭയപ്പെടരുത്, അവയിൽ നിന്ന് പഠിക്കുക.\"",
            "\"സ്ഥിരതയാണ് നിക്ഷേപത്തിലെ വിജയം.\"",
            "വരുമാനത്തിന്റെ കുറഞ്ഞത് 20% എങ്കിലും നിക്ഷേപിക്കുക.",
            "വീട് വാങ്ങുന്നത് വൈകിപ്പിക്കുന്നത് നിക്ഷേപത്തിന് കൂടുതൽ പണം നൽകും.",
            "കാർ വാങ്ങുമ്പോൾ ഉപയോഗം മാത്രം പരിഗണിക്കുക.",
            "പലിശ കൂടിയ ലോണുകൾ ആദ്യം തീർക്കുക.",
            "ഇൻഷുറൻസും നിക്ഷേപവും കൂട്ടിക്കുഴയ്ക്കരുത്.",
            "ടാക്സ് പ്ലാനിംഗ് വർഷാരംഭത്തിൽ തന്നെ തുടങ്ങുക.",
            "ബോണസുകളും അധിക വരുമാനവും നിക്ഷേപത്തിലേക്ക് മാറ്റുക.",
            "പണത്തെക്കുറിച്ച് മക്കളോട് സംസാരിക്കുക, അവരെ പഠിപ്പിക്കുക.",
            "തെറ്റായ നിക്ഷേപങ്ങളിൽ നിന്ന് വേഗത്തിൽ പുറത്തുകടക്കുക.",
            "മറ്റുള്ളവരുടെ ലാഭം കണ്ട് അന്ധമായി നിക്ഷേപിക്കരുത്.",
            "ഓരോ നിക്ഷേപത്തിനും ഒരു കാലാവധി നൽകുക.",
            "സാമ്പത്തിക ഉപദേഷ്ടാവിന്റെ സഹായം തേടാൻ മടിക്കരുത്.",
            "പണം കൈകാര്യം ചെയ്യുന്നത് ഒരു കലയാണ്.",
            "ഇന്നത്തെ ത്യാഗം നാളത്തെ സ്വാതന്ത്ര്യമാണ്.",
            "സമ്പത്ത് നിശബ്ദമായി വളരുന്ന ഒന്നാണ്.",
            "പ്രദർശിപ്പിക്കാനുള്ളതല്ല പണം, സുരക്ഷിതമായി ജീവിക്കാനുള്ളതാണ്.",
            "സന്തോഷം പണം കൊണ്ട് വാങ്ങാനാവില്ല, പക്ഷേ പണം സമാധാനം നൽകും.",
            "ഓരോ രൂപയും നിങ്ങളുടെ സാമ്പത്തിക സൈനികനാണ്.",
            "മടിയന്മാരല്ല, ദീർഘവീക്ഷ്യമുള്ളവരാണ് വിജയികൾ.",
            "അച്ചടക്കം പണത്തേക്കാൾ വലുതാണ്.",
            "സാമ്പത്തിക വിജയം പെട്ടെന്നുണ്ടാകുന്ന ഒന്നല്ല.",
            "സ്വപ്നം കാണുക, അതിനായി ആസൂത്രണം ചെയ്യുക.",
            "ഇപ്പോൾ തുടങ്ങുക!"
        ]

        self.ins_quotes = [
            "Insurance is for protection; investment is for growth.",
            "Insurance covers risk, investment builds wealth.",
            "Mixing protection and growth weakens both goals.",
            "Insurance is a safety net, not a return generator.",
            "Investment needs confidence; insurance provides it.",
            "Expect returns from investments, not insurance.",
            "Insurance handles uncertainty; investment handles opportunity.",
            "Combining both increases cost and reduces efficiency.",
            "Insurance protects income; investment multiplies savings.",
            "Protection comes first, growth follows.",
            "Insurance prevents financial loss; investment creates financial gain.",
            "One product cannot serve two opposite purposes well.",
            "Insurance secures your future; investment shapes it.",
            "Proper insurance allows disciplined investing.",
            "Insurance reduces risk; investment accepts it.",
            "Clear separation leads to better financial outcomes.",
            "Insurance is a shield; investment is a tool.",
            "Investment works best when risks are already covered.",
            "Insurance is a necessity; investment is a choice.",
            "Separate decisions create stronger personal finance."
        ]

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", font=("Inter", 11, "bold"), padding=[15, 8], 
                        background="#1F2937", foreground=self.text_secondary)
        style.map("TNotebook.Tab", background=[("selected", self.surface_color)], 
                  foreground=[("selected", self.accent_color)])
        
        header = tk.Frame(root, bg=self.bg_color, pady=20)
        header.pack(fill="x")
        tk.Label(header, text="FINANCIAL CALCULATORS", font=("Inter", 22, "bold"), 
                 fg=self.text_primary, bg=self.bg_color).pack()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=15, pady=5)

        self.tab_sip = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_lumpsum = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_cagr = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_insurance = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_xirr = tk.Frame(self.notebook, bg=self.bg_color)
        self.tab_reverse_cagr = tk.Frame(self.notebook, bg=self.bg_color)

        self.notebook.add(self.tab_sip, text=" SIP ")
        self.notebook.add(self.tab_lumpsum, text=" LUMPSUM ")
        self.notebook.add(self.tab_cagr, text=" CAGR ")
        self.notebook.add(self.tab_insurance, text=" INSURANCE ")
        self.notebook.add(self.tab_xirr, text=" XIRR PRO ")
        self.notebook.add(self.tab_reverse_cagr, text=" REV CAGR ")

        self.setup_sip_tab()
        self.setup_lumpsum_tab()
        self.setup_cagr_tab()
        self.setup_insurance_tab()
        self.setup_xirr_pro_tab() 
        self.setup_rev_cagr_tab()

    def play_type_sound(self, event=None):
        try:
            winsound.Beep(850, 15)
        except: pass

    def create_input_field(self, parent, label):
        tk.Label(parent, text=label, font=("Inter", 10), bg=self.surface_color, fg=self.text_secondary).pack(anchor="w", pady=(10, 2))
        entry = tk.Entry(parent, font=("JetBrains Mono", 14), bg="#121826", fg=self.text_primary, 
                         insertbackground=self.accent_color, borderwidth=0, highlightthickness=1, 
                         highlightbackground="#374151", highlightcolor=self.accent_color)
        entry.pack(fill="x", pady=(0, 10), ipady=8)
        entry.bind("<Key>", self.play_type_sound)
        return entry

    def setup_sip_tab(self):
        container = tk.Frame(self.tab_sip, bg=self.bg_color, padx=20, pady=10)
        container.pack(fill="both", expand=True)
        cards_frame = tk.Frame(container, bg=self.bg_color)
        cards_frame.pack(fill="both", expand=True)
        
        l_card = tk.Frame(cards_frame, bg=self.surface_color, padx=20, pady=20, highlightbackground="#374151", highlightthickness=1)
        l_card.place(relx=0, rely=0, relwidth=0.48, relheight=0.8)
        self.goal_amt = self.create_input_field(l_card, "Target Goal (₹)")
        
        tk.Label(l_card, text="Start Date:", font=("Inter", 10), bg=self.surface_color, fg=self.text_secondary).pack(anchor="w")
        self.goal_date_ent = DateEntry(l_card, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.goal_date_ent.pack(fill="x", pady=(0, 10))

        self.goal_rate = self.create_input_field(l_card, "Expected Return (%)")
        self.goal_years = self.create_input_field(l_card, "Time Period (Years)")
        
        btn_f = tk.Frame(l_card, bg=self.surface_color)
        btn_f.pack(fill="x", pady=15)
        tk.Button(btn_f, text="Calculate", command=self.calc_goal_sip, bg=self.accent_color, fg="white", font=("Inter", 11, "bold"), pady=8).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_f, text="Reset", command=lambda: self.reset_fields([self.goal_amt, self.goal_rate, self.goal_years], self.goal_res, self.goal_quote), bg="#4B5563", fg="white", font=("Inter", 11, "bold"), pady=8).pack(side="left", expand=True, fill="x", padx=2)

        self.goal_res = tk.Label(l_card, text="", font=("JetBrains Mono", 22, "bold"), bg=self.surface_color, fg=self.accent_color)
        self.goal_res.pack()
        self.goal_quote = tk.Label(l_card, text="", font=("Inter", 10, "italic"), bg=self.surface_color, fg=self.accent_color, wraplength=400)
        self.goal_quote.pack(pady=10)

        r_card = tk.Frame(cards_frame, bg=self.surface_color, padx=20, pady=20, highlightbackground="#374151", highlightthickness=1)
        r_card.place(relx=0.52, rely=0, relwidth=0.48, relheight=0.8)
        self.sip_amt = self.create_input_field(r_card, "Monthly Investment (₹)")
        
        tk.Label(r_card, text="Start Date:", font=("Inter", 10), bg=self.surface_color, fg=self.text_secondary).pack(anchor="w")
        self.sip_date_ent = DateEntry(r_card, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.sip_date_ent.pack(fill="x", pady=(0, 10))

        self.sip_rate = self.create_input_field(r_card, "Expected Return (%)")
        self.sip_years = self.create_input_field(r_card, "Time Period (Years)")
        
        btn_f2 = tk.Frame(r_card, bg=self.surface_color)
        btn_f2.pack(fill="x", pady=15)
        tk.Button(btn_f2, text="Calculate", command=self.calc_wealth_sip, bg=self.accent_color, fg="white", font=("Inter", 11, "bold"), pady=8).pack(side="left", expand=True, fill="x", padx=2)
        tk.Button(btn_f2, text="Reset", command=lambda: self.reset_fields([self.sip_amt, self.sip_rate, self.sip_years], self.wealth_res, self.wealth_quote), bg="#4B5563", fg="white", font=("Inter", 11, "bold"), pady=8).pack(side="left", expand=True, fill="x", padx=2)

        self.wealth_res = tk.Label(r_card, text="", font=("JetBrains Mono", 18, "bold"), bg=self.surface_color, fg=self.text_primary)
        self.wealth_res.pack()
        self.wealth_quote = tk.Label(r_card, text="", font=("Inter", 10, "italic"), bg=self.surface_color, fg=self.accent_color, wraplength=400)
        self.wealth_quote.pack(pady=10)

    def reset_fields(self, entries, res_label, quote_label=None):
        for e in entries: e.delete(0, tk.END)
        res_label.config(text="")
        if quote_label: quote_label.config(text="")

    def calc_goal_sip(self):
        try:
            target = float(self.goal_amt.get())
            annual_rate = float(self.goal_rate.get()) / 100
            years = int(self.goal_years.get())
            monthly_rate = (1 + annual_rate)**(1/12) - 1
            n = years * 12
            res = target * (monthly_rate / (((1 + monthly_rate)**n - 1) * (1 + monthly_rate)))
            self.goal_res.config(text=f"₹{round(res):,}")
            self.goal_quote.config(text=f"\"{random.choice(self.sip_quotes)}\"")
        except: messagebox.showerror("Error", "Check values")

    def calc_wealth_sip(self):
        try:
            p = float(self.sip_amt.get())
            annual_rate = float(self.sip_rate.get()) / 100
            years = int(self.sip_years.get())
            monthly_rate = (1 + annual_rate)**(1/12) - 1
            n = years * 12
            total = p * (((1 + monthly_rate)**n - 1) / monthly_rate) * (1 + monthly_rate)
            self.wealth_res.config(text=f"Wealth: ₹{round(total):,}")
            self.wealth_quote.config(text=f"\"{random.choice(self.sip_quotes)}\"")
        except: messagebox.showerror("Error", "Check values")

    def setup_lumpsum_tab(self):
        container = tk.Frame(self.tab_lumpsum, bg=self.bg_color, padx=30, pady=30)
        container.pack(fill="both", expand=True)
        card = tk.Frame(container, bg=self.surface_color, padx=25, pady=25, highlightbackground="#374151", highlightthickness=1)
        card.pack(fill="x")
        self.lump_p = self.create_input_field(card, "Investment (₹)")
        self.lump_r = self.create_input_field(card, "Return (%)")
        self.lump_n = self.create_input_field(card, "Years")
        
        btn_f = tk.Frame(card, bg=self.surface_color)
        btn_f.pack(fill="x", pady=20)
        tk.Button(btn_f, text="Calculate", command=self.calc_lumpsum, bg=self.accent_color, fg="white", font=("Inter", 12, "bold"), pady=12).pack(side="left", expand=True, fill="x", padx=5)
        tk.Button(btn_f, text="Reset", command=lambda: self.reset_fields([self.lump_p, self.lump_r, self.lump_n], self.lump_res), bg="#4B5563", fg="white", font=("Inter", 12, "bold"), pady=12).pack(side="left", expand=True, fill="x", padx=5)
        
        self.lump_res = tk.Label(container, text="₹ 0", font=("JetBrains Mono", 36, "bold"), bg=self.bg_color, fg=self.accent_color)
        self.lump_res.pack()

    def calc_lumpsum(self):
        try:
            p = float(self.lump_p.get()); r = float(self.lump_r.get())/100; n = float(self.lump_n.get())
            fv = p * ((1 + r) ** n); self.lump_res.config(text=f"₹{round(fv):,}")
        except: messagebox.showerror("Error", "Check values")

    def setup_cagr_tab(self):
        container = tk.Frame(self.tab_cagr, bg=self.bg_color, padx=30, pady=30)
        container.pack(fill="both", expand=True)
        card = tk.Frame(container, bg=self.surface_color, padx=25, pady=25, highlightbackground="#374151", highlightthickness=1)
        card.pack(fill="x")
        self.cagr_initial = self.create_input_field(card, "Initial (₹)")
        self.cagr_final = self.create_input_field(card, "Final (₹)")
        self.cagr_years = self.create_input_field(card, "Years")
        
        btn_f = tk.Frame(card, bg=self.surface_color)
        btn_f.pack(fill="x", pady=20)
        tk.Button(btn_f, text="Calculate", command=self.calc_cagr, bg=self.accent_color, fg="white", font=("Inter", 12, "bold"), pady=12).pack(side="left", expand=True, fill="x", padx=5)
        tk.Button(btn_f, text="Reset", command=lambda: self.reset_fields([self.cagr_initial, self.cagr_final, self.cagr_years], self.cagr_res), bg="#4B5563", fg="white", font=("Inter", 12, "bold"), pady=12).pack(side="left", expand=True, fill="x", padx=5)

        self.cagr_res = tk.Label(container, text="CAGR: --%", font=("JetBrains Mono", 32, "bold"), bg=self.bg_color, fg=self.accent_color)
        self.cagr_res.pack()

    def calc_cagr(self):
        try:
            i = float(self.cagr_initial.get()); f = float(self.cagr_final.get()); y = float(self.cagr_years.get())
            res = ((f / i) ** (1 / y) - 1) * 100; self.cagr_res.config(text=f"{res:.2f}%")
        except: messagebox.showerror("Error", "Check values")

    def setup_insurance_tab(self):
        self.ins_flows = []
        container = tk.Frame(self.tab_insurance, bg=self.bg_color, padx=20, pady=20)
        container.pack(fill="both", expand=True)
        input_card = tk.Frame(container, bg=self.surface_color, padx=20, pady=20, highlightbackground="#374151", highlightthickness=1)
        input_card.pack(fill="x")
        self.ins_amt = self.create_input_field(input_card, "Amount (₹)")
        tk.Label(input_card, text="Select Date:", bg=self.surface_color, fg=self.text_secondary).pack(anchor="w")
        self.ins_date = DateEntry(input_card, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        self.ins_date.pack(fill="x", pady=5)
        self.ins_type_var = tk.StringVar(value="Premium")
        radio_frame = tk.Frame(input_card, bg=self.surface_color)
        radio_frame.pack(fill="x", pady=10)
        tk.Radiobutton(radio_frame, text="Insurance Premium", variable=self.ins_type_var, value="Premium", bg=self.surface_color, fg="white", selectcolor="#000").pack(side="left", padx=5)
        tk.Radiobutton(radio_frame, text="Survival/MoneyBack", variable=self.ins_type_var, value="Survival", bg=self.surface_color, fg="white", selectcolor="#000").pack(side="left", padx=5)
        tk.Radiobutton(radio_frame, text="Maturity Amount", variable=self.ins_type_var, value="Maturity", bg=self.surface_color, fg="white", selectcolor="#000").pack(side="left", padx=5)
        tk.Button(input_card, text="Add to List", command=self.add_ins_flow, bg="#27ae60", fg="white", font=("bold"), pady=8).pack(fill="x", pady=10)
        
        self.ins_tree = ttk.Treeview(container, columns=("Date", "Type", "Amount"), show='headings', height=6)
        self.ins_tree.heading("Date", text="Date")
        self.ins_tree.heading("Type", text="Entry Type")
        self.ins_tree.heading("Amount", text="Amount (₹)")
        self.ins_tree.pack(fill="x", pady=15)
        
        self.ins_quote_lbl = tk.Label(container, text="", font=("Inter", 11, "italic"), bg=self.bg_color, fg=self.text_secondary, wraplength=800)
        self.ins_quote_lbl.pack(pady=5)

        self.ins_res_lbl = tk.Label(container, text="Annual Return: --%", font=("JetBrains Mono", 18, "bold"), bg=self.bg_color, fg=self.accent_color)
        self.ins_res_lbl.pack(pady=5)
        btn_frame = tk.Frame(container, bg=self.bg_color)
        btn_frame.pack(fill="x")
        tk.Button(btn_frame, text="Calculate Result", command=self.calc_ins_xirr, bg="#2980b9", fg="white", font=("bold"), pady=10).pack(side="left", expand=True, fill="x", padx=5)
        tk.Button(btn_frame, text="Reset / Clear", command=self.clear_ins_data, bg="#e67e22", fg="white", font=("bold"), pady=10).pack(side="left", expand=True, fill="x", padx=5)

    def add_ins_flow(self):
        try:
            amt = float(self.ins_amt.get()); dt = self.ins_date.get_date(); etype = self.ins_type_var.get()
            actual = -abs(amt) if etype == "Premium" else abs(amt)
            d_type = "Insurance Premium" if etype == "Premium" else ("Survival Benefit" if etype == "Survival" else "Maturity Amount")
            self.ins_flows.append((dt, actual))
            self.ins_tree.insert("", "end", values=(dt.strftime('%d/%m/%Y'), d_type, f"{amt:,.2f}"))
            self.ins_amt.delete(0, tk.END)
        except: messagebox.showerror("Error", "Valid number required")

    def calc_ins_xirr(self):
        if len(self.ins_flows) < 2: return
        try:
            dates = [f[0] for f in self.ins_flows]; amounts = [f[1] for f in self.ins_flows]
            result = xirr(dates, amounts)
            if result is not None:
                p = result * 100
                self.ins_res_lbl.config(text=f"Annual Return: {p:.2f}%")
                self.ins_quote_lbl.config(text=random.choice(self.ins_quotes))
                if p < 6:
                    messagebox.showwarning("Inflation Warning", "ഇൻഫ്‌ളേഷൻ ബീറ്റ് ചെയ്യാത്ത റിട്ടേൺ ആണ് നന്നായി പഠിച്ച ശേഷം നിക്ഷേപ തീരുമാനം എടുക്കുക")
        except: messagebox.showerror("Error", "Check data logic")

    def clear_ins_data(self):
        self.ins_flows = []; self.ins_tree.delete(*self.ins_tree.get_children())
        self.ins_res_lbl.config(text="Annual Return: --%")
        self.ins_quote_lbl.config(text="")

    def setup_xirr_pro_tab(self):
        container = tk.Frame(self.tab_xirr, bg=self.bg_color, padx=15, pady=10)
        container.pack(fill="both", expand=True)
        
        note_frame = tk.LabelFrame(container, text=" ⚠️ IMPORTANT NOTE ", font=("Arial", 10, "bold"), fg=self.error_color, bg="#1E293B", padx=10, pady=10, bd=1)
        note_frame.pack(fill="x", padx=5, pady=10)
        note_text = "• INVESTMENT: Enter as NEGATIVE value (e.g., -10000)\n• RETURNS / VALUE: Enter as POSITIVE value (e.g., 25000)"
        tk.Label(note_frame, text=note_text, font=("Arial", 9, "bold"), bg="#1E293B", fg=self.error_color, justify="left").pack()
        
        lbl_frame = tk.Frame(container, bg=self.bg_color)
        lbl_frame.pack(fill="x", padx=10, pady=(5,0))
        tk.Label(lbl_frame, text="Date (Click box)", font=("Arial", 10, "bold"), bg=self.bg_color, fg=self.text_secondary).pack(side="left", padx=40)
        
        tk.Button(lbl_frame, text="Reset All Rows", command=self.reset_xirr_pro, bg="#EF4444", fg="white", font=("Arial", 8, "bold")).pack(side="right", padx=10)
        tk.Label(lbl_frame, text="Amount (INR)", font=("Arial", 10, "bold"), bg=self.bg_color, fg=self.text_secondary).pack(side="right", padx=20)
        
        scroll_container = tk.Frame(container, bg=self.bg_color)
        scroll_container.pack(fill="both", expand=True, pady=5)
        canvas = tk.Canvas(scroll_container, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
        self.x_scroll_frame = tk.Frame(canvas, bg=self.bg_color)
        self.x_scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.x_scroll_frame, anchor="nw", width=950)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.x_rows = []
        for i in range(50):
            row_frame = tk.Frame(self.x_scroll_frame, bg=self.bg_color, pady=3)
            row_frame.pack(fill="x")
            tk.Label(row_frame, text=f"{i+1}.", width=4, bg=self.bg_color, fg="#555").pack(side="left")
            d_ent = tk.Entry(row_frame, width=18, font=("JetBrains Mono", 11), bg="#121826", fg="white", justify="center", insertbackground=self.accent_color)
            d_ent.pack(side="left", padx=20); d_ent.bind("<Button-1>", lambda e, ent=d_ent: self.pop_cal_pro(e, ent))
            a_ent = tk.Entry(row_frame, width=25, font=("JetBrains Mono", 11), bg="#121826", fg="white", justify="right", insertbackground=self.accent_color)
            a_ent.pack(side="right", padx=20); a_ent.bind("<KeyRelease>", lambda e: self.calc_xirr_pro()); a_ent.bind("<Key>", self.play_type_sound)
            self.x_rows.append({'date': d_ent, 'amount': a_ent})

        footer = tk.Frame(container, bg=self.surface_color, pady=10)
        footer.pack(fill="x")
        self.xirr_pro_res = tk.Label(footer, text="XIRR: --%", font=("JetBrains Mono", 24, "bold"), bg=self.surface_color, fg=self.accent_color)
        self.xirr_pro_res.pack()

    def pop_cal_pro(self, event, entry):
        top = tk.Toplevel(self.root)
        top.geometry("+%d+%d" % (event.x_root, event.y_root))
        cal = Calendar(top, selectmode='day', date_pattern='dd/mm/yyyy')
        cal.pack()
        def set_date():
            entry.delete(0, tk.END)
            entry.insert(0, cal.get_date())
            top.destroy()
            self.calc_xirr_pro()
        tk.Button(top, text="OK", command=set_date).pack()

    def calc_xirr_pro(self):
        dates = []; amounts = []
        for row in self.x_rows:
            d_str = row['date'].get(); a_str = row['amount'].get()
            if d_str and a_str:
                try:
                    dates.append(datetime.strptime(d_str, "%d/%m/%Y"))
                    amounts.append(float(a_str))
                except: pass
        if len(dates) >= 2:
            try:
                res = xirr(dates, amounts)
                if res: self.xirr_pro_res.config(text=f"XIRR: {res*100:.2f}%")
            except: self.xirr_pro_res.config(text="XIRR: Error")
        else: self.xirr_pro_res.config(text="XIRR: --%")

    def reset_xirr_pro(self):
        for row in self.x_rows:
            row['date'].delete(0, tk.END)
            row['amount'].delete(0, tk.END)
        self.xirr_pro_res.config(text="XIRR: --%")

    def setup_rev_cagr_tab(self):
        container = tk.Frame(self.tab_reverse_cagr, bg=self.bg_color, padx=30, pady=30)
        container.pack(fill="both", expand=True)
        card = tk.Frame(container, bg=self.surface_color, padx=25, pady=25, highlightbackground="#374151", highlightthickness=1)
        card.pack(fill="x")
        self.rev_initial = self.create_input_field(card, "Initial Amount (₹)")
        self.rev_cagr = self.create_input_field(card, "CAGR (%)")
        self.rev_years = self.create_input_field(card, "Years")
        btn_f = tk.Frame(card, bg=self.surface_color)
        btn_f.pack(fill="x", pady=20)
        tk.Button(btn_f, text="Calculate", command=self.calc_rev_cagr, bg=self.accent_color, fg="white", font=("Inter", 12, "bold"), pady=12).pack(side="left", expand=True, fill="x", padx=5)
        self.rev_res = tk.Label(container, text="Final: ₹ 0", font=("JetBrains Mono", 32, "bold"), bg=self.bg_color, fg=self.accent_color)
        self.rev_res.pack(pady=20)

    def calc_rev_cagr(self):
        try:
            p = float(self.rev_initial.get()); r = float(self.rev_cagr.get())/100; y = float(self.rev_years.get())
            fv = p * ((1 + r) ** y)
            self.rev_res.config(text=f"Final: ₹{round(fv):,}")
        except: messagebox.showerror("Error", "Check values")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialSuite(root)
    root.mainloop()