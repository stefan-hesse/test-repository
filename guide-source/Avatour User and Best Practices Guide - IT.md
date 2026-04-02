# Avatour User and Best Practices Guide

## 1. Per tutti gli utenti di Avatour {#for-all-avatour-users}
Se sei nuovo ad Avatour, le seguenti risorse forniscono un'introduzione utile alla piattaforma e alle sue capacità:

1. [Video Avatour Come funziona](https://avatour.com/how-it-works)  
Una breve panoramica delle funzionalità principali di Avatour e di come la piattaforma consente la collaborazione remota immersiva.
2. [Domande frequenti](https://avatour.com/faqs)  
Risposte alle domande frequenti.
3. [Glossario](https://avatour.com/glossary)  
Definizioni dei termini e dei concetti chiave di Avatour utilizzati frequentemente.
4. Sito web  
Dai un'occhiata soprattutto alla pagina [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate Casi d'uso e Settori per scoprire come Avatour può supportare le tue esigenze specifiche.## 2. Tipi di Utenti Avatour  {#avatour-user-types}

### 2.1 Partecipanti alla riunione (Nessun account richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi per un account Avatour.
Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono accedere per l'autenticazione.

Gli utenti accedono alla riunione come segue:

- Ricevono un invito del calendario dall'host.
- Utilizzano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'host ne ha abilitata una.
- I partecipanti possono partecipare senza un account Avatour a meno che la riunione non sia ristretta e richieda l'accesso per l'autenticazione.

#### 2.1.1 Partecipante

- Può partecipare e interagire completamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, utilizzare un microfono, presentare, riprodurre/mettere in pausa Asset o acquisire Snapshot.
- Massimo 10 spettatori per riunione.
- Insieme ai partecipanti, una riunione può ospitare fino a 30 partecipanti.### 2.2 Utenti Registrati

Gli utenti registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitati dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di iscrizione** per completare la configurazione dell'account e impostare una password.  
- **Invitati da Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce all'utente l'accesso a livello Host.  
- **SSO auto-provisioning (solo Enterprise/Business tier):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account con provisioning SSO vengono aggiunti al **gruppo Guest**, a meno che non sia diversamente specificato tramite **mapping dei gruppi SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza ai gruppi direttamente anche quando SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in più modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).  
- **Provisioning SSO:** Per i clienti Enterprise o Business tier con SSO abilitato, l'IdP può fornire automaticamente account e assegnare l'appartenenza ai gruppi, che definisce il ruolo sulla piattaforma dell'utente.  
- **Utenti invitati da Host:** Gli Host possono invitare altri utenti come collaboratori Editor a Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Pratica Consigliata Consigliata (Clienti Enterprise):**  
Per le organizzazioni che prevedono un gran numero di utenti che hanno bisogno di accesso ad Avatour, si consiglia di **integrare Single Sign-On (SSO)** e gestire gli utenti e le appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione dei gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo di accesso coerente.

#### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.  
- Possono **visualizzare Assets** all'interno dei Workspace in cui sono stati aggiunti come **collaboratori Viewer**.  
- Non possono creare workspace, ospitare riunioni o caricare contenuti.  
- Gli account Guest con provisioning SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

#### 2.2.2 Utenti Licenziati (Accesso Web Console)

##### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori a un workspace, **ospitare riunioni live**, caricare **Quick Captures**.  
- Hanno accesso alla **Host Dashboard** e **Operator App** su fotocamere 360° supportate.  

##### Utenti Admin (Gruppo: Admin)

- Include tutte le funzionalità Host più l'amministrazione completa dell'account.

**I privilegi Admin aggiuntivi includono:**

**Gestione Account**  

- Creare nuovi utenti e assegnarli a gruppi.
- Reimpostare le password quando gestite da Avatour (non applicabile quando SSO è abilitato). 
- Aggiornare utenti Guest a Host.  
- Disattivare utenti (gli account Admin devono essere prima convertiti a Host prima dell'eliminazione).  
- Trasferire asset da un utente Host a un altro durante l'eliminazione.

**Impostazioni**  

- Configurare **impostazioni di sicurezza a livello di organizzazione** per asset, workspace e riunioni ospitate sulla piattaforma (ad esempio, se un Host deve essere presente per avviare una riunione, se i volti devono essere offuscati su tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare **funzionalità AI** o **registrazione**.  
- Applicare branding aziendale in modo coerente sulla piattaforma se è configurato un **dominio personalizzato**.
  

**Asset e Analytics** 
 
- Visualizzare tutti gli Asset caricati da qualsiasi utente dell'organizzazione.  
- Rivedere l'utilizzo della piattaforma in tutta l'organizzazione.

---

#### 2.2.3 Autorizzazioni Collaboratore Workspace

Le autorizzazioni Workspace definiscono cosa un utente può fare **all'interno di uno specifico Workspace**. Queste sono separate dall'appartenenza ai gruppi a livello di piattaforma (Guest, Host, Admin).

- **Collaboratore Editor:** Gli utenti con questa autorizzazione possono:
  - Gestire Asset (caricare, rimuovere, offuscare volti, generare riepiloghi)  
  - Gestire le impostazioni della riunione (abilitare/disabilitare la registrazione, consentire o rimuovere partecipanti)  
  - Pianificare e ospitare riunioni live  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dal Workspace  

- **Collaboratore Viewer:** Gli utenti con questa autorizzazione hanno accesso di sola lettura agli Asset del Workspace. **Non possono modificare gli Asset, gestire le riunioni o gestire i collaboratori**, ma **possono creare Note su Assets**.## 3. Per i partecipanti alle riunioni remote e i visitatori dello spazio di lavoro {#for-remote-meeting-participants-and-workspace-visitors}
Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipa a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota dal vivo del sito** o rivedere gli asset insieme in modo sincrono.

- **Visita uno Workspace (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore di uno Workspace** per rivedere gli asset **in modo asincrono** (secondo il tuo programma).### 3.1 Come partecipare a una riunione Avatour e visitare uno spazio di lavoro Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi dispositivo "Flat Screen" con browser web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.

##### Partecipazione a una riunione Avatour

> **Nota:** La partecipazione a una riunione Avatour richiede che tu **consenta i permessi del microfono**. Accetta eventuali richieste di permesso dal tuo browser.

1. **Tramite invito del calendario (consigliato):**  
   - In genere riceverai un **invito del calendario** con un **link di accesso diretto** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Facendo clic sul link, il **codice riunione di 5 caratteri** verrà compilato automaticamente e verrai indirizzato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono riservate agli utenti registrati. In questo caso, l'invito indicherà che devi **accedere per accedere alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'host condivide un **codice riunione di 5 caratteri** separatamente, vai a [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'host.  
   - Se la riunione richiede **autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il tuo microfono non funzionano, potrebbe essere in uso da un'altra applicazione (ad esempio Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o il tuo microfono, quindi esci e partecipa di nuovo alla riunione Avatour.  

> **Suggerimento 2:** Se ancora non riesci a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la tua rete** sta bloccando l'accesso, e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando **trasmetti una riunione in diretta da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire il software Avatour 360° direttamente e richiedono uno smartphone per assistere.

##### Visitare uno spazio di lavoro Avatour (senza partecipare a una riunione Avatour)

Puoi accedere a uno spazio di lavoro nei seguenti modi:

- **Spazio di lavoro pubblico:**  
  Se lo spazio di lavoro è pubblico, il link è accessibile direttamente — nessun accesso richiesto.

- **Spazio di lavoro limitato:**  
  Se lo spazio di lavoro è limitato, devi essere aggiunto come **collaboratore** con autorizzazioni **Editor** o **Viewer**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica email** con un link allo spazio di lavoro.
  2. Fai clic sul link nell'email per aprire lo spazio di lavoro. Se non sei già connesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta connesso, lo spazio di lavoro si aprirà automaticamente.

  In alternativa, puoi accedere a [https://avatour.live/login](https://avatour.live/login) e accedere allo spazio di lavoro dalla tua **lista di spazi di lavoro**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare uno spazio di lavoro da una gamma di visori Meta e Pico compatibili. Per farlo: 

1. Installa la nostra app Avatour dal rispettivo app store VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona uno spazio di lavoro per partecipare a una riunione. Per ulteriori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Strumenti di Collaborazione per Riunioni e Spazi di Lavoro {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite in loco dal vivo o revisione congiunta di asset registrati.  
2. **Spazi di lavoro (asincroni):** Rivedi e interagisci con gli asset secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra le riunioni e gli spazi di lavoro, con alcune differenze dovute al contesto sincrono rispetto a quello asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia di Avatour è organizzata intorno a tre aree principali:

- **Pannello sinistro** – Asset dello spazio di lavoro e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video dal vivo o asset  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu inferiore**.  
Facendo clic su un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Visualizzazione della Riunione

Ecco un esempio di visualizzazione in una Riunione di Avatour:

![Interfaccia Avatour Meeting con pannello Asset, Canvas vuoto e pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione di Avatour con pannello Asset (sinistra), Canvas (centro) e pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Visualizzazione dello Spazio di Lavoro

Ecco un esempio di visualizzazione dello Spazio di Lavoro:

![Avatour Workspace con pannello Asset, Canvas vuoto e pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Spazio di Lavoro di Avatour con pannello Asset (sinistra), Canvas (centro) e pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del Menu Inferiore

Il menu inferiore fornisce accesso ai controlli dell'interfaccia principale e ai pannelli:

**Menu Inferiore della Riunione**  

![Menu Inferiore della Riunione di Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu Inferiore della Riunione di Avatour*

- **Asset** – Rivedi i file dello spazio di lavoro, inclusi video registrati, immagini, snapshot e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti della riunione.  
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Disattiva o attiva l'audio.  
- **Presenta** – Presenta un asset, il desktop o il feed della webcam (vedi la sezione Presenta di seguito).  
- **Strumenti Host** (solo per host):  
  - **Blocca Focus** – Blocca la visualizzazione per tutti i partecipanti.  
  - **Disattiva Audio a Tutti** – Disattiva l'audio per tutti i partecipanti.  
- **Abilita Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Abbandona la riunione.  
- **Avvia Registrazione** – Utilizza questo pulsante per avviare e interrompere la registrazione manualmente durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se la **registrazione automatica** è abilitata nelle impostazioni dello spazio di lavoro. In entrambi i casi, le registrazioni vengono salvate negli asset dello spazio di lavoro.
- **Mappa** – Apri o chiudi il pannello della mappa per gli asset con un tracciato GPS. Facendo clic su una posizione vai al punto esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Partecipanti** – Apri o chiudi il pannello dei partecipanti.  
- **Informazioni Riunione** – Visualizza il codice della riunione, il link di invito e accedi ai tutorial correlati.  

![Informazioni Riunione di Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Informazioni Riunione di Avatour*

- **Impostazioni** – Regola le impostazioni di lingua, audio e video. Per le riunioni video 360° dal vivo, utilizza **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu inferiore della riunione ti consente di condividere il contenuto con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Può anche essere utilizzato durante una riunione video 360° dal vivo per sovrapporre una visualizzazione secondaria per ingrandimenti o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Asset** – Presenta un asset dallo spazio di lavoro. La selezione di un asset apre la **barra degli strumenti Asset**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per l'asset in presentazione.

##### Barra degli Strumenti Asset (Riunione)

Quando presenti un asset in una riunione, la **barra degli strumenti Asset** appare sopra il canvas. Ecco gli strumenti e le opzioni di menu disponibili quando <u>presenti un Asset in una Riunione</u> - spiegati da sinistra a destra.

![Menu di Avatour durante la Presentazione di un Asset in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu di Avatour quando presenti un Asset in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Fai clic su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Riproduci / Pausa**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dall'asset.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni dal vivo.  
- **Mostra/Nascondi Punto di Vista (POV)** – Visualizza dove ogni partecipante sta guardando nel video 360°.  
- **Note** – Crea note ancorate a momenti specifici dell'asset. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperta → In Corso → Risolta) e condivise tramite link diretti.  

  ![Nota di Avatour e Filtri Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota di Avatour e Filtri Note*

  - **Note Comando Vocale** – Questi sono segnaposti generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "scrivi una nota". Queste note vengono visualizzate sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note di Avatour - Generate da Comando Vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note di Avatour - Generate da Comando Vocale*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che visualizza tutte le note, gli argomenti chiave e un riepilogo esecutivo per l'asset. Facendo clic su un elemento accedi a quel momento del video.  

  ![Riepilogo Esecutivo Asset di Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo di Avatour durante la Presentazione di un Asset in una Riunione*

  ![Argomenti di Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti di Avatour durante la Presentazione di un Asset in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report dell'asset** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati da IA e trascrizioni complete. Puoi anche **scegliere quali elementi includere** prima dell'esportazione.  

  ![Menu di Stampa Report Asset di Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menu di Stampa / Download Report Asset di Avatour*  

  ![Menu di Selezione Elementi Report Asset di Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menu di Selezione Elementi Report Asset di Avatour*

- **Condividi Link** – Condividi un link a una nota specifica o a una scena nell'asset.  
- **Sottotitoli Chiusi (CC)** – Visualizza la trascrizione del testo sullo schermo durante la riproduzione del video.

##### Barra degli Strumenti Asset (Spazio di Lavoro)

Quando rivedi un asset in uno spazio di lavoro, la barra degli strumenti è simile ma ottimizzata per l'uso individuale:

![Menu di Avatour durante la Presentazione di un Asset al di fuori di una riunione, ad es. durante la visita di uno spazio di lavoro](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu di Avatour quando presenti un Asset in uno Spazio di Lavoro*

- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dalla traccia audio. Fai clic in qualsiasi punto della timeline per scorrere il video. Fai clic su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Riproduci / Pausa**.  
- **Snapshot, Note, Pannello Note e Riepilogo, Condividi Link, Sottotitoli Chiusi**  
- Non disponibili: **Spotlight, POV** (richiedono partecipanti dal vivo)  
- Controlli aggiuntivi:
  - **Salti di 10 secondi** – Avanza/Indietreggia  
  - **Velocità di Riproduzione** – Regola la velocità (0,5×–2×)  
  - **Taglia Video** – Taglia l'inizio o la fine dell'asset## 4. Per utenti Host e Admin - Avatour Web Console {#for-host-and-admin-users-avatour-web-console}
Quando accedi al tuo Account Utente Avatour, accederai alla **Web Console**.### 4.1 Web Console - Panoramica Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai i seguenti elementi di menu:

![Avatour Web Console - Menu Principale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Avatour Web Console - Menu Principale*

- **Workspaces** – Organizza i tuoi contenuti in modo efficiente. Ogni workspace contiene **Assets**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Assets** – Accedi e gestisci tutti i tuoi asset (video, immagini, PDF). Gli amministratori possono visualizzare tutti gli asset dell'account e gli asset condivisi sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analytics** – Traccia l'attività della sessione, l'utilizzo del workspace e le metriche ROI.  
- **Impostazioni** *(Solo amministratore)* – Configura i valori predefiniti di workspace, riunione e asset all'interno dell'organizzazione. Gli amministratori possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo amministratore)* – Gestisci gli utenti registrati e le fotocamere 360°.  
- **Accesso dispositivo** – Immetti il codice visualizzato sulla tua fotocamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Le sezioni come Profilo, Accesso dispositivo, Tutorial ed Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---### 4.2 Web Console - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Workspaces

Gli spazi di lavoro sono unità organizzative flessibili che ti permettono di gestire risorse, collaboratori e riunioni in un unico luogo. Puoi creare un nuovo spazio di lavoro con il pulsante **New Workspace** nell'angolo in alto a destra.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Main Menu Item Workspaces*

Fai clic sull'icona della campana per visualizzare un riepilogo dell'attività dello spazio di lavoro degli ultimi 7 giorni.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Workspace Recent Activities*

All'interno di uno spazio di lavoro:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace with Assets (left), Canvas (center), Meetings (right)*

- **Assets** – Gestisci i file allocati a questo spazio di lavoro.  
- **Collaborators** – 
  Controlla l'accesso agli spazi di lavoro tramite 
  - **Viewer** – Può visualizzare le risorse. L'invito crea un utente Guest se necessario.  
  - **Editor** – Controllo completo dello spazio di lavoro, gli stessi diritti dell'Host. L'invito aggiorna l'utente a Host se necessario.  
> Più utenti possono accedere a uno spazio di lavoro contemporaneamente senza una riunione. Gli spazi di lavoro pubblici e le impostazioni di accesso alle riunioni forniscono accessi alternativi.  
- **Report** – Genera un report utilizzando un modello di checklist sulle risorse dello spazio di lavoro selezionato.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Workspace Report and Asset Selection*

- **Map** – Visualizza le posizioni delle risorse abilitate per GPS su una mappa.  
- **Meetings** – Organizza riunioni nello spazio di lavoro.  
- **Settings** – Configura i valori predefiniti dello spazio di lavoro e delle riunioni:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Workspace Settings*

**Workspace Settings**

- **Report Template** – Seleziona il modello di checklist per il report AI.  
- **Enable Notifications** – Email con digest giornaliero per le modifiche dello stato delle note.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Email Notifications Example*

- **Public Workspace** – Chiunque disponga del link può visualizzare le risorse direttamente.

**Meeting Settings**
  
* **Authentication required** – I partecipanti devono effettuare l'accesso.  
* **Allow guest access** – Permetti agli utenti non registrati di visualizzare le risorse.  
* **Auto-Start Recording / Manual Start** – Scegli se le riunioni vengono registrate automaticamente o avviate manualmente.  
* **Require host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host se ne va.  
* **Allow spectator access** – Accedi senza microfono o fotocamera; comunica tramite chat.  
* **Password protected meetings** – Richiedi una password per partecipare.  
* **Show Travel-Savings Question** – Chiedi ai partecipanti se la riunione ha ridotto i viaggi.  

> Le impostazioni possono essere combinate (ad es., nessun host richiesto ma protetto da password).

---

#### 4.2.2 Assets

Gestisci tutti i video 360°/2D, le immagini e i PDF. Carica/scarica risorse, assegnale agli spazi di lavoro, condividile con altri utenti, rinomina, stampa/scarica report, attiva la sfocatura dei volti e il riassunto AI.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Main Menu Item Assets*

---

#### 4.2.3 Analytics

Fornisce informazioni dettagliate su riunioni, utilizzo dello spazio di lavoro e metriche di ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Analytics Overview*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Meeting Activity & Workspace Usage*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Device License Usage & ROI*## 5. In loco - Come utilizzare il kit chiavi in mano di Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Iniziare
[Guida Rapida – Avatour Turnkey Kit 3.1 (Configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per estrarre, assemblare e accendere la tua fotocamera.

---### 5.2 Suggerimenti Utili

#### Batteria Esterna – Riunioni più Lunghe e Termiche Migliori

- **Se il tuo kit include una batteria Ulanzi:** Collegala tra la base del treppiede e il bastone estensibile, quindi connetti la batteria alla fotocamera tramite USB-C.

- **Se il tuo kit include un battery stick Telesin:** Monta la fotocamera direttamente sul battery stick estensibile Telesin e collegalo tramite USB-C.

Utilizzando la batteria esterna:

1. Estende la durata totale della batteria da ~40 minuti (solo batteria fotocamera) a ~3 ore.
2. Aggiunge stabilità al setup della fotocamera.
3. Aiuta a prevenire possibili surriscaldamenti.

> Consigliamo di utilizzare sempre la batteria esterna dall'inizio, soprattutto per le riunioni live.

#### Considerazioni Audio per Riunioni Live e Registrazioni

- **Ambienti rumorosi:**
  Utilizza le cuffie Shokz incluse nel tuo kit per una cattura audio chiara.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).
  - **Modalità Abbinamento Bluetooth:** Con l'auricolare spento, tieni premuto il pulsante "+" per 5 secondi (LED lampeggia blu/rosso).
  - **Volume:** Utilizza i pulsanti "+" e "-".

- **Ambienti più silenziosi / più partecipanti vicini alla fotocamera:**
  Utilizza l'altoparlante clip-on NoxGear. Non ha la stessa fedeltà di altoparlanti per conferenze (ad es. Jabra Speak), ma è facile da clip sulla camicia e cattura efficacemente le voci nelle vicinanze.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Play/Pausa per 2 secondi.
  - **Modalità Abbinamento Bluetooth:** Entra automaticamente in modalità abbinamento quando acceso (LED lampeggia blu/rosso; blu fisso quando abbinato).
  - **Volume:** Utilizza i pulsanti "+" e "-".

- **Utilizzando il tuo dispositivo:** Se preferisci un'alternativa (ad es. un altoparlante per conferenze o un auricolare personale), puoi abbinarlo tramite la fotocamera: Impostazioni → Bluetooth.

#### Connettività, Connettività, Connettività
**Prima di iniziare:** Assicurati della connessione internet tramite:

- **WiFi locale** (consigliato)
- **Rete mobile** (se fuori dalla portata del WiFi)

**Larghezza di banda consigliata:** 10 Mbps upload/download per lo streaming 360° completo (~5 Mbps). Una larghezza di banda più bassa (1–2 Mbps) funziona solo quando si è fermi.

##### Prova Velocità di Rete
- **Test in una singola posizione:** Qualsiasi verificatore di velocità che usi normalmente (ad es. [Speedtest](https://www.speedtest.net)) per verificare la larghezza di banda di upload.
- **Test a piedi sul sito:** Dalla fotocamera: Impostazioni → Rete → Test Connessione. Cammina attraverso l'intero spazio per confermare la copertura e la larghezza di banda.

##### WiFi Locale
- Altamente consigliato per connessioni stabili.
- Se l'IT richiede l'inserimento nella lista bianca, trova l'indirizzo MAC: Impostazioni → Informazioni → Indirizzo WiFi.

##### Rete Mobile
**Opzione A: Hotspot e SIM forniti nel kit**

- Collega l'hotspot GlocalMe al battery stick Telesin (magnete).
- Garantisce nessuna interferenza e mantiene la connessione se ti allontani dalla fotocamera.
- Risoluzione dei problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).
  - Abilita 5G in SIM Card Manager.
  - Verifica il corretto APN per la tua regione ([guida configurazione APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Utilizza il tuo smartphone o hotspot dedicato.

**Nota Importante:**
> Mantieni l'hotspot spento quando connesso a WiFi; abilitalo solo quando fuori dalla portata. Il sistema operativo della fotocamera passa dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe passare involontariamente all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili potrebbero limitare la larghezza di banda inaspettatamente. Verifica con il tuo operatore i limiti del piano dati, o contatta il supporto Avatour se utilizzi il nostro hotspot e SIM.

##### Situazioni di Larghezza di Banda Bassa
- Pre-registra video della posizione per la riproduzione successiva ([guida registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Condividi uno stream della fotocamera dello smartphone per integrare le aree con bassa larghezza di banda (0,1–0,3 Mbps upload).

##### Nessuna Connettività
- Solo i video pre-registrati possono essere utilizzati ([guida registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri Partecipanti in Loco – Migliori Pratiche

Quando più partecipanti si uniscono a una riunione Avatour live dalla stessa posizione della fotocamera 360°, la gestione attenta dell'**audio e della larghezza di banda** è cruciale:

- Ogni smartphone, tablet o laptop connesso in loco consuma la larghezza di banda della rete e può avere un impatto negativo sul feed della fotocamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

#### Altri Partecipanti in Loco – Migliori Pratiche

Quando più partecipanti si uniscono a una riunione Avatour live dalla stessa posizione della fotocamera 360°, la gestione attenta dell'**audio e della larghezza di banda** è cruciale:

- Ogni smartphone, tablet o laptop connesso in loco consuma la larghezza di banda della rete e può avere un impatto negativo sul feed della fotocamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **migliori pratiche**:

- **Utilizza cuffie cablate o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.
- **Modalità In Loco:** Unisciti alla riunione in modalità In Loco quando sei fisicamente vicino alla fotocamera 360°.
  - Questa modalità è ottimizzata per l'uso in loco:
    - Disattiva il microfono e l'altoparlante del partecipante per impostazione predefinita.
    - **Non** invia il feed della fotocamera del partecipante.
    - **Non** visualizza il feed della fotocamera 360° nel browser del partecipante.
    - Conserva la larghezza di banda della rete, garantendo che la fotocamera 360° abbia il massimo upload disponibile per il live stream.
    - Utile quando un utente vuole condividere dettagli specifici; puoi **ricondividere la tua fotocamera** per visualizzazioni mirate.
- **Disattiva quando non parli attivamente:** Previene feedback audio indesiderati e distrazioni.
- **Utilizza una rete separata se possibile:** Connetti il tuo smartphone a una rete diversa da quella della fotocamera per ridurre le interferenze.

Seguire queste linee guida garantisce un tour live fluido e di alta qualità sia per i partecipanti in loco che remoti.### 5.3 App Fotocamera Avatour

Ecco (1) il menu di livello superiore, (2) Impostazioni e (3) menu Impostazioni di rete.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360° Camera App - 3 Menu*

**Quick Capture** - Per la registrazione di video 360° offline. - Per una descrizione dettagliata, consulta [Come registrare e caricare video 360 con l'app Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Ti consigliamo di utilizzare un dispositivo audio esterno (collegato via bluetooth). N.B. Puoi anche fare video e foto 2D standard - semplicemente cambia la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata QC.

**Live Meeting** - Per videoconferenza 360° in diretta. Vedrai i tuoi spazi di lavoro e facendo clic su uno avvierai lo streaming video in diretta dalla fotocamera 360°. Prima di poter partecipare alla riunione con la tua fotocamera 360°, devi connettere un dispositivo audio via bluetooth. Per una descrizione dettagliata, consulta [Come avviare una riunione Live Capture con la tua fotocamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando ospiti una riunione Live Capture con la tua fotocamera 360, avrai a disposizione strumenti di riunione simili a quelli che rispecchiano l'esperienza web. Ecco un collegamento al nostro articolo della Knowledge Base che spiega questi strumenti in maggior dettaglio: [Operator App Tools](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Gallery** - Qui troverai tutti i tuoi video e foto 360° da caricare nella Console Web Avatour.

**Impostazioni** - All'interno delle Impostazioni, hai le seguenti opzioni:

- **Rete**: Questa opzione ti permette di cambiare a quale rete WiFi è connessa la fotocamera o di eseguire un test di connessione di rete per visualizzare il tuo throughput di streaming
- **Live Capture**: Regola le impostazioni di Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti, o se gli obiettivi protettivi della tua fotocamera sono installati:
  - **Target Frame Rate**: Regola la frequenza fotogrammi per il tuo video Live Capture tra 15 fps, 24 fps e 30 fps. Frequenze fotogrammi più alte producono video più fluidi, ma richiederanno più larghezza di banda per l'upload. Predefinito: 15 fps
  - **Target Bitrate**: Ti permette di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il tuo target bitrate tra 1 Mbps e 10 Mbps. Bitrate più alti risulteranno in una risoluzione video più alta, ma richiederanno più larghezza di banda per l'upload. Predefinito: 5 Mbps
  - **Optimize Motion**: Questo diminuirà la frequenza fotogrammi video, generando meno carico sulla larghezza di banda di upload della tua rete, e aumenterà il tuo bitrate di streaming. Inoltre, questa opzione aiuta a ridurre la cinetosi per i partecipanti VR. Predefinito: Off
  - **Protective Lenses**: Questo influenzerà il modo in cui il video 360° viene cucito a seconda se gli obiettivi protettivi sono stati installati sulla tua fotocamera. Se non hai obiettivi protettivi, imposta questo su "No". Se hai ricevuto un Kit 3.0, hai obiettivi protettivi preinstallati e dovresti impostare questo su "Sì". Predefinito: Sì

- **Quick Capture**: Regola le impostazioni di Quick Capture in base alla frequenza fotogrammi video preferita, alla larghezza di banda disponibile per i caricamenti di video registrati, o se gli obiettivi protettivi della tua fotocamera sono installati. Quick Capture ha una risoluzione impostata di 4k che di solito rappresenta un buon equilibrio tra qualità video e dimensione file. (Per risoluzioni più alte puoi utilizzare le app fotocamera native, anche su PanoX V2, per i dettagli consulta [Come registrare e caricare video 360 con l'app Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Target Frame Rate**: Regola la frequenza fotogrammi per le tue registrazioni video Quick Capture tra 15 fps, 24 fps e 30 fps. Frequenze fotogrammi più alte producono video più fluidi, ma aumenteranno le dimensioni del file video e il tempo di upload. Consigliato: 30 fps
  - **Target Bitrate**: Imposta il target bitrate per i caricamenti di Quick Capture tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano la velocità di upload, ma diminuiranno la qualità video. Consigliato: 20 Mbps
  - **Protective Lenses**: *Consulta la sezione Protective Lenses per Live Capture sopra*
- **About**: Visualizza il numero di serie del dispositivo e la versione del software

**Account** - Per accedere con il tuo account host o admin Avatour.## 6. Consigli sulle Migliori Pratiche {#best-practice-advice}

### 6.1 Primi usi (informali) e familiarizzazione

Per i vostri primi usi e per familiarizzarvi con la Console Web di Avatour e il Kit Turnkey di Avatour consigliamo i seguenti passaggi:

1. Portate il kit a casa e provate con la famiglia e gli amici utilizzando la vostra connessione internet domestica.
2. Portate il kit in ufficio e collegatelo a una rete aziendale (potrebbero emergere problemi aziendali, ad es. firewall aziendali - ma sapete dal passaggio uno che Avatour funziona e questo è un argomento da risolvere dal vostro team IT con l'aiuto di Avatour).
3. Iniziate a utilizzare Avatour in loco (fuori dal vostro ufficio) nella sede della riunione dove i partecipanti remoti di solito dovrebbero viaggiare. Potrebbero emergere altri argomenti di connettività. Avatour aiuterà in cooperazione con il vostro team IT.
4. Iniziate a utilizzare con partecipanti remoti interni ed esterni.### 6.2 Prima di una riunione live in video a 360°

- Consigliamo di effettuare un tour in video a 360° registrato prima di qualsiasi tour live se il tempo lo consente, per tre motivi: (1) Avere una soluzione di fallback per il tour live, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour live registrato) e (3) iniziare a creare una libreria di video a 360° di tutti i vostri siti, utile per molti casi d'uso.
- Tutti i componenti del kit devono essere caricati per almeno 90 minuti prima della riunione live. In ogni caso, consigliamo di mantenere tutti i dispositivi in carica continua quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni ad hoc non pianificate.
- Avere il kit completamente assemblato (1. base treppiede + 2. batteria Ulanzi + 3. bastone estensibile + 4. fotocamera 360°).

- Confermare che uno Workspace è stato creato per ospitare una riunione live e includere tutti gli Asset rilevanti.

- Invitare tutti i partecipanti alla riunione tramite il vostro Workspace. Questo crea un invito sui calendari di tutti i partecipanti e include il link di invito alla riunione.

- Accoppiare e connettere le cuffie Bluetooth o l'altoparlante che intendete utilizzare per il vostro tour alla fotocamera.

- Tutti gli utenti di smartphone in loco dovrebbero connettersi da una rete diversa da quella della fotocamera. Questo ridurrà il carico sulla larghezza di banda della rete della fotocamera.

- Se siete soli come operatore della fotocamera, portate con voi uno smartphone nel caso in cui vogliate condividere la fotocamera dello smartphone e mostrare i dettagli.

- Confermare che la fotocamera 360 può connettersi al vostro WiFi locale.

- Prima di una riunione Avatour, pianificate il percorso che seguirete nella struttura. Effettuate una riunione Avatour di prova con la fotocamera e verificate che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Ciò può essere visualizzato sulla schermata della fotocamera stessa, oppure come partecipante remoto andando in Impostazioni e attivando Mostra bitrate.

- Se notate che alcune aree hanno poca o nessuna larghezza di banda, è meglio scattare foto o effettuare una registrazione. Questi possono essere presentati durante la riunione per i partecipanti remoti da rivedere. Potete seguire la guida qui che spiega il nostro Quick Capture per la registrazione e il caricamento di video/immagini a 360°: [Come registrare e caricare video a 360° con l'app Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se avete partecipanti remoti che si uniscono alla riunione e non hanno mai usato Avatour prima, fornite loro un breve riepilogo della piattaforma, delle sue funzionalità (video live a 360°, asset, snapshot, annotazioni, spotlight) e degli strumenti della riunione.

- Potete iniziare con un'altra soluzione di videoconferenza (ad es. Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudete completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del vostro dispositivo, causandone la disattivazione per Avatour. Inoltre, NON eseguite Avatour E un'altra videoconferenza contemporaneamente poiché ciò ridurrà la larghezza di banda disponibile.

- Se state pianificando di utilizzare la fotocamera 360 in un ambiente ad alta temperatura, si consiglia di utilizzare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la fotocamera si surriscaldi e si spenga automaticamente.### 6.3 Quando si utilizza la fotocamera in loco per una riunione video live a 360°

- Quando si utilizza la fotocamera, assicurarsi di camminare lentamente. Questo aiuta con la qualità del video e riduce qualsiasi potenziale tempo di inattività video quando la connessione di rete della fotocamera passa tra i punti di accesso WiFi.

- Tenere la fotocamera di fronte a voi e sopra il livello degli occhi. Questo consente a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Nei casi in cui la fotocamera deve rimanere stabile, utilizzare il supporto treppiede e estendere la fotocamera all'altezza corretta, preferibilmente al livello degli occhi.

- Collegare sempre la fotocamera alla rete WiFi locale quando possibile. Per le aree senza accesso WiFi, utilizzare l'hotspot fornito. L'hotspot dispone di una scheda SIM che si collegherà a una rete cellulare affidabile nelle vostre vicinanze. Mantenere sempre l'hotspot spento quando non in uso al chiuso, altrimenti la fotocamera 360° potrebbe connettersi all'hotspot, cosa che non vogliamo al chiuso. Quando all'aperto, mantenere l'hotspot vicino alla fotocamera 360°.

- Quando il bitrate della fotocamera inizia a scendere al di sotto di 2 Mbps, camminare più lentamente o fermarsi completamente fino a quando il segnale non si stabilizza di nuovo. Questo di solito accade quando si passa da un punto di accesso WiFi a un altro.

- Se sapete che la connettività e il video diminuiranno quando vi sposterete in una posizione specifica (Esempio: spostamento da un'area di produzione interna a un'area esterna), informate in anticipo i partecipanti remoti.

- Se è necessario mostrare qualcosa con grande dettaglio o con scritte piccole, utilizzare il proprio o lo smartphone di un partecipante in loco per partecipare alla riunione e presentare la fotocamera posteriore del vostro/loro telefono.

- Se possibile consigliamo che una persona aggiuntiva sia in loco per aiutare con la condivisione dello schermo della fotocamera dello smartphone come descritto sopra, in quanto spesso si rivela utile/necessaria.

- Idealmente gli utenti di smartphone in loco dovrebbero partecipare alla riunione (1) in modalità in loco e (2) su una rete diversa da quella utilizzata dalla fotocamera per non sottrarre la larghezza di banda di caricamento cruciale dalla fotocamera 360°.

- Tutti i partecipanti in loco che partecipano dal loro smartphone dovrebbero essere silenziati, a meno che non stiano parlando attivamente.