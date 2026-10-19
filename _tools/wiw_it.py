# Italian copy for the client city. Keys mirror wiw_content.P by "num".
DISTRICTS = {
    "old-town": ("Centro Storico", "Titolari e operatività", "Aziende di servizi dove ogni lavoro è un preventivo nuovo, un cantiere nuovo o un ordine nuovo. Qui l'AI deve reggere l'operatività vera."),
    "business-district": ("Quartiere degli Affari", "Direzione e lavoro regolamentato", "Persone le cui decisioni pesano: un CEO, uno studio medico, un revisore, un progetto con rischi di sicurezza. Qui l'AI deve essere verificabile."),
    "market-square": ("Piazza del Mercato", "Marketing e vendite", "Chi vive di attenzione e di pipeline. Qui l'AI deve suonare umana e portare lavoro."),
    "the-station": ("La Stazione", "Cambio di rotta", "Per chi si sta spostando verso il prossimo ruolo. Qui l'AI costruisce le prove per decidere dove andare."),
}

T = {}

T["01"] = dict(
    slug="aziende-eventi", persona="Il Titolare con Tanta <em>Operatività</em>", persona_plain="Il Titolare con Tanta Operatività",
    sector="Eventi e produzione live", country="Italia",
    h1="AI per aziende di eventi e produzione live",
    title="AI per Aziende di Eventi: Preventivi e Brief in Automatico",
    desc="Come un'azienda di produzione eventi ha automatizzato l'85–90% di preventivi e brief per il team con l'AI. Una giornata tipo, cosa è stato costruito e come iniziare.",
    roles=["Titolare", "Responsabile operativo", "Coordinatore del team"],
    answer="Un'azienda di eventi può usare l'AI per trasformare la trascrizione di un sopralluogo in tre documenti insieme: un brief logistico, uno tecnico e il preventivo per il cliente. Il segreto è un prezzario e delle regole di sconto scritte che l'AI può leggere, non un prompt più lungo.",
    story=[
        "Gestisci un'azienda di servizi dove ogni lavoro è un preventivo nuovo, un brief nuovo e mille pezzi in movimento: specifiche tecniche per il team e una versione curata per il cliente. Hai provato a passare tutto all'AI e si rompeva appena la richiesta non era semplice: impaginazione sbagliata, voci mancanti, documenti che il team non poteva usare.",
        "<strong>Il problema non è mai stato lo strumento. Era trattare un'azienda da 400 eventi l'anno come un singolo prompt.</strong> Quando il lavoro è stato diviso nei documenti giusti per le persone giuste, con un prezzario vero e regole di sconto scritte, il risultato è cambiato completamente.",
    ],
    result="Preventivi e brief ora sono automatizzati per circa l'85–90%. Il titolare interviene solo sulla strategia e sui casi davvero particolari.",
    day=[
        ("08:00", "I vocali del sopralluogo di ieri sono ancora nel telefono.", "La trascrizione entra nel progetto. Tre bozze ti aspettano prima del caffè."),
        ("10:00", "Riscrivi lo stesso lavoro due volte: per il team e per il cliente.", "I brief logistico e tecnico arrivano al team nel loro formato."),
        ("13:00", "Il prezzo dipende da chi chiede. Sta nella tua testa.", "Le regole di sconto per tipo di cliente sono scritte. L'AI le applica e chiede se ha dubbi."),
        ("16:00", "Il preventivo parte tardi, con una voce dimenticata.", "Il preventivo segue il tuo modello e il tuo prezzario veri. Tu controlli, non scrivi."),
        ("19:00", "Sei ancora sulle email.", "Sei sull'evento, dove l'azienda vive davvero."),
    ],
    signals=[
        "Ho provato l'AI per preventivi e proposte, ma crolla appena il lavoro è complesso",
        "Il mio team ha bisogno di informazioni diverse dai clienti e riscrivo tutto due volte",
        "Non ho tempo di diventare un prompt engineer. Deve funzionare e basta",
        "Niente è scritto da nessuna parte in un modo che l'AI possa usare",
    ],
    outcomes=[
        "Un sistema a documenti separati: uno per l'operatività interna, uno per il cliente",
        "Un brief scritto per ogni ruolo del team, così l'AI smette di indovinare",
        "Una percentuale di automazione realistica per la tua azienda, non una promessa vaga",
        "Una lista con le priorità: cosa delegare prima e cosa tenere",
    ],
    faq=[
        ("L'AI può fare preventivi per un'azienda di eventi?", "Sì, se ha il tuo prezzario reale, le tue regole di sconto e due o tre preventivi di esempio. Senza, tira a indovinare, ed è proprio questo che si rompe sui lavori complessi."),
        ("Devo cambiare software?", "No. In questo caso si è usato il Google Drive che il titolare aveva già e un progetto Claude. La novità è stata mettere per iscritto regole che esistevano solo nella sua testa."),
        ("Quanto ci vuole per risparmiare tempo?", "Il primo test con una trascrizione reale ha prodotto un brief e un preventivo utilizzabili nelle prime lezioni. Dopo, quasi tutto il lavoro è colmare i vuoti che l'AI mette in luce, come un listino artisti mancante."),
    ],
)

T["02"] = dict(
    slug="ingegneria-infrastrutture", persona="Lo Specialista dei Settori <em>Regolamentati</em>", persona_plain="Lo Specialista dei Settori Regolamentati",
    sector="Permessi e conformità nei progetti infrastrutturali", country="Progetti internazionali",
    h1="AI per ingegneria e conformità nei progetti infrastrutturali",
    title="AI per Ingegneria e Infrastrutture: Sistemi Verificabili, non Chatbot",
    desc="Come un coordinatore dei permessi di lavoro su progetti internazionali ha costruito sottosistemi AI verificabili, senza perdita di dati tra i cantieri.",
    roles=["Compliance", "Responsabile tecnico", "Auditor"],
    answer="Nell'ingegneria regolamentata l'AI è utile quando è costruita come piccoli agenti verificabili, con input e regole definiti, non come un'unica finestra di chat. Ogni agente fa un lavoro e una persona può controllare ogni passaggio.",
    story=[
        "Lavori dove un errore ha conseguenze reali: documentazione di sicurezza, permessi, coordinamento tra più cantieri, tutto sotto controllo. Non vuoi un chatbot. Vuoi un sistema che puoi verificare.",
        "<strong>Non si tratta di scrivere prompt migliori. Si tratta di costruire un sistema a più passaggi</strong>: agenti che gestiscono parti definite del lavoro, con regole controllabili e nessuna perdita silenziosa di dati tra un passaggio e l'altro.",
    ],
    result="Sottosistemi verificati senza perdita di dati tra i cantieri, ora in crescita verso un sistema di coordinamento completo. Il cliente ha poi ampliato il progetto di sua iniziativa.",
    day=[
        ("07:30", "Arrivano permessi da tre cantieri in tre formati diversi.", "Un agente d'ingresso li normalizza in un unico formato controllato."),
        ("09:00", "Confronti i documenti con le regole a mano.", "Un agente delle regole segnala cosa manca. Controlli le segnalazioni, non ogni pagina."),
        ("12:00", "Due cantieri, due fusi orari, un foglio di calcolo che si disallinea.", "Ogni passaggio è registrato. Niente cambia tra i cantieri senza traccia."),
        ("15:00", "Un auditor chiede perché un permesso è stato approvato.", "La traccia c'è: input, regola applicata, chi ha firmato."),
        ("18:00", "Resti fino a tardi per essere sicuro che nulla sia sfuggito.", "Torni a casa sapendo cosa ha fatto il sistema e perché."),
    ],
    signals=[
        "Mi serve qualcosa di più rigoroso di una chat di cui non mi fido del tutto",
        "Il coordinamento tra cantieri mi mangia ore ogni settimana",
        "Non voglio solo un output. Voglio verificare che sia corretto",
        "Quasi tutti i consigli sull'AI per le aziende sono troppo generici per un lavoro ad alto rischio",
    ],
    outcomes=[
        "Una mappa di quali passaggi si possono automatizzare in sicurezza e quali richiedono un controllo umano",
        "Un primo sistema verificabile e funzionante, non una demo",
        "Un metodo per passare da un pezzo che funziona a un sistema coordinato",
        "La certezza di cosa fa il sistema a ogni passaggio",
    ],
    faq=[
        ("L'AI è sicura per permessi di lavoro e documenti di conformità?", "Può esserlo, se ogni agente ha regole ristrette e ogni risultato viene controllato da una persona prima di valere. L'AI redige e segnala; la persona qualificata approva."),
        ("I team regolamentati dovrebbero usare un'AI sul proprio server?", "Spesso sì, per il controllo dei dati. Gli agenti sul tuo server tengono i documenti fuori dalle app di chat e ti danno un registro completo di cosa è stato eseguito."),
        ("Da dove si parte?", "Da un sottosistema con un input e un controllo chiari, per esempio normalizzare i permessi di cantieri diversi. Lo dimostri, poi colleghi il successivo."),
    ],
)

T["03"] = dict(
    slug="team-marketing", persona="Il Responsabile Marketing <em>Interno</em>", persona_plain="Il Responsabile Marketing Interno",
    sector="Marketing aziendale e produzione creativa", country="Italia",
    h1="Produzione video con l'AI per i team marketing aziendali",
    title="Video con l'AI per i Team Marketing: una Pipeline di Produzione Vera",
    desc="Come un responsabile marketing interno ha costruito una pipeline video AI coerente per una campagna aziendale: schede personaggi e location, piano di regia, consegna reale.",
    roles=["Direttore creativo", "Responsabile contenuti", "Campaign manager"],
    answer="Il video AI sembra professionale quando blocchi personaggi e location prima di generare qualsiasi cosa e segui un piano di regia scritto. Le schede di coerenza e il piano delle inquadrature contano più dello strumento video che scegli.",
    story=[
        "Sei responsabile di ciò che la tua azienda pubblica, e oggi questo include il video. Hai provato gli strumenti video AI e hai sbattuto subito contro il problema: personaggi e luoghi cambiano da un'inquadratura all'altra e niente è all'altezza del marchio.",
        "<strong>La soluzione non è uno strumento migliore. È la disciplina di una produzione vera</strong>: bloccare prima la coerenza di personaggi e location, poi girare con un piano di regia invece che con prompt isolati.",
    ],
    result="Pipeline di produzione completa: sistema di coerenza, piano di regia e un contenuto reale usato in una campagna aziendale a un grande evento di settore.",
    day=[
        ("09:00", "Il brief dice «un video breve per l'evento». Niente troupe, niente budget.", "Scrivi la sceneggiatura con l'AI e la dividi in inquadrature."),
        ("10:30", "In ogni clip la persona è leggermente diversa.", "Le schede di personaggi e location bloccano l'aspetto di tutto."),
        ("13:00", "Provi cinque strumenti e ottieni cinque stili.", "Un piano scritto delle inquadrature va nello strumento più adatto a ciascuna."),
        ("16:00", "Montare le clip sembra amatoriale.", "Movimenti di camera e luci sono pianificati, quindi il montaggio regge."),
        ("18:00", "Ti chiedi se è all'altezza per farlo vedere al CEO.", "Entra nella campagna vera."),
    ],
    signals=[
        "Genero clip, ma metterle insieme in modo coerente è un caos",
        "Personaggi e ambienti cambiano in ogni inquadratura",
        "Mi serve qualcosa all'altezza di una campagna vera",
        "Non vengo dalla produzione. Mi serve un sistema da seguire",
    ],
    outcomes=[
        "Un sistema di coerenza riutilizzabile per personaggi e location",
        "Un piano di regia scritto da dare a qualsiasi strumento video AI",
        "Un confronto tra gli strumenti attuali, per smettere di tirare a indovinare",
        "Un contenuto reale per la campagna, non solo tecniche",
    ],
    faq=[
        ("Come si mantengono coerenti i personaggi nei video AI?", "Prepara prima una scheda di riferimento del personaggio: vista a 360°, primi piani, espressioni, palette e una lista «da non cambiare». Usa i suoi pannelli come immagini di riferimento in ogni prompt."),
        ("Qual è lo strumento video AI migliore per il marketing?", "Cambia ogni pochi mesi. Scegli per inquadratura: alcuni gestiscono meglio le persone, altri i movimenti di camera. È il piano scritto delle inquadrature a tenere coerente il risultato."),
        ("Può farlo chi lavora nel marketing senza esperienza di cinema?", "Sì. Questo percorso è partito senza esperienza di produzione. Il metodo prende i passaggi di una produzione vera e li trasforma in checklist."),
    ],
)

T["04"] = dict(
    slug="freelance-multicliente", persona="Il Freelance <em>Multicliente</em>", persona_plain="Il Freelance Multicliente",
    sector="Servizi freelance", country="Svizzera e altri paesi",
    h1="AI per freelance che lavorano con più clienti",
    title="AI per Freelance con Più Clienti: Report e Amministrazione",
    desc="Come i freelance con più clienti usano l'AI per smettere di rifare a mano gli stessi report e la stessa amministrazione: report dal vivo, fatture e liste clienti.",
    roles=["Consulente", "Freelance", "Assistente virtuale"],
    answer="Un freelance con più clienti ottiene il massimo dall'AI costruendo un unico sistema riutilizzabile attorno al lavoro che ripete ogni mese, come report, fatture e liste clienti, collegato a dati reali invece che al copia e incolla.",
    story=[
        "Segui più clienti insieme e buona parte della settimana se ne va in lavoro che non fa crescere nessuno: lo stesso report rifatto a mano, fatture, liste clienti. Sai che l'AI dovrebbe occuparsene. Non hai avuto il tempo di costruirlo bene.",
        "<strong>La svolta non è uno strumento AI generico. È un sistema costruito sul tuo modo reale di lavorare</strong>, collegato a dati veri e riutilizzato per ogni cliente invece di ripartire da zero ogni mese.",
    ],
    result="Un freelance è passato da un report mensile fatto a mano a un sistema di report interattivo su dati dal vivo, e ha acquisito un nuovo cliente anche grazie a quello. Un altro, in Svizzera, sta trasformando uno strumento di fatturazione fatto da sé per un'attività fitness in agenti che collaborano.",
    day=[
        ("08:30", "Lunedì: cinque clienti vogliono cinque report.", "I report si aggiornano con i dati dal vivo. Tu aggiungi il commento che solo tu puoi scrivere."),
        ("11:00", "Le fatture si fanno una per una da un modello.", "Fatture e liste clienti escono da un solo posto, costruito con l'AI, senza abbonamenti."),
        ("14:00", "Un potenziale cliente chiede come sono i tuoi report.", "Gli mostri il sistema dal vivo. Vende al posto tuo."),
        ("16:00", "L'amministrazione si mangia le ore fatturabili.", "Piccoli agenti fanno il lavoro ripetitivo e si passano il passo successivo."),
        ("18:00", "Più clienti vorrebbe dire più serate.", "Più clienti vuol dire più righe nello stesso sistema."),
    ],
    signals=[
        "Rifaccio lo stesso report ogni mese per clienti diversi",
        "So che l'AI potrebbe velocizzarlo, ma non ho un modo strutturato per costruirlo",
        "I clienti si aspettano report più veloci e più precisi di quanto riesca a fare a mano",
        "Voglio più clienti, non più ore",
    ],
    outcomes=[
        "Un sistema di report riutilizzabile, costruito sul tuo modo di lavorare",
        "Un percorso per collegare dati reali dei clienti invece del copia e incolla",
        "Consegne che i clienti notano e che aiutano a vincere il prossimo",
        "Ore libere ogni mese per lavoro fatturabile",
    ],
    faq=[
        ("Come possono i freelance automatizzare i report con l'AI?", "Scegli il report che rifai più spesso, collegalo alla sua fonte dati e lascia che l'AI generi struttura e grafici. Tieni per te le due o tre righe di analisi vera."),
        ("Posso sostituire un software a pagamento con qualcosa costruito con l'AI?", "Spesso sì, per strumenti semplici come fatture o liste clienti. Prima verifica cosa perdi: backup, regole fiscali e assistenza contano ancora."),
        ("Cosa sono gli agenti che collaborano?", "Piccoli assistenti AI che fanno ciascuno un lavoro, come prenotazioni, fatture o promemoria, e passano il risultato al successivo. Più facili da sistemare di un unico grande assistente."),
    ],
)

T["05"] = dict(
    slug="professionisti-vendite", persona="Il Venditore che Cerca un <em>Vantaggio</em>", persona_plain="Il Venditore che Cerca un Vantaggio",
    sector="Vendite e business development", country="Europa",
    h1="AI per professionisti delle vendite e del business development",
    title="AI per Venditori: Prospecting e Ricerca senza Sembrare un Robot",
    desc="Un flusso AI per account executive, SDR e consulenti: prospecting più mirato, messaggi personalizzati e ricerca prima della call in pochi minuti.",
    roles=["Account executive", "SDR", "Consulente"],
    answer="Chi vende ottiene il massimo dall'AI nella ricerca e nella preparazione: studio degli account, preparazione delle call e prime bozze dei messaggi. La parte umana resta la relazione e il giudizio su cosa dire.",
    story=[
        "Sei bravo nel tuo lavoro. Ma i migliori intorno a te usano l'AI per fare prospecting meglio, personalizzare più in fretta e approfondire di più, e il distacco cresce ogni trimestre.",
        "<strong>Hai l'istinto e le relazioni. Ti mancano gli strumenti giusti sopra.</strong> Non prompt generici: un flusso costruito su come vendi tu.",
    ],
    result="Obiettivo fissato nel percorso: ridurre la ricerca prima di ogni call da 45 minuti a 5.",
    day=[
        ("08:00", "Scorri LinkedIn cercando chi chiamare.", "C'è una lista corta di account con un motivo per chiamare oggi."),
        ("09:30", "Ogni email parte da una pagina bianca.", "Le prime bozze usano dettagli reali dell'account. Tu le rendi tue."),
        ("12:00", "45 minuti di preparazione prima di una call.", "Cinque minuti con una scheda di una pagina: azienda, persona, obiezioni probabili."),
        ("15:00", "Dopo la call gli appunti restano nella tua testa.", "Il riepilogo e i prossimi passi si scrivono da soli nel CRM."),
        ("17:30", "Ti chiedi come faccia il migliore del team.", "Adesso lo sai."),
    ],
    signals=[
        "Voglio usare l'AI per il prospecting senza sembrare un bot",
        "Devo sembrare a mio agio con l'AI agli occhi di clienti e management",
        "I migliori chiudono di più. Voglio sapere esattamente come",
        "Ricerca e preparazione mi prendono troppo tempo",
    ],
    outcomes=[
        "Un flusso di prospecting con l'AI su misura per il tuo modo di vendere",
        "Schemi di prompt per messaggi che non sembrano generati",
        "Un sistema di ricerca pre-call: 5 minuti invece di 45",
        "Un modo per presentare la tua padronanza dell'AI ai clienti",
    ],
    faq=[
        ("Come usano l'AI i venditori senza sembrare robot?", "Usa l'AI per ricerca e struttura, poi scrivi tu la frase d'apertura e la richiesta. I dettagli concreti sulla persona battono qualsiasi modello."),
        ("Qual è il risultato più rapido dell'AI nelle vendite?", "La ricerca prima della call. Una scheda di una pagina su azienda e persona, da fonti pubbliche, è ciò che fa risparmiare più tempo nella prima settimana."),
        ("Mi serve uno strumento AI specifico per le vendite?", "Non per iniziare. Un assistente generico con il profilo del tuo cliente ideale ed esempi delle tue email migliori copre quasi tutto."),
    ],
)

T["06"] = dict(
    slug="cambio-carriera", persona="Chi Cambia <em>Carriera</em>", persona_plain="Chi Cambia Carriera",
    sector="Passaggio tra settori", country="Spagna",
    h1="Coaching di carriera con l'AI per chi cambia settore",
    title="Coaching di Carriera con l'AI: Trasforma un Percorso Vario in una Proposta",
    desc="Come una persona che cambia carriera usa l'AI per una ricerca di lavoro basata sui dati: stipendi, aziende target e posizionamento su tre categorie di ruolo.",
    roles=["Cambio di carriera", "Più settori", "Riposizionamento"],
    answer="Chi cambia carriera può usare l'AI per capire quanto pagano e cosa chiedono i ruoli target, preparare una lista di aziende e riscrivere un percorso vario come un'unica storia chiara. Il valore sta nei dati, non in un CV più bello.",
    story=[
        "Hai fatto un lavoro vero in più di un mondo, e questa varietà è un valore. Nessuno ti ha insegnato a raccontarla, così sembra dispersione invece che una scelta.",
        "<strong>Non è una ritoccata al CV. È costruire una proposta basata sui dati</strong>: cosa pagano e cosa chiedono quei ruoli, e un posizionamento che trasforma il tuo percorso nel tuo vantaggio.",
    ],
    result="Una proposta basata sui dati su tre categorie di ruolo, con stipendi reali di riferimento, liste di aziende target, un sito personale e un posizionamento per ciascuna.",
    day=[
        ("09:00", "Ti candidi a tutto ciò che sembra simile.", "Ti candidi dentro tre categorie definite, con fasce di stipendio reali."),
        ("11:00", "Il tuo CV prova a dire tutto.", "Una versione per categoria racconta un'unica storia chiara."),
        ("14:00", "Arriva un colloquio: hai una sera per prepararti.", "La ricerca con l'AI su azienda e selezionatore è pronta in un'ora."),
        ("17:00", "Ti chiedi se il tuo passato abbia senso per qualcuno.", "Un sito personale lo mostra come un percorso, non come uno zigzag."),
        ("20:00", "Un'altra sera sui siti di annunci.", "Un piano di 30 giorni ti dice cosa fare domani."),
    ],
    signals=[
        "Il mio percorso non sta in una casella e non so spiegarlo come un punto di forza",
        "Non voglio un CV più bello. Voglio una strategia su dove andare",
        "Non so quanto pagano né cosa chiedono davvero questi ruoli",
        "Tutti dicono «usa l'AI» per cercare lavoro, nessuno dice come",
    ],
    outcomes=[
        "Un racconto che trasforma un percorso vario in una storia chiara",
        "Fasce di stipendio e requisiti per le tue categorie target",
        "Una lista di aziende su cui puntare, con contatti caldi",
        "Un piano concreto per i prossimi 30 giorni",
    ],
    faq=[
        ("Come mi aiuta l'AI a cambiare carriera?", "A studiare ruoli e stipendi, collegare la tua esperienza a ciò che chiedono quei ruoli e preparare i colloqui. Accelera la ricerca; la direzione la scegli tu."),
        ("Devo fare un CV diverso per ogni ruolo?", "Sì, uno per categoria. Con l'AI è veloce quando tutto il tuo percorso sta in un progetto da cui può attingere."),
        ("È pensato per chi cerca il primo lavoro?", "No. Funziona meglio per chi ha esperienza vera in più campi e deve spiegare il filo che li unisce."),
    ],
)

T["07"] = dict(
    slug="elettricisti-e-artigiani", persona="Il Titolare di un'Impresa <em>Artigiana</em>", persona_plain="Il Titolare di un'Impresa Artigiana",
    sector="Impianti elettrici", country="Australia",
    h1="AI per elettricisti e imprese artigiane",
    title="AI per Elettricisti e Imprese Artigiane: una Dashboard che Trova Soldi Persi",
    desc="Come un'impresa di impianti elettrici in Australia ha collegato l'AI a gestionale lavori e contabilità per scovare lavori non incassati e contatti mai richiamati.",
    roles=["Titolare", "Direttore generale", "Ufficio"],
    answer="Un'impresa artigiana può collegare l'AI al gestionale dei lavori e alla contabilità per individuare lavori finiti ma non incassati, contatti che nessuno ha seguito e lavori senza note. Il valore sta nel trovare le perdite, non nel contare i lavori.",
    story=[
        "Hai una squadra di tecnici sul campo e un ufficio. I contatti arrivano da email, modulo web e WhatsApp; i lavori stanno nel gestionale, i soldi nella contabilità. Ti accorgi che qualcosa è sfuggito solo quando un cliente si lamenta o manca liquidità.",
        "<strong>Un lavoro può valere più di dieci. Quindi la domanda non è quanti lavori hai fatto.</strong> È quali soldi sono bloccati, quale contatto nessuno ha richiamato e chi nel team ha bisogno di aiuto.",
    ],
    result="Al primo test lo spazio di lavoro AI ha scovato un pagamento scaduto che il titolare non conosceva; il successivo ha trovato un contatto mai lavorato. Un report settimanale dei lavori per le agenzie immobiliari è passato da circa cinque minuti a uno.",
    day=[
        ("06:30", "I tecnici escono. Non sai se ogni lavoro ha le note.", "Il controllo del mattino segnala i lavori senza note prima che partano i furgoni."),
        ("09:00", "Gli ordini di lavoro arrivano come email e PDF.", "Ognuno diventa un lavoro con il tipo di cliente assegnato, così i report tornano."),
        ("12:00", "Qualcuno dice che un cliente non ha pagato. Quale?", "I lavori finiti e non incassati sono in cima alla dashboard."),
        ("15:00", "Un contatto della settimana scorsa si è raffreddato.", "I contatti non lavorati vengono segnalati il giorno stesso."),
        ("21:00", "Controlli di nuovo l'azienda dal telefono.", "Una dashboard, sul telefono, pensata per titolare e direttore."),
    ],
    signals=[
        "Scopro i problemi solo quando un cliente si lamenta",
        "Il gestionale ha tutto, ma non vedo il quadro",
        "Non mi interessa quanti lavori abbiamo fatto. Mi interessa quali hanno reso",
        "Gestisco quasi tutta l'azienda dal telefono",
    ],
    outcomes=[
        "AI collegata al gestionale dei lavori e alla contabilità",
        "Report settimanali salvati per tipo di cliente, in un minuto invece di cinque",
        "Un regolamento di categorie, così i dati smettono di mentire",
        "Una dashboard visiva per titolare e direttore, pensata per il telefono",
    ],
    faq=[
        ("Si può collegare l'AI a ServiceM8 e Xero?", "Sì. In questo caso entrambi sono stati collegati a Claude con connettori ufficiali, quindi i report leggono dati di lavori e contabilità dal vivo invece di esportazioni."),
        ("Cosa dovrebbe tenere d'occhio con l'AI un'impresa artigiana?", "I soldi fermi tra «lavoro fatto» e «incassato», i contatti senza seguito, i lavori senza note e quelli senza tipo di cliente. Il numero di lavori conta meno."),
        ("Mi serve uno sviluppatore?", "Non per iniziare. Connettori e un progetto scritto bene coprono i primi mesi. Automazioni e API arrivano dopo, quando sai quali report usi davvero."),
    ],
)

T["08"] = dict(
    slug="imprese-edili", persona="Il Direttore Operativo di <em>Cantiere</em>", persona_plain="Il Direttore Operativo di Cantiere",
    sector="Facciate e rivestimenti", country="Regno Unito",
    h1="AI per l'operatività edile e i report su salute e sicurezza",
    title="AI per Imprese Edili: Report al CdA, Mancati Infortuni e Sopralluoghi",
    desc="Come il direttore operativo di un'impresa di facciate nel Regno Unito usa l'AI per report al consiglio, mancati infortuni, salute e sicurezza e verbali di sopralluogo.",
    roles=["Direttore operativo", "Responsabile sicurezza", "Capocantiere"],
    answer="Le imprese edili possono usare l'AI per trasformare vocali di cantiere e registri di sicurezza in report scritti, liste di azioni e sintesi per il consiglio. Funziona quando l'AI ha le regole e i modelli dell'azienda, impostati una volta in uno spazio condiviso.",
    story=[
        "Un gruppo più grande è entrato nel capitale della tua azienda e con lui è arrivata la reportistica aziendale: il pacchetto mensile per il consiglio, i registri dei mancati infortuni, i toolbox talk, i report di cantiere. Hai provato a sistemare un solo modulo di mancato infortunio con l'AI e hai perso undici ore e duecento prompt.",
        "<strong>Il problema non era l'impegno. Era ripartire da zero in ogni chat.</strong> Uno spazio di lavoro che conosce già la tua azienda, i tuoi modelli e le tue regole di sicurezza trasforma ogni report in una revisione veloce invece che in una battaglia.",
    ],
    result="Uno spazio AI aziendale è impostato con istruzioni e materiale dei toolbox talk; report al consiglio e sintesi dei thread email sono già operativi. Prossimo passo: il registro mensile di salute e sicurezza trasformato in una sintesi pronta per il consiglio.",
    day=[
        ("07:00", "Tre cantieri, tre liste di problemi, un solo te.", "I vocali del sopralluogo diventano un report scritto e una lista di azioni in Excel."),
        ("10:00", "Un mancato infortunio va registrato come si deve.", "Il modulo si compila dai tuoi appunti, nel formato aziendale."),
        ("13:00", "Un thread di 40 email da capire.", "Una sintesi di una pagina: chi ha deciso cosa, cosa resta aperto."),
        ("16:00", "Scade il report al consiglio. I numeri sono sparsi in più file.", "Il registro mensile di sicurezza diventa la bozza della sintesi."),
        ("19:00", "Scrivi report sul tavolo della cucina.", "Rivedi e invii. Fatto prima di cena."),
    ],
    signals=[
        "È arrivata la reportistica aziendale e nessuno mi ha dato più ore",
        "Ho passato giornate intere a litigare con l'AI per un solo modulo",
        "Non sono un tecnico. Mi serve passo dopo passo",
        "I miei appunti di cantiere non diventano mai report in tempo",
    ],
    outcomes=[
        "Uno spazio AI aziendale che conosce regole, modelli e termini",
        "Dal vocale al report di cantiere più sintesi delle azioni in Excel",
        "Registri di mancati infortuni e toolbox talk nel tuo formato",
        "Un report mensile al consiglio da rivedere invece che da scrivere",
    ],
    faq=[
        ("L'AI può scrivere report di salute e sicurezza in cantiere?", "Può redigerli dai tuoi appunti, nel formato della tua azienda. Una persona competente continua a rivedere e firmare. Il risparmio è nella scrittura e nell'impaginazione."),
        ("Perché l'AI non ha funzionato quando l'ho provata?", "Di solito perché ogni chat ripartiva da zero. Un progetto con modelli, regole ed esempi salvati dà all'AI il contesto che servirebbe a un nuovo collega."),
        ("Devo essere bravo con il computer?", "No. Questo percorso va clic per clic. L'obiettivo è che tu lo usi da solo, non che qualcuno lo faccia al posto tuo."),
    ],
)

T["09"] = dict(
    slug="assistente-ia-per-ceo", persona="Il <em>CEO</em>", persona_plain="Il CEO",
    sector="Direzione aziendale", country="Africa",
    h1="Un assistente AI per CEO",
    title="Assistente AI per CEO: Report Vendite, Presentazioni e un Briefing Quotidiano",
    desc="Come il CEO di un'azienda di 60 persone in Africa usa l'AI come capo di gabinetto: scalette di slide da schizzi a mano, report vendite e monitoraggio dei concorrenti.",
    roles=["CEO", "Amministratore delegato", "Fondatore"],
    answer="Un CEO ottiene il massimo dall'AI come capo di gabinetto personale: uno spazio di lavoro che conosce l'azienda, trasforma schizzi in scalette di slide, sintetizza le vendite e osserva i concorrenti. Il CEO continua a prendere ogni decisione.",
    story=[
        "Guidi un'azienda di circa sessanta persone con una rete commerciale che si muove ogni giorno. Le presentazioni ti mangiano le serate. I numeri di vendita che ricevi dicono cosa è successo, non chi rende né quali prodotti si muovono.",
        "<strong>Non devi imparare a programmare. Ti serve l'AI al centro del modo in cui guidi l'azienda.</strong> Due assistenti, impostati una volta, portano con sé il contesto aziendale così ogni richiesta parte da ciò che sai già.",
    ],
    result="Alla prima lezione il CEO ha creato due assistenti: uno per le presentazioni, che trasforma schizzi di slide fatti a mano in scalette, e un Assistente CEO con il profilo aziendale, il report vendite e la brochure. Prossimo passo: un report vendite quotidiano per venditore e un monitoraggio regionale dei concorrenti.",
    day=[
        ("07:00", "Le vendite di ieri: un totale, non una storia.", "Un briefing: chi ha venduto, cosa si è venduto, cosa chiedere al team."),
        ("09:00", "Presentazione al consiglio stasera. Slide vuote.", "Disegni le slide su carta. L'assistente trasforma la foto in una scaletta."),
        ("12:00", "Un concorrente ha lanciato qualcosa. Lo hai saputo tardi.", "Un monitoraggio settimanale della tua regione e del tuo settore."),
        ("15:00", "Un partner vuole la storia dell'azienda in una pagina.", "L'assistente conosce già profilo e brochure. Una bozza, le tue modifiche."),
        ("20:00", "Di nuovo slide.", "Tempo con la tua famiglia."),
    ],
    signals=[
        "Le presentazioni mi mangiano le serate",
        "I miei report dicono cosa è successo, non perché",
        "Voglio l'AI al centro del mio lavoro senza diventare tecnico",
        "Scopro le mosse dei concorrenti troppo tardi",
    ],
    outcomes=[
        "Un assistente CEO che conosce la tua azienda",
        "Slide dai tuoi schizzi, con la tua struttura",
        "Un report vendite quotidiano più ricco: per persona e per prodotto",
        "Un monitoraggio regolare di concorrenti e settore",
    ],
    faq=[
        ("Come può un CEO usare l'AI ogni giorno?", "Parti dai compiti che ti mangiano le serate, di solito presentazioni e report. Metti il profilo aziendale e i report recenti in un progetto AI, così ogni richiesta parte con il contesto."),
        ("L'AI può trasformare schizzi a mano in slide?", "Sì. Fotografi lo schizzo e un assistente con le tue istruzioni lo trasforma in una scaletta slide per slide con la tua struttura, pronta per la grafica."),
        ("I dati della mia azienda sono al sicuro in un assistente AI?", "Usa un piano business che non addestra sui tuoi dati e limita i file sensibili a ciò che serve a ogni assistente. Lo impostiamo alla prima lezione."),
    ],
)

T["10"] = dict(
    slug="agenti-immobiliari", persona="L'Agente <em>Immobiliare</em>", persona_plain="L'Agente Immobiliare",
    sector="Immobiliare residenziale", country="Emirati Arabi Uniti",
    h1="AI per agenti immobiliari",
    title="AI per Agenti Immobiliari: Sistema i Dati, poi Attiva i Tuoi Contatti",
    desc="Come un agente immobiliare negli Emirati ha sistemato la sincronizzazione di contatti e immobili tra fogli di calcolo e AI, poi ha trasformato 5.000 contatti in un piano marketing.",
    roles=["Agente", "Team leader", "Gestione immobili"],
    answer="Gli agenti immobiliari ottengono il massimo dall'AI quando contatti e immobili sono puliti. Con un CRM leggero su fogli di calcolo collegato a uno spazio AI, il passo successivo è il marketing ai contatti esistenti: brand book, landing page e campagne di messaggi.",
    story=[
        "Il tuo piccolo team lavora con fogli di calcolo e uno spazio AI invece di un CRM. Contatti, immobili e dashboard per la direzione hanno smesso di coincidere e nessuno si fidava più dei numeri.",
        "<strong>Fare marketing a 5.000 contatti non funziona con dati rotti.</strong> Quindi la prima cosa è stata sistemare la sincronizzazione. La seconda è trasformare quei contatti in una campagna che la gente voglia leggere.",
    ],
    result="Dopo la prima sessione la sincronizzazione tra contatti, immobili e dashboard era in gran parte sistemata. L'attenzione si è spostata sul marketing a circa 5.000 contatti esistenti: brand book, landing page e un canale social.",
    day=[
        ("09:00", "Il foglio dei contatti e quello degli immobili non coincidono.", "Un'unica fonte di verità, sincronizzata con lo spazio AI."),
        ("11:00", "Il riepilogo settimanale per la direzione richiede ore.", "Si costruisce dai fogli, con numeri affidabili."),
        ("13:00", "5.000 contatti e nessun piano.", "Contatti divisi tra acquirenti, venditori e inquilini, ognuno con il suo messaggio."),
        ("16:00", "I messaggi non portano da nessuna parte.", "Una landing semplice raccoglie ogni risposta."),
        ("18:00", "Pubblichi quando te ne ricordi.", "Un canale social con un piano."),
    ],
    signals=[
        "I nostri fogli e le dashboard non tornano",
        "Abbiamo migliaia di contatti e non ne facciamo niente",
        "Non voglio pagare un altro strumento",
        "La direzione vuole numeri di cui non mi fido",
    ],
    outcomes=[
        "Sincronizzazione pulita tra contatti, immobili e report",
        "Contatti segmentati con un messaggio per segmento",
        "Un brand book e una landing per le campagne",
        "Una divisione chiara di cosa va all'IT, al marketing e a te",
    ],
    faq=[
        ("Un agente immobiliare può usare l'AI senza CRM?", "Sì, in un team piccolo. Google Sheets più uno spazio AI può funzionare come CRM leggero, purché contatti e immobili restino sincronizzati."),
        ("Come fare marketing ai vecchi contatti?", "Dividili tra acquirenti, venditori e inquilini, scrivi un messaggio utile per ciascun gruppo e porta le persone su una pagina semplice che raccoglie le risposte."),
        ("Qual è la prima sistemazione AI in un'agenzia?", "I dati. Se contatti, immobili e report non coincidono, ogni sintesi dell'AI eredita l'errore."),
    ],
)

T["11"] = dict(
    slug="studi-dentistici", persona="Il Titolare dello Studio <em>Dentistico</em>", persona_plain="Il Titolare dello Studio Dentistico",
    sector="Studio dentistico", country="Stati Uniti",
    h1="AI per titolari di studi dentistici",
    title="AI per Studi Dentistici: Automazione Sicura di Assicurazioni, Procedure e Riunioni",
    desc="Come il titolare di uno studio dentistico negli USA pianifica l'AI per pagamenti assicurativi, rettifiche, procedure e riunioni, partendo da pazienti fittizi e dalla privacy.",
    roles=["Titolare dello studio", "Office manager", "Team leader"],
    answer="Gli studi dentistici possono usare subito l'AI per sintesi delle riunioni, procedure e manuali di formazione. Scrivere nel gestionale, per pagamenti assicurativi o rettifiche, richiede prima un'impostazione sicura: un accordo che copra i dati dei pazienti e test su pazienti fittizi.",
    story=[
        "Hai uno studio di dodici persone che funziona già con un sistema di gestione chiaro: riunioni settimanali, scorecard, obiettivi. Usi l'AI in chat. Vuoi che entri nel gestionale dello studio per registrare pagamenti assicurativi e rettifiche, senza rischiare i dati dei pazienti né il sistema stesso.",
        "<strong>La regola è semplice: niente tocca pazienti reali finché non funziona su quelli fittizi.</strong> Per questo il primo progetto è una prova con dati inventati, e l'accordo sui dati dei pazienti arriva prima di qualsiasi messa in funzione.",
    ],
    result="Primo progetto concordato: una dashboard di prova con pazienti fittizi per testare in sicurezza l'API del gestionale, mentre lo studio ottiene un accordo sui dati dei pazienti per i suoi strumenti AI.",
    day=[
        ("07:30", "Riunione settimanale del team: appunti in una registrazione che nessuno ascolta.", "Ordine del giorno e sintesi dalla trascrizione, nel tuo formato di riunione."),
        ("10:00", "Pagamenti assicurativi inseriti a mano.", "In programma: l'AI prepara le registrazioni, una persona approva, con un collegamento sicuro."),
        ("13:00", "Un nuovo assunto ha bisogno delle procedure.", "Procedure e manuali di formazione scritti a partire da come lavorate davvero."),
        ("15:00", "I conti scaduti in un report che apri di rado.", "In programma: una sintesi settimanale di scaduti e stato delle pratiche."),
        ("18:00", "Ti chiedi se l'AI sia sicura per uno studio medico.", "Sai cosa tocca i dati dei pazienti e cosa no."),
    ],
    signals=[
        "Voglio l'AI nel gestionale, ma non a scapito dei dati dei pazienti",
        "Riunioni e procedure vivono in registrazioni e nelle teste",
        "Le assicurazioni si mangiano ore di reception",
        "Il mio team non usa ancora l'AI",
    ],
    outcomes=[
        "Una linea chiara tra ciò che l'AI può fare subito e ciò che richiede un accordo sui dati",
        "Una prova su pazienti fittizi prima di toccare dati reali",
        "Ordini del giorno, sintesi, procedure e manuali di formazione",
        "Un piano per coinvolgere il team",
    ],
    faq=[
        ("L'AI è conforme alla HIPAA per uno studio dentistico?", "Dipende dal piano e dall'accordo, non dal modello. Usa un piano business con un accordo firmato per i dati dei pazienti e tieni quei dati fuori dagli strumenti consumer."),
        ("L'AI può registrare pagamenti assicurativi nel gestionale dello studio?", "Tecnicamente sì, tramite l'API del gestionale. Fallo solo dopo i test su pazienti fittizi, con una persona che approva ogni scrittura."),
        ("Per cosa può usare l'AI uno studio oggi, in sicurezza?", "Ordini del giorno e sintesi delle riunioni, procedure, descrizioni dei ruoli e manuali di formazione: tutto ciò che non contiene dati dei pazienti."),
    ],
)

T["12"] = dict(
    slug="software-ospitalita", persona="L'Imprenditrice dell'Ospitalità che Costruisce un <em>SaaS</em>", persona_plain="L'Imprenditrice dell'Ospitalità che Costruisce un SaaS",
    sector="Software gestionale per l'ospitalità", country="Spagna",
    h1="AI per chi lavora nell'ospitalità e costruisce il proprio software",
    title="AI per l'Ospitalità: Costruisci e Possiedi il Tuo Gestionale per Bar",
    desc="Come un'imprenditrice dell'ospitalità in Spagna sta portando la sua app gestionale per bar fuori da una costosa piattaforma no-code e la sta trasformando in un SaaS per altri locali.",
    roles=["Gestione", "Consulente", "Fondatrice"],
    answer="Chi lavora nell'ospitalità può costruire il proprio gestionale con l'AI, ma le piattaforme no-code diventano care man mano che l'uso cresce. La strada tipica è ricostruire un modulo alla volta su uno stack proprio, poi impacchettarlo per altri locali.",
    story=[
        "Gestisci operatività e contabilità di diversi bar e hai costruito un'app per gestirli: finanza, budget, personale, aspetti legali, ordini ai fornitori. Funziona e la usano ogni giorno. Ma la piattaforma no-code su cui gira costa di più ogni mese e la logica si è ingarbugliata.",
        "<strong>L'obiettivo non è solo un hosting più economico. È possedere il prodotto</strong>, perché possa diventare un software che altri bar pagano, insieme all'esperienza che c'è dietro.",
    ],
    result="Una prima app gira già su hosting e database propri, fuori dalla piattaforma no-code. Il piano: dimezzare i costi mensili, ricostruire i moduli uno alla volta e impacchettare un piano base per altri bar.",
    day=[
        ("08:00", "Gli incassi di ieri sera, in tre sistemi.", "Vendite e costi finiscono in un report settimanale per locale."),
        ("11:00", "Ogni responsabile chiede i suoi numeri.", "Ogni responsabile vede solo il suo locale. Tu vedi tutto."),
        ("14:00", "Arriva la fattura del no-code.", "I moduli passano al tuo stack, uno alla volta."),
        ("17:00", "Un altro titolare di bar chiede cosa usate.", "C'è una versione che puoi vendergli."),
        ("23:00", "Servizio. Il telefono vibra di domande.", "L'app risponde a quelle di routine."),
    ],
    signals=[
        "La mia app no-code funziona, ma la fattura continua a salire",
        "La ricostruirei se sapessi da dove iniziare",
        "Altri locali vogliono quello che abbiamo noi",
        "I dati economici dei clienti devono restare privati",
    ],
    outcomes=[
        "Un piano di migrazione modulo per modulo, non una ricostruzione rischiosa tutta insieme",
        "Hosting e database tuoi",
        "Un piano prodotto che altri locali possono acquistare",
        "Regole di privacy per i dati economici dei clienti",
    ],
    faq=[
        ("Posso costruire un gestionale per bar con l'AI?", "Sì. Un'app funzionante per finanza, personale e ordini è realistica. Pensa presto alla proprietà: hosting, database e permessi di accesso."),
        ("Devo lasciare la mia piattaforma no-code?", "Quando il costo mensile e la logica ingarbugliata pesano più della velocità. Sposta un modulo alla volta, così i locali non si fermano mai."),
        ("Come trasformo uno strumento interno in un SaaS?", "Parti dal modulo che gli altri locali chiedono di più, metti un prezzo a un piano base e tieni la tua consulenza come livello premium."),
    ],
)

T["13"] = dict(
    slug="commercialisti", persona="La <em>Commercialista</em>", persona_plain="La Commercialista",
    sector="Contabilità e revisione", country="Europa",
    h1="AI per commercialisti che costruiscono i propri strumenti di revisione",
    title="AI per Commercialisti: dal Copia e Incolla di Prompt al Tuo Software di Revisione",
    desc="Come una commercialista europea sta passando dall'incollare prompt tra strumenti AI a costruire un MVP strutturato del proprio software di revisione contabile.",
    roles=["Commercialista", "Revisore", "Titolare di studio"],
    answer="I commercialisti possono usare l'AI per costruire i propri strumenti, come checklist di revisione e controlli sulle anomalie, senza essere programmatori. Il passo decisivo è passare dal copiare prompt tra chat a un progetto strutturato con un MVP chiaro.",
    story=[
        "Vuoi passare meno tempo sulla routine e più sui nuovi clienti. Hai già costruito uno strumento desktop funzionante per la revisione contabile scrivendo prompt in un'AI e incollandoli in un'altra.",
        "<strong>Funziona, ma non scala.</strong> Il passo successivo è la struttura: un unico posto per la logica, un MVP definito e un'AI che segnala le anomalie mentre tu firmi la revisione.",
    ],
    result="Le prime lezioni definiscono l'obiettivo del software e la struttura dell'MVP, così lo strumento cresce con un disegno invece che a forza di copia e incolla.",
    day=[
        ("09:00", "Mastrini da controllare, riga per riga.", "Lo strumento segnala le anomalie. Tu controlli le segnalazioni."),
        ("11:00", "Un prompt scritto in un'AI e incollato in un'altra.", "Un progetto raccoglie logica, versioni e test."),
        ("14:00", "Un cliente fa la stessa domanda di routine per la terza volta.", "Una risposta preparata e controllata da te."),
        ("16:00", "Nessun tempo per i nuovi clienti.", "La routine si riduce. Crescono le ore per i nuovi clienti."),
        ("18:00", "Il tuo software vive su un solo PC.", "Un MVP che puoi mostrare e migliorare."),
    ],
    signals=[
        "Ho costruito qualcosa con l'AI, ma sta in piedi a forza di copia e incolla",
        "Voglio passare dall'usare l'AI come un collega a costruire con il codice",
        "La routine non mi lascia tempo per nuovi clienti",
        "Firma il professionista, non l'AI",
    ],
    outcomes=[
        "Un MVP chiaro per il tuo software",
        "Un progetto strutturato invece di prompt incollati",
        "Un'AI che segnala e tu che approvi",
        "Un percorso dallo strumento desktop al prodotto",
    ],
    faq=[
        ("I commercialisti possono creare software con l'AI senza programmare?", "Sì, fino a uno strumento funzionante. Conta più la struttura del codice: un obiettivo definito, un MVP e un progetto dove vive la logica."),
        ("L'AI può fare una revisione contabile?", "No. Può segnalare anomalie e preparare le carte di lavoro. Il commercialista rivede e firma."),
        ("Cos'è un MVP per uno strumento di revisione?", "La versione più piccola che esegue un controllo dall'inizio alla fine su file reali, per esempio la quadratura del mastro con gli estratti conto."),
    ],
)
