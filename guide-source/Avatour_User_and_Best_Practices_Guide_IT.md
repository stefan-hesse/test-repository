# Guida Utente e Buone Pratiche di Avatour

## 1. Per Tutti gli Utenti Avatour {#for-all-avatour-users}

Se sei nuovo su Avatour, le seguenti risorse forniscono un'utile introduzione alla piattaforma e alle sue funzionalità:

1. [Video "Come Funziona Avatour"](https://avatour.com/how-it-works) 
   Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma consente la collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs) 
   Risposte alle domande frequenti
3. [Glossario](https://avatour.com/glossary) 
   Definizioni dei principali termini e concetti di Avatour.
4. Sito Web
   Consulta la pagina [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate ai Casi d'Uso e ai Settori per scoprire come Avatour può supportare le tue esigenze specifiche.

## 2. Tipi di Utenti Avatour

### 2.1 Partecipanti alla Riunione (Nessun Account Richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi a un account Avatour.
Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare l'accesso per autenticarsi.

Gli utenti accedono alla riunione come segue:
- Ricevono un invito del calendario dall'host.
- Utilizzano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'host ne ha abilitata una.
- I partecipanti possono unirsi senza un account Avatour a meno che la riunione non sia limitata e richieda l'accesso per autenticarsi.

#### 2.1.1 Partecipante 

- Può partecipare e interagire pienamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, usare un microfono, presentare, riprodurre/mettere in pausa gli Asset o acquisire Snapshot.
- Massimo 10 Spettatori per riunione.
- Insieme ai Partecipanti, una riunione può ospitare fino a 30 partecipanti.

## 2.2 Utenti Registrati

Gli Utenti Registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitato dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di iscrizione** per completare la configurazione dell'account e impostare una password.  
- **Invitato dall'Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce all'utente un accesso di livello Host.  
- **Provisioning automatico SSO (solo livello Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account con provisioning SSO vengono aggiunti al **gruppo Guest**, a meno che non vengano sovrascritti tramite **mappature di gruppo SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza a un gruppo direttamente anche quando SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in più modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).  
- **Provisioning SSO:** Per i clienti di livello Enterprise o Business con SSO abilitato, l'IdP può effettuare automaticamente il provisioning degli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo dell'utente sulla piattaforma.  
- **Utenti invitati dall'Host:** Gli Host possono invitare altri utenti come collaboratori Editor a Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Buona Pratica Consigliata (Clienti Enterprise):**  
Per le organizzazioni che si aspettano un gran numero di utenti che necessitano di accesso ad Avatour, si consiglia di **integrare il Single Sign-On (SSO)** e gestire utenti e appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione ai gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo degli accessi coerente.

---

### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.  
- Possono **visualizzare gli Asset** nei Workspace in cui sono stati aggiunti come **collaboratori Viewer**.  
- Non possono creare workspace, ospitare riunioni o caricare contenuti.  
- Gli account Guest con provisioning SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

### 2.2.2 Utenti con Licenza (Accesso alla Web Console)

#### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori a un workspace, **ospitare riunioni live**, caricare **Quick Capture**.  
- Hanno accesso alla **Dashboard Host** e all'**App Operatore** sulle telecamere 360° supportate.  

#### Utenti Admin (Gruppo: Admin)

- Include tutte le funzionalità Host più l'amministrazione completa dell'account.

**Privilegi Admin aggiuntivi includono:**

**Gestione Account**  
- Creare nuovi utenti e assegnarli a gruppi.
- Reimpostare le password quando gestite da Avatour (non applicabile quando SSO è abilitato). 
- Aggiornare gli utenti Guest a Host.  
- Disattivare gli utenti (gli account Admin devono prima essere convertiti in Host prima dell'eliminazione).  
- Trasferire gli asset da un utente Host a un altro durante l'eliminazione.

**Impostazioni**  
- Configurare le **impostazioni di sicurezza a livello di organizzazione** per asset, workspace e riunioni ospitate sulla piattaforma (ad esempio, se un Host deve essere presente per avviare una riunione, se i volti devono essere oscurati su tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare le **funzionalità AI** o la **registrazione**.  
- Applicare il branding aziendale in modo coerente sulla piattaforma se è configurato un **dominio personalizzato**.

**Asset e Analytics**  
- Visualizzare tutti gli Asset caricati da qualsiasi utente nell'organizzazione.  
- Rivedere l'utilizzo della piattaforma in tutta l'organizzazione.

---

### 2.2.3 Permessi dei Collaboratori del Workspace

I permessi del Workspace definiscono cosa può fare un utente **all'interno di un Workspace specifico**. Questi sono separati dall'appartenenza al gruppo a livello di piattaforma (Guest, Host, Admin).

- **Collaboratore Editor:** Gli utenti con questo permesso possono:
  - Gestire gli Asset (caricare, rimuovere, oscurare i volti, generare riepiloghi)  
  - Gestire le impostazioni della riunione (abilitare/disabilitare la registrazione, consentire o rimuovere partecipanti)  
  - Pianificare e ospitare riunioni live  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dal Workspace  

- **Collaboratore Viewer:** Gli utenti con questo permesso hanno accesso in sola lettura agli Asset del Workspace. **Non possono modificare gli Asset, gestire le riunioni o gestire i collaboratori**, ma **possono creare Note sugli Asset**. 
  
## 3. Per i Partecipanti alle Riunioni Remote e i Visitatori del Workspace {#for-remote-meeting-participants-and-workspace-visitors}

Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione live:**  
  Potresti ricevere un **invito del calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita al sito remoto in tempo reale** o rivedere gli asset insieme in modo sincrono.

- **Visitare un Workspace:**  
  Potresti anche essere invitato come **collaboratore a un Workspace** per rivedere gli asset **in modo asincrono** (secondo il tuo programma).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare un Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### Qualsiasi Dispositivo "Flat Screen" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

> **Nota:** Per partecipare a una riunione Avatour è necessario **concedere i permessi al microfono**. Accetta le richieste di autorizzazione dal tuo browser.

1. **Tramite invito del calendario (consigliato):**  
   - Di solito riceverai un **invito del calendario** con un **link diretto per partecipare** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando sul link verrà automaticamente inserito il **codice riunione a 5 caratteri** e si accederà alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono limitate agli utenti registrati. In questo caso, l'invito indicherà che è necessario **effettuare l'accesso per partecipare alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'host condivide separatamente un **codice riunione a 5 caratteri**, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione** e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.  
   - Se la riunione richiede **autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio, Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o il microfono, poi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se non riesci ancora a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il **firewall aziendale o la rete** blocca l'accesso e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando si **trasmette una riunione live da una telecamera Insta360**, poiché queste telecamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone come supporto.

### Visitare un Workspace Senza Partecipare a una Riunione

Puoi accedere a un Workspace senza partecipare a una riunione live nei seguenti modi:

- **Workspace Pubblico:**  
  Se il Workspace è pubblico, è possibile accedere direttamente al link senza necessità di accesso.

- **Workspace Limitato:**  
  Se il Workspace è limitato, devi essere aggiunto come **collaboratore** con permessi **Editor** o **Viewer**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica via email** con un link al Workspace.
  2. Clicca sul link nell'email per aprire il Workspace. Se non hai già effettuato l'accesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, il Workspace si aprirà automaticamente.

  In alternativa, puoi accedere su  
  https://avatour.live/login  
  e accedere al Workspace dal tuo **elenco di Workspace**.

#### Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare un workspace da una serie di visori Meta e Pico compatibili. Per farlo: 

1. Installa la nostra app Avatour dal rispettivo store di app VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona un Workspace per partecipare a una riunione. Per ulteriori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite al sito live o revisione di asset registrati insieme.  
2. **Workspace (asincroni):** Rivedi e interagisci con gli asset secondo il tuo programma, 24/7.

Gli **strumenti di collaborazione sono principalmente simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata attorno a tre aree principali:

- **Pannello sinistro** – Asset del Workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video live o asset  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu in basso**.  
Cliccando su un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
### 3.2.2 Esempio di Vista Riunione

Ecco un esempio di vista in una Riunione Avatour:

![Avatour Meeting UI with Assets Panel, blank Canvas and Participants Panel](https://res.cloudinary.com/avatour/image/upload/v1772362400/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

### 3.2.3 Esempio di Vista Workspace

Ecco un esempio di vista Workspace:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Riunioni (destra)*

---

### 3.2.4 Panoramica del Menu in Basso

Il menu in basso fornisce accesso ai principali controlli dell'interfaccia e ai pannelli:

**Menu in Basso della Riunione**  

![Avatour Meeting Bottom Menu](https://res.cloudinary.com/avatour/image/upload/v1772300383/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu in Basso della Riunione Avatour*

- **Asset** – Rivedi i file del workspace, inclusi video registrati, immagini, snapshot e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti alla riunione.  
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Silenzia o riattiva te stesso.  
- **Presenta** – Presenta un asset, il desktop o il feed della webcam (vedi la sezione Presenta di seguito).  
- **Strumenti Host** (solo host):  
  - **Blocca Focus** – Blocca la visualizzazione per tutti i partecipanti.  
  - **Silenzia Tutti** – Silenzia tutti i partecipanti.  
- **Attiva Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Lascia la riunione.  
- **Avvia Registrazione** – Utilizza questo pulsante per avviare e interrompere manualmente la registrazione durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se la **registrazione automatica** è abilitata nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate negli asset del workspace.
- **Mappa** – Apri o chiudi il pannello della mappa per gli asset con una traccia GPS. Cliccando su una posizione si passa al punto esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Partecipanti** – Apri o chiudi il pannello dei partecipanti.  
- **Info Riunione** – Visualizza il codice della riunione, il link di invito e accedi ai tutorial correlati.  

![Avatour Meeting Info](https://res.cloudinary.com/avatour/image/upload/v1772547439/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Informazioni Riunione Avatour*

- **Impostazioni** – Regola le impostazioni di lingua, audio e video. Per le riunioni video live 360°, usa **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

**Menu Presenta**

**Fotocamera** - Consente di condividere la tua webcam o la fotocamera dello smartphone/tablet. Può essere utilizzata anche come Video-nel-Video durante la presentazione di un asset o in una riunione video live 360°, ad esempio per mostrare un dettaglio in loco (anche se avvicinarsi con la telecamera 360° fornisce anche una buona visione dettagliata, ad esempio di un codice a barre, di una scritta piccola su un'etichetta).

**Desktop** - Consente di condividere lo schermo del tuo desktop

**Asset** - Mostra uno degli asset dalla sezione asset - vedi sopra. Durante la presentazione di un asset apparirà il menu Asset - vedi il punto successivo.



**Menu Asset Presenta** 

Ci sono lievi differenze nelle voci del Menu quando si presenta un Asset in una <u>Riunione</u> e quando si presenta in un <u>Workspace</u> (asincrono).

Ecco gli strumenti e le voci del menu disponibili quando si <u>presenta un Asset in una Riunione</u> - spiegati da sinistra a destra.

![Avatour Menu while Presenting an Asset in a Meeting](https://res.cloudinary.com/avatour/image/upload/v1772303706/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour durante la presentazione di un Asset in una Riunione*

**Snapshot** - Scatta una foto 360° o 2D all'interno di una Live Capture o di un Asset presentato. Tutti gli snapshot possono essere salvati negli Asset della riunione/workspace. Uno snapshot 360° SuperFreeze ha una risoluzione più elevata (ca. 6k) e interromperà il live stream per alcuni secondi.

**Spotlight** - Disponibile durante una live capture 360 o se viene presentato un Asset. Questo crea un puntatore visibile da tutti i partecipanti alla riunione e dall'operatore della telecamera, consentendo di attirare l'attenzione del gruppo su un oggetto o un'area specifica sullo schermo.

**Mostra/Nascondi Punto di Vista (POV)** - Questa opzione mostra il focus di ciascun partecipante - Punto di Vista - nel video 360° - registrato o live (cerchi con il nome del partecipante sottostante)

**Note** - crea note (= caselle di dialogo) in determinate posizioni negli snapshot e nei video registrati. Qualsiasi partecipante alla riunione può creare una nota. Solo il creatore della nota può modificare ed eliminare una nota. Quando si crea una nota, è possibile impostare un Tipo: Osservazione, Problema, Azione o Raccomandazione (gli ultimi tre possono essere eseguiti solo da Host, Viewer e Editor Collaboratori Avatour). 

![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/v1772374822/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

Questo chiarisce se una nota è informativa o richiede un follow-up. Nella timeline di un video le note sono ancorate al momento preciso nella registrazione.

I collaboratori principali (Host, Viewer e Editor Collaboratori Avatour) possono aggiornare lo Stato di una nota man mano che il lavoro avanza: Aperto → In Corso → Risolto.

Puoi condividere un link che porta direttamente alla nota. Copia il link e usalo/incorporalo dove vuoi.

<u>Note Generate da Comandi Vocali</u> - È ora possibile generare note tramite comandi vocali (ad esempio, dicendo "prendi nota") da una traccia audio in qualsiasi video (live/registrato, 360°/2D). I segnaposto vengono mostrati sulla timeline del video e la posizione della nota può essere trascinata nel video nella posizione esatta e ovviamente anche modificata con ulteriori contenuti.

![Avatour Notes - Voice Command Generated](https://res.cloudinary.com/avatour/image/upload/v1772921944/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da Comandi Vocali*

**Pannello Laterale con Note, Riepilogo Esecutivo, Argomenti ecc. e Report** - mostra tutte le note e gli argomenti di un asset in un pannello laterale (clicca sull'icona elenco accanto all'icona nota nel menu sopra). Clicca nel pannello laterale nelle note/argomenti per andare alla nota/argomento nel video. Nel pannello Note puoi applicare filtri alle Note.

![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour durante la presentazione di un Asset in una Riunione*

Gli Argomenti sono evidenziati anche sotto la timeline del video. Gli Argomenti sono generati dall'AI in base all'audio di un asset e possono essere avviati durante il Caricamento dall'app cam Avatour o nella sezione Asset nella Web Console.

![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di un Asset in una Riunione*

Puoi anche stampare un report dell'asset - o scaricarlo come file TXT/CSV...

![Avatour Asset Report Print Menus](https://res.cloudinary.com/avatour/image/upload/v1773496969/avatour-screenshot-asset-report-print-menus_kn0syn.png) *Menu Stampa/Download Report Asset Avatour*

...con tutte le note, gli argomenti ecc. anche una trascrizione completa per un asset e seleziona cosa includere:

![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/v1772376570/avatour-screenshot-asset-report-element-selection_ud8c5k.png) *Menu Selezione Elementi Report Asset Avatour*

**Link di Condivisione** - Condividi link a note e scene specifiche (=angoli di visione) in un video/snapshot tramite email o copia direttamente il link e usalo/incorporalo dove vuoi.

**Sottotitoli (CC)** - Qui puoi attivare la visualizzazione delle trascrizioni testuali sullo schermo durante la presentazione di un video.



Ed ecco gli strumenti di collaborazione e le voci del menu disponibili quando si presenta un Asset in un <u>Workspace</u>. La maggior parte degli strumenti è come in una riunione, ma alcuni mancano poiché hanno senso solo quando altri sono presenti (POV e Spotlight) e alcuni sono disponibili solo nei workspace - principalmente relativi alle operazioni video, spiegati di seguito.

![Avatour Menu while Presenting an Asset outside a meeting, e.g. when visiting a workspace](https://res.cloudinary.com/avatour/image/upload/v1772303705/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour durante la presentazione di un Asset in un Workspace*

**Passi da 10 secondi** - Salta il video in passi da 10 secondi - avanti e indietro.

**Velocità di Riproduzione** - Qui puoi scegliere un fattore di velocità di riproduzione (0.5-2)

**Taglio video (forbici)** - Con le forbici puoi tagliare un video all'inizio e alla fine.



## 4. Per Utenti Host e Admin - Web Console Avatour{#for-registered-users}

Quando accedi al tuo Account Utente Avatour accederai alla Web Console. 

### 4.1 Web Console - Panoramica del Menu Principale

Sul lato sinistro vedrai le seguenti voci del menu.

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/v1772366766/avatour-screenshot-main-menu_qwpthq.png) *Web Console Avatour - Menu Principale*

**Workspace** - I Workspace possono essere configurati per molti scopi (ad esempio siti, progetti, clienti, fornitori) e sono unità organizzative che ti aiutano a lavorare in modo efficiente in un ambiente controllato che comprende i seguenti elementi.

**Asset** - Tutti i tuoi asset (video, immagini, pdf) in un unico posto sotto <u>I Miei Asset</u>. Gli utenti Admin possono vedere tutti gli <u>Asset dell'Account</u> per tutti gli utenti host. Gli <u>Asset Condivisi</u> sono quelli che gli host condividono con tutti gli altri utenti sulla piattaforma Avatour. Qui puoi rinominare gli asset, attivare la sfocatura dei volti e generare argomenti.

**Profilo** - Gestisci la tua lingua e reimposta la tua password.

**Analytics** - Ottieni informazioni sulle sessioni e sull'utilizzo

**Impostazioni** - Solo per Utenti Admin. Gestisci alcune impostazioni generali e personalizza il tuo branding.

**Account** - Solo per Utenti Admin. Gestisci gli utenti e i dispositivi (= telecamere 360° assegnate alla tua istanza della piattaforma Avatour).

**Accesso Dispositivo** - Inserisci qui il numero mostrato sull'app Avatour sulla tua telecamera 360° per accedere come utente sulla telecamera 360°. Puoi anche accedere sulla tua telecamera 360° con l'email e la password del tuo account host Avatour, ma inserire semplicemente il codice dispositivo sulla Web Console Avatour potrebbe essere più comodo.

**Disconnetti** dal tuo account.

 

### 4.2 Web Console - Dettagli per Voce di Menu

### 4.2.1 Workspace

I Workspace possono essere configurati per molti scopi (ad esempio siti, progetti, clienti, fornitori) e sono unità organizzative che ti aiutano a lavorare in modo efficiente in un ambiente controllato. Puoi crearne uno nuovo con il pulsante "Nuovo Workspace" nell'angolo in alto a destra dello schermo.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/v1772360323/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Web Console Avatour - Voce Menu Principale Workspace*

Clicca sulle notifiche (l'icona campanella) per ottenere un riepilogo delle attività in un workspace negli ultimi 7 giorni.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/v1772919758/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Web Console Avatour - Attività Recenti del Workspace*

Puoi accedere a un workspace cliccando su di esso. Ecco una vista della struttura in un workspace.

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace Avatour con Pannello Asset (sinistra), Canvas vuoto (centro) e Pannello Riunioni (destra)*

Ogni workspace comprende i seguenti elementi (spiegati da sinistra a destra).

**Asset** - Gestisci gli asset assegnati a quel workspace 

**Collaboratori** - Gestisci l'accesso al Workspace

- **Viewer** - possono visualizzare gli asset nel workspace. L'aggiunta di un Collaboratore Viewer invierà un invito a diventare un utente Guest Avatour registrato.
- **Editor** - hanno gli stessi diritti dell'Host (proprietario del workspace) e con questo il pieno controllo del workspace. L'aggiunta di un Collaboratore Editor invierà un invito a diventare un utente Host Avatour registrato.

> N.B.: Diversi utenti possono accedere a un workspace contemporaneamente senza "incontrarsi". Questo rende un "workspace" diverso da una "riunione". Oltre all'utilizzo dei ruoli Collaboratore, puoi anche rendere il Workspace Pubblico e concedere l'accesso tramite le varie impostazioni di Accesso alla Riunione - per entrambi vedi di seguito sotto "Impostazioni".

**Report** - Crea un report rispetto alla checklist selezionata nelle impostazioni del workspace in base agli asset del workspace che scegli. Puoi modificare le risposte proposte.

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/v1772924118/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report Workspace Avatour e Selezione Asset*

**Mappa** - Per gli asset con metadati GPS mostra la posizione sulla mappa/immagine satellite.

**Riunioni** - Host e Collaboratori Editor possono organizzare riunioni nel workspace

**Impostazioni**

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/v1772387752/avatour-screenshot-workspace-settings_llcei3.png) *Avatour Impostazioni - Vista Workspace*

**(1) Impostazioni Workspace**

<u>Modello di Report</u> - seleziona un modello di checklist rispetto al quale la nostra AI riporterà in base agli asset del workspace scelti (vedi anche Report sopra)

<u>Abilita Notifiche</u> - Ricevi email di riepilogo giornaliero per notificare ai collaboratori quando Problemi e Azioni delle Note cambiano stato (ad esempio, In Corso → Risolto).

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/v1772804314/Screenshot_2026-03-05_140654_bjk0xk.png) *Notifiche Email - Esempio*

<u>Workspace Pubblico</u> - Il workspace è come un sito web - chiunque abbia il link del workspace può visualizzare tutti gli asset e ha accesso diretto agli asset tramite link agli asset. I link diretti agli asset funzionano solo con l'impostazione Workspace Pubblico (Nota: I non-collaboratori non vedranno le informazioni sulla riunione / il pulsante di partecipazione).

**(2) Impostazioni Riunione**

<u>Autenticazione richiesta</u> - Quando abilitata, i partecipanti devono accedere con il loro account utente Avatour registrato (Guest, Host o Admin) per partecipare alla riunione.

<u>Consenti accesso guest</u> agli asset del workspace

<u>Avvio Automatico Registrazione</u> e Richiedi consenso per le riunioni registrate

<u>Richiedi host</u> - Quando abilitato, l'host deve ammettere ogni partecipante alla riunione e la riunione termina quando l'host se ne va. Quando disabilitato, i partecipanti alla riunione possono avviare/partecipare a una riunione senza un host in qualsiasi momento. 

<u>Consenti accesso spettatore</u> - Quando abilitato, i partecipanti possono utilizzare il codice spettatore per partecipare a una riunione senza microfono o webcam. Gli spettatori usano la chat per comunicare con gli altri nella riunione.

<u>Riunioni protette da password</u> - Quando abilitato, i partecipanti devono inserire una password per partecipare alla riunione che è definita dall'host nelle impostazioni della riunione.

<u>Mostra Domanda sul Risparmio di Viaggio</u> - Chiede se la riunione Avatour consente di risparmiare sui viaggi.

> N.B.: È naturalmente possibile utilizzare le impostazioni di cui sopra in combinazione (ad esempio, non richiedere un host ma una password).

### 4.2.2 Asset

Qui gestisci tutti i tuoi asset (video 360°/2D, immagini e file pdf). Puoi caricare e scaricare asset, allocare asset ai workspace, condividere asset con altri utenti sulla piattaforma Avatour. Puoi anche rinominare gli asset, stampare/scaricare report degli asset, attivare la sfocatura dei volti e la riepilogazione AI. Per modificare un Asset clicca sul nome o selezionalo.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/v1772360326/avatour-screenshot-main-menu-assets_ky5emz.png) *Web Console Avatour - Voce Menu Principale Asset*

### 4.2.3 Profilo

Qui puoi gestire i dettagli del tuo profilo come la tua password.

![Avatour Web Console - Main Menu Item Profile](https://res.cloudinary.com/avatour/image/upload/v1772360324/avatour-screenshot-main-menu-profile_j934va.png) *Web Console Avatour - Voce Menu Principale Profilo*

### 4.2.4 Impostazioni

Questa voce di menu è disponibile solo per gli Utenti Admin. Qui puoi (1) gestire le impostazioni predefinite per il tuo account e persino bloccare tali impostazioni in modo che altri utenti non possano modificarle e (2) personalizzare alcuni elementi di branding (ad esempio il tuo logo. Per ulteriori informazioni vedi [Come aggiungo il branding della mia azienda all'esperienza Avatour?](https://avatour.com/support/how-do-i-add-my-company-branding-to-the-avatour-experience)).

![Avatour Web Console - Main Menu Item Settings (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360321/avatour-screenshot-main-menu-settings-1-of-2_fsaatf.png) *Web Console Avatour - Voce Menu Principale Impostazioni (1 di 2)*

![Avatour Web Console - Main Menu Item Settings (2 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360320/avatour-screenshot-main-menu-settings-2-of-2_qimc09.png) *Web Console Avatour - Voce Menu Principale Impostazioni (2 di 2)*

### 4.2.5 Account

Qui gli Utenti Admin possono gestire gli utenti registrati (host, guest, admin) e i dispositivi di acquisizione (telecamere 360° assegnate alla tua istanza della piattaforma Avatour).

![Avatour Web Console - Main Menu Item Account (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772803328/avatour-screenshot-main-menu-account-1-of-2_oq5amr.png) *Web Console Avatour - Voce Menu Principale Account*

### 4.2.6 Analytics

Questa sezione fornisce informazioni sulle tue riunioni e sui risparmi.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360315/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Web Console Avatour - Voce Menu Principale Analytics (1 di 3)*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360313/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Web Console Avatour - Voce Menu Principale Analytics (2 di 3)*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360312/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Web Console Avatour - Voce Menu Principale Analytics (3 di 3)*

### 4.2.7 Accesso Dispositivo

Utilizza questa sezione per inserire il codice a 6 cifre mostrato sulla tua telecamera 360° (ad esempio quando devi effettuare nuovamente l'accesso o a volte è necessario aggiornare). Questo è un modo più comodo che inserire le credenziali di accesso tramite la piccola tastiera nello schermo della telecamera 360°.

![Avatour Web Console - Main Menu Item Device Login](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-device-login_vlymhj.png) *Web Console Avatour - Voce Menu Principale Accesso Dispositivo*

### 4.2.8 Tutorial

Qui puoi avviare tutorial su determinati argomenti.

![Avatour Web Console - Main Menu Item Tutorials](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-tutorials_nr9hme.png) *Web Console Avatour - Voce Menu Principale Tutorial*

 

## 5. In Loco - **Come Utilizzare il Kit Turnkey Avatour**{#for-camera-operators}

### 5.1 Kit Turnkey Avatour 3.1 [(configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2) 

Assicurarsi di collegare la batteria esterna Ulanzi tra la base del treppiede e il bastone estensibile o montare la telecamera direttamente sul bastone batteria estensibile Telesin. Oltre a (1) estendere la durata totale della batteria da ca. 1 ora (solo batteria della telecamera) a ca. 3 ore, aiuterà anche (2) ad estendere l'altezza della configurazione della telecamera, (3) aggiungere peso al fondo per una migliore stabilità e (4) aiutare a prevenire eventuali surriscaldamenti della telecamera. Si consiglia di utilizzare sempre le batterie esterne sin dall'inizio, specialmente per le riunioni live. 

*Per i modelli di telecamera precedenti vedere Kit 2.1:* [*configurazione Pilot One*](https://avatour.com/quickstart-pilot-one/) *e Kit 3.0* [*configurazione Pilot Pano*](https://avatour.com/quickstart-labpano-pilot-pano/)*)*

- *Kit 2.1: Collega un cavo USB dalla batteria alla porta USB-C dell'hub USB-C. Quindi, collega la telecamera direttamente all'hub.*
- *Kit 3.0 / 3.1: Collega un cavo USB dalla batteria alla telecamera.*
- Solo Kit 3.0 / telecamera Pilot Pano: Installazione del modulo di raffreddamento (accessorio opzionale):
  - *(1) Rimuovi la batteria del Pilot Pano aprendo il pannello laterale ed estraendo la batteria*
  - (2) Inserisci il modulo di raffreddamento al posto della batteria
  - *(3) Collega la batteria esterna Ulanzi al modulo di raffreddamento tramite cavo USB-A a USB-C. Questo cavo sarebbe stato incluso con il modulo di raffreddamento.*

### 5.2 Connettività

<u>**Prima di iniziare:**</u> Per i tour live devi essere connesso a Internet utilizzando (1) un WiFi locale o (2) una rete mobile. Dovresti avere almeno 10 Mbps di banda Uplink e Downlink. Questo consente una larghezza di banda disponibile sufficiente per il live streaming della telecamera a 5 Mbps raccomandati. Puoi comunque trasmettere a larghezze di banda inferiori (1-2 Mbps), che funziona meglio quando sei fermo (vedi anche di seguito e. Buone Pratiche: Durante una Riunione). Per testare la velocità e la qualità della connettività puoi utilizzare i seguenti metodi:

Test in una posizione: Qualsiasi misuratore di velocità già in uso (ad esempio https://www.speedtest.net/)

**Strumenti di test di Avatour (consigliati):**

1. Test in una posizione: Apri https://avatour.live/test da qualsiasi dispositivo in qualsiasi browser (dovrebbe richiedere meno di un minuto) inserisci il tuo indirizzo email e una breve ragione per il test - misura in posizioni diverse in loco. Per la valutazione dei risultati, vedi [Come interpreto i risultati del Test di Rete Avatour?](https://avatour.com/support/how-do-i-interpret-the-results-of-the-avatour-network-test)
2. Test durante la camminata (migliore per verificare l'intero tour!): Test di rete con la nostra app Host Avatour per smartphone (Android: disponibile, iOS: prev. Feb. 2024). Quando si è connessi all'app, selezionare un Workspace e scegliere "Esegui Test di Connettività". Guarda il grafico di connettività mentre cammini attraverso il sito e conferma che la larghezza di banda della rete soddisfa i nostri 10 Mbps consigliati
3. Test durante la camminata (migliore per verificare l'intero tour!): Esegui un test di rete con la tua telecamera Avatour 360°. Accedi all'app Avatour dalla schermata home della telecamera e vai al Menu (le tre linee rosse nell'angolo in alto a destra) Impostazioni → Rete → Test di Connessione. Guarda il grafico di connettività mentre cammini attraverso il sito e conferma che la larghezza di banda della rete soddisfa i nostri 10 Mbps consigliati

**WiFi Locale**: 

> **<u>È fortemente consigliato connettere la telecamera a una rete WiFi locale.</u>**

Se il tuo team IT richiede che l'indirizzo MAC del nostro dispositivo sia nella whitelist, puoi trovare sulle telecamere Pilot l'indirizzo MAC qui: App Impostazioni (schermata home della telecamera) --> Informazioni --> scorri verso il basso fino a Indirizzo WiFi

**Rete Mobile:** Per le aree al di fuori della portata del WiFi locale, collega la telecamera a una rete mobile

<u>Opzione A: Utilizza l'hotspot e la scheda SIM forniti con il kit</u>

**Kit 3.0 / 3.1**: Metti l'hotspot GlocalMe in tasca o tienilo su di te.

- *Nota di risoluzione dei problemi*: Se il tuo hotspot GlocalMe mostra il messaggio "La connessione dati non è abilitata", dovresti verificare che l'hotspot sia configurato per utilizzare la scheda SIM preinstallata anziché una Cloud SIM. Per confermarlo, scorri a destra fino alla terza schermata sull'hotspot, scegli "Gestore SIM Card" e seleziona "SIM Card".
- *Nota di risoluzione dei problemi*: Assicurati anche che la "rete 5G" sia abilitata nel Gestore SIM Card
- *Nota di risoluzione dei problemi*: Se non riesci ancora a connetterti alla rete di un operatore, verifica di avere l'APN corretto selezionato per la tua regione. Consulta l'articolo [qui](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot) per creare/gestire gli APN del tuo hotspot.

***Kit 2.1**: Utilizza l'hotspot collegato con un magnete al bastone estensibile. Puoi connetterti all'hotspot tramite WiFi o connessione ethernet cablata (hotspot all'hub USB-C)*

Si consiglia di utilizzare prima la scheda SIM preinstallata nell'hotspot fornito con il kit. Questa è una scheda SIM "globale" che funziona in oltre 200 paesi, solitamente connettendosi automaticamente a una rete mobile disponibile localmente. Possiamo implementare Profili di Roaming con fornitori di reti mobili preferiti per paese. Dopo ulteriori test sulla connettività e se la qualità della connessione rimane scarsa, si consiglia di procurarsi una propria scheda SIM locale dall'Operatore di Rete Mobile con il segnale più forte nelle tue posizioni.

<u>Opzione B: Utilizza la tua attrezzatura</u> - hotspot (smartphone o dispositivo hotspot dedicato) e scheda dati SIM

**Note Importanti**: 

- Tieni l'hotspot spento mentre sei connesso alla tua rete WiFi locale. Una volta fuori portata di questa rete, connetti la telecamera ai tuoi dati SIM.
- Porta l'hotspot con te idealmente nel taschino della camicia anteriore. Le tasche posteriori, ad esempio dei pantaloni, sono meno ideali perché il tuo corpo blocherà parte del segnale WiFi tra l'hotspot e la telecamera 360°.
- Gli operatori di rete mobile a volte limitano la larghezza di banda senza motivo apparente ("throttling") per gestire la loro rete complessiva. Questo può avere un impatto negativo sull'esperienza Avatour. Contatta il tuo CSM Avatour o il nostro team di supporto ([support@avatour.live](mailto:support@avatour.live)) se pensi che stia accadendo.
- Se si utilizza l'hotspot GlocalMe, puoi trovare il nome WiFi e la password scorrendo una schermata a sinistra. La prima schermata visualizzata può essere ignorata.

**Situazioni di bassa larghezza di banda**

- Registra un video della posizione in anticipo - per i dettagli vedi [Come si registrano e caricano video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app) Questo può poi essere presentato durante la tua riunione.
- L'operatore o altri membri del team in loco possono scegliere di condividere la fotocamera del proprio smartphone per trasmettere in live streaming la posizione. Ciò richiederà solo una larghezza di banda di caricamento della rete di 0,1 - 0,3 Mbps.

**Nessuna connettività** - Solo video registrato - vedi [Come si registrano e caricano video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

### 5.3 Audio

#### Telecamera 360° e Operatore

In linea di principio, puoi collegare qualsiasi dispositivo audio bluetooth incluse le cuffie DPI se supportano il bluetooth.

Se prevedi di ospitare una riunione Avatour in un ambiente esterno o rumoroso, si consiglia di collegare le **cuffie Shokz** fornite nel tuo kit: 

- **Accensione/Spegnimento**: Tieni premuto il pulsante "+" per 3 secondi. Vedrai una luce LED blu quando le cuffie sono accese e una luce LED rossa quando le cuffie sono spente
- **Modalità di Abbinamento Bluetooth**: Mentre le cuffie sono spente, tieni premuto il pulsante "+" per 5 secondi. Una luce LED lampeggerà in blu e rosso quando è in modalità di abbinamento
- **Aumento/Diminuzione Volume**: Usa i pulsanti "+" e "-" per aumentare o diminuire il volume di ascolto

In un ambiente più tranquillo, puoi scegliere di collegare un altoparlante bluetooth, come il **diffusore NoxGear** a clip:

- **Accensione/Spegnimento**: Tieni premuto il pulsante Riproduci/Pausa al centro del dispositivo per 2 secondi
- **Modalità di Abbinamento Bluetooth:** Una volta acceso il dispositivo, entrerà in modalità di abbinamento (LED blu e rosso lampeggianti). Una volta abbinato, mostrerà un LED blu
- **Aumento/Diminuzione Volume**: Usa i pulsanti "+" e "-" per aumentare o diminuire il volume di ascolto

**Kit 3.0 / 3.1:** Puoi abbinare/connettere qualsiasi dispositivo bluetooth dalla schermata home della telecamera tramite l'app Impostazioni. Vai su Impostazioni → Bluetooth.

***Kit 2.1**: Per abbinare/connettere un auricolare/altoparlante bluetooth, è necessario avere prima una connessione cablata tra l'hub USB-C (con dongle bluetooth Jabra) e la telecamera. Se si utilizzano le cuffie Shokz o l'altoparlante NoxGear, si connetteranno non appena vengono accesi.*



#### Altri Partecipanti in Loco

Connettiti alla riunione utilizzando il browser del tuo smartphone/tablet/laptop e utilizza cuffie cablate o wireless (preferibilmente con cancellazione del rumore abilitata). **Tieni presente che ogni smartphone in loco sottrarrà larghezza di banda alla telecamera 360°** e può avere un impatto negativo sulla riunione Avatour per tutti i partecipanti! Pertanto **consigliamo di partecipare in**

- **Modalità In Loco** - Partecipa alla riunione in modalità In Loco quando sei fisicamente presente nella stessa posizione della telecamera 360°. La Modalità In Loco è perfetta per gli utenti che desiderano utilizzare il proprio telefono principalmente per primi piani dettagliati. La Modalità In Loco silenzia il microfono e l'altoparlante per impostazione predefinita per eliminare l'eco audio

  ***Screenshot Modalità In Loco DA FARE !!!***

**Nota Importante**: 

- Assicurarsi di essere silenziati quando non si parla attivamente
- Se possibile, avere lo smartphone connesso a una rete diversa dalla rete della telecamera.



### 5.4 App Telecamera Avatour

Ecco i menu (1) Livello Principale, (2) Impostazioni e (3) Impostazioni Rete.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/v1772918698/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App Telecamera 360° Avatour - 3 Menu*

**Quick Capture** - Per la registrazione video 360° offline. - Per una descrizione dettagliata vedi [Come si registrano e caricano video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Consigliamo di utilizzare un dispositivo audio esterno (collegato tramite bluetooth). N.B. Puoi anche fare video e immagini standard 2D - cambia semplicemente la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata QC.

**Riunione Live** - Per la Videoconferenza live 360°. Vedrai i tuoi workspace e cliccando su uno si avvierà il live streaming video dalla telecamera 360°. Prima di poter partecipare alla riunione con la tua telecamera 360°, devi connettere un dispositivo audio tramite bluetooth. Per una descrizione dettagliata vedi [Come avviare una riunione Live Capture con la tua telecamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando si ospita una riunione Live Capture con la tua telecamera 360°, avrai strumenti di riunione simili disponibili che rispecchiano l'esperienza web. Ecco un link al nostro articolo della Knowledge Base che spiega questi strumenti in modo più dettagliato: [Strumenti App Operatore](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galleria** - Qui trovi tutti i tuoi video e immagini 360° da caricare sulla Web Console Avatour.

**Impostazioni** - In Impostazioni hai le seguenti opzioni:

- **Rete**: Questa opzione ti consente di cambiare la rete WiFi a cui è connessa la telecamera o eseguire un test di connessione di rete per visualizzare il throughput di streaming
- **Live Capture**: Regola le impostazioni di Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti o all'installazione delle lenti protettive della tua telecamera:
  - **Frame Rate Target**: Regola il frame rate per il tuo video Live Capture tra 15 fps, 24 fps e 30 fps. Frame rate più elevati producono un video più fluido, ma richiederanno una maggiore larghezza di banda di caricamento. Predefinito: 15 fps
  - **Bitrate Target**: Ti consente di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il tuo bitrate target tra 1 Mbps e 10 Mbps. Bitrate più elevati risulteranno in una risoluzione video più alta, ma richiederanno una maggiore larghezza di banda di caricamento. Predefinito: 5 Mbps
  - **Ottimizza Movimento**: Questo diminuirà il frame rate video, generando meno carico sulla larghezza di banda di caricamento della rete, e aumenterà il tuo bitrate di streaming. Inoltre, questa opzione aiuta a ridurre il mal di movimento per i partecipanti VR. Predefinito: Disattivato
  - **Lenti Protettive**: Questo influenzerà il modo in cui il video 360° viene assemblato a seconda che le lenti protettive siano state installate sulla tua telecamera. Se non hai lenti protettive, impostalo su "No". Se hai ricevuto un Kit 3.0, hai lenti protettive preinstallate e dovresti impostarlo su "Sì". Predefinito: Sì

- **Quick Capture**: Regola le impostazioni di Quick Capture in base al frame rate video preferito, alla larghezza di banda disponibile per i caricamenti di video registrati o all'installazione delle lenti protettive della tua telecamera. Quick Capture ha una risoluzione fissa di 4k che di solito raggiunge un buon equilibrio tra qualità video e dimensione del file. (Per risoluzioni più elevate puoi utilizzare le app native della telecamera, anche sul PanoX V2, per i dettagli vedi [Come si registrano e caricano video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Frame Rate Target**: Regola il frame rate per le registrazioni video Quick Capture tra 15 fps, 24 fps e 30 fps. Frame rate più elevati producono un video più fluido, ma aumenteranno la dimensione del file video e il tempo di caricamento. Consigliato: 30 fps
  - **Bitrate Target**: Imposta il bitrate target per i caricamenti Quick Capture tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano le velocità di caricamento, ma diminuiranno la qualità video. Consigliato: 20 Mbps
  - **Lenti Protettive**: *Vedi la sezione Lenti Protettive per Live Capture sopra*
- **Informazioni**: Visualizza il numero seriale del dispositivo e la versione del software

**Account** - Per accedere con il tuo account host o admin Avatour.

## 6. Consigli di Buone Pratiche

### 6.1 Primi Usi (Informali) e Familiarizzazione

Per i tuoi primi utilizzi e per familiarizzare con la Web Console Avatour e il Kit Turnkey Avatour, consigliamo i seguenti passaggi:

1. Porta il kit a casa e giocaci con familiari e amici usando la tua connessione internet di casa.
2. Porta il kit in ufficio e connettiti a una rete aziendale (potrebbero emergere problemi aziendali, ad esempio firewall aziendali - ma sai dal passaggio uno che Avatour funziona e questo è un argomento da risolvere dal tuo team IT con l'aiuto di Avatour).
3. Inizia a usare Avatour in loco (fuori dal tuo ufficio) nella sede della riunione a cui i partecipanti remoti di solito dovrebbero recarsi. Potrebbero emergere ulteriori problemi di connettività. Avatour aiuterà in cooperazione con il tuo team IT.
4. Inizia a usare con partecipanti remoti interni ed esterni.

### 6.2 Prima di una Riunione Live con Video 360°

- Consigliamo di fare un tour video 360° registrato prima di qualsiasi tour live se il tempo lo consente per tre ragioni: (1) Avere una soluzione di riserva per il tour live, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour live registrato) e (3) iniziare a creare una libreria di video 360° di tutti i tuoi siti che può essere utile per molti casi d'uso. 
- Tutti i componenti del kit carichi per almeno 90 minuti prima della riunione live. Consigliamo comunque di avere tutti i dispositivi in carica continua quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni ad hoc non pianificate.
- Avere il kit completamente assemblato (1. base treppiede + 2. batteria Ulanzi + 3. bastone estensibile + 4. telecamera 360°).

- Confermare che un Workspace è stato creato per ospitare una riunione live e includere tutti gli Asset pertinenti.

- Invitare tutti i partecipanti alla riunione tramite il tuo Workspace. Questo crea un invito nei calendari di tutti i partecipanti e include il link di invito alla riunione.

- Abbinare e connettere le cuffie bluetooth o l'altoparlante che intendi utilizzare per il tour alla telecamera.

- Tutti gli utenti di smartphone in loco dovrebbero connettersi da una rete diversa da quella della telecamera. Questo ridurrà il carico sulla larghezza di banda della rete della telecamera.

- Se sei solo come operatore della telecamera, porta con te uno smartphone nel caso in cui tu voglia condividere la fotocamera dello smartphone e mostrare dettagli fini.

- Confermare che la telecamera 360° può connettersi al tuo WiFi locale.

- Prima di una riunione Avatour, pianifica il percorso che prenderai attraverso la struttura. Fai una riunione Avatour di prova con la telecamera e controlla che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Questo può essere visto direttamente sullo schermo della telecamera, o come partecipante remoto andando su Impostazioni e attivando Mostra Bitrate.

- Se noti che alcune aree hanno poca o nessuna larghezza di banda, è meglio scattare immagini o fare una registrazione. Queste possono poi essere presentate durante la riunione per la revisione dei partecipanti remoti. Puoi seguire la guida qui che spiega il nostro Quick Capture per la registrazione e il caricamento di video/immagini: [Come si registrano e caricano video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se hai partecipanti remoti che partecipano alla riunione che non hanno mai usato Avatour prima, fornisci loro un breve riepilogo della piattaforma, la sua funzionalità (video live 360°, asset, snapshot, annotazioni, spotlight) e gli strumenti della riunione.

- Puoi iniziare in un'altra soluzione di videoconferenza (ad esempio Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudi completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del tuo dispositivo, causandone la disabilitazione per Avatour. Inoltre, NON eseguire Avatour E un'altra videoconferenza contemporaneamente poiché questo ridurrà la larghezza di banda disponibile.

- Se stai pianificando di utilizzare la telecamera 360° in un ambiente ad alta temperatura, si consiglia di utilizzare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la telecamera si surriscaldi e si spenga automaticamente.

### 6.3 Durante l'Operazione della Telecamera in Loco per una Riunione Live con Video 360°

- Quando si opera la telecamera, assicurarsi di camminare lentamente. Questo aiuta con la qualità video e riduce eventuali tempi di inattività video quando la connessione di rete della telecamera si sposta tra i punti di accesso WiFi.

- Tieni la telecamera davanti a te e sopra il livello degli occhi. Questo consente a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Per i casi in cui la telecamera deve rimanere stabile, usa il treppiede ed estendi la telecamera all'altezza corretta, meglio al livello degli occhi.

- Connetti sempre la telecamera alla tua rete WiFi locale dove possibile. Per le aree senza accesso WiFi, usa l'hotspot fornito. L'hotspot ha una scheda SIM che si connetterà a una rete cellulare affidabile vicino a te. Tieni sempre l'hotspot spento quando non è in uso in interni poiché altrimenti la telecamera 360° potrebbe connettersi all'hotspot il che non vogliamo in interni. Quando sei all'esterno, tieni l'hotspot vicino alla telecamera 360°.

- Quando il bitrate sulla telecamera inizia a scendere sotto i 2 Mbps, cammina più lentamente o fermati completamente finché il segnale non si stabilizza di nuovo. Questo di solito accade quando passi da un punto di accesso WiFi a un altro. 

- Se sai che la connettività e il video cadranno quando ti sposti in una posizione specifica (esempio: spostandoti da un'area di produzione interna a un'area esterna), avvisa i partecipanti remoti in anticipo.

- Se è necessario mostrare qualcosa in alto dettaglio o una scritta piccola, usa il tuo smartphone o quello di un partecipante in loco per partecipare alla riunione e presentare la fotocamera (posteriore) del telefono.

- Se possibile, consigliamo che una persona aggiuntiva sia in loco per aiutare con la condivisione della fotocamera dello smartphone descritta sopra poiché spesso si rivela utile/necessaria.

- Idealmente gli utenti di smartphone in loco dovrebbero partecipare alla riunione (1) in modalità in loco e (2) su una rete diversa da quella che utilizza la telecamera per non sottrarre larghezza di banda di caricamento cruciale alla telecamera 360°.

- Tutti i partecipanti in loco che partecipano dal loro smartphone dovrebbero essere silenziati, a meno che non stiano parlando attivamente.
