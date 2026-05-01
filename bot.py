from botbuilder.core import ActivityHandler, TurnContext, MessageFactory, ConversationState

# Baza proizvoda - više po kategoriji
PROIZVODI = {
    "laptop": {
        "ured": {
            "nizak": [
                {"naziv": "Lenovo IdeaPad 3", "cijena": "~400€", "opis": "Solidan za uredski rad, AMD Ryzen 5, 8GB RAM, 256GB SSD"},
                {"naziv": "Acer Aspire 5", "cijena": "~450€", "opis": "Pouzdana opcija, Intel i5, 8GB RAM, 512GB SSD"},
            ],
            "srednji": [
                {"naziv": "HP EliteBook 640", "cijena": "~700€", "opis": "Poslovni laptop, Intel i5, 16GB RAM, 512GB SSD"},
                {"naziv": "Lenovo ThinkPad E14", "cijena": "~750€", "opis": "Klasik za ured, odlična tipkovnica, 16GB RAM"},
            ],
            "visi": [
                {"naziv": "Dell Latitude 5540", "cijena": "~1200€", "opis": "Premium poslovni, Intel i7, 16GB RAM, 512GB SSD"},
                {"naziv": "HP EliteBook 840", "cijena": "~1250€", "opis": "Lagani poslovni, Intel i7, 16GB RAM, odlična baterija"},
            ],
            "visok": [
                {"naziv": "Lenovo ThinkPad X1 Carbon", "cijena": "~1800€", "opis": "Vrhunski poslovni, Intel i7, 32GB RAM, ultra lagan"},
                {"naziv": "Dell XPS 13", "cijena": "~1700€", "opis": "Kompaktni premium, Intel i7, 16GB RAM, OLED zaslon"},
            ],
        },
        "gaming": {
            "nizak": [
                {"naziv": "Acer Nitro 5", "cijena": "~650€", "opis": "Ulazni gaming, AMD Ryzen 5, RTX 3050, 8GB RAM"},
                {"naziv": "Lenovo IdeaPad Gaming 3", "cijena": "~600€", "opis": "Pristupačan gaming, Ryzen 5, RTX 3050, 144Hz"},
            ],
            "srednji": [
                {"naziv": "ASUS TUF Gaming A15", "cijena": "~800€", "opis": "Odličan omjer cijene i performansi, RTX 4060, 16GB RAM"},
                {"naziv": "MSI Thin GF63", "cijena": "~850€", "opis": "Tanak gaming, Intel i7, RTX 4060, 144Hz"},
            ],
            "visi": [
                {"naziv": "Lenovo Legion 5 Pro", "cijena": "~1300€", "opis": "Vrhunske gaming performanse, RTX 4070, 165Hz, 32GB RAM"},
                {"naziv": "ASUS ROG Strix G16", "cijena": "~1350€", "opis": "Gaming zvijer, RTX 4070, 240Hz, 16GB RAM"},
            ],
            "visok": [
                {"naziv": "ASUS ROG Zephyrus G16", "cijena": "~2000€+", "opis": "Top gaming, RTX 4080, OLED 240Hz, 32GB RAM"},
                {"naziv": "Razer Blade 16", "cijena": "~2500€+", "opis": "Premium gaming dizajn, RTX 4090, 240Hz"},
            ],
        },
        "programiranje": {
            "nizak": [
                {"naziv": "Lenovo IdeaPad 5", "cijena": "~500€", "opis": "Solidan za početnike, Ryzen 5, 16GB RAM, 512GB SSD"},
                {"naziv": "Acer Aspire 5", "cijena": "~480€", "opis": "Intel i5, 16GB RAM, dobra za Python/web dev"},
            ],
            "srednji": [
                {"naziv": "Apple MacBook Air M2", "cijena": "~1100€", "opis": "Idealan za razvoj softvera, nevjerojatna baterija, ARM chip"},
                {"naziv": "ASUS Zenbook 14", "cijena": "~950€", "opis": "Kompaktan, Intel i7, 16GB RAM, OLED zaslon"},
            ],
            "visi": [
                {"naziv": "Dell XPS 15", "cijena": "~1400€", "opis": "Moćan za programiranje i multitasking, Intel i7, 32GB RAM"},
                {"naziv": "Apple MacBook Pro M3", "cijena": "~1600€", "opis": "Profesionalni razvoj, M3 chip, 18GB RAM, odlična optimizacija"},
            ],
            "visok": [
                {"naziv": "Apple MacBook Pro M3 Max", "cijena": "~2500€+", "opis": "Za profesionalce, M3 Max, 36GB RAM, nevjerojatne performanse"},
                {"naziv": "Dell XPS 17", "cijena": "~2000€", "opis": "Veliki zaslon za multitasking, Intel i9, 32GB RAM"},
            ],
        },
        "dizajn": {
            "srednji": [
                {"naziv": "Apple MacBook Air M2", "cijena": "~1100€", "opis": "Odličan za grafički dizajn, M2 chip, True Tone zaslon"},
                {"naziv": "ASUS ProArt Studiobook 16", "cijena": "~1200€", "opis": "OLED zaslon, Intel i7, RTX 4060, kalibrirane boje"},
            ],
            "visi": [
                {"naziv": "Apple MacBook Pro M3", "cijena": "~1600€", "opis": "Standard za kreativce, M3 chip, Liquid Retina zaslon"},
                {"naziv": "Dell XPS 15 OLED", "cijena": "~1500€", "opis": "OLED 3.5K zaslon, Intel i7, RTX 4060, za Photoshop/Premiere"},
            ],
            "visok": [
                {"naziv": "ASUS ProArt Studiobook Pro", "cijena": "~2500€", "opis": "Profesionalni dizajn, RTX 4080, OLED, Pantone validacija"},
                {"naziv": "Apple MacBook Pro M3 Max", "cijena": "~2800€+", "opis": "Vrhunac za video i motion graphics, M3 Max, 36GB RAM"},
            ],
        },
    },
    "router": {
        "mali_prostor": {
            "nizak": [
                {"naziv": "TP-Link Archer A6", "cijena": "~35€", "opis": "WiFi 5, AC1200, dovoljan za stan do 60m²"},
                {"naziv": "D-Link DIR-842", "cijena": "~40€", "opis": "WiFi 5, AC1200, dual-band, lako postavljanje"},
            ],
            "srednji": [
                {"naziv": "ASUS RT-AX55", "cijena": "~70€", "opis": "WiFi 6, AX1800, odlična pokrivenost za stan"},
                {"naziv": "TP-Link Archer AX23", "cijena": "~65€", "opis": "WiFi 6, AX1800, brz i stabilan"},
            ],
            "visi": [
                {"naziv": "ASUS RT-AX86U", "cijena": "~180€", "opis": "WiFi 6, AX5700, gaming optimizacija, odličan za stan"},
                {"naziv": "TP-Link Archer AX73", "cijena": "~150€", "opis": "WiFi 6, AX5400, 6 antena, široka pokrivenost"},
            ],
        },
        "velika_kuca": {
            "srednji": [
                {"naziv": "TP-Link Deco M4 (2-pack)", "cijena": "~100€", "opis": "Mesh sustav, WiFi 5, do 260m² pokrivenosti"},
                {"naziv": "D-Link COVR-1102", "cijena": "~110€", "opis": "Mesh WiFi 5, elegantni dizajn, do 250m²"},
            ],
            "visi": [
                {"naziv": "ASUS ZenWiFi AX (2-pack)", "cijena": "~200€", "opis": "Mesh WiFi 6, do 370m², odlične performanse"},
                {"naziv": "TP-Link Deco XE75 (2-pack)", "cijena": "~220€", "opis": "Mesh WiFi 6E, trifrekventni, do 400m²"},
            ],
        },
        "ured": {
            "srednji": [
                {"naziv": "TP-Link Archer AX55", "cijena": "~100€", "opis": "WiFi 6, AX3000, dobar za manji ured"},
                {"naziv": "ASUS RT-AX68U", "cijena": "~120€", "opis": "WiFi 6, AX2700, pouzdan za ured"},
            ],
            "visi": [
                {"naziv": "Ubiquiti UniFi AP", "cijena": "~180€", "opis": "Profesionalno rješenje, centralno upravljanje"},
                {"naziv": "Cisco Meraki MR36", "cijena": "~300€", "opis": "Enterprise WiFi 6, cloud upravljanje, idealno za ured"},
            ],
        },
    },
    "periferija": {
        "mis": {
            "nizak": [
                {"naziv": "Logitech B100", "cijena": "~10€", "opis": "Pouzdan žičani miš, plug & play"},
                {"naziv": "HP X1000", "cijena": "~12€", "opis": "Ergonomski žičani miš, USB"},
            ],
            "srednji": [
                {"naziv": "Logitech MX Master 3", "cijena": "~80€", "opis": "Premium bežični, MagSpeed kotačić, 70 dana baterije"},
                {"naziv": "Razer DeathAdder V3", "cijena": "~70€", "opis": "Gaming miš, 30000 DPI, ultra lagan"},
            ],
            "visi": [
                {"naziv": "Logitech MX Master 3S", "cijena": "~110€", "opis": "Tihi klikovi, 8000 DPI, Multi-Device"},
                {"naziv": "Apple Magic Mouse", "cijena": "~85€", "opis": "Za Mac korisnike, Multi-Touch površina"},
            ],
        },
        "tipkovnica": {
            "nizak": [
                {"naziv": "Logitech K120", "cijena": "~20€", "opis": "Jednostavna žičana, tiha, HR layout"},
                {"naziv": "HP 125", "cijena": "~18€", "opis": "Kompaktna žičana tipkovnica, USB"},
            ],
            "srednji": [
                {"naziv": "Keychron K2", "cijena": "~90€", "opis": "Mehanička, bežična, kompaktna 75%, višeplatformska"},
                {"naziv": "Logitech MX Keys", "cijena": "~100€", "opis": "Tiha, bežična, backlit, idealna za ured"},
            ],
            "visi": [
                {"naziv": "Keychron Q3", "cijena": "~150€", "opis": "Mehanička premium, aluminijsko kućište, QMK"},
                {"naziv": "Logitech MX Mechanical", "cijena": "~130€", "opis": "Mehanička, bežična, Tactile Quiet switches"},
            ],
        },
        "monitor": {
            "srednji": [
                {"naziv": "LG 24MK430H", "cijena": "~150€", "opis": "24\", Full HD, IPS, AMD FreeSync"},
                {"naziv": "ASUS VA24EHE", "cijena": "~130€", "opis": "24\", Full HD, 75Hz, Eye Care"},
            ],
            "visi": [
                {"naziv": "Dell U2722D", "cijena": "~400€", "opis": "27\", 4K, IPS, USB-C, profesionalni"},
                {"naziv": "LG 27UK850", "cijena": "~350€", "opis": "27\", 4K, IPS, HDR, USB-C hub"},
            ],
            "visok": [
                {"naziv": "LG UltraWide 34WN80C", "cijena": "~550€", "opis": "34\", UltraWide, 4K, Nano IPS, USB-C"},
                {"naziv": "Dell UltraSharp U3223QE", "cijena": "~700€", "opis": "32\", 4K, IPS Black, USB-C, hub"},
            ],
        },
        "slusalice": {
            "nizak": [
                {"naziv": "JBL Tune 510BT", "cijena": "~30€", "opis": "Bežične, 40h baterije, JBL Pure Bass"},
                {"naziv": "Anker Soundcore Q20", "cijena": "~35€", "opis": "ANC, 40h baterije, odličan omjer cijene"},
            ],
            "srednji": [
                {"naziv": "Sony WH-1000XM4", "cijena": "~250€", "opis": "Vrhunske ANC slušalice, 30h baterije, LDAC"},
                {"naziv": "Bose QuietComfort 45", "cijena": "~230€", "opis": "Odličan ANC, udobne, 24h baterije"},
            ],
            "visi": [
                {"naziv": "Sony WH-1000XM5", "cijena": "~320€", "opis": "Najnoviji ANC, 30h, kristalno čist zvuk"},
                {"naziv": "Apple AirPods Max", "cijena": "~550€", "opis": "Premium ANC, Spatial Audio, za Apple ekosustav"},
            ],
        },
    },
}


def dohvati_proizvode(vrsta, namjena, budzet):
    try:
        return PROIZVODI[vrsta][namjena][budzet]
    except KeyError:
        return None


def formatiraj_proizvode(proizvodi):
    tekst = ""
    for i, p in enumerate(proizvodi, 1):
        tekst += f"{i}️⃣ **{p['naziv']}** – {p['cijena']}\n   {p['opis']}\n\n"
    return tekst


class ITOpremaBot(ActivityHandler):

    def __init__(self, conversation_state: ConversationState):
        self.conversation_state = conversation_state
        self.state_accessor = conversation_state.create_property("ConversationData")

    async def on_message_activity(self, turn_context: TurnContext):
        data = await self.state_accessor.get(turn_context, lambda: {
            "korak": "pocetak",
            "namjena": None,
            "budzet": None,
            "vrsta": None,
            "zadnji_proizvodi": None,
            "usporedba": []
        })

        user_text = turn_context.activity.text.lower().strip()
        odgovor = await self.obradi_poruku(user_text, data)

        await self.state_accessor.set(turn_context, data)
        await self.conversation_state.save_changes(turn_context)
        await turn_context.send_activity(MessageFactory.text(odgovor))

    async def obradi_poruku(self, tekst: str, data: dict) -> str:

        # INTENCIJA: pozdrav
        if any(w in tekst for w in ["zdravo", "bok", "hej", "pozdrav", "hello", "hi"]):
            data["korak"] = "pitaj_vrstu"
            data["namjena"] = None
            data["budzet"] = None
            data["vrsta"] = None
            data["zadnji_proizvodi"] = None
            data["usporedba"] = []
            return (
                "Pozdrav! Ja sam IT Oprema Bot 🤖\n\n"
                "Pomažem ti pronaći odgovarajuću IT opremu.\n\n"
                "Što te zanima?\n"
                "1️⃣ Laptop\n"
                "2️⃣ Router\n"
                "3️⃣ Periferija (miš, tipkovnica, monitor...)"
            )

        # INTENCIJA: usporedba - korisnik bira proizvode
        if data["korak"] == "usporedba_odabir":
            odabrani = []
            if "1" in tekst:
                odabrani.append(0)
            if "2" in tekst:
                odabrani.append(1)

            if len(odabrani) == 2 and data.get("zadnji_proizvodi"):
                proizvodi = data["zadnji_proizvodi"]
                p1 = proizvodi[odabrani[0]]
                p2 = proizvodi[odabrani[1]]
                data["korak"] = "gotovo"
                return (
                    f"📊 Usporedba:\n\n"
                    f"🔵 **{p1['naziv']}** – {p1['cijena']}\n{p1['opis']}\n\n"
                    f"🟢 **{p2['naziv']}** – {p2['cijena']}\n{p2['opis']}\n\n"
                    f"Oba su odlični izbori – razlika je uglavnom u cijeni i detaljima specifikacija.\n\n"
                    f"Želiš li pogledati drugu kategoriju? (da/ne)"
                )
            else:
                return "Molim te upiši npr. '1 i 2' kako bih usporedio ta dva proizvoda."

        # INTENCIJA: odabir vrste opreme
        if data["korak"] in ["pocetak", "pitaj_vrstu"] or any(w in tekst for w in ["laptop", "router", "periferija", "miš", "monitor", "tipkovnica"]):
            if any(w in tekst for w in ["laptop", "1"]):
                data["vrsta"] = "laptop"
                data["korak"] = "pitaj_namjenu"
                return (
                    "Odličan odabir! 💻\n\n"
                    "Za što ćeš koristiti laptop?\n"
                    "1️⃣ Ured / škola\n"
                    "2️⃣ Gaming\n"
                    "3️⃣ Programiranje\n"
                    "4️⃣ Grafički dizajn / video"
                )
            elif any(w in tekst for w in ["router", "2", "wifi", "mreža"]):
                data["vrsta"] = "router"
                data["korak"] = "pitaj_namjenu_router"
                return (
                    "Router! 📡\n\n"
                    "Kakva ti je situacija?\n"
                    "1️⃣ Mali stan / apartman\n"
                    "2️⃣ Kuća / veći prostor\n"
                    "3️⃣ Ured / poslovni prostor"
                )
            elif any(w in tekst for w in ["periferija", "3", "miš", "monitor", "tipkovnica", "slušalice"]):
                data["vrsta"] = "periferija"
                data["korak"] = "pitaj_namjenu_periferija"
                return (
                    "Periferija! 🖱️\n\n"
                    "Što točno tražiš?\n"
                    "1️⃣ Miš\n"
                    "2️⃣ Tipkovnica\n"
                    "3️⃣ Monitor\n"
                    "4️⃣ Slušalice"
                )

        # INTENCIJA: namjena laptopa
        if data["korak"] == "pitaj_namjenu":
            if any(w in tekst for w in ["ured", "škola", "office", "1"]):
                data["namjena"] = "ured"
            elif any(w in tekst for w in ["gaming", "igr", "2"]):
                data["namjena"] = "gaming"
            elif any(w in tekst for w in ["programiranje", "razvoj", "kod", "3"]):
                data["namjena"] = "programiranje"
            elif any(w in tekst for w in ["grafik", "dizajn", "video", "4"]):
                data["namjena"] = "dizajn"

            if data["namjena"]:
                data["korak"] = "pitaj_budzet"
                return (
                    "Odlično! 👍\n\n"
                    "Koji je tvoj budžet?\n"
                    "1️⃣ Do 500€\n"
                    "2️⃣ 500€ - 1000€\n"
                    "3️⃣ 1000€ - 1500€\n"
                    "4️⃣ Više od 1500€"
                )

        # INTENCIJA: namjena routera
        if data["korak"] == "pitaj_namjenu_router":
            if any(w in tekst for w in ["stan", "apartman", "mali", "1"]):
                data["namjena"] = "mali_prostor"
            elif any(w in tekst for w in ["kuća", "veći", "veliki", "2"]):
                data["namjena"] = "velika_kuca"
            elif any(w in tekst for w in ["ured", "poslovni", "3"]):
                data["namjena"] = "ured"

            if data["namjena"]:
                data["korak"] = "pitaj_budzet"
                return (
                    "Jasno! 📶\n\n"
                    "Koji je tvoj budžet za router?\n"
                    "1️⃣ Do 50€\n"
                    "2️⃣ 50€ - 150€\n"
                    "3️⃣ Više od 150€"
                )

        # INTENCIJA: namjena periferije
        if data["korak"] == "pitaj_namjenu_periferija":
            if any(w in tekst for w in ["miš", "mis", "1"]):
                data["namjena"] = "mis"
            elif any(w in tekst for w in ["tipkovnica", "keyboard", "2"]):
                data["namjena"] = "tipkovnica"
            elif any(w in tekst for w in ["monitor", "ekran", "3"]):
                data["namjena"] = "monitor"
            elif any(w in tekst for w in ["slušalice", "headset", "4"]):
                data["namjena"] = "slusalice"

            if data["namjena"]:
                data["korak"] = "pitaj_budzet"
                return (
                    "Super! 💡\n\n"
                    "Koji je tvoj budžet?\n"
                    "1️⃣ Do 30€\n"
                    "2️⃣ 30€ - 100€\n"
                    "3️⃣ Više od 100€"
                )

        # INTENCIJA: budžet + preporuka više proizvoda
        if data["korak"] == "pitaj_budzet":
            rijeci = tekst.split()

            # Pokušaj izvući broj iz teksta
            iznos = None
            for r in rijeci:
                r_clean = r.replace("€", "").replace(",", "").strip()
                try:
                    iznos = int(r_clean)
                    break
                except ValueError:
                    continue

            if iznos is not None and iznos <= 4:
                # Korisnik odabrao opciju 1-4
                if iznos == 1:
                    data["budzet"] = "nizak"
                elif iznos == 2:
                    data["budzet"] = "srednji"
                elif iznos == 3:
                    data["budzet"] = "visi"
                elif iznos == 4:
                    data["budzet"] = "visok"
            elif iznos is not None and iznos > 4:
                # Korisnik upisao stvarni iznos
                if data["vrsta"] == "laptop":
                    if iznos <= 500:
                        data["budzet"] = "nizak"
                    elif iznos <= 1000:
                        data["budzet"] = "srednji"
                    elif iznos <= 1500:
                        data["budzet"] = "visi"
                    else:
                        data["budzet"] = "visok"
                elif data["vrsta"] == "router":
                    if iznos <= 50:
                        data["budzet"] = "nizak"
                    elif iznos <= 150:
                        data["budzet"] = "srednji"
                    else:
                        data["budzet"] = "visi"
                elif data["vrsta"] == "periferija":
                    if iznos <= 30:
                        data["budzet"] = "nizak"
                    elif iznos <= 100:
                        data["budzet"] = "srednji"
                    else:
                        data["budzet"] = "visi"
            else:
                # Korisnik upisao riječ
                if any(w in tekst for w in ["jeftin", "najjeftin"]):
                    data["budzet"] = "nizak"
                elif "srednji" in tekst:
                    data["budzet"] = "srednji"
                elif any(w in tekst for w in ["više", "visok", "premium"]):
                    data["budzet"] = "visok"

            if data["budzet"]:
                proizvodi = dohvati_proizvode(data["vrsta"], data["namjena"], data["budzet"])
                if proizvodi:
                    data["zadnji_proizvodi"] = proizvodi
                    data["korak"] = "ponudi_usporedbu"
                    formatirani = formatiraj_proizvode(proizvodi)
                    return (
                        f"🎯 Pronašao sam {len(proizvodi)} preporuke za tebe:\n\n"
                        f"{formatirani}"
                        f"Želiš li usporediti ova dva proizvoda? (da/ne)"
                    )
                else:
                    data["korak"] = "gotovo"
                    return (
                        "Za tu kombinaciju trenutno nemam preporuku.\n"
                        "Pogledaj na Hanna.hr, Links.hr ili Mall.hr\n\n"
                        "Želiš li probati drugu kategoriju? (da/ne)"
                    )

        # INTENCIJA: korisnik želi usporedbu
        if data["korak"] == "ponudi_usporedbu":
            if any(w in tekst for w in ["da", "yes", "usporedi", "usporedba", "uspoređ"]):
                data["korak"] = "usporedba_odabir"
                return "Upiši npr. **'1 i 2'** kako bih usporedio prva dva proizvoda."
            elif any(w in tekst for w in ["ne", "no", "nije", "nema"]):
                data["korak"] = "gotovo"
                return "Razumijem! Želiš li pogledati drugu kategoriju? (da/ne)"

        # INTENCIJA: nova pretraga
        if data["korak"] == "gotovo" or any(w in tekst for w in ["nova", "novo", "restart", "ponovo", "opet", "još", "da"]):
            data["korak"] = "pitaj_vrstu"
            data["namjena"] = None
            data["budzet"] = None
            data["vrsta"] = None
            data["zadnji_proizvodi"] = None
            data["usporedba"] = []
            return (
                "Krenimo iznova! 🔄\n\n"
                "Što te zanima?\n"
                "1️⃣ Laptop\n"
                "2️⃣ Router\n"
                "3️⃣ Periferija"
            )

        # INTENCIJA: pomoć
        if any(w in tekst for w in ["pomoć", "help", "ne znam", "što možeš"]):
            return (
                "Mogu ti pomoći pronaći:\n"
                "💻 Laptop – za ured, gaming, programiranje ili dizajn\n"
                "📡 Router – za stan, kuću ili ured\n"
                "🖱️ Periferiju – miš, tipkovnica, monitor, slušalice\n\n"
                "Samo mi reci što tražiš!"
            )

        return (
            "Nisam siguran što tražiš. 🤔\n"
            "Možeš reći npr. 'laptop', 'router', 'periferija' ili 'pomoć'."
        )