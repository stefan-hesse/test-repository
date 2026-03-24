# Guida Utente e Buone Pratiche di Avatour

## 1. Per Tutti gli Utenti Avatour {#for-all-avatour-users}

Se sei nuovo su Avatour, le seguenti risorse forniscono un'utile introduzione alla piattaforma e alle sue funzionalità:

1. [Video su come funziona Avatour](https://avatour.com/how-it-works)  
   Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma consente la collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs)  
   Risposte alle domande frequenti
3. [Glossario](https://avatour.com/glossary)  
   Definizioni dei principali termini e concetti di Avatour.
4. Sito Web  
   Consulta la pagina delle [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate ai Casi d'Uso e ai Settori per scoprire come Avatour può supportare le tue esigenze specifiche.

## 2. Tipi di Utenti Avatour {#avatour-user-types}

### 2.1 Partecipanti alla Riunione (Nessun Account Richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi a un account Avatour.Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare l'accesso per autenticarsi.

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
- Insieme ai Partecipanti, una riunione può ospitare fino a 30 persone.

### 2.2 Utenti Registrati

Gli Utenti Registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitato dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di registrazione** per completare la configurazione dell'account e impostare una password.
- **Invitato dall'Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce all'utente un accesso di livello Host.
- **Provisioning automatico SSO (solo livello Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account con provisioning SSO vengono aggiunti al **gruppo Guest**, a meno che non vengano sovrascritti tramite **mappature di gruppo SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza a un gruppo direttamente anche quando SSO è abilitato.

**Riepilogo:**

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in più modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).
- **Provisioning SSO:** Per i clienti di livello Enterprise o Business con SSO abilitato, l'IdP può effettuare automaticamente il provisioning degli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo dell'utente sulla piattaforma.
- **Utenti invitati dall'Host:** Gli Host possono invitare altri utenti come collaboratori Editor a Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Buona Pratica Consigliata (Clienti Enterprise):**
Per le organizzazioni che si aspettano un gran numero di utenti che necessitano di accesso ad Avatour, si consiglia di **integrare il Single Sign-On (SSO)** e gestire utenti e appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione ai gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo degli accessi coerente.

#### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.
- Possono **visualizzare gli Asset** nei Workspace in cui sono stati aggiunti come **collaboratori Viewer**.
- Non possono creare workspace, ospitare riunioni o caricare contenuti.
- Gli account Guest con provisioning SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

#### 2.2.2 Utenti con Licenza (Accesso alla Web Console)

##### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori a un workspace, **ospitare riunioni live**, caricare **Quick Capture**.
- Hanno accesso alla **Dashboard Host** e all'**App Operatore** sulle telecamere 360° supportate.

##### Utenti Admin (Gruppo: Admin)

- Include tutte le funzionalità Host più l'amministrazione completa dell'account.

**I privilegi Admin aggiuntivi includono:**

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

#### 2.2.3 Permessi dei Collaboratori del Workspace

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
  Potresti ricevere un **invito del calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita al sito remota in tempo reale** o rivedere gli asset insieme in modo sincrono.

- **Visitare un Workspace:**
  Potresti anche essere invitato come **collaboratore a un Workspace** per rivedere gli asset **in modo asincrono** (secondo il tuo programma).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare un Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo "Flat Screen" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.

##### Partecipare a una Riunione

> **Nota:** Per partecipare a una riunione Avatour è necessario **concedere i permessi al microfono**. Accetta le richieste di autorizzazione dal tuo browser.

1. **Tramite invito del calendario (consigliato):**
   - Di solito riceverai un **invito del calendario** con un **link diretto per partecipare** (ad esempio: `https://avatour.live/join?s=xxxxx`).
   - Cliccando sul link verrà automaticamente inserito il **codice riunione a 5 caratteri** e verrai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono limitate agli utenti registrati. In questo caso, l'invito indicherà che è necessario **accedere per partecipare alla riunione**.
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**
   - Se l'host condivide separatamente un **codice riunione a 5 caratteri**, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione** e partecipa alla riunione.
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.
   - Se la riunione richiede **autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio, Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o il microfono, poi esci e rientra nella riunione Avatour.

> **Suggerimento 2:** Se non riesci ancora a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).
> Il test può identificare se il **firewall aziendale o la rete** blocca l'accesso e fornirà informazioni per guidare le discussioni con il tuo team IT.

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando si **trasmette una riunione live da una telecamera Insta360**, poiché queste telecamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone come supporto.

##### Visitare un Workspace Senza Partecipare a una Riunione

Puoi accedere a un Workspace senza partecipare a una riunione live nei seguenti modi:

- **Workspace Pubblico:**
  Se il Workspace è pubblico, è possibile accedere al link direttamente — senza necessità di accesso.

- **Workspace Limitato:**
  Se il Workspace è limitato, devi essere aggiunto come **collaboratore** con permessi **Editor** o **Viewer**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica via email** con un link al Workspace.
  2. Clicca sul link nell'email per aprire il Workspace. Se non hai già effettuato l'accesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, il Workspace si aprirà automaticamente.

  In alternativa, puoi accedere su
  https://avatour.live/login
  e accedere al Workspace dal tuo **elenco di Workspace**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare un workspace da una serie di visori Meta e Pico compatibili. Per farlo:

1. Installa la nostra app Avatour dal rispettivo store di app VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona un Workspace per partecipare a una riunione. Per ulteriori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite al sito live o revisione di asset registrati insieme.
2. **Workspace (asincroni):** Rivedi e interagisci con gli asset secondo il tuo programma, 24/7.

Gli **strumenti di collaborazione sono principalmente simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata attorno a tre aree principali:

- **Pannello sinistro** – Asset del Workspace e strumenti di supporto
- **Canvas centrale** – Area di visualizzazione principale per video live o asset
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat

La maggior parte delle interazioni viene avviata dal **menu in basso**.
Cliccando su un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Vista Riunione

Ecco un esempio di vista in una Riunione Avatour:

![Avatour Meeting UI with Assets Panel, blank Canvas and Participants Panel](https://res.cloudinary.com/avatour/image/upload/v1772362400/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)
*Riunione Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Vista Workspace

Ecco un esempio di vista Workspace:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)
*Workspace Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del Menu in Basso

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

##### Menu Presenta

L'opzione **Presenta** nel menu in basso della riunione consente di condividere contenuti con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Può essere utilizzata anche durante una riunione video live 360° per sovrapporre una vista secondaria per primi piani o dettagli specifici.
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.
- **Asset** – Presenta un asset dal workspace. Selezionando un asset si apre la **barra degli strumenti Asset**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per l'asset presentato.

##### Barra degli Strumenti Asset (Riunione)

Quando si presenta un asset in una riunione, la **Barra degli Strumenti Asset** appare sopra il canvas. Ecco gli strumenti e le voci del menu disponibili quando si <u>presenta un Asset in una Riunione</u> - spiegati da sinistra a destra.

![Avatour Menu while Presenting an Asset in a Meeting](https://res.cloudinary.com/avatour/image/upload/v1772303706/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour durante la presentazione di un Asset in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca su una nota o un argomento per passare a quel momento e aprire la nota. Include i controlli **Riproduci / Pausa**.
- **Snapshot** – Cattura un'immagine 360° o 2D dall'asset.
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni live.
- **Mostra/Nascondi Punto di Vista (POV)** – Mostra dove ogni partecipante sta guardando nel video 360°.
- **Note** – Crea note ancorate a momenti specifici nell'asset. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperto → In Corso → Risolto) e condivise tramite link diretti.

  ![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/v1772374822/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

  - **Note da Comandi Vocali** – Questi sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente.

  ![Avatour Notes - Voice Command Generated](https://res.cloudinary.com/avatour/image/upload/v1772921944/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da Comandi Vocali*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che mostra tutte le note, gli argomenti chiave e un riepilogo esecutivo per l'asset. Cliccando su un elemento si passa a quel momento nel video.

  ![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour durante la presentazione di un Asset in una Riunione*

  ![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di un Asset in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report dell'asset** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati dall'AI e trascrizioni complete. Puoi anche **scegliere quali elementi includere** prima di esportare.

  ![Avatour Asset Report Print Menus](https://res.cloudinary.com/avatour/image/upload/v1773496969/avatour-screenshot-asset-report-print-menus_kn0syn.png)
  *Menu Stampa / Download Report Asset Avatour*

  ![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/v1772376570/avatour-screenshot-asset-report-element-selection_ud8c5k.png)
  *Menu Selezione Elementi Report Asset Avatour*

- **Link di Condivisione** – Condividi un link a una nota specifica o a una scena nell'asset.
- **Sottotitoli (CC)** – Mostra la trascrizione testuale sullo schermo durante la riproduzione video.

##### Barra degli Strumenti Asset (Workspace)

Quando si rivede un asset in un workspace, la barra degli strumenti è simile ma ottimizzata per uso individuale:

![Avatour Menu while Presenting an Asset outside a meeting, e.g. when visiting a workspace](https://res.cloudinary.com/avatour/image/upload/v1772303705/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour durante la presentazione di un Asset in un Workspace*

- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca in qualsiasi punto della timeline per scorrere il video. Clicca su una nota o un argomento per passare a quel momento e aprire la nota. Include i controlli **Riproduci / Pausa**.
- **Snapshot, Note, Pannello Note e Riepilogo, Link di Condivisione, Sottotitoli**
- Non disponibili: **Spotlight, POV** (richiedono partecipanti live)
- Controlli aggiuntivi:
  - **Passi da 10 secondi** – Salta avanti/indietro
  - **Velocità di Riproduzione** – Regola la velocità (0,5×–2×)
  - **Taglia Video** – Taglia l'inizio o la fine dell'asset


## 4. Per Utenti Host e Admin - Web Console Avatour {#for-host-and-admin-users-avatour-web-console}

Quando accedi al tuo Account Utente Avatour, accederai alla **Web Console**.

### 4.1 Web Console - Panoramica del Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro vedrai le seguenti voci del menu:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload//v1774364052/avatour-screenshot-main-menu_qwpthq.png) *Web Console Avatour - Menu Principale*

- **Workspace** – Organizza i tuoi contenuti in modo efficiente. Ogni workspace contiene **Asset**, **Collaboratori**, **Riunioni** e **Impostazioni**.
- **Asset** – Accedi e gestisci tutti i tuoi asset (video, immagini, PDF). Gli Admin possono visualizzare tutti gli asset dell'account e gli asset condivisi sono visibili a tutti gli utenti.
- **Profilo** – Gestisci la tua lingua e la password.
- **Analytics** – Monitora l'attività delle sessioni, l'utilizzo del workspace e le metriche ROI.
- **Impostazioni** *(solo Admin)* – Configura le impostazioni predefinite di workspace, riunione e asset in tutta l'organizzazione. Gli Admin possono anche personalizzare il branding (logo, colori, sfondi).
- **Account** *(solo Admin)* – Gestisci gli utenti registrati e le telecamere 360°.
- **Accesso Dispositivo** – Inserisci il codice visualizzato sulla tua telecamera 360° per associarla al tuo account.
- **Tutorial** – Accedi ai tutorial guidati.
- **Disconnetti** – Esci dalla console.

> Le sezioni come Profilo, Accesso Dispositivo, Tutorial e Disconnetti sono autoesplicative e non hanno sottosezioni dettagliate.

---

### 4.2 Web Console - Dettagli per Voce di Menu (con immagini)  {#web-console-details-by-menu-item} 

#### 4.2.1 Workspace

I Workspace sono unità organizzative flessibili che consentono di gestire asset, collaboratori e riunioni in un unico posto. Puoi creare un nuovo workspace con il pulsante **Nuovo Workspace** nell'angolo in alto a destra.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/v1772360323/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Web Console Avatour - Voce Menu Principale Workspace*

Clicca sull'icona campanella per vedere un riepilogo delle attività del workspace negli ultimi 7 giorni.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/v1772919758/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti del Workspace*

All'interno di un workspace:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace con Asset (sinistra), Canvas (centro), Riunioni (destra)*

- **Asset** – Gestisci i file allocati a questo workspace.
- **Collaboratori** –
  Controlla l'accesso ai workspace tramite
  - **Viewer** – Può visualizzare gli asset. L'invito crea un utente Guest se necessario.
  - **Editor** – Controllo completo del workspace, stessi diritti dell'Host. L'invito aggiorna l'utente a Host se necessario.
> Più utenti possono accedere a un workspace contemporaneamente senza una riunione. I workspace pubblici e le impostazioni di accesso alle riunioni forniscono accesso alternativo.
- **Report** – Genera un report utilizzando un modello di checklist sugli asset del workspace selezionati.

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/v1772924118/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report Workspace e Selezione Asset*

- **Mappa** – Mostra le posizioni degli asset con GPS abilitato su una mappa.
- **Riunioni** – Organizza riunioni nel workspace.
- **Impostazioni** – Configura le impostazioni predefinite di workspace e riunione:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/v1772387752/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni Workspace*

**Impostazioni Workspace**

- **Modello di Report** – Seleziona il modello di checklist per la reportistica AI.
- **Abilita Notifiche** – Email di riepilogo giornaliero per le modifiche di stato delle note.

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/v1772804314/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio di Notifiche Email*

- **Workspace Pubblico** – Chiunque abbia il link può visualizzare gli asset direttamente.

**Impostazioni Riunione**

- **Autenticazione richiesta** – I partecipanti devono effettuare l'accesso.
- **Consenti accesso guest** – Permetti agli utenti non registrati di visualizzare gli asset.
- **Avvio Automatico Registrazione / Avvio Manuale** – Scegli se le riunioni vengono registrate automaticamente o avviate manualmente.
- **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host se ne va.
- **Consenti accesso spettatore** – Partecipa senza microfono o fotocamera; comunica tramite chat.
- **Riunioni protette da password** – Richiedi una password per partecipare.
- **Mostra Domanda sul Risparmio di Viaggio** – Chiedi ai partecipanti se la riunione ha ridotto i viaggi.

> Le impostazioni possono essere combinate (ad esempio, nessun host richiesto ma protetto da password).

---

#### 4.2.2 Asset

Gestisci tutti i video 360°/2D, le immagini e i PDF. Carica/scarica asset, allocali ai workspace, condividili con altri utenti, rinominali, stampa/scarica report, attiva la sfocatura dei volti e la riepilogazione AI.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/v1772360326/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Asset*

---

#### 4.2.3 Analytics

Fornisce informazioni su riunioni, utilizzo del workspace e metriche ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360315/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analytics*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360313/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Riunioni e Utilizzo Workspace*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360312/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenze Dispositivo e ROI*

## 5. In Loco - Come Utilizzare il Kit Turnkey Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Per Iniziare
[Guida Rapida – Kit Turnkey Avatour 3.1 (configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per disimballare, assemblare e accendere la telecamera.

---

### 5.2 Consigli Utili

#### Batteria Esterna – Riunioni Live Più Lunghe e Migliore Gestione Termica

- **Se il kit include una batteria Ulanzi:** Collegala tra la base del treppiede e il bastone estensibile, quindi collega la batteria alla telecamera tramite USB-C.

- **Se il kit include un bastone batteria Telesin:** Monta la telecamera direttamente sul bastone batteria estensibile Telesin e collegala tramite USB-C.

Utilizzo della batteria esterna:

1. Estende la durata totale della batteria da ~40 minuti (solo batteria della telecamera) a ~3 ore.
2. Aggiunge stabilità alla configurazione della telecamera.
3. Aiuta a prevenire potenziali surriscaldamenti.

> Si consiglia di utilizzare sempre la batteria esterna sin dall'inizio, specialmente per le riunioni live.

#### Considerazioni Audio per Riunioni Live e Registrazioni

- **Ambienti rumorosi:**
  Usa le cuffie Shokz incluse nel kit per una cattura audio chiara.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).
  - **Modalità di Abbinamento Bluetooth:** Con le cuffie spente, tieni premuto il pulsante "+" per 5 secondi (il LED lampeggia blu/rosso).
  - **Volume:** Usa i pulsanti "+" e "-".

- **Ambienti più tranquilli / più partecipanti vicino alla telecamera:**
  Usa il diffusore a clip NoxGear. Non ha la stessa fedeltà degli altoparlanti per conferenze (ad esempio Jabra Speak), ma è facile da agganciare alla camicia e cattura le voci nelle vicinanze in modo efficace.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Riproduci/Pausa per 2 secondi.
  - **Modalità di Abbinamento Bluetooth:** Entra automaticamente in modalità di abbinamento all'accensione (LED lampeggia blu/rosso; blu fisso quando abbinato).
  - **Volume:** Usa i pulsanti "+" e "-".

- **Utilizzo del proprio dispositivo:** Se preferisci un'alternativa (ad esempio un altoparlante per conferenze o un auricolare personale), puoi abbinarlo tramite la telecamera: Impostazioni → Bluetooth.

#### Connettività, Connettività, Connettività
**Prima di iniziare:** Assicura la connessione Internet tramite:

- **WiFi locale** (preferito)
- **Rete Mobile** (se fuori portata del WiFi)

**Larghezza di banda consigliata:** 10 Mbps uplink/downlink per lo streaming 360° completo (~5 Mbps). La larghezza di banda inferiore (1–2 Mbps) funziona solo quando si è fermi.

##### Test della Velocità di Rete
- **Test in una singola posizione:** Qualsiasi misuratore di velocità che usi normalmente (ad esempio [Speedtest](https://www.speedtest.net)) per verificare la larghezza di banda di caricamento.
- **Test camminando per il sito:** Dalla telecamera: Impostazioni → Rete → Test di Connessione. Cammina attraverso tutto lo spazio per confermare la copertura e la larghezza di banda.

##### WiFi Locale
- Altamente consigliato per connessioni stabili.
- Se l'IT richiede la whitelist, trova l'indirizzo MAC: Impostazioni → Informazioni → Indirizzo WiFi.

##### Rete Mobile
**Opzione A: Hotspot e SIM forniti con il kit**

- Collega l'hotspot GlocalMe al bastone batteria Telesin (magnete).
- Garantisce nessuna interferenza e mantiene la connessione se ci si allontana dalla telecamera.
- Risoluzione dei problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).
  - Abilita il 5G nel Gestore SIM Card.
  - Verifica l'APN corretto per la tua regione ([guida configurazione APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Usa il tuo smartphone o un hotspot dedicato.

**Nota Importante:**
> Tieni l'hotspot spento mentre sei connesso al WiFi; abilitalo solo quando sei fuori portata. Il sistema operativo della telecamera cambia dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe passare involontariamente all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili potrebbero limitare la larghezza di banda in modo imprevisto. Controlla con il tuo operatore i limiti del piano dati, o contatta il supporto Avatour se stai usando il nostro hotspot e SIM.

##### Situazioni di Bassa Larghezza di Banda
- Pre-registra video delle posizioni per la riproduzione successiva ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Condividi uno stream della fotocamera dello smartphone per integrare le aree a bassa larghezza di banda (0,1–0,3 Mbps di caricamento).

##### Nessuna Connettività
- È possibile utilizzare solo video pre-registrati ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri Partecipanti in Loco – Buone Pratiche

Quando più partecipanti si uniscono a una riunione Avatour live dalla stessa posizione della telecamera 360°, è fondamentale gestire attentamente **audio e larghezza di banda**:

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della telecamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **eco audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **buone pratiche**:

- **Usa cuffie cablate o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.
- **Modalità In Loco:** Partecipa alla riunione in modalità In Loco quando sei fisicamente presente vicino alla telecamera 360°.
  - Questa modalità è ottimizzata per l'uso in loco:
    - Silenzia il microfono e l'altoparlante del partecipante per impostazione predefinita.
    - **Non** invia il feed della fotocamera del partecipante.
    - **Non** mostra il feed della telecamera 360° nel browser del partecipante.
    - Conserva la larghezza di banda di rete, garantendo alla telecamera 360° il massimo caricamento disponibile per lo streaming live.
    - Utile quando un utente vuole condividere dettagli specifici; **puoi condividere la tua fotocamera** per visualizzazioni mirate.
- **Silenziati quando non stai parlando attivamente:** Previene feedback audio indesiderati e distrazioni.
- **Usa una rete separata se possibile:** Avere lo smartphone connesso a una rete diversa da quella della telecamera per ridurre le interferenze.

Seguire queste linee guida garantisce un tour live fluido e di alta qualità sia per i partecipanti in loco che per quelli remoti.

### 5.3 App Telecamera Avatour

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

## 6. Consigli di Buone Pratiche {#best-practice-advice}

### 6.1 Primi Usi (Informali) e Familiarizzazione

Per i tuoi primi utilizzi e per familiarizzare con la Web Console Avatour e il Kit Turnkey Avatour, consigliamo i seguenti passaggi:

1. Porta il kit a casa e giocaci con familiari e amici usando la tua connessione internet domestica.
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
