# Avatour User and Best Practices Guide

## 1. For All Avatour Users {#for-all-avatour-users}

If you are new to Avatour, the following resources provide a helpful introduction to the platform and its capabilities:

1. [Avatour How it Works video](https://avatour.com/how-it-works) 
   A short overview of Avatour’s main features and how the platform enables immersive remote collaboration.
2. [FAQs](https://avatour.com/faqs) 
   Answers to frequently asked questions
3. [Glossary](https://avatour.com/glossary) 
   Definitions of key Avatour terms and concepts.
4. Website
   Have a look at the [Avatour Features](https://avatour.com/features) page along with the dedicated Use Cases and Industries sections to learn how Avatour can support your specific needs.

## 2. Avatour User Types

### 2.1 Meeting Attendees (No Account required)
Users can join the meeting without registering for an Avatour account.
Exception: If the host has restricted the meeting to registered users — for example, to allow only internal employees to join via Single Sign-On (SSO) — the calendar invitation will indicate that participants must log in to authenticate.

Users access the meeting as follows:
- Receive a calendar invitation from the host.
- Use the meeting link in the invitation to join.
- Enter a meeting password if the host has enabled one.
- Participants can join without an Avatour account unless the meeting is restricted and requires login to authenticate.

#### 2.1.1 Participant 

- Can join and interact fully (webcam, microphone, chat, and Present functionality).
- Maximum of 20 interactive participants per meeting.

#### 2.1.2 Spectator

- Can view the meeting and participate via chat only.
- Cannot share video, use a microphone, present, play/pause Assets, or capture Snapshots.
- Maximum of 10 Spectators per meeting.
- Together with Participants, a meeting can host up to 30 attendees.

## 2.2 Registered Users

Registered Users have an Avatour account. Accounts are created in one of the following ways:

- **Admin-invited:** During onboarding, Avatour sets up a **dedicated tenant** for the organization and creates one or more **Admin accounts**. Admins can then **invite users** within the organization and assign them to **groups**, which define their platform role (Guest, Host, or Admin). Invited users receive a **signup link** to complete account setup and set a password.  
- **Host-invited:** Hosts can add users as **Editor collaborators** to a Workspace. This consumes a **Host license** and ensures the user has Host-level access.  
- **SSO auto-provisioning (Enterprise/Business tier only):** Accounts can be automatically created by the IdP. By default, SSO-provisioned accounts are added to the **Guest group**, unless overridden via **SAML group mappings**. Admins can still invite users and assign group membership directly even when SSO is enabled.

**Summary:**  

Registered users and their group membership can be managed in multiple ways:

- **Admin management:** An Admin in the Avatour console can create users and assign them to groups, which define their platform role (Guest, Host, or Admin).  
- **SSO provisioning:** For Enterprise or Business tier customers with SSO enabled, the IdP can automatically provision accounts and assign group membership, which defines the user’s platform role.  
- **Host-invited users:** Hosts can invite other users as Editor collaborators to specific Workspaces. Assigning the Editor collaborator role consumes a Host license.

**Recommended Best Practice (Enterprise Customers):**  
For organizations expecting a large number of users who need access to Avatour, it is recommended to **integrate Single Sign-On (SSO)** and manage users and group memberships from the **IdP**. This approach streamlines account provisioning, group assignment, and license management, reducing administrative overhead and ensuring consistent access control.

---

### 2.2.1 Guest Users

- Added to the **Guest group**.  
- Can **view Assets** within Workspaces where they have been added as **Viewer collaborators**.  
- Cannot create workspaces, host meetings or upload content.  
- SSO-provisioned Guest accounts **authenticate via the IdP**; no Avatour-managed password is required.

---

### 2.2.2 Licensed Users (Web Console Access)

#### Host Users (Group: Host)

- Can create/ manage Workspaces, invite collaborators to a workspace, **host live meetings**, upload **Quick Captures**.  
- Has access to the **Host Dashboard** and **Operator App** on supported 360° cameras.  

#### Admin Users (Group: Admin)

- Includes all Host capabilities plus full account administration.

**Additional Admin privileges include:**

**Account Management**  
- Create new users and assign them to groups.
- Reset passwords when managed by Avatour (not applicable when SSO is enabled). 
- Upgrade Guest users to Host.  
- Deactivate users (Admin accounts must first be converted to Host before deletion).  
- Transfer assets from one Host user to another during deletion.

**Settings**  
- Configure **organization-wide security settings** for assets, workspaces and meetings hosted on the platform (e.g., whether a Host must be present to start a meeting, whether faces should be blurred on all videos uploaded to the platform).  
- Enable or disable **AI features** or **recording**.  
- Apply company branding consistently across the platform if a **custom domain** is configured.
  

**Assets & Analytics**  
- View all Assets uploaded by any user in the organization.  
- Review platform usage across the organization.

---

### 2.2.3 Workspace Collaborator Permissions

Workspace permissions define what a user can do **within a specific Workspace**. These are separate from platform-level group membership (Guest, Host, Admin).

- **Editor collaborator:** Users with this permission can:
  - Manage Assets (upload, remove, blur faces, generate summaries)  
  - Manage meeting settings (enable/disable recording, allow or remove participants)  
  - Schedule and host live meetings  
  - Generate reports based on predefined templates  
  - Add or remove collaborators from the Workspace  

- **Viewer collaborator:** Users with this permission have read-only access to Workspace Assets. They **cannot modify Assets, manage meetings, or manage collaborators**, but they **can create Notes on Assets**. 
  
## 3. For Remote Meeting Participants and Workspace Visitors {#for-remote-meeting-participants-and-workspace-visitors}

Avatour allows users to collaborate in two primary ways:

- **Join a live meeting:**  
  You may receive a **calendar invitation** to join an Avatour meeting. During the meeting, participants can conduct a **live remote site visit** or synchronously review assets together.

- **Visit a Workspace:**  
  You may also be invited as a **collaborator to a Workspace** to review assets **asynchronously** (on your own schedule).

### 3.1 How to Join an Avatour meeting and Visit an Avatour Workspace {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### Any "Flat Screen" Device with a Web Browser {#any-flat-screen}
You can join an Avatour meeting from **any desktop or laptop computer, smartphone, or tablet** using a web browser.  

> **Note:** Joining an Avatour meeting requires that you **grant microphone permissions**. Please accept any permission prompts from your browser.

1. **Via calendar invitation (recommended):**  
   - You will typically receive a **calendar invitation** with a **direct join link** (for example: `https://avatour.live/join?s=xxxxx`).  
   - Clicking the link will automatically populate the **5-character meeting code** and take you to the meeting.
   - **Authentication required:** Some meetings are restricted to registered users. In this case, the invitation will indicate that you need to **log in to access the meeting**.  
   - **Password-protected meetings:** Some meetings may require a password. In that case, the invitation will include the password you must enter to join.

2. **Via meeting code:**  
   - If the host shares a **5-character meeting code** separately, go to [https://avatour.live/join](https://avatour.live/join), enter your **name** and the **meeting code**, and join the meeting.  
   - If the meeting is **password-protected**, enter the password provided by the host.  
   - If the meeting requires **authentication**, you will need to **log in with your Avatour account** before joining.

> **Tip 1:** If your camera or microphone does not work, it may be in use by another application (for example, Microsoft Teams or Zoom). Close any apps that might be using your camera or microphone, then leave and rejoin the Avatour meeting.  

> **Tip 2:** If you are still unable to join the meeting, run this test: [https://avatour.live/test](https://avatour.live/test).  
> The test can identify whether your **corporate firewall or network** is blocking access, and will provide information to guide discussions with your IT team.  

> **Tip 3:** Do **not** use the Avatour iOS or Android apps to join meetings. These apps are only required when **streaming a live meeting from an Insta360 camera**, since those cameras cannot run the Avatour 360° software directly and require a smartphone to assist.

### Visiting a Workspace Without Joining a Meeting

You can access a Workspace without joining a live meeting in the following ways:

- **Public Workspace:**  
  If the Workspace is public, the link can be accessed directly—no login required.

- **Restricted Workspace:**  
  If the Workspace is restricted, you must be added as a **collaborator** with either **Editor** or **Viewer** permissions.

  1. When you are added as a collaborator, you will receive an **email notification** with a link to the Workspace.
  2. Click the link in the email to open the Workspace. If you are not already logged in, you will be prompted to **log in or complete signup**.
  3. Once logged in, the Workspace will open automatically.

  Alternatively, you can log in at  
  https://avatour.live/login  
  and access the Workspace from your **list of Workspaces**.

#### VR Headset {#vr-headset}
You can join a meeting and visit a workspace from a range of compatible Meta and Pico headsets. To do this: 

1. Install our Avatour app from your respective VR store app: [How to install Avatour VR app](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Load our app and input the meeting code or select a Workspace to join a meeting. For more information on how to use our VR app, see our Knowledge Base article [here](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Meeting and Workspace Collaboration Tools {#meeting-tools}

Avatour allows collaboration in two main contexts:

1. **Meetings (synchronous):** Collaborate in real-time with other participants, including live site visits or reviewing recorded assets together.  
2. **Workspaces (asynchronous):** Review and interact with assets on your own schedule, 24/7.

The **collaboration tools are mostly similar** between meetings and workspaces, with some differences due to the synchronous vs asynchronous context.

### 3.2.1 Interface Layout

The Avatour interface is organized around three main areas:

- **Left panel** – Workspace assets and supporting tools  
- **Center canvas** – Main viewing area for live video or assets  
- **Right panel** – Contextual information, such as participants, meetings, or chat  

Most interactions are initiated from the **bottom menu**.  
Clicking a menu option opens a **side panel** on the left or right side of the screen, while the **center canvas** remains the primary viewing area.

---
### 3.2.2 Meeting View Example

Here is an example of a view in an Avatour Meeting:

![Avatour Meeting UI with Assets Panel, blank Canvas and Participants Panel](https://res.cloudinary.com/avatour/image/upload/v1772362400/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Avatour Meeting with Assets Panel (left), Canvas (center), and Participants Panel (right)*

---

### 3.2.3 Workspace View Example

Here is an example of a Workspace view:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Avatour Workspace with Assets Panel (left), Canvas (center), and Meetings Panel (right)*

---

### 3.2.4 Bottom Menu Overview

The bottom menu provides access to the main interface controls and panels:

**Meeting Bottom Menu**  

![Avatour Meeting Bottom Menu](https://res.cloudinary.com/avatour/image/upload/v1772300383/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Avatour Meeting Bottom Menu*

- **Assets** – Review workspace files, including recorded videos, images, snapshots, and PDFs. 
- **Chat** – Send messages to all meeting participants.  
- **Camera** – Turn your webcam on or off.  
- **Microphone** – Mute or unmute yourself.  
- **Present** – Present an asset, desktop, or webcam feed (see Present section below).  
- **Host Tools** (hosts only):  
  - **Lock Focus** – Lock the view for all participants.  
  - **Mute All** – Mute all participants.  
- **Enable Full Screen** – Make the meeting tab full screen.  
- **Exit Meeting** – Leave the meeting.  
- **Start Recording** – Use this button to start and stop recording manually during a meeting. Alternatively, meetings can be recorded automatically if **auto-start recording** is enabled in the workspace settings. In both cases, recordings are saved to the workspace assets.
- **Map** – Open or close the map panel for assets with a GPS track. Clicking a location jumps to the exact point in the video. The map updates live as the video plays.
- **Participants** – Open or close the participants panel.  
- **Meeting Info** – View the meeting code, invite link, and access related tutorials.  

![Avatour Meeting Info](https://res.cloudinary.com/avatour/image/upload/v1772547439/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Avatour Meeting Info Side Pane*

- **Settings** – Adjust language, audio, and video settings. For live 360° video meetings, use **Show Bitrate** to monitor connectivity stats.

> Tip: Send the meeting link or add it to a calendar item to invite participants.

---

### Present Menu

The **Present** option in the meeting bottom menu allows you to share content with all participants.

- **Camera** – Share your smartphone/tablet camera. This can also be used during a live 360° video meeting to overlay a secondary view for close-ups or specific details. 
- **Desktop** – Share your desktop screen with all participants.  
- **Asset** – Present an asset from the workspace. Selecting an asset opens the **Asset toolbar**, which provides playback controls and collaboration tools specific to the asset being presented.

### Asset Toolbar (Meeting)

When presenting an asset in a meeting, the **Asset Toolbar** appears above the canvas. Here are the tools and menu items available when <u>presenting an Asset in a Meeting</u> - explained from left to right.

![Avatour Menu while Presenting an Asset in a Meeting](https://res.cloudinary.com/avatour/image/upload/v1772303706/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Avatour Menu when presenting an Asset in a Meeting*


- **Video Timeline / Progress Bar** – Shows video progress with notes and key topics extracted from audio. Click a note or topic to jump to that moment and open the note. Includes **Play / Pause** controls.   
- **Snapshot** – Capture a 360° or 2D image from the asset.  
- **Spotlight** – Highlight a specific area for all participants during live sessions.  
- **Show/Hide Point-of-View (POV)** – Display where each participant is looking in the 360° video.  
- **Notes** – Create notes anchored to specific moments in the asset. Notes can be categorized (Observation, Issue, Action, Recommendation), tracked by status (Open → In Progress → Resolved), and shared via direct links.  

  ![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/v1772374822/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Avatour Note and Note Filters*

  **Voice Command Notes** – These are automatically generated placeholders when the recording detects mentions like “insert note,” “take a note,” or “make a note.” These notes appear on the timeline and need to be **positioned and finalized** by the user. 

  ![Avatour Notes - Voice Command Generated](https://res.cloudinary.com/avatour/image/upload/v1772921944/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Avatour Notes - Voice Command Generated*

- **Notes and Summary Panel** – Opens a side panel that displays all notes, key topics, and an executive summary for the asset. Clicking an item jumps to that moment in the video.  

  ![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Avatour Executive Summary while presenting an Asset in a Meeting*

  ![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Avatour Topics while presenting an Asset in a Meeting*

  From the **Side Panel**, you can **print an asset report** or **download it as TXT or CSV**. Reports can include notes, AI-generated topics, and full transcriptions. You can also **choose which elements to include** before exporting.  

  ![Avatour Asset Report Print Menus](https://res.cloudinary.com/avatour/image/upload/v1773496969/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Avatour Asset Report Print / Download Menus*  

  ![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/v1772376570/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Avatour Asset Report Element Selection Menu*

- **Share Link** – Share a link to a specific note or scene in the asset.  
- **Closed Captions (CC)** – Display on-screen text transcription during video playback.

### Asset Toolbar (Workspace)

When reviewing an asset in a workspace, the toolbar is similar but optimized for individual use:

![Avatour Menu while Presenting an Asset outside a meeting, e.g. when visiting a workspace](https://res.cloudinary.com/avatour/image/upload/v1772303705/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Avatour Menu when presenting an Asset in a Workspace*

- **Video Timeline / Progress Bar** – Shows video progress with notes and key topics extracted from audio. Click anywhere on the timeline to scrub through the video. Click a note or topic to jump to that moment and open the note. Includes **Play / Pause** controls.  
- **Snapshot, Notes, Notes and Summary Panel Panel, Share Link, Closed Captions**  
- Not available: **Spotlight, POV** (these require live participants)  
- Additional controls:
  - **10-second steps** – Skip forward/backward  
  - **Playback Speed** – Adjust speed (0.5×–2×)  
  - **Trim Video** – Trim beginning or end of the asset

## 4. For Host and Admin Users - Avatour Web Console{#for-registered-users}

When you log in to your Avatour User Accoung you will access the Web Console. 

### 4.1 Web Console - Overview Main Menu

On the left hand side you will see the following menu items.

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/v1772366766/avatour-screenshot-main-menu_qwpthq.png) *Avatour Web Console - Main Menu*

**Workspaces** - Workspaces can be set up for many purposes (e.g. sites, projects, customer, supplier) and are organisational units helping you to work efficiently in a controlled environment comprising of the following elements.

**Assets** - All your assets (videos, pictures, pdfs) in one place under <u>My Assets</u>. Admin users can see all <u>Account Assets</u> across all host users. <u>Shared Assets</u> are those which hosts share with all other users on the Avatour platform. Here you can rename assets, activate face blur and generate topics.

**Profile** - Manage your language and reset your password.

**Analytics** - Get insight about sessions and usage

**Settings** - For Admin Users only. Manage some general settings and customize your branding.

**Account** - For Admin Users only. Manage users and devices (= 360° cams).

**Device Login** - Enter here the number shown on the Avatour app on your 360° cam to log in as user on the 360° cam. You can also log in on your 360° cam with your Avatour host account email and password but simply entering the device code on the Avatour Web Console might be easier.

**Sign out** of your account.

 

### 4.2 Web Console - Details by Menu Item

### 4.2.1 Workspaces

Workspaces can be set up for many purposes (e.g. sites, projects, customer, supplier) and are organisational units helping you to work efficiently in a controlled environment.  You can create a new one with the "New Workspace" button in the upper right corner of the screen.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/v1772360323/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Main Menu Item Workspaces*

Click notifications (the bell icon) to get a summary of activities in a workspace over the last 7 days.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/v1772919758/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Avatour Web Console - Workspace Recent Activities*

You can enter a workspace by clicking on it. Here is a view of the structure in a workspace.

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Avatour Workspace with Assets Panel (left), blank Canvas (center) and Meetings Panel (right)*

Each workspace comprises of the following elements (explained from left to right).

**Assets** - Manage assets allocated to that workspace 

**Collaborators** - Manage Access to the Workspace

- **Viewer** - can view assets in the workspace. Adding a Collaborator Viewer will send an invitation to become a registered Avatour Guest user.
- **Editor** - have the same right as the Host (owner of the workspace) and with this full workspace control. Adding a Collaborator Viewer will send an invitation to become a registered Avatour Host user.

> N.B.: Several users can access a workspace at the same time without “meeting” each other. This makes a “workspace” different from a “meeting”. In addition to using the Collaborator roles you can also make the Workspace Public and give access through the various Meeting Access settings - for both see below under “Settings”.

**Report** - Create a report against the checklist selected in the workspace settings based on the workspace assets that you choose. You can edit the proposed answers.

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/v1772924118/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Avatour Workspace Report and Asset Selection*

**Map** - For assets with GPS meta data show the location on the map / satellite image.

**Meetings** - Hosts and Collaborator Editors can organise meetings in the workspace

**Settings**

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/v1772387752/avatour-screenshot-workspace-settings_llcei3.png) *Avatour Settings - Workspace View*

**(1) Workspace Settings**

<u>Report Template</u> - select a checklist template against which our AI will report based on the chosen workspace assets (see also above Report)

<u>Enable Notifications</u> - Get daily digest emails to notify collaborators when Issues and Actions of Notes change status (for example, In Progress → Resolved).

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/v1772804314/Screenshot_2026-03-05_140654_bjk0xk.png) *Email Notifications - Example*

<u>Public Workspace</u> - The workspace is like a website - everybody with the workspace link can view all assets and has direct access to assets via asset links. Direct asset links only work with the Public Workspace setting (Note: Non-collaborators will not see meeting info / join button).

**(2) Meeting Settings**

<u>Authentication required</u> - When enabled, participants need to sign in with their Avatour registered user account (Guest, Host or Admin) to join the meeting.

<u>Allow guest access</u> to workspace assets

<u>Auto-Start Recording</u> and Require consent for recorded meetings

<u>Require host</u> - When enabled, the host must admit each participant to the meeting, and the meeting ends when the host leaves. When disabled, meeting participants can start / join a meeting without a host any time. 

<u>Allow spectator access</u> - When enabled, participants can use the spectator code to join a meeting without a microphone or webcam. Spectators use chat to communicate with others in the meeting.

<u>Password protected meetings</u> - When enabled, participants must enter a password to join the meeting which is defined by the host in the meeting settings.

<u>Show Travel-Savings Question</u> - Asks if Avatour meeting saves travel.

> N.B.: It is of course possible to use the above settings in combination (e.g. not require a host but a password).

### 4.2.2 Assets

Here you manage all your assets (360° / 2D videos / pictures and pdf files). You can up- and download assets, allocate assets to workspaces, share assets with other users on the Avatour platform. You can also rename assets, print / download asset reports, activate face blur and AI summarization. To edit an Asset click on the name or select it.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/v1772360326/avatour-screenshot-main-menu-assets_ky5emz.png) *Avatour Web Console - Main Menu Item Assets*

### 4.2.3 Profile

Here you can manage your profile details like your password.

![Avatour Web Console - Main Menu Item Profile](https://res.cloudinary.com/avatour/image/upload/v1772360324/avatour-screenshot-main-menu-profile_j934va.png) *Avatour Web Console - Main Menu Item Profile*

### 4.2.4 Settings

This menu item is only available to Admin Users. Here you can (1) manage default settings for your account and even look those settings so that other users can not change those settings and (2) adjust some customise some branding elements (e.g. your logo. For more info see [How do I add my company branding to the Avatour experience?](https://avatour.com/support/how-do-i-add-my-company-branding-to-the-avatour-experience)).

![Avatour Web Console - Main Menu Item Settings (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360321/avatour-screenshot-main-menu-settings-1-of-2_fsaatf.png) *Avatour Web Console - Main Menu Item Settings (1 of 2)*

![Avatour Web Console - Main Menu Item Settings (2 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360320/avatour-screenshot-main-menu-settings-2-of-2_qimc09.png) *Avatour Web Console - Main Menu Item Settings (2 of 2)*

### 4.2.5 Account

Here Admin Users can manage your registered users (host, guest, admin) and capture devices (360° cams allocated to your Avatour platform instance).

![Avatour Web Console - Main Menu Item Account (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772803328/avatour-screenshot-main-menu-account-1-of-2_oq5amr.png) *Avatour Web Console - Main Menu Item Account*

### 4.2.6 Analytics

This section gives you information about your meetings and savings.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360315/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Avatour Web Console - Main Menu Item Analytics (1 of 3)*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360313/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Avatour Web Console - Main Menu Item Analytics (2 of 3)*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360312/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Avatour Web Console - Main Menu Item Analytics (3 of 3)*

### 4.2.7 Device Login

Use this section to enter the 6-digit code which is shown on your 360° cam (e.g. when you need to log in again or sometimes it needs refreshing). This is a more convenient way that entering your login credentials through the small keyboard in the 360° cam screen.

![Avatour Web Console - Main Menu Item Device Login](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-device-login_vlymhj.png) *Avatour Web Console - Main Menu Item Device Login*

### 4.2.8 Tutorials

Here you can start tutorials on certain topics.

![Avatour Web Console - Main Menu Item Tutorials](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-tutorials_nr9hme.png) *Avatour Web Console - Main Menu Item Tutorials*

 

## 5. Onsite - **How to use the Avatour Turnkey Kit**{#for-camera-operators}

### 5.1 Avatour Turnkey Kit 3.1 [(Pilot PanoX V2 setup)](https://avatour.com/quickstart-panox-v2) 

Be sure to attach the Ulanzi external battery between the tripod base and extendable stick or mount the camera directly onto the Telesin extendable battery stick. In addition to (1) extending the total battery life from ca. 1 hour (camera battery only) to ca. 3 hours, it will also help (2) to extend the height of the camera setup, (3) add weight to the bottom for better stability and (4) also help to prevent any potential overheating of the camera. We recommend to always use the external batteries right from the start, especially for live meetings. 

*For previous camera models see Kit 2.1:* [*Pilot One setup*](https://avatour.com/quickstart-pilot-one/) *and Kits 3.0* [*Pilot Pano setup*](https://avatour.com/quickstart-labpano-pilot-pano/)*)*

- *Kit 2.1: Connect a USB cable from the battery to the USB-C port of the USB-C hub. Then, connect the camera directly to the hub.*
- *Kits 3.0 / 3.1: Connect a USB cable from the battery to the camera.*
- Kit 3.0 / Pilot Pano cam only: Installing the cooling module (optional accessory):
  - *(1) Remove the Pilot Pano battery by opening the side panel and pulling the battery out*
  - (2) Insert the cooling module where the battery was before
  - *(3) Connect the Ulanzi external battery to the cooling module by USB-A to USB-C cable. This cable would have been packed with the cooling module.*

### 5.2 Connectivity

<u>**Before you start:**</u> For live tours you need to be connected to the internet using (1) a local WiFi or (2) a Mobile Network. You should have at least 10 Mbps Uplink and Downlink bandwidth. This allows enough available bandwidth for the camera to Live Capture stream at our recommended 5 Mbps. You can still stream at lower bandwidths (1-2 Mbps), which works best when you are standing still (see also below e. Best Practices: During a Meeting). To test connectivity speed and quality you can use the following methods:

Test at one location: Any speed checker you might already use (e.g. https://www.speedtest.net/)

**Testing tools from Avatour (recommended):**

1. Test at one location: Open https://avatour.live/test from any device in any browser (should take less than one minute) enter your email address and a short reason for the test - measure at different locations onsite. For evaluation of the results, see [How do I interpret the results of the Avatour Network Test?](https://avatour.com/support/how-do-i-interpret-the-results-of-the-avatour-network-test)
2. Test while walking (better for checking the entire tour!): Network test with our Avatour Host app for smartphones (Android: available,  iOS: exp. Feb. 2024). When logged into the app, select a Workspace and choose “Run Connectivity Test”. Watch the connectivity graph while walking through the site, and confirm your network bandwidth meets our recommended 10 Mbps
3. Test while walking (better for checking the entire tour!): Run a network test with your Avatour 360°camera. Login to the Avatour app from the camera’s home screen and go to the Menu (the three red lines in the top right corner) Settings → Network → Connection Test. Watch the connectivity graph while walking through the site, and confirm your network bandwidth meets our recommended 10 Mbps

**Local Wifi**: 

> **<u>It is highly recommended to connect your camera to a local WiFi network.</u>**

If your IT team requires our device MAC address to be whitelisted, you can find on the Pilot cameras the MAC address here: Settings app (camera home screen) --> About --> scroll down to WiFi Address

**Mobile Network:** For areas outside of local WiFi range, connect the camera to a mobile network

<u>Option A: Use the kit provided hotspot and SIM card</u>

**Kits 3.0 / 3.1**: Place the GlocalMe hotspot in your pocket, or keep it somewhere on your person.

- *Troubleshooting Note*: If your GlocalMe hotspot is displaying the message “Data connection is not enabled”, you should check that the hotspot is configured to use the pre-installed SIM card rather than a Cloud SIM. To confirm this, swipe right to the third screen on the hotspot, choose "SIM Card Manager", and select "SIM Card".
- *Troubleshooting Note*: Please also make sure that “5G network” is enabled in the SIM Card Manager
- *Troubleshooting Note*: If you are still unable to connect to a carrier’s network, confirm that you have the correct APN selected for your region. Review the article [here](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot) to create/manage your hotspot’s APNs.

***Kit 2.1**: Use the hotspot attached by magnet to the extendable stick. You can connect to the hotspot via WiFi or wired ethernet connection (hotspot to USB-C hub)*

It’s recommended to first use the SIM card that is preinstalled in your kit provided hotspot. This is a “global” SIM card working in over 200 countries usually automatically connecting to a locally available mobile network. We can implement Roaming Profiles with preferred mobile network providers per country. After testing further the connectivity and if the connection quality remains poor, we recommend sourcing your own local SIM card from the Mobile Network Operator with the strongest signal at your location(s).

<u>Option B: Use your own equipment</u> - hotspot (smartphone or dedicated hotspot device) and SIM data card

**Important Notes**: 

- Keep the hotspot switched off while connected to your local WiFi network. Once you are out of range of this network, then connect the camera to your SIM data.
- Carry the hotspot with you ideally in your shirt front pocket. Back pockets, e.g. trousers are less ideal because your body will block some of the wifi signal between the hotspot and the 360° camera.
- Mobile Network Operators sometimes limit bandwidth for no obvious reason (“throttling”) to manage their overall network. This can have a negative impact on the Avatour experience. Get in touch with your Avatour CSM or our Support team ([support@avatour.live](mailto:support@avatour.live)) if you think that is happening.
- If using the GlocalMe hotspot, you can find the WiFi name and password by swiping one screen to the left. The first screen that displays can be ignored.

**Low bandwidth situations**

- Record a video of the location ahead of time - for details see [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app) This can then be presented during your meeting.
- The operator or other team members onsite can choose to share their smartphone's camera to live stream the location. This will only require a network upload bandwidth of 0.1 - 0.3 Mbps.

**No connectivity at all** - Recorded video only - see [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

### 5.3 Audio

#### 360° Camera and Operator

In principle, you can connect any bluetooth audio device including your PPE headsets if they support bluetooth.

If you plan to host an Avatour meeting in an outdoor or noisy environment, we recommend connecting the **Shokz headphones** provided in your kit: 

- **Power On/Off**: Hold the “+” button for 3 seconds. You will see a blue LED light when the headset is turned on and a red LED light when the headset is turned off
- **Bluetooth Pairing Mode**: While the headset is turned off, hold the “+” button for 5 seconds. An LED light will flash blue and red when in pairing mode
- **Volume Up/Down**: Use the “+” and “-” buttons to increase or decrease listening volume

If in a quieter environment, you can choose to connect a bluetooth speaker, such as the clip on **NoxGear speaker**:

- **Power On/Off**: Hold the Play/Pause button in the center of the device for 2 seconds
- **Bluetooth Pairing Mode:** Once the device is turned on, it will enter pairing mode (blue and red flashing LEDs). Once paired, it will display a blue LED
- **Volume Up/Down**: Use the “+” and “-” buttons to increase or decrease listening volume

**Kits 3.0 / 3.1:** You can pair/connect any bluetooth device from the camera’s home screen’s Settings app. Go to Settings → Bluetooth.

***Kit 2.1**: In order to pair/connect a bluetooth headset/speaker, you must first have a wired connection between the USB-C hub (with Jabra bluetooth dongle) and the camera. If using the Shokz headset or NoxGear speaker, these will connect as soon as they are turned on.*



#### Other Onsite Participants

Connect to the meeting using your smartphone’s / tablet’s / laptop’s browser, and use any wired or wireless headphones (preferably ones with noise canceling enabled). **Please be aware that each smartphone onsite will take away bandwidth from the 360° camera** and can have a negative impact on the Avatour meeting for all participants! Therefore **we recommend to join in**

- **On-Site Mode** - Join the meeting in On-Site mode when you're physically present at the same location as the 360 camera. On-Site Mode is perfect for users who wish to utilize their phones primarily for detailed close-ups. On-Site Mode mutes the mic and speaker by default to eliminate audio feedback

  ***Screenshot Onsite Mode To Do !!!***

**Important Note**: 

- Make sure that you are muted when not actively speaking
- Have your smartphone connected to a different network than the camera’s network, if possible.



### 5.4 Avatour Camera App

Here are (1) the Top Level, (2) Settings and (3) Network Settings menus.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/v1772918698/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360° Camera App - 3 Menus*

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

## 6. Best Practice Advice

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
