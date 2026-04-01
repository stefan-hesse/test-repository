# Avatour User and Best Practices Guide

## 1. Per Tutti gli Utenti di Avatour {#for-all-avatour-users}
Se sei nuovo su Avatour, le seguenti risorse forniscono un'utile introduzione alla piattaforma e alle sue funzionalità:

1. [Video Come funziona Avatour](https://avatour.com/how-it-works)  
Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma consente la collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs)  
Risposte alle domande frequenti.
3. [Glossario](https://avatour.com/glossary)  
Definizioni dei termini e concetti chiave di Avatour utilizzati frequentemente.
4. Sito web  
Dai un'occhiata in particolare alla pagina [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate ai Casi d'uso e ai Settori per scoprire come Avatour può supportare le tue esigenze specifiche.## 2. Tipi di utenti Avatour  {#avatour-user-types}
### 2.1 Partecipanti alla Riunione (Account non richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi per un account Avatour.
Eccezione: Se l'organizzatore ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare il login per autenticarsi.

Gli utenti accedono alla riunione come segue:

- Ricevono un invito del calendario dall'organizzatore.
- Usano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'organizzatore ne ha abilitata una.
- I partecipanti possono partecipare senza un account Avatour a meno che la riunione non sia limitata e richieda il login per autenticarsi.

#### 2.1.1 Partecipante 

- Può partecipare e interagire completamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, usare un microfono, presentare, riprodurre/mettere in pausa Asset o acquisire Istantanee.
- Massimo 10 Spettatori per riunione.
- Insieme ai Partecipanti, una riunione può ospitare fino a 30 partecipanti.

### 2.2 Utenti Registrati

Gli Utenti Registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitati dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Ospite, Organizzatore o Admin). Gli utenti invitati ricevono un **link di registrazione** per completare la configurazione dell'account e impostare una password.  
- **Invitati dall'Organizzatore:** Gli Organizzatori possono aggiungere utenti come **collaboratori Editor** a uno Spazio di Lavoro. Questo consuma una **licenza Organizzatore** e garantisce che l'utente abbia accesso di livello Organizzatore.  
- **Provisioning automatico SSO (solo livello Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account provisionati tramite SSO vengono aggiunti al **gruppo Ospite**, a meno che non venga sovrascritto tramite **mappature dei gruppi SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza ai gruppi direttamente anche quando l'SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in diversi modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Ospite, Organizzatore o Admin).  
- **Provisioning SSO:** Per i clienti di livello Enterprise o Business con SSO abilitato, l'IdP può provisionare automaticamente gli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo dell'utente sulla piattaforma.  
- **Utenti invitati dall'Organizzatore:** Gli Organizzatori possono invitare altri utenti come collaboratori Editor in Spazi di Lavoro specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Organizzatore.

**Best Practice Raccomandata (Clienti Enterprise):**  
Per le organizzazioni che prevedono un grande numero di utenti che necessitano di accesso ad Avatour, si raccomanda di **integrare il Single Sign-On (SSO)** e gestire utenti e appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione dei gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo degli accessi coerente.

#### 2.2.1 Utenti Ospite

- Aggiunti al **gruppo Ospite**.  
- Possono **visualizzare gli Asset** all'interno degli Spazi di Lavoro dove sono stati aggiunti come **collaboratori Visualizzatore**.  
- Non possono creare spazi di lavoro, organizzare riunioni o caricare contenuti.  
- Gli account Ospite provisionati tramite SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

#### 2.2.2 Utenti con Licenza (Accesso alla Console Web)

##### Utenti Organizzatore (Gruppo: Organizzatore)

- Possono creare/gestire Spazi di Lavoro, invitare collaboratori a uno spazio di lavoro, **organizzare riunioni dal vivo**, caricare **Acquisizioni Rapide**.  
- Ha accesso alla **Dashboard Organizzatore** e all'**App Operatore** su telecamere 360° supportate.  

##### Utenti Admin (Gruppo: Admin)

- Include tutte le capacità dell'Organizzatore più l'amministrazione completa dell'account.

**I privilegi aggiuntivi dell'Admin includono:**

**Gestione Account**  

- Creare nuovi utenti e assegnarli a gruppi.
- Reimpostare le password quando gestite da Avatour (non applicabile quando l'SSO è abilitato). 
- Aggiornare gli utenti Ospite a Organizzatore.  
- Disattivare utenti (gli account Admin devono prima essere convertiti in Organizzatore prima dell'eliminazione).  
- Trasferire asset da un utente Organizzatore a un altro durante l'eliminazione.

**Impostazioni**  

- Configurare **impostazioni di sicurezza a livello organizzativo** per asset, spazi di lavoro e riunioni ospitate sulla piattaforma (ad es., se un Organizzatore deve essere presente per avviare una riunione, se i volti devono essere sfocati su tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare le **funzionalità AI** o la **registrazione**.  
- Applicare il branding aziendale in modo coerente su tutta la piattaforma se è configurato un **dominio personalizzato**.
  

**Asset e Analisi** 
 
- Visualizzare tutti gli Asset caricati da qualsiasi utente nell'organizzazione.  
- Esaminare l'utilizzo della piattaforma in tutta l'organizzazione.

---

#### 2.2.3 Permessi dei Collaboratori dello Spazio di Lavoro

I permessi dello Spazio di Lavoro definiscono cosa un utente può fare **all'interno di uno specifico Spazio di Lavoro**. Questi sono separati dall'appartenenza ai gruppi a livello di piattaforma (Ospite, Organizzatore, Admin).

- **Collaboratore Editor:** Gli utenti con questo permesso possono:
  - Gestire Asset (caricare, rimuovere, sfocare volti, generare riepiloghi)  
  - Gestire le impostazioni della riunione (abilitare/disabilitare la registrazione, consentire o rimuovere partecipanti)  
  - Programmare e organizzare riunioni dal vivo  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dallo Spazio di Lavoro  

- **Collaboratore Visualizzatore:** Gli utenti con questo permesso hanno accesso in sola lettura agli Asset dello Spazio di Lavoro. **Non possono modificare Asset, gestire riunioni o gestire collaboratori**, ma **possono creare Note sugli Asset**. ## 3. Per i partecipanti alle riunioni da remoto e i visitatori dello spazio di lavoro {#for-remote-meeting-participants-and-workspace-visitors}
Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione Avatour (Collaborazione Sincrona):**  
  Potresti ricevere un **invito sul calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota dal vivo al sito** o rivedere insieme le risorse in modo sincrono.

- **Visitare un Workspace (Collaborazione Asincrona):**  
  Potresti anche essere invitato come **collaboratore in un Workspace** per rivedere le risorse **in modo asincrono** (secondo i tuoi tempi).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare un Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo "Schermo Piatto" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

##### Partecipare a una Riunione Avatour

> **Nota:** Per partecipare a una riunione Avatour è necessario **concedere i permessi per il microfono**. Si prega di accettare le richieste di autorizzazione dal browser.

1. **Tramite invito sul calendario (consigliato):**  
   - Riceverai tipicamente un **invito sul calendario** con un **link diretto per partecipare** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando il link verrà automaticamente inserito il **codice riunione di 5 caratteri** e verrai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono riservate agli utenti registrati. In questo caso, l'invito indicherà che devi **effettuare l'accesso per accedere alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che dovrai inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'organizzatore condivide separatamente un **codice riunione di 5 caratteri**, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'organizzatore.  
   - Se la riunione richiede **l'autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua videocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio, Microsoft Teams o Zoom). Chiudi tutte le app che potrebbero utilizzare la videocamera o il microfono, quindi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se non riesci ancora a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la rete** sta bloccando l'accesso e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando si **trasmette una riunione dal vivo da una videocamera Insta360**, poiché queste videocamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone come supporto.

##### Visitare un Workspace Avatour (senza partecipare a una Riunione Avatour)

Puoi accedere a un Workspace nei seguenti modi:

- **Workspace Pubblico:**  
  Se il Workspace è pubblico, il link può essere accessibile direttamente—non è richiesto l'accesso.

- **Workspace con Restrizioni:**  
  Se il Workspace ha restrizioni, devi essere aggiunto come **collaboratore** con permessi di **Editor** o **Visualizzatore**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica email** con un link al Workspace.
  2. Clicca il link nell'email per aprire il Workspace. Se non hai già effettuato l'accesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, il Workspace si aprirà automaticamente.

  In alternativa, puoi accedere su [https://avatour.live/login](https://avatour.live/login) e accedere al Workspace dalla tua **lista dei Workspace**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare un workspace da una gamma di visori Meta e Pico compatibili. Per fare questo: 

1. Installa la nostra app Avatour dal rispettivo store app VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona un Workspace per partecipare a una riunione. Per maggiori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite dal vivo al sito o revisione insieme delle risorse registrate.  
2. **Workspace (asincroni):** Rivedi e interagisci con le risorse secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata attorno a tre aree principali:

- **Pannello sinistro** – Risorse del workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video dal vivo o risorse  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni viene avviata dal **menu inferiore**.  
Cliccando un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Vista Riunione

Ecco un esempio di vista in una Riunione Avatour:

![Interfaccia Riunione Avatour con Pannello Risorse, Canvas vuoto e Pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con Pannello Risorse (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Vista Workspace

Ecco un esempio di vista Workspace:

![Workspace Avatour con Pannello Risorse, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace Avatour con Pannello Risorse (sinistra), Canvas (centro) e Pannello Riunioni (destra)*

---

#### 3.2.4 Panoramica del Menu Inferiore

Il menu inferiore fornisce accesso ai controlli principali dell'interfaccia e ai pannelli:

**Menu Inferiore Riunione**  

![Menu Inferiore Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu Inferiore Riunione Avatour*

- **Risorse** – Rivedi i file del workspace, inclusi video registrati, immagini, snapshot e PDF. 
- **Chat** – Invia messaggi a tutti i partecipanti alla riunione.  
- **Videocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Attiva o disattiva il tuo audio.  
- **Presenta** – Presenta una risorsa, il desktop o il feed della webcam (vedi la sezione Presenta sotto).  
- **Strumenti Organizzatore** (solo organizzatori):  
  - **Blocca Focus** – Blocca la vista per tutti i partecipanti.  
  - **Silenzia Tutti** – Silenzia tutti i partecipanti.  
- **Attiva Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Lascia la riunione.  
- **Avvia Registrazione** – Usa questo pulsante per avviare e fermare manualmente la registrazione durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se l'**avvio automatico della registrazione** è abilitato nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate nelle risorse del workspace.
- **Mappa** – Apri o chiudi il pannello mappa per le risorse con traccia GPS. Cliccando una posizione si salta al punto esatto nel video. La mappa si aggiorna in tempo reale durante la riproduzione del video.
- **Partecipanti** – Apri o chiudi il pannello partecipanti.  
- **Info Riunione** – Visualizza il codice riunione, il link di invito e accedi ai tutorial correlati.  

![Info Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Info Riunione Avatour*

- **Impostazioni** – Regola le impostazioni di lingua, audio e video. Per le riunioni con video 360° dal vivo, usa **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu inferiore della riunione ti consente di condividere contenuti con tutti i partecipanti.

- **Videocamera** – Condividi la videocamera del tuo smartphone/tablet. Questo può essere utilizzato anche durante una riunione con video 360° dal vivo per sovrapporre una vista secondaria per primi piani o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Risorsa** – Presenta una risorsa dal workspace. Selezionando una risorsa si apre la **Barra degli strumenti Risorsa**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per la risorsa presentata.

##### Barra degli Strumenti Risorsa (Riunione)

Quando presenti una risorsa in una riunione, la **Barra degli Strumenti Risorsa** appare sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>presenti una Risorsa in una Riunione</u> - spiegati da sinistra a destra.

![Menu Avatour durante la Presentazione di una Risorsa in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour durante la presentazione di una Risorsa in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dalla risorsa.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni dal vivo.  
- **Mostra/Nascondi Punto di Vista (POV)** – Visualizza dove ogni partecipante sta guardando nel video 360°.  
- **Note** – Crea note ancorate a momenti specifici nella risorsa. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperto → In Corso → Risolto) e condivise tramite link diretti.  

  ![Nota Avatour e Filtri Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

  - **Note da Comando Vocale** – Questi sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note Avatour - Generate da Comando Vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da Comando Vocale*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che visualizza tutte le note, gli argomenti chiave e un riepilogo esecutivo per la risorsa. Cliccando un elemento si salta a quel momento nel video.  

  ![Riepilogo Esecutivo Risorsa Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour durante la presentazione di una Risorsa in una Riunione*

  ![Argomenti Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di una Risorsa in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report della risorsa** o **scaricarlo come TXT o CSV**. I report possono includere note, argomenti generati dall'IA e trascrizioni complete. Pu## 4. Per utenti Host e Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}
Quando accedi al tuo Account Utente Avatour, accederai alla **Console Web**.  

### 4.1 Console Web - Panoramica del Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai le seguenti voci di menu:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principale*

- **Spazi di lavoro** – Organizza i tuoi contenuti in modo efficiente. Ogni spazio di lavoro contiene **Risorse**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Risorse** – Accedi e gestisci tutte le tue risorse (video, immagini, PDF). Gli amministratori possono visualizzare tutte le risorse dell'account e le risorse condivise sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analisi** – Monitora l'attività delle sessioni, l'utilizzo degli spazi di lavoro e le metriche ROI.  
- **Impostazioni** *(Solo amministratore)* – Configura le impostazioni predefinite di spazi di lavoro, riunioni e risorse in tutta l'organizzazione. Gli amministratori possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo amministratore)* – Gestisci gli utenti registrati e le telecamere 360°.  
- **Accesso Dispositivo** – Inserisci il codice visualizzato sulla tua telecamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Accesso Dispositivo, Tutorial ed Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---

### 4.2 Console Web - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Spazi di lavoro

Gli spazi di lavoro sono unità organizzative flessibili che ti permettono di gestire risorse, collaboratori e riunioni in un unico posto. Puoi creare un nuovo spazio di lavoro con il pulsante **Nuovo Spazio di Lavoro** nell'angolo in alto a destra.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Voce Menu Principale Spazi di lavoro*

Clicca sull'icona della campana per vedere un riepilogo dell'attività dello spazio di lavoro negli ultimi 7 giorni.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti dello Spazio di Lavoro*

All'interno di uno spazio di lavoro:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Spazio di lavoro con Risorse (sinistra), Canvas (centro), Riunioni (destra)*

- **Risorse** – Gestisci i file allocati a questo spazio di lavoro.  
- **Collaboratori** – 
  Controlla l'accesso agli spazi di lavoro tramite 
  - **Visualizzatore** – Può visualizzare le risorse. L'invito crea un utente Ospite se necessario.  
  - **Editor** – Controllo completo dello spazio di lavoro, stessi diritti dell'Host. L'invito promuove l'utente a Host se necessario.  
> Più utenti possono accedere a uno spazio di lavoro contemporaneamente senza una riunione. Gli spazi di lavoro pubblici e le impostazioni di accesso alle riunioni forniscono accessi alternativi.  
- **Report** – Genera un report utilizzando un modello di checklist sulle risorse selezionate dello spazio di lavoro.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report dello Spazio di Lavoro e Selezione Risorse*

- **Mappa** – Visualizza le posizioni delle risorse abilitate GPS su una mappa.  
- **Riunioni** – Organizza riunioni nello spazio di lavoro.  
- **Impostazioni** – Configura le impostazioni predefinite dello spazio di lavoro e delle riunioni:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni dello Spazio di Lavoro*

**Impostazioni dello Spazio di Lavoro**

- **Modello di Report** – Seleziona il modello di checklist per la reportistica AI.  
- **Abilita Notifiche** – Email di riepilogo giornaliero per le modifiche di stato delle note.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio di Notifiche Email*

- **Spazio di Lavoro Pubblico** – Chiunque abbia il link può visualizzare le risorse direttamente.

**Impostazioni Riunione**
  
* **Autenticazione richiesta** – I partecipanti devono effettuare l'accesso.  
* **Consenti accesso ospiti** – Permetti agli utenti non registrati di visualizzare le risorse.  
* **Avvio Automatico Registrazione / Avvio Manuale** – Scegli se le riunioni vengono registrate automaticamente o avviate manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host esce.  
* **Consenti accesso spettatore** – Partecipa senza microfono o telecamera; comunica via chat.  
* **Riunioni protette da password** – Richiedi una password per partecipare.  
* **Mostra Domanda sul Risparmio di Viaggio** – Chiedi ai partecipanti se la riunione ha ridotto i viaggi.  

> Le impostazioni possono essere combinate (es. nessun host richiesto ma protetto da password).

---

#### 4.2.2 Risorse

Gestisci tutti i video 360°/2D, immagini e PDF. Carica/scarica risorse, allocale agli spazi di lavoro, condividile con altri utenti, rinominale, stampa/scarica report, attiva la sfocatura dei volti e la sintesi AI.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Risorse*

---

#### 4.2.3 Analisi

Fornisce approfondimenti su riunioni, utilizzo degli spazi di lavoro e metriche ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analisi*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Riunioni e Utilizzo Spazi di Lavoro*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenze Dispositivo e ROI*## 5. Onsite - Come Utilizzare il Kit Chiavi in Mano Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}
### 5.1 Per Iniziare
[Guida Rapida – Kit Chiavi in Mano Avatour 3.1 (Configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per disimballare, assemblare e accendere la tua fotocamera.

---

### 5.2 Suggerimenti Utili

#### Batteria Esterna – Riunioni Live più Lunghe e Migliore Gestione Termica

- **Se il tuo kit include una batteria Ulanzi:** Fissala tra la base del treppiede e l'asta estensibile, poi collega la batteria alla fotocamera tramite USB-C.

- **Se il tuo kit include un'asta batteria Telesin:** Monta la fotocamera direttamente sull'asta batteria estensibile Telesin e collegala tramite USB-C.

Utilizzando la batteria esterna:

1. Estendi la durata totale della batteria da ~40 minuti (solo batteria della fotocamera) a ~3 ore.
2. Aggiungi stabilità alla configurazione della fotocamera.
3. Aiuta a prevenire potenziali surriscaldamenti.

> Raccomandiamo di utilizzare sempre la batteria esterna fin dall'inizio, specialmente per le riunioni live.

#### Considerazioni Audio per Riunioni Live e Registrazioni

- **Ambienti rumorosi:**
  Usa le cuffie Shokz incluse nel tuo kit per una cattura audio chiara.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).
  - **Modalità Accoppiamento Bluetooth:** Con le cuffie spente, tieni premuto il pulsante "+" per 5 secondi (il LED lampeggia blu/rosso).
  - **Volume:** Usa i pulsanti "+" e "-".

- **Ambienti più silenziosi / più partecipanti vicino alla fotocamera:**
  Usa l'altoparlante a clip NoxGear. Non è ad alta fedeltà come gli altoparlanti da conferenza (es. Jabra Speak), ma è facile da agganciare alla camicia e cattura efficacemente le voci vicine.
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Play/Pausa per 2 secondi.
  - **Modalità Accoppiamento Bluetooth:** Entra automaticamente in modalità accoppiamento all'accensione (il LED lampeggia blu/rosso; blu fisso quando accoppiato).
  - **Volume:** Usa i pulsanti "+" e "-".

- **Utilizzare il proprio dispositivo:** Se preferisci un'alternativa (es. un altoparlante da conferenza o cuffie personali), puoi accoppiarlo tramite la fotocamera: Impostazioni → Bluetooth.

#### Connettività, Connettività, Connettività
**Prima di iniziare:** Assicura la connessione internet tramite:

- **WiFi Locale** (preferito)
- **Rete Mobile** (se fuori dalla copertura WiFi)

**Larghezza di banda raccomandata:** 10 Mbps uplink/downlink per lo streaming completo a 360° (~5 Mbps). Una larghezza di banda inferiore (1–2 Mbps) funziona solo stando fermi.

##### Test della Velocità di Rete
- **Test in singola posizione:** Qualsiasi strumento di test della velocità che usi normalmente (es. [Speedtest](https://www.speedtest.net)) per verificare la larghezza di banda in upload.
- **Test camminando attraverso il sito:** Dalla fotocamera: Impostazioni → Rete → Test di Connessione. Cammina attraverso l'intero spazio per confermare copertura e larghezza di banda.

##### WiFi Locale
- Altamente raccomandato per connessioni stabili.
- Se l'IT richiede il whitelisting, trova l'indirizzo MAC: Impostazioni → Informazioni → Indirizzo WiFi.

##### Rete Mobile
**Opzione A: Hotspot e SIM forniti nel kit**

- Attacca l'hotspot GlocalMe all'asta batteria Telesin (magnete).
- Garantisce nessuna interferenza e mantiene la connessione se ti allontani dalla fotocamera.
- Risoluzione problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).
  - Abilita il 5G nel Gestore Scheda SIM.
  - Verifica l'APN corretto per la tua regione ([guida configurazione APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Usa il tuo smartphone o hotspot dedicato.

**Nota Importante:**
> Mantieni l'hotspot spento mentre sei connesso al WiFi; abilitalo solo quando sei fuori copertura. Il sistema operativo della fotocamera passa dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe passare inavvertitamente all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili potrebbero limitare la larghezza di banda inaspettatamente. Verifica con il tuo operatore i limiti del piano dati, o contatta il supporto Avatour se usi il nostro hotspot e SIM.

##### Situazioni di Bassa Larghezza di Banda
- Pre-registra i video delle location per la riproduzione successiva ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Condividi uno stream dalla fotocamera dello smartphone per integrare le aree a bassa larghezza di banda (0,1–0,3 Mbps upload).

##### Nessuna Connettività
- Possono essere utilizzati solo video pre-registrati ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri Partecipanti in Loco – Migliori Pratiche

Quando più partecipanti si uniscono a una riunione live Avatour dalla stessa posizione della fotocamera 360°, una gestione attenta di **audio e larghezza di banda** è cruciale:

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

#### Altri Partecipanti in Loco – Migliori Pratiche

Quando più partecipanti si uniscono a una riunione live Avatour dalla stessa posizione della fotocamera 360°, una gestione attenta di **audio e larghezza di banda** è cruciale:

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera 360°.
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **migliori pratiche**:

- **Usa cuffie con filo o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.
- **Modalità In Loco:** Unisciti alla riunione in modalità In Loco quando sei fisicamente presente vicino alla fotocamera 360°.
  - Questa modalità è ottimizzata per l'uso in loco:
    - Silenzia il microfono e l'altoparlante del partecipante di default.
    - **Non** invia il feed della fotocamera del partecipante.
    - **Non** visualizza il feed della fotocamera 360° nel browser del partecipante.
    - Conserva la larghezza di banda di rete, assicurando che la fotocamera 360° abbia il massimo upload disponibile per lo stream live.
    - Utile quando un utente vuole condividere dettagli specifici; **puoi condividere la tua fotocamera** per visualizzazioni mirate.
- **Silenzia quando non stai parlando attivamente:** Previene feedback audio indesiderati e distrazioni.
- **Usa una rete separata se possibile:** Connetti il tuo smartphone a una rete diversa da quella della fotocamera per ridurre le interferenze.

Seguire queste linee guida garantisce un tour live fluido e di alta qualità sia per i partecipanti in loco che per quelli remoti.

### 5.3 App Fotocamera Avatour

Ecco (1) il Livello Principale, (2) Impostazioni e (3) i menu Impostazioni di Rete.

![App Fotocamera 360° Avatour - Tre Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App Fotocamera 360° Avatour - 3 Menu*

**Cattura Rapida** - Per la registrazione video 360° offline. - Per una descrizione dettagliata vedi [Come registrare e caricare video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Raccomandiamo l'uso di un dispositivo audio esterno (connesso via bluetooth). N.B. Puoi anche fare video e foto 2D standard - cambia semplicemente la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata CR.

**Riunione Live** - Per videoconferenze live a 360°. Vedrai i tuoi spazi di lavoro e cliccando su uno si avvierà lo stream video live dalla fotocamera 360°. Prima di poterti unire alla riunione con la tua fotocamera 360° devi connettere un dispositivo audio via bluetooth. Per una descrizione dettagliata vedi [Come avviare una riunione Live Capture con la tua fotocamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando ospiti una riunione Live Capture con la tua fotocamera 360, avrai strumenti di riunione simili disponibili che rispecchiano l'esperienza web. Ecco un link al nostro articolo della Knowledge Base che spiega questi strumenti in maggior dettaglio: [Strumenti App Operatore](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galleria** - Trova qui tutti i tuoi video e foto 360° per il caricamento sulla Console Web Avatour.

**Impostazioni** - All'interno delle Impostazioni, hai le seguenti opzioni:

- **Rete**: Questa opzione ti permette di cambiare a quale rete WiFi è connessa la fotocamera o eseguire un test di connessione di rete per visualizzare il throughput di streaming
- **Live Capture**: Regola le impostazioni Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti, o se le lenti protettive della fotocamera sono installate:
  - **Frame Rate Target**: Regola il frame rate per il tuo video Live Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma richiederanno più larghezza di banda in upload. Default: 15 fps
  - **Bitrate Target**: Ti permette di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il bitrate target tra 1 Mbps e 10 Mbps. Bitrate più alti risulteranno in una risoluzione video maggiore, ma richiederanno più larghezza di banda in upload. Default: 5 Mbps
  - **Ottimizza Movimento**: Questo diminuirà il frame rate del video, generando meno carico sulla larghezza di banda in upload della tua rete, e aumenterà il bitrate di streaming. Inoltre, questa opzione aiuta a ridurre la cinetosi per i partecipanti VR. Default: Off
  - **Lenti Protettive**: Questo influenzerà come il video 360° viene unito a seconda se le lenti protettive sono state installate sulla tua fotocamera. Se non hai lenti protettive, imposta su "No". Se hai ricevuto un Kit 3.0, hai lenti protettive preinstallate e dovresti impostare su "Sì". Default: Sì

- **Cattura Rapida**: Regola le impostazioni Cattura Rapida in base al frame rate video preferito, alla larghezza di banda disponibile per i caricamenti video registrati, o se le lenti protettive della fotocamera sono installate. Cattura Rapida ha una risoluzione impostata di 4k che solitamente raggiunge un buon equilibrio tra qualità video e dimensione file. (Per risoluzioni più alte puoi usare le app native della fotocamera, anche sulla PanoX V2, per dettagli vedi [Come registrare e caricare video 360 con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Frame Rate Target**: Regola il frame rate per le tue registrazioni video Cattura Rapida tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma aumenteranno la dimensione del file video e il tempo di caricamento. Raccomandato: 30 fps
  - **Bitrate Target**: Imposta il bitrate target per i caricamenti Cattura Rapida tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano le velocità di caricamento, ma diminuiranno la qualità video. Raccomandato: 20 Mbps
  - **Lenti Protettive**: *Vedi la sezione Lenti Protettive per Live Capture sopra*
- **Informazioni**: Visualizza numero di serie del dispositivo e versione software

**Account** - Per l'accesso con il tuo account host o admin Avatour.## 6. Consigli sulle migliori pratiche {#best-practice-advice}
### 6.1 Primi utilizzi (informali) e familiarizzazione

Per i primi utilizzi e per familiarizzare con la Console Web Avatour e il Kit Chiavi in Mano Avatour raccomandiamo i seguenti passaggi:

1. Porta il kit a casa e provalo con familiari e amici utilizzando la tua connessione internet domestica.
2. Porta il kit in ufficio e collegalo a una rete aziendale (potrebbero emergere problematiche aziendali, ad es. firewall aziendali - ma dal primo passaggio sai che Avatour funziona e questo è un argomento da risolvere con il tuo team IT con l'aiuto di Avatour).
3. Inizia a utilizzare Avatour in loco (fuori dal tuo ufficio) presso il luogo dell'incontro verso cui i partecipanti remoti dovrebbero normalmente viaggiare. Potrebbero emergere ulteriori problematiche di connettività. Avatour può aiutare in collaborazione con il tuo team IT.
4. Inizia a utilizzarlo con partecipanti remoti interni ed esterni.

### 6.2 Prima di una riunione live in video 360°

- Raccomandiamo di effettuare un tour video 360° registrato prima di qualsiasi tour live, se il tempo lo permette, per tre motivi: (1) Avere una soluzione di riserva per il tour live, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour live registrato) e (3) iniziare a creare una libreria di video 360° di tutti i tuoi siti che può essere utile per molti casi d'uso.
- Tutti i componenti del kit devono essere caricati per almeno 90 minuti prima della riunione live. Raccomandiamo comunque di tenere tutti i dispositivi in carica continua quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni ad hoc non pianificate.
- Avere il kit completamente assemblato (1. base treppiede + 2. batteria Ulanzi + 3. asta estensibile + 4. cam 360°).

- Conferma che sia stato creato uno Spazio di Lavoro per ospitare una riunione live e includi tutti gli Asset pertinenti.

- Invita tutti i partecipanti alla riunione tramite il tuo Spazio di Lavoro. Questo crea un invito sui calendari di tutti i partecipanti e include il link di invito alla riunione.

- Associa e collega le tue cuffie bluetooth o l'altoparlante che intendi utilizzare per il tuo tour alla telecamera.

- Tutti gli utenti smartphone in loco dovrebbero connettersi da una rete diversa dalla rete della telecamera. Questo ridurrà il carico sulla larghezza di banda della rete della telecamera.

- Se sei solo come operatore della telecamera, porta con te uno smartphone nel caso in cui tu voglia condividere la fotocamera dello smartphone e mostrare dettagli fini.

- Conferma che la telecamera 360 possa connettersi al tuo WiFi locale.

- Prima di una riunione Avatour, pianifica il percorso che farai attraverso la struttura. Fai una riunione Avatour di prova con la telecamera e verifica che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Questo può essere visualizzato sullo schermo della telecamera stessa, o come partecipante remoto andando in Impostazioni e attivando Mostra Bitrate.

- Se noti che alcune aree hanno poca o nessuna larghezza di banda, è meglio scattare immagini o fare una registrazione. Queste possono poi essere presentate durante la riunione per la revisione dei partecipanti remoti. Puoi seguire la guida qui che spiega la nostra Acquisizione Rapida per registrare e caricare video/immagini: [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se hai partecipanti remoti che si uniscono alla riunione che non hanno mai usato Avatour prima, fornisci loro un breve riassunto della piattaforma, delle sue funzionalità (video live 360, asset, istantanee, annotazioni, spotlight) e degli strumenti della riunione.

- Puoi iniziare in un'altra soluzione di videoconferenza (ad es. Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudi completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del tuo dispositivo, causandone la disattivazione per Avatour. Inoltre, NON eseguire Avatour E un'altra videoconferenza contemporaneamente poiché questo ridurrà la larghezza di banda disponibile.

- Se hai intenzione di utilizzare la telecamera 360 in un ambiente ad alta temperatura, si raccomanda di utilizzare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la telecamera si surriscaldi e si spenga automaticamente.

### 6.3 Quando si opera la cam in loco per una riunione live in video 360°

- Quando operi la telecamera, assicurati di camminare lentamente. Questo aiuta con la qualità video e riduce qualsiasi potenziale interruzione video quando la connessione di rete della telecamera passa tra punti di accesso WiFi.

- Tieni la telecamera davanti a te e sopra il livello degli occhi. Questo permette a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Per i casi in cui la telecamera deve rimanere stabile, usa il supporto treppiede ed estendi la telecamera all'altezza corretta, preferibilmente al livello degli occhi.

- Connetti sempre la telecamera alla tua rete WiFi locale quando possibile. Per le aree senza accesso WiFi, usa l'hotspot fornito. L'hotspot ha una scheda SIM che si connetterà a una rete cellulare affidabile vicino a te. Tieni sempre l'hotspot spento quando non in uso all'interno poiché altrimenti la cam 360° potrebbe connettersi all'hotspot, cosa che non vogliamo all'interno. Quando sei all'esterno, tieni l'hotspot vicino alla telecamera 360°.

- Quando il bitrate sulla telecamera inizia a scendere sotto i 2 Mbps, cammina più lentamente o fermati completamente finché il segnale non si stabilizza di nuovo. Questo di solito accade quando passi da un Punto di Accesso WiFi a un altro.

- Se sai che la connettività e il video si interromperanno quando ti sposti in una posizione specifica (Esempio: spostandoti da un'area di produzione interna a un'area esterna), avvisa i partecipanti remoti in anticipo.

- Se hai bisogno di mostrare qualcosa in alto dettaglio o scritte piccole, usa il tuo smartphone o quello di un partecipante in loco per unirti alla riunione e presentare la fotocamera (posteriore) del tuo / loro telefono.

- Se possibile raccomandiamo che una persona aggiuntiva sia in loco per aiutare con la condivisione della fotocamera smartphone descritta sopra poiché questo spesso si rivela utile / necessario.

- Idealmente gli utenti smartphone in loco dovrebbero unirsi alla riunione (1) in modalità in loco e (2) su una rete diversa da quella che sta usando la telecamera per non sottrarre larghezza di banda di upload cruciale dalla cam 360°.

- Tutti i partecipanti in loco che si uniscono dal loro smartphone dovrebbero essere silenziati, a meno che non stiano parlando attivamente.