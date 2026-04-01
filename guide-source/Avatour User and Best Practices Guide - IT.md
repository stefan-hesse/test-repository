# Avatour User and Best Practices Guide

## 1. Per Tutti gli Utenti Avatour {#for-all-avatour-users}

Se sei nuovo su Avatour, le seguenti risorse forniscono un'utile introduzione alla piattaforma e alle sue funzionalità:

1. [Video Come funziona Avatour](https://avatour.com/how-it-works)  
Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma consente una collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs)  
Risposte alle domande frequenti.
3. [Glossario](https://avatour.com/glossary)  
Definizioni dei principali termini e concetti di Avatour utilizzati frequentemente.
4. Sito web  
Dai un'occhiata in particolare alla pagina [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate ai Casi d'uso e ai Settori per scoprire come Avatour può supportare le tue esigenze specifiche.

## 2. Tipi di utenti Avatour  {#avatour-user-types}

### 2.1 Partecipanti alle riunioni (Nessun account richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi per un account Avatour.
Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare l'accesso per autenticarsi.

Gli utenti accedono alla riunione come segue:

- Ricevono un invito del calendario dall'host.
- Utilizzano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'host ne ha abilitata una.
- I partecipanti possono partecipare senza un account Avatour a meno che la riunione non sia limitata e richieda l'accesso per autenticarsi.

#### 2.1.1 Partecipante 

- Può partecipare e interagire completamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, usare il microfono, presentare, riprodurre/mettere in pausa Asset o acquisire Snapshot.
- Massimo 10 Spettatori per riunione.
- Insieme ai Partecipanti, una riunione può ospitare fino a 30 partecipanti.

### 2.2 Utenti registrati

Gli Utenti registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitati dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di registrazione** per completare la configurazione dell'account e impostare una password.  
- **Invitati dall'Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce che l'utente abbia accesso a livello Host.  
- **Provisioning automatico SSO (solo livello Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account provisionati tramite SSO vengono aggiunti al **gruppo Guest**, a meno che non venga sovrascritto tramite **mappature dei gruppi SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza ai gruppi direttamente anche quando SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in diversi modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).  
- **Provisioning SSO:** Per i clienti di livello Enterprise o Business con SSO abilitato, l'IdP può provisionare automaticamente gli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo dell'utente sulla piattaforma.  
- **Utenti invitati dall'Host:** Gli Host possono invitare altri utenti come collaboratori Editor in Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Best Practice raccomandata (Clienti Enterprise):**  
Per le organizzazioni che prevedono un gran numero di utenti che necessitano accesso ad Avatour, si raccomanda di **integrare Single Sign-On (SSO)** e gestire utenti e appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione dei gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo degli accessi coerente.

#### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.  
- Possono **visualizzare Asset** all'interno dei Workspace dove sono stati aggiunti come **collaboratori Viewer**.  
- Non possono creare workspace, ospitare riunioni o caricare contenuti.  
- Gli account Guest provisionati tramite SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

#### 2.2.2 Utenti con licenza (Accesso alla Console Web)

##### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori a un workspace, **ospitare riunioni live**, caricare **Quick Capture**.  
- Hanno accesso alla **Dashboard Host** e all'**App Operator** su fotocamere 360° supportate.  

##### Utenti Admin (Gruppo: Admin)

- Includono tutte le funzionalità Host più l'amministrazione completa dell'account.

**I privilegi Admin aggiuntivi includono:**

**Gestione Account**  

- Creare nuovi utenti e assegnarli a gruppi.
- Reimpostare le password quando gestite da Avatour (non applicabile quando SSO è abilitato). 
- Aggiornare utenti Guest a Host.  
- Disattivare utenti (gli account Admin devono prima essere convertiti in Host prima della cancellazione).  
- Trasferire asset da un utente Host a un altro durante la cancellazione.

**Impostazioni**  

- Configurare **impostazioni di sicurezza a livello organizzativo** per asset, workspace e riunioni ospitate sulla piattaforma (ad es., se un Host deve essere presente per avviare una riunione, se i volti devono essere sfocati su tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare **funzionalità AI** o **registrazione**.  
- Applicare il branding aziendale in modo coerente su tutta la piattaforma se è configurato un **dominio personalizzato**.
  

**Asset e Analytics** 
 
- Visualizzare tutti gli Asset caricati da qualsiasi utente nell'organizzazione.  
- Esaminare l'utilizzo della piattaforma in tutta l'organizzazione.

---

#### 2.2.3 Permessi dei collaboratori del Workspace

I permessi del Workspace definiscono cosa un utente può fare **all'interno di un Workspace specifico**. Questi sono separati dall'appartenenza ai gruppi a livello di piattaforma (Guest, Host, Admin).

- **Collaboratore Editor:** Gli utenti con questo permesso possono:
  - Gestire Asset (caricare, rimuovere, sfocare volti, generare riepiloghi)  
  - Gestire impostazioni delle riunioni (abilitare/disabilitare registrazione, consentire o rimuovere partecipanti)  
  - Pianificare e ospitare riunioni live  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dal Workspace  

- **Collaboratore Viewer:** Gli utenti con questo permesso hanno accesso in sola lettura agli Asset del Workspace. **Non possono modificare Asset, gestire riunioni o gestire collaboratori**, ma **possono creare Note sugli Asset**. 
  
## 3. Per i Partecipanti alle Riunioni da Remoto e i Visitatori dello Spazio di Lavoro {#for-remote-meeting-participants-and-workspace-visitors}
<section>

Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito nel calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota dal vivo al sito** o rivedere insieme le risorse in modo sincrono.

- **Visitare uno Workspace (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore in uno Workspace** per rivedere le risorse **in modo asincrono** (secondo i tuoi tempi).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare uno Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo "Flat Screen" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

##### Partecipare a una Riunione Avatour

> **Nota:** Partecipare a una riunione Avatour richiede che tu **conceda i permessi per il microfono**. Per favore accetta eventuali richieste di permesso dal tuo browser.

1. **Tramite invito nel calendario (consigliato):**  
   - Riceverai tipicamente un **invito nel calendario** con un **link diretto di accesso** (per esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando sul link verrà automaticamente inserito il **codice riunione di 5 caratteri** e sarai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono riservate agli utenti registrati. In questo caso, l'invito indicherà che devi **effettuare l'accesso per partecipare alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'host condivide un **codice riunione di 5 caratteri** separatamente, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.  
   - Se la riunione richiede **autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (per esempio, Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o il microfono, poi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se ancora non riesci a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la rete** sta bloccando l'accesso, e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando **si trasmette una riunione dal vivo da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone per l'assistenza.

##### Visitare uno Workspace Avatour (senza partecipare a una Riunione Avatour)

Puoi accedere a uno Workspace nei seguenti modi:

- **Workspace Pubblico:**  
  Se lo Workspace è pubblico, il link può essere accessibile direttamente—non è richiesto l'accesso.

- **Workspace Ristretto:**  
  Se lo Workspace è ristretto, devi essere aggiunto come **collaboratore** con permessi di **Editor** o **Viewer**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica email** con un link allo Workspace.
  2. Clicca sul link nell'email per aprire lo Workspace. Se non hai già effettuato l'accesso, ti verrà richiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, lo Workspace si aprirà automaticamente.

  In alternativa, puoi accedere su [https://avatour.live/login](https://avatour.live/login) e accedere allo Workspace dalla tua **lista di Workspace**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare uno workspace da una gamma di visori Meta e Pico compatibili. Per fare questo: 

1. Installa la nostra app Avatour dal rispettivo store di app VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona uno Workspace per partecipare a una riunione. Per maggiori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite al sito dal vivo o revisione insieme di risorse registrate.  
2. **Workspace (asincroni):** Rivedi e interagisci con le risorse secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata intorno a tre aree principali:

- **Pannello sinistro** – Risorse dello workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video dal vivo o risorse  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu in basso**.  
Cliccando su un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Vista Riunione

Ecco un esempio di una vista in una Riunione Avatour:

![Interfaccia Riunione Avatour con Pannello Risorse, Canvas vuoto e Pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con Pannello Risorse (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Vista Workspace

Ecco un esempio di una vista Workspace:

![Workspace Avatour con Pannello Risorse, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace Avatour con Pannello Risorse (sinistra), Canvas (centro) e Pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del Menu in Basso

Il menu in basso fornisce accesso ai controlli principali dell'interfaccia e ai pannelli:

**Menu in Basso della Riunione**  

![Menu in Basso Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu in Basso Riunione Avatour*

- **Risorse** – Rivedi i file dello workspace, inclusi video registrati, immagini, snapshot e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti della riunione.  
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Silenzia o riattiva te stesso.  
- **Presenta** – Presenta una risorsa, il desktop o il feed della webcam (vedi sezione Presenta sotto).  
- **Strumenti Host** (solo host):  
  - **Blocca Focus** – Blocca la vista per tutti i partecipanti.  
  - **Silenzia Tutti** – Silenzia tutti i partecipanti.  
- **Abilita Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Lascia la riunione.  
- **Avvia Registrazione** – Usa questo pulsante per avviare e fermare la registrazione manualmente durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se **l'avvio automatico della registrazione** è abilitato nelle impostazioni dello workspace. In entrambi i casi, le registrazioni vengono salvate nelle risorse dello workspace.
- **Mappa** – Apri o chiudi il pannello mappa per le risorse con una traccia GPS. Cliccando su una posizione si salta al punto esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Partecipanti** – Apri o chiudi il pannello partecipanti.  
- **Info Riunione** – Visualizza il codice riunione, il link di invito e accedi ai tutorial correlati.  

![Info Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Info Riunione Avatour*

- **Impostazioni** – Regola lingua, impostazioni audio e video. Per le riunioni con video 360° dal vivo, usa **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu in basso della riunione ti permette di condividere contenuti con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Può essere utilizzata anche durante una riunione con video 360° dal vivo per sovrapporre una vista secondaria per primi piani o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Risorsa** – Presenta una risorsa dallo workspace. Selezionando una risorsa si apre la **Barra degli strumenti Risorsa**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per la risorsa presentata.

##### Barra degli Strumenti Risorsa (Riunione)

Quando presenti una risorsa in una riunione, la **Barra degli Strumenti Risorsa** appare sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>presenti una Risorsa in una Riunione</u> - spiegati da sinistra a destra.

![Menu Avatour durante la Presentazione di una Risorsa in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour quando si presenta una Risorsa in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dalla risorsa.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni dal vivo.  
- **Mostra/Nascondi Punto di Vista (POV)** – Mostra dove ogni partecipante sta guardando nel video 360°.  
- **Note** – Crea note ancorate a momenti specifici nella risorsa. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperto → In Corso → Risolto), e condivise tramite link diretti.  

  ![Nota Avatour e Filtro Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

  - **Note da Comando Vocale** – Questi sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note Avatour - Generate da Comando Vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da Comando Vocale*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che mostra tutte le note, gli argomenti chiave e un riepilogo esecutivo per la risorsa. Cliccando su un elemento si salta a quel momento nel video.  

  ![Riepilogo Esecutivo Risorsa Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour mentre si presenta una Risorsa in una Riunione*

  ![Argomenti Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour mentre si presenta una Risorsa in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report della risorsa** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati dall'IA e trascrizioni complete. Puoi anche **## 4. Per utenti Host e Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}

Quando accedi al tuo Account Utente Avatour, accederai alla **Console Web**.  

### 4.1 Console Web - Panoramica del Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai le seguenti voci di menu:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principale*

- **Aree di Lavoro** – Organizza i tuoi contenuti in modo efficiente. Ogni area di lavoro contiene **Risorse**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Risorse** – Accedi e gestisci tutte le tue risorse (video, immagini, PDF). Gli amministratori possono visualizzare tutte le risorse dell'account e le risorse condivise sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analisi** – Monitora l'attività delle sessioni, l'utilizzo delle aree di lavoro e le metriche ROI.  
- **Impostazioni** *(Solo Amministratore)* – Configura le impostazioni predefinite per aree di lavoro, riunioni e risorse in tutta l'organizzazione. Gli amministratori possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo Amministratore)* – Gestisci gli utenti registrati e le telecamere 360°.  
- **Accesso Dispositivo** – Inserisci il codice visualizzato sulla tua telecamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Accesso Dispositivo, Tutorial ed Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---

### 4.2 Console Web - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Aree di Lavoro

Le Aree di Lavoro sono unità organizzative flessibili che ti permettono di gestire risorse, collaboratori e riunioni in un unico posto. Puoi creare una nuova area di lavoro con il pulsante **Nuova Area di Lavoro** nell'angolo in alto a destra.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Voce Menu Principale Aree di Lavoro*

Clicca sull'icona della campanella per vedere un riepilogo dell'attività dell'area di lavoro negli ultimi 7 giorni.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti dell'Area di Lavoro*

All'interno di un'area di lavoro:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Area di Lavoro con Risorse (sinistra), Canvas (centro), Riunioni (destra)*

- **Risorse** – Gestisci i file assegnati a questa area di lavoro.  
- **Collaboratori** – 
  Controlla l'accesso alle aree di lavoro tramite 
  - **Visualizzatore** – Può visualizzare le risorse. L'invito crea un utente Ospite se necessario.  
  - **Editor** – Controllo completo dell'area di lavoro, stessi diritti dell'Host. L'invito promuove l'utente a Host se necessario.  
> Più utenti possono accedere a un'area di lavoro contemporaneamente senza una riunione. Le aree di lavoro pubbliche e le impostazioni di accesso alle riunioni forniscono accessi alternativi.  
- **Report** – Genera un report utilizzando un modello di checklist sulle risorse selezionate dell'area di lavoro.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report dell'Area di Lavoro e Selezione Risorse*

- **Mappa** – Visualizza le posizioni delle risorse abilitate GPS su una mappa.  
- **Riunioni** – Organizza riunioni nell'area di lavoro.  
- **Impostazioni** – Configura le impostazioni predefinite dell'area di lavoro e delle riunioni:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni Area di Lavoro*

**Impostazioni Area di Lavoro**

- **Modello Report** – Seleziona il modello di checklist per la reportistica AI.  
- **Abilita Notifiche** – Email di riepilogo giornaliero per i cambiamenti di stato delle note.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio di Notifiche Email*

- **Area di Lavoro Pubblica** – Chiunque abbia il link può visualizzare le risorse direttamente.

**Impostazioni Riunione**
  
* **Autenticazione richiesta** – I partecipanti devono effettuare l'accesso.  
* **Consenti accesso ospiti** – Permetti agli utenti non registrati di visualizzare le risorse.  
* **Avvio Automatico Registrazione / Avvio Manuale** – Scegli se le riunioni si registrano automaticamente o vengono avviate manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host se ne va.  
* **Consenti accesso spettatore** – Partecipa senza microfono o videocamera; comunica tramite chat.  
* **Riunioni protette da password** – Richiedi una password per partecipare.  
* **Mostra Domanda Risparmio Viaggi** – Chiedi ai partecipanti se la riunione ha ridotto i viaggi.  

> Le impostazioni possono essere combinate (es., nessun host richiesto ma protetto da password).

---

#### 4.2.2 Risorse

Gestisci tutti i video 360°/2D, immagini e PDF. Carica/scarica risorse, assegnale alle aree di lavoro, condividile con altri utenti, rinominale, stampa/scarica report, attiva la sfocatura dei volti e la sintesi AI.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Risorse*

---

#### 4.2.3 Analisi

Fornisce approfondimenti su riunioni, utilizzo delle aree di lavoro e metriche ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analisi*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Riunioni e Utilizzo Aree di Lavoro*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenze Dispositivo e ROI* 

## 5. Onsite - Come Utilizzare il Kit Chiavi in Mano Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Per Iniziare
[Guida Rapida – Avatour Turnkey Kit 3.1 (configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per disimballare, assemblare e accendere la tua fotocamera.

---

### 5.2 Suggerimenti Utili

#### Batteria Esterna – Riunioni Live più Lunghe e Gestione Termica Migliorata 

- **Se il tuo kit include una batteria Ulanzi:** Fissala tra la base del treppiede e l'asta estensibile, quindi collega la batteria alla fotocamera tramite USB-C.  

- **Se il tuo kit include un'asta batteria Telesin:** Monta la fotocamera direttamente sull'asta batteria estensibile Telesin e collegala tramite USB-C.  

Utilizzando la batteria esterna:

1. Estende la durata totale della batteria da ~40 minuti (solo batteria della fotocamera) a ~3 ore.  
2. Aggiunge stabilità alla configurazione della fotocamera.  
3. Aiuta a prevenire il potenziale surriscaldamento.  

> Raccomandiamo di utilizzare sempre la batteria esterna dall'inizio, specialmente per le riunioni live.

#### Considerazioni Audio per Riunioni Live e Registrazioni

- **Ambienti rumorosi:** 
  Usa le cuffie Shokz incluse nel tuo kit per una cattura audio chiara.  
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).  
  - **Modalità Abbinamento Bluetooth:** Con le cuffie spente, tieni premuto il pulsante "+" per 5 secondi (LED lampeggia blu/rosso).  
  - **Volume:** Usa i pulsanti "+" e "-".  

- **Ambienti più silenziosi / più partecipanti vicino alla fotocamera:** 
  Usa l'altoparlante clip-on NoxGear. Non ha la stessa alta fedeltà degli altoparlanti da conferenza (es. Jabra Speak), ma è facile da agganciare alla camicia e cattura efficacemente le voci vicine.  
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Play/Pausa per 2 secondi.  
  - **Modalità Abbinamento Bluetooth:** Entra automaticamente in modalità abbinamento quando acceso (LED lampeggia blu/rosso; blu fisso quando abbinato).  
  - **Volume:** Usa i pulsanti "+" e "-".  

- **Utilizzo del proprio dispositivo:** Se preferisci un'alternativa (es. altoparlante da conferenza o cuffie personali), puoi abbinarlo tramite la fotocamera: Impostazioni → Bluetooth.  

#### Connettività, Connettività, Connettività
**Prima di iniziare:** Assicurati di avere una connessione internet tramite:

- **WiFi Locale** (preferito)
- **Rete Mobile** (se fuori dalla portata WiFi)

**Larghezza di banda raccomandata:** 10 Mbps uplink/downlink per lo streaming completo a 360° (~5 Mbps). Larghezza di banda inferiore (1–2 Mbps) funziona solo stando fermi.

##### Test della Velocità di Rete
- **Test in singola posizione:** Qualsiasi speed checker che usi normalmente (es. [Speedtest](https://www.speedtest.net)) per verificare la larghezza di banda in upload.   
- **Test in movimento attraverso il sito:** Dalla fotocamera: Impostazioni → Rete → Test Connessione. Cammina attraverso l'intero spazio per confermare copertura e larghezza di banda.

##### WiFi Locale
- Altamente raccomandato per connessioni stabili.  
- Se l'IT richiede il whitelisting, trova l'indirizzo MAC: Impostazioni → Info → Indirizzo WiFi.

##### Rete Mobile
**Opzione A: Hotspot e SIM forniti nel kit**  

- Fissa l'hotspot GlocalMe all'asta batteria Telesin (magnete).  
- Assicura nessuna interferenza e mantiene la connessione se ti allontani dalla fotocamera.  
- Risoluzione problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).  
  - Abilita il 5G nel Gestore Schede SIM.  
  - Verifica l'APN corretto per la tua regione ([guida configurazione APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Usa il tuo smartphone o hotspot dedicato.  

**Nota Importante:**  
> Mantieni l'hotspot spento mentre sei connesso al WiFi; abilitalo solo quando fuori portata. Il sistema operativo della fotocamera passa dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe passare inavvertitamente all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili potrebbero limitare la larghezza di banda inaspettatamente. Verifica con il tuo operatore i limiti del piano dati, o contatta il supporto Avatour se usi il nostro hotspot e SIM.

##### Situazioni di Bassa Larghezza di Banda
- Pre-registra video delle location per la riproduzione successiva ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Condividi uno stream dalla fotocamera dello smartphone per integrare le aree a bassa larghezza di banda (0,1–0,3 Mbps upload).

##### Nessuna Connettività
- Può essere utilizzato solo video pre-registrato ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri Partecipanti in Loco – Migliori Pratiche

Quando più partecipanti si uniscono a una riunione Avatour live dalla stessa posizione della fotocamera a 360°, una gestione attenta di **audio e larghezza di banda** è cruciale:  

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera a 360°.  
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

#### Altri Partecipanti in Loco – Migliori Pratiche

Quando più partecipanti si uniscono a una riunione Avatour live dalla stessa posizione della fotocamera a 360°, una gestione attenta di **audio e larghezza di banda** è cruciale:  

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera a 360°.  
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **migliori pratiche**:

- **Usa cuffie cablate o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.  
- **Modalità In Loco:** Unisciti alla riunione in modalità In Loco quando sei fisicamente presente vicino alla fotocamera a 360°.  
  - Questa modalità è ottimizzata per l'uso in loco:  
    - Silenzia il microfono e l'altoparlante del partecipante per impostazione predefinita.  
    - **Non** invia il feed della fotocamera del partecipante.  
    - **Non** visualizza il feed della fotocamera a 360° nel browser del partecipante.  
    - Conserva la larghezza di banda di rete, assicurando che la fotocamera a 360° abbia il massimo upload disponibile per lo stream live.  
    - Utile quando un utente vuole condividere dettagli specifici; **puoi condividere la tua fotocamera** per visualizzazioni mirate.  
- **Silenzia quando non stai parlando attivamente:** Previene feedback audio indesiderati e distrazioni.  
- **Usa una rete separata se possibile:** Connetti il tuo smartphone a una rete diversa da quella della fotocamera per ridurre le interferenze.  

Seguire queste linee guida assicura un tour live fluido e di alta qualità sia per i partecipanti in loco che da remoto.

### 5.3 App Fotocamera Avatour

Ecco (1) il Livello Principale, (2) le Impostazioni e (3) i menu delle Impostazioni di Rete.

![App Fotocamera 360° Avatour - Tre Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App Fotocamera 360° Avatour - 3 Menu*

**Quick Capture** - Per la registrazione video a 360° offline. - Per una descrizione dettagliata vedi [Come registri e carichi video a 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Raccomandiamo l'uso di un dispositivo audio esterno (connesso via bluetooth). N.B. Puoi anche fare video e foto standard 2D - cambia semplicemente la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata QC.

**Live Meeting** - Per videoconferenze live a 360°. Vedrai i tuoi workspace e cliccando su uno si avvierà lo stream video live dalla fotocamera a 360°. Prima di poterti unire alla riunione con la tua fotocamera a 360° devi connettere un dispositivo audio via bluetooth. Per una descrizione dettagliata vedi [Come avviare una riunione Live Capture con la tua fotocamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando ospiti una riunione Live Capture con la tua fotocamera a 360°, avrai strumenti di riunione simili disponibili che rispecchiano l'esperienza web. Ecco un link al nostro articolo della Knowledge Base che spiega questi strumenti in maggior dettaglio: [Strumenti App Operatore](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Gallery** - Trova qui tutti i tuoi video e foto a 360° per il caricamento sulla Console Web Avatour.

**Settings** - All'interno delle Impostazioni, hai le seguenti opzioni:

- **Network**: Questa opzione ti permette di cambiare a quale rete WiFi è connessa la fotocamera o eseguire un test di connessione di rete per visualizzare il tuo throughput di streaming
- **Live Capture**: Regola le impostazioni di Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti, o se le lenti protettive della fotocamera sono installate:
  - **Target Frame** **Rate**: Regola il frame rate per il tuo video Live Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma richiederanno più larghezza di banda in upload. Predefinito: 15 fps
  - **Target Bitrate**: Ti permette di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il tuo bitrate target tra 1 Mbps e 10 Mbps. Bitrate più alti risulteranno in una risoluzione video più alta, ma richiederanno più larghezza di banda in upload. Predefinito: 5 Mbps
  - **Optimize Motion**: Questo diminuirà il frame rate video, generando meno carico sulla larghezza di banda in upload della tua rete, e aumenterà il tuo bitrate di streaming. Inoltre, questa opzione aiuta a ridurre il mal di movimento per i partecipanti VR. Predefinito: Off
  - **Protective Lenses**: Questo influenzerà come il video a 360° viene unito a seconda se le lenti protettive sono state installate sulla tua fotocamera. Se non hai lenti protettive, imposta questo su "No". Se hai ricevuto un Kit 3.0, hai lenti protettive preinstallate e dovresti impostare questo su "Yes". Predefinito: Yes

- **Quick Capture**: Regola le impostazioni di Quick Capture in base al tuo frame rate video preferito, alla larghezza di banda disponibile per i caricamenti video registrati, o se le lenti protettive della fotocamera sono installate. Quick Capture ha una risoluzione impostata di 4k che solitamente trova un buon equilibrio tra qualità video e dimensione file. (Per risoluzioni più alte puoi usare le app native della fotocamera, anche sulla PanoX V2, per dettagli vedi [Come registri e carichi video a 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Target Frame Rate**: Regola il frame rate per le tue registrazioni video Quick Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma aumenteranno la dimensione del file video e il tempo di caricamento. Raccomandato: 30 fps
  - **Target Bitrate**: Imposta il bitrate target per i caricamenti Quick Capture tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano la velocità di caricamento, ma diminuiranno la qualità video. Raccomandato: 20 Mbps
  - **Protective Lenses**: *Vedi la sezione Protective Lenses per Live Capture sopra*
- **About**: Visualizza il numero di serie del dispositivo e la versione del software

**Account** - Per il login con il tuo account host o admin Avatour.

## 6. Consigli sulle migliori pratiche {#best-practice-advice}

### 6.1 Primi utilizzi (informali) e familiarizzazione

Per i primi utilizzi e per familiarizzare con la Console Web Avatour e il Kit Chiavi in Mano Avatour, raccomandiamo i seguenti passaggi:

1. Porta il kit a casa e provalo con familiari e amici utilizzando la tua connessione internet domestica.
2. Porta il kit in ufficio e collegalo a una rete aziendale (potrebbero emergere problematiche aziendali, ad es. firewall aziendali - ma dal primo passaggio sai che Avatour funziona e questo è un argomento da risolvere con il tuo team IT con l'aiuto di Avatour).
3. Inizia a usare Avatour sul campo (fuori dal tuo ufficio) nel luogo della riunione dove normalmente i partecipanti remoti dovrebbero recarsi. Potrebbero emergere ulteriori problematiche di connettività. Avatour può aiutare in collaborazione con il tuo team IT.
4. Inizia a usarlo con partecipanti remoti interni ed esterni.

### 6.2 Prima di una riunione dal vivo con video a 360°

- Raccomandiamo di effettuare un tour video a 360° registrato prima di qualsiasi tour dal vivo, se il tempo lo consente, per tre motivi: (1) Avere una soluzione di riserva per il tour dal vivo, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour dal vivo registrato) e (3) iniziare a creare una libreria di video a 360° di tutti i tuoi siti che può essere utile per molti casi d'uso.
- Tutti i componenti del kit devono essere caricati per almeno 90 minuti prima della riunione dal vivo. Raccomandiamo comunque di tenere tutti i dispositivi in carica continua quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni improvvisate non pianificate.
- Avere il kit completamente assemblato (1. base del treppiede + 2. batteria Ulanzi + 3. asta estensibile + 4. cam a 360°).

- Confermare che sia stato creato uno Spazio di Lavoro per ospitare una riunione dal vivo e includere tutti gli Asset pertinenti.

- Invitare tutti i partecipanti alla riunione tramite il tuo Spazio di Lavoro. Questo crea un invito nei calendari di tutti i partecipanti e include il link di invito alla riunione.

- Associare e collegare le cuffie o l'altoparlante bluetooth che intendi usare per il tuo tour alla fotocamera.

- Tutti gli utenti smartphone in loco dovrebbero connettersi da una rete diversa da quella della fotocamera. Questo ridurrà il carico sulla larghezza di banda della rete della fotocamera.

- Se sei solo come operatore della fotocamera, porta con te uno smartphone nel caso volessi condividere la fotocamera dello smartphone e mostrare dettagli fini.

- Confermare che la fotocamera a 360° possa connettersi al tuo WiFi locale.

- Prima di una riunione Avatour, pianifica il percorso che farai attraverso la struttura. Fai una riunione Avatour di prova con la fotocamera e verifica che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Questo può essere visto sullo schermo della fotocamera stessa, o come partecipante remoto andando su Impostazioni e attivando Mostra Bitrate.

- Se noti che alcune aree hanno poca o nessuna larghezza di banda, è meglio scattare immagini o effettuare una registrazione. Queste possono poi essere presentate durante la riunione per la revisione dei partecipanti remoti. Puoi seguire la guida qui che spiega la nostra Acquisizione Rapida per registrare e caricare video/immagini: [Come si registrano e caricano video a 360° con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se hai partecipanti remoti che si uniscono alla riunione e che non hanno mai usato Avatour prima, fornisci loro un breve riepilogo della piattaforma, delle sue funzionalità (video dal vivo a 360°, asset, istantanee, annotazioni, spotlight) e degli strumenti della riunione.

- Puoi iniziare in un'altra soluzione di videoconferenza (ad es. Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudi completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del tuo dispositivo, causandone la disattivazione per Avatour. Inoltre, NON eseguire Avatour E un'altra videoconferenza contemporaneamente poiché questo ridurrà la larghezza di banda disponibile.

- Se prevedi di usare la fotocamera a 360° in un ambiente ad alta temperatura, si raccomanda di usare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la fotocamera si surriscaldi e si spenga automaticamente.

### 6.3 Durante l'utilizzo della cam in loco per una riunione dal vivo con video a 360°

- Quando utilizzi la fotocamera, assicurati di camminare lentamente. Questo aiuta con la qualità video e riduce qualsiasi potenziale interruzione video quando la connessione di rete della fotocamera passa da un punto di accesso WiFi a un altro.

- Tieni la fotocamera davanti a te e sopra il livello degli occhi. Questo permette a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Per le situazioni in cui la fotocamera deve rimanere stabile, usa il supporto del treppiede ed estendi la fotocamera all'altezza corretta, preferibilmente al livello degli occhi.

- Collega sempre la fotocamera alla tua rete WiFi locale quando possibile. Per le aree senza accesso WiFi, usa l'hotspot fornito. L'hotspot ha una scheda SIM che si connetterà a una rete cellulare affidabile vicino a te. Tieni sempre l'hotspot spento quando non in uso all'interno poiché altrimenti la cam a 360° potrebbe connettersi all'hotspot, cosa che non vogliamo al chiuso. Quando sei all'aperto, tieni l'hotspot vicino alla fotocamera a 360°.

- Quando il bitrate sulla fotocamera inizia a scendere sotto i 2 Mbps, cammina più lentamente o fermati completamente finché il segnale non si stabilizza di nuovo. Questo di solito accade quando passi da un Punto di Accesso WiFi a un altro.

- Se sai che la connettività e il video si interromperanno quando ti sposti in una posizione specifica (Esempio: spostandoti da un'area di produzione interna a un'area esterna), avvisa in anticipo i partecipanti remoti.

- Se hai bisogno di mostrare qualcosa in alta definizione o scritte piccole, usa il tuo smartphone o quello di un partecipante in loco per unirti alla riunione e presentare la fotocamera (posteriore) del tuo/suo telefono.

- Se possibile raccomandiamo che una persona aggiuntiva sia presente in loco per aiutare con la condivisione della fotocamera dello smartphone sopra descritta, poiché questo spesso si rivela utile/necessario.

- Idealmente gli utenti smartphone in loco dovrebbero unirsi alla riunione (1) in modalità in loco e (2) su una rete diversa da quella che sta usando la fotocamera per non sottrarre larghezza di banda di upload cruciale dalla cam a 360°.

- Tutti i partecipanti in loco che si uniscono dal loro smartphone dovrebbero essere silenziati, a meno che non stiano parlando attivamente.
