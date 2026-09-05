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
Benutzer können an der Besprechung teilnehmen, ohne sich für ein Avatour-Konto zu registrieren. Ausnahme: Wenn der Gastgeber die Besprechungseinstellung „Authentifizierung erforderlich“ aktiviert hat (siehe auch 4.2.1 Einstellungen für Arbeitsbereiche und Besprechungen) – beispielsweise, um nur internen Mitarbeitern die Teilnahme über Single Sign-On (SSO) zu ermöglichen –, wird in der Kalendereinladung darauf hingewiesen, dass sich die Teilnehmer zur Authentifizierung anmelden müssen.

Benutzer nehmen wie folgt an der Besprechung teil:

- Sie erhalten vom Gastgeber einen Besprechungslink.
- Sie geben ein Besprechungskennwort ein, falls der Gastgeber eines aktiviert hat.
- Teilnehmer können ohne Avatour-Konto teilnehmen, es sei denn, die Besprechung ist eingeschränkt und erfordert eine Anmeldung zur Authentifizierung.

#### 2.1.1 Teilnehmer 

- Kann teilnehmen und uneingeschränkt interagieren (Webcam, Mikrofon, Chat und Präsentationsfunktionen).
- Maximal 20 interaktive Teilnehmer pro Besprechung.

#### 2.1.2 Zuschauer

- Kann die Besprechung verfolgen und ausschließlich über den Chat teilnehmen.
- Kann kein Video teilen, kein Mikrofon verwenden, keine Präsentationen halten, keine Assets abspielen/anhalten und keine Schnappschüsse aufnehmen.
- Maximal 10 Zuschauer pro Meeting.
- Zusammen mit den Teilnehmern kann ein Meeting bis zu 30 Teilnehmer umfassen.

### 2.2 Registrierte Nutzer

Registrierte Nutzer verfügen über ein Avatour-Konto. Konten werden auf eine der folgenden Weisen erstellt:

- **Vom Administrator eingeladen:** Während des Onboardings richtet Avatour einen **dedizierten Tenant** für die Organisation ein und erstellt ein oder mehrere **Administratorkonten**. Administratoren können dann **Nutzer** innerhalb der Organisation **einladen** und ihnen **Gruppen** zuweisen, die ihre Rolle auf der Plattform definieren (Gast, Gastgeber oder Administrator). Eingeladene Nutzer erhalten einen **Anmeldelink**, über den sie die Kontoeinrichtung abschließen und ein Passwort festlegen können.  
- **Vom Gastgeber eingeladen:** Hosts können Benutzer als **Mitarbeiter mit Bearbeitungsrechten** zu einem Arbeitsbereich hinzufügen. Dies verbraucht eine **Host-Lizenz** und stellt sicher, dass der Benutzer Zugriff auf Host-Ebene hat.  
- **Automatische SSO-Bereitstellung (nur Enterprise-/Business-Stufe):** Konten können automatisch vom Identitätsanbieter (IdP) angelegt werden. Standardmäßig werden über SSO bereitgestellte Konten der **Gästegruppe** hinzugefügt, sofern dies nicht über **SAML-Gruppenzuordnungen** überschrieben wird. Administratoren können auch bei aktiviertem SSO weiterhin Nutzer einladen und ihnen direkt eine Gruppenmitgliedschaft zuweisen.

**Zusammenfassung:**  

Registrierte Nutzer und ihre Gruppenzugehörigkeit können auf verschiedene Arten verwaltet werden:

- **Verwaltung durch Administratoren:** Ein Administrator in der Avatour-Konsole kann Nutzer anlegen und ihnen Gruppen zuweisen, die ihre Rolle auf der Plattform definieren (Gast, Host oder Administrator).  
- **SSO-Bereitstellung:** Für Kunden der Enterprise- oder Business-Stufe mit aktiviertem SSO kann der IdP automatisch Konten bereitstellen und Gruppenmitgliedschaften zuweisen, die die Plattformrolle des Benutzers definieren.  
- **Von Hosts eingeladene Benutzer:** Hosts können andere Benutzer als „Editor“-Mitarbeiter zu bestimmten Arbeitsbereichen einladen. Die Zuweisung der Rolle „Editor“-Mitarbeiter verbraucht eine Host-Lizenz.

**Empfohlene Vorgehensweise (Enterprise-Kunden):**  
Für Organisationen, die mit einer großen Anzahl von Benutzern rechnen, die Zugriff auf Avatour benötigen, wird empfohlen, **Single Sign-On (SSO) zu integrieren** und Benutzer sowie Gruppenmitgliedschaften über den **IdP** zu verwalten. Dieser Ansatz optimiert die Kontoeinrichtung, die Gruppenzuweisung und die Lizenzverwaltung, reduziert den Verwaltungsaufwand und gewährleistet eine einheitliche Zugriffskontrolle.

#### 2.2.1 Gastbenutzer

- Werden der **Gastgruppe** hinzugefügt.  
- Können **Assets** in Arbeitsbereichen **anzeigen**, in denen sie als **Mitwirkende mit Betrachterrechten** hinzugefügt wurden.  
- Können keine Arbeitsbereiche erstellen, keine Besprechungen veranstalten und keine Inhalte hochladen.  
- Über SSO bereitgestellte Gastkonten **authentifizieren sich über den IdP**; ein von Avatour verwaltetes Passwort ist nicht erforderlich.

---

#### 2.2.2 Lizenzierte Benutzer (Zugriff auf die Webkonsole)

##### Host-Benutzer (Gruppe: Host)

- Können Arbeitsbereiche erstellen/verwalten, Mitwirkende in einen Arbeitsbereich einladen, **Live-Meetings veranstalten** und **Schnellaufnahmen** hochladen.  
- Haben Zugriff auf das **Host-Dashboard** und die **Operator-App** auf unterstützten 360°-Kameras.  

##### Admin-Benutzer (Gruppe: Admin)

- Umfassen alle Host-Funktionen sowie die vollständige Kontoverwaltung.

**Zu den zusätzlichen Admin-Rechten gehören:**

**Kontoverwaltung**  

- Neue Benutzer anlegen und diesen Gruppen zuweisen.
- Passwörter zurücksetzen, wenn die Verwaltung durch Avatour erfolgt (gilt nicht, wenn SSO aktiviert ist). 
- Gastbenutzer auf Host hochstufen.  
- Benutzer deaktivieren (Admin-Konten müssen vor dem Löschen zunächst in Host-Konten umgewandelt werden).  
- Assets beim Löschen von einem Host-Benutzer auf einen anderen übertragen.

**Einstellungen**  

- Konfigurieren Sie **unternehmensweite Sicherheitseinstellungen** für Assets, Arbeitsbereiche und Meetings, die auf der Plattform gehostet werden (z. B. ob ein Host anwesend sein muss, um ein Meeting zu starten, oder ob Gesichter in allen auf die Plattform hochgeladenen Videos unkenntlich gemacht werden sollen).  
- **KI-Funktionen** oder **Aufzeichnung** aktivieren oder deaktivieren.  
- Das Unternehmensbranding plattformweit einheitlich anwenden, wenn eine **benutzerdefinierte Domain** konfiguriert ist.
  

**Assets & Analysen** 
 
- Alle von beliebigen Benutzern in der Organisation hochgeladenen Assets anzeigen.  
- Überprüfen Sie die Plattformnutzung in der gesamten Organisation.

---

#### 2.2.3 Berechtigungen für Arbeitsbereich-Mitarbeiter

Arbeitsbereichsberechtigungen legen fest, was ein Benutzer **innerhalb eines bestimmten Arbeitsbereichs** tun darf. Diese sind unabhängig von der Gruppenmitgliedschaft auf Plattformebene (Gast, Gastgeber, Administrator).

- **Mitarbeiter mit Bearbeitungsrechten:** Benutzer mit dieser Berechtigung können:
  - Assets verwalten (hochladen, entfernen, Gesichter unkenntlich machen, Zusammenfassungen erstellen)  
  - Meeting-Einstellungen verwalten (Aufzeichnung aktivieren/deaktivieren, Teilnehmer zulassen oder entfernen)  
  - Live-Meetings planen und leiten  
  - Berichte auf Basis vordefinierter Vorlagen erstellen  
  - Mitwirkende zum Workspace hinzufügen oder daraus entfernen  

- **Mitwirkender mit Leserechten:** Benutzer mit dieser Berechtigung haben Lesezugriff auf die Assets des Arbeitsbereichs. Sie **können weder Assets bearbeiten noch Besprechungen oder Mitwirkende verwalten**, aber sie **können Notizen zu Assets erstellen**. 
  
## 3. Für Teilnehmer an Remote-Besprechungen und Besucher des Arbeitsbereichs {#for-remote-meeting-participants-and-workspace-visitors}

Avatour bietet Nutzern zwei Hauptmöglichkeiten zur Zusammenarbeit:

- **An einem Avatour-Meeting teilnehmen (synchrone Zusammenarbeit):**  
  Möglicherweise erhalten Sie eine **Kalendereinladung** zur Teilnahme an einem Avatour-Meeting. Während des Meetings können die Teilnehmer eine **Live-Besichtigung vor Ort** durchführen oder Assets gemeinsam synchron begutachten.

- **Einen Arbeitsbereich besuchen (asynchrone Zusammenarbeit):**  
  Möglicherweise werden Sie auch als **Mitarbeiter zu einem Arbeitsbereich** eingeladen, um Objekte **asynchron** (nach Ihrem eigenen Zeitplan) zu begutachten.

### 3.1 So nehmen Sie an einem Avatour-Meeting teil und besuchen einen Avatour-Arbeitsbereich {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Jedes Gerät mit „Flachbildschirm“ und Webbrowser {#any-flat-screen}
Sie können über einen Webbrowser von **jedem Desktop- oder Laptop-Computer, Smartphone oder Tablet** aus an einem Avatour-Meeting teilnehmen.  

##### An einem Avatour-Meeting teilnehmen

> **Hinweis:** Um an einem Avatour-Meeting teilzunehmen, müssen Sie **die Mikrofonberechtigungen erteilen**. Bitte akzeptieren Sie alle Berechtigungsabfragen Ihres Browsers.

1. **Über eine Kalendereinladung (empfohlen):** 
 - In der Regel erhalten Sie eine **Kalendereinladung** mit einem **Direktlink zur Teilnahme** (zum Beispiel: `https://avatour.live/join?s=xxxxx`).  
   - Wenn Sie auf den Link klicken, wird der **5-stellige Meeting-Code** automatisch ausgefüllt und Sie werden zum Meeting weitergeleitet.
   - **Authentifizierung erforderlich:** Einige Meetings sind auf registrierte Nutzer beschränkt. In diesem Fall wird in der Einladung darauf hingewiesen, dass Sie sich **anmelden müssen, um an der Besprechung teilzunehmen**. 
 - **Passwortgeschützte Besprechungen:** Für manche Besprechungen ist möglicherweise ein Passwort erforderlich. In diesem Fall enthält die Einladung das Passwort, das Sie eingeben müssen, um teilzunehmen.

2. **Über den Besprechungscode:** 
 - Wenn der Gastgeber einen **5-stelligen Besprechungscode** separat weitergibt, rufen Sie [https://avatour.live/join](https://avatour.live/join) auf, geben Sie Ihren **Namen** und den **Besprechungscode** ein und nehmen Sie an der Besprechung teil.  
   - Wenn die Besprechung **passwortgeschützt** ist, geben Sie das vom Gastgeber bereitgestellte Passwort ein. 
 - Wenn für die Besprechung eine **Authentifizierung** erforderlich ist, müssen Sie sich vor der Teilnahme **mit Ihrem Avatour-Konto anmelden**.

> **Tipp 1:** Wenn Ihre Kamera oder Ihr Mikrofon nicht funktioniert, werden diese möglicherweise von einer anderen Anwendung (z. B. Microsoft Teams oder Zoom) verwendet. Schließen Sie alle Apps, die möglicherweise Ihre Kamera oder Ihr Mikrofon nutzen, und verlassen Sie das Avatour-Meeting, um anschließend erneut beizutreten.  

> **Tipp 2:** Wenn Sie dem Meeting immer noch nicht beitreten können, führen Sie diesen Test durch: [https://avatour.live/test](https://avatour.live/test).  
> Der Test kann feststellen, ob Ihre **Unternehmensfirewall oder Ihr Netzwerk** den Zugriff blockiert, und liefert Informationen, die Ihnen als Grundlage für Gespräche mit Ihrem IT-Team dienen.  

> **Tipp 3:** Verwenden Sie **nicht** die Avatour-Apps für iOS oder Android, um an Meetings teilzunehmen. Diese Apps werden nur benötigt, wenn **ein Live-Meeting von einer Insta360-Kamera gestreamt wird**, da diese Kameras die Avatour-360°-Software nicht direkt ausführen können und ein Smartphone zur Unterstützung benötigen.

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
Sie können mit einer Reihe kompatibler Meta- und Pico-Headsets an einem Meeting teilnehmen und einen Workspace besuchen. Gehen Sie dazu wie folgt vor: 

1. Installieren Sie unsere Avatour-App aus Ihrem jeweiligen VR-Store: [So installieren Sie die Avatour-VR-App](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Starten Sie unsere App und geben Sie den Besprechungscode ein oder wählen Sie einen Arbeitsbereich aus, um an einer Besprechung teilzunehmen. Weitere Informationen zur Nutzung unserer VR-App finden Sie in unserem Knowledge-Base-Artikel [hier](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Tools für die Zusammenarbeit in Meetings und Workspaces {#meeting-tools}

Avatour ermöglicht die Zusammenarbeit in zwei Hauptkontexten:

1. **Meetings (synchron):** Arbeiten Sie in Echtzeit mit anderen Teilnehmern zusammen, beispielsweise bei Live-Besichtigungen vor Ort oder beim gemeinsamen Betrachten aufgezeichneter Inhalte.  
2. **Arbeitsbereiche (asynchron):** Betrachten und bearbeiten Sie Inhalte nach Ihrem eigenen Zeitplan, rund um die Uhr.

Die **Tools zur Zusammenarbeit sind in Meetings und Arbeitsbereichen weitgehend ähnlich**, wobei es aufgrund des synchronen bzw. asynchronen Kontexts einige Unterschiede gibt.

#### 3.2.1 Aufbau der Benutzeroberfläche

Die Avatour-Benutzeroberfläche gliedert sich in drei Hauptbereiche:

- **Linkes Fenster** – Arbeitsbereich-Objekte und unterstützende Tools  
- **Mittlerer Bildschirmbereich** – Hauptanzeigebereich für Live-Video, Objekte und das Arbeitsbereich-Dashboard  
- **Rechtes Fenster** – Kontextbezogene Informationen, wie Teilnehmer, Besprechungen oder Chat  

Die meisten Interaktionen werden über das **untere Menü** initiiert.  
Durch Klicken auf eine Menüoption wird ein **Seitenbereich** auf der linken oder rechten Seite des Bildschirms geöffnet, während die **zentrale Arbeitsfläche** der primäre Anzeigebereich bleibt.

---
#### 3.2.2 Beispiel für die Besprechungsansicht

Hier ist ein Beispiel für eine Ansicht in einem Avatour-Meeting:

![Avatour-Meeting-Benutzeroberfläche mit Medienbereich, leerem Arbeitsbereich und Teilnehmerbereich](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Avatour-Meeting mit Asset-Panel (links), Arbeitsbereich (Mitte) und Teilnehmer-Panel (rechts)*

---

#### 3.2.3 Beispiel für die Arbeitsbereichsansicht

Hier ist ein Beispiel für eine Arbeitsbereichsansicht:

![Avatour-Arbeitsbereich mit Asset-Panel, leerer Arbeitsfläche und Meeting-Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Avatour-Arbeitsbereich mit dem Bereich „Assets“ (links), der Arbeitsfläche (Mitte) und dem Bereich „Meetings“ (rechts)*

---

#### 3.2.4 Übersicht über das untere Menü

Das untere Menü bietet Zugriff auf die wichtigsten Steuerelemente und Bereiche der Benutzeroberfläche:

**Unteres Menü im Meeting**  

![Unteres Menü im Avatour-Meeting](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Unteres Menü im Avatour-Meeting*

- **Assets** – Zeigen Sie Dateien im Arbeitsbereich an, darunter aufgezeichnete Videos, Bilder, Screenshots und PDFs. 
- **Chat** – Senden Sie Nachrichten an alle Besprechungsteilnehmer.  
- **Kamera** – Schalten Sie Ihre Webcam ein oder aus.  
- **Mikrofon** – Stummschalten oder Stummschaltung aufheben.  
- **Präsentieren** – Ein Asset, den Desktop oder das Webcam-Bild präsentieren (siehe Abschnitt „Präsentieren“ weiter unten).  
- **Host-Tools** (nur für Gastgeber):  
  - **Fokus sperren** – Sperren Sie die Ansicht für alle Teilnehmer.  
  - **Alle stummschalten** – Schalten Sie alle Teilnehmer stumm.  
- **Vollbild aktivieren** – Schalten Sie die Besprechungsregisterkarte auf Vollbild um.  
- **Besprechung verlassen** – Verlassen Sie die Besprechung.  
- **Aufzeichnung starten** – Verwenden Sie diese Schaltfläche, um die Aufzeichnung während eines Meetings manuell zu starten und zu beenden. Alternativ können Meetings automatisch aufgezeichnet werden, wenn in den Arbeitsbereichseinstellungen die Option **„Aufzeichnung automatisch starten“** aktiviert ist. In beiden Fällen werden die Aufzeichnungen in den Assets des Arbeitsbereichs gespeichert.
- **Karte** – Öffnen oder schließen Sie das Kartenfenster, um die Kamerabewegung für Assets mit GPS-Tracking anzuzeigen. Durch Klicken auf einen Ort springen Sie zum genauen Punkt im Video. Die Karte wird während der Videowiedergabe in Echtzeit aktualisiert. Auf der Karte werden auch Notizen angezeigt.
- **Teilnehmer** – Öffnen oder schließen Sie das Teilnehmerfenster.  
- **Besprechungsinfo** – Zeigen Sie den Besprechungscode und den Besprechungslink an und greifen Sie auf entsprechende Tutorials zu.  

![Avatour-Besprechungsinfo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Seitenbereich „Avatour-Besprechungsinfo“*

- **Einstellungen** – Passen Sie die Sprach-, Audio- und Videoeinstellungen an. Bei Live-360°-Videobesprechungen können Sie mit **Bitrate anzeigen** die Verbindungsstatistiken überwachen.

> Tipp: Senden Sie den Besprechungslink oder fügen Sie ihn einem Kalendereintrag hinzu, um Teilnehmer einzuladen.

---

##### Menü „Präsentieren“

Über die Option **Präsentieren** im unteren Menü des Meetings können Sie Inhalte für alle Teilnehmer freigeben.

- **Kamera** – Geben Sie die Kamera Ihres Geräts (Laptop, Smartphone usw.) frei. Diese Funktion kann auch während eines Live-360°-Videomeetings genutzt werden, um eine zweite Ansicht für Nahaufnahmen oder bestimmte Details einzublenden. Wenn Sie die Kamera eines Smartphones (Vorder- oder Rückkamera) freigeben, können die Teilnehmer des Remote-Meetings den Zoom des Smartphones nutzen und die Taschenlampe ein- und ausschalten.
- **Desktop** – Geben Sie Ihren Desktop-Bildschirm für alle Teilnehmer frei.  
- **Asset** – Präsentieren Sie ein Asset aus dem Arbeitsbereich. Durch die Auswahl eines Assets wird die **Asset-Symbolleiste** geöffnet, die Wiedergabesteuerungen und Kollaborationswerkzeuge speziell für das präsentierte Asset bereitstellt.

##### Asset- und Live-360°-Symbolleisten in Meetings

Wenn Sie ein Asset in einem Meeting präsentieren, erscheint die **Asset-Symbolleiste** über der Arbeitsfläche. Hier sind die Werkzeuge und Menüpunkte, die bei der <u>Präsentation eines Assets in einem Meeting</u> verfügbar sind – von links nach rechts erklärt.

![Avatour-Menü bei der Präsentation eines Assets in einem Meeting](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Avatour-Menü bei der Präsentation eines Assets in einem Meeting*

Wenn ein Live-360°-Video in ein Meeting gestreamt wird, wird dieses Menü am unteren Rand der Arbeitsfläche angezeigt.

<img src="https://res.cloudinary.com/avatour/image/upload/c_fill,g_auto,w_600,h_120/avatour-screenshot-live360video-menu-meeting_cguwzb.png" alt="Avatour-Menü mit Live-360°-Video in einem Meeting" style="width:50%; display:block; border:1px solid #DDE5EA; border-radius:6px; margin:20px 0 4px;"> *Avatour-Menü mit Live-360°-Video in einer Besprechung*

Hier finden Sie eine Beschreibung aller Elemente, die in den obenstehenden Menüs angezeigt werden.

- **Video-Zeitleiste / Fortschrittsbalken** – Zeigt den Videofortschritt mit Notizen und aus dem Audio extrahierten Schlüsselthemen an. Klicken Sie auf eine Notiz oder ein Thema, um zu diesem Moment zu springen und die Notiz zu öffnen. Enthält **Wiedergabe-/Pause**-Steuerelemente.   
- **Schnappschuss** – Erfassen Sie ein 360°- oder 2D-Bild aus dem Asset.  
- **Spotlight** – Hebt während Live-Sitzungen einen bestimmten Bereich für alle Teilnehmer hervor.  
- **Blickwinkel (POV) anzeigen/ausblenden** – Zeigt an, wohin jeder Teilnehmer im 360°-Video blickt.  
- **Notizen** – Erstellen Sie Notizen, die an bestimmte Momente in einem Asset oder während eines Live-Videostreams verankert sind. (Hinweis: In einem Live-Stream wird automatisch ein Asset (= Schnappschuss) erstellt, um die Notiz zu erfassen.) Jede Notiz hat einen Verfasser und kann kategorisiert (Beobachtung, Problem, Maßnahme, Empfehlung), nach Status verfolgt (Offen → In Bearbeitung → Gelöst), einem Verantwortlichen zugewiesen und über direkte Links geteilt werden. Verfügt das Asset über einen GPS-Track, zeigen die Notizen zusätzlich die GPS-Koordinaten an. Notizen können zudem an eine andere Position verschoben (durch Ziehen die Position ändern) und in der Zeitleiste verschoben werden (in der Zeitleiste vorwärts oder rückwärts bewegen).

  ![Avatour-Notiz und Notizfilter](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-notes-and-filters_g181oc.png) *Avatour-Notizen und Notizfilter*

- **Notizen per Sprachbefehl** – Hierbei handelt es sich um automatisch generierte Platzhalter, wenn in einem aufgezeichneten Video Äußerungen wie „Notiz einfügen“, „Notiz machen“ oder „eine Notiz erstellen“ erkannt werden. Diese Notizen erscheinen auf der Zeitachse und müssen vom Benutzer **positioniert und fertiggestellt** werden. 

  ![Avatour-Notizen – durch Sprachbefehle generiert](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Avatour-Notizen – Durch Sprachbefehl generiert*

- **Von der KI generierte Notizen** – Hierbei handelt es sich um automatisch generierte Platzhalter, wenn die Aufzeichnung im Audiospuren des Videos Erwähnungen erkennt, die nach Problemen klingen, die zur weiteren Bearbeitung erfasst werden müssen. KI-generierte Notizen müssen zunächst vom Notizbesitzer genehmigt werden (siehe Workspace-Dashboard unten). Nach der Freigabe verhalten sie sich wie Sprachbefehlsnotizen, da sie auf der Zeitachse erscheinen und vom Benutzer **positioniert und fertiggestellt** werden müssen. 

- **Notizen- und Zusammenfassungsbereich** – Öffnet einen Seitenbereich, in dem alle Notizen, Schlüsselthemen und eine Zusammenfassung für das Asset angezeigt werden. Ein Klick auf einen Eintrag führt Sie zu diesem Moment im Video. 

 ![Avatour-Zusammenfassung zum Asset](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Avatour-Zusammenfassung bei der Präsentation eines Assets in einer Besprechung*

  ![Avatour-Themen](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Avatour-Themen bei der Präsentation eines Assets in einer Besprechung*

  Über das **Seitenpanel** können Sie **einen Asset-Bericht ausdrucken** oder **als TXT- oder CSV-Datei herunterladen**. Berichte können verschiedene Elemente enthalten, die Sie **vor dem Export auswählen** können. 

  ![Avatour-Menüs zum Drucken von Asset-Berichten](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Avatour-Menüs zum Drucken/Herunterladen von Asset-Berichten*  

  ![Auswahl der Elemente für den Avatour-Asset-Bericht zum Drucken](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menü zur Elementauswahl im Avatour-Asset-Bericht*

- **Link teilen** – Einen Link zu einer bestimmten Notiz oder Szene im Asset teilen.  
- **Untertitel (CC)** – Während der Videowiedergabe eine Texttranskription auf dem Bildschirm anzeigen.

##### Asset-Symbolleiste (Arbeitsbereich)

Beim Anzeigen eines Assets in einem Arbeitsbereich ist die Symbolleiste ähnlich, jedoch für die individuelle Nutzung optimiert:

![Avatour-Menü bei der Präsentation eines Assets außerhalb einer Besprechung, z. B. beim Besuch eines Arbeitsbereichs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Avatour-Menü bei der Präsentation eines Assets in einem Arbeitsbereich*

- **Video-Zeitleiste / Fortschrittsbalken** – Zeigt den Videofortschritt mit Notizen und Schlüsselthemen an, die aus der Audiospur extrahiert wurden. Klicken Sie an eine beliebige Stelle auf der Zeitleiste, um im Video zu navigieren. Klicken Sie auf eine Notiz oder ein Thema, um zu diesem Moment zu springen und die Notiz zu öffnen. Enthält **Wiedergabe-/Pause-**-Steuerelemente.  
- **Schnappschuss, Notizen, Notizen- und Zusammenfassungsbereich, Link teilen, Untertitel**  
- Nicht verfügbar: **Spotlight, POV** (dafür sind Live-Teilnehmer erforderlich)  
- Zusätzliche Steuerelemente:
  - **10-Sekunden-Schritte** – Vorwärts/rückwärts springen  
  - **Wiedergabegeschwindigkeit** – Geschwindigkeit anpassen (0,5×–2×)  
  - **Video zuschneiden** – Anfang oder Ende des Clips zuschneiden


## 4. Für Host- und Admin-Benutzer – Avatour-Webkonsole {#for-host-and-admin-users-avatour-web-console}

Wenn Sie sich bei Ihrem Avatour-Benutzerkonto anmelden, gelangen Sie zur **Webkonsole**.  

### 4.1 Webkonsole – Übersicht Hauptmenü {#web-console-overview-main-menu}

Auf der linken Seite sehen Sie die folgenden Menüpunkte:

![Avatour-Webkonsole – Hauptmenü](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Avatour-Webkonsole – Hauptmenü*

- **Arbeitsbereiche** – Organisieren Sie Ihre Inhalte effizient. Jeder Arbeitsbereich enthält **Assets**, **Mitarbeiter**, **Besprechungen** und **Einstellungen**.  
- **Assets** – Greifen Sie auf alle Ihre Assets (Videos, Bilder, PDFs) zu und verwalten Sie diese. Administratoren können alle Assets des Kontos einsehen, und freigegebene Assets sind für alle Benutzer sichtbar.  
- **Profil** – Verwalten Sie Ihre Sprache und Ihr Passwort.  
- **Analysen** – Verfolgen Sie Sitzungsaktivitäten, die Nutzung der Arbeitsbereiche und ROI-Kennzahlen.  
- **Einstellungen** *(nur für Administratoren)* – Konfigurieren Sie die Standardwerte für Arbeitsbereiche, Besprechungen und Assets unternehmensweit. Administratoren können außerdem das Branding (Logo, Farben, Hintergründe) anpassen.  
- **Konto** *(nur für Administratoren)* – Verwalten Sie registrierte Benutzer und 360°-Kameras.  
- **Geräteanmeldung** – Geben Sie den auf Ihrer 360°-Kamera angezeigten Code ein, um sie mit Ihrem Konto zu koppeln.  
- **Anleitungen** – Greifen Sie auf geführte Anleitungen zu.  
- **Abmelden** – Melden Sie sich von der Konsole ab.

> Bereiche wie „Profil“, „Geräteanmeldung“, „Tutorials“ und „Abmelden“ sind selbsterklärend und weisen keine detaillierten Unterabschnitte auf.

---

### 4.2 Webkonsole – Details nach Menüpunkt (mit Bildern) {#web-console-details-by-menu-item}

#### 4.2.1 Arbeitsbereiche

Arbeitsbereiche sind flexible Organisationseinheiten, mit denen Sie Assets, Mitwirkende und Besprechungen an einem Ort verwalten können. Über die Schaltfläche **Neuer Arbeitsbereich** in der oberen rechten Ecke können Sie einen neuen Arbeitsbereich erstellen.

![Avatour-Webkonsole – Hauptmenüpunkt „Arbeitsbereiche“](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour-Webkonsole – Hauptmenüpunkt „Arbeitsbereiche“*

Klicken Sie auf das Glockensymbol, um eine Übersicht über die Aktivitäten im Arbeitsbereich der letzten 7 Tage anzuzeigen.

![Avatour-Webkonsole – Letzte Aktivitäten im Arbeitsbereich](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Letzte Aktivitäten im Arbeitsbereich*

Innerhalb eines Arbeitsbereichs:

![Avatour-Arbeitsbereich mit Asset-Bereich, Dashboard und Besprechungsbereich](https://res.cloudinary.com/avatour/image/upload/v1785929001/avatour-screenshot-workspace-dashboard_dqp5ff.png) *Arbeitsbereich mit Assets (links), Arbeitsbereich-Dashboard (Mitte), Meetings (rechts)*

In der Mitte sehen Sie das Arbeitsbereich-Dashboard, das Ihnen einen Überblick über alle Notizen in den diesem Arbeitsbereich zugewiesenen Assets bietet, mit mehreren Dropdown-Menüs zur Auswahl nach verschiedenen Notizenattributen. Hier können Sie auch die von der KI vorgeschlagenen Notizen annehmen oder löschen. Außerdem können Sie alle Notizen aus dieser Ansicht exportieren.

In den Menüs unten finden Sie:

- **Assets** – Verwalten Sie die diesem Arbeitsbereich zugewiesenen Dateien.  
- **Mitarbeiter** – 
  Zugriff auf Arbeitsbereiche steuern durch 
  - **Betrachter** – Kann Assets anzeigen. Bei einer Einladung wird bei Bedarf ein Gastbenutzer angelegt.  
  - **Bearbeiter** – Vollständige Kontrolle über den Arbeitsbereich, gleiche Rechte wie der Host. Bei einer Einladung wird der Benutzer bei Bedarf zum Host hochgestuft.  
> Mehrere Benutzer können gleichzeitig ohne Besprechung auf einen Arbeitsbereich zugreifen. Öffentliche Arbeitsbereiche und Zugriffseinstellungen für Besprechungen bieten alternative Zugriffsmöglichkeiten.  
- **Bericht** – Erstellen Sie mithilfe einer Inspektionsvorlage einen Bericht zu ausgewählten Assets des Arbeitsbereichs. Die Antworten werden von der KI auf der Grundlage der Audiospuren in den ausgewählten Videos generiert.  

![Avatour-Arbeitsbereichsbericht und Objektauswahl](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Arbeitsbereichsbericht und Objektauswahl*

- **Karte** – Zeigen Sie die Standorte von Objekten mit GPS-Funktion auf einer Karte an, wie oben für Besprechungen beschrieben. 
- **Besprechungen** – Organisieren Sie Besprechungen im Arbeitsbereich.  
- **Einstellungen** – Konfigurieren Sie die Standardeinstellungen für den Arbeitsbereich und Besprechungen:

![Avatour-Einstellungen – Arbeitsbereichsansicht](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Arbeitsbereichseinstellungen*

**Arbeitsbereichseinstellungen**

- **Berichtsvorlage** – Wählen Sie eine Inspektionsvorlage für KI-generierte Berichte aus. Diese können Sie im Konto hochladen (siehe unten).  
- **Benachrichtigungen aktivieren** – Tägliche E-Mail-Zusammenfassungen zu Statusänderungen bei Notizen.  

![E-Mail-Benachrichtigungen – Beispiel](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Beispiel für E-Mail-Benachrichtigungen*

- **Öffentlicher Arbeitsbereich** – Jeder, der über den Link verfügt, kann Assets direkt einsehen.

**Besprechungseinstellungen**
  
* **Authentifizierung erforderlich** – Teilnehmer müssen sich anmelden.  
* **Gastzugang zulassen** – Nicht registrierten Benutzern wird das Anzeigen von Assets gestattet.  
* **Aufzeichnung automatisch starten / Manuell starten** – Wählen Sie aus, ob Besprechungen automatisch aufgezeichnet oder manuell gestartet werden sollen.  
* **Moderator erforderlich** – Der Moderator muss Teilnehmer zulassen; die Besprechung endet, wenn der Moderator die Besprechung verlässt.  
* **Zugang für Zuschauer zulassen** – Teilnahme ohne Mikrofon oder Kamera; Kommunikation über den Chat.  
* **Passwortgeschützte Besprechungen** – Für die Teilnahme ist ein Passwort erforderlich.  
* **Frage zu Reiseeinsparungen anzeigen** – Fragen Sie die Teilnehmer, ob die Besprechung zu Reiseeinsparungen geführt hat.  

> Einstellungen können kombiniert werden (z. B. kein Gastgeber erforderlich, aber passwortgeschützt).

---

#### 4.2.2 Assets

Verwalten Sie alle 360°-/2D-Videos, Bilder und PDFs. Laden Sie Assets hoch bzw. herunter, ordnen Sie sie Arbeitsbereichen zu, teilen Sie sie mit anderen Benutzern, benennen Sie sie um, drucken oder laden Sie Berichte herunter, aktivieren Sie die Gesichtsverwischung und die KI-Zusammenfassung.

![Avatour-Webkonsole – Hauptmenüpunkt „Assets“](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Hauptmenüpunkt „Assets“*

Sie können auch den HTML-Code generieren, um eine öffentliche Einbettung eines Assets zu ermöglichen, z. B. auf Ihrer Website. Aktivieren Sie dazu einfach das Kontrollkästchen „Öffentliche Einbettung aktivieren“ und klicken Sie anschließend auf „Speichern“, um den Code zu erhalten.

![Avatour-Webkonsole – Hauptmenüpunkt „Assets“](https://res.cloudinary.com/avatour/image/upload/v1785921604/avatour-screenshot-main-menu-assets-embed-code_mtau8g.png) *Hauptmenüpunkt „Assets“*

#### 4.2.3 Einstellungen

Admin-Benutzer haben Zugriff auf dieses Menü, um die Einstellungen für die gesamte Avatour-Plattform zentral zu verwalten. Jede Einstellung kann aktiviert oder deaktiviert werden, um als Standardeinstellung für die gesamte Plattform festgelegt zu werden. Jede Einstellung kann zudem gesperrt werden, was bedeutet, dass die Standardeinstellung von anderen Nutzern der Plattform nicht geändert werden kann. Hier können Sie auch Marketing-Anpassungen hinsichtlich Ihres Brandings (Logo, Farben usw.) vornehmen.

![Avatour-Webkonsole – Hauptmenüpunkt „Einstellungen“](https://res.cloudinary.com/avatour/image/upload/v1781172727/avatour-screenshot-main-menu-settings-1-of-2_fsaatf.jpg) *Bereich „Einstellungen“*

#### 4.2.4 Konto

Hier können Sie Details zu Ihrem Konto einsehen und registrierte Benutzerkonten (Host, Admin, Gast) verwalten, einschließlich deren Zugriffsrechte auf den Arbeitsbereich, sowie Inspektionsvorlagen hochladen, um Arbeitsbereichsberichte zu erstellen (siehe oben).

![Avatour-Webkonsole – Hauptmenüpunkt „Konto“](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-account-1-of-3_oq5amr.png) *Kontoübersicht – Obere Bereiche*

![Avatour-Webkonsole – Hauptmenüpunkt „Konto“](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-account-2-of-3_oq5amr.png) *Kontoübersicht – Verwaltung der Arbeitsbereichszugriffe*

![Avatour-Webkonsole – Hauptmenüpunkt „Konto“](https://res.cloudinary.com/avatour/image/upload/v1772360316/avatour-screenshot-main-menu-account-3-of-3_udgyjz.png) *Kontoübersicht – Untere Bereiche*

#### 4.2.5 Analysen

Bietet Einblicke in Besprechungen, die Nutzung von Arbeitsbereichen und ROI-Kennzahlen.

![Avatour-Webkonsole – Hauptmenüpunkt „Analytik“ (1 von 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Übersicht „Analytik“*

![Avatour-Webkonsole – Hauptmenüpunkt „Analytik“ (2 von 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Besprechungsaktivität und Arbeitsbereichsnutzung*

![Avatour-Webkonsole – Hauptmenüpunkt „Analytik“ (3 von 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Einsparungen und Nutzung von Gerätelizenzen* 

## 5. Vor Ort – So verwenden Sie das Avatour-Komplettpaket {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Erste Schritte
Hier finden Sie eine sehr umfassende Online-Anleitung für Ihre ersten Schritte mit dem Avatour Turnkey Kit: [Schnellstartanleitung – Avatour Turnkey Kit 3.1 (Einrichtung des Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Und hier ist auch das Bild mit den Anweisungen, das Sie auf der Innenseite des Deckels des 3.1-Kit-Koffers finden.
![Abbildung auf der Innenseite des Deckels des Avatour-Kit-Koffers](https://res.cloudinary.com/avatour/image/upload/v1775994773/avatour-turnkey-kit-3.1-inside-lid-picture_dq4ipl.png) *Bild auf der Innenseite des Deckels des Avatour-Kit-Koffers* 

Befolgen Sie die Anleitung und die Anweisungen zum Auspacken, Zusammenbauen und Einschalten Ihrer Kamera.

---

### 5.2 Nützliche Tipps

#### Externer Akku – Längere Live-Meetings und verbesserte Wärmeableitung 

Der interne Akku der Kamera hält ca. 30–45 Minuten. Wenn der Akku fast leer ist, wird eine Warnmeldung angezeigt. Mit einem externen Akku können Sie die Betriebszeit verlängern und sogar unbegrenzt nutzen, da Sie die Akkus während des Betriebs austauschen können.

- **Falls Ihr Set einen Ulanzi-Akku enthält:** Befestigen Sie ihn zwischen dem Stativfuß und dem ausziehbaren Stab und schließen Sie den Akku dann über USB-C an die Kamera an.  

- **Wenn Ihr Set einen Telesin-Akustab enthält:** Befestigen Sie die Kamera direkt am ausziehbaren Telesin-Akustab und verbinden Sie sie über USB-C.  

Verwendung des externen Akkus:

1. Verlängert die Gesamtlaufzeit von ca. 40 Minuten (nur Kamera-Akku) auf ca. 3 Stunden.  
2. Verleiht dem Kameraaufbau zusätzliche Stabilität.  
3. Trägt dazu bei, eine mögliche Überhitzung zu verhindern.  

> Wir empfehlen, den externen Akku von Anfang an zu verwenden, insbesondere bei Live-Meetings.

#### Audio-Hinweise für Live-Meetings und Aufnahmen

- **Lärmreiche Umgebungen:** 
  Verwenden Sie die im Lieferumfang enthaltenen Shokz-Kopfhörer für eine klare Audioaufnahme.  
  - **Ein-/Ausschalten:** Halten Sie die „+“-Taste 3 Sekunden lang gedrückt (blaue LED = ein, rote LED = aus).  
  - **Bluetooth-Kopplungsmodus:** Halten Sie bei ausgeschaltetem Headset die Taste „+“ 5 Sekunden lang gedrückt (LED blinkt blau/rot).  
  - **Lautstärke:** Verwenden Sie die Tasten „+“ und „-“.  

- **Ruhigere Umgebungen / mehrere Teilnehmer in der Nähe der Kamera:** 
  Verwenden Sie den NoxGear-Aufstecklautsprecher. Er bietet zwar nicht die gleiche Klangqualität wie Konferenzlautsprecher (z. B. Jabra Speak), lässt sich aber einfach an Ihrem Hemd befestigen und nimmt Stimmen in der Nähe effektiv auf.  
  - **Ein-/Ausschalten:** Halten Sie die Wiedergabe-/Pause-Taste 2 Sekunden lang gedrückt.  
  - **Bluetooth-Kopplungsmodus:** Wechselt beim Einschalten automatisch in den Kopplungsmodus (LED blinkt blau/rot; leuchtet blau, wenn die Kopplung hergestellt ist).  
  - **Lautstärke:** Verwenden Sie die Tasten „+“ und „-“.  

- **Verwendung eines eigenen Geräts:** Wenn Sie ein alternatives Gerät bevorzugen (z. B. einen Konferenzlautsprecher oder ein eigenes Headset), können Sie es über die Kamera koppeln: Einstellungen → Bluetooth.  

#### Konnektivität
**Bevor Sie beginnen:** Stellen Sie eine Internetverbindung her über:

- **Lokales WLAN** (bevorzugt)
- **Mobilfunknetz** (außerhalb der WLAN-Reichweite)

**Empfohlene Bandbreite:** 10 Mbit/s Upload/Download für vollständiges 360°-Streaming (~5 Mbit/s). Eine geringere Bandbreite (1–2 Mbit/s) funktioniert nur im Stillstand.

##### Netzwerkgeschwindigkeit testen
- **Test an einem Standort:** Verwenden Sie einen beliebigen Geschwindigkeitsmesser, den Sie normalerweise nutzen (z. B. [Speedtest](https://www.speedtest.net)), um sowohl die Upload- als auch die Download-Bandbreite zu überprüfen.   
- **Test beim Gehen durch den Standort:** Über die Kamera: Einstellungen → Netzwerk → Verbindungstest. Gehen Sie durch den gesamten Raum, um die Netzabdeckung und die Bandbreite zu überprüfen.

##### Lokales WLAN
- Für stabile Verbindungen dringend empfohlen.  
- Falls die IT-Abteilung eine Whitelist-Eintragung verlangt, finden Sie die MAC-Adresse hier: Einstellungen → Über → WLAN-Adresse.

##### Mobilfunknetz
**Option A: Im Kit enthaltener Hotspot & SIM-Karte**  

- Befestigen Sie den GlocalMe-Hotspot am Telesin-Akku-Stick (Magnet).  
- Dies gewährleistet, dass keine Störungen auftreten und die Verbindung auch dann aufrechterhalten bleibt, wenn Sie sich von der Kamera entfernen.  
- Fehlerbehebung:
  - Vergewissern Sie sich, dass die vorinstallierte SIM-Karte (nicht die Cloud-SIM) verwendet wird.  
  - Aktivieren Sie 5G im SIM-Karten-Manager.  
  - Überprüfen Sie den korrekten APN für Ihre Region ([APN-Einrichtungsanleitung](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B: Persönlicher Hotspot / SIM-Karte**
- Verwenden Sie Ihr eigenes Smartphone oder einen dedizierten Hotspot.  

**Wichtiger Hinweis:**  
> Lassen Sie den Hotspot ausgeschaltet, solange eine WLAN-Verbindung besteht; aktivieren Sie ihn nur, wenn Sie sich außerhalb der Reichweite befinden. Das Betriebssystem der Kamera wechselt je nach Signalstärke dynamisch zwischen WLAN-Netzwerken und wechselt möglicherweise versehentlich zum Hotspot, selbst wenn WLAN verfügbar ist.

> Mobilfunknetze können die Bandbreite unerwartet drosseln. Erkundigen Sie sich bei Ihrem Mobilfunkanbieter nach den Limits Ihres Datentarifs oder wenden Sie sich an den Avatour-Support, wenn Sie unseren Hotspot und unsere SIM-Karte nutzen.

##### Situationen mit geringer Bandbreite
- Nehmen Sie Standortvideos vorab auf, um sie später abzuspielen ([Anleitung zur Aufnahme](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Geben Sie den Live-Stream einer Smartphone-Kamera weiter, um Bereiche mit geringer Bandbreite (0,1–0,3 Mbit/s Upload) zu ergänzen.

##### Keine Internetverbindung
- Es können nur vorab aufgezeichnete Videos verwendet werden ([Anleitung zur Aufzeichnung](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Weitere Teilnehmer vor Ort – Bewährte Vorgehensweisen

Wenn mehrere Teilnehmer von demselben Standort wie die 360°-Kamera aus an einem Live-Avatour-Meeting teilnehmen, ist ein sorgfältiges Management von **Audio und Bandbreite** entscheidend:  

- Jedes vor Ort verbundene Smartphone, Tablet oder Laptop beansprucht Netzwerkbandbreite und kann die Übertragung der 360°-Kamera beeinträchtigen.  
- Mehrere Mikrofone und Lautsprecher im selben Raum können **Audio-Rückkopplungen** verursachen, was das Meeting-Erlebnis für alle Teilnehmer unangenehm macht.

#### Weitere Teilnehmer vor Ort – Bewährte Vorgehensweisen

Wenn mehrere Teilnehmer von demselben Standort aus wie die 360°-Kamera an einem Live-Avatour-Meeting teilnehmen, ist ein sorgfältiges Management von **Audio und Bandbreite** entscheidend:  

- Jedes vor Ort verbundene Smartphone, Tablet oder jeder Laptop beansprucht Netzwerkbandbreite und kann die Übertragung der 360°-Kamera beeinträchtigen.  
- Mehrere Mikrofone und Lautsprecher im selben Raum können **Audio-Rückkopplungen** verursachen, was das Meeting-Erlebnis für alle Teilnehmer unangenehm macht.

Befolgen Sie zur Bewältigung dieser Herausforderungen die folgenden **Best Practices**:

- **Verwenden Sie kabelgebundene oder kabellose Kopfhörer:** Vorzugsweise mit Geräuschunterdrückung, um Echo und Rückkopplungen zu vermeiden.  
- **Vor-Ort-Modus:** Nehmen Sie im Vor-Ort-Modus am Meeting teil, wenn Sie sich physisch in der Nähe der 360°-Kamera befinden, da dieser Modus für den Einsatz vor Ort optimiert ist:

  - Schaltet das Mikrofon und den Lautsprecher des Teilnehmers standardmäßig stumm.
  - Sendet **nicht** das Kamerabild des Teilnehmers.
  - Zeigt das Bild der 360°-Kamera **nicht** im Browser des Teilnehmers an.
  - Schont die Netzwerkbandbreite und stellt sicher, dass der 360°-Kamera die maximal verfügbare Upload-Bandbreite für den Livestream zur Verfügung steht.
  - Nützlich, wenn ein Nutzer bestimmte Details zeigen möchte; Sie **können Ihr Kamerabild zurücksenden**, um gezielte Ansichten zu ermöglichen.
- **Stummschalten, wenn Sie nicht aktiv sprechen:** Verhindert unerwünschte Rückkopplungen und Ablenkungen.
- **Verwenden Sie nach Möglichkeit ein separates Netzwerk:** Verbinden Sie Ihr Smartphone mit einem anderen Netzwerk als dem der Kamera, um Störungen zu reduzieren.

Die Befolgung dieser Richtlinien gewährleistet eine reibungslose, qualitativ hochwertige Live-Tour sowohl für Teilnehmer vor Ort als auch für Remote-Teilnehmer.

### 5.3 Avatour-Kamera-App

Hier sind (1) das Hauptmenü, (2) die Einstellungen und (3) die Netzwerkeinstellungen.

![Avatour 360°-Kamera-App – Drei Menüs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360°-Kamera-App – 3 Menüs*

**Schnellaufnahme** – Für die Offline-Aufnahme von 360°-Videos auf die SD-Speicherkarte in der 360°-Kamera. – Eine ausführliche Beschreibung findest du unter [Wie nimmt man mit der Avatour-App 360°-Videos auf und lädt sie hoch?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Wir empfehlen die Verwendung eines externen Audiogeräts (über Bluetooth verbunden). Hinweis: Sie können den Aufnahmewinkel auch von 360° auf 270°, 180° sowie auf Standard-2D-Videos und -Bilder ändern, z. B. um den Fokus anzupassen oder vertrauliche Bereiche auszublenden – wechseln Sie dazu einfach im QC-Bildschirm den Modus in der unteren rechten Ecke (*dies ist jedoch nur möglich, wenn in den Einstellungen für „Quick Capture“ eine 4K-Auflösung ausgewählt wurde – siehe unten*)

**Live-Meeting** – Für Live-360°-Videokonferenzen. Sie sehen Ihre Arbeitsbereiche; wenn Sie auf einen davon klicken, wird der Live-Videostream von der 360°-Kamera gestartet. Bevor Sie mit Ihrer 360°-Kamera am Meeting teilnehmen können, müssen Sie ein Audiogerät über Bluetooth verbinden. Eine ausführliche Beschreibung findest du unter [Wie starte ich ein Live-Capture-Meeting mit deiner Pilot-Kamera?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Wenn Sie ein Live-Capture-Meeting mit Ihrer 360°-Kamera veranstalten, stehen Ihnen ähnliche Meeting-Tools zur Verfügung, die der Web-Erfahrung entsprechen. Hier ist ein Link zu unserem Knowledge-Base-Artikel, in dem diese Tools ausführlicher erläutert werden: [Tools der Operator-App](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galerie** – Hier finden Sie alle Ihre 360°-Videos und -Bilder zum Hochladen in die Avatour-Webkonsole. Sie können Assets in großen Mengen hochladen und löschen – tippen Sie dazu oben auf dem Bildschirm auf „Auswählen“. Vor dem Hochladen können Sie verschiedene Verarbeitungsschritte auswählen, wie z. B. „Gesichter unscharf machen“, eine „KI-Zusammenfassung“ erstellen und das Audiosignal mit „Sprachverbesserung“ optimieren. Sie können sogar einen Arbeitsbereich auswählen, dem das Asset zugeordnet werden soll – es wird natürlich auch im allgemeinen Asset-Bereich der Webkonsole zu finden sein.

**Einstellungen** – In den Einstellungen stehen Ihnen folgende Optionen zur Verfügung:

- **Netzwerk**: Mit dieser Option können Sie das WLAN-Netzwerk ändern, mit dem die Kamera verbunden ist, oder einen Netzwerkverbindungstest durchführen, um Ihren Streaming-Durchsatz anzuzeigen
- **Live-Aufnahme**: Passen Sie Ihre Live-Aufnahme-Einstellungen je nach verfügbarer Bandbreite, der VR-Empfindlichkeit des Gastes oder je nachdem, ob die Schutzgläser Ihrer Kamera installiert sind, an:

  - **Zielbildrate (optional)**: Passen Sie die Bildrate für Ihr Live-Aufnahme-Video zwischen 15 fps, 24 fps und 30 fps an. Höhere Bildraten sorgen für ein flüssigeres Video, erfordern jedoch mehr Upload-Bandbreite. Standard: 15 fps
  - **Zielbitrate**: Hiermit können Sie die maximale Streaming-Bitrate für Ihre Live-Aufnahme erhöhen oder verringern. Sie können Ihre Zielbitrate zwischen 1 Mbit/s und 10 Mbit/s einstellen. Höhere Bitraten führen zu einer höheren Videoauflösung, erfordern jedoch mehr Upload-Bandbreite. Standard: 5 Mbit/s
  - **Bewegung optimieren**: Dadurch wird die Bildrate des Videos verringert, was die Upload-Bandbreite Ihres Netzwerks entlastet und Ihre Streaming-Bitrate erhöht. Zudem hilft diese Option dabei, Bewegungsübelkeit bei VR-Teilnehmern zu reduzieren. Standard: Aus
  - **Richtungssperre**: Damit wird die 360°-Ansicht „gesperrt“, unabhängig davon, wie Sie die 360°-Kamera bewegen. Wenn Sie möchten, dass sich das 360°-Video mit der Kamerabewegung mitbewegt – z. B. wenn Sie mit dem vorderen Objektiv auf etwas „zeigen“ möchten –, stellen Sie die Richtungssperre auf „Nein“ ein. Dann verhält sich die Kamera wie eine herkömmliche Kamera, was für Führungen möglicherweise praktischer ist. Standard: Ja
  - **Anfangsausrichtung**: Wenn Sie die Richtungssperre auf „Nein“ setzen, können Sie wählen, welches Objektiv (vorne oder hinten) die Anfangsausrichtung sein soll, wenn Sie das Live-Video starten. Standard: Auf den Bediener gerichtet, da dies die natürlichste Art ist, ein Live-Meeting zu beginnen (= Rückkamera). Bei der „Schnellaufnahme“ ist dies anders (die Frontkamera ist standardmäßig die „Anfangsausrichtung“ – siehe unten).

- **Schnellaufnahme**: Passen Sie Ihre Einstellungen für die Schnellaufnahme entsprechend Ihrer bevorzugten Videobildrate, der verfügbaren Bandbreite für das Hochladen von Videoaufnahmen und anderen Präferenzen an. Kartenbezogene Funktionen, wie oben erläutert (z. B. Kartenansicht, Notizen auf einer Karte), sind möglich, wenn ein GPS-Signal empfangen wird und die Standorteinstellung in den nativen Kameraeinstellungen aktiviert ist (sollte standardmäßig der Fall sein). Das Standort-/GPS-Symbol in der oberen rechten Ecke von „Schnellaufnahme“ sollte grün sein. Es kann einen Moment dauern, bis das GPS-Signal empfangen und die Verbindung hergestellt ist.
  - **Auflösung**: Hier können Sie die Auflösung ändern. *(Die 6k-Auflösungen sind experimentell und erfordern vor dem Hochladen in die Avatour-Webkonsole einen manuellen Stitching-Schritt in der Galerie.)*

    - **4k** – Dies ist der Standard und bietet ein gutes Gleichgewicht zwischen Videoqualität und Dateigröße.
    - **6k bei 30 fps** *(erfordert einen zusätzlichen Schritt zum Zusammenfügen in der Galerie)*
    - **6k bei 10 fps** *(erfordert einen zusätzlichen Schritt zum Zusammenfügen in der Galerie)* – Dies ist nützlich, wenn Sie die Dateigröße geringer halten möchten als bei 30 fps, sofern flüssige Bewegungen weniger wichtig sind.
    - Für andere Auflösungen kannst du auch die nativen Kamera-Apps verwenden, auch auf dem PanoX V2. Details findest du unter [Wie nimmt man 360°-Videos mit der Avatour-App auf und lädt sie hoch?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)
  - **Zielbildrate** *(nur für 4k-Auflösung verfügbar)* - Stellen Sie die Bildrate für Ihre „Quick Capture“-Videoaufnahmen zwischen 15 fps, 24 fps und 30 fps ein. Höhere Bildraten sorgen für ein flüssigeres Video, erhöhen jedoch die Dateigröße und die Upload-Dauer. Empfohlen: 30 fps
  - **Ziel-Bitrate** *(nur für 4K-Auflösung verfügbar)* Stellen Sie die Ziel-Bitrate für „Quick Capture“-Uploads zwischen 5 Mbit/s und 20 Mbit/s ein. Niedrigere Bitraten erhöhen die Upload-Geschwindigkeit, verringern jedoch die Videoqualität. Empfohlen: 20 Mbit/s
  - **Ausrichtungssperre**: Wie oben unter „Live Capture“ beschrieben. Die Standard-Ausgangsausrichtung ist bei „Quick Capture“ immer die Frontlinse.

  > Weitere Hinweise zu den oben genannten Einstellungen und Videodateigrößen finden Sie in unserem [Avatour 360°-Videodateigrößenrechner](https://avatour.com/support/avatour-360deg-video-file-size-calculator). Um zu verhindern, dass der Speicherplatz knapp wird, wird eine Warnmeldung angezeigt, damit Sie die Aufnahme beenden und Speicherplatz freigeben können (z. B. durch Hochladen von Videos aus der Galerie in die Avatour-Webkonsole „Assets“).

- **Über**: Seriennummer des Geräts und Softwareversion anzeigen

**Konto** – Zum Einloggen mit Ihrem Avatour-Host- oder Admin-Konto.

## 6. Empfehlungen zu bewährten Vorgehensweisen {#best-practice-advice}

### 6.1 Erste (informelle) Nutzung und Einarbeitung

Für Ihre ersten Schritte und zum Kennenlernen der Avatour-Webkonsole und des Avatour-Turnkey-Kits empfehlen wir folgende Vorgehensweise:

1. Nehmen Sie das Kit mit nach Hause und probieren Sie es gemeinsam mit Familie und Freunden über Ihre private Internetverbindung aus.
2. Nehmen Sie das Kit mit ins Büro und verbinden Sie es mit einem Unternehmensnetzwerk (hier können unternehmensspezifische Probleme auftreten, z. B. Unternehmens-Firewalls – aber Sie wissen bereits aus Schritt 1, dass Avatour funktioniert, und dies ist ein Thema, das Ihr IT-Team mit Hilfe von Avatour klären kann).
3. Beginnen Sie damit, Avatour vor Ort (außerhalb Ihres Büros) an dem Tagungsort zu nutzen, zu dem Remote-Teilnehmer normalerweise anreisen müssten. Dabei könnten weitere Fragen zur Konnektivität auftauchen. Avatour hilft Ihnen dabei in Zusammenarbeit mit Ihrem IT-Team.
4. Beginnen Sie mit der Nutzung mit internen und externen Remote-Teilnehmern.

### 6.2 Vor einem 360°-Video-Live-Meeting

- Wir empfehlen, vor jeder Live-Tour – sofern es die Zeit erlaubt – eine aufgezeichnete 360°-Videotour durchzuführen, und zwar aus drei Gründen: (1) Sie haben eine Ausweichlösung für die Live-Tour, (2) Sie verfügen über Material zur Dokumentation und späteren Nachbereitung (zusätzlich zur aufgezeichneten Live-Tour) und (3) Sie beginnen damit, eine Bibliothek mit 360°-Videos all Ihrer Standorte aufzubauen, die für viele Anwendungsfälle hilfreich sein kann. 

- Laden Sie alle Komponenten des Sets vor dem Live-Meeting mindestens 90 Minuten lang auf. Wir empfehlen, alle Geräte kontinuierlich aufzuladen, wenn sie nicht in Gebrauch sind. So sind alle Geräte stets einsatzbereit, auch für ungeplante Ad-hoc-Meetings.

- Stellen Sie sicher, dass das Kit vollständig zusammengebaut ist (1. Stativsockel + 2. Ulanzi-Akku + 3. ausziehbarer Stab + 4. 360°-Kamera).

- Vergewissern Sie sich, dass ein Workspace für die Durchführung eines Live-Meetings erstellt wurde und fügen Sie alle relevanten Assets hinzu.

- Laden Sie alle Teilnehmer über Ihren Workspace zur Besprechung ein. Dadurch wird in den Kalendern aller Teilnehmer eine Einladung erstellt, die den Link zur Besprechung enthält.

- Koppeln und verbinden Sie Ihre Bluetooth-Kopfhörer oder den Lautsprecher, den Sie für Ihre Führung verwenden möchten, mit der Kamera.

- Alle Smartphone-Nutzer vor Ort sollten sich über ein anderes Netzwerk als das der Kamera verbinden. Dadurch wird die Belastung der Netzwerkbandbreite der Kamera verringert.

- Wenn Sie als Kameramann allein sind, nehmen Sie ein Smartphone mit, falls Sie die Smartphone-Kamera teilen und feine Details zeigen möchten.

- Vergewissern Sie sich, dass die 360°-Kamera eine Verbindung zu Ihrem lokalen WLAN herstellen kann.

- Planen Sie vor einem Avatour-Meeting die Route, die Sie durch die Einrichtung nehmen werden. Führen Sie ein Test-Avatour-Meeting mit der Kamera durch und überprüfen Sie, ob alle Bereiche eine Bandbreite von über 1 Mbit/s aufweisen. Dies können Sie auf dem Kamerabildschirm selbst sehen oder als Remote-Teilnehmer, indem Sie in den Einstellungen die Option „Bitrate anzeigen“ aktivieren.

- Sollten Sie feststellen, dass in einigen Bereichen nur wenig oder gar keine Bandbreite zur Verfügung steht, sollten Sie am besten Fotos oder eine Aufzeichnung machen. Diese können dann während des Meetings den Remote-Teilnehmern zur Ansicht präsentiert werden. Befolgen Sie dazu die obige Anleitung, in der unsere „Quick Capture“-Funktion für Offline-Aufnahmen und das Hochladen von Videos/Bildern erläutert wird.

- Wenn Remote-Teilnehmer an der Besprechung teilnehmen, die Avatour noch nicht zuvor genutzt haben, geben Sie ihnen eine kurze Übersicht über die Plattform, ihre Funktionen (360°-Live-Video, Assets, Schnappschüsse, Anmerkungen, Spotlight) und die Besprechungstools.

- Sie können zunächst eine andere Videokonferenzlösung (z. B. Teams, Zoom, Google Meet) nutzen, sollten jedoch die andere Videokonferenzanwendung vollständig schließen, bevor Sie zu Avatour wechseln. In einigen Fällen priorisieren diese anderen Anwendungen das Mikrofon, die Lautsprecher oder die Webcam Ihres Geräts, was dazu führt, dass diese für Avatour deaktiviert werden. Lassen Sie außerdem Avatour NICHT gleichzeitig mit einer anderen Videokonferenz laufen, da dies die verfügbare Bandbreite verringert.

- Wenn Sie die 360°-Kamera in einer Umgebung mit hohen Temperaturen einsetzen möchten, wird die Verwendung des Kühlmoduls empfohlen (nur Pilot Pano). Dies trägt dazu bei, das Risiko einer Überhitzung der Kamera und einer automatischen Abschaltung zu verringern.

### 6.3 Bei der Bedienung der Kamera vor Ort für ein 360°-Video-Live-Meeting

- Achten Sie bei der Bedienung der Kamera darauf, **langsam zu gehen** und **häufig anzuhalten, um die Kamera auf ihrem Stativ abzustellen**. Dies trägt dazu bei, (1) die Videoqualität zu verbessern, da durch den Verzicht auf unnötige Kamerabewegungen weniger Videodaten erzeugt werden, und (2) mögliche Videoausfälle zu verringern, wenn die Netzwerkverbindung der Kamera zwischen WLAN-Zugangspunkten wechselt.

- Halten Sie die Kamera vor sich und über Augenhöhe. So können alle Remote-Teilnehmer den Großteil Ihrer Umgebung sehen.

- Wenn die Kamera stabil stehen bleiben muss, verwenden Sie das Stativ und stellen Sie die Kamera auf die richtige Höhe ein, am besten auf Augenhöhe.

- Verbinden Sie die Kamera nach Möglichkeit immer mit Ihrem lokalen WLAN-Netzwerk. In Bereichen ohne WLAN-Zugang nutzen Sie den mitgelieferten Hotspot. Der Hotspot verfügt über eine SIM-Karte, die eine Verbindung zu einem zuverlässigen Mobilfunknetz in Ihrer Nähe herstellt. Schalten Sie den Hotspot immer aus, wenn er in Innenräumen nicht genutzt wird, da sich die 360°-Kamera sonst mit dem Hotspot verbinden könnte, was in Innenräumen nicht erwünscht ist. Halten Sie den Hotspot im Freien in der Nähe der 360°-Kamera.

- Wenn die Bitrate der Kamera unter 2 Mbit/s fällt, gehen Sie langsamer oder bleiben Sie ganz stehen, bis sich das Signal wieder stabilisiert hat. Dies geschieht in der Regel, wenn Sie von einem WLAN-Zugangspunkt zu einem anderen wechseln. 

- Wenn Sie wissen, dass die Verbindung und die Videoqualität beim Wechsel zu einem bestimmten Ort abfallen (Beispiel: beim Wechsel von einem Produktionsbereich in Innenräumen zu einem Außenbereich), informieren Sie die Remote-Teilnehmer bitte im Voraus darüber.

- Wenn Sie etwas sehr detailliert oder mit kleiner Schrift zeigen müssen, können Sie mit der 360°-Kamera ganz nah herangehen. Sie können auch Ihr eigenes Smartphone oder das eines Teilnehmers vor Ort nutzen, um an der Besprechung teilzunehmen und die (Rück-)Kamera Ihres bzw. dessen Smartphones einzublenden.

- Wenn möglich, empfehlen wir, dass eine weitere Person vor Ort ist, um bei der oben beschriebenen Freigabe der Smartphone-Kamera zu helfen, da sich dies oft als hilfreich oder notwendig erweist.

- Idealerweise sollten Smartphone-Nutzer vor Ort der Besprechung (1) im Vor-Ort-Modus und (2) über ein anderes Netzwerk als das der Kamera beitreten, um der 360°-Kamera keine wichtige Upload-Bandbreite wegzunehmen.

- Alle Teilnehmer vor Ort, die über ihr Smartphone teilnehmen, sollten stummgeschaltet sein, sofern sie nicht gerade aktiv sprechen.

### 6.4 Bei der Bedienung der Kamera vor Ort für Schnellaufnahmen (Offline-360°-Videoaufzeichnung)

- Die oben genannten, nicht auf die Netzwerkverbindung bezogenen Hinweise gelten im Allgemeinen auch für Offline-Aufnahmen (z. B. langsam vorgehen).

- Verwenden Sie immer ein externes Bluetooth-Audio-Headset.

- Überprüfen Sie bei Bedarf, ob das GPS funktioniert.

- Antizipieren Sie, was die Zuschauer sehen möchten, z. B. Details: Gehen Sie mit der 360°-Kamera ganz nah heran und warten Sie einen Moment.

- Stellen Sie die Kamera ab und richten Sie sie auf Dinge, die Sie hervorheben möchten. Wenn Sie die Richtungssperre auf „Nein“ setzen, können Sie mit der 360°-Kamera sogar auf etwas zeigen (z. B. mit dem vorderen Objektiv).  

- Wenn Sie aufnehmen, um einen KI-generierten Bericht zu erhalten, und dabei auch Sprachbefehle verwenden, sprechen Sie laut und deutlich. Um der KI dabei zu helfen, Orte, Maße und Probleme zu identifizieren und Ihre Inspektionsvorlagen auszufüllen, nennen Sie diese ausdrücklich und verwenden Sie dabei dieselbe Terminologie, die in Ihrer Vorlage verwendet wird.


> Hinweis: Die meisten Avatour-Funktionen sind auch für 2D-Videos verfügbar.
