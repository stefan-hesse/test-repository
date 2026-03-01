# Avatour User and Best Practices Guide

## 1. For All Avatour Users {#for-all-avatour-users}

Here are some good starting points to understand Avatour:

1. [Avatour How it Works video](https://avatour.com/how-it-works) 
   This video will give a good overview of the main features.
2. [FAQs](https://avatour.com/faqs) 
   Read our Frequently Asked Questions
3. [Glossary](https://avatour.com/glossary) 
   Here you find the major Avatour Terms
4. Website
   Have a look at the [Avatour Features](https://avatour.com/features) and also at the dedicated pages on Use Cases and Industries especially relevent to you.



## 2. Avatour User Types

### 2.1 Users not needing to be a Registered User

#### 2.1.1 Meeting Participant 

Anyone who joins an Avatour meeting. There is currently a limitation of 20 participants in any meeting.

#### 2.1.2 Spectator

Meeting participants who have limited feature access. In a meeting, Spectators are unable to display their webcam feed, use their device's microphone, or use the Present functionality. Spectators are also prevented from playing/pausing Assets and capturing Snapshots. There is currently a limitation of 10 spectators in any meeting bringing the total number in a meeting to a maximum of 30.

### 2.2 Registered Users

Registered Users have registered with their email address and have established a password.

#### 2.2.1 Guest User (free)

This user only has access to view Assets within a Workspace they have been added to as Viewer Collaborator. When Single-Sign-On (SSO) is activated for an Avatour customer (domain) Guest accounts are automatically created when logging in to Avatour with the customer domain email account. 

#### 2.2.2 Licensed Users (with access to the Web Console)

**Host User** - This is the main licensed user type and enables hosting Live Capture video, uploading Quick Captures, and creating Workspaces. Host users have a login to access the Host Dashboard and the Operator App on the 360° cam. You must be a Host or Admin to be added as an Editor Collaborator in a Workspace.

**Admin User** - These users have host feature access and can manage all aspects of the Avatour account. Additional Admin privileges include:

- Account Assets: View all assets that have been uploaded by all Host users in your account. This tab is seen within the "Assets" section of the Host Dashboard
- Settings: Decide if all meetings by default do not require a Host to be present, or if the Igloo projection feature is enabled. If you have requested a custom domain, Admins may also edit the Host Dashboard and meeting room branding images.
- User Management: Create new Host users, and upgrade Guest users to Host. Deleting users (Admin users have to be changed to Host User before they can be deleted / removed. When deleting a user one can transfer the assets of that Host User to another Host / Admin user.
- View all Host Analytics: View all account host's meeting analytics



## 3. For Remote Meeting Participants and Workspace Visitors {#for-remote-meeting-participants-and-workspace-visitors}

### 3.1 How to Join an Avatour meeting and Visit an Avatour Workspace {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### Any "Flat Screen" Device with a Web Browser {#any-flat-screen}
You can join from any desktop/laptop computer, smartphone, or tablet. Simply open your preferred browser, navigate to [https://avatour.live/join](https://avatour.live/join), and type in your name and the meeting code. If the owner of the meeting has sent an invitation that includes an Avatour meeting join link (ex: https://avatour.live/join?s=xxxxx), the meeting code will be auto-populated once you open the link. 

> **Tip 1:** Sometimes the camera in Avatour is blocked when you have been in a Teams call before. Best solution in that case is to stop Teams running in the background and to exit and re-join the Avatour meeting.

> **Tip 2:** Do NOT use the Avatour iOS / Android apps. These are only needed if you want to stream Avatour live meetings with an Insta360 cam as those cams can not directly run our live 360° software and need the “help” of a smartphone!

For visiting a workspace (without incurring a meeting) you will need to have the link to the workspace and depending on the workspace settings you need to login as a registered Avtour User.  

#### VR Headset {#vr-headset}
You can join a meeting and visit a workspace from a range of compatible Meta and Pico headsets. To do this: 

1. Install our Avatour app from your respective VR store app: [How to install Avatour VR app](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Load our app and input the meeting code or select a Workspace to join a meeting. For more information on how to use our VR app, see our Knowledge Base article [here](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Meeting and Workspace Collaboration Tools {#meeting-tools}

You can access Assets and collaborate in Meetings (synchronously = together with other meeting participants, is like in any other Video Conference) and in Workspaces (asynchronously, 24/7). The collaboration tools are very similar in both but there are some differences due to the difference collaboration context (sync versus async).

Below are from left to right short explanations of the above meeting menu items. For more details see also [What meeting tools are available to remote guests on the web?](https://avatour.com/support/what-meeting-tools-are-available-to-remote-guests-on-the-web)

Here is an example of a view in an Avatour Meeting showing in the left side pane the Assets in the Workspace in which the Meeting happens, the Canvas in the middle (blank - here Assets can be shown), and in the right side pane the Meeting Participants.

![Avatour Meeting UI with Assets Panel, blank Canvas and Participants Panel](https://res.cloudinary.com/avatour/image/upload/v1772362400/avatour-screenshot-meeting-assets-blank-participants_pugprq.png) *Avatour Meeting with Assets Panel (left), blank Canvas (center) and Participants Panel (right)*

Here is an example of a view in a Workspace showing in the left side pane the again the Assets in that Workspace in which the Meeting happens, the Canvas in the middle (blank - here Assets can be shown), and in the right side pane the Meetings schedule.

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Avatour Workspace with Assets Panel (left), blank Canvas (center) and Meetings Panel (right)*

We will explain the workspace structure and bottom menu items further below.

Coming back to Meetings: Here is the bottom menu and in the following are explanations of each menu item from left to right starting with Assets.

![Avatour Meeting Bottom Menu](https://res.cloudinary.com/avatour/image/upload/v1772300383/avatour-screenshot-meeting-bottom-menu_bflaor.png) *Avatour Meeting Bottom Menu*

**Assets** - Files in the workspace that can be reviewed with all participants in the meeting. This includes recorded videos, images/snapshots, and PDFs. Hosts and Collaborator Editors can up- and download assets.

**Chat** - By clicking the chat bubble, you can send messages to all meeting participants.

**Camera** - Turn off/on 

**Microphone** - Mute/unmute

**Present** - see the separate section on the Present menu below

**Host Tools** - (for the meeting host only): 

- **Lock Focus** - lock the view for all participants to the host view - see also Meeting Tools.
- **Mute All** - mute all participants

**Enable Full Screen** - Puts the meeting tab in full screen

**Exit the Meeting** - leave the meeting.

**Start Recording** - When enabled in the workspace settings you can record an Avatour meeting. The recording will be available in your assets and also automatically allocated to the workspace in which the meeting happened.

**Geo Location** - For assets and live streaming with GPS open/close the map pane. In the map you will see the route of the video and you can click on a point in that route which will take you exactls to the moment in the video.

**Participants** - Open/close the participants pane.

**Meeting Info** - This section gives you information about your meeting (e.g. the meeting code and invite link to the meeting). From here you can also access the related Online Tutorial.

> Tip: Send the meeting link or add it to any calendar item to invite meeting participants.

***Add picture meeting tutorial***

While in a meeting you can also start the meeting Tutorial from the Info section.

**Settings** - Adjust your language, audio, and video settings. For live 360° video meetings you can use "<u>Show Bitrate</u>" wich will show you in the upper left corner of the canvas the connectivity stats for the live 360° video stream (1. Upload Bandwidth Onsite, 2. Your Download Capacity, 3. Your Download Speed). This can be very helpful to analyze any potential connectivity issues (is it onsite or with the remote participant?)



**Present Menu**

**Camera** - Allows you to share your webcam or smartphone/tablet camera. Can also be used as Video-in-Video while presenting an asset or in a live 360° video meeting, e.g. to show a detail on site (although going close with the 360° cam also gives a good detailed view, e.g. of a barcode, small print on a lable).

**Desktop** - Allows you to share your desktop’s screen

**Asset** - Show one of the assets from the asset section - see above. While presenting an asset the Asset menu will appear - see next point.



**Present Asset Menu** 

There are slight differences in the Menu Items when presenting an Asset in a <u>Meeting</u> and when presenting in a <u>Workspace</u> (async).

Here are the tools and menu items available when <u>presenting an Asset in a Meeting</u> - explained from left to right.

![Avatour Menu while Presenting an Asset in a Meeting](https://res.cloudinary.com/avatour/image/upload/v1772303706/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Avatour Menu when presenting an Asset in a Meeting*

**Snapshot** - Take a 360° or 2D picture within a Live Capture or a presented Asset. All snapshots can be saved to the Assets in the meeting/workspace - see also Meeting Tools. A SuperFreeze 360° snapshot has a higher resolution (ca. 6k) and will pause the live stream for some seconds.

**Spotlight** - Available during a live 360 capture or if an Asset is being presented. This creates a pointer visible by all meeting participants and the camera operator, enabling you to draw the group’s attention to a specific object or area on screen.

**Show/Hide Point-of-View (POV)** - This option displays each participants focus - Point of View - in the 360° video - recorded or live (circles with the participant’s name underneath)

**Recorded video only!?**

**Notes** - create notes (= dialog boxes) at certain positions in snapshots and videos. Any meeting participant can create a note. Only the note creator can edit and delete a note. When creating a note, you can set a Type: Observation, Issue, Action or Recommendation (the latter three can only be done by Hosts, Avatour Collaborator Viewers and Editors). 

![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/v1772374822/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Avatour Note and Note Filters*

This makes it clear whether a note is informational or requires follow-up. In the timeline of a video notes are anchored to the precise moment in the capture.

- Core collaborators (Host, Avatour Collaborator Viewers and Editors) can update a note’s Status as work moves forward: Open → In Progress → Resolved. Topics are also highlighted under the timeline of the video. Topics are AI generated based on the audio of an asset and can be initiated during Upload from the Avatour cam app or in the Assets section in the Web Console.
- Share links to notes and specific scenes (=viewangles) in a video / snapshot either by email or directly copy the link and use/embed wherever you want.

**Side Panel with Notes, Executive Summary, Topics etc. and Reports** - show all notes and topics of an asset in a side panel (click on the list icon next to the note icon in the above menu). Click in the side panel in the notes / topics to get to the note / topic in the video. In the Notes panel you can apply Note filters

![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Avatour Executive Summary while presenting an Asset in a Meeting*



![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Avatour Topics while presenting an Asset in a Meeting*

You can also print a report with all notes, topics etc. even a full transciption for an asset and select what to include:

![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/v1772376570/avatour-screenshot-asset-report-element-selection_ud8c5k.png)

**Share Link** - Share links to notes and specific scenes (=viewangles) in a video / snapshot either by email or directly copy the link and use/embed wherever you want.

***Add Closed Caption***

And Here are the collaboration tools and menu items available when presenting an Asset in a <u>Workspace</u>. Most tools are like in a meeting but some are missing as these do only make sense when others are present (POV and Spotlight) and some are only available in workspaces - mainly video opertions related, which are explained below.

![Avatour Menu while Presenting an Asset outside a meeting, e.g. when visiting a workspace](https://res.cloudinary.com/avatour/image/upload/v1772303705/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Avatour Menu when presenting an Asset in a Workspace*

**10 seconds back and forth** - ...

**faster playback seconds back and forth** - ...

**Trimming a video (scissors)** - ...



## 4. For Host and Admin Users - Avatour Web Console{#for-registered-users}

When you log in to the Avatour Web Console you will see on the left hand side the below menu pane.

### 4.1 Web Console - Overview Main Menu

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/w_0.5/v1772366766/avatour-screenshot-main-menu_qwpthq.png)

 *Avatour Web Console - Main Menu*

**Workspaces** - Workspaces can be set up for many purposes (e.g. sites, projects, customer, supplier) and are organisational units helping you to work efficiently in a controlled environment comprising of the following elements.

Please watch this video to see how to keep assets, meetings and collaborators organized (e.g. by project, site, customer, supplier) and the various workspace settings. And here is more information on Managing access to Avatour meetings

**Assets** - All your assets (360° videos / pictures, pdfs…) in one place under My Assets. Admin users can see all Account Assets across all host users. Shared Assets are those which hosts share with all other users on the Avatour platform. Here you can rename assets, activate face blur and generate topics.

**Profile** - Manage your language and reset your password.

**Analytics** - Get insight about sessions and usage

**Settings** - For Admin Users only. Manage some general settings and customize your branding.

**Account** - For Admin Users only. Manage users and devices (= 360° cams).

**Device Login** - Enter here the number shown on the Avatour app on your 360° cam to log in as user on the 360° cam. You can also log in on your 360° cam with your Avatour host account email and password but simply entering the device code on the Avatour Web Console might be easier.

**Sign out** of your account.

 

### 4.2 Web Console - Details by Menu Item

### Workspaces

Workspaces can be set up for many purposes (e.g. sites, projects, customer, supplier) and are organisational units helping you to work efficiently in a controlled environment. 

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/v1772360323/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Main Menu Item Workspaces*

?? Please watch this video to see how to keep assets, meetings and collaborators organized (e.g. by project, site, customer, supplier) and the various workspace settings. 

Here is a view of the structure in a workspace.

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Avatour Workspace with Assets Panel (left), blank Canvas (center) and Meetings Panel (right)*

Each workspace comprises of the following elements:

**Assets** - Manage assets allocated to that workspace 

**Collaborators** - Manage Access to the Workspace

- **Viewer** - can view assets in the workspace. Adding a Collaborator Viewer will send an invitation to become a registered Avatour Guest user.
- **Editor** - have the same right as the Host (owner of the workspace) and with this full workspace control. Adding a Collaborator Viewer will send an invitation to become a registered Avatour Host user.

N.B.: Several users can access a workspace at the same time without “meeting” each other. This makes a “workspace” different from a “meeting”. In addition to using the Collaborator roles you can also make the Workspace Public and give access through the various Meeting Access settings - for both see below under “Settings”.

**Report** - Create a report against the checklist selected in the workspace settings based on the workspace assets that you choose:

![Avatour Workspace Report Asset Selection](https://res.cloudinary.com/avatour/image/upload/w_0.5/v1772378496/avatour-screenshot-workspace-report-asset-selection_jmojyu.png) 

*Avatour Workspace Report Asset Selection*

**Map** - For assets with GPS meta data show the location on the map / satellite image.

**Meetings** - Hosts and Collaborator Editors can organise meetings in the workspace

**Settings** for Workspace

image-20260213-105313.png

- Report Template - select a checklist template against which our AI will report based on the chosen workspace assets.

- Enable Notifications - Get daily digest emails to notify collaborators when Issues and Actions of Notes change status (for example, In Progress → Resolved).

- image-20260125-104127.png

- Public Workspace - The workspace is like a website - everybody with the workspace link can view all assets and has direct access to assets via asset links. Direct asset links only work with the Public Workspace setting (Note: Non-collaborators will not see meeting info / join button).

- Meeting Settings

  - Authentication required - When enabled, participants need to sign in with their Avatour registered user account (Guest, Host or Admin) to join the meeting.
  - Allow guest access to workspace assets
  - Auto-Start Recording and Require consent for recorded meetings
  - Require host - When enabled, the host must admit each participant to the meeting, and the meeting ends when the host leaves. When disabled, meeting participants can start / join a meeting without a host any time. 
  - Allow spectator access - When enabled, participants can use the spectator code to join a meeting without a microphone or webcam. Spectators use chat to communicate with others in the meeting.
  - Password protected meetings - When enabled, participants must enter a password to join the meeting which is defined by the host in the meeting settings.
  - Show Travel-Savings QuestionTravel-

  N.B.: It is of course possible to use the above settings in combination (e.g. do not require a host but a password).

### Assets

Here you manage all your assets (360° / 2D videos / pictures and pdf files). You can up- and download assets, allocate assets to workspaces, share assets with other users on the Avatour platform. You can also rename assets, acivate face blur and AI summarization when editing an asset.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/v1772360326/avatour-screenshot-main-menu-assets_ky5emz.png) *Avatour Web Console - Main Menu Item Assets*

### Profile

Here you can manage your profile details like your password.

![Avatour Web Console - Main Menu Item Profile](https://res.cloudinary.com/avatour/image/upload/v1772360324/avatour-screenshot-main-menu-profile_j934va.png) *Avatour Web Console - Main Menu Item Profile*

### Settings

This menu item is only available to Admin Users. Here you can (1) manage default settings for your account and even look those settings so that other users can not change those settings and (2) adjust some customise some branding elements (e.g. your logo. For more info see How do I add my company branding to the Avatour experience?).

![Avatour Web Console - Main Menu Item Settings (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360321/avatour-screenshot-main-menu-settings-1-of-2_fsaatf.png) *Avatour Web Console - Main Menu Item Settings (1 of 2)*

![Avatour Web Console - Main Menu Item Settings (2 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360320/avatour-screenshot-main-menu-settings-2-of-2_qimc09.png) *Avatour Web Console - Main Menu Item Settings (2 of 2)*

### Account

Here Admin Users can manage your users and devices (360° cams allocted to your Avatour platform instance).

![Avatour Web Console - Main Menu Item Account (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360318/avatour-screenshot-main-menu-account-1-of-2_oq5amr.png) *Avatour Web Console - Main Menu Item Account (1 of 2)*

![Avatour Web Console - Main Menu Item Account (2 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360316/avatour-screenshot-main-menu-account-2-of-2_udgyjz.png) *Avatour Web Console - Main Menu Item Account (2 of 2)*

### Analytics

This section gives you information about your meetings and savings.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360315/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Avatour Web Console - Main Menu Item Analytics (1 of 3)*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360313/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Avatour Web Console - Main Menu Item Analytics (2 of 3)*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360312/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Avatour Web Console - Main Menu Item Analytics (3 of 3)*

### Device Login

Use this section to enter the 6-digit code which is shown on your 360° cam (e.g. when you need to log in again or sometimes it needs refreshing). This is a more convenient way that entering your login credentials through the small keyboard in the 360° cam screen.

![Avatour Web Console - Main Menu Item Device Login](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-device-login_vlymhj.png) *Avatour Web Console - Main Menu Item Device Login*

### Tutorials

Here you can start tutorials on certain topics.

![Avatour Web Console - Main Menu Item Tutorials](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-tutorials_nr9hme.png) *Avatour Web Console - Main Menu Item Tutorials*

 

## 5. For Camera Operators {#for-camera-operators}

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

- If you notice some areas have little to no bandwidth, it is best to take images or a recording. These can then be presented during the meeting for remote participants to review. You can follow the guide here that explains our Quick Capture for recording and uploading videos/images: How do you record and upload 360 videos with the Avatour App?

- If you have remote participants joining the meeting who have not used Avatour before, provide them with a short summary of the platform, its functionality (360 live video, assets, snapshots, annotations, spotlight) and the meeting tools.

- You can start in another video conferencing solution (e.g. Teams, Zoom, Google Meet) but before moving over to Avatour, completely close the other video conference application. In some cases, these other applications will prioritize your device’s microphone/speakers/webcam, causing them to be disabled for Avatour. Additionally, do NOT run Avatour AND another video conference at the same time as this will reduce available bandwidth.

- If you are planning to use the 360 camera in a high temperature environment, it’s recommended to use the cooling module (Pilot Pano only). This will help reduce the chances of the camera overheating and shutting down automatically.

### When Operating the Cam Onsite for a 360° Video Live Meeting

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
