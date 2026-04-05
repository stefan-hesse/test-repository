# Avatour User and Best Practices Guide

## 1. Für alle Avatour-Nutzer {#for-all-avatour-users}

Wenn Sie Avatour noch nicht kennen, bieten die folgenden Ressourcen eine hilfreiche Einführung in die Plattform und ihre Funktionen:

1. [Video „So funktioniert Avatour“](https://avatour.com/how-it-works)  
Ein kurzer Überblick über die wichtigsten Funktionen von Avatour und darüber, wie die Plattform eine immersive Zusammenarbeit aus der Ferne ermöglicht.
2. [FAQs](https://avatour.com/faqs)  
Antworten auf häufig gestellte Fragen.
3. [Glossar](https://avatour.com/glossary)  
Definitionen der wichtigsten Begriffe und Konzepte, die bei Avatour häufig verwendet werden.
4. Website  
Werfen Sie insbesondere einen Blick auf die [Avatour-Funktionen](https://avatour.com/features) sowie auf die speziellen Abschnitte zu Anwendungsfällen und Branchen, um zu erfahren, wie Avatour Ihre spezifischen Anforderungen unterstützen kann.

## 2. Avatour-Benutzertypen  {#avatour-user-types}

### 2.1 Teilnehmer an Besprechungen (kein Konto erforderlich)
Benutzer können an der Besprechung teilnehmen, ohne sich für ein Avatour-Konto zu registrieren.
Ausnahme: Wenn der Gastgeber die Besprechung auf registrierte Benutzer beschränkt hat – beispielsweise, um nur internen Mitarbeitern die Teilnahme über Single Sign-On (SSO) zu ermöglichen –, wird in der Kalendereinladung darauf hingewiesen, dass sich die Teilnehmer zur Authentifizierung anmelden müssen.

Benutzer nehmen wie folgt an der Besprechung teil:

- Sie erhalten eine Kalendereinladung vom Gastgeber.
- Sie nutzen den Besprechungslink in der Einladung, um teilzunehmen.
- Sie geben ein Besprechungskennwort ein, falls der Gastgeber eines aktiviert hat.
- Teilnehmer können ohne Avatour-Konto teilnehmen, es sei denn, die Besprechung ist eingeschränkt und erfordert eine Anmeldung zur Authentifizierung.

#### 2.1.1 Teilnehmer 

- Kann teilnehmen und uneingeschränkt interagieren (Webcam, Mikrofon, Chat und Präsentationsfunktionen).
- Maximal 20 interaktive Teilnehmer pro Besprechung.

#### 2.1.2 Zuschauer

- Kann die Besprechung verfolgen und nur über den Chat teilnehmen.
- Kann kein Video teilen, kein Mikrofon verwenden, keine Präsentationen halten, keine Assets abspielen/anhalten und keine Schnappschüsse aufnehmen.
- Maximal 10 Zuschauer pro Besprechung.
- Zusammen mit den Teilnehmern kann ein Meeting bis zu 30 Teilnehmer umfassen.

### 2.2 Registrierte Benutzer

Registrierte Benutzer verfügen über ein Avatour-Konto. Konten werden auf eine der folgenden Arten erstellt:

- **Vom Administrator eingeladen:** Während der Einbindung richtet Avatour einen **dedizierten Mandanten** für die Organisation ein und erstellt ein oder mehrere **Administratorkonten**. Admins können dann **Benutzer** innerhalb der Organisation **einladen** und sie **Gruppen** zuweisen, die ihre Rolle auf der Plattform definieren (Gast, Host oder Admin). Eingeladene Benutzer erhalten einen **Anmeldelink**, um die Kontoeinrichtung abzuschließen und ein Passwort festzulegen.  
- **Vom Host eingeladen:** Hosts können Benutzer als **Mitarbeiter mit Bearbeitungsrechten** zu einem Workspace hinzufügen. Dies verbraucht eine **Host-Lizenz** und stellt sicher, dass der Benutzer Zugriff auf Host-Ebene hat.  
- **Automatische SSO-Bereitstellung (nur Enterprise-/Business-Tier):** Konten können automatisch vom IdP erstellt werden. Standardmäßig werden SSO-bereitgestellte Konten der **Gastgruppe** hinzugefügt, sofern dies nicht über **SAML-Gruppenzuordnungen** überschrieben wird. Administratoren können auch bei aktiviertem SSO weiterhin Benutzer einladen und ihnen direkt eine Gruppenmitgliedschaft zuweisen.

**Zusammenfassung:**  

Registrierte Benutzer und ihre Gruppenmitgliedschaft können auf verschiedene Arten verwaltet werden:

- **Verwaltung durch Administratoren:** Ein Administrator in der Avatour-Konsole kann Benutzer anlegen und ihnen Gruppen zuweisen, die ihre Plattformrolle (Gast, Host oder Administrator) definieren.  
- **SSO-Bereitstellung:** Für Kunden der Enterprise- oder Business-Stufe mit aktiviertem SSO kann der IdP automatisch Konten bereitstellen und Gruppenmitgliedschaften zuweisen, die die Plattformrolle des Benutzers definieren.  
- **Vom Host eingeladene Benutzer:** Hosts können andere Benutzer als Editor-Mitarbeiter zu bestimmten Arbeitsbereichen einladen. Die Zuweisung der Editor-Mitarbeiterrolle verbraucht eine Host-Lizenz.

**Empfohlene Vorgehensweise (Enterprise-Kunden):**  
Für Organisationen, die mit einer großen Anzahl von Benutzern rechnen, die Zugriff auf Avatour benötigen, wird empfohlen, **Single Sign-On (SSO)** zu integrieren und Benutzer sowie Gruppenmitgliedschaften über den **IdP** zu verwalten. Dieser Ansatz optimiert die Kontobereitstellung, die Gruppenzuweisung und die Lizenzverwaltung, reduziert den Verwaltungsaufwand und gewährleistet eine einheitliche Zugriffskontrolle.

#### 2.2.1 Gastbenutzer

- Der **Gastgruppe** hinzugefügt.  
- Kann **Assets** in Arbeitsbereichen anzeigen, in denen sie als **Viewer-Mitarbeiter** hinzugefügt wurden.  
- Können keine Arbeitsbereiche erstellen, keine Meetings veranstalten und keine Inhalte hochladen.  
- SSO-bereitgestellte Gastkonten **authentifizieren sich über den IdP**; es ist kein von Avatour verwaltetes Passwort erforderlich.

---

#### 2.2.2 Lizenzierte Benutzer (Zugriff auf die Webkonsole)

##### Host-Benutzer (Gruppe: Host)

- Kann Arbeitsbereiche erstellen/verwalten, Mitarbeiter in einen Arbeitsbereich einladen, **Live-Meetings veranstalten** und **Quick Captures** hochladen.  
- Hat Zugriff auf das **Host-Dashboard** und die **Operator-App** auf unterstützten 360°-Kameras.  

##### Admin-Benutzer (Gruppe: Admin)

- Umfasst alle Host-Funktionen sowie die vollständige Kontoverwaltung.

**Zusätzliche Administratorrechte umfassen:**

**Kontoverwaltung**  

- Neue Benutzer anlegen und ihnen Gruppen zuweisen.
- Passwörter zurücksetzen, wenn die Verwaltung durch Avatour erfolgt (gilt nicht, wenn SSO aktiviert ist). 
- Gastbenutzer zu Hosts hochstufen.  
- Benutzer deaktivieren (Admin-Konten müssen vor dem Löschen zunächst in Host-Konten umgewandelt werden).  
- Übertragen von Assets von einem Host-Benutzer auf einen anderen während der Löschung.

**Einstellungen**  

- Konfigurieren von **unternehmensweiten Sicherheitseinstellungen** für Assets, Arbeitsbereiche und Meetings, die auf der Plattform gehostet werden (z. B. ob ein Host anwesend sein muss, um ein Meeting zu starten, ob Gesichter in allen auf die Plattform hochgeladenen Videos unkenntlich gemacht werden sollen).  
- Aktivieren oder deaktivieren Sie **KI-Funktionen** oder **Aufzeichnungen**.  
- Wenden Sie das Unternehmensbranding einheitlich auf der gesamten Plattform an, wenn eine **benutzerdefinierte Domain** konfiguriert ist.
  

**Assets & Analysen** 
 
- Alle von beliebigen Benutzern in der Organisation hochgeladenen Assets anzeigen.  
- Die Plattformnutzung in der gesamten Organisation überprüfen.

---

#### 2.2.3 Berechtigungen für Workspace-Mitarbeiter

Workspace-Berechtigungen legen fest, was ein Benutzer **innerhalb eines bestimmten Workspaces** tun kann. Diese sind unabhängig von der Gruppenmitgliedschaft auf Plattformebene (Gast, Host, Admin).

- **Mitarbeiter mit Bearbeitungsrechten:** Benutzer mit dieser Berechtigung können:
  - Assets verwalten (hochladen, entfernen, Gesichter unkenntlich machen, Zusammenfassungen erstellen)  
  - Meeting-Einstellungen verwalten (Aufzeichnung aktivieren/deaktivieren, Teilnehmer zulassen oder entfernen)  
  - Live-Meetings planen und veranstalten  
  - Berichte auf Basis vordefinierter Vorlagen erstellen  
  - Mitwirkende zum Arbeitsbereich hinzufügen oder daraus entfernen  

- **Mitwirkender mit Leserechten:** Benutzer mit dieser Berechtigung haben Lesezugriff auf die Assets des Arbeitsbereichs. Sie **können keine Assets ändern, keine Meetings verwalten und keine Mitwirkenden verwalten**, aber sie **können Notizen zu Assets erstellen**. 
  
## 3. Für Teilnehmer an Remote-Besprechungen und Besucher des Arbeitsbereichs {#for-remote-meeting-participants-and-workspace-visitors}

Avatour bietet Nutzern zwei Hauptmöglichkeiten zur Zusammenarbeit:

- **An einem Avatour-Meeting teilnehmen (synchrone Zusammenarbeit):**  
  Möglicherweise erhalten Sie eine **Kalendereinladung** zur Teilnahme an einem Avatour-Meeting. Während des Meetings können die Teilnehmer eine **Live-Besichtigung vor Ort** durchführen oder gemeinsam und synchron Inhalte prüfen.

- **Einen Arbeitsbereich besuchen (asynchrone Zusammenarbeit):**  
  Sie können auch als **Mitarbeiter in einen Arbeitsbereich** eingeladen werden, um Assets **asynchron** (nach Ihrem eigenen Zeitplan) zu prüfen.

### 3.1 So nehmen Sie an einem Avatour-Meeting teil und besuchen einen Avatour-Arbeitsbereich {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Jedes Gerät mit Flachbildschirm und Webbrowser {#any-flat-screen}
Sie können über einen Webbrowser von **jedem Desktop- oder Laptop-Computer, Smartphone oder Tablet** aus an einem Avatour-Meeting teilnehmen.  

##### An einem Avatour-Meeting teilnehmen

> **Hinweis:** Um an einem Avatour-Meeting teilzunehmen, müssen Sie **die Mikrofonberechtigungen erteilen**. Bitte akzeptieren Sie alle Berechtigungsanfragen Ihres Browsers.

1. **Über eine Kalendereinladung (empfohlen):** 
 - In der Regel erhalten Sie eine **Kalendereinladung** mit einem **Direktlink zur Teilnahme** (zum Beispiel: `https://avatour.live/join?s=xxxxx`). 
 - Wenn Sie auf den Link klicken, wird der **5-stellige Meeting-Code** automatisch ausgefüllt und Sie werden zum Meeting weitergeleitet.
   - **Authentifizierung erforderlich:** Einige Besprechungen sind auf registrierte Benutzer beschränkt. In diesem Fall wird in der Einladung darauf hingewiesen, dass Sie sich **anmelden müssen, um auf die Besprechung zuzugreifen**. 
 - **Passwortgeschützte Besprechungen:** Für einige Besprechungen ist möglicherweise ein Passwort erforderlich. In diesem Fall enthält die Einladung das Passwort, das Sie eingeben müssen, um teilzunehmen.

2. **Über den Meeting-Code:** 
 - Wenn der Gastgeber einen **5-stelligen Meeting-Code** separat teilt, gehen Sie zu [https://avatour.live/join](https://avatour.live/join), geben Sie Ihren **Namen** und den **Meeting-Code** ein und nehmen Sie am Meeting teil.  
   - Wenn die Besprechung **passwortgeschützt** ist, geben Sie das vom Gastgeber bereitgestellte Passwort ein. 
 - Wenn für die Besprechung eine **Authentifizierung** erforderlich ist, müssen Sie sich **mit Ihrem Avatour-Konto anmelden**, bevor Sie beitreten.

> **Tipp 1:** Wenn Ihre Kamera oder Ihr Mikrofon nicht funktioniert, wird es möglicherweise von einer anderen Anwendung (z. B. Microsoft Teams oder Zoom) verwendet. Schließen Sie alle Apps, die Ihre Kamera oder Ihr Mikrofon nutzen könnten, verlassen Sie dann das Avatour-Meeting und treten Sie erneut bei.  

> **Tipp 2:** Wenn Sie immer noch nicht am Meeting teilnehmen können, führen Sie diesen Test durch: [https://avatour.live/test](https://avatour.live/test).  
> Der Test kann feststellen, ob Ihre **Unternehmensfirewall oder Ihr Netzwerk** den Zugriff blockiert, und liefert Informationen, die Ihnen als Grundlage für Gespräche mit Ihrem IT-Team dienen.  

> **Tipp 3:** Verwenden Sie **nicht** die Avatour-Apps für iOS oder Android, um an Meetings teilzunehmen. Diese Apps sind nur erforderlich, wenn Sie **ein Live-Meeting von einer Insta360-Kamera streamen**, da diese Kameras die Avatour-360°-Software nicht direkt ausführen können und ein Smartphone zur Unterstützung benötigen.

##### Einen Avatour-Workspace besuchen (ohne an einem Avatour-Meeting teilzunehmen)

Sie können auf folgende Weise auf einen Arbeitsbereich zugreifen:

- **Öffentlicher Arbeitsbereich:**  
  Wenn der Arbeitsbereich öffentlich ist, kann der Link direkt aufgerufen werden – eine Anmeldung ist nicht erforderlich.

- **Eingeschränkter Arbeitsbereich:**  
  Wenn der Arbeitsbereich eingeschränkt ist, müssen Sie als **Mitarbeiter** mit den Berechtigungen **Editor** oder **Betrachter** hinzugefügt werden.

  1. Wenn Sie als Mitwirkender hinzugefügt wurden, erhalten Sie eine **E-Mail-Benachrichtigung** mit einem Link zum Arbeitsbereich.
  2. Klicken Sie auf den Link in der E-Mail, um den Arbeitsbereich zu öffnen. Falls Sie noch nicht angemeldet sind, werden Sie aufgefordert, sich **anzumelden oder die Registrierung abzuschließen**.
  3. Sobald Sie angemeldet sind, öffnet sich der Arbeitsbereich automatisch.

  Alternativ können Sie sich unter [https://avatour.live/login](https://avatour.live/login) anmelden und über Ihre **Liste der Arbeitsbereiche** auf den Arbeitsbereich zugreifen.

#### 3.1.2 VR-Headset {#vr-headset}
Sie können an einem Meeting teilnehmen und einen Arbeitsbereich über eine Reihe kompatibler Meta- und Pico-Headsets besuchen. Gehen Sie dazu wie folgt vor: 

1. Installieren Sie unsere Avatour-App aus Ihrem jeweiligen VR-Store: [So installieren Sie die Avatour VR-App](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Starten Sie unsere App und geben Sie den Meeting-Code ein oder wählen Sie einen Workspace aus, um an einem Meeting teilzunehmen. Weitere Informationen zur Verwendung unserer VR-App finden Sie in unserem Knowledge-Base-Artikel [hier](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Tools für die Zusammenarbeit in Meetings und Arbeitsbereichen {#meeting-tools}

Avatour ermöglicht die Zusammenarbeit in zwei Hauptkontexten:

1. **Meetings (synchron):** Arbeiten Sie in Echtzeit mit anderen Teilnehmern zusammen, beispielsweise bei Live-Standortbesichtigungen oder der gemeinsamen Überprüfung aufgezeichneter Assets.  
2. **Workspaces (asynchron):** Überprüfen Sie Assets und interagieren Sie mit ihnen nach Ihrem eigenen Zeitplan, rund um die Uhr.

Die **Tools für die Zusammenarbeit sind in Meetings und Workspaces weitgehend ähnlich**, wobei es aufgrund des synchronen bzw. asynchronen Kontexts einige Unterschiede gibt.

#### 3.2.1 Aufbau der Benutzeroberfläche

Die Avatour-Benutzeroberfläche gliedert sich in drei Hauptbereiche:

- **Linkes Fenster** – Arbeitsbereichs-Assets und unterstützende Tools  
- **Mittlerer Bildschirm** – Hauptanzeigebereich für Live-Video oder Assets  
- **Rechtes Fenster** – Kontextinformationen, wie Teilnehmer, Meetings oder Chat  

Die meisten Interaktionen werden über das **untere Menü** initiiert.  
Durch Klicken auf eine Menüoption wird ein **Seitenbereich** auf der linken oder rechten Seite des Bildschirms geöffnet, während die **zentrale Arbeitsfläche** der primäre Anzeigebereich bleibt.

---
#### 3.2.2 Beispiel für die Ansicht in einem Meeting

Hier ist ein Beispiel für eine Ansicht in einem Avatour-Meeting:

![Avatour-Meeting-Benutzeroberfläche mit Medienbereich, leerer Arbeitsfläche und Teilnehmerbereich](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Avatour-Meeting mit Medienbereich (links), Arbeitsfläche (Mitte) und Teilnehmerbereich (rechts)*

---

#### 3.2.3 Beispiel für die Arbeitsbereichsansicht

Hier ist ein Beispiel für eine Arbeitsbereichsansicht:

![Avatour-Arbeitsbereich mit Assets-Panel, leerer Leinwand und Meetings-Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Avatour-Arbeitsbereich mit Assets-Panel (links), Leinwand (Mitte) und Meetings-Panel (rechts)*

---

#### 3.2.4 Übersicht über das untere Menü

Das untere Menü bietet Zugriff auf die wichtigsten Steuerelemente und Panels der Benutzeroberfläche:

**Unteres Menü für Meetings**  

![Avatour-Besprechungs-Untermenü](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Avatour-Besprechungs-Untermenü*

- **Assets** – Zeigen Sie Dateien im Arbeitsbereich an, darunter aufgezeichnete Videos, Bilder, Screenshots und PDFs. 
- **Chat** – Senden Sie Nachrichten an alle Meeting-Teilnehmer.  
- **Kamera** – Schalten Sie Ihre Webcam ein oder aus.  
- **Mikrofon** – Schalten Sie Ihr Mikrofon stumm oder heben Sie die Stummschaltung auf.  
- **Präsentieren** – Präsentieren Sie ein Asset, Ihren Desktop oder Ihr Webcam-Bild (siehe Abschnitt „Präsentieren“ weiter unten).  
- **Host-Tools** (nur für Hosts):  
  - **Fokus sperren** – Sperren Sie die Ansicht für alle Teilnehmer.  
  - **Alle stummschalten** – Schalten Sie alle Teilnehmer stumm.  
- **Vollbild aktivieren** – Schalten Sie die Besprechungsregisterkarte auf Vollbild um.  
- **Besprechung verlassen** – Verlassen Sie die Besprechung.  
- **Aufzeichnung starten** – Verwenden Sie diese Schaltfläche, um die Aufzeichnung während einer Besprechung manuell zu starten und zu stoppen. Alternativ können Meetings automatisch aufgezeichnet werden, wenn in den Arbeitsbereichseinstellungen die Option **Aufzeichnung automatisch starten** aktiviert ist. In beiden Fällen werden die Aufzeichnungen in den Arbeitsbereichsressourcen gespeichert.
- **Karte** – Öffnen oder schließen Sie das Kartenfenster für Ressourcen mit GPS-Track. Durch Klicken auf einen Ort springen Sie zu dem genauen Punkt im Video. Die Karte wird während der Videowiedergabe live aktualisiert.
- **Teilnehmer** – Öffnen oder schließen Sie das Teilnehmerfenster.  
- **Besprechungsinfo** – Zeigen Sie den Besprechungscode und den Einladungslink an und greifen Sie auf zugehörige Tutorials zu.  

![Avatour-Besprechungsinfo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Avatour-Besprechungsinfo – Seitenbereich*

- **Einstellungen** – Passen Sie die Sprach-, Audio- und Videoeinstellungen an. Bei Live-360°-Videobesprechungen können Sie mit **Bitrate anzeigen** die Verbindungsstatistiken überwachen.

> Tipp: Senden Sie den Besprechungslink oder fügen Sie ihn einem Kalendereintrag hinzu, um Teilnehmer einzuladen.

---

##### Menü „Präsentieren“

Über die Option **Präsentieren** im unteren Menü des Meetings können Sie Inhalte für alle Teilnehmer freigeben.

- **Kamera** – Geben Sie die Kamera Ihres Smartphones/Tablets frei. Dies kann auch während eines Live-360°-Videomeetings genutzt werden, um eine zweite Ansicht für Nahaufnahmen oder bestimmte Details einzublenden. 
- **Desktop** – Geben Sie Ihren Desktop-Bildschirm für alle Teilnehmer frei.  
- **Asset** – Präsentieren Sie ein Asset aus dem Arbeitsbereich. Durch die Auswahl eines Assets wird die **Asset-Symbolleiste** geöffnet, die Wiedergabesteuerungen und Kollaborationswerkzeuge speziell für das präsentierte Asset bereitstellt.

##### Asset-Symbolleiste (Meeting)

Wenn Sie ein Asset in einem Meeting präsentieren, erscheint die **Asset-Symbolleiste** über der Arbeitsfläche. Hier sind die Werkzeuge und Menüpunkte, die bei der <u>Präsentation eines Assets in einem Meeting</u> verfügbar sind – von links nach rechts erklärt.

![Avatour-Menü bei der Präsentation eines Assets in einem Meeting](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Avatour-Menü bei der Präsentation eines Assets in einem Meeting*


- **Video-Zeitleiste / Fortschrittsbalken** – Zeigt den Videofortschritt mit Notizen und aus dem Audio extrahierten Schlüsselthemen an. Klicken Sie auf eine Notiz oder ein Thema, um zu diesem Moment zu springen und die Notiz zu öffnen. Enthält **Wiedergabe-/Pause-**-Steuerelemente.   
- **Schnappschuss** – Erfassen Sie ein 360°- oder 2D-Bild aus dem Asset.  
- **Spotlight** – Heben Sie während Live-Sitzungen einen bestimmten Bereich für alle Teilnehmer hervor.  
- **Blickwinkel (POV) anzeigen/ausblenden** – Zeigt an, wohin jeder Teilnehmer im 360°-Video blickt.  
- **Notizen** – Erstellen Sie Notizen, die an bestimmte Momente im Asset angeheftet sind. Notizen können kategorisiert (Beobachtung, Problem, Maßnahme, Empfehlung), nach Status verfolgt (Offen → In Bearbeitung → Gelöst) und über direkte Links geteilt werden.  

  ![Avatour-Notiz und Notizfilter](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Avatour-Notiz und Notizfilter*

  - **Sprachbefehl-Notizen** – Dies sind automatisch generierte Platzhalter, wenn die Aufzeichnung Äußerungen wie „Notiz einfügen“, „Notiz machen“ oder „Notiz erstellen“ erkennt. Diese Notizen erscheinen auf der Zeitachse und müssen vom Benutzer **positioniert und fertiggestellt** werden. 

  ![Avatour-Notizen – Durch Sprachbefehl generiert](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Avatour-Notizen – Durch Sprachbefehl generiert*

- **Notizen und Zusammenfassungsfenster** – Öffnet ein Seitenfenster, in dem alle Notizen, Schlüsselthemen und eine Zusammenfassung für das Asset angezeigt werden. Durch Klicken auf einen Eintrag gelangen Sie zu diesem Moment im Video.  

  ![Avatour-Asset-Zusammenfassung](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Avatour-Zusammenfassung bei der Präsentation eines Assets in einer Besprechung*

  ![Avatour-Themen](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Avatour-Themen bei der Präsentation eines Assets in einem Meeting*

  Über das **Seitenpanel** können Sie **einen Asset-Bericht ausdrucken** oder **als TXT- oder CSV-Datei herunterladen**. Berichte können Notizen, KI-generierte Themen und vollständige Transkriptionen enthalten. Sie können vor dem Exportieren auch **auswählen, welche Elemente enthalten sein sollen**.  

  ![Avatour-Asset-Bericht: Druckmenüs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Avatour-Asset-Bericht: Druck- und Download-Menüs* 

 ![Avatour: Auswahl der Elemente für den Asset-Bericht](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Avatour-Asset-Bericht: Menü zur Elementauswahl*

- **Link teilen** – Teilen Sie einen Link zu einer bestimmten Notiz oder Szene im Asset.  
- **Untertitel (CC)** – Zeigen Sie während der Videowiedergabe eine Texttranskription auf dem Bildschirm an.

##### Asset-Symbolleiste (Arbeitsbereich)

Beim Anzeigen eines Assets in einem Arbeitsbereich ist die Symbolleiste ähnlich, jedoch für die individuelle Nutzung optimiert:

![Avatour-Menü bei der Präsentation eines Assets außerhalb eines Meetings, z. B. beim Besuch eines Arbeitsbereichs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Avatour-Menü bei der Präsentation eines Assets in einem Arbeitsbereich*

- **Video-Zeitleiste / Fortschrittsbalken** – Zeigt den Videofortschritt mit Notizen und Schlüsselthemen an, die aus der Audiospur extrahiert wurden. Klicken Sie an einer beliebigen Stelle auf der Zeitleiste, um durch das Video zu scrollen. Klicken Sie auf eine Notiz oder ein Thema, um zu diesem Moment zu springen und die Notiz zu öffnen. Enthält **Wiedergabe-/Pause-**-Steuerelemente.  
- **Snapshot, Notizen, Notizen- und Zusammenfassungsbereich, Link teilen, Untertitel**  
- Nicht verfügbar: **Spotlight, POV** (dafür sind Live-Teilnehmer erforderlich)  
- Zusätzliche Steuerelemente:
  - **10-Sekunden-Schritte** – Vorwärts/rückwärts springen  
  - **Wiedergabegeschwindigkeit** – Geschwindigkeit anpassen (0,5×–2×)  
  - **Video zuschneiden** – Anfang oder Ende des Assets zuschneiden


## 4. Für Host- und Admin-Benutzer – Avatour-Webkonsole {#for-host-and-admin-users-avatour-web-console}

Wenn Sie sich bei Ihrem Avatour-Benutzerkonto anmelden, gelangen Sie zur **Webkonsole**.  

### 4.1 Webkonsole – Übersicht Hauptmenü {#web-console-overview-main-menu}

Auf der linken Seite sehen Sie die folgenden Menüpunkte:

![Avatour Webkonsole – Hauptmenü](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Avatour Webkonsole – Hauptmenü*

- **Arbeitsbereiche** – Organisieren Sie Ihre Inhalte effizient. Jeder Arbeitsbereich enthält **Assets**, **Mitarbeiter**, **Meetings** und **Einstellungen**.  
- **Assets** – Greifen Sie auf alle Ihre Assets (Videos, Bilder, PDFs) zu und verwalten Sie diese. Administratoren können alle Assets des Kontos einsehen, und freigegebene Assets sind für alle Benutzer sichtbar.  
- **Profil** – Verwalten Sie Ihre Sprache und Ihr Passwort.  
- **Analysen** – Verfolgen Sie Sitzungsaktivitäten, die Nutzung von Arbeitsbereichen und ROI-Kennzahlen.  
- **Einstellungen** *(nur für Administratoren)* – Konfigurieren Sie die Standardeinstellungen für Arbeitsbereiche, Meetings und Assets für das gesamte Unternehmen. Administratoren können außerdem das Branding (Logo, Farben, Hintergründe) anpassen.  
- **Konto** *(nur für Administratoren)* – Verwalten Sie registrierte Benutzer und 360°-Kameras.  
- **Geräteanmeldung** – Geben Sie den auf Ihrer 360°-Kamera angezeigten Code ein, um sie mit Ihrem Konto zu koppeln.  
- **Tutorials** – Greifen Sie auf geführte Tutorials zu.  
- **Abmelden** – Melden Sie sich von der Konsole ab.

> Abschnitte wie „Profil“, „Geräteanmeldung“, „Tutorials“ und „Abmelden“ sind selbsterklärend und haben keine detaillierten Unterabschnitte.

---

### 4.2 Webkonsole – Details nach Menüpunkt (mit Bildern) {#web-console-details-by-menu-item}

#### 4.2.1 Arbeitsbereiche

Arbeitsbereiche sind flexible Organisationseinheiten, mit denen Sie Assets, Mitarbeiter und Besprechungen an einem Ort verwalten können. Sie können einen neuen Arbeitsbereich über die Schaltfläche **Neuer Arbeitsbereich** in der oberen rechten Ecke erstellen.

![Avatour-Webkonsole – Hauptmenüpunkt „Arbeitsbereiche“](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour-Webkonsole – Hauptmenüpunkt „Arbeitsbereiche“*

Klicken Sie auf das Glockensymbol, um eine Übersicht über die Aktivitäten im Arbeitsbereich der letzten 7 Tage anzuzeigen.

![Avatour-Webkonsole – Letzte Aktivitäten im Arbeitsbereich](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Letzte Aktivitäten im Arbeitsbereich*

Innerhalb eines Arbeitsbereichs:

![Avatour-Arbeitsbereich mit Assets-Panel, leerer Leinwand und Meetings-Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Arbeitsbereich mit Assets (links), Leinwand (Mitte), Meetings (rechts)*

- **Assets** – Verwalten Sie die diesem Arbeitsbereich zugewiesenen Dateien.  
- **Mitarbeiter** – 
  Steuern Sie den Zugriff auf Arbeitsbereiche durch 
  - **Betrachter** – Kann Assets anzeigen. Durch die Einladung wird bei Bedarf ein Gastbenutzer erstellt.  
  - **Editor** – Vollständige Kontrolle über den Arbeitsbereich, gleiche Rechte wie der Host. Durch die Einladung wird der Benutzer bei Bedarf zum Host hochgestuft.  
> Mehrere Benutzer können gleichzeitig ohne Meeting auf einen Arbeitsbereich zugreifen. Öffentliche Arbeitsbereiche und Zugriffseinstellungen für Meetings bieten alternative Zugriffsmöglichkeiten.  
- **Bericht** – Erstellen Sie einen Bericht anhand einer Checklistenvorlage für ausgewählte Assets des Arbeitsbereichs.  

![Avatour-Arbeitsbereichsbericht und Asset-Auswahl](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Arbeitsbereichsbericht und Asset-Auswahl*

- **Karte** – Zeigt GPS-fähige Asset-Standorte auf einer Karte an.  
- **Meetings** – Organisieren Sie Meetings im Arbeitsbereich.  
- **Einstellungen** – Konfigurieren Sie die Standardeinstellungen für den Arbeitsbereich und Meetings:

![Avatour-Einstellungen – Arbeitsbereichsansicht](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Arbeitsbereichseinstellungen*

**Arbeitsbereichseinstellungen**

- **Berichtsvorlage** – Wählen Sie eine Checklistenvorlage für die KI-Berichterstellung aus.  
- **Benachrichtigungen aktivieren** – Tägliche E-Mail-Zusammenfassungen zu Änderungen des Notizstatus.  

![E-Mail-Benachrichtigungen – Beispiel](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Beispiel für E-Mail-Benachrichtigungen*

- **Öffentlicher Arbeitsbereich** – Jeder, der über den Link verfügt, kann Assets direkt anzeigen.

**Besprechungseinstellungen**
  
* **Authentifizierung erforderlich** – Teilnehmer müssen sich anmelden.  
* **Gastzugang zulassen** – Nicht registrierten Benutzern das Anzeigen von Assets erlauben.  
* **Aufzeichnung automatisch starten / Manuell starten** – Wählen Sie aus, ob Besprechungen automatisch aufgezeichnet oder manuell gestartet werden.  
* **Host erforderlich** – Der Host muss Teilnehmer zulassen; das Meeting endet, wenn der Host das Meeting verlässt.  
* **Zuschauerzugang zulassen** – Ohne Mikrofon oder Kamera teilnehmen; über den Chat kommunizieren.  
* **Passwortgeschützte Meetings** – Für die Teilnahme ist ein Passwort erforderlich.  
* **Frage zu Reiseeinsparungen anzeigen** – Fragen Sie die Teilnehmer, ob das Meeting zu Reiseeinsparungen geführt hat.  

> Einstellungen können kombiniert werden (z. B. kein Gastgeber erforderlich, aber passwortgeschützt).

---

#### 4.2.2 Assets

Verwalten Sie alle 360°-/2D-Videos, Bilder und PDFs. Laden Sie Assets hoch/herunter, weisen Sie sie Arbeitsbereichen zu, teilen Sie sie mit anderen Benutzern, benennen Sie sie um, drucken/laden Sie Berichte herunter, aktivieren Sie die Gesichtsunschärfe und die KI-Zusammenfassung.

![Avatour Webkonsole – Hauptmenüpunkt „Assets“](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Hauptmenüpunkt „Assets“*

---

#### 4.2.3 Analysen

Bietet Einblicke in Meetings, die Nutzung von Arbeitsbereichen und ROI-Kennzahlen.

![Avatour-Webkonsole – Hauptmenüpunkt „Analytics“ (1 von 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Übersicht über Analytics*

![Avatour-Webkonsole – Hauptmenüpunkt „Analytics“ (2 von 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Besprechungsaktivität und Arbeitsbereichsnutzung*

![Avatour Web Console – Hauptmenüpunkt „Analytics“ (3 von 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Nutzung von Gerätelizenzen & ROI* 

## 5. Vor Ort – So verwenden Sie das Avatour-Komplettpaket {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Erste Schritte
[Schnellstartanleitung – Avatour Turnkey Kit 3.1 (Einrichtung des Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Befolgen Sie die Anleitung zum Auspacken, Zusammenbauen und Einschalten Ihrer Kamera.

---

### 5.2 Nützliche Tipps

#### Externer Akku – Längere Live-Meetings & verbesserte Wärmeableitung 

- **Wenn Ihr Kit einen Ulanzi-Akku enthält:** Befestigen Sie ihn zwischen dem Stativfuß und dem ausziehbaren Stab und schließen Sie den Akku dann über USB-C an die Kamera an.  

- **Wenn Ihr Set einen Telesin-Akku-Stick enthält:** Befestigen Sie die Kamera direkt am ausziehbaren Telesin-Akku-Stick und schließen Sie sie über USB-C an.  

Verwendung des externen Akkus:

1. Verlängert die Gesamtlaufzeit von ca. 40 Minuten (nur Kamera-Akku) auf ca. 3 Stunden.  
2. Verleiht dem Kamera-Setup mehr Stabilität.  
3. Hilft, eine mögliche Überhitzung zu verhindern.  

> Wir empfehlen, den externen Akku von Anfang an zu verwenden, insbesondere bei Live-Meetings.

#### Audio-Hinweise für Live-Meetings und Aufzeichnungen

- **Lauter Umgebung:** 
  Verwenden Sie die im Kit enthaltenen Shokz-Kopfhörer für eine klare Audioaufnahme.  
  - **Ein-/Ausschalten:** Halten Sie die Taste „+“ 3 Sekunden lang gedrückt (blaue LED = ein, rote LED = aus).  
  - **Bluetooth-Kopplungsmodus:** Halten Sie bei ausgeschaltetem Headset die Taste „+“ 5 Sekunden lang gedrückt (LED blinkt blau/rot).  
  - **Lautstärke:** Verwenden Sie die Tasten „+“ und „-“.  

- **Leisere Umgebungen / mehrere Teilnehmer in der Nähe der Kamera:** 
  Verwenden Sie den NoxGear-Aufstecklautsprecher. Er bietet zwar nicht die gleiche Klangqualität wie Konferenzlautsprecher (z. B. Jabra Speak), lässt sich aber einfach an Ihrem Hemd befestigen und erfasst Stimmen in der Nähe effektiv.  
  - **Ein-/Ausschalten:** Halten Sie die Wiedergabe-/Pause-Taste 2 Sekunden lang gedrückt.  
  - **Bluetooth-Kopplungsmodus:** Wechselt beim Einschalten automatisch in den Kopplungsmodus (LED blinkt blau/rot; leuchtet blau, wenn gekoppelt).  
  - **Lautstärke:** Verwenden Sie die Tasten „+“ und „-“.  

- **Verwendung Ihres eigenen Geräts:** Wenn Sie eine Alternative bevorzugen (z. B. einen Konferenzlautsprecher oder ein persönliches Headset), können Sie diese über die Kamera koppeln: Einstellungen → Bluetooth.  

#### Konnektivität, Konnektivität, Konnektivität
**Bevor Sie beginnen:** Stellen Sie eine Internetverbindung her über:

- **Lokales WLAN** (bevorzugt)
- **Mobilfunknetz** (außerhalb der WLAN-Reichweite)

**Empfohlene Bandbreite:** 10 Mbit/s Upload/Download für vollständiges 360°-Streaming (~5 Mbit/s). Eine geringere Bandbreite (1–2 Mbit/s) funktioniert nur im Stillstand.

##### Netzwerkgeschwindigkeit testen
- **Test an einem Standort:** Verwenden Sie einen beliebigen Geschwindigkeitsmesser, den Sie normalerweise nutzen (z. B. [Speedtest](https://www.speedtest.net)), um sowohl die Upload- als auch die Download-Bandbreite zu überprüfen.   
- **Test beim Gehen durch den Standort:** Über die Kamera: Einstellungen → Netzwerk → Verbindungstest. Gehen Sie durch den gesamten Raum, um die Abdeckung und Bandbreite zu überprüfen.

##### Lokales WLAN
- Für stabile Verbindungen sehr zu empfehlen.  
- Falls die IT-Abteilung eine Whitelist erfordert, finden Sie die MAC-Adresse unter: Einstellungen → Info → WLAN-Adresse.

##### Mobilfunknetz
**Option A: Im Kit enthaltener Hotspot & SIM-Karte**  

- Befestigen Sie den GlocalMe-Hotspot am Telesin-Akku-Stick (Magnet).  
- Stellt sicher, dass keine Störungen auftreten, und hält die Verbindung aufrecht, wenn Sie sich von der Kamera entfernen.  
- Fehlerbehebung:
  - Vergewissern Sie sich, dass die vorinstallierte SIM-Karte (nicht die Cloud-SIM) verwendet wird.  
  - Aktivieren Sie 5G im SIM-Karten-Manager.  
  - Überprüfen Sie den korrekten APN für Ihre Region ([APN-Einrichtungsanleitung](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B: Persönlicher Hotspot / SIM-Karte**
- Verwenden Sie Ihr eigenes Smartphone oder einen dedizierten Hotspot.  

**Wichtiger Hinweis:**  
> Lassen Sie den Hotspot ausgeschaltet, solange eine WLAN-Verbindung besteht; aktivieren Sie ihn nur, wenn Sie sich außerhalb der Reichweite befinden. Das Betriebssystem der Kamera wechselt je nach Signalstärke dynamisch zwischen WLAN-Netzwerken und wechselt möglicherweise versehentlich zum Hotspot, selbst wenn WLAN verfügbar ist.

> Mobilfunknetze können die Bandbreite unerwartet drosseln. Erkundigen Sie sich bei Ihrem Mobilfunkanbieter nach den Datenvolumen-Limits oder wenden Sie sich an den Avatour-Support, wenn Sie unseren Hotspot und unsere SIM-Karte nutzen.

##### Situationen mit geringer Bandbreite
- Nehmen Sie Standortvideos vorab auf, um sie später abzuspielen ([Aufnahmeanleitung](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Teilen Sie den Stream einer Smartphone-Kamera, um Bereiche mit geringer Bandbreite (0,1–0,3 Mbit/s Upload) zu ergänzen.

##### Keine Verbindung
- Es können nur vorab aufgezeichnete Videos verwendet werden ([Aufnahmeanleitung](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Weitere Teilnehmer vor Ort – Bewährte Vorgehensweisen

Wenn mehrere Teilnehmer von demselben Standort wie die 360°-Kamera aus an einem Live-Avatour-Meeting teilnehmen, ist ein sorgfältiges Management von **Audio und Bandbreite** entscheidend:  

- Jedes vor Ort verbundene Smartphone, Tablet oder Laptop beansprucht Netzwerkbandbreite und kann die Übertragung der 360°-Kamera beeinträchtigen.  
- Mehrere Mikrofone und Lautsprecher im selben Raum können **Audio-Rückkopplungen** verursachen, was das Meeting-Erlebnis für alle Teilnehmer unangenehm macht.

#### Weitere Teilnehmer vor Ort – Best Practices

Wenn mehrere Teilnehmer von demselben Standort wie die 360°-Kamera aus an einem Live-Avatour-Meeting teilnehmen, ist eine sorgfältige Verwaltung von **Audio und Bandbreite** entscheidend:  

- Jedes vor Ort verbundene Smartphone, Tablet oder Laptop beansprucht Netzwerkbandbreite und kann die Übertragung der 360°-Kamera beeinträchtigen.  
- Mehrere Mikrofone und Lautsprecher im selben Raum können **Audio-Rückkopplungen** verursachen, was das Meeting-Erlebnis für alle Teilnehmer unangenehm macht.

Befolgen Sie zur Bewältigung dieser Herausforderungen die folgenden **Best Practices**:

- **Verwenden Sie kabelgebundene oder kabellose Kopfhörer:** Vorzugsweise mit Geräuschunterdrückung, um Echo und Rückkopplungen zu vermeiden.  
- **Vor-Ort-Modus:** Nehmen Sie im Vor-Ort-Modus am Meeting teil, wenn Sie sich physisch in der Nähe der 360°-Kamera befinden.  
  - Dieser Modus ist für die Nutzung vor Ort optimiert: 
 - Schaltet das Mikrofon und den Lautsprecher des Teilnehmers standardmäßig stumm. 
 - Sendet **nicht** das Kamerabild des Teilnehmers. 
 - Zeigt **nicht** das Bild der 360°-Kamera im Browser des Teilnehmers an.  
    - Schont die Netzwerkbandbreite und stellt sicher, dass der 360°-Kamera die maximal verfügbare Upload-Bandbreite für den Live-Stream zur Verfügung steht. 
 - Nützlich, wenn ein Benutzer bestimmte Details teilen möchte; Sie **können Ihr Kamerabild zurücksenden**, um gezielte Ansichten zu ermöglichen.  
- **Stummschalten, wenn Sie nicht aktiv sprechen:** Verhindert unerwünschte akustische Rückkopplungen und Ablenkungen.  
- **Verwenden Sie nach Möglichkeit ein separates Netzwerk:** Verbinden Sie Ihr Smartphone mit einem anderen Netzwerk als dem der Kamera, um Interferenzen zu reduzieren.  

Die Befolgung dieser Richtlinien gewährleistet eine reibungslose, qualitativ hochwertige Live-Tour sowohl für Teilnehmer vor Ort als auch für Remote-Teilnehmer.

### 5.3 Avatour-Kamera-App

Hier sind (1) das Hauptmenü, (2) die Einstellungen und (3) das Netzwerk-Einstellungsmenü.

![Avatour 360°-Kamera-App – Drei Menüs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360°-Kamera-App – 3 Menüs*

**Schnellaufnahme** – Für die Offline-Aufnahme von 360°-Videos. – Eine detaillierte Beschreibung finden Sie unter [Wie nimmt man 360°-Videos mit der Avatour-App auf und lädt sie hoch?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Wir empfehlen die Verwendung eines externen Audiogeräts (verbunden über Bluetooth). Hinweis: Sie können auch normale 2D-Videos und -Bilder aufnehmen – wechseln Sie dazu einfach im QC-Bildschirm in der unteren rechten Ecke zwischen dem 360°- und dem 2D-Modus.

**Live-Meeting** – Für Live-360°-Videokonferenzen. Sie sehen Ihre Arbeitsbereiche; wenn Sie auf einen davon klicken, wird der Live-Videostream von der 360°-Kamera gestartet. Bevor Sie mit Ihrer 360°-Kamera an der Besprechung teilnehmen können, müssen Sie ein Audiogerät über Bluetooth verbinden. Eine detaillierte Beschreibung finden Sie unter [Wie starte ich eine Live-Capture-Besprechung mit Ihrer Pilot-Kamera?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Wenn Sie ein Live-Capture-Meeting mit Ihrer 360°-Kamera veranstalten, stehen Ihnen ähnliche Meeting-Tools zur Verfügung, die das Web-Erlebnis widerspiegeln. Hier ist ein Link zu unserem Knowledge-Base-Artikel, der diese Tools näher erläutert: [Operator-App-Tools](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galerie** – Hier finden Sie alle Ihre 360°-Videos und -Bilder zum Hochladen in die Avatour-Webkonsole.

**Einstellungen** – In den Einstellungen stehen Ihnen folgende Optionen zur Verfügung:

- **Netzwerk**: Mit dieser Option können Sie das WLAN-Netzwerk ändern, mit dem die Kamera verbunden ist, oder einen Netzwerkverbindungstest durchführen, um Ihren Streaming-Durchsatz anzuzeigen
- **Live-Aufnahme**: Passen Sie Ihre Live-Aufnahme-Einstellungen je nach verfügbarer Bandbreite, der VR-Empfindlichkeit des Gastes oder dem Vorhandensein von Schutzgläsern an Ihrer Kamera an:
  - **Ziel-Bildrate**: Stellen Sie die Bildrate für Ihr Live-Aufnahme-Video zwischen 15 fps, 24 fps und 30 fps ein. Höhere Bildraten sorgen für ein flüssigeres Video, erfordern jedoch mehr Upload-Bandbreite. Standard: 15 fps
  - **Zielbitrate**: Ermöglicht es Ihnen, die maximale Streaming-Bitrate für Ihre Live-Aufnahme zu erhöhen oder zu verringern. Sie können Ihre Zielbitrate zwischen 1 Mbit/s und 10 Mbit/s einstellen. Höhere Bitraten führen zu einer höheren Videoauflösung, erfordern jedoch mehr Upload-Bandbreite. Standard: 5 Mbit/s
  - **Bewegung optimieren**: Dies verringert die Videobildrate, wodurch die Upload-Bandbreite Ihres Netzwerks weniger belastet wird, und erhöht Ihre Streaming-Bitrate. Darüber hinaus hilft diese Option, die Bewegungsübelkeit bei VR-Teilnehmern zu reduzieren. Standard: Aus
  - **Schutzlinsen**: Dies beeinflusst, wie das 360°-Video zusammengefügt wird, je nachdem, ob Schutzlinsen an Ihrer Kamera installiert wurden. Wenn Sie keine Schutzlinsen haben, setzen Sie diese Option auf „Nein“. Wenn Sie ein Kit 3.0 erhalten haben, sind Schutzlinsen bereits vorinstalliert und Sie sollten diese Option auf „Ja“ setzen. Standard: Ja

- **Schnellaufnahme**: Passen Sie Ihre Schnellaufnahme-Einstellungen an Ihre bevorzugte Videobildrate, die verfügbare Bandbreite für das Hochladen von aufgezeichneten Videos oder daran an, ob die Schutzgläser Ihrer Kamera installiert sind. Die Schnellaufnahme hat eine festgelegte Auflösung von 4k, was in der Regel ein gutes Gleichgewicht zwischen Videoqualität und Dateigröße bietet. (Für höhere Auflösungen können Sie die nativen Kamera-Apps verwenden, auch auf der PanoX V2; Details finden Sie unter [Wie nimmt man 360°-Videos mit der Avatour-App auf und lädt sie hoch?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Zielbildrate**: Passen Sie die Bildrate für Ihre Quick Capture-Videoaufnahmen zwischen 15 fps, 24 fps und 30 fps an. Höhere Bildraten sorgen für flüssigere Videos, erhöhen jedoch die Dateigröße und die Upload-Dauer. Empfohlen: 30 fps
  - **Zielbitrate**: Stellen Sie die Zielbitrate für Quick Capture-Uploads zwischen 5 Mbit/s und 20 Mbit/s ein. Niedrigere Bitraten erhöhen die Upload-Geschwindigkeit, verringern jedoch die Videoqualität. Empfohlen: 20 Mbit/s
  - **Schutzgläser**: *Siehe Abschnitt „Schutzgläser“ für Live Capture oben*

  > Weitere Hinweise zu den oben genannten Einstellungen und Videodateigrößen finden Sie in unserem [Avatour 360°-Videodateigrößenrechner](https://avatour.com/file-size-calculator).

- **Über**: Zeigt die Seriennummer des Geräts und die Softwareversion an


**Konto** – Zum Anmelden mit Ihrem Avatour-Host- oder Admin-Konto.

## 6. Empfehlungen für bewährte Verfahren {#best-practice-advice}

### 6.1 Erste (informelle) Schritte und Einarbeitung

Für Ihre ersten Schritte und zum Kennenlernen der Avatour-Webkonsole und des Avatour-Turnkey-Kits empfehlen wir folgende Vorgehensweise:

1. Nehmen Sie das Kit mit nach Hause und probieren Sie es gemeinsam mit Familie und Freunden über Ihre private Internetverbindung aus.
2. Nehmen Sie das Kit mit ins Büro und verbinden Sie es mit dem Unternehmensnetzwerk (es können unternehmensspezifische Probleme auftreten, z. B. Unternehmensfirewalls – aber Sie wissen bereits aus Schritt 1, dass Avatour funktioniert, und dies ist ein Thema, das Ihr IT-Team mit Hilfe von Avatour klären kann).
3. Beginnen Sie, Avatour vor Ort (außerhalb Ihres Büros) an dem Treffpunkt zu nutzen, zu dem Remote-Teilnehmer normalerweise anreisen müssten. Es könnten weitere Verbindungsprobleme auftreten. Avatour hilft Ihnen dabei in Zusammenarbeit mit Ihrem IT-Team.
4. Beginnen Sie mit der Nutzung mit internen und externen Remote-Teilnehmern.

### 6.2 Vor einem 360°-Video-Live-Meeting

- Wir empfehlen, vor jeder Live-Tour eine aufgezeichnete 360°-Videotour durchzuführen, sofern es die Zeit erlaubt, und zwar aus drei Gründen: (1) Sie haben eine Ausweichlösung für die Live-Tour, (2) Sie verfügen über Material zur Dokumentation und späteren Nachbereitung (zusätzlich zur aufgezeichneten Live-Tour) und (3) Sie beginnen damit, eine Bibliothek mit 360°-Videos all Ihrer Standorte aufzubauen, die für viele Anwendungsfälle hilfreich sein kann. 
- Laden Sie alle Komponenten des Sets mindestens 90 Minuten vor dem Live-Meeting auf. Wir empfehlen ohnehin, alle Geräte kontinuierlich aufzuladen, wenn sie nicht in Gebrauch sind. So sind alle Geräte immer einsatzbereit, auch für ungeplante Ad-hoc-Meetings.
- Stellen Sie das Set vollständig zusammen (1. Stativfuß + 2. Ulanzi-Akku + 3. ausziehbarer Stab + 4. 360°-Kamera).

- Vergewissern Sie sich, dass ein Workspace für die Durchführung eines Live-Meetings erstellt wurde und alle relevanten Assets enthält.

- Laden Sie alle Teilnehmer über Ihren Workspace zum Meeting ein. Dadurch wird in den Kalendern aller Teilnehmer eine Einladung erstellt, die den Link zur Meeting-Einladung enthält.

- Koppeln und verbinden Sie Ihre Bluetooth-Kopfhörer oder den Lautsprecher, den Sie für Ihre Tour verwenden möchten, mit der Kamera.

- Alle Smartphone-Nutzer vor Ort sollten sich über ein anderes Netzwerk als das der Kamera verbinden. Dies reduziert die Belastung der Netzwerkbandbreite der Kamera.

- Wenn Sie als Kameramann allein sind, nehmen Sie ein Smartphone mit, falls Sie die Smartphone-Kamera teilen und feine Details zeigen möchten.

- Vergewissern Sie sich, dass die 360°-Kamera eine Verbindung zu Ihrem lokalen WLAN herstellen kann.

- Planen Sie vor einem Avatour-Meeting die Route, die Sie durch die Einrichtung nehmen werden. Führen Sie ein Test-Avatour-Meeting mit der Kamera durch und überprüfen Sie, ob alle Bereiche eine Bandbreite von über 1 Mbit/s aufweisen. Dies können Sie auf dem Kamerabildschirm selbst sehen oder als Remote-Teilnehmer, indem Sie zu „Einstellungen“ gehen und „Bitrate anzeigen“ aktivieren.

- Wenn Sie feststellen, dass einige Bereiche nur wenig oder gar keine Bandbreite haben, ist es am besten, Bilder oder eine Aufzeichnung zu machen. Diese können dann während des Meetings den Remote-Teilnehmern zur Ansicht präsentiert werden. Sie können der Anleitung hier folgen, die unsere „Quick Capture“-Funktion zum Aufnehmen und Hochladen von Videos/Bildern erklärt: [Wie nimmt man 360°-Videos mit der Avatour-App auf und lädt sie hoch?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Wenn Remote-Teilnehmer an der Besprechung teilnehmen, die Avatour noch nicht zuvor genutzt haben, geben Sie ihnen eine kurze Übersicht über die Plattform, ihre Funktionen (360°-Live-Video, Assets, Schnappschüsse, Anmerkungen, Spotlight) und die Besprechungstools.

- Sie können in einer anderen Videokonferenzlösung (z. B. Teams, Zoom, Google Meet) beginnen, aber bevor Sie zu Avatour wechseln, schließen Sie die andere Videokonferenzanwendung vollständig. In einigen Fällen priorisieren diese anderen Anwendungen das Mikrofon, die Lautsprecher oder die Webcam Ihres Geräts, wodurch diese für Avatour deaktiviert werden. Führen Sie außerdem NICHT Avatour UND eine andere Videokonferenz gleichzeitig aus, da dies die verfügbare Bandbreite verringert.

- Wenn Sie die 360°-Kamera in einer Umgebung mit hohen Temperaturen einsetzen möchten, wird die Verwendung des Kühlmoduls empfohlen (nur Pilot Pano). Dies verringert das Risiko, dass die Kamera überhitzt und sich automatisch abschaltet.

### 6.3 Bei der Bedienung der Kamera vor Ort für ein 360°-Video-Live-Meeting

- Achten Sie beim Bedienen der Kamera darauf, **langsam zu gehen** und **häufig anzuhalten, um die Kamera auf ihrem Stativ abzustellen**. Dies trägt dazu bei, (1) die Videoqualität zu verbessern, da Sie weniger Videodaten erzeugen, wenn Sie die Kamera nicht unnötig bewegen, und (2) mögliche Videoausfälle zu reduzieren, wenn die Netzwerkverbindung der Kamera zwischen WLAN-Zugangspunkten wechselt.

- Halten Sie die Kamera vor sich und über Augenhöhe. So können alle Remote-Teilnehmer den Großteil Ihrer Umgebung sehen.

- Wenn die Kamera stabil stehen muss, verwenden Sie das Stativ und stellen Sie die Kamera auf die richtige Höhe ein, am besten auf Augenhöhe.

- Verbinden Sie die Kamera nach Möglichkeit immer mit Ihrem lokalen WLAN-Netzwerk. In Bereichen ohne WLAN-Zugang nutzen Sie den mitgelieferten Hotspot. Der Hotspot verfügt über eine SIM-Karte, die eine Verbindung zu einem zuverlässigen Mobilfunknetz in Ihrer Nähe herstellt. Schalten Sie den Hotspot immer aus, wenn er in Innenräumen nicht genutzt wird, da sich die 360°-Kamera sonst mit dem Hotspot verbinden könnte, was in Innenräumen nicht erwünscht ist. Halten Sie den Hotspot im Freien in der Nähe der 360°-Kamera.

- Wenn die Bitrate der Kamera unter 2 Mbit/s fällt, gehen Sie langsamer oder bleiben Sie ganz stehen, bis sich das Signal wieder stabilisiert hat. Dies geschieht in der Regel, wenn Sie von einem WLAN-Zugangspunkt zu einem anderen wechseln. 

- Wenn Sie wissen, dass die Verbindung und die Videoqualität beim Wechsel zu einem bestimmten Ort abfallen (Beispiel: Wechsel von einem Produktionsbereich in Innenräumen zu einem Außenbereich), informieren Sie die Remote-Teilnehmer im Voraus.

- Wenn Sie etwas sehr detailliert oder mit kleiner Schrift zeigen müssen, nutzen Sie Ihr eigenes Smartphone oder das eines Teilnehmers vor Ort, um an der Besprechung teilzunehmen, und zeigen Sie die (Rück-)Kamera Ihres/dessen Telefons.

- Wenn möglich, empfehlen wir, dass eine weitere Person vor Ort ist, um bei der oben beschriebenen Smartphone-Kamerafreigabe zu helfen, da sich dies oft als hilfreich oder notwendig erweist.

- Idealerweise sollten Smartphone-Nutzer vor Ort (1) im Vor-Ort-Modus und (2) über ein anderes Netzwerk als das der Kamera am Meeting teilnehmen, um der 360°-Kamera keine wichtige Upload-Bandbreite wegzunehmen.

- Alle Teilnehmer vor Ort, die über ihr Smartphone am Meeting teilnehmen, sollten stummgeschaltet sein, sofern sie nicht gerade aktiv sprechen.
