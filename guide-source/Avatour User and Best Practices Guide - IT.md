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
  
## 3. Per i Partecipanti alle Riunioni da Remoto e i Visitatori degli Spazi di Lavoro {#for-remote-meeting-participants-and-workspace-visitors}
<section>

Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito tramite calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota dal vivo al sito** o rivedere insieme gli asset in modo sincrono.

- **Visitare un Workspace (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore in un Workspace** per rivedere gli asset **in modo asincrono** (secondo i tuoi tempi).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare un Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo con "Schermo Piatto" e Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

##### Partecipare a una Riunione Avatour

> **Nota:** Partecipare a una riunione Avatour richiede che tu **conceda i permessi per il microfono**. Accetta eventuali richieste di autorizzazione dal tuo browser.

1. **Tramite invito calendario (consigliato):**  
   - Riceverai tipicamente un **invito tramite calendario** con un **link diretto per partecipare** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando il link verrà automaticamente inserito il **codice riunione di 5 caratteri** e verrai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono limitate agli utenti registrati. In questo caso, l'invito indicherà che devi **effettuare l'accesso per entrare nella riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che dovrai inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'host condivide separatamente un **codice riunione di 5 caratteri**, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.  
   - Se la riunione richiede **l'autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio, Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o microfono, poi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se non riesci ancora a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la rete** sta bloccando l'accesso, e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando si **trasmette una riunione dal vivo da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire direttamente il software Avatour 360° e richiedono l'assistenza di uno smartphone.

##### Visitare un Workspace Avatour (senza partecipare a una Riunione Avatour)

Puoi accedere a un Workspace nei seguenti modi:

- **Workspace Pubblico:**  
  Se il Workspace è pubblico, il link può essere acceduto direttamente—non è richiesto l'accesso.

- **Workspace Limitato:**  
  Se il Workspace è limitato, devi essere aggiunto come **collaboratore** con permessi di **Editor** o **Viewer**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica via email** con un link al Workspace.
  2. Clicca il link nell'email per aprire il Workspace. Se non hai già effettuato l'accesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, il Workspace si aprirà automaticamente.

  In alternativa, puoi accedere su [https://avatour.live/login](https://avatour.live/login) e accedere al Workspace dalla tua **lista di Workspace**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare un workspace da una gamma di visori Meta e Pico compatibili. Per farlo: 

1. Installa la nostra app Avatour dal rispettivo store VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona un Workspace per partecipare a una riunione. Per maggiori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite al sito dal vivo o revisione insieme di asset registrati.  
2. **Workspace (asincroni):** Rivedi e interagisci con gli asset secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata attorno a tre aree principali:

- **Pannello sinistro** – Asset del workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video dal vivo o asset  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu inferiore**.  
Cliccando un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Vista Riunione

Ecco un esempio di una vista in una Riunione Avatour:

![Interfaccia Riunione Avatour con Pannello Asset, Canvas vuoto e Pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Vista Workspace

Ecco un esempio di una vista Workspace:

![Workspace Avatour con Pannello Asset, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace Avatour con Pannello Asset (sinistra), Canvas (centro) e Pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del Menu Inferiore

Il menu inferiore fornisce accesso ai principali controlli e pannelli dell'interfaccia:

**Menu Inferiore Riunione**  

![Menu Inferiore Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu Inferiore Riunione Avatour*

- **Asset** – Rivedi i file del workspace, inclusi video registrati, immagini, snapshot e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti della riunione.  
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Attiva o disattiva l'audio.  
- **Presenta** – Presenta un asset, desktop o feed della webcam (vedi sezione Presenta sotto).  
- **Strumenti Host** (solo host):  
  - **Blocca Focus** – Blocca la vista per tutti i partecipanti.  
  - **Silenzia Tutti** – Silenzia tutti i partecipanti.  
- **Attiva Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Lascia la riunione.  
- **Avvia Registrazione** – Usa questo pulsante per avviare e fermare la registrazione manualmente durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se **l'avvio automatico della registrazione** è abilitato nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate negli asset del workspace.
- **Mappa** – Apri o chiudi il pannello mappa per gli asset con traccia GPS. Cliccando una posizione si salta al punto esatto nel video. La mappa si aggiorna in tempo reale mentre il video viene riprodotto.
- **Partecipanti** – Apri o chiudi il pannello partecipanti.  
- **Info Riunione** – Visualizza il codice riunione, il link di invito e accedi ai tutorial correlati.  

![Info Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Info Riunione Avatour*

- **Impostazioni** – Regola le impostazioni di lingua, audio e video. Per le riunioni video 360° dal vivo, usa **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu inferiore della riunione ti permette di condividere contenuti con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Può essere utilizzata anche durante una riunione video 360° dal vivo per sovrapporre una vista secondaria per primi piani o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Asset** – Presenta un asset dal workspace. Selezionando un asset si apre la **Barra degli strumenti Asset**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per l'asset presentato.

##### Barra degli Strumenti Asset (Riunione)

Quando si presenta un asset in una riunione, la **Barra degli Strumenti Asset** appare sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>si presenta un Asset in una Riunione</u> - spiegati da sinistra a destra.

![Menu Avatour durante la Presentazione di un Asset in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour quando si presenta un Asset in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca su una nota o argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dall'asset.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni dal vivo.  
- **Mostra/Nascondi Punto di Vista (POV)** – Mostra dove ogni partecipante sta guardando nel video 360°.  
- **Note** – Crea note ancorate a momenti specifici nell'asset. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperto → In Corso → Risolto) e condivise tramite link diretti.  

  ![Nota Avatour e Filtro Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

  - **Note con Comando Vocale** – Questi sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note Avatour - Generate con Comando Vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate con Comando Vocale*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che mostra tutte le note, gli argomenti chiave e un riepilogo esecutivo per l'asset. Cliccando un elemento ti porta a quel momento nel video.  

  ![Riepilogo Esecutivo Asset Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour durante la presentazione di un Asset in una Riunione*

  ![Argomenti Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di un Asset in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report dell'asset** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati dall'IA e trascrizioni complete. Puoi anche **scegliere quali elementi includere** prima dell'esportazione.  

  ![Menu Stampa Report Asset Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menu## 4. Per utenti Host e Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}

Quando accedi al tuo Account Utente Avatour, accederai alla **Console Web**.  

### 4.1 Console Web - Panoramica Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai le seguenti voci di menu:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principale*

- **Spazi di lavoro** – Organizza i tuoi contenuti in modo efficiente. Ogni spazio di lavoro contiene **Risorse**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Risorse** – Accedi e gestisci tutte le tue risorse (video, immagini, PDF). Gli amministratori possono visualizzare tutte le risorse dell'account e le risorse condivise sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analisi** – Monitora l'attività delle sessioni, l'utilizzo degli spazi di lavoro e le metriche ROI.  
- **Impostazioni** *(Solo amministratore)* – Configura le impostazioni predefinite di spazi di lavoro, riunioni e risorse in tutta l'organizzazione. Gli amministratori possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo amministratore)* – Gestisci gli utenti registrati e le telecamere 360°.  
- **Accesso dispositivo** – Inserisci il codice visualizzato sulla tua telecamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Accesso dispositivo, Tutorial e Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---

### 4.2 Console Web - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Spazi di lavoro

Gli spazi di lavoro sono unità organizzative flessibili che ti permettono di gestire risorse, collaboratori e riunioni in un unico posto. Puoi creare un nuovo spazio di lavoro con il pulsante **Nuovo Spazio di Lavoro** nell'angolo in alto a destra.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Voce Menu Principale Spazi di lavoro*

Clicca sull'icona della campana per vedere un riepilogo dell'attività dello spazio di lavoro negli ultimi 7 giorni.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività recenti dello spazio di lavoro*

All'interno di uno spazio di lavoro:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Spazio di lavoro con Risorse (sinistra), Canvas (centro), Riunioni (destra)*

- **Risorse** – Gestisci i file allocati a questo spazio di lavoro.  
- **Collaboratori** – 
  Controlla l'accesso agli spazi di lavoro tramite 
  - **Visualizzatore** – Può visualizzare le risorse. L'invito crea un utente Ospite se necessario.  
  - **Editor** – Controllo completo dello spazio di lavoro, stessi diritti dell'Host. L'invito aggiorna l'utente a Host se necessario.  
> Più utenti possono accedere a uno spazio di lavoro contemporaneamente senza una riunione. Gli spazi di lavoro pubblici e le impostazioni di accesso alle riunioni forniscono accessi alternativi.  
- **Report** – Genera un report utilizzando un modello di checklist sulle risorse selezionate dello spazio di lavoro.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report dello spazio di lavoro e Selezione risorse*

- **Mappa** – Visualizza le posizioni delle risorse con GPS su una mappa.  
- **Riunioni** – Organizza riunioni nello spazio di lavoro.  
- **Impostazioni** – Configura le impostazioni predefinite dello spazio di lavoro e delle riunioni:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni dello spazio di lavoro*

**Impostazioni dello spazio di lavoro**

- **Modello di report** – Seleziona il modello di checklist per la reportistica AI.  
- **Abilita notifiche** – Email di riepilogo giornaliero per i cambiamenti di stato delle note.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio di notifiche email*

- **Spazio di lavoro pubblico** – Chiunque abbia il link può visualizzare le risorse direttamente.

**Impostazioni delle riunioni**
  
* **Autenticazione richiesta** – I partecipanti devono accedere.  
* **Consenti accesso ospiti** – Permetti agli utenti non registrati di visualizzare le risorse.  
* **Avvio automatico registrazione / Avvio manuale** – Scegli se le riunioni si registrano automaticamente o vengono avviate manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host esce.  
* **Consenti accesso spettatore** – Partecipa senza microfono o telecamera; comunica tramite chat.  
* **Riunioni protette da password** – Richiedi una password per partecipare.  
* **Mostra domanda sul risparmio di viaggio** – Chiedi ai partecipanti se la riunione ha ridotto gli spostamenti.  

> Le impostazioni possono essere combinate (es. nessun host richiesto ma protetto da password).

---

#### 4.2.2 Risorse

Gestisci tutti i video 360°/2D, immagini e PDF. Carica/scarica risorse, allocale agli spazi di lavoro, condividile con altri utenti, rinominale, stampa/scarica report, attiva la sfocatura dei volti e la sintesi AI.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Risorse*

---

#### 4.2.3 Analisi

Fornisce approfondimenti su riunioni, utilizzo degli spazi di lavoro e metriche ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analisi*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività riunioni e utilizzo spazi di lavoro*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo licenze dispositivo e ROI* 

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
## 6. Best Practice Advice {#best-practice-advice}

### 6.1 First (informal) Uses and Getting Familiar

For your first uses and getting familiar with the Avatour Web Console and the Avatour Turnkey Kit we recommend the following steps:

1. Take the kit home and play with it with family and friends using your home internet connection.
2. Take the kit to the office and connect to a corporate network (corporate issues might evolve, e.g. corporate firewalls - but you know from step one that Avatour is working and this is a topic to sort out by your IT team with the help of Avatour).
3. Start to use Avatour onsite (outside your office) at the meeting location to which remote participants would usually need to travel to. More connectivity topics might evolve. Avatour to help in cooperation with your IT team.
4. Start using with internal and external remote participants.

### 6.2 Before a 360° Video Live Meeting

- We recommend to do a recorded 360° video tour before any live tour if time allows for three reasons: (1) Have a fallback solution for the live tour, (2) have something for documentation and later review (on top of the recorded live tour) and (3) start to create a library of 360° videos of all your sites which can be helpful for many use cases. 
- All kit components charged for at least 90 minutes before the live meeting. We anyway recommend to have all devices on continuous charge when not in use. Like that all devices will always be ready, also for unplanned ad hoc meetings.
- Have the kit fully assembled (1. tripod base + 2. Ulanzi battery + 3. extendable stick + 4. 360° cam).

- Confirm a Workspace is created for hosting a live meeting and include all relevant Assets.

- Invite all participants to the meeting through your Workspace. This creates an invite on all participants calendars, and includes the meeting invite link.

- Pair and connect your bluetooth headphones or speaker you plan to use for your tour to the camera.

- All onsite smartphone users should connect from a different network than the camera’s network. This will reduce the load on the camera’s network bandwidth.

- If you are alone as a camera operator, take a smartphone with you in the case you want to smartphone camera-share and show fine details.

- Confirm the 360 camera can connect to your local WiFi.

- Prior to an Avatour meeting, plan out the route you will take through the facility. Do a test Avatour meeting with the camera, and check that all areas have bitrates above 1 Mbps bandwidth. This can be seen on the camera screen itself, or as a remote participant by going to Settings and activating Show Bitrate.

- If you notice some areas have little to no bandwidth, it is best to take images or a recording. These can then be presented during the meeting for remote participants to review. You can follow the guide here that explains our Quick Capture for recording and uploading videos/images: [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- If you have remote participants joining the meeting who have not used Avatour before, provide them with a short summary of the platform, its functionality (360 live video, assets, snapshots, annotations, spotlight) and the meeting tools.

- You can start in another video conferencing solution (e.g. Teams, Zoom, Google Meet) but before moving over to Avatour, completely close the other video conference application. In some cases, these other applications will prioritize your device’s microphone/speakers/webcam, causing them to be disabled for Avatour. Additionally, do NOT run Avatour AND another video conference at the same time as this will reduce available bandwidth.

- If you are planning to use the 360 camera in a high temperature environment, it’s recommended to use the cooling module (Pilot Pano only). This will help reduce the chances of the camera overheating and shutting down automatically.

### 6.3 When Operating the Cam Onsite for a 360° Video Live Meeting

- When operating the camera, make sure that you are walking slowly. This helps with the video quality and reduces any potential video downtime when the camera’s network connection switches between WiFi access points.

- Hold the camera out in front of you, and above eye level. This allows all remote participants to see the majority of your surrounding area.

- For instances where the camera needs to remain stable, use the tripod stand and extend the camera to the correct height, best to eye-level.

- Always connect the camera to your local WiFi network where possible. For areas without WiFi access, use the provided hotspot. The hotspot has a SIM card that will connect to a reliable cell network near you. Always keep the hotspot switched off when not in use indoors as otherwise the 360° cam could connect to the hotspot which we do not want indoors. When outdoors, keep the hotspot near the 360° camera.

- When the on camera bitrate starts to drop below 2 Mbps, walk slower or stop completely until the signal stabilizes again. This usually happens when you change from one WiFi Access Point to another. 

- If you know the connectivity and video will drop when moving to a specific location (Example: moving from an indoor production area to an outdoor area), let the remote participants know in advance.

- If needing to show something in high detail or small writing, use your own or an onsite participant's smartphone to join the meeting and present your / their phone’s (back-facing) camera.

- If possible we recommend that one additional person is onsite to help with the above described smartphone camera share as this often proves to be helpful / needed.

- Ideally onsite smartphone users should join the meeting (1) in onsite mode and (2) on a different network from that the camera is using to not take away crucial upload bandwidth from the 360° cam.

- All onsite participants joining from their smartphone should be muted, unless actively speaking.
