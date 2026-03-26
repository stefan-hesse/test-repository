# Avatour User and Best Practices Guide

## 1. Per tutti gli utenti Avatour {#for-all-avatour-users}

Se sei nuovo su Avatour, le seguenti risorse forniscono un'utile introduzione alla piattaforma e alle sue funzionalità:

1. [Video Come funziona Avatour](https://avatour.com/how-it-works)  
Una breve panoramica delle principali funzionalità di Avatour e di come la piattaforma consente una collaborazione remota immersiva.
2. [FAQ](https://avatour.com/faqs)  
Risposte alle domande frequenti su varie aree.
3. [Glossario](https://avatour.com/glossary)  
Definizioni dei termini e concetti chiave di Avatour.
4. Sito web  
Dai un'occhiata in particolare alla pagina [Funzionalità di Avatour](https://avatour.com/features) insieme alle sezioni dedicate Casi d'uso e Settori per scoprire come Avatour può supportare le tue esigenze specifiche.## 2. Tipi di Utenti Avatour  {#avatour-user-types}

### 2.1 Partecipanti alle Riunioni (Nessun Account richiesto)
Gli utenti possono partecipare alla riunione senza registrarsi per un account Avatour.
Eccezione: Se l'host ha limitato la riunione agli utenti registrati — ad esempio, per consentire solo ai dipendenti interni di partecipare tramite Single Sign-On (SSO) — l'invito del calendario indicherà che i partecipanti devono effettuare l'accesso per autenticarsi.

Gli utenti accedono alla riunione nel seguente modo:

- Ricevono un invito del calendario dall'host.
- Utilizzano il link della riunione nell'invito per partecipare.
- Inseriscono una password della riunione se l'host ne ha abilitata una.
- I partecipanti possono partecipare senza un account Avatour a meno che la riunione non sia limitata e richieda l'accesso per autenticarsi.

#### 2.1.1 Partecipante 

- Può partecipare e interagire completamente (webcam, microfono, chat e funzionalità Presenta).
- Massimo 20 partecipanti interattivi per riunione.

#### 2.1.2 Spettatore

- Può visualizzare la riunione e partecipare solo tramite chat.
- Non può condividere video, utilizzare un microfono, presentare, riprodurre/mettere in pausa Asset o acquisire Snapshot.
- Massimo 10 Spettatori per riunione.
- Insieme ai Partecipanti, una riunione può ospitare fino a 30 partecipanti.

### 2.2 Utenti Registrati

Gli Utenti Registrati hanno un account Avatour. Gli account vengono creati in uno dei seguenti modi:

- **Invitato dall'Admin:** Durante l'onboarding, Avatour configura un **tenant dedicato** per l'organizzazione e crea uno o più **account Admin**. Gli Admin possono quindi **invitare utenti** all'interno dell'organizzazione e assegnarli a **gruppi**, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin). Gli utenti invitati ricevono un **link di registrazione** per completare la configurazione dell'account e impostare una password.  
- **Invitato dall'Host:** Gli Host possono aggiungere utenti come **collaboratori Editor** a un Workspace. Questo consuma una **licenza Host** e garantisce che l'utente abbia accesso a livello Host.  
- **Provisioning automatico SSO (solo livello Enterprise/Business):** Gli account possono essere creati automaticamente dall'IdP. Per impostazione predefinita, gli account provisionati tramite SSO vengono aggiunti al **gruppo Guest**, a meno che non venga sovrascritto tramite **mappature dei gruppi SAML**. Gli Admin possono comunque invitare utenti e assegnare l'appartenenza ai gruppi direttamente anche quando SSO è abilitato.

**Riepilogo:**  

Gli utenti registrati e la loro appartenenza ai gruppi possono essere gestiti in diversi modi:

- **Gestione Admin:** Un Admin nella console Avatour può creare utenti e assegnarli a gruppi, che definiscono il loro ruolo sulla piattaforma (Guest, Host o Admin).  
- **Provisioning SSO:** Per i clienti di livello Enterprise o Business con SSO abilitato, l'IdP può provisionare automaticamente gli account e assegnare l'appartenenza ai gruppi, che definisce il ruolo dell'utente sulla piattaforma.  
- **Utenti invitati dall'Host:** Gli Host possono invitare altri utenti come collaboratori Editor in Workspace specifici. L'assegnazione del ruolo di collaboratore Editor consuma una licenza Host.

**Best Practice Raccomandata (Clienti Enterprise):**  
Per le organizzazioni che prevedono un gran numero di utenti che necessitano di accesso ad Avatour, si raccomanda di **integrare il Single Sign-On (SSO)** e gestire gli utenti e le appartenenze ai gruppi dall'**IdP**. Questo approccio semplifica il provisioning degli account, l'assegnazione dei gruppi e la gestione delle licenze, riducendo il carico amministrativo e garantendo un controllo degli accessi coerente.

#### 2.2.1 Utenti Guest

- Aggiunti al **gruppo Guest**.  
- Possono **visualizzare Asset** all'interno dei Workspace dove sono stati aggiunti come **collaboratori Viewer**.  
- Non possono creare workspace, ospitare riunioni o caricare contenuti.  
- Gli account Guest provisionati tramite SSO **si autenticano tramite l'IdP**; non è richiesta una password gestita da Avatour.

---

#### 2.2.2 Utenti con Licenza (Accesso alla Console Web)

##### Utenti Host (Gruppo: Host)

- Possono creare/gestire Workspace, invitare collaboratori in un workspace, **ospitare riunioni dal vivo**, caricare **Quick Capture**.  
- Hanno accesso alla **Dashboard Host** e all'**App Operatore** sulle telecamere 360° supportate.  

##### Utenti Admin (Gruppo: Admin)

- Include tutte le capacità Host più l'amministrazione completa dell'account.

**I privilegi Admin aggiuntivi includono:**

**Gestione Account**  

- Creare nuovi utenti e assegnarli a gruppi.
- Reimpostare le password quando gestite da Avatour (non applicabile quando SSO è abilitato). 
- Aggiornare utenti Guest a Host.  
- Disattivare utenti (gli account Admin devono prima essere convertiti in Host prima dell'eliminazione).  
- Trasferire asset da un utente Host a un altro durante l'eliminazione.

**Impostazioni**  

- Configurare **impostazioni di sicurezza a livello organizzativo** per asset, workspace e riunioni ospitate sulla piattaforma (ad es., se un Host deve essere presente per avviare una riunione, se i volti devono essere sfocati su tutti i video caricati sulla piattaforma).  
- Abilitare o disabilitare **funzionalità AI** o **registrazione**.  
- Applicare il branding aziendale in modo coerente su tutta la piattaforma se è configurato un **dominio personalizzato**.
  

**Asset e Analytics** 
 
- Visualizzare tutti gli Asset caricati da qualsiasi utente nell'organizzazione.  
- Esaminare l'utilizzo della piattaforma in tutta l'organizzazione.

---

#### 2.2.3 Permessi dei Collaboratori del Workspace

I permessi del Workspace definiscono cosa un utente può fare **all'interno di uno specifico Workspace**. Questi sono separati dall'appartenenza ai gruppi a livello di piattaforma (Guest, Host, Admin).

- **Collaboratore Editor:** Gli utenti con questo permesso possono:
  - Gestire Asset (caricare, rimuovere, sfocare volti, generare riepiloghi)  
  - Gestire le impostazioni delle riunioni (abilitare/disabilitare la registrazione, consentire o rimuovere partecipanti)  
  - Pianificare e ospitare riunioni dal vivo  
  - Generare report basati su modelli predefiniti  
  - Aggiungere o rimuovere collaboratori dal Workspace  

- **Collaboratore Viewer:** Gli utenti con questo permesso hanno accesso in sola lettura agli Asset del Workspace. **Non possono modificare Asset, gestire riunioni o gestire collaboratori**, ma **possono creare Note sugli Asset**.## 3. Per i Partecipanti a Riunioni da Remoto e i Visitatori del Workspace {#for-remote-meeting-participants-and-workspace-visitors}

Avatour consente agli utenti di collaborare in due modi principali:

- **Partecipare a una riunione dal vivo:**  
  Potresti ricevere un **invito sul calendario** per partecipare a una riunione Avatour. Durante la riunione, i partecipanti possono condurre una **visita remota dal vivo al sito** o rivedere insieme le risorse in modo sincrono.

- **Visitare un Workspace:**  
  Potresti anche essere invitato come **collaboratore in un Workspace** per rivedere le risorse **in modo asincrono** (secondo i tuoi tempi).

### 3.1 Come Partecipare a una Riunione Avatour e Visitare un Workspace Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualsiasi Dispositivo "Schermo Piatto" con un Browser Web {#any-flat-screen}
Puoi partecipare a una riunione Avatour da **qualsiasi computer desktop o laptop, smartphone o tablet** utilizzando un browser web.  

##### Partecipare a una Riunione

> **Nota:** Partecipare a una riunione Avatour richiede che tu **conceda i permessi per il microfono**. Accetta eventuali richieste di autorizzazione dal tuo browser.

1. **Tramite invito sul calendario (consigliato):**  
   - Normalmente riceverai un **invito sul calendario** con un **link diretto per partecipare** (ad esempio: `https://avatour.live/join?s=xxxxx`).  
   - Cliccando il link verrà automaticamente inserito il **codice riunione di 5 caratteri** e verrai portato alla riunione.
   - **Autenticazione richiesta:** Alcune riunioni sono limitate agli utenti registrati. In questo caso, l'invito indicherà che devi **effettuare l'accesso per accedere alla riunione**.  
   - **Riunioni protette da password:** Alcune riunioni potrebbero richiedere una password. In tal caso, l'invito includerà la password che devi inserire per partecipare.

2. **Tramite codice riunione:**  
   - Se l'organizzatore condivide separatamente un **codice riunione di 5 caratteri**, vai su [https://avatour.live/join](https://avatour.live/join), inserisci il tuo **nome** e il **codice riunione**, e partecipa alla riunione.  
   - Se la riunione è **protetta da password**, inserisci la password fornita dall'organizzatore.  
   - Se la riunione richiede **l'autenticazione**, dovrai **accedere con il tuo account Avatour** prima di partecipare.

> **Suggerimento 1:** Se la tua fotocamera o il microfono non funzionano, potrebbero essere in uso da un'altra applicazione (ad esempio, Microsoft Teams o Zoom). Chiudi eventuali app che potrebbero utilizzare la fotocamera o il microfono, poi esci e rientra nella riunione Avatour.  

> **Suggerimento 2:** Se non riesci ancora a partecipare alla riunione, esegui questo test: [https://avatour.live/test](https://avatour.live/test).  
> Il test può identificare se il tuo **firewall aziendale o la rete** sta bloccando l'accesso, e fornirà informazioni per guidare le discussioni con il tuo team IT.  

> **Suggerimento 3:** **Non** utilizzare le app Avatour per iOS o Android per partecipare alle riunioni. Queste app sono necessarie solo quando **trasmetti una riunione dal vivo da una fotocamera Insta360**, poiché quelle fotocamere non possono eseguire direttamente il software Avatour 360° e richiedono uno smartphone di supporto.

##### Visitare un Workspace Senza Partecipare a una Riunione

Puoi accedere a un Workspace senza partecipare a una riunione dal vivo nei seguenti modi:

- **Workspace Pubblico:**  
  Se il Workspace è pubblico, il link può essere accessibile direttamente—non è richiesto l'accesso.

- **Workspace con Restrizioni:**  
  Se il Workspace ha restrizioni, devi essere aggiunto come **collaboratore** con permessi di **Editor** o **Visualizzatore**.

  1. Quando vieni aggiunto come collaboratore, riceverai una **notifica email** con un link al Workspace.
  2. Clicca il link nell'email per aprire il Workspace. Se non hai già effettuato l'accesso, ti verrà chiesto di **accedere o completare la registrazione**.
  3. Una volta effettuato l'accesso, il Workspace si aprirà automaticamente.

  In alternativa, puoi accedere su  
  https://avatour.live/login  
  e accedere al Workspace dalla tua **lista di Workspace**.

#### 3.1.2 Visore VR {#vr-headset}
Puoi partecipare a una riunione e visitare un workspace da una gamma di visori Meta e Pico compatibili. Per farlo: 

1. Installa la nostra app Avatour dal rispettivo app store VR: [Come installare l'app Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carica la nostra app e inserisci il codice riunione o seleziona un Workspace per partecipare a una riunione. Per maggiori informazioni su come utilizzare la nostra app VR, consulta il nostro articolo della Knowledge Base [qui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Strumenti di Collaborazione per Riunioni e Workspace {#meeting-tools}

Avatour consente la collaborazione in due contesti principali:

1. **Riunioni (sincrone):** Collabora in tempo reale con altri partecipanti, incluse visite al sito dal vivo o revisione insieme di risorse registrate.  
2. **Workspace (asincroni):** Rivedi e interagisci con le risorse secondo i tuoi tempi, 24/7.

Gli **strumenti di collaborazione sono per lo più simili** tra riunioni e workspace, con alcune differenze dovute al contesto sincrono vs asincrono.

#### 3.2.1 Layout dell'Interfaccia

L'interfaccia Avatour è organizzata intorno a tre aree principali:

- **Pannello sinistro** – Risorse del workspace e strumenti di supporto  
- **Canvas centrale** – Area di visualizzazione principale per video dal vivo o risorse  
- **Pannello destro** – Informazioni contestuali, come partecipanti, riunioni o chat  

La maggior parte delle interazioni vengono avviate dal **menu inferiore**.  
Cliccando un'opzione del menu si apre un **pannello laterale** sul lato sinistro o destro dello schermo, mentre il **canvas centrale** rimane l'area di visualizzazione principale.

---
#### 3.2.2 Esempio di Visualizzazione Riunione

Ecco un esempio di visualizzazione in una Riunione Avatour:

![Interfaccia Riunione Avatour con Pannello Risorse, Canvas vuoto e Pannello Partecipanti](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Riunione Avatour con Pannello Risorse (sinistra), Canvas (centro) e Pannello Partecipanti (destra)*

---

#### 3.2.3 Esempio di Visualizzazione Workspace

Ecco un esempio di visualizzazione Workspace:

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
- **Fotocamera** – Attiva o disattiva la tua webcam.  
- **Microfono** – Disattiva o attiva il tuo audio.  
- **Presenta** – Presenta una risorsa, il desktop o il feed della webcam (vedi sezione Presenta sotto).  
- **Strumenti Organizzatore** (solo organizzatori):  
  - **Blocca Focus** – Blocca la visualizzazione per tutti i partecipanti.  
  - **Silenzia Tutti** – Silenzia tutti i partecipanti.  
- **Attiva Schermo Intero** – Rendi la scheda della riunione a schermo intero.  
- **Esci dalla Riunione** – Lascia la riunione.  
- **Avvia Registrazione** – Usa questo pulsante per avviare e fermare manualmente la registrazione durante una riunione. In alternativa, le riunioni possono essere registrate automaticamente se l'**avvio automatico della registrazione** è abilitato nelle impostazioni del workspace. In entrambi i casi, le registrazioni vengono salvate nelle risorse del workspace.
- **Mappa** – Apri o chiudi il pannello mappa per le risorse con traccia GPS. Cliccando una posizione si salta al punto esatto nel video. La mappa si aggiorna in tempo reale mentre il video viene riprodotto.
- **Partecipanti** – Apri o chiudi il pannello partecipanti.  
- **Info Riunione** – Visualizza il codice riunione, il link di invito e accedi ai tutorial correlati.  

![Info Riunione Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Pannello Laterale Info Riunione Avatour*

- **Impostazioni** – Regola le impostazioni di lingua, audio e video. Per le riunioni video 360° dal vivo, usa **Mostra Bitrate** per monitorare le statistiche di connettività.

> Suggerimento: Invia il link della riunione o aggiungilo a un elemento del calendario per invitare i partecipanti.

---

##### Menu Presenta

L'opzione **Presenta** nel menu inferiore della riunione ti consente di condividere contenuti con tutti i partecipanti.

- **Fotocamera** – Condividi la fotocamera del tuo smartphone/tablet. Può essere utilizzata anche durante una riunione video 360° dal vivo per sovrapporre una visualizzazione secondaria per primi piani o dettagli specifici. 
- **Desktop** – Condividi lo schermo del tuo desktop con tutti i partecipanti.  
- **Risorsa** – Presenta una risorsa dal workspace. Selezionando una risorsa si apre la **Barra strumenti Risorsa**, che fornisce controlli di riproduzione e strumenti di collaborazione specifici per la risorsa presentata.

##### Barra Strumenti Risorsa (Riunione)

Quando presenti una risorsa in una riunione, la **Barra Strumenti Risorsa** appare sopra il canvas. Ecco gli strumenti e le voci di menu disponibili quando <u>presenti una Risorsa in una Riunione</u> - spiegati da sinistra a destra.

![Menu Avatour durante la Presentazione di una Risorsa in una Riunione](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour quando presenti una Risorsa in una Riunione*


- **Timeline Video / Barra di Avanzamento** – Mostra l'avanzamento del video con note e argomenti chiave estratti dall'audio. Clicca una nota o un argomento per saltare a quel momento e aprire la nota. Include controlli **Play / Pausa**.   
- **Snapshot** – Cattura un'immagine 360° o 2D dalla risorsa.  
- **Spotlight** – Evidenzia un'area specifica per tutti i partecipanti durante le sessioni dal vivo.  
- **Mostra/Nascondi Punto di Vista (POV)** – Mostra dove ogni partecipante sta guardando nel video 360°.  
- **Note** – Crea note ancorate a momenti specifici nella risorsa. Le note possono essere categorizzate (Osservazione, Problema, Azione, Raccomandazione), tracciate per stato (Aperta → In Corso → Risolta) e condivise tramite link diretti.  

  ![Nota Avatour e Filtro Note](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota Avatour e Filtri Note*

  - **Note da Comando Vocale** – Questi sono segnaposto generati automaticamente quando la registrazione rileva menzioni come "inserisci nota", "prendi una nota" o "fai una nota". Queste note appaiono sulla timeline e devono essere **posizionate e finalizzate** dall'utente. 

  ![Note Avatour - Generate da Comando Vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Note Avatour - Generate da Comando Vocale*

- **Pannello Note e Riepilogo** – Apre un pannello laterale che mostra tutte le note, gli argomenti chiave e un riepilogo esecutivo per la risorsa. Cliccando un elemento si salta a quel momento nel video.  

  ![Riepilogo Esecutivo Risorsa Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Riepilogo Esecutivo Avatour durante la presentazione di una Risorsa in una Riunione*

  ![Argomenti Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Argomenti Avatour durante la presentazione di una Risorsa in una Riunione*

  Dal **Pannello Laterale**, puoi **stampare un report della risorsa** o **scaricarlo come## 4. Per utenti Host e Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}

Quando accedi al tuo Account Utente Avatour, avrai accesso alla **Console Web**.  

### 4.1 Console Web - Panoramica del Menu Principale {#web-console-overview-main-menu}

Sul lato sinistro, vedrai le seguenti voci di menu:

![Console Web Avatour - Menu Principale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principale*

- **Workspace** – Organizza i tuoi contenuti in modo efficiente. Ogni workspace contiene **Risorse**, **Collaboratori**, **Riunioni** e **Impostazioni**.  
- **Risorse** – Accedi e gestisci tutte le tue risorse (video, immagini, PDF). Gli Admin possono visualizzare tutte le risorse dell'account e le risorse condivise sono visibili a tutti gli utenti.  
- **Profilo** – Gestisci la tua lingua e password.  
- **Analisi** – Monitora l'attività delle sessioni, l'utilizzo dei workspace e le metriche ROI.  
- **Impostazioni** *(Solo Admin)* – Configura le impostazioni predefinite di workspace, riunioni e risorse in tutta l'organizzazione. Gli Admin possono anche personalizzare il branding (logo, colori, sfondi).  
- **Account** *(Solo Admin)* – Gestisci gli utenti registrati e le telecamere 360°.  
- **Login Dispositivo** – Inserisci il codice visualizzato sulla tua telecamera 360° per associarla al tuo account.  
- **Tutorial** – Accedi ai tutorial guidati.  
- **Esci** – Disconnettiti dalla console.

> Sezioni come Profilo, Login Dispositivo, Tutorial ed Esci sono autoesplicative e non hanno sottosezioni dettagliate.

---

### 4.2 Console Web - Dettagli per Voce di Menu (con immagini) {#web-console-details-by-menu-item}

#### 4.2.1 Workspace

I workspace sono unità organizzative flessibili che ti permettono di gestire risorse, collaboratori e riunioni in un unico posto. Puoi creare un nuovo workspace con il pulsante **Nuovo Workspace** nell'angolo in alto a destra.

![Console Web Avatour - Voce Menu Principale Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Voce Menu Principale Workspace*

Clicca sull'icona della campanella per vedere un riepilogo dell'attività del workspace negli ultimi 7 giorni.

![Console Web Avatour - Attività Recenti Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Attività Recenti Workspace*

All'interno di un workspace:

![Workspace Avatour con Pannello Risorse, Canvas vuoto e Pannello Riunioni](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace con Risorse (sinistra), Canvas (centro), Riunioni (destra)*

- **Risorse** – Gestisci i file allocati a questo workspace.  
- **Collaboratori** – 
  Controlla l'accesso ai workspace tramite 
  - **Visualizzatore** – Può visualizzare le risorse. L'invito crea un utente Ospite se necessario.  
  - **Editor** – Controllo completo del workspace, stessi diritti dell'Host. L'invito promuove l'utente a Host se necessario.  
> Più utenti possono accedere a un workspace contemporaneamente senza una riunione. I workspace pubblici e le impostazioni di accesso alle riunioni forniscono accessi alternativi.  
- **Report** – Genera un report utilizzando un modello checklist sulle risorse selezionate del workspace.  

![Report Workspace Avatour e Selezione Risorse](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Report Workspace e Selezione Risorse*

- **Mappa** – Visualizza le posizioni delle risorse abilitate GPS su una mappa.  
- **Riunioni** – Organizza le riunioni nel workspace.  
- **Impostazioni** – Configura le impostazioni predefinite del workspace e delle riunioni:

![Impostazioni Avatour - Vista Workspace](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Impostazioni Workspace*

**Impostazioni Workspace**

- **Modello Report** – Seleziona il modello checklist per i report AI.  
- **Abilita Notifiche** – Email di riepilogo giornaliero per le modifiche di stato delle note.  

![Notifiche Email - Esempio](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Esempio Notifiche Email*

- **Workspace Pubblico** – Chiunque abbia il link può visualizzare le risorse direttamente.

**Impostazioni Riunione**
  
* **Autenticazione richiesta** – I partecipanti devono effettuare l'accesso.  
* **Consenti accesso ospiti** – Permetti agli utenti non registrati di visualizzare le risorse.  
* **Avvio Automatico Registrazione / Avvio Manuale** – Scegli se le riunioni vengono registrate automaticamente o avviate manualmente.  
* **Richiedi host** – L'host deve ammettere i partecipanti; la riunione termina quando l'host esce.  
* **Consenti accesso spettatore** – Partecipa senza microfono o telecamera; comunica tramite chat.  
* **Riunioni protette da password** – Richiedi una password per partecipare.  
* **Mostra Domanda Risparmio Viaggi** – Chiedi ai partecipanti se la riunione ha ridotto gli spostamenti.  

> Le impostazioni possono essere combinate (es., nessun host richiesto ma protetto da password).

---

#### 4.2.2 Risorse

Gestisci tutti i video 360°/2D, immagini e PDF. Carica/scarica risorse, alloca ai workspace, condividi con altri utenti, rinomina, stampa/scarica report, attiva la sfocatura volti e la sintesi AI.

![Console Web Avatour - Voce Menu Principale Risorse](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Voce Menu Principale Risorse*

---

#### 4.2.3 Analisi

Fornisce informazioni su riunioni, utilizzo dei workspace e metriche ROI.

![Console Web Avatour - Voce Menu Principale Analisi (1 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Panoramica Analisi*

![Console Web Avatour - Voce Menu Principale Analisi (2 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Attività Riunioni & Utilizzo Workspace*

![Console Web Avatour - Voce Menu Principale Analisi (3 di 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilizzo Licenze Dispositivi & ROI*## 5. In loco - Come utilizzare il kit chiavi in mano Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Per iniziare
[Guida rapida – Kit chiavi in mano Avatour 3.1 (configurazione Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Segui la guida per disimballare, assemblare e accendere la tua fotocamera.

---

### 5.2 Suggerimenti utili

#### Batteria esterna – Riunioni dal vivo più lunghe e gestione termica migliorata 

- **Se il tuo kit include una batteria Ulanzi:** Fissala tra la base del treppiede e l'asta estensibile, quindi collega la batteria alla fotocamera tramite USB-C.  

- **Se il tuo kit include un'asta batteria Telesin:** Monta la fotocamera direttamente sull'asta batteria estensibile Telesin e collegala tramite USB-C.  

Utilizzando la batteria esterna:

1. Estendi la durata totale della batteria da ~40 minuti (solo batteria della fotocamera) a ~3 ore.  
2. Aggiungi stabilità alla configurazione della fotocamera.  
3. Aiuta a prevenire potenziali surriscaldamenti.  

> Ti consigliamo di utilizzare sempre la batteria esterna fin dall'inizio, specialmente per le riunioni dal vivo.

#### Considerazioni audio per riunioni dal vivo e registrazioni

- **Ambienti rumorosi:** 
  Usa le cuffie Shokz incluse nel tuo kit per una cattura audio chiara.  
  - **Accensione/Spegnimento:** Tieni premuto il pulsante "+" per 3 secondi (LED blu = acceso, LED rosso = spento).  
  - **Modalità di accoppiamento Bluetooth:** Con le cuffie spente, tieni premuto il pulsante "+" per 5 secondi (il LED lampeggia blu/rosso).  
  - **Volume:** Usa i pulsanti "+" e "-".  

- **Ambienti più silenziosi / più partecipanti vicino alla fotocamera:** 
  Usa l'altoparlante clip-on NoxGear. Non è di alta fedeltà come gli altoparlanti da conferenza (es. Jabra Speak), ma è facile da agganciare alla camicia e cattura efficacemente le voci vicine.  
  - **Accensione/Spegnimento:** Tieni premuto il pulsante Play/Pausa per 2 secondi.  
  - **Modalità di accoppiamento Bluetooth:** Entra automaticamente in modalità di accoppiamento quando acceso (il LED lampeggia blu/rosso; blu fisso quando accoppiato).  
  - **Volume:** Usa i pulsanti "+" e "-".  

- **Utilizzo del tuo dispositivo:** Se preferisci un'alternativa (es. un altoparlante da conferenza o cuffie personali), puoi accoppiarlo tramite la fotocamera: Impostazioni → Bluetooth.  

#### Connettività, connettività, connettività
**Prima di iniziare:** Assicura la connessione internet tramite:

- **WiFi locale** (preferito)
- **Rete mobile** (se fuori dalla copertura WiFi)

**Larghezza di banda consigliata:** 10 Mbps uplink/downlink per lo streaming completo a 360° (~5 Mbps). Una larghezza di banda inferiore (1–2 Mbps) funziona solo stando fermi.

##### Test della velocità di rete
- **Test in posizione singola:** Qualsiasi strumento di verifica della velocità che usi normalmente (es. [Speedtest](https://www.speedtest.net)) per verificare la larghezza di banda in upload.   
- **Test camminando nel sito:** Dalla fotocamera: Impostazioni → Rete → Test di connessione. Cammina attraverso l'intero spazio per confermare copertura e larghezza di banda.

##### WiFi locale
- Altamente consigliato per connessioni stabili.  
- Se l'IT richiede la whitelist, trova l'indirizzo MAC: Impostazioni → Info → Indirizzo WiFi.

##### Rete mobile
**Opzione A: Hotspot e SIM forniti nel kit**  

- Collega l'hotspot GlocalMe all'asta batteria Telesin (magnete).  
- Garantisce nessuna interferenza e mantiene la connessione se ti allontani dalla fotocamera.  
- Risoluzione dei problemi:
  - Conferma la SIM preinstallata (non Cloud SIM).  
  - Abilita il 5G nel Gestore scheda SIM.  
  - Verifica l'APN corretto per la tua regione ([guida alla configurazione APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opzione B: Hotspot personale / SIM**
- Usa il tuo smartphone o un hotspot dedicato.  

**Nota importante:**  
> Mantieni l'hotspot spento mentre sei connesso al WiFi; abilitalo solo quando sei fuori copertura. Il sistema operativo della fotocamera passa dinamicamente tra le reti WiFi in base alla potenza del segnale e potrebbe inavvertitamente passare all'hotspot anche quando il WiFi è disponibile.

> Le reti mobili potrebbero limitare la larghezza di banda inaspettatamente. Verifica con il tuo operatore i limiti del piano dati, o contatta il supporto Avatour se usi il nostro hotspot e SIM.

##### Situazioni di bassa larghezza di banda
- Pre-registra video delle location per la riproduzione successiva ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Condividi uno stream della fotocamera dello smartphone per integrare le aree a bassa larghezza di banda (0,1–0,3 Mbps upload).

##### Nessuna connettività
- Si possono utilizzare solo video pre-registrati ([guida alla registrazione](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Altri partecipanti in loco – Migliori pratiche

Quando più partecipanti si uniscono a una riunione Avatour dal vivo dalla stessa posizione della fotocamera a 360°, è fondamentale una gestione attenta di **audio e larghezza di banda**:  

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera a 360°.  
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

#### Altri partecipanti in loco – Migliori pratiche

Quando più partecipanti si uniscono a una riunione Avatour dal vivo dalla stessa posizione della fotocamera a 360°, è fondamentale una gestione attenta di **audio e larghezza di banda**:  

- Ogni smartphone, tablet o laptop connesso in loco consuma larghezza di banda di rete e può influire negativamente sul feed della fotocamera a 360°.  
- Più microfoni e altoparlanti nello stesso spazio possono causare **feedback audio**, rendendo l'esperienza della riunione spiacevole per tutti i partecipanti.

Per affrontare queste sfide, segui queste **migliori pratiche**:

- **Usa cuffie con cavo o wireless:** Preferibilmente con cancellazione del rumore per prevenire eco e feedback.  
- **Modalità In Loco:** Unisciti alla riunione in modalità In Loco quando sei fisicamente presente vicino alla fotocamera a 360°.  
  - Questa modalità è ottimizzata per l'uso in loco:  
    - Silenzia il microfono e l'altoparlante del partecipante per impostazione predefinita.  
    - **Non** invia il feed della fotocamera del partecipante.  
    - **Non** visualizza il feed della fotocamera a 360° nel browser del partecipante.  
    - Conserva la larghezza di banda di rete, garantendo che la fotocamera a 360° abbia il massimo upload disponibile per lo streaming dal vivo.  
    - Utile quando un utente vuole condividere dettagli specifici; **puoi condividere la tua fotocamera** per visualizzazioni mirate.  
- **Silenzia quando non stai parlando attivamente:** Previene feedback audio indesiderati e distrazioni.  
- **Usa una rete separata se possibile:** Connetti il tuo smartphone a una rete diversa da quella della fotocamera per ridurre le interferenze.  

Seguire queste linee guida garantisce un tour dal vivo fluido e di alta qualità sia per i partecipanti in loco che per quelli da remoto.

### 5.3 App Avatour Camera

Ecco (1) il Livello Principale, (2) Impostazioni e (3) i menu delle Impostazioni di Rete.

![App Avatour Camera 360° - Tre Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App Avatour Camera 360° - 3 Menu*

**Quick Capture** - Per la registrazione video a 360° offline. - Per una descrizione dettagliata vedi [Come si registrano e caricano video a 360° con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Consigliamo di utilizzare un dispositivo audio esterno (connesso via bluetooth). N.B. Puoi anche fare video e foto 2D standard - basta cambiare la modalità tra 360° e 2D nell'angolo in basso a destra una volta nella schermata QC.

**Live Meeting** - Per videoconferenze dal vivo a 360°. Vedrai i tuoi spazi di lavoro e cliccando su uno di essi avvierai lo streaming video dal vivo dalla fotocamera a 360°. Prima di poter unirti alla riunione con la tua fotocamera a 360° devi connettere un dispositivo audio via bluetooth. Per una descrizione dettagliata vedi [Come avviare una riunione Live Capture con la tua fotocamera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Quando ospiti una riunione Live Capture con la tua fotocamera a 360°, avrai a disposizione strumenti di riunione simili a quelli dell'esperienza web. Ecco un link al nostro articolo della Knowledge Base che spiega questi strumenti in maggiore dettaglio: [Strumenti App Operatore](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Gallery** - Trova qui tutti i tuoi video e foto a 360° per il caricamento sulla Console Web Avatour.

**Settings** - All'interno delle Impostazioni, hai le seguenti opzioni:

- **Network**: Questa opzione ti permette di cambiare a quale rete WiFi è connessa la fotocamera o eseguire un test di connessione di rete per visualizzare il throughput di streaming
- **Live Capture**: Regola le impostazioni di Live Capture in base alla larghezza di banda disponibile, alla sensibilità VR degli ospiti, o se sono installate le lenti protettive della fotocamera:
  - **Target Frame** **Rate**: Regola il frame rate per il tuo video Live Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma richiederanno più larghezza di banda in upload. Predefinito: 15 fps
  - **Target Bitrate**: Ti permette di aumentare o diminuire il bitrate massimo di streaming per il tuo Live Capture. Puoi impostare il bitrate target tra 1 Mbps e 10 Mbps. Bitrate più alti risulteranno in una risoluzione video più alta, ma richiederanno più larghezza di banda in upload. Predefinito: 5 Mbps
  - **Optimize Motion**: Questo diminuirà il frame rate del video, generando meno carico sulla larghezza di banda in upload della tua rete, e aumenterà il bitrate di streaming. Inoltre, questa opzione aiuta a ridurre il mal di movimento per i partecipanti VR. Predefinito: Off
  - **Protective Lenses**: Questo influenzerà come il video a 360° viene unito a seconda se le lenti protettive sono state installate sulla tua fotocamera. Se non hai lenti protettive, imposta su "No". Se hai ricevuto un Kit 3.0, hai lenti protettive preinstallate e dovresti impostare su "Yes". Predefinito: Yes

- **Quick Capture**: Regola le impostazioni di Quick Capture in base al frame rate video preferito, alla larghezza di banda disponibile per i caricamenti video registrati, o se sono installate le lenti protettive della fotocamera. Quick Capture ha una risoluzione fissa di 4k che di solito trova un buon equilibrio tra qualità video e dimensione del file. (Per risoluzioni più alte puoi usare le app native della fotocamera, anche sulla PanoX V2, per dettagli vedi [Come si registrano e caricano video a 360° con l'App Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Target Frame Rate**: Regola il frame rate per le tue registrazioni video Quick Capture tra 15 fps, 24 fps e 30 fps. Frame rate più alti producono un video più fluido, ma aumenteranno la dimensione del file e il tempo di caricamento. Consigliato: 30 fps
  - **Target Bitrate**: Imposta il bitrate target per i caricamenti Quick Capture tra 5 Mbps e 20 Mbps. Bitrate più bassi aumentano la velocità di caricamento, ma diminuiranno la qualità video. Consigliato: 20 Mbps
  - **Protective Lenses**: *Vedi la sezione Protective Lenses per Live Capture sopra*
- **About**: Visualizza il numero di serie del dispositivo e la versione del software

**Account** - Per l'accesso con il tuo account host o admin Avatour.## 6. Consigli sulle Migliori Pratiche {#best-practice-advice}

### 6.1 Primi Utilizzi (informali) e Familiarizzazione

Per i primi utilizzi e per familiarizzare con la Console Web Avatour e il Kit Chiavi in Mano Avatour, raccomandiamo i seguenti passaggi:

1. Portate il kit a casa e provatelo con familiari e amici utilizzando la vostra connessione internet domestica.
2. Portate il kit in ufficio e collegatevi a una rete aziendale (potrebbero emergere problematiche aziendali, ad es. firewall aziendali - ma saprete dal primo passaggio che Avatour funziona e questo è un argomento da risolvere con il vostro team IT con l'aiuto di Avatour).
3. Iniziate a usare Avatour in loco (fuori dal vostro ufficio) presso la sede della riunione dove i partecipanti remoti dovrebbero normalmente recarsi. Potrebbero emergere ulteriori problematiche di connettività. Avatour può aiutare in collaborazione con il vostro team IT.
4. Iniziate a utilizzarlo con partecipanti remoti interni ed esterni.

### 6.2 Prima di una Riunione Live con Video a 360°

- Raccomandiamo di effettuare un tour video a 360° registrato prima di qualsiasi tour live, se il tempo lo consente, per tre motivi: (1) Avere una soluzione di riserva per il tour live, (2) avere qualcosa per la documentazione e la revisione successiva (oltre al tour live registrato) e (3) iniziare a creare una libreria di video a 360° di tutti i vostri siti che può essere utile per molti casi d'uso.
- Tutti i componenti del kit devono essere caricati per almeno 90 minuti prima della riunione live. Raccomandiamo comunque di tenere tutti i dispositivi sempre in carica quando non in uso. In questo modo tutti i dispositivi saranno sempre pronti, anche per riunioni ad hoc non pianificate.
- Tenete il kit completamente assemblato (1. base del treppiede + 2. batteria Ulanzi + 3. asta estensibile + 4. cam a 360°).

- Confermate che sia stato creato uno Spazio di Lavoro per ospitare una riunione live e includete tutti gli Asset pertinenti.

- Invitate tutti i partecipanti alla riunione attraverso il vostro Spazio di Lavoro. Questo crea un invito nei calendari di tutti i partecipanti e include il link di invito alla riunione.

- Abbinate e collegate le vostre cuffie o altoparlanti bluetooth che intendete usare per il tour alla videocamera.

- Tutti gli utenti smartphone in loco dovrebbero connettersi da una rete diversa da quella della videocamera. Questo ridurrà il carico sulla larghezza di banda della rete della videocamera.

- Se siete soli come operatore della videocamera, portate con voi uno smartphone nel caso vogliate condividere la fotocamera dello smartphone e mostrare dettagli precisi.

- Confermate che la videocamera a 360° possa connettersi al vostro WiFi locale.

- Prima di una riunione Avatour, pianificate il percorso che farete attraverso la struttura. Fate una riunione Avatour di prova con la videocamera e verificate che tutte le aree abbiano bitrate superiori a 1 Mbps di larghezza di banda. Questo può essere visto sullo schermo della videocamera stessa, o come partecipante remoto andando in Impostazioni e attivando Mostra Bitrate.

- Se notate che alcune aree hanno poca o nessuna larghezza di banda, è meglio scattare immagini o effettuare una registrazione. Queste possono poi essere presentate durante la riunione per la revisione dei partecipanti remoti. Potete seguire la guida qui che spiega la nostra Cattura Rapida per registrare e caricare video/immagini: [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se avete partecipanti remoti che si uniscono alla riunione e non hanno mai usato Avatour prima, fornite loro un breve riepilogo della piattaforma, delle sue funzionalità (video live a 360°, asset, istantanee, annotazioni, spotlight) e degli strumenti della riunione.

- Potete iniziare in un'altra soluzione di videoconferenza (ad es. Teams, Zoom, Google Meet) ma prima di passare ad Avatour, chiudete completamente l'altra applicazione di videoconferenza. In alcuni casi, queste altre applicazioni daranno priorità al microfono/altoparlanti/webcam del vostro dispositivo, causando la loro disattivazione per Avatour. Inoltre, NON eseguite Avatour E un'altra videoconferenza contemporaneamente poiché questo ridurrà la larghezza di banda disponibile.

- Se prevedete di usare la videocamera a 360° in un ambiente ad alta temperatura, si raccomanda di usare il modulo di raffreddamento (solo Pilot Pano). Questo aiuterà a ridurre le possibilità che la videocamera si surriscaldi e si spenga automaticamente.

### 6.3 Durante l'Utilizzo della Cam in Loco per una Riunione Live con Video a 360°

- Quando operate la videocamera, assicuratevi di camminare lentamente. Questo aiuta la qualità video e riduce eventuali interruzioni video quando la connessione di rete della videocamera passa da un punto di accesso WiFi all'altro.

- Tenete la videocamera davanti a voi e sopra il livello degli occhi. Questo permette a tutti i partecipanti remoti di vedere la maggior parte dell'area circostante.

- Nei casi in cui la videocamera deve rimanere stabile, usate il supporto del treppiede ed estendete la videocamera all'altezza corretta, preferibilmente al livello degli occhi.

- Collegate sempre la videocamera alla vostra rete WiFi locale quando possibile. Per le aree senza accesso WiFi, usate l'hotspot fornito. L'hotspot ha una scheda SIM che si collegherà a una rete cellulare affidabile nelle vostre vicinanze. Tenete sempre l'hotspot spento quando non in uso all'interno poiché altrimenti la cam a 360° potrebbe connettersi all'hotspot, cosa che non vogliamo al chiuso. Quando siete all'esterno, tenete l'hotspot vicino alla videocamera a 360°.

- Quando il bitrate sulla videocamera inizia a scendere sotto i 2 Mbps, camminate più lentamente o fermatevi completamente finché il segnale non si stabilizza di nuovo. Questo di solito accade quando passate da un Punto di Accesso WiFi a un altro.

- Se sapete che la connettività e il video cadranno spostandovi in una posizione specifica (Esempio: spostandovi da un'area di produzione interna a un'area esterna), avvisate in anticipo i partecipanti remoti.

- Se dovete mostrare qualcosa in alta definizione o scritte piccole, usate il vostro smartphone o quello di un partecipante in loco per unirvi alla riunione e presentare la fotocamera (posteriore) del vostro/loro telefono.

- Se possibile raccomandiamo che una persona aggiuntiva sia in loco per aiutare con la condivisione della fotocamera dello smartphone descritta sopra, poiché questo spesso si rivela utile/necessario.

- Idealmente gli utenti smartphone in loco dovrebbero unirsi alla riunione (1) in modalità in loco e (2) su una rete diversa da quella che sta usando la videocamera per non sottrarre larghezza di banda di upload cruciale alla cam a 360°.

- Tutti i partecipanti in loco che si collegano dal loro smartphone dovrebbero avere il microfono disattivato, a meno che non stiano parlando attivamente.