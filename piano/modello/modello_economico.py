#!/usr/bin/env python3
"""
Modello economico — Fase 4 del piano di sviluppo della libera professione.

Genera:
  piano/04_modello_economico.csv   (mese per mese, 3 scenari)
  piano/04_sintesi_annuale.csv     (anno per anno, 3 scenari x 2 ipotesi fiscali)

Tutti i numeri sono IPOTESI: modificare i PARAMETRI qui sotto e rilanciare
    python3 piano/modello/modello_economico.py
Le formule fiscali sono semplificate e vanno verificate con il commercialista.
"""
import csv
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# PARAMETRI GENERALI
# ---------------------------------------------------------------------------
MESI = [(2026, m) for m in (10, 11, 12)] + [(a, m) for a in (2027, 2028) for m in range(1, 13)]
NOMI_MESE = "gen feb mar apr mag giu lug ago set ott nov dic".split()

# Settimane lavorate per mese (44 settimane l'anno: agosto ridotto, dicembre 3)
def settimane(mese):
    return {8: 1, 12: 3}.get(mese, 4)

STIPENDIO_NETTO_MESE = 2000        # netto mensile Azienda (+ tredicesima a dicembre)
REDDITO_DIPENDENTE_ANNUO = 34000   # imponibile IRPEF stimato (vicino alla soglia di 35.000)
DOCENZA_LORDO_ANNUO = 3000         # docenza universitaria (ENPAPI)
DOCENZA_REDDITO_ANNUO = 2520       # al netto dei contributi ENPAPI stimati
DOCENZA_NETTO_ANNUO = 1700         # netto stimato dopo IRPEF marginale

ADDIZIONALI = 0.03                 # addizionali regionale + comunale (stima forfettaria)
ENPAP_ALIQ = 0.10                  # contributo soggettivo minimo (elevabile fino al 30%)
ENPAP_MIN = 856                    # minimo soggettivo 2026
ENPAP_MATERNITA = 135              # contributo di maternità
COEFF_FORFETTARIO = 0.78
IMPOSTA_FORFETTARIO = 0.15         # 5% solo se ricorrono i requisiti di "nuova attività"

# Costi fissi mensili (dati dell'intervista)
COSTI_FISSI_MESE = (1560 + 300 + 450 + 80 + 700 + 200) / 12   # ~274 €
COSTO_IA_MESE = 25                 # dal nov 2026
COSTO_PIATTAFORMA_MESE = 15        # dall'avvio del gruppo online
COSTO_MATERIALI_MESE = 20
COSTO_RC_EXTRA_MESE = 100 / 12     # estensione polizza (gruppo, online, outdoor) dal 2027

# ---------------------------------------------------------------------------
# SCENARI
# ---------------------------------------------------------------------------
# Date espresse come (anno, mese). None = non avviene nell'orizzonte del modello.
SCENARI = {
    "prudente": dict(
        sedute_iniziali=6, crescita_mese=0.3, crescita_mese_aspettativa=0.6,
        prezzo_finale=70, mesi_per_prezzo=18,
        gruppo_avvio=(2027, 2), gruppo_membri_iniziali=3, gruppo_mesi_per_nuovo_membro=3, gruppo_prezzo=36,
        online_avvio=(2028, 1), online_membri_iniziali=3, online_mesi_per_nuovo_membro=3, online_prezzo=35,
        cicli=[(2027, 4), (2027, 10), (2028, 4), (2028, 10)], ciclo_ricavo=840,
        caregiver=[(2027, 5), (2027, 11), (2028, 4), (2028, 10)], caregiver_ricavo=900,
        supervisione=[((2028, 1), 250)],
        altri_gruppi=[(2028, 5)], altri_gruppi_ricavo=1200,
        outdoor=[(2028, 5), (2028, 6), (2028, 9)],
        biblioteca=[],
        aspettativa=None,
    ),
    "realistico": dict(
        sedute_iniziali=6, crescita_mese=0.5, crescita_mese_aspettativa=1.0,
        prezzo_finale=72, mesi_per_prezzo=18,
        gruppo_avvio=(2026, 12), gruppo_membri_iniziali=3, gruppo_mesi_per_nuovo_membro=2, gruppo_prezzo=37,
        online_avvio=(2027, 10), online_membri_iniziali=3, online_mesi_per_nuovo_membro=2, online_prezzo=35,
        cicli=[(2027, 3), (2027, 6), (2027, 11), (2028, 3), (2028, 6), (2028, 11)], ciclo_ricavo=840,
        caregiver=[(2027, 1), (2027, 5), (2027, 10), (2028, 2), (2028, 5), (2028, 10), (2028, 11)], caregiver_ricavo=900,
        supervisione=[((2027, 9), 250)],
        altri_gruppi=[(2027, 10), (2028, 3), (2028, 10)], altri_gruppi_ricavo=1200,
        outdoor=[(2027, 5), (2027, 6), (2027, 9), (2028, 5), (2028, 6), (2028, 9)],
        biblioteca=[(2028, 3), (2028, 4), (2028, 10), (2028, 11)],
        aspettativa=(2028, 9),
    ),
    "ottimistico": dict(
        sedute_iniziali=6, crescita_mese=0.7, crescita_mese_aspettativa=1.4,
        prezzo_finale=73, mesi_per_prezzo=15,
        gruppo_avvio=(2026, 11), gruppo_membri_iniziali=4, gruppo_mesi_per_nuovo_membro=2, gruppo_prezzo=38,
        online_avvio=(2027, 6), online_membri_iniziali=4, online_mesi_per_nuovo_membro=2, online_prezzo=35,
        cicli=[(2027, 2), (2027, 4), (2027, 6), (2027, 11), (2028, 2), (2028, 4), (2028, 6), (2028, 11)], ciclo_ricavo=840,
        caregiver=[(2027, 1), (2027, 3), (2027, 5), (2027, 10), (2028, 1), (2028, 3), (2028, 5), (2028, 9), (2028, 10), (2028, 11)], caregiver_ricavo=900,
        supervisione=[((2027, 4), 250), ((2028, 1), 250)],
        altri_gruppi=[(2027, 4), (2027, 10), (2028, 3), (2028, 10)], altri_gruppi_ricavo=1200,
        outdoor=[(2027, 5), (2027, 6), (2027, 9), (2028, 4), (2028, 5), (2028, 6), (2028, 9), (2028, 10)],
        biblioteca=[(2028, 3), (2028, 4), (2028, 10), (2028, 11)],
        aspettativa=(2028, 3),
    ),
}

OUTDOOR_RICAVO, OUTDOOR_COSTO_GUIDA = 250, 100
BIBLIOTECA_RICAVO = 200
ORE_CLINICHE_MAX_DIPENDENTE = 12
ORE_CLINICHE_MAX_ASPETTATIVA = 22
ORE_GRUPPO = 1.5

# ---------------------------------------------------------------------------
def idx(am):
    return MESI.index(am) if am in MESI else None

def mesi_da(am_corrente, am_inizio):
    """Mesi trascorsi da am_inizio (0 nel mese di avvio); None se non ancora avviato."""
    if am_inizio is None:
        return None
    d = (am_corrente[0] - am_inizio[0]) * 12 + am_corrente[1] - am_inizio[1]
    return d if d >= 0 else None

def membri(am, avvio, iniziali, ogni, massimo):
    d = mesi_da(am, avvio)
    return 0 if d is None else min(massimo, iniziali + d // ogni)

def simula(nome, p):
    righe = []
    sedute = p["sedute_iniziali"]
    for i, (a, m) in enumerate(MESI):
        am = (a, m)
        in_asp = p["aspettativa"] is not None and mesi_da(am, p["aspettativa"]) is not None
        g1 = membri(am, p["gruppo_avvio"], p["gruppo_membri_iniziali"], p["gruppo_mesi_per_nuovo_membro"], 7)
        g2 = membri(am, p["online_avvio"], p["online_membri_iniziali"], p["online_mesi_per_nuovo_membro"], 6)
        ore_gruppi = ORE_GRUPPO * ((g1 > 0) + (g2 > 0))
        cap = (ORE_CLINICHE_MAX_ASPETTATIVA if in_asp else ORE_CLINICHE_MAX_DIPENDENTE) - ore_gruppi
        if i > 0:
            sedute += p["crescita_mese_aspettativa"] if in_asp else p["crescita_mese"]
        sedute = min(sedute, cap)
        prezzo = 60 + (p["prezzo_finale"] - 60) * min(1, i / p["mesi_per_prezzo"])
        sett = settimane(m)
        r_ind = sedute * prezzo * sett
        r_g1 = g1 * p["gruppo_prezzo"] * sett
        r_g2 = g2 * p["online_prezzo"] * sett
        r_cicli = p["ciclo_ricavo"] * p["cicli"].count(am)
        r_care = p["caregiver_ricavo"] * p["caregiver"].count(am)
        r_sup = sum(v for inizio, v in p["supervisione"] if mesi_da(am, inizio) is not None and m != 8)
        r_altri = p["altri_gruppi_ricavo"] * p["altri_gruppi"].count(am)
        n_out = p["outdoor"].count(am)
        r_out = OUTDOOR_RICAVO * n_out
        r_bib = BIBLIOTECA_RICAVO * p["biblioteca"].count(am)
        ricavi = r_ind + r_g1 + r_g2 + r_cicli + r_care + r_sup + r_altri + r_out + r_bib
        costi = COSTI_FISSI_MESE + COSTO_MATERIALI_MESE
        costi += COSTO_IA_MESE if am >= (2026, 11) else 0
        costi += COSTO_RC_EXTRA_MESE if a >= 2027 else 0
        costi += COSTO_PIATTAFORMA_MESE if g2 > 0 else 0
        costi += OUTDOOR_COSTO_GUIDA * n_out
        costi += 150 if am == (2026, 11) else 0                               # copie autore del libro
        costi += 400 if (p["outdoor"] and am == (min(p["outdoor"])[0], 1)) else 0  # formazione pratica outdoor (gennaio dell'anno del pilota)
        stip = 0 if in_asp else STIPENDIO_NETTO_MESE * (2 if m == 12 else 1)
        righe.append(dict(
            scenario=nome, anno=a, mese=f"{NOMI_MESE[m-1]} {a}",
            stato="aspettativa" if in_asp else "dipendente",
            sedute_individuali_settimana=round(sedute, 1), prezzo_medio_seduta=round(prezzo, 1),
            membri_gruppo_trofarello=g1, membri_gruppo_online=g2,
            ore_cliniche_settimana=round(sedute + ore_gruppi, 1),
            ricavi_individuale=round(r_ind), ricavi_gruppo_trofarello=round(r_g1), ricavi_gruppo_online=round(r_g2),
            ricavi_cicli_brevi=r_cicli, ricavi_caregiver_comuni=r_care, ricavi_supervisione_equipe=r_sup,
            ricavi_altri_gruppi=r_altri, ricavi_outdoor=r_out, ricavi_biblioteca=r_bib,
            ricavi_totali=round(ricavi), costi=round(costi), stipendio_netto=stip,
        ))
    # Fatturato annualizzato: ricavi degli ultimi 6 mesi riportati a 44 settimane lavorative.
    # Soglia di uscita raggiunta quando, da 6 mesi, si fattura al ritmo di almeno 60.000 euro l'anno.
    for i, r in enumerate(righe):
        fin = righe[max(0, i - 5): i + 1]
        sett = sum(settimane(NOMI_MESE.index(x["mese"].split()[0]) + 1) for x in fin)
        r["fatturato_annualizzato_6_mesi"] = round(sum(x["ricavi_totali"] for x in fin) / sett * 44)
        r["soglia_60k_raggiunta"] = "SI" if (i >= 5 and r["fatturato_annualizzato_6_mesi"] >= 60000) else ""
    return righe

# ---------------------------------------------------------------------------
# FISCO (semplificato)
# ---------------------------------------------------------------------------
def irpef_lorda(x):
    x = max(0, x)
    return 0.23 * min(x, 28000) + 0.33 * max(0, min(x, 50000) - 28000) + 0.43 * max(0, x - 50000)

def detrazioni_dipendente(rc, quota_anno):
    """Art. 13 TUIR + ulteriore detrazione (L. 207/2024), rapportate ai mesi di lavoro."""
    if quota_anno <= 0:
        return 0
    if rc <= 15000:
        d = 1955
    elif rc <= 28000:
        d = 1910 + 1190 * (28000 - rc) / 13000
    elif rc <= 50000:
        d = 1910 * (50000 - rc) / 22000
    else:
        d = 0
    if 20000 < rc <= 32000:
        d += 1000
    elif 32000 < rc <= 40000:
        d += 1000 * (40000 - rc) / 8000
    return d * quota_anno

def imposte_totali(reddito_dip, reddito_doc, reddito_lp_irpef, rc_per_detrazioni, quota_anno):
    base = reddito_dip + reddito_doc + reddito_lp_irpef
    lorda = irpef_lorda(base)
    netta = max(0, lorda - detrazioni_dipendente(rc_per_detrazioni, quota_anno))
    return netta + ADDIZIONALI * base

def contributi_enpap(reddito, anno_intero):
    # sui soli mesi ott-dic 2026 non si applicano minimo e maternità (contano sull'intero anno)
    if not anno_intero:
        return ENPAP_ALIQ * reddito
    return max(ENPAP_MIN, ENPAP_ALIQ * reddito) + ENPAP_MATERNITA

def fisco_anno(ricavi, costi, mesi_dipendente, regime, anno_intero=True):
    quota = mesi_dipendente / 12
    rd = REDDITO_DIPENDENTE_ANNUO * quota
    rdoc = DOCENZA_REDDITO_ANNUO
    senza_lp = imposte_totali(rd, rdoc, 0, rd + rdoc, quota)
    if regime == "ordinario":
        reddito = max(0, ricavi - costi)
        enpap = contributi_enpap(reddito, anno_intero)
        imp = max(0, reddito - enpap)
        con_lp = imposte_totali(rd, rdoc, imp, rd + rdoc + imp, quota)
        tasse_lp = con_lp - senza_lp
    else:  # forfettario
        reddito = COEFF_FORFETTARIO * ricavi
        enpap = contributi_enpap(reddito, anno_intero)
        imp = max(0, reddito - enpap)
        sostitutiva = IMPOSTA_FORFETTARIO * imp
        # il reddito forfettario conta per il calcolo delle detrazioni (L. 190/2014, c. 75)
        con_lp = imposte_totali(rd, rdoc, 0, rd + rdoc + imp, quota)
        tasse_lp = sostitutiva + (con_lp - senza_lp)
    return enpap, tasse_lp

# ---------------------------------------------------------------------------
def main():
    tutte = []
    sintesi = []
    for nome, p in SCENARI.items():
        righe = simula(nome, p)
        tutte += righe
        for anno in (2026, 2027, 2028):
            ra = [r for r in righe if r["anno"] == anno]
            ricavi = sum(r["ricavi_totali"] for r in ra)
            costi = sum(r["costi"] for r in ra)
            mesi_dip = sum(1 for r in ra if r["stato"] == "dipendente") + (9 if anno == 2026 else 0)
            stip = sum(r["stipendio_netto"] for r in ra)
            for regime in ("ordinario", "forfettario"):
                if anno == 2026 and regime == "forfettario":
                    continue  # nel 2026 il regime è certamente quello semplificato
                enpap, tasse = fisco_anno(ricavi, costi, mesi_dip, regime, anno_intero=len(ra) == 12)
                netto_lp = ricavi - costi - enpap - tasse
                doc = DOCENZA_NETTO_ANNUO * len(ra) / 12
                sintesi.append(dict(
                    scenario=nome, anno=anno, mesi_nel_modello=len(ra), regime_fiscale=regime,
                    ricavi_libera_professione=round(ricavi), costi=round(costi), enpap=round(enpap),
                    imposte_attribuibili_lp=round(tasse),
                    aliquota_effettiva_su_utile=f"{(enpap + tasse) / max(1, ricavi - costi):.0%}",
                    netto_libera_professione=round(netto_lp), stipendio_netto=round(stip),
                    docenza_netto=round(doc), netto_totale=round(netto_lp + stip + doc),
                    netto_medio_mensile=round((netto_lp + stip + doc) / len(ra)),
                    fatturato_annualizzato_dicembre=[r for r in ra if r["mese"].startswith("dic")][0]["fatturato_annualizzato_6_mesi"],
                ))
    with open(os.path.join(BASE, "04_modello_economico.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(tutte[0].keys()), delimiter=";")
        w.writeheader(); w.writerows(tutte)
    with open(os.path.join(BASE, "04_sintesi_annuale.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sintesi[0].keys()), delimiter=";")
        w.writeheader(); w.writerows(sintesi)
    # riepilogo a video
    for s in sintesi:
        print(f"{s['scenario']:11} {s['anno']} {s['regime_fiscale']:11} ricavi {s['ricavi_libera_professione']:>6} "
              f"costi {s['costi']:>5} enpap {s['enpap']:>5} tasse {s['imposte_attribuibili_lp']:>6} "
              f"({s['aliquota_effettiva_su_utile']}) nettoLP {s['netto_libera_professione']:>6} "
              f"netto tot/mese {s['netto_medio_mensile']:>5} annualizz.dic {s['fatturato_annualizzato_dicembre']}")
    for nome in SCENARI:
        rr = [r for r in tutte if r["scenario"] == nome]
        ok = next((r["mese"] for r in rr if r["soglia_60k_raggiunta"]), None)
        print(f"{nome}: soglia di uscita (60k annualizzati sugli ultimi 6 mesi) raggiunta a: {ok}")

if __name__ == "__main__":
    main()
