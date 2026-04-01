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
Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito nel calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota in tempo reale del sito** o rivedere insieme le risorse in modo sincrono.

- **Visitare uno Spazio di Lavoro (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore in uno Spazio di Lavoro** per rivedere le risorse in modo **asincrono** (secondo i tuoi tempi).### 3.1 Come Partecipare a una Riunione Avatour e Visitare uno Spazio di Lavoro Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo "Schermo Piatto" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

##### Partecipare a una Riunione Avatour

> **Nota:** Partecipare a una riunione Avatour richiede di **concedere i permessi del microfono**. Accetta eventuali richieste di autorizzazione dal tuo browser.

1. **Tramite invito del calendario (consigliato):**  
   - Riceverai tipicamente un **invito del calendario** con un **link di accesso diretto** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando il link verrà automaticamente inserito il **codice riunione di 5 caratteri** e verrai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono limitate agli utenti registrati. In questo caso, l'invito indicherà che devi **effettuare l'accesso per accedere alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'organizzatore condivide separatamente un **codice riunione di 5 caratteri**, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'organizzatore.  
   - Se la riunione richiede **l'autenticazione**, dovrai **effettuare l'accesso con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la tua fotocamera o il microfono, poi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se ancora non riesci a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la rete** sta bloccando l'accesso e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando si **trasmette una riunione in diretta da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone di supporto.

##### Visitare uno Spazio di Lavoro Avatour (senza partecipare a una Riunione Avatour)

Puoi accedere a uno Spazio di Lavoro nei seguenti modi:

- **Spazio di Lavoro Pubblico:**  
  Se lo Spazio di Lavoro è pubblico, il link può essere accessibile direttamente — nessun accesso richiesto.

- **Spazio di Lavoro Limitato:**  
  Se lo Spazio di Lavoro è limitato, devi essere aggiunto come **collaboratore** con permessi di **Editor** o **Visualizzatore**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica email** con un link allo Spazio di Lavoro.
  2. Clicca il link nell'email per aprire lo Spazio di Lavoro. Se non hai già effettuato l'accesso, ti verrà richiesto di **effettuare l'accesso o completare la registrazione**.
  3. Una volta effettuato l'accesso, lo Spazio di Lavoro si aprirà automaticamente.

  In alternativa, puoi effettuare l'accesso su [https://avatour.live/login](https://avatour.live/login) e accedere allo Spazio di Lavoro dalla tua **lista degli Spazi di Lavoro**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare uno spazio di lavoro da una gamma di visori Meta e Pico compatibili. Per farlo: 

1. Installa la nostra app Avatour dal rispettivo store VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona uno Spazio di Lavoro per partecipare a una riunione. Per maggiori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Strumenti di collaborazione per riunioni e workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite in loco dal vivo o revisione insieme di asset registrati.  
2. **Workspace (asincroni):** Rivedi e interagisci con gli asset secondo i tuoi tempi, 24 ore su 24, 7 giorni su 7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'interfaccia

L'interfaccia di Avatour è organizzata intorno a tre aree principali:

- **Pannello sinistro** – Asset del workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video in diretta o asset  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu inferiore**.  
Cliccando un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di visualizzazione riunione

Ecco un esempio di visualizzazione in una riunione Avatour:

![Interfaccia riunione Avatour con pannello Asset, Canvas vuoto e pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con pannello Asset (sinistra), Canvas (centro) e pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di visualizzazione workspace

Ecco un esempio di visualizzazione workspace:

![Workspace Avatour con pannello Asset, Canvas vuoto e pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace Avatour con pannello Asset (sinistra), Canvas (centro) e pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del menu inferiore

Il menu inferiore fornisce accesso ai controlli e ai pannelli principali dell'interfaccia:

**Menu inferiore riunione**  

![Menu inferiore riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu inferiore riunione Avatour*

- **Asset** – Rivedi i file del workspace, inclusi video registrati, immagini, snapshot e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti della riunione.  
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Attiva o disattiva l'audio.  
- **Presenta** – Presenta un asset, il desktop o il feed della webcam (vedi la sezione Presenta di seguito).  
- **Strumenti host** (solo host):  
  - **Blocca focus** – Blocca la visualizzazione per tutti i partecipanti.  
  - **Silenzia tutti** – Silenzia tutti i partecipanti.  
- **Attiva schermo intero** – Metti la scheda della riunione a schermo intero.  
- **Esci dalla riunione** – Lascia la riunione.  
- **Avvia registrazione** – Usa questo pulsante per avviare e interrompere manualmente la registrazione durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se l'**avvio automatico della registrazione** è abilitato nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate negli asset del workspace.
- **Mappa** – Apri o chiudi il pannello mappa per gli asset con traccia GPS. Cliccando una posizione si salta al punto esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Partecipanti** – Apri o chiudi il pannello partecipanti.  
- **Info riunione** – Visualizza il codice della riunione, il link di invito e accedi ai tutorial correlati.  

![Info riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello laterale Info riunione Avatour*

- **Impostazioni** – Regola lingua, impostazioni audio e video. Per le riunioni con video 360° in diretta, usa **Mostra bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu inferiore della riunione ti consente di condividere contenuti con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Può essere usata anche durante una riunione con video 360° in diretta per sovrapporre una visualizzazione secondaria per primi piani o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Asset** – Presenta un asset dal workspace. Selezionando un asset si apre la **barra degli strumenti Asset**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per l'asset presentato.

##### Barra degli strumenti Asset (Riunione)

Quando presenti un asset in una riunione, la **barra degli strumenti Asset** appare sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>presenti un Asset in una Riunione</u> - spiegati da sinistra a destra.

![Menu Avatour durante la presentazione di un Asset in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour durante la presentazione di un Asset in una Riunione*


- **Timeline video / Barra di avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dall'asset.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni in diretta.  
- **Mostra/Nascondi punto di vista (POV)** – Visualizza dove ogni partecipante sta guardando nel video 360°.  
- **Note** – Crea note ancorate a momenti specifici nell'asset. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperta → In corso → Risolta) e condivise tramite link diretti.  

  ![Nota Avatour e filtro Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e filtri Note*

  - **Note da comando vocale** – Sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note Avatour - Generate da comando vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da comando vocale*

- **Pannello Note e riepilogo** – Apre un pannello laterale che mostra tutte le note, gli argomenti chiave e un riepilogo esecutivo per l'asset. Cliccando un elemento ti porta a quel momento nel video.  

  ![Riepilogo esecutivo Asset Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo esecutivo Avatour durante la presentazione di un Asset in una Riunione*

  ![Argomenti Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di un Asset in una Riunione*

  Dal **pannello laterale**, puoi **stampare un report dell'asset** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati dall'IA e trascrizioni complete. Puoi anche **scegliere quali elementi includere** prima dell'esportazione.  

  ![Menu stampa report Asset Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menu stampa / download report Asset Avatour*  

  ![Selezione elementi report Asset Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menu selezione elementi report Asset Avatour*

- **Condividi link** – Condividi un link a una nota o scena specifica nell'asset.  
- **Sottotitoli (CC)** – Visualizza la trascrizione testuale sullo schermo durante la riproduzione video.

##### Barra degli strumenti Asset (Workspace)

Quando rivedi un asset in un workspace, la barra degli strumenti è simile ma ottimizzata per l'uso individuale:

![Menu Avatour durante la presentazione di un Asset fuori da una riunione, es. quando si visita un workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour durante la presentazione di un Asset in un Workspace*

- **Timeline video / Barra di avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dalla traccia audio. Clicca ovunque sulla timeline per scorrere il video. Clicca su una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.  
- **Snapshot, Note, Pannello Note e riepilogo, Condividi link, Sottotitoli**  
- Non disponibili: **Spotlight, POV** (richiedono partecipanti in diretta)  
- Controlli aggiuntivi:
  - **Passi di 10 secondi** – Salta avanti/indietro  
  - **Velocità di riproduzione** – Regola la velocità (0,5×–2×)  
  - **Taglia video** – Taglia l'inizio o la fine dell'asset## 4. Per utenti Host e Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}
Quando accedi al tuo Account Utente Avatour, accederai alla **Console Web**.  ### 4.1 Console Web - Panoramica del Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai le seguenti voci di menu:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principale*

- **Spazi di lavoro** – Organizza i tuoi contenuti in modo efficiente. Ogni spazio di lavoro contiene **Risorse**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Risorse** – Accedi e gestisci tutte le tue risorse (video, immagini, PDF). Gli amministratori possono visualizzare tutte le risorse dell'account e le risorse condivise sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analisi** – Monitora l'attività delle sessioni, l'utilizzo degli spazi di lavoro e le metriche ROI.  
- **Impostazioni** *(Solo amministratore)* – Configura le impostazioni predefinite di spazi di lavoro, riunioni e risorse in tutta l'organizzazione. Gli amministratori possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo amministratore)* – Gestisci gli utenti registrati e le telecamere a 360°.  
- **Accesso Dispositivo** – Inserisci il codice visualizzato sulla tua telecamera a 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Accesso Dispositivo, Tutorial ed Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---### 4.2 Console Web - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Aree di Lavoro

Le aree di lavoro sono unità organizzative flessibili che ti permettono di gestire risorse, collaboratori e riunioni in un unico posto. Puoi creare una nuova area di lavoro con il pulsante **Nuova Area di Lavoro** nell'angolo in alto a destra.

![Avatour Console Web - Voce Menu Principale Aree di Lavoro](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Console Web - Voce Menu Principale Aree di Lavoro*

Clicca sull'icona della campana per vedere un riepilogo delle attività dell'area di lavoro negli ultimi 7 giorni.

![Avatour Console Web - Attività Recenti Area di Lavoro](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti Area di Lavoro*

All'interno di un'area di lavoro:

![Area di Lavoro Avatour con Pannello Risorse, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Area di Lavoro con Risorse (sinistra), Canvas (centro), Riunioni (destra)*

- **Risorse** – Gestisci i file allocati a questa area di lavoro.  
- **Collaboratori** – 
  Controlla l'accesso alle aree di lavoro tramite 
  - **Visualizzatore** – Può visualizzare le risorse. L'invito crea un utente Ospite se necessario.  
  - **Editor** – Controllo completo dell'area di lavoro, stessi diritti dell'Host. L'invito promuove l'utente a Host se necessario.  
> Più utenti possono accedere a un'area di lavoro simultaneamente senza una riunione. Le aree di lavoro pubbliche e le impostazioni di accesso alle riunioni forniscono accesso alternativo.  
- **Report** – Genera un report utilizzando un modello di checklist sulle risorse selezionate dell'area di lavoro.  

![Report Area di Lavoro Avatour e Selezione Risorse](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report Area di Lavoro e Selezione Risorse*

- **Mappa** – Visualizza le posizioni delle risorse abilitate GPS su una mappa.  
- **Riunioni** – Organizza riunioni nell'area di lavoro.  
- **Impostazioni** – Configura le impostazioni predefinite dell'area di lavoro e delle riunioni:

![Impostazioni Avatour - Vista Area di Lavoro](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni Area di Lavoro*

**Impostazioni Area di Lavoro**

- **Modello Report** – Seleziona il modello di checklist per i report AI.  
- **Abilita Notifiche** – Email di riepilogo giornaliero per le modifiche di stato delle note.  

![Notifiche Email - Esempio](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio Notifiche Email*

- **Area di Lavoro Pubblica** – Chiunque abbia il link può visualizzare le risorse direttamente.

**Impostazioni Riunione**
  
* **Autenticazione richiesta** – I partecipanti devono accedere.  
* **Consenti accesso ospiti** – Permetti agli utenti non registrati di visualizzare le risorse.  
* **Avvio Automatico Registrazione / Avvio Manuale** – Scegli se le riunioni vengono registrate automaticamente o avviate manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host esce.  
* **Consenti accesso spettatore** – Partecipa senza microfono o videocamera; comunica tramite chat.  
* **Riunioni protette da password** – Richiedi una password per partecipare.  
* **Mostra Domanda Risparmio Viaggi** – Chiedi ai partecipanti se la riunione ha ridotto i viaggi.  

> Le impostazioni possono essere combinate (es., nessun host richiesto ma protetto da password).

---

#### 4.2.2 Risorse

Gestisci tutti i video 360°/2D, immagini e PDF. Carica/scarica risorse, alloca alle aree di lavoro, condividi con altri utenti, rinomina, stampa/scarica report, attiva la sfocatura volti e la sintesi AI.

![Avatour Console Web - Voce Menu Principale Risorse](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Risorse*

---

#### 4.2.3 Analisi

Fornisce approfondimenti su riunioni, utilizzo delle aree di lavoro e metriche ROI.

![Avatour Console Web - Voce Menu Principale Analisi (1 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analisi*

![Avatour Console Web - Voce Menu Principale Analisi (2 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Riunioni e Utilizzo Aree di Lavoro*

![Avatour Console Web - Voce Menu Principale Analisi (3 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenze Dispositivi e ROI*## 5. Onsite - How to Use the Avatour Turnkey Kit {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Getting Started
[Quick Start Guide – Avatour Turnkey Kit 3.1 (Pilot PanoX V2 setup)](https://avatour.com/quickstart-panox-v2)

Follow the guide to unpack, assemble, and power on your camera.

---

### 5.2 Useful Tips

#### External Battery – Longer Live Meetings & Improved Thermals 

- **If your kit includes a Ulanzi battery:** Attach it between the tripod base and the extendable stick, then connect the battery to the camera via USB-C.  

- **If your kit includes a Telesin battery stick:** Mount the camera directly onto the Telesin extendable battery stick and connect it via USB-C.  

Using the external battery:

1. Extends total battery life from ~40 minutes (camera battery only) to ~3 hours.  
2. Adds stability to the camera setup.  
3. Helps prevent potential overheating.  

> We recommend always using the external battery from the start, especially for live meetings.

#### Audio Considerations for Live Meetings and Recordings

- **Noisy environments:** 
  Use the Shokz headphones included in your kit for clear audio capture.  
  - **Power On/Off:** Hold the “+” button for 3 seconds (blue LED = on, red LED = off).  
  - **Bluetooth Pairing Mode:** While the headset is off, hold the “+” button for 5 seconds (LED flashes blue/red).  
  - **Volume:** Use the “+” and “-” buttons.  

- **Quieter environments / multiple participants near camera:** 
  Use the NoxGear clip-on speaker. It’s not as high fidelity as conference speakers (e.g., Jabra Speak), but is easy to clip onto your shirt and captures nearby voices effectively.  
  - **Power On/Off:** Hold the Play/Pause button for 2 seconds.  
  - **Bluetooth Pairing Mode:** Automatically enters pairing mode when powered on (LED flashes blue/red; solid blue when paired).  
  - **Volume:** Use the “+” and “-” buttons.  

- **Using your own device:** If you prefer an alternative (e.g., a conference speaker or personal headset), you can pair it via the camera: Settings → Bluetooth.  

#### Connectivity, Connectivity, Connectivity
**Before you start:** Ensure internet connection via:

- **Local WiFi** (preferred)
- **Mobile Network** (if outside WiFi range)

**Recommended bandwidth:** 10 Mbps uplink/downlink for full 360° streaming (~5 Mbps). Lower bandwidth (1–2 Mbps) only works when standing still.

##### Test Network Speed
- **Single-location test:** Any speed checker you normally use (e.g., [Speedtest](https://www.speedtest.net)) to verify both upload  bandwidth.   
- **Walking test across site:** From the camera: Settings → Network → Connection Test. Walk through the entire space to confirm coverage and bandwidth.

##### Local WiFi
- Highly recommended for stable connections.  
- If IT requires whitelisting, find MAC address: Settings → About → WiFi Address.

##### Mobile Network
**Option A: Kit-provided hotspot & SIM**  

- Attach GlocalMe hotspot to Telesin battery stick (magnet).  
- Ensures no interference and maintains connection if moving away from camera.  
- Troubleshooting:
  - Confirm pre-installed SIM (not Cloud SIM).  
  - Enable 5G in SIM Card Manager.  
  - Verify correct APN for your region ([APN setup guide](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B: Personal hotspot / SIM**
- Use your own smartphone or dedicated hotspot.  

**Important Note:**  
> Keep hotspot off while connected to WiFi; enable only when out of range. The camera's OS dynamically switches between WiFi networks based on signal strength and may inadvertently switch to the hotspot even when WiFi is available.

> Mobile networks may throttle bandwidth unexpectedly. Check with your carrier on data plan limits, or contact Avatour support if using our hotspot and SIM.

##### Low Bandwidth Situations
- Pre-record location videos for later playback ([recording guide](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Share a smartphone camera stream to supplement low-bandwidth areas (0.1–0.3 Mbps upload).

##### No Connectivity
- Only pre-recorded video can be used ([recording guide](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Other Onsite Participants – Best Practices

When multiple participants join a live Avatour meeting from the same location as the 360° camera, careful management of **audio and bandwidth** is crucial:  

- Each smartphone, tablet, or laptop connected onsite consumes network bandwidth and can negatively impact the 360° camera feed.  
- Multiple microphones and speakers in the same space can cause **audio feedback**, making the meeting experience unpleasant for all participants.

#### Other Onsite Participants – Best Practices

When multiple participants join a live Avatour meeting from the same location as the 360° camera, careful management of **audio and bandwidth** is crucial:  

- Each smartphone, tablet, or laptop connected onsite consumes network bandwidth and can negatively impact the 360° camera feed.  
- Multiple microphones and speakers in the same space can cause **audio feedback**, making the meeting experience unpleasant for all participants.

To address these challenges, follow these **best practices**:

- **Use wired or wireless headphones:** Preferably with noise-canceling to prevent echo and feedback.  
- **On-Site Mode:** Join the meeting in On-Site mode when physically present near the 360° camera.  
  - This mode is optimized for onsite use:  
    - Mutes the participant’s mic and speaker by default.  
    - Does **not** send the participant’s camera feed.  
    - Does **not** display the 360° camera feed in the participant’s browser.  
    - Conserves network bandwidth, ensuring the 360° camera has maximum available upload for the live stream.  
    - Useful when a user wants to share specific details; you **can share back your camera** for targeted views.  
- **Mute when not actively speaking:** Prevents unwanted audio feedback and distractions.  
- **Use a separate network if possible:** Have your smartphone connected to a different network than the camera’s network to reduce interference.  

Following these guidelines ensures a smooth, high-quality live tour for both onsite and remote participants.

### 5.3 Avatour Camera App

Here are (1) the Top Level, (2) Settings and (3) Network Settings menus.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360° Camera App - 3 Menus*

**Quick Capture** - For offline 360° video recording. - For a detailed description see [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). We recommend using an external audio device (connected via bluetooth). N.B. You can also do standard 2D videos and pictures - simply change the mode between 360° and 2D in the bottom right corner once in the QC screen.

**Live Meeting** - For live 360° Video Conferencing. You will see your workspaces and clicking on one will initiate the live video stream from the 360° camera. Before you can join the meeting with your 360° cam you need to connect an audio device via bluetooth. For a detailed description see [How to start a Live Capture meeting with your Pilot camera?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> When hosting a Live Capture meeting with your 360 camera, you will have similar meeting tools available to you that mirror the web experience. Here is a link to our Knowledge Base article that explains these tools in more detail: [Operator App Tools](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Gallery** - Find here all your 360° videos and pictures for upload to the Avatour Web Console.

**Settings** - Within Settings, you have the following options:

- **Network**: This option allows you to change which WiFi network the camera is connected to or run a network connection test to view your streaming throughput
- **Live Capture**: Adjust your Live Capture settings depending on available bandwidth, guest’s VR sensitivity, or if your camera’s protective lenses are installed:
  - **Target Frame** **Rate**: Adjust the frame rate for your Live Capture video between 15 fps, 24 fps, and 30 fps. Higher frame rates produce a smoother video, but will require more upload bandwidth. Default: 15 fps
  - **Target Bitrate**: Enables you to increase or decrease the maximum streaming bitrate for your Live Capture. You can set your target bitrate between 1 Mbps and 10 Mbps. Higher bitrates will result in higher video resolution, but will require more upload bandwidth. Default: 5 Mbps
  - **Optimize Motion**: This will decrease the video frame rate, generating less load on your network's upload bandwidth, and increase your streaming bitrate. In addition, this option helps to reduce motion sickness for VR participants. Default: Off
  - **Protective Lenses**: This will affect how the 360° video is stitched depending if protective lenses have been installed on your camera. If you do not have protective lenses, set this to “No”. If you received a Kit 3.0, you have pre-installed protective lenses on and should set this to “Yes”. Default: Yes

- **Quick Capture**: Adjust your Quick Capture settings depending on your preferred video frame rate, available bandwidth for recorded video uploads, or if your camera’s protective lenses are installed. Quick Capture has a set resolution of 4k which usually strikes a good balance between video quality and file size. (For higher resolutions you can use the native camera apps, also on the PanoX V2, for details see [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Target Frame Rate**: Adjust the frame rate for your Quick Capture video recordings between 15 fps, 24 fps, and 30 fps. Higher frame rates produce a smoother video, but will increase video file size and upload time. Recommended: 30 fps
  - **Target Bitrate**: Set the target bitrate for Quick Capture uploads between 5 Mbps and 20 Mbps. Lower bitrates increase upload speeds, but will decrease video quality. Recommended: 20 Mbps
  - **Protective Lenses**: *See Protective Lenses section for Live Capture above*
- **About**: View device serial number and software version

**Account** - For login with your Avatour host or admin account.

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
