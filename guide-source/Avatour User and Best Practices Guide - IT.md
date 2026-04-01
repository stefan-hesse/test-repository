# Avatour User and Best Practices Guide

## 1. Per Tutti gli Utenti Avatour {#for-all-avatour-users}

Se sei nuovo su Avatour, le seguenti risorse forniscono un'utile introduzione alla piattaforma e alle sue funzionalità:

1. [Video Come Funziona Avatour](https://avatour.com/how-it-works)  
Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma consente una collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs)  
Risposte alle domande frequenti.
3. [Glossario](https://avatour.com/glossary)  
Definizioni dei termini e concetti chiave di Avatour utilizzati frequentemente.
4. Sito Web  
Dai un'occhiata in particolare alla pagina [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate ai Casi d'Uso e ai Settori per scoprire come Avatour può supportare le tue esigenze specifiche.## 2. Tipi di Utenti Avatour  {#avatour-user-types}

### 2.1 Partecipanti alle Riunioni (Account non richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi per un account Avatour.
Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare il login per autenticarsi.

Gli utenti accedono alla riunione come segue:

- Ricevono un invito del calendario dall'host.
- Utilizzano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'host ne ha abilitata una.
- I partecipanti possono partecipare senza un account Avatour a meno che la riunione non sia limitata e richieda il login per autenticarsi.

#### 2.1.1 Partecipante 

- Può partecipare e interagire completamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, usare il microfono, presentare, riprodurre/mettere in pausa Asset o acquisire Snapshot.
- Massimo 10 Spettatori per riunione.
- Insieme ai Partecipanti, una riunione può ospitare fino a 30 partecipanti.

### 2.2 Utenti Registrati

Gli Utenti Registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitato dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di registrazione** per completare la configurazione dell'account e impostare una password.  
- **Invitato dall'Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce che l'utente abbia accesso di livello Host.  
- **Auto-provisioning SSO (solo tier Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account provisionati tramite SSO vengono aggiunti al **gruppo Guest**, a meno che non sia sovrascritto tramite **mappature dei gruppi SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza ai gruppi direttamente anche quando SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in diversi modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).  
- **Provisioning SSO:** Per i clienti tier Enterprise o Business con SSO abilitato, l'IdP può provisionare automaticamente gli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo dell'utente sulla piattaforma.  
- **Utenti invitati dall'Host:** Gli Host possono invitare altri utenti come collaboratori Editor in Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Best Practice Raccomandata (Clienti Enterprise):**  
Per le organizzazioni che prevedono un gran numero di utenti che necessitano accesso ad Avatour, si raccomanda di **integrare il Single Sign-On (SSO)** e gestire gli utenti e le appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione dei gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo degli accessi coerente.

#### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.  
- Possono **visualizzare Asset** all'interno dei Workspace dove sono stati aggiunti come **collaboratori Viewer**.  
- Non possono creare workspace, ospitare riunioni o caricare contenuti.  
- Gli account Guest provisionati tramite SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

#### 2.2.2 Utenti con Licenza (Accesso alla Console Web)

##### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori a un workspace, **ospitare riunioni live**, caricare **Quick Capture**.  
- Hanno accesso alla **Dashboard Host** e all'**App Operator** sulle fotocamere 360° supportate.  

##### Utenti Admin (Gruppo: Admin)

- Include tutte le funzionalità Host più l'amministrazione completa dell'account.

**I privilegi Admin aggiuntivi includono:**

**Gestione Account**  

- Creare nuovi utenti e assegnarli a gruppi.
- Reimpostare le password quando gestite da Avatour (non applicabile quando SSO è abilitato). 
- Aggiornare utenti Guest a Host.  
- Disattivare utenti (gli account Admin devono prima essere convertiti in Host prima della cancellazione).  
- Trasferire asset da un utente Host a un altro durante la cancellazione.

**Impostazioni**  

- Configurare le **impostazioni di sicurezza a livello organizzazione** per asset, workspace e riunioni ospitate sulla piattaforma (ad es., se un Host deve essere presente per avviare una riunione, se i volti devono essere sfocati su tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare le **funzionalità AI** o la **registrazione**.  
- Applicare il branding aziendale in modo coerente su tutta la piattaforma se è configurato un **dominio personalizzato**.
  

**Asset e Analytics** 
 
- Visualizzare tutti gli Asset caricati da qualsiasi utente nell'organizzazione.  
- Esaminare l'utilizzo della piattaforma in tutta l'organizzazione.

---

#### 2.2.3 Permessi dei Collaboratori del Workspace

I permessi del Workspace definiscono cosa un utente può fare **all'interno di un Workspace specifico**. Questi sono separati dall'appartenenza ai gruppi a livello di piattaforma (Guest, Host, Admin).

- **Collaboratore Editor:** Gli utenti con questo permesso possono:
  - Gestire Asset (caricare, rimuovere, sfocare volti, generare riassunti)  
  - Gestire le impostazioni delle riunioni (abilitare/disabilitare la registrazione, consentire o rimuovere partecipanti)  
  - Pianificare e ospitare riunioni live  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dal Workspace  

- **Collaboratore Viewer:** Gli utenti con questo permesso hanno accesso in sola lettura agli Asset del Workspace. **Non possono modificare Asset, gestire riunioni o gestire collaboratori**, ma **possono creare Note sugli Asset**.## 3. Per i Partecipanti a Riunioni da Remoto e i Visitatori dei Workspace {#for-remote-meeting-participants-and-workspace-visitors}

Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito sul calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota in tempo reale al sito** o rivedere gli asset insieme in modo sincrono.

- **Visitare un Workspace (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore in un Workspace** per rivedere gli asset **in modo asincrono** (secondo i tuoi tempi).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare un Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo "Schermo Piatto" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

##### Partecipare a una Riunione Avatour

> **Nota:** Partecipare a una riunione Avatour richiede che tu **conceda i permessi per il microfono**. Accetta eventuali richieste di autorizzazione dal tuo browser.

1. **Tramite invito sul calendario (consigliato):**  
   - Riceverai generalmente un **invito sul calendario** con un **link diretto per partecipare** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando il link verrà automaticamente inserito il **codice riunione di 5 caratteri** e verrai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono limitate agli utenti registrati. In questo caso, l'invito indicherà che devi **effettuare il login per accedere alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'host condivide un **codice riunione di 5 caratteri** separatamente, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.  
   - Se la riunione richiede **l'autenticazione**, dovrai **effettuare il login con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio, Microsoft Teams o Zoom). Chiudi qualsiasi app che potrebbe utilizzare la tua fotocamera o il microfono, quindi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se ancora non riesci a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la rete** sta bloccando l'accesso, e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando si **trasmette una riunione in diretta da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone di supporto.

##### Visitare un Workspace Avatour (senza partecipare a una Riunione Avatour)

Puoi accedere a un Workspace nei seguenti modi:

- **Workspace Pubblico:**  
  Se il Workspace è pubblico, il link può essere accessibile direttamente—non è richiesto il login.

- **Workspace con Restrizioni:**  
  Se il Workspace è con restrizioni, devi essere aggiunto come **collaboratore** con permessi di **Editor** o **Visualizzatore**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica email** con un link al Workspace.
  2. Clicca il link nell'email per aprire il Workspace. Se non hai già effettuato il login, ti verrà chiesto di **effettuare il login o completare la registrazione**.
  3. Una volta effettuato il login, il Workspace si aprirà automaticamente.

  In alternativa, puoi effettuare il login su [https://avatour.live/login](https://avatour.live/login) e accedere al Workspace dalla tua **lista di Workspace**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare un workspace da una gamma di visori Meta e Pico compatibili. Per farlo: 

1. Installa la nostra app Avatour dal rispettivo store di app VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona un Workspace per partecipare a una riunione. Per maggiori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo nella Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite in diretta al sito o revisione insieme di asset registrati.  
2. **Workspace (asincroni):** Rivedi e interagisci con gli asset secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata attorno a tre aree principali:

- **Pannello sinistro** – Asset del workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video in diretta o asset  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu in basso**.  
Cliccando un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Vista Riunione

Ecco un esempio di vista in una Riunione Avatour:

![Interfaccia Riunione Avatour con Pannello Asset, Canvas vuoto e Pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Vista Workspace

Ecco un esempio di vista Workspace:

![Workspace Avatour con Pannello Asset, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del Menu in Basso

Il menu in basso fornisce accesso ai principali controlli dell'interfaccia e ai pannelli:

**Menu in Basso della Riunione**  

![Menu in Basso Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu in Basso Riunione Avatour*

- **Asset** – Rivedi i file del workspace, inclusi video registrati, immagini, istantanee e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti alla riunione.  
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Silenzia o riattiva te stesso.  
- **Presenta** – Presenta un asset, il desktop o il feed della webcam (vedi sezione Presenta sotto).  
- **Strumenti Host** (solo per gli host):  
  - **Blocca Focus** – Blocca la vista per tutti i partecipanti.  
  - **Silenzia Tutti** – Silenzia tutti i partecipanti.  
- **Abilita Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Lascia la riunione.  
- **Avvia Registrazione** – Usa questo pulsante per avviare e interrompere manualmente la registrazione durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se l'**avvio automatico della registrazione** è abilitato nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate negli asset del workspace.
- **Mappa** – Apri o chiudi il pannello mappa per gli asset con traccia GPS. Cliccando una posizione si salta al punto esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Partecipanti** – Apri o chiudi il pannello partecipanti.  
- **Info Riunione** – Visualizza il codice riunione, il link di invito e accedi ai tutorial correlati.  

![Info Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Info Riunione Avatour*

- **Impostazioni** – Regola le impostazioni di lingua, audio e video. Per le riunioni video in diretta a 360°, usa **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un evento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu in basso della riunione ti consente di condividere contenuti con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Questo può essere utilizzato anche durante una riunione video in diretta a 360° per sovrapporre una vista secondaria per primi piani o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Asset** – Presenta un asset dal workspace. Selezionando un asset si apre la **Barra degli strumenti Asset**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per l'asset presentato.

##### Barra degli Strumenti Asset (Riunione)

Quando presenti un asset in una riunione, la **Barra degli Strumenti Asset** appare sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>presenti un Asset in una Riunione</u> - spiegati da sinistra a destra.

![Menu Avatour durante la Presentazione di un Asset in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour durante la presentazione di un Asset in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.   
- **Istantanea** – Cattura un'immagine a 360° o 2D dall'asset.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni in diretta.  
- **Mostra/Nascondi Punto di Vista (POV)** – Mostra dove ogni partecipante sta guardando nel video a 360°.  
- **Note** – Crea note ancorate a momenti specifici nell'asset. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperta → In Corso → Risolta) e condivise tramite link diretti.  

  ![Nota Avatour e Filtro Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

  - **Note da Comando Vocale** – Questi sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note Avatour - Generate da Comando Vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da Comando Vocale*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che mostra tutte le note, gli argomenti chiave e un riepilogo esecutivo per l'asset. Cliccando un elemento si salta a quel momento nel video.  

  ![Riepilogo Esecutivo Asset Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour durante la presentazione di un Asset in una Riunione*

  ![Argomenti Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di un Asset in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report dell'asset** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati dall'IA e trascrizioni complete. Puoi anche **scegliere quali## 4. Per Utenti Host e Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}

Quando accedi al tuo Account Utente Avatour, accederai alla **Console Web**.  

### 4.1 Console Web - Panoramica Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai le seguenti voci di menu:

![Console Web Avatour - Menu Principale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principale*

- **Workspace** – Organizza i tuoi contenuti in modo efficiente. Ogni workspace contiene **Asset**, **Collaboratori**, **Meeting** e **Impostazioni**.  
- **Asset** – Accedi e gestisci tutti i tuoi asset (video, immagini, PDF). Gli admin possono visualizzare tutti gli asset dell'account, e gli asset condivisi sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analytics** – Monitora l'attività delle sessioni, l'utilizzo dei workspace e le metriche ROI.  
- **Impostazioni** *(Solo Admin)* – Configura le impostazioni predefinite di workspace, meeting e asset in tutta l'organizzazione. Gli admin possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo Admin)* – Gestisci gli utenti registrati e le videocamere 360°.  
- **Login Dispositivo** – Inserisci il codice visualizzato sulla tua videocamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Login Dispositivo, Tutorial ed Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---

### 4.2 Console Web - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Workspace

I workspace sono unità organizzative flessibili che ti permettono di gestire asset, collaboratori e meeting in un unico posto. Puoi creare un nuovo workspace con il pulsante **Nuovo Workspace** nell'angolo in alto a destra.

![Console Web Avatour - Voce Menu Principale Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Voce Menu Principale Workspace*

Clicca sull'icona della campana per vedere un riepilogo dell'attività del workspace negli ultimi 7 giorni.

![Console Web Avatour - Attività Recenti Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti Workspace*

All'interno di un workspace:

![Workspace Avatour con Pannello Asset, Canvas vuoto e Pannello Meeting](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace con Asset (sinistra), Canvas (centro), Meeting (destra)*

- **Asset** – Gestisci i file allocati a questo workspace.  
- **Collaboratori** – 
  Controlla l'accesso ai workspace tramite 
  - **Visualizzatore** – Può visualizzare gli asset. L'invito crea un utente Ospite se necessario.  
  - **Editor** – Controllo completo del workspace, stessi diritti dell'Host. L'invito aggiorna l'utente a Host se necessario.  
> Più utenti possono accedere a un workspace contemporaneamente senza un meeting. I workspace pubblici e le impostazioni di accesso ai meeting forniscono accesso alternativo.  
- **Report** – Genera un report utilizzando un modello di checklist sugli asset del workspace selezionati.  

![Report Workspace Avatour e Selezione Asset](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report Workspace e Selezione Asset*

- **Mappa** – Visualizza le posizioni degli asset abilitati GPS su una mappa.  
- **Meeting** – Organizza meeting nel workspace.  
- **Impostazioni** – Configura le impostazioni predefinite del workspace e dei meeting:

![Impostazioni Avatour - Vista Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni Workspace*

**Impostazioni Workspace**

- **Modello Report** – Seleziona il modello di checklist per il reporting AI.  
- **Abilita Notifiche** – Email di riepilogo giornaliero per le modifiche di stato delle note.  

![Notifiche Email - Esempio](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio Notifiche Email*

- **Workspace Pubblico** – Chiunque abbia il link può visualizzare gli asset direttamente.

**Impostazioni Meeting**
  
* **Autenticazione richiesta** – I partecipanti devono effettuare l'accesso.  
* **Consenti accesso ospiti** – Permetti agli utenti non registrati di visualizzare gli asset.  
* **Registrazione Automatica / Avvio Manuale** – Scegli se i meeting vengono registrati automaticamente o avviati manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; il meeting termina quando l'host esce.  
* **Consenti accesso spettatore** – Partecipa senza microfono o videocamera; comunica tramite chat.  
* **Meeting protetti da password** – Richiedi una password per partecipare.  
* **Mostra Domanda Risparmio Viaggi** – Chiedi ai partecipanti se il meeting ha ridotto i viaggi.  

> Le impostazioni possono essere combinate (es., nessun host richiesto ma protetto da password).

---

#### 4.2.2 Asset

Gestisci tutti i video 360°/2D, immagini e PDF. Carica/scarica asset, alloca ai workspace, condividi con altri utenti, rinomina, stampa/scarica report, attiva la sfocatura volti e il riepilogo AI.

![Console Web Avatour - Voce Menu Principale Asset](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Asset*

---

#### 4.2.3 Analytics

Fornisce approfondimenti su meeting, utilizzo dei workspace e metriche ROI.

![Console Web Avatour - Voce Menu Principale Analytics (1 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analytics*

![Console Web Avatour - Voce Menu Principale Analytics (2 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Meeting e Utilizzo Workspace*

![Console Web Avatour - Voce Menu Principale Analytics (3 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenze Dispositivo e ROI*## 5. In loco - Come Utilizzare il Kit Chiavi in Mano Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Per Iniziare
[Guida Rapida – Kit Chiavi in Mano Avatour 3.1 (configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per disimballare, assemblare e accendere la tua videocamera.

---

### 5.2 Consigli Utili

#### Batteria Esterna – Meeting Live più Lunghi e Miglior Gestione Termica

- **Se il tuo kit include una batteria Ulanzi:** Fissala tra la base del treppiede e l'asta estensibile, quindi collega la batteria alla videocamera tramite USB-C.

- **Se il tuo kit include un'asta batteria Telesin:** Monta la videocamera direttamente sull'asta batteria estensibile Telesin e collegala tramite USB-C.

Utilizzare la batteria esterna:

1. Estende la durata totale della batteria da ~40 minuti (solo batteria della videocamera) a ~3 ore.
2. Aggiunge stabilità alla configurazione della videocamera.
3. Aiuta a prevenire potenziali surriscaldamenti.

> Raccomandiamo di utilizzare sempre la batteria esterna fin dall'inizio, specialmente per i meeting live.

#### Considerazioni Audio per Meeting Live e Registrazioni

- **Ambienti rumorosi:**
  Usa le cuffie Shokz incluse nel tuo kit per una cattura audio chiara.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).
  - **Modalità Accoppiamento Bluetooth:** Con le cuffie spente, tieni premuto il pulsante "+" per 5 secondi (il LED lampeggia blu/rosso).
  - **Volume:** Usa i pulsanti "+" e "-".

- **Ambienti più silenziosi / più partecipanti vicino alla videocamera:**
  Usa l'altoparlante clip-on NoxGear. Non è ad alta fedeltà come gli altoparlanti da conferenza (es. Jabra Speak), ma è facile da agganciare alla camicia e cattura efficacemente le voci vicine.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Play/Pausa per 2 secondi.
  - **Modalità Accoppiamento Bluetooth:** Entra automaticamente in modalità accoppiamento all'accensione (il LED lampeggia blu/rosso; blu fisso quando accoppiato).
  - **Volume:** Usa i pulsanti "+" e "-".

- **Utilizzo del proprio dispositivo:** Se preferisci un'alternativa (es. un altoparlante da conferenza o cuffie personali), puoi accoppiarlo tramite la videocamera: Impostazioni → Bluetooth.

#### Connettività, Connettività, Connettività
**Prima di iniziare:** Assicurati della connessione internet tramite:

- **WiFi Locale** (preferito)
- **Rete Mobile** (se fuori dalla copertura WiFi)

**Larghezza di banda raccomandata:** 10 Mbps uplink/downlink per lo streaming completo a 360° (~5 Mbps). Una larghezza di banda inferiore (1–2 Mbps) funziona solo restando fermi.

##### Test della Velocità di Rete
- **Test in singola posizione:** Qualsiasi strumento di speed test che usi normalmente (es. [Speedtest](https://www.speedtest.net)) per verificare la larghezza di banda in upload.
- **Test in movimento attraverso il sito:** Dalla videocamera: Impostazioni → Rete → Test di Connessione. Cammina attraverso l'intero spazio per confermare copertura e larghezza di banda.

##### WiFi Locale
- Altamente raccomandato per connessioni stabili.
- Se l'IT richiede la whitelist, trova l'indirizzo MAC: Impostazioni → Info → Indirizzo WiFi.

##### Rete Mobile
**Opzione A: Hotspot e SIM forniti nel kit**

- Fissa l'hotspot GlocalMe all'asta batteria Telesin (magnete).
- Garantisce nessuna interferenza e mantiene la connessione se ci si allontana dalla videocamera.
- Risoluzione problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).
  - Abilita il 5G nel Gestore Scheda SIM.
  - Verifica l'APN corretto per la tua regione ([guida configurazione APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Usa il tuo smartphone o hotspot dedicato.

**Nota Importante:**
> Tieni l'hotspot spento mentre sei connesso al WiFi; abilitalo solo quando sei fuori copertura. Il sistema operativo della videocamera passa dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe passare inavvertitamente all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili possono limitare la larghezza di banda in modo imprevisto. Verifica con il tuo operatore i limiti del piano dati, o contatta il supporto Avatour se utilizzi il nostro hotspot e SIM.

##### Situazioni di Bassa Larghezza di Banda
- Pre-registra video delle location per la riproduzione successiva ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Condividi uno stream della fotocamera dello smartphone per integrare le aree a bassa larghezza di banda (0,1–0,3 Mbps in upload).

##### Nessuna Connettività
- È possibile utilizzare solo video pre-registrati ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri Partecipanti in Loco – Best Practice

Quando più partecipanti si uniscono a un meeting Avatour live dalla stessa posizione della videocamera a 360°, è cruciale una gestione attenta di **audio e larghezza di banda**:

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della videocamera a 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza del meeting sgradevole per tutti i partecipanti.

#### Altri Partecipanti in Loco – Best Practice

Quando più partecipanti si uniscono a un meeting Avatour live dalla stessa posizione della videocamera a 360°, è cruciale una gestione attenta di **audio e larghezza di banda**:

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della videocamera a 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza del meeting sgradevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **best practice**:

- **Usa cuffie cablate o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.
- **Modalità In Loco:** Unisciti al meeting in modalità In Loco quando sei fisicamente presente vicino alla videocamera a 360°.
  - Questa modalità è ottimizzata per l'uso in loco:
    - Silenzia il microfono e l'altoparlante del partecipante per impostazione predefinita.
    - **Non** invia il feed della videocamera del partecipante.
    - **Non** mostra il feed della videocamera a 360° nel browser del partecipante.
    - Conserva la larghezza di banda di rete, garantendo alla videocamera a 360° il massimo upload disponibile per lo streaming live.
    - Utile quando un utente vuole condividere dettagli specifici; **puoi condividere la tua videocamera** per visualizzazioni mirate.
- **Silenzia quando non stai parlando attivamente:** Previene feedback audio indesiderati e distrazioni.
- **Usa una rete separata se possibile:** Connetti il tuo smartphone a una rete diversa da quella della videocamera per ridurre le interferenze.

Seguire queste linee guida garantisce un tour live fluido e di alta qualità sia per i partecipanti in loco che per quelli remoti.

### 5.3 App Videocamera Avatour

Ecco (1) il Livello Principale, (2) Impostazioni e (3) i menu delle Impostazioni di Rete.

![App Videocamera Avatour 360° - Tre Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App Videocamera Avatour 360° - 3 Menu*

**Quick Capture** - Per la registrazione video a 360° offline. - Per una descrizione dettagliata vedi [Come registri e carichi video a 360° con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Raccomandiamo l'uso di un dispositivo audio esterno (connesso via bluetooth). N.B. Puoi anche fare video e foto 2D standard - cambia semplicemente la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata QC.

**Live Meeting** - Per videoconferenze live a 360°. Vedrai i tuoi workspace e cliccando su uno di essi avvierai lo stream video live dalla videocamera a 360°. Prima di poter unirti al meeting con la tua videocamera a 360° devi connettere un dispositivo audio via bluetooth. Per una descrizione dettagliata vedi [Come avviare un meeting Live Capture con la tua videocamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando ospiti un meeting Live Capture con la tua videocamera a 360°, avrai a disposizione strumenti di meeting simili che rispecchiano l'esperienza web. Ecco un link al nostro articolo della Knowledge Base che spiega questi strumenti in maggior dettaglio: [Strumenti App Operatore](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galleria** - Qui trovi tutti i tuoi video e foto a 360° per il caricamento sulla Console Web Avatour.

**Impostazioni** - All'interno di Impostazioni, hai le seguenti opzioni:

- **Rete**: Questa opzione ti permette di cambiare la rete WiFi a cui è connessa la videocamera o eseguire un test di connessione di rete per visualizzare il throughput di streaming
- **Live Capture**: Regola le tue impostazioni Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti, o se sono installate le lenti protettive della videocamera:
  - **Frame Rate Target**: Regola il frame rate per il tuo video Live Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma richiederanno più larghezza di banda in upload. Predefinito: 15 fps
  - **Bitrate Target**: Ti permette di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il tuo bitrate target tra 1 Mbps e 10 Mbps. Bitrate più alti risulteranno in una risoluzione video più alta, ma richiederanno più larghezza di banda in upload. Predefinito: 5 Mbps
  - **Ottimizza Movimento**: Questo diminuirà il frame rate video, generando meno carico sulla larghezza di banda in upload della tua rete, e aumenterà il tuo bitrate di streaming. Inoltre, questa opzione aiuta a ridurre il motion sickness per i partecipanti VR. Predefinito: Disattivato
  - **Lenti Protettive**: Questo influenzerà come il video a 360° viene unito a seconda che le lenti protettive siano state installate sulla tua videocamera. Se non hai lenti protettive, imposta su "No". Se hai ricevuto un Kit 3.0, hai lenti protettive preinstallate e dovresti impostare su "Sì". Predefinito: Sì

- **Quick Capture**: Regola le tue impostazioni Quick Capture in base al frame rate video preferito, alla larghezza di banda disponibile per i caricamenti video registrati, o se sono installate le lenti protettive della videocamera. Quick Capture ha una risoluzione fissa di 4k che di solito offre un buon equilibrio tra qualità video e dimensione del file. (Per risoluzioni più alte puoi usare le app native della videocamera, anche sulla PanoX V2, per dettagli vedi [Come registri e carichi video a 360° con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Frame Rate Target**: Regola il frame rate per le tue registrazioni video Quick Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma aumenteranno la dimensione del file video e il tempo di caricamento. Raccomandato: 30 fps
  - **Bitrate Target**: Imposta il bitrate target per i caricamenti Quick Capture tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano la velocità di caricamento, ma diminuiranno la qualità video. Raccomandato: 20 Mbps
  - **Lenti Protettive**: *Vedi sezione Lenti Protettive per Live Capture sopra*
- **Info**: Visualizza il numero di serie del dispositivo e la versione del software

**Account** - Per l'accesso con il tuo account host o admin Avatour.## 6. Consigli sulle Migliori Pratiche {#best-practice-advice}

### 6.1 Primi Utilizzi (informali) e Familiarizzazione

Per i primi utilizzi e per familiarizzare con la Console Web Avatour e il Kit Chiavi in Mano Avatour raccomandiamo i seguenti passaggi:

1. Porta il kit a casa e provalo con familiari e amici utilizzando la tua connessione internet domestica.
2. Porta il kit in ufficio e connettiti a una rete aziendale (potrebbero emergere problematiche aziendali, ad es. firewall aziendali - ma sai dal primo passaggio che Avatour funziona e questo è un argomento da risolvere con il tuo team IT con l'aiuto di Avatour).
3. Inizia a utilizzare Avatour sul campo (fuori dal tuo ufficio) nel luogo della riunione verso cui i partecipanti remoti dovrebbero normalmente viaggiare. Potrebbero emergere ulteriori problematiche di connettività. Avatour può aiutare in collaborazione con il tuo team IT.
4. Inizia a utilizzarlo con partecipanti remoti interni ed esterni.

### 6.2 Prima di una Riunione Live con Video a 360°

- Raccomandiamo di effettuare un tour video a 360° registrato prima di qualsiasi tour live, se il tempo lo consente, per tre motivi: (1) Avere una soluzione di riserva per il tour live, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour live registrato) e (3) iniziare a creare una libreria di video a 360° di tutti i tuoi siti che può essere utile per molti casi d'uso.
- Tutti i componenti del kit devono essere caricati per almeno 90 minuti prima della riunione live. Raccomandiamo comunque di tenere tutti i dispositivi in carica continua quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni improvvisate non pianificate.
- Tieni il kit completamente assemblato (1. base del treppiede + 2. batteria Ulanzi + 3. asta estensibile + 4. cam a 360°).

- Conferma che sia stato creato uno Spazio di Lavoro per ospitare una riunione live e includi tutte le Risorse pertinenti.

- Invita tutti i partecipanti alla riunione attraverso il tuo Spazio di Lavoro. Questo crea un invito nei calendari di tutti i partecipanti e include il link di invito alla riunione.

- Associa e connetti le tue cuffie bluetooth o l'altoparlante che intendi utilizzare per il tour alla fotocamera.

- Tutti gli utenti smartphone in loco dovrebbero connettersi da una rete diversa da quella della fotocamera. Questo ridurrà il carico sulla larghezza di banda della rete della fotocamera.

- Se sei solo come operatore della fotocamera, porta con te uno smartphone nel caso tu voglia condividere la fotocamera dello smartphone e mostrare dettagli fini.

- Conferma che la fotocamera a 360° possa connettersi al tuo WiFi locale.

- Prima di una riunione Avatour, pianifica il percorso che farai attraverso la struttura. Fai una riunione Avatour di prova con la fotocamera e verifica che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Questo può essere visualizzato sullo schermo della fotocamera stessa, o come partecipante remoto andando in Impostazioni e attivando Mostra Bitrate.

- Se noti che alcune aree hanno poca o nessuna larghezza di banda, è meglio scattare immagini o effettuare una registrazione. Queste possono poi essere presentate durante la riunione per la revisione dei partecipanti remoti. Puoi seguire la guida qui che spiega la nostra Cattura Rapida per registrare e caricare video/immagini: [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se hai partecipanti remoti che si uniscono alla riunione e non hanno mai usato Avatour prima, fornisci loro un breve riepilogo della piattaforma, delle sue funzionalità (video live a 360°, risorse, istantanee, annotazioni, spotlight) e degli strumenti di riunione.

- Puoi iniziare in un'altra soluzione di videoconferenza (ad es. Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudi completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del tuo dispositivo, causando la loro disabilitazione per Avatour. Inoltre, NON eseguire Avatour E un'altra videoconferenza contemporaneamente poiché questo ridurrà la larghezza di banda disponibile.

- Se hai intenzione di utilizzare la fotocamera a 360° in un ambiente ad alta temperatura, si raccomanda di utilizzare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la fotocamera si surriscaldi e si spenga automaticamente.

### 6.3 Durante l'Utilizzo della Cam in Loco per una Riunione Live con Video a 360°

- Quando utilizzi la fotocamera, assicurati di camminare lentamente. Questo aiuta con la qualità video e riduce qualsiasi potenziale interruzione video quando la connessione di rete della fotocamera passa tra i punti di accesso WiFi.

- Tieni la fotocamera davanti a te e sopra il livello degli occhi. Questo permette a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Per le situazioni in cui la fotocamera deve rimanere stabile, usa il supporto treppiede ed estendi la fotocamera all'altezza corretta, preferibilmente al livello degli occhi.

- Connetti sempre la fotocamera alla tua rete WiFi locale quando possibile. Per le aree senza accesso WiFi, usa l'hotspot fornito. L'hotspot ha una scheda SIM che si connetterà a una rete cellulare affidabile vicino a te. Tieni sempre l'hotspot spento quando non in uso all'interno poiché altrimenti la cam a 360° potrebbe connettersi all'hotspot, cosa che non vogliamo negli ambienti interni. Quando sei all'esterno, tieni l'hotspot vicino alla fotocamera a 360°.

- Quando il bitrate sulla fotocamera inizia a scendere sotto i 2 Mbps, cammina più lentamente o fermati completamente finché il segnale non si stabilizza di nuovo. Questo accade solitamente quando passi da un Punto di Accesso WiFi a un altro.

- Se sai che la connettività e il video si interromperanno quando ti sposti in una posizione specifica (Esempio: spostandoti da un'area di produzione interna a un'area esterna), avvisa i partecipanti remoti in anticipo.

- Se hai bisogno di mostrare qualcosa in alta definizione o scritte piccole, usa il tuo smartphone o quello di un partecipante in loco per unirti alla riunione e presentare la fotocamera (posteriore) del tuo/loro telefono.

- Se possibile raccomandiamo che una persona aggiuntiva sia in loco per aiutare con la condivisione della fotocamera smartphone sopra descritta poiché questo spesso si rivela utile/necessario.

- Idealmente gli utenti smartphone in loco dovrebbero unirsi alla riunione (1) in modalità in loco e (2) su una rete diversa da quella che sta usando la fotocamera per non sottrarre larghezza di banda di upload cruciale dalla cam a 360°.

- Tutti i partecipanti in loco che si uniscono dal loro smartphone dovrebbero essere silenziati, a meno che non stiano parlando attivamente.