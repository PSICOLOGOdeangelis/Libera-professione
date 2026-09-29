# Fase 4 — Modello economico

*Versione 1 del 29/09/2026. Orizzonte: ottobre 2026 – dicembre 2028 (27 mesi, così il 2027 e il 2028 sono completi).*

**File**
- [`04_modello_economico.csv`](04_modello_economico.csv): mese per mese, 3 scenari.
- [`04_sintesi_annuale.csv`](04_sintesi_annuale.csv): anno per anno, 3 scenari × 2 regimi fiscali.
- [`modello/modello_economico.py`](modello/modello_economico.py): il calcolo. Per cambiare un'ipotesi (prezzi, date, crescita) si modificano i **PARAMETRI** in cima al file e si rilancia `python3 piano/modello/modello_economico.py`, oppure lo si chiede a Claude Code.

> ⚠️ Tutti i numeri sono **stime**: servono a confrontare le scelte, non sono una previsione. La parte fiscale è semplificata (vedi §6) e **va verificata con il commercialista**, soprattutto per il 2027.

---

## 1. Situazione attuale di reddito (base di partenza)
| Voce | Lordo/anno | Netto/anno (stima) | Note |
|---|---|---|---|
| Stipendio (infermiere, part-time al 50%) | ~34.000 € imponibile (stima) | ~26.000 € (2.000 € × 13) | contributi INPS, TFR, Perseo Sirio |
| Docenza universitaria (docente a contratto SSN) | ~3.000 € | ~1.700 € | contributi ENPAPI |
| Libera professione (proiezione di partenza) | ~16–20 k€ | vedi §3: nel regime semplificato, **meno della metà** | contributi ENPAP |
| **Totale netto oggi** | | **~3.100 €/mese** | |

---

## 2. Le ipotesi dei tre scenari
| Leva | Prudente | **Realistico** | Ottimistico |
|---|---|---|---|
| Sedute individuali/settimana (oggi 6) | +0,3 al mese | **+0,5 al mese** | +0,7 al mese |
| Tetto clinico da dipendente / in aspettativa | 12 h / 22 h | 12 h / 22 h | 12 h / 22 h |
| Prezzo medio a seduta (vecchi + nuovi pazienti) | 60 → 70 € in 18 mesi | **60 → 72 € in 18 mesi** | 60 → 73 € in 15 mesi |
| Gruppo a Trofarello (mercoledì, massimo 7) | febbraio 2027, 3 membri, +1 ogni 3 mesi, 36 € | **dicembre 2026, 3 membri, +1 ogni 2 mesi, 37 €** | novembre 2026, 4 membri, +1 ogni 2 mesi, 38 € |
| Gruppo online (massimo 6) | gennaio 2028 | **ottobre 2027** | giugno 2027 |
| Cicli brevi (7 × 120 € = 840 €) | 2 all'anno | **3 all'anno** | 4 all'anno |
| Formazione caregiver (900 € l'uno) | 2 all'anno | **3 nel 2027, 4 nel 2028** | 4 nel 2027, 6 nel 2028 |
| Supervisione d'équipe (250 €/mese) | da gennaio 2028 | **da settembre 2027** | da aprile 2027, 2 contratti dal 2028 |
| Altri gruppi (caregiver, familiari DNA: 1.200 € a ciclo) | 1 nel 2028 | **1 nel 2027, 2 nel 2028** | 2 all'anno |
| Outdoor, biblioteca a pagamento | dal 2028 | **pilota nel 2027, biblioteca nel 2028** | come il realistico, ma più uscite |
| **Aspettativa** | non nell'orizzonte | **settembre 2028** | marzo 2028 |
| Settimane lavorate | 44 all'anno (agosto quasi fermo, dicembre 3) | | |
| Costi | ~274 €/mese di costi fissi + IA 25 € + materiali 20 € + estensione della polizza RC + piattaforma online 15 € + copie autore del libro + formazione outdoor 400 € + guida 100 € a uscita | | |

**Il vincolo delle 12 ore da dipendente.** Quando parte il gruppo online, il modello **toglie 1,5 h di individuale** per restare nelle 12 h. È una scelta economicamente giusta: un'ora di gruppo rende 150–170 €, un'ora di individuale ~70 €. Ma va tenuta presente clinicamente: quelle ore si liberano con la normale conclusione di alcuni percorsi, non interrompendoli.

---

## 3. Risultati annuali

### 3.1 Fatturato della libera professione
| Scenario | 2027 | 2028 | Ritmo annuo a dicembre 2028* |
|---|---|---|---|
| Prudente | 33,8 k€ | 53,5 k€ | ~54 k€ |
| **Realistico** | **44,9 k€** | **63,9 k€** | **~67 k€** (e in crescita: in aspettativa da settembre) |
| Ottimistico | 54,4 k€ | 86,2 k€ ⚠️ | ~98 k€ |

\* "Ritmo annuo": il fatturato degli ultimi 6 mesi riportato a un anno intero. Il valore esatto è nella colonna `fatturato_annualizzato_6_mesi` del CSV mensile.
⚠️ Nell'ottimistico il 2028 **supera gli 85.000 €**, il limite del forfettario: dall'anno successivo si esce dal regime (oltre i 100.000 € l'uscita è immediata). Va programmato.

### 3.2 Quanto resta in tasca: regime semplificato ("ordinario") contro forfettario
| Scenario / anno | Regime | Contributi ENPAP + imposte sulla libera professione | **Prelievo effettivo sull'utile** | Netto libera professione | **Netto totale medio/mese** (con stipendio e docenza) |
|---|---|---|---|---|---|
| Prudente 2027 | ordinario | 3,1 + 12,6 k€ | **53%** | 14,2 k€ | 3.490 € |
| Prudente 2027 | forfettario | 2,8 + 5,1 k€ | **26%** | 22,0 k€ | 4.140 € |
| **Realistico 2027** | **ordinario** | 4,2 + 16,9 k€ | **52%** | **19,2 k€** | **3.910 €** |
| **Realistico 2027** | **forfettario** | 3,6 + 6,3 k€ | **25%** | **30,3 k€** | **4.830 €** |
| Realistico 2028 (aspettativa da settembre) | ordinario | 6,1 + 23,9 k€ | 50% | 29,5 k€ | 3.930 € |
| Realistico 2028 (aspettativa da settembre) | forfettario | 5,1 + 8,8 k€ | 23% | 45,5 k€ | 5.270 € |
| Ottimistico 2028 | ordinario | 8,3 + 27,9 k€ | 44% | 45,4 k€ | 4.260 € |
| Ottimistico 2028 | forfettario | 6,9 + 9,4 k€ | 20% | 65,4 k€ | 5.920 € |

### 3.3 Il dato più importante di questa fase
**Nel regime semplificato, mentre sei dipendente, ogni euro in più di libera professione ti costa circa il 50% tra contributi e imposte.** La ragione: il reddito professionale si somma a uno stipendio di ~34–36 k€ e cade nella fascia in cui, contemporaneamente:
- l'aliquota IRPEF è del 33%, e del 43% oltre i 50 k€;
- le **detrazioni da lavoro dipendente si riducono** man mano che il reddito sale (fino a zero a 50 k€);
- si perde l'**ulteriore detrazione** introdotta dalla L. 207/2024 per i redditi tra 32 e 40 k€;
- si pagano le addizionali regionali e comunali e il contributo ENPAP.

Nel forfettario il prelievo scende al **~25%**. **Nello scenario realistico la differenza vale ~11 k€ nel 2027 e ~16 k€ nel 2028.** Nessun'altra azione del piano rende così tanto per così poco lavoro.

Il modello tiene conto anche del fatto che, per legge, il reddito forfettario **conta comunque** per il calcolo delle detrazioni sullo stipendio (L. 190/2014, art. 1 c. 75). Per questo nel forfettario il prelievo effettivo non è il 15% ma circa il 20–26%.

---

## 4. La soglia di uscita

### 4.1 Definizione (confermata)
**Si può chiedere l'aspettativa quando, da 6 mesi consecutivi, il fatturato viaggia a un ritmo ≥ 60.000 €/anno** (colonna `soglia_60k_raggiunta` del CSV mensile). In più servono:
- un **fondo di sicurezza** pari a 6 mesi di spese personali e dello studio: con 600–900 €/mese di spese personali più ~450 €/mese di costi dello studio (con i contributi), **~8.000 €**;
- il **gruppo in presenza pieno** (≥ 6 membri) e il gruppo online avviato;
- ≥ 2 invii al mese da altri professionisti, stabili da almeno 6 mesi.

### 4.2 Quando la si raggiunge
| Scenario | Ritmo ≥ 60 k€ sugli ultimi 6 mesi | Commento |
|---|---|---|
| Prudente | **non entro il 2028**: a fine 2028 si arriva a ~54 k€ | L'aspettativa andrebbe rinviata al 2029, o anticipata per liberare ore (vedi §4.4) |
| **Realistico** | **giugno 2028, ancora da dipendente** | **L'aspettativa a settembre 2028 è coerente**: si parte con la soglia già raggiunta |
| Ottimistico | **gennaio 2028** | L'aspettativa potrebbe essere anticipata a inizio 2028 |

**Perché la soglia si raggiunge anche con sole 12 ore.** Merito dei gruppi: con 7 + 6 membri, 3 ore settimanali fanno ~1.900 €/mese, quanto 7 ore di individuale. **Le due variabili che decidono i tempi sono l'avvio del gruppo in presenza entro dicembre e quello del gruppo online entro l'autunno 2027.** Tutto il resto conta meno.

### 4.3 Il costo dell'aspettativa
Durante l'aspettativa non ricevi stipendio (−2.000 €/mese), non versi contributi INPS e non maturi TFR né anzianità. Nel modello realistico, dopo l'avvio a settembre 2028, il fatturato mensile passa da ~5 k€ a ~7,5 k€ entro novembre 2028 grazie alle ore liberate (la media sugli ultimi 6 mesi a dicembre è ~67 k€ e continua a salire). Il **netto mensile resta paragonabile a quello di oggi** (ordinario) o migliora (forfettario). È una fase di **investimento sostenibile**, non di sacrificio.

### 4.4 Le tue spese cambiano la lettura della soglia
Con **600–900 €/mese di spese personali** (dato del 30/09) le soglie diventano due, ben distinte:

| Soglia | Cosa significa | Fatturato annuo necessario (stima, forfettario) |
|---|---|---|
| **Soglia di sicurezza** | Coprire le tue spese personali, lo studio, i contributi e le imposte, senza intaccare i risparmi | **~20–22 k€** (si arriva a 16–18 k€ di spese e costi netti) |
| **Soglia di parità** (la tua: 60 k€) | Guadagnare quanto oggi, compensando anche i contributi e il TFR che perdi | **~60 k€** |

**Conseguenze:**
1. Il **rischio economico dell'aspettativa è basso**: oggi fatturi già circa quanto serve per la soglia di sicurezza, e con il gruppo la superi nel 2027 in tutti gli scenari.
2. La soglia dei 60 k€ resta l'obiettivo per **lasciare definitivamente** l'Azienda (dimissioni), perché lì si perdono per sempre contributi, TFR e posto. **Per l'aspettativa, che è reversibile, può bastare una soglia più bassa**: propongo **~45 k€ annualizzati** con il gruppo in presenza pieno.
3. Anticipare l'aspettativa conviene per due motivi, **le ore** (il tetto delle 12 h è il vero freno alla crescita) e **il fisco** (se parte a gennaio, il forfettario si apre l'anno successivo). Il costo principale è **previdenziale**, non di sopravvivenza. **L'opzione "aspettativa a gennaio 2028"** va quindi valutata al checkpoint di ottobre 2027 (Fase 5).

---

## 5. Pensione e contributi: cosa cambia con il passaggio
*(Una tua domanda aperta. Qui ci sono i punti da portare all'ufficio del personale e a un patronato; le risposte cambieranno il modello.)*

| Tema | Cosa succede (da verificare) | Effetto |
|---|---|---|
| **INPS durante l'aspettativa** | Aspettativa "senza assegni": di norma **niente contribuzione**, salvo riscatto o versamenti volontari | Si interrompe l'accumulo sulla pensione INPS |
| **INPS dopo le eventuali dimissioni** | I contributi versati dal 1996 restano; la pensione di vecchiaia (67 anni con i requisiti attuali) sarà calcolata su ~32 anni invece di ~43 | Importo più basso: chiedere una **simulazione** al patronato o su "La mia pensione futura" (INPS) nei due casi, "resto fino a 67 anni" ed "esco a 56–57 anni" |
| **ENPAP** | Diventa la tua cassa principale. Il contributo minimo è del 10% del reddito, **ma si può scegliere un'aliquota più alta, fino al 30%** | Leva per compensare la perdita di contributi INPS; i contributi sono deducibili (utile nel regime ordinario) |
| **Cumulo gratuito** | INPS + ENPAP possono essere cumulati per una pensione unica (L. 232/2016) | Da verificare requisiti ed età |
| **Perseo Sirio** | In aspettativa e dopo l'uscita si interrompe il contributo del datore. Opzioni: mantenere la posizione, riscatto, trasferimento | Valutare di tenerlo e continuare con versamenti propri |
| **TFR** | Liquidazione differita per i dipendenti pubblici in caso di dimissioni | Non contarci come liquidità immediata |
| **ENPAPI (docenza)** | Resta legata all'incarico SSN | Da verificare cosa succede in aspettativa |

**Stima indicativa.** Con ~32 anni INPS invece di ~43, la parte INPS della pensione si riduce grosso modo del 20–25%. Una parte si può recuperare con un'aliquota ENPAP più alta, per esempio il 14–16%. **È una stima grezza**: serve la simulazione ufficiale.

---

## 6. Fisco: semplificazioni del modello e cose da sapere

**Semplificazioni usate:**
- aliquote IRPEF 2026 (23% / 33% / 43%);
- detrazioni da lavoro dipendente (art. 13 TUIR) e ulteriore detrazione (L. 207/2024);
- addizionali stimate al 3% forfettario;
- ENPAP al 10% con minimo di 856 € e 135 € di maternità;
- contributo integrativo del 2% considerato neutro (si addebita in fattura e si versa);
- forfettario con coefficiente del 78% e imposta sostitutiva al 15% (il 5% è escluso prudenzialmente);
- stipendio imponibile ~34 k€;
- nessun'altra detrazione (spese mediche, familiari…).

**Il calendario delle decisioni fiscali**
| Quando | Cosa | Perché conta |
|---|---|---|
| **Ottobre–novembre 2026** | Chiedere al commercialista: (1) se versamenti aggiuntivi a Perseo Sirio entro dicembre riducono il reddito da lavoro dipendente che conta per la soglia; (2) che soglia è prevista per il 2027 (Legge di Bilancio 2027 in discussione) | Si decide il regime del **2027**: ~11 k€ di differenza |
| **Dicembre 2026 / gennaio 2027** | Reddito da lavoro dipendente 2026 definitivo → scelta del regime per il 2027 | |
| **Autunno 2027** | Stessa verifica sul reddito da lavoro dipendente 2027 → regime del 2028 | Se a fine 2026 non ci sei rientrato, **il 2027 è l'anno per organizzarsi**: aumenti contrattuali possono spingerti sopra la soglia |
| **Settembre 2028** (aspettativa) | Il reddito da lavoro dipendente 2028 sarà di ~8/12 → **forfettario quasi certo dal 2029** | Da verificare come si applica la causa ostativa durante l'aspettativa |
| **Sempre** | Tenere il fatturato sotto gli 85 k€ se si vuole restare nel forfettario | Scenario ottimistico 2028 |

**Un'osservazione strategica.** Se si resta nel regime ordinario nel 2027–2028, **anticipare l'aspettativa all'inizio di un anno** (per esempio gennaio invece di settembre) fa scendere il reddito da lavoro dipendente di quell'anno e apre il forfettario per l'anno successivo. Il momento di avvio dell'aspettativa è quindi anche una **scelta fiscale**. Da valutare con il commercialista a fine 2027.

---

## 7. Indicatori di "pronto a uscire" (per l'aspettativa)
| # | Indicatore | Soglia | Dove si misura |
|---|---|---|---|
| 1 | Fatturato annualizzato sugli ultimi 6 mesi | ≥ 60.000 € | CSV / dashboard (Fase 6) |
| 2 | Quota di fatturato **ricorrente** (individuale + gruppi + supervisione) | ≥ 80% | Dashboard |
| 3 | Gruppo in presenza | ≥ 6 membri stabili da 3 mesi | Registro |
| 4 | Gruppo online | avviato, ≥ 4 membri | Registro |
| 5 | Nuove richieste | ≥ 4 primi colloqui al mese, **lista d'attesa** ≥ 3 persone | Registro dei contatti |
| 6 | Invii da altri professionisti | ≥ 2 al mese da 6 mesi | Domanda al primo colloquio |
| 7 | Fondo di sicurezza | ≥ 6 mesi di spese | Conto dedicato |
| 8 | Previdenza | simulazione della pensione fatta, scelta dell'aliquota ENPAP decisa | Patronato |
| 9 | Regime fiscale dell'anno successivo | chiaro e verificato | Commercialista |

**Regola decisionale (proposta, adottata in attesa di un tuo parere).** 7 indicatori su 9, tra cui obbligatoriamente l'1, il 3 e il 7, significano "sì" all'aspettativa. Meno di 7 significano rinviare di 6 mesi e rivedere il piano. Per l'**aspettativa**, l'indicatore 1 si può abbassare a 45 k€ (§4.4). Per le **dimissioni** resta a 60 k€, e si aggiunge la simulazione della pensione.

**Scenario di riferimento per la roadmap: realistico.** Il prudente è il "piano B" e l'ottimistico serve a capire quando accelerare.

---

## Da verificare
| # | Cosa | Con chi | Quando |
|---|---|---|---|
| 1 | Versamenti a Perseo Sirio e soglia dei 35.000 €; soglia prevista per il 2027 | Commercialista, ufficio stipendi | **Entro novembre 2026** |
| 2 | Reddito da lavoro dipendente imponibile effettivo (il modello usa 34.000 €) | Certificazione Unica / cedolino | Dicembre 2026 |
| 3 | Addizionali regionale e comunale effettive; detrazioni personali | Commercialista | Dicembre 2026 |
| 4 | Aliquota ENPAP da scegliere (10% o più) e minimi aggiornati | ENPAP | Annuale |
| 5 | Simulazione della pensione: resto fino a 67 anni / esco a 56–57 anni; cumulo con ENPAP | Patronato, INPS | Entro il 2027 |
| 6 | Aspettativa: contributi, Perseo Sirio, TFR, anzianità, docenza ENPAPI; causa ostativa del forfettario durante l'aspettativa | Ufficio del personale, commercialista | Entro il 2027 |
| 7 | Tempi di liquidazione del TFR in caso di dimissioni | Ufficio del personale | Prima delle dimissioni |
| 8 | ~~Spese personali mensili~~ → 600–900 €/mese (risposta del 30/09) | — | ✔ |

**Fonti consultate il 29/09/2026:**
- IRPEF 2026: [Fiscomania](https://fiscomania.com/aliquote-irpef/), [CGIL Lazio](https://lazio.cgil.it/2026/01/novita-irpef-2026-aliquote-scaglioni-detrazioni/);
- ENPAP: [FISCOeTASSE](https://www.fiscoetasse.com/domande-e-risposte/12196-contributi-enpap-psicologi-acconto-entro-il-3-marzo.html), [ENPAP](https://www.enpap.it/come-fare-per/versare-i-contributi/);
- soglia del forfettario: [Eutekne](https://www.eutekne.info/Sezioni/Art_1075059_forfetario_con_soglia_a_35_000_euro_per_i_redditi_di_lavoro_dipendente.aspx);
- aspettativa: [Nurse24](https://www.nurse24.it/dossier/pubblico-impiego/pubblico-impiego-aspettativa-attivita-imprenditoriale.html).
