# Avatour User and Best Practices Guide

## 1. Per Tutti gli Utenti di Avatour {#for-all-avatour-users}
Se sei nuovo ad Avatour, le seguenti risorse forniscono un'introduzione utile alla piattaforma e alle sue capacità:

1. [Video Avatour How it Works](https://avatour.com/how-it-works)  
Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma abilita la collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs)  
Risposte alle domande frequenti.
3. [Glossario](https://avatour.com/glossary)  
Definizioni di termini e concetti chiave di Avatour usati frequentemente.
4. Sito web  
Dai un'occhiata soprattutto alla pagina [Avatour Features](https://avatour.com/features) insieme alle sezioni dedicate Use Cases e Industries per scoprire come Avatour può supportare le tue esigenze specifiche.## 2. Tipi di Utenti Avatour  {#avatour-user-types}

### 2.1 Partecipanti alla riunione (nessun account richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi per un account Avatour.
Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare l'accesso per autenticarsi.

Gli utenti accedono alla riunione come segue:

- Ricevono un invito del calendario dall'host.
- Utilizzano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'host ne ha abilitata una.
- I partecipanti possono partecipare senza un account Avatour a meno che la riunione non sia limitata e richieda l'accesso per autenticarsi.

#### 2.1.1 Partecipante

- Può partecipare e interagire pienamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, utilizzare un microfono, presentare, riprodurre/mettere in pausa gli Asset o acquisire istantanee.
- Massimo 10 spettatori per riunione.
- Insieme ai partecipanti, una riunione può ospitare fino a 30 partecipanti.### 2.2 Utenti Registrati

Gli Utenti Registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invito dell'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di iscrizione** per completare la configurazione dell'account e impostare una password.  
- **Invito dell'Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce che l'utente abbia accesso a livello Host.  
- **Auto-provisioning SSO (solo tier Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account con provisioning SSO vengono aggiunti al **gruppo Guest**, a meno che non venga sovrascritto tramite **mappature gruppi SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza ai gruppi direttamente anche quando SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e l'appartenenza ai gruppi possono essere gestiti in diversi modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).  
- **Provisioning SSO:** Per i clienti con tier Enterprise o Business con SSO abilitato, l'IdP può eseguire automaticamente il provisioning degli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo della piattaforma dell'utente.  
- **Utenti invitati da Host:** Gli Host possono invitare altri utenti come collaboratori Editor per Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Pratica consigliata (Clienti Enterprise):**  
Per le organizzazioni che si aspettano un gran numero di utenti che necessitano di accesso a Avatour, si consiglia di **integrare Single Sign-On (SSO)** e gestire gli utenti e le appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione dei gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo di accesso coerente.

#### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.  
- Possono **visualizzare Asset** all'interno dei Workspace dove sono stati aggiunti come **collaboratori Viewer**.  
- Non possono creare workspace, ospitare riunioni o caricare contenuti.  
- Gli account Guest con provisioning SSO **si autenticano tramite l'IdP**; non è richiesta alcuna password gestita da Avatour.

---

#### 2.2.2 Utenti Licenziati (Accesso alla Console Web)

##### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori a un workspace, **ospitare riunioni dal vivo**, caricare **Quick Captures**.  
- Ha accesso al **Dashboard Host** e all'**App Operatore** su fotocamere 360° supportate.  

##### Utenti Admin (Gruppo: Admin)

- Include tutte le funzionalità Host più l'amministrazione completa dell'account.

**I privilegi Admin aggiuntivi includono:**

**Gestione Account**  

- Creare nuovi utenti e assegnarli a gruppi.
- Ripristinare password quando gestite da Avatour (non applicabile quando SSO è abilitato). 
- Aggiornare utenti Guest a Host.  
- Disattivare utenti (gli account Admin devono prima essere convertiti a Host prima dell'eliminazione).  
- Trasferire asset da un utente Host a un altro durante l'eliminazione.

**Impostazioni**  

- Configurare **impostazioni di sicurezza a livello organizzativo** per asset, workspace e riunioni ospitati sulla piattaforma (ad es., se un Host deve essere presente per avviare una riunione, se i volti devono essere offuscati in tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare **funzionalità AI** o **registrazione**.  
- Applicare il branding aziendale in modo coerente su tutta la piattaforma se è configurato un **dominio personalizzato**.
  

**Asset e Analitiche** 
 
- Visualizzare tutti gli Asset caricati da qualsiasi utente nell'organizzazione.  
- Rivedere l'utilizzo della piattaforma in tutta l'organizzazione.

---

#### 2.2.3 Autorizzazioni dei Collaboratori del Workspace

Le autorizzazioni del Workspace definiscono cosa un utente può fare **all'interno di uno specifico Workspace**. Queste sono separate dall'appartenenza ai gruppi a livello di piattaforma (Guest, Host, Admin).

- **Collaboratore Editor:** Gli utenti con questa autorizzazione possono:
  - Gestire Asset (caricare, rimuovere, offuscare volti, generare riepiloghi)  
  - Gestire le impostazioni delle riunioni (abilitare/disabilitare registrazione, consentire o rimuovere partecipanti)  
  - Programmare e ospitare riunioni dal vivo  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dal Workspace  

- **Collaboratore Viewer:** Gli utenti con questa autorizzazione hanno accesso di sola lettura agli Asset del Workspace. **Non possono modificare Asset, gestire riunioni o gestire collaboratori**, ma **possono creare Note su Asset**.## 3. Per i partecipanti alle riunioni remote e i visitatori dello spazio di lavoro {#for-remote-meeting-participants-and-workspace-visitors}
Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipa a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito del calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita del sito remoto dal vivo** o rivedere gli asset insieme in modo sincrono.

- **Visita uno Spazio di lavoro (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore di uno Spazio di lavoro** per rivedere gli asset **in modo asincrono** (secondo i tuoi tempi).### 3.1 Come partecipare a una riunione Avatour e visitare uno spazio di lavoro Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi dispositivo "Flat Screen" con browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.

##### Partecipazione a una riunione Avatour

> **Nota:** Per partecipare a una riunione Avatour è necessario **concedere i permessi del microfono**. Accetta tutti i prompt di autorizzazione del tuo browser.

1. **Tramite invito del calendario (consigliato):**
   - Riceverai solitamente un **invito del calendario** con un **link di accesso diretto** (ad esempio: `https://avatour.live/join?s=xxxxx`).
   - Facendo clic sul link verranno compilati automaticamente il **codice riunione di 5 caratteri** e accederai alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono riservate agli utenti registrati. In questo caso, l'invito indicherà che devi **accedere per accedere alla riunione**.
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**
   - Se l'host condivide un **codice riunione di 5 caratteri** separatamente, vai a [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.
   - Se la riunione richiede **autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbe essere in uso da un'altra applicazione (ad esempio Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o il tuo microfono, quindi esci e ricollega alla riunione Avatour.

> **Suggerimento 2:** Se non riesci ancora a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).
> Il test può identificare se il tuo **firewall aziendale o rete** sta bloccando l'accesso e fornirà informazioni per guidare le discussioni con il tuo team IT.

> **Suggerimento 3:** **Non** utilizzare le app Avatour iOS o Android per partecipare a riunioni. Queste app sono necessarie solo quando **trasmetti una riunione live da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire il software Avatour 360° direttamente e richiedono uno smartphone per assistere.

##### Visita di uno spazio di lavoro Avatour (senza partecipare a una riunione Avatour)

Puoi accedere a uno spazio di lavoro nei seguenti modi:

- **Spazio di lavoro pubblico:**
  Se lo spazio di lavoro è pubblico, il link può essere accessibile direttamente — non è richiesto il login.

- **Spazio di lavoro con accesso limitato:**
  Se lo spazio di lavoro è con accesso limitato, devi essere aggiunto come **collaboratore** con i permessi **Editor** o **Viewer**.

  1. Quando vengono aggiunti come collaboratore, riceverai una **notifica email** con un link allo spazio di lavoro.
  2. Fai clic sul link nell'email per aprire lo spazio di lavoro. Se non hai già effettuato l'accesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, lo spazio di lavoro si aprirà automaticamente.

  In alternativa, puoi accedere a [https://avatour.live/login](https://avatour.live/login) e accedere allo spazio di lavoro dalla tua **lista di spazi di lavoro**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare uno spazio di lavoro da una serie di visori Meta e Pico compatibili. Per farlo:

1. Installa la nostra app Avatour dal rispettivo app store VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona uno spazio di lavoro per partecipare a una riunione. Per ulteriori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Strumenti di Riunione e Collaborazione in Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite dal vivo del sito o revisione di risorse registrate insieme.  
2. **Workspace (asincrone):** Rivedi e interagisci con le risorse secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono rispetto a quello asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata attorno a tre aree principali:

- **Pannello sinistro** – Risorse workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video dal vivo o risorse  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu in basso**.  
Facendo clic su un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Visualizzazione Riunione

Ecco un esempio di visualizzazione in una Riunione Avatour:

![Avatour Meeting UI con Assets Panel, Canvas vuoto e Participants Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Avatour Meeting con Assets Panel (sinistra), Canvas (centro) e Participants Panel (destra)*

---

#### 3.2.3 Esempio di Visualizzazione Workspace

Ecco un esempio di visualizzazione di un Workspace:

![Avatour Workspace con Assets Panel, Canvas vuoto e Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Avatour Workspace con Assets Panel (sinistra), Canvas (centro) e Meetings Panel (destra)*

---

#### 3.2.4 Panoramica del Menu in Basso

Il menu in basso fornisce l'accesso ai controlli e ai pannelli dell'interfaccia principale:

**Meeting Bottom Menu**  

![Avatour Meeting Bottom Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Avatour Meeting Bottom Menu*

- **Assets** – Rivedi i file del workspace, inclusi video registrati, immagini, istantanee e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti della riunione.  
- **Camera** – Accendi o spegni la webcam.  
- **Microfono** – Attiva o disattiva il microfono.  
- **Present** – Presenta una risorsa, il desktop o il feed della webcam (vedi la sezione Present di seguito).  
- **Host Tools** (solo host):  
  - **Lock Focus** – Blocca la visualizzazione per tutti i partecipanti.  
  - **Mute All** – Silenzia tutti i partecipanti.  
- **Enable Full Screen** – Rendi la scheda della riunione a schermo intero.  
- **Exit Meeting** – Esci dalla riunione.  
- **Start Recording** – Utilizza questo pulsante per avviare e interrompere la registrazione manualmente durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se **auto-start recording** è abilitato nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate nelle risorse del workspace.
- **Map** – Apri o chiudi il pannello della mappa per le risorse con un tracciato GPS. Facendo clic su una posizione vai al momento esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Participants** – Apri o chiudi il pannello dei partecipanti.  
- **Meeting Info** – Visualizza il codice della riunione, il link di invito e accedi ai tutorial correlati.  

![Avatour Meeting Info](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Avatour Meeting Info Side Pane*

- **Settings** – Regola le impostazioni di lingua, audio e video. Per le riunioni video 360° dal vivo, utilizza **Show Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Present

L'opzione **Present** nel menu in basso della riunione ti consente di condividere contenuti con tutti i partecipanti.

- **Camera** – Condividi la fotocamera del tuo smartphone/tablet. Può anche essere utilizzato durante una riunione video 360° dal vivo per sovrapporre una visualizzazione secondaria per zoom o dettagli specifici. 
- **Desktop** – Condividi lo schermo del desktop con tutti i partecipanti.  
- **Asset** – Presenta una risorsa dal workspace. Selezionando una risorsa si apre la **Asset toolbar**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici della risorsa presentata.

##### Asset Toolbar (Riunione)

Quando presenti una risorsa in una riunione, appare la **Asset Toolbar** sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>presenti una Risorsa in una Riunione</u> - spiegati da sinistra a destra.

![Avatour Menu mentre si presenta una Risorsa in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Avatour Menu quando si presenta una Risorsa in una Riunione*


- **Video Timeline / Progress Bar** – Mostra l'avanzamento del video con note e argomenti principali estratti dall'audio. Fai clic su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli di **Play / Pause**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dalla risorsa.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni dal vivo.  
- **Show/Hide Point-of-View (POV)** – Visualizza dove ogni partecipante sta guardando nel video 360°.  
- **Notes** – Crea note ancorate a momenti specifici della risorsa. Le note possono essere categorizzate (Observation, Issue, Action, Recommendation), tracciate per stato (Open → In Progress → Resolved) e condivise tramite link diretti.  

  ![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Avatour Note and Note Filters*

  - **Voice Command Notes** – Questi sono segnaposti generati automaticamente quando la registrazione rileva menzioni come "insert note", "take a note" o "make a note". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Avatour Notes - Voice Command Generated](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Avatour Notes - Voice Command Generated*

- **Notes and Summary Panel** – Apre un pannello laterale che visualizza tutte le note, gli argomenti principali e un riepilogo esecutivo della risorsa. Facendo clic su un elemento vai a quel momento nel video.  

  ![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Avatour Executive Summary mentre si presenta una Risorsa in una Riunione*

  ![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Avatour Topics mentre si presenta una Risorsa in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un rapporto della risorsa** o **scaricarlo come TXT o CSV**. I rapporti possono includere note, argomenti generati dall'AI e trascrizioni complete. Puoi anche **scegliere quali elementi includere** prima di esportare.  

  ![Avatour Asset Report Print Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Avatour Asset Report Print / Download Menus*  

  ![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Avatour Asset Report Element Selection Menu*

- **Share Link** – Condividi un link a una nota specifica o una scena nella risorsa.  
- **Closed Captions (CC)** – Visualizza la trascrizione del testo sullo schermo durante la riproduzione del video.

##### Asset Toolbar (Workspace)

Quando rivedi una risorsa in un workspace, la toolbar è simile ma ottimizzata per l'uso individuale:

![Avatour Menu mentre si presenta una Risorsa fuori da una riunione, ad es. quando si visita un workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Avatour Menu quando si presenta una Risorsa in un Workspace*

- **Video Timeline / Progress Bar** – Mostra l'avanzamento del video con note e argomenti principali estratti dalla traccia audio. Fai clic in qualsiasi punto della timeline per scorrere il video. Fai clic su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli di **Play / Pause**.  
- **Snapshot, Notes, Notes and Summary Panel Panel, Share Link, Closed Captions**  
- Non disponibile: **Spotlight, POV** (questi richiedono partecipanti dal vivo)  
- Controlli aggiuntivi:
  - **10-second steps** – Salta avanti/indietro  
  - **Playback Speed** – Regola la velocità (0,5×–2×)  
  - **Trim Video** – Taglia l'inizio o la fine della risorsa## 4. Per Host e Admin Users - Avatour Web Console {#for-host-and-admin-users-avatour-web-console}
Quando accedi al tuo Account Utente Avatour, accederai alla **Web Console**.### 4.1 Web Console - Panoramica Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai i seguenti elementi del menu:

![Avatour Web Console - Menu Principale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Avatour Web Console - Menu Principale*

- **Workspace** – Organizza i tuoi contenuti in modo efficiente. Ogni workspace contiene **Asset**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Asset** – Accedi e gestisci tutti i tuoi asset (video, immagini, PDF). Gli amministratori possono visualizzare tutti gli asset dell'account e gli asset condivisi sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analytics** – Monitora l'attività della sessione, l'utilizzo del workspace e le metriche del ROI.  
- **Impostazioni** *(Solo amministratore)* – Configura i valori predefiniti di workspace, riunioni e asset in tutta l'organizzazione. Gli amministratori possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo amministratore)* – Gestisci gli utenti registrati e le fotocamere 360°.  
- **Accesso Dispositivo** – Inserisci il codice visualizzato sulla tua fotocamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Accesso Dispositivo, Tutorial e Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---### 4.2 Web Console - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Workspace

Gli workspace sono unità organizzative flessibili che ti permettono di gestire asset, collaboratori e riunioni in un'unica posizione. Puoi creare un nuovo workspace con il pulsante **Nuovo Workspace** nell'angolo in alto a destra.

![Avatour Web Console - Voce di Menu Principale Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Voce di Menu Principale Workspace*

Fai clic sull'icona della campana per visualizzare un riepilogo dell'attività del workspace negli ultimi 7 giorni.

![Avatour Web Console - Attività Recenti Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti Workspace*

All'interno di un workspace:

![Avatour Workspace con Pannello Asset, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace con Asset (sinistra), Canvas (centro), Riunioni (destra)*

- **Asset** – Gestisci i file allocati a questo workspace.  
- **Collaboratori** – 
  Controlla l'accesso ai workspace tramite 
  - **Visualizzatore** – Può visualizzare gli asset. L'invito crea un utente Guest se necessario.  
  - **Editor** – Controllo completo del workspace, stessi diritti dell'Host. L'invito aggiorna l'utente a Host se necessario.  
> Più utenti possono accedere a un workspace contemporaneamente senza una riunione. I workspace pubblici e le impostazioni di accesso alle riunioni forniscono accessi alternativi.  
- **Report** – Genera un report utilizzando un modello di checklist sugli asset del workspace selezionato.  

![Report Workspace e Selezione Asset](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report Workspace e Selezione Asset*

- **Mappa** – Visualizza le posizioni degli asset abilitate da GPS su una mappa.  
- **Riunioni** – Organizza riunioni nel workspace.  
- **Impostazioni** – Configura le impostazioni predefinite del workspace e delle riunioni:

![Avatour Impostazioni - Visualizzazione Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni Workspace*

**Impostazioni Workspace**

- **Modello di Report** – Seleziona il modello di checklist per il reporting AI.  
- **Abilita Notifiche** – Email di riepilogo giornaliero per i cambiamenti dello stato delle note.  

![Notifiche Email - Esempio](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio di Notifiche Email*

- **Workspace Pubblico** – Chiunque disponga del link può visualizzare gli asset direttamente.

**Impostazioni Riunioni**
  
* **Autenticazione richiesta** – I partecipanti devono effettuare l'accesso.  
* **Consenti accesso ospite** – Permetti agli utenti non registrati di visualizzare gli asset.  
* **Registrazione Automatica / Avvio Manuale** – Scegli se le riunioni vengono registrate automaticamente o avviate manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host se ne va.  
* **Consenti accesso spettatore** – Accedi senza microfono o fotocamera; comunica tramite chat.  
* **Riunioni protette da password** – Richiedi una password per partecipare.  
* **Mostra Domanda su Risparmi di Viaggio** – Chiedi ai partecipanti se la riunione ha ridotto i viaggi.  

> Le impostazioni possono essere combinate (ad es. nessun host richiesto ma protette da password).

---

#### 4.2.2 Asset

Gestisci tutti i video 360°/2D, le immagini e i PDF. Carica/scarica asset, allocali ai workspace, condividili con altri utenti, rinominali, stampa/scarica report, attiva la sfocatura del volto e il riassunto AI.

![Avatour Web Console - Voce di Menu Principale Asset](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce di Menu Principale Asset*

---

#### 4.2.3 Analytics

Fornisce informazioni dettagliate sulle riunioni, sull'utilizzo dei workspace e sulle metriche del ROI.

![Avatour Web Console - Voce di Menu Principale Analytics (1 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analytics*

![Avatour Web Console - Voce di Menu Principale Analytics (2 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Riunioni e Utilizzo Workspace*

![Avatour Web Console - Voce di Menu Principale Analytics (3 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenza Dispositivo e ROI*## 5. In Loco - Come Utilizzare il Kit Chiavi in Mano Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Iniziare
[Guida di avvio rapido – Avatour Turnkey Kit 3.1 (Configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per disimballare, assemblare e accendere la fotocamera.

---### 5.2 Suggerimenti Utili

#### Batteria Esterna – Riunioni Più Lunghe e Migliore Dissipazione Termica

- **Se il tuo kit include una batteria Ulanzi:** Collegala tra la base del treppiede e il bastone estensibile, quindi collega la batteria alla fotocamera tramite USB-C.

- **Se il tuo kit include un bastone batteria Telesin:** Monta la fotocamera direttamente sul bastone batteria estensibile Telesin e collegalo tramite USB-C.

Utilizzando la batteria esterna:

1. Estende la durata totale della batteria da ~40 minuti (solo batteria della fotocamera) a ~3 ore.
2. Aggiunge stabilità alla configurazione della fotocamera.
3. Aiuta a prevenire il possibile surriscaldamento.

> Ti consigliamo di utilizzare sempre la batteria esterna da subito, soprattutto per le riunioni in diretta.

#### Considerazioni Audio per Riunioni e Registrazioni in Diretta

- **Ambienti rumorosi:**
  Utilizza le cuffie Shokz incluse nel tuo kit per una chiara acquisizione dell'audio.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).
  - **Modalità Associazione Bluetooth:** Con il cuffia spento, tieni premuto il pulsante "+" per 5 secondi (LED lampeggia blu/rosso).
  - **Volume:** Utilizza i pulsanti "+" e "-".

- **Ambienti più silenziosi / più partecipanti vicino alla fotocamera:**
  Utilizza l'altoparlante clip-on NoxGear. Non è all'altezza di altoparlanti per conferenze (ad es. Jabra Speak), ma è facile da agganciare alla tua maglietta e cattura efficacemente le voci vicine.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Play/Pausa per 2 secondi.
  - **Modalità Associazione Bluetooth:** Entra automaticamente in modalità associazione quando acceso (LED lampeggia blu/rosso; blu fisso quando associato).
  - **Volume:** Utilizza i pulsanti "+" e "-".

- **Utilizzo del tuo dispositivo:** Se preferisci un'alternativa (ad es. un altoparlante per conferenze o un cuffia personale), puoi associarlo tramite la fotocamera: Impostazioni → Bluetooth.

#### Connettività, Connettività, Connettività
**Prima di iniziare:** Assicurati della connessione Internet tramite:

- **WiFi locale** (consigliato)
- **Rete mobile** (se fuori dalla portata del WiFi)

**Larghezza di banda consigliata:** 10 Mbps upload/download per lo streaming 360° completo (~5 Mbps). Una larghezza di banda inferiore (1–2 Mbps) funziona solo quando si è fermi.

##### Test della Velocità di Rete
- **Test a singola posizione:** Qualsiasi controllo di velocità che normalmente usi (ad es. [Speedtest](https://www.speedtest.net)) per verificare sia la larghezza di banda di upload.
- **Test a piedi in tutto il sito:** Dalla fotocamera: Impostazioni → Rete → Test di Connessione. Cammina attraverso l'intero spazio per confermare la copertura e la larghezza di banda.

##### WiFi Locale
- Altamente consigliato per connessioni stabili.
- Se l'IT richiede l'inserimento in whitelist, trova l'indirizzo MAC: Impostazioni → Informazioni → Indirizzo WiFi.

##### Rete Mobile
**Opzione A: Hotspot e SIM forniti dal kit**

- Attacca l'hotspot GlocalMe al bastone batteria Telesin (magnete).
- Assicura l'assenza di interferenze e mantiene la connessione se ci si allontana dalla fotocamera.
- Risoluzione dei problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).
  - Abilita 5G in Gestore Scheda SIM.
  - Verifica l'APN corretto per la tua regione ([guida alla configurazione dell'APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Utilizza il tuo smartphone o hotspot dedicato.

**Nota Importante:**
> Mantieni l'hotspot spento durante la connessione al WiFi; abilitalo solo quando fuori portata. Il sistema operativo della fotocamera cambia dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe involontariamente passare all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili possono limitare inaspettatamente la larghezza di banda. Contatta il tuo operatore per i limiti del piano dati, o contatta l'assistenza Avatour se utilizzi il nostro hotspot e la nostra SIM.

##### Situazioni di Scarsa Larghezza di Banda
- Pre-registra video della posizione per la riproduzione successiva ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Condividi uno streaming della fotocamera dello smartphone per integrare le aree a bassa larghezza di banda (0,1–0,3 Mbps upload).

##### Nessuna Connettività
- Solo video pre-registrati possono essere utilizzati ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri Partecipanti In Loco – Migliori Pratiche

Quando più partecipanti partecipano a una riunione Avatour in diretta dalla stessa posizione della fotocamera 360°, la gestione attenta di **audio e larghezza di banda** è cruciale:

- Ogni smartphone, tablet o laptop collegato in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione sgradevole per tutti i partecipanti.

#### Altri Partecipanti In Loco – Migliori Pratiche

Quando più partecipanti partecipano a una riunione Avatour in diretta dalla stessa posizione della fotocamera 360°, la gestione attenta di **audio e larghezza di banda** è cruciale:

- Ogni smartphone, tablet o laptop collegato in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione sgradevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **migliori pratiche**:

- **Utilizza cuffie cablate o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.
- **Modalità In Loco:** Partecipa alla riunione in modalità In Loco quando fisicamente presente vicino alla fotocamera 360°.
  - Questa modalità è ottimizzata per l'uso in loco:
    - Silenzia il microfono e l'altoparlante del partecipante per impostazione predefinita.
    - **Non** invia il feed della fotocamera del partecipante.
    - **Non** visualizza il feed della fotocamera 360° nel browser del partecipante.
    - Conserva la larghezza di banda di rete, assicurando che la fotocamera 360° abbia il massimo upload disponibile per il flusso in diretta.
    - Utile quando un utente vuole condividere dettagli specifici; **puoi condividere indietro la tua fotocamera** per viste mirate.
- **Silenzia quando non parli attivamente:** Previene feedback audio indesiderato e distrazioni.
- **Utilizza una rete separata se possibile:** Collega il tuo smartphone a una rete diversa da quella della fotocamera per ridurre le interferenze.

Seguire queste linee guida garantisce un tour in diretta fluido e di alta qualità sia per i partecipanti in loco che remoti.### 5.3 App Fotocamera Avatour

Ecco (1) il menu di primo livello, (2) Impostazioni e (3) i menu Impostazioni di rete.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360° Camera App - 3 Menu*

**Quick Capture** - Per la registrazione di video 360° offline. - Per una descrizione dettagliata, consulta [Come registri e carichi video 360 con l'app Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Consigliamo di utilizzare un dispositivo audio esterno (connesso tramite bluetooth). N.B. Puoi anche creare video e foto 2D standard - semplicemente cambia la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata QC.

**Live Meeting** - Per videoconferenze 360° in diretta. Vedrai i tuoi spazi di lavoro e facendo clic su uno avvierai lo streaming video in diretta dalla fotocamera 360°. Prima di poter partecipare alla riunione con la tua fotocamera 360° è necessario collegare un dispositivo audio tramite bluetooth. Per una descrizione dettagliata, consulta [Come avviare una riunione Live Capture con la tua fotocamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando ospiti una riunione Live Capture con la tua fotocamera 360, avrai a disposizione strumenti di riunione simili a quelli che rispecchiano l'esperienza web. Ecco un link al nostro articolo della Knowledge Base che spiega questi strumenti in modo più dettagliato: [Operator App Tools](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Gallery** - Qui troverai tutti i tuoi video e foto 360° da caricare nella console web Avatour.

**Impostazioni** - All'interno delle impostazioni, hai le seguenti opzioni:

- **Network**: Questa opzione ti consente di cambiare la rete WiFi a cui è connessa la fotocamera o di eseguire un test di connessione di rete per visualizzare il throughput di streaming
- **Live Capture**: Regola le impostazioni di Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti o se sulla tua fotocamera sono installati i coperchietti protettivi:
  - **Target Frame Rate**: Regola la frequenza fotogrammi per il video Live Capture tra 15 fps, 24 fps e 30 fps. Frequenze fotogrammi più elevate producono video più fluidi, ma richiedono una maggiore larghezza di banda di upload. Predefinito: 15 fps
  - **Target Bitrate**: Ti consente di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il bitrate di destinazione tra 1 Mbps e 10 Mbps. Bitrate più elevati comporteranno una risoluzione video più elevata, ma richiederanno una maggiore larghezza di banda di upload. Predefinito: 5 Mbps
  - **Optimize Motion**: Ciò ridurrà la frequenza fotogrammi video, generando meno carico sulla larghezza di banda di upload della rete, e aumenterà il bitrate di streaming. Inoltre, questa opzione aiuta a ridurre la cinetosi per i partecipanti VR. Predefinito: Off
  - **Protective Lenses**: Questo influenzerà il modo in cui il video 360° viene cucito a seconda che i coperchietti protettivi siano stati installati sulla tua fotocamera. Se non hai coperchietti protettivi, imposta questo su "No". Se hai ricevuto un Kit 3.0, hai coperchietti protettivi preinstallati e devi impostare questo su "Sì". Predefinito: Sì

- **Quick Capture**: Regola le impostazioni di Quick Capture in base alla frequenza fotogrammi video preferita, alla larghezza di banda disponibile per i caricamenti di video registrati o se sulla tua fotocamera sono installati i coperchietti protettivi. Quick Capture ha una risoluzione impostata di 4k che di solito rappresenta un buon equilibrio tra qualità video e dimensione del file. (Per risoluzioni più elevate puoi utilizzare le app fotocamera native, anche su PanoX V2, per i dettagli consulta [Come registri e carichi video 360 con l'app Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Target Frame Rate**: Regola la frequenza fotogrammi per le registrazioni video di Quick Capture tra 15 fps, 24 fps e 30 fps. Frequenze fotogrammi più elevate producono video più fluidi, ma aumenteranno le dimensioni del file video e il tempo di upload. Consigliato: 30 fps
  - **Target Bitrate**: Imposta il bitrate di destinazione per i caricamenti di Quick Capture tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano le velocità di upload, ma diminuiranno la qualità video. Consigliato: 20 Mbps
  - **Protective Lenses**: *Vedi la sezione Protective Lenses per Live Capture qui sopra*
- **About**: Visualizza il numero di serie del dispositivo e la versione del software

**Account** - Per accedere con il tuo account host o admin di Avatour.## 6. Consigli di Best Practice {#best-practice-advice}

### 6.1 Primi usi (informali) e familiarizzazione

Per i tuoi primi usi e per familiarizzare con la Console Web Avatour e il Kit Turnkey Avatour consigliamo i seguenti passaggi:

1. Porta il kit a casa e gioca con esso con la famiglia e gli amici utilizzando la tua connessione Internet domestica.
2. Porta il kit in ufficio e connettiti a una rete aziendale (potrebbero emergere problemi aziendali, ad es. firewall aziendali - ma dal passaggio uno sai che Avatour funziona e questo è un argomento da risolvere dal tuo team IT con l'aiuto di Avatour).
3. Inizia a utilizzare Avatour in loco (fuori dal tuo ufficio) presso la sede riunioni a cui i partecipanti remoti di solito dovrebbero recarsi. Potrebbero emergere ulteriori problemi di connettività. Avatour aiuta in cooperazione con il tuo team IT.
4. Inizia a utilizzare con partecipanti remoti interni ed esterni.### 6.2 Prima di una riunione live in video 360°

- Si consiglia di effettuare un tour video 360° registrato prima di qualsiasi tour in diretta, se il tempo lo consente, per tre motivi: (1) avere una soluzione di fallback per il tour in diretta, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour in diretta registrato) e (3) iniziare a creare una libreria di video 360° di tutti i vostri siti, che può essere utile per molti casi d'uso.
- Tutti i componenti del kit devono essere caricati per almeno 90 minuti prima della riunione in diretta. Consigliamo comunque di mantenere tutti i dispositivi in carica continua quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni ad hoc non pianificate.
- Avere il kit completamente assemblato (1. base del treppiede + 2. batteria Ulanzi + 3. stick estendibile + 4. fotocamera 360°).

- Confermare che uno Workspace sia stato creato per ospitare una riunione in diretta e includervi tutti gli Asset rilevanti.

- Invitare tutti i partecipanti alla riunione attraverso il vostro Workspace. Questo crea un invito sul calendario di tutti i partecipanti e include il link di invito alla riunione.

- Abbinare e connettere gli auricolari Bluetooth o l'altoparlante che intendete utilizzare per il vostro tour alla fotocamera.

- Tutti gli utenti di smartphone in loco dovrebbero connettersi da una rete diversa da quella della fotocamera. Questo ridurrà il carico sulla larghezza di banda della rete della fotocamera.

- Se siete solo come operatore della fotocamera, portate con voi uno smartphone nel caso in cui vogliate condividere la fotocamera dello smartphone e mostrare dettagli fini.

- Confermare che la fotocamera 360° possa connettersi al vostro WiFi locale.

- Prima di una riunione Avatour, pianificate il percorso che farete attraverso la struttura. Effettuate una riunione Avatour di prova con la fotocamera e controllate che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Questo può essere visto sullo schermo della fotocamera stessa, o come partecipante remoto andando a Impostazioni e attivando Mostra bitrate.

- Se notate che alcune aree hanno poca o nessuna larghezza di banda, è meglio acquisire immagini o una registrazione. Queste possono essere presentate durante la riunione affinché i partecipanti remoti le possano rivedere. Potete seguire la guida qui che spiega il nostro Quick Capture per la registrazione e il caricamento di video/immagini: [Come registrare e caricare video 360° con l'app Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se avete partecipanti remoti che si uniscono alla riunione e che non hanno mai utilizzato Avatour prima, fornite loro un breve riassunto della piattaforma, della sua funzionalità (video live 360°, asset, istantanee, annotazioni, spotlight) e degli strumenti della riunione.

- Potete iniziare con un'altra soluzione di videoconferenza (ad es. Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudete completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del vostro dispositivo, causandone la disabilitazione per Avatour. Inoltre, NON eseguite contemporaneamente Avatour e un'altra videoconferenza in quanto ciò ridurrà la larghezza di banda disponibile.

- Se state pianificando di utilizzare la fotocamera 360° in un ambiente ad alta temperatura, si consiglia di utilizzare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la fotocamera si surriscaldi e si spenga automaticamente.### 6.3 Quando si utilizza la telecamera in loco per una riunione video live a 360°

- Quando si utilizza la telecamera, assicurarsi di camminare lentamente. Questo aiuta la qualità video e riduce eventuali tempi di inattività video quando la connessione di rete della telecamera passa da un punto di accesso WiFi a un altro.

- Tenere la telecamera di fronte a sé e sopra il livello degli occhi. Questo consente a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Nei casi in cui la telecamera deve rimanere stabile, utilizzare il supporto treppiede e estendere la telecamera all'altezza corretta, preferibilmente a livello degli occhi.

- Collegare sempre la telecamera alla rete WiFi locale quando possibile. Per le aree senza accesso WiFi, utilizzare l'hotspot fornito. L'hotspot dispone di una scheda SIM che si collegherà a una rete cellulare affidabile nelle vicinanze. Mantenere sempre l'hotspot spento quando non in uso al chiuso, altrimenti la telecamera 360° potrebbe connettersi all'hotspot, cosa che non vogliamo al chiuso. Quando all'esterno, mantenere l'hotspot vicino alla telecamera 360°.

- Quando il bitrate della telecamera inizia a scendere al di sotto di 2 Mbps, camminare più lentamente o fermarsi completamente fino a quando il segnale non si stabilizza di nuovo. Questo di solito accade quando si passa da un punto di accesso WiFi a un altro.

- Se si sa che la connettività e il video si interromperanno quando ci si sposta in una posizione specifica (Esempio: passare da un'area di produzione interna a un'area esterna), informare in anticipo i partecipanti remoti.

- Se è necessario mostrare qualcosa in alta definizione o con piccoli caratteri, utilizzare lo smartphone proprio o di un partecipante in loco per partecipare alla riunione e presentare la fotocamera posteriore del telefono proprio / loro.

- Se possibile, consigliamo che una persona aggiuntiva sia presente in loco per aiutare con la condivisione della fotocamera dello smartphone descritta sopra, poiché spesso risulta utile / necessaria.

- Idealmente, gli utenti di smartphone in loco dovrebbero partecipare alla riunione (1) in modalità in loco e (2) su una rete diversa da quella utilizzata dalla telecamera per non togliere larghezza di banda di upload cruciale alla telecamera 360°.

- Tutti i partecipanti in loco che si uniscono dal loro smartphone dovrebbero essere disattivati, a meno che non stiano parlando attivamente.