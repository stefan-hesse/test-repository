# Avatour User and Best Practices Guide

## 1. Pour tous les utilisateurs d'Avatour {#for-all-avatour-users}

Si vous êtes nouveau sur Avatour, les ressources suivantes offrent une introduction utile à la plateforme et à ses fonctionnalités :

1. [Vidéo Avatour Comment ça marche](https://avatour.com/how-it-works)  
Un bref aperçu des principales fonctionnalités d'Avatour et de la façon dont la plateforme permet une collaboration à distance immersive.
2. [FAQ](https://avatour.com/faqs)  
Réponses aux questions fréquemment posées.
3. [Glossaire](https://avatour.com/glossary)  
Définitions des termes et concepts clés d'Avatour fréquemment utilisés.
4. Site web  
Consultez notamment la page [Fonctionnalités d'Avatour](https://avatour.com/features) ainsi que les sections dédiées aux Cas d'utilisation et aux Industries pour découvrir comment Avatour peut répondre à vos besoins spécifiques.## 2. Types d'utilisateurs Avatour  {#avatour-user-types}

### 2.1 Participants aux réunions (aucun compte requis)
Les utilisateurs peuvent rejoindre la réunion sans créer de compte Avatour.
Exception : Si l'hôte a restreint la réunion aux utilisateurs enregistrés — par exemple, pour permettre uniquement aux employés internes de se connecter via l'authentification unique (SSO) — l'invitation du calendrier indiquera que les participants doivent se connecter pour s'authentifier.

Les utilisateurs accèdent à la réunion comme suit :

- Reçoivent une invitation de calendrier de la part de l'hôte.
- Utilisent le lien de réunion dans l'invitation pour rejoindre.
- Saisissent un mot de passe de réunion si l'hôte en a activé un.
- Les participants peuvent rejoindre sans compte Avatour, sauf si la réunion est restreinte et nécessite une connexion pour s'authentifier.

#### 2.1.1 Participant 

- Peut rejoindre et interagir pleinement (webcam, microphone, chat et fonctionnalité Présenter).
- Maximum de 20 participants interactifs par réunion.

#### 2.1.2 Spectateur

- Peut visualiser la réunion et participer uniquement via le chat.
- Ne peut pas partager de vidéo, utiliser un microphone, présenter, lire/mettre en pause les Assets, ni capturer des Snapshots.
- Maximum de 10 Spectateurs par réunion.
- Avec les Participants, une réunion peut accueillir jusqu'à 30 participants.

### 2.2 Utilisateurs enregistrés

Les Utilisateurs enregistrés possèdent un compte Avatour. Les comptes sont créés de l'une des manières suivantes :

- **Invité par un Admin :** Lors de l'intégration, Avatour configure un **tenant dédié** pour l'organisation et crée un ou plusieurs **comptes Admin**. Les Admins peuvent ensuite **inviter des utilisateurs** au sein de l'organisation et les assigner à des **groupes**, qui définissent leur rôle sur la plateforme (Guest, Host ou Admin). Les utilisateurs invités reçoivent un **lien d'inscription** pour finaliser la création du compte et définir un mot de passe.  
- **Invité par un Host :** Les Hosts peuvent ajouter des utilisateurs comme **collaborateurs Editor** à un Workspace. Cela consomme une **licence Host** et garantit que l'utilisateur dispose d'un accès de niveau Host.  
- **Provisionnement automatique SSO (niveau Enterprise/Business uniquement) :** Les comptes peuvent être automatiquement créés par l'IdP. Par défaut, les comptes provisionnés par SSO sont ajoutés au **groupe Guest**, sauf si cela est remplacé via les **mappages de groupes SAML**. Les Admins peuvent toujours inviter des utilisateurs et assigner l'appartenance aux groupes directement même lorsque le SSO est activé.

**Résumé :**  

Les utilisateurs enregistrés et leur appartenance aux groupes peuvent être gérés de plusieurs manières :

- **Gestion par Admin :** Un Admin dans la console Avatour peut créer des utilisateurs et les assigner à des groupes, qui définissent leur rôle sur la plateforme (Guest, Host ou Admin).  
- **Provisionnement SSO :** Pour les clients de niveau Enterprise ou Business avec SSO activé, l'IdP peut automatiquement provisionner les comptes et assigner l'appartenance aux groupes, ce qui définit le rôle de l'utilisateur sur la plateforme.  
- **Utilisateurs invités par un Host :** Les Hosts peuvent inviter d'autres utilisateurs comme collaborateurs Editor sur des Workspaces spécifiques. L'attribution du rôle de collaborateur Editor consomme une licence Host.

**Meilleure pratique recommandée (Clients Enterprise) :**  
Pour les organisations prévoyant un grand nombre d'utilisateurs ayant besoin d'accéder à Avatour, il est recommandé d'**intégrer l'authentification unique (SSO)** et de gérer les utilisateurs et les appartenances aux groupes depuis l'**IdP**. Cette approche simplifie le provisionnement des comptes, l'attribution des groupes et la gestion des licences, réduisant la charge administrative et assurant un contrôle d'accès cohérent.

#### 2.2.1 Utilisateurs Guest

- Ajoutés au **groupe Guest**.  
- Peuvent **visualiser les Assets** dans les Workspaces où ils ont été ajoutés comme **collaborateurs Viewer**.  
- Ne peuvent pas créer de workspaces, héberger de réunions ni téléverser de contenu.  
- Les comptes Guest provisionnés par SSO **s'authentifient via l'IdP** ; aucun mot de passe géré par Avatour n'est requis.

---

#### 2.2.2 Utilisateurs sous licence (Accès à la console Web)

##### Utilisateurs Host (Groupe : Host)

- Peuvent créer/gérer des Workspaces, inviter des collaborateurs dans un workspace, **héberger des réunions en direct**, téléverser des **Quick Captures**.  
- Ont accès au **Host Dashboard** et à l'**Operator App** sur les caméras 360° compatibles.  

##### Utilisateurs Admin (Groupe : Admin)

- Incluent toutes les capacités Host plus l'administration complète du compte.

**Les privilèges Admin supplémentaires incluent :**

**Gestion des comptes**  

- Créer de nouveaux utilisateurs et les assigner à des groupes.
- Réinitialiser les mots de passe lorsqu'ils sont gérés par Avatour (non applicable lorsque le SSO est activé). 
- Promouvoir les utilisateurs Guest en Host.  
- Désactiver des utilisateurs (les comptes Admin doivent d'abord être convertis en Host avant suppression).  
- Transférer les assets d'un utilisateur Host à un autre lors de la suppression.

**Paramètres**  

- Configurer les **paramètres de sécurité à l'échelle de l'organisation** pour les assets, workspaces et réunions hébergés sur la plateforme (par ex., si un Host doit être présent pour démarrer une réunion, si les visages doivent être floutés sur toutes les vidéos téléversées sur la plateforme).  
- Activer ou désactiver les **fonctionnalités IA** ou l'**enregistrement**.  
- Appliquer l'image de marque de l'entreprise de manière cohérente sur la plateforme si un **domaine personnalisé** est configuré.
  

**Assets et Analytiques** 
 
- Visualiser tous les Assets téléversés par n'importe quel utilisateur de l'organisation.  
- Examiner l'utilisation de la plateforme à travers l'organisation.

---

#### 2.2.3 Permissions des collaborateurs de Workspace

Les permissions de Workspace définissent ce qu'un utilisateur peut faire **au sein d'un Workspace spécifique**. Celles-ci sont distinctes de l'appartenance aux groupes au niveau de la plateforme (Guest, Host, Admin).

- **Collaborateur Editor :** Les utilisateurs avec cette permission peuvent :
  - Gérer les Assets (téléverser, supprimer, flouter les visages, générer des résumés)  
  - Gérer les paramètres de réunion (activer/désactiver l'enregistrement, autoriser ou retirer des participants)  
  - Planifier et héberger des réunions en direct  
  - Générer des rapports basés sur des modèles prédéfinis  
  - Ajouter ou retirer des collaborateurs du Workspace  

- **Collaborateur Viewer :** Les utilisateurs avec cette permission ont un accès en lecture seule aux Assets du Workspace. Ils **ne peuvent pas modifier les Assets, gérer les réunions, ni gérer les collaborateurs**, mais ils **peuvent créer des Notes sur les Assets**.## 3. Pour les participants aux réunions à distance et les visiteurs d'espace de travail {#for-remote-meeting-participants-and-workspace-visitors}

Avatour permet aux utilisateurs de collaborer de deux manières principales :

- **Rejoindre une réunion Avatour (Collaboration synchrone) :**  
  Vous pouvez recevoir une **invitation de calendrier** pour rejoindre une réunion Avatour. Pendant la réunion, les participants peuvent effectuer une **visite de site à distance en direct** ou examiner des ressources de manière synchrone ensemble.

- **Visiter un espace de travail (Collaboration asynchrone) :**  
  Vous pouvez également être invité en tant que **collaborateur dans un espace de travail** pour examiner des ressources **de manière asynchrone** (selon votre propre emploi du temps).

### 3.1 Comment rejoindre une réunion Avatour et visiter un espace de travail Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Tout appareil « écran plat » avec un navigateur web {#any-flat-screen}
Vous pouvez rejoindre une réunion Avatour depuis **n'importe quel ordinateur de bureau ou portable, smartphone ou tablette** en utilisant un navigateur web.  

##### Rejoindre une réunion Avatour

> **Remarque :** Rejoindre une réunion Avatour nécessite que vous **accordiez les autorisations du microphone**. Veuillez accepter toute demande d'autorisation de votre navigateur.

1. **Via une invitation de calendrier (recommandé) :**  
   - Vous recevrez généralement une **invitation de calendrier** avec un **lien de connexion direct** (par exemple : `https://avatour.live/join?s=xxxxx`).  
   - Cliquer sur le lien remplira automatiquement le **code de réunion à 5 caractères** et vous amènera à la réunion.
   - **Authentification requise :** Certaines réunions sont réservées aux utilisateurs enregistrés. Dans ce cas, l'invitation indiquera que vous devez **vous connecter pour accéder à la réunion**.  
   - **Réunions protégées par mot de passe :** Certaines réunions peuvent nécessiter un mot de passe. Dans ce cas, l'invitation inclura le mot de passe que vous devez entrer pour rejoindre.

2. **Via le code de réunion :**  
   - Si l'hôte partage séparément un **code de réunion à 5 caractères**, rendez-vous sur [https://avatour.live/join](https://avatour.live/join), entrez votre **nom** et le **code de réunion**, et rejoignez la réunion.  
   - Si la réunion est **protégée par mot de passe**, entrez le mot de passe fourni par l'hôte.  
   - Si la réunion nécessite une **authentification**, vous devrez **vous connecter avec votre compte Avatour** avant de rejoindre.

> **Astuce 1 :** Si votre caméra ou microphone ne fonctionne pas, il peut être utilisé par une autre application (par exemple, Microsoft Teams ou Zoom). Fermez toutes les applications qui pourraient utiliser votre caméra ou microphone, puis quittez et rejoignez à nouveau la réunion Avatour.  

> **Astuce 2 :** Si vous ne parvenez toujours pas à rejoindre la réunion, exécutez ce test : [https://avatour.live/test](https://avatour.live/test).  
> Le test peut identifier si votre **pare-feu d'entreprise ou réseau** bloque l'accès, et fournira des informations pour guider les discussions avec votre équipe informatique.  

> **Astuce 3 :** N'utilisez **pas** les applications Avatour iOS ou Android pour rejoindre les réunions. Ces applications ne sont requises que lors de la **diffusion d'une réunion en direct depuis une caméra Insta360**, car ces caméras ne peuvent pas exécuter directement le logiciel Avatour 360° et nécessitent un smartphone pour les assister.

##### Visiter un espace de travail Avatour (sans rejoindre une réunion Avatour)

Vous pouvez accéder à un espace de travail des manières suivantes :

- **Espace de travail public :**  
  Si l'espace de travail est public, le lien peut être accédé directement — aucune connexion requise.

- **Espace de travail restreint :**  
  Si l'espace de travail est restreint, vous devez être ajouté en tant que **collaborateur** avec des autorisations d'**Éditeur** ou de **Lecteur**.

  1. Lorsque vous êtes ajouté en tant que collaborateur, vous recevrez une **notification par e-mail** avec un lien vers l'espace de travail.
  2. Cliquez sur le lien dans l'e-mail pour ouvrir l'espace de travail. Si vous n'êtes pas déjà connecté, vous serez invité à **vous connecter ou à compléter votre inscription**.
  3. Une fois connecté, l'espace de travail s'ouvrira automatiquement.

  Alternativement, vous pouvez vous connecter sur [https://avatour.live/login](https://avatour.live/login) et accéder à l'espace de travail depuis votre **liste d'espaces de travail**.

#### 3.1.2 Casque VR {#vr-headset}
Vous pouvez rejoindre une réunion et visiter un espace de travail depuis une gamme de casques Meta et Pico compatibles. Pour ce faire : 

1. Installez notre application Avatour depuis votre boutique d'applications VR respective : [Comment installer l'application Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Chargez notre application et entrez le code de réunion ou sélectionnez un espace de travail pour rejoindre une réunion. Pour plus d'informations sur l'utilisation de notre application VR, consultez notre article de la base de connaissances [ici](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Outils de collaboration pour les réunions et les espaces de travail {#meeting-tools}

Avatour permet la collaboration dans deux contextes principaux :

1. **Réunions (synchrone) :** Collaborez en temps réel avec d'autres participants, y compris des visites de site en direct ou l'examen de ressources enregistrées ensemble.  
2. **Espaces de travail (asynchrone) :** Examinez et interagissez avec les ressources selon votre propre emploi du temps, 24h/24 et 7j/7.

Les **outils de collaboration sont essentiellement similaires** entre les réunions et les espaces de travail, avec quelques différences dues au contexte synchrone vs asynchrone.

#### 3.2.1 Disposition de l'interface

L'interface Avatour est organisée autour de trois zones principales :

- **Panneau de gauche** – Ressources de l'espace de travail et outils de support  
- **Canevas central** – Zone de visualisation principale pour la vidéo en direct ou les ressources  
- **Panneau de droite** – Informations contextuelles, telles que les participants, les réunions ou le chat  

La plupart des interactions sont initiées depuis le **menu inférieur**.  
Cliquer sur une option de menu ouvre un **panneau latéral** sur le côté gauche ou droit de l'écran, tandis que le **canevas central** reste la zone de visualisation principale.

---
#### 3.2.2 Exemple de vue de réunion

Voici un exemple de vue dans une réunion Avatour :

![Interface de réunion Avatour avec panneau des ressources, canevas vide et panneau des participants](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Réunion Avatour avec panneau des ressources (gauche), canevas (centre) et panneau des participants (droite)*

---

#### 3.2.3 Exemple de vue d'espace de travail

Voici un exemple de vue d'espace de travail :

![Espace de travail Avatour avec panneau des ressources, canevas vide et panneau des réunions](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espace de travail Avatour avec panneau des ressources (gauche), canevas (centre) et panneau des réunions (droite)*

---

#### 3.2.4 Aperçu du menu inférieur

Le menu inférieur donne accès aux contrôles et panneaux principaux de l'interface :

**Menu inférieur de réunion**  

![Menu inférieur de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu inférieur de réunion Avatour*

- **Ressources** – Examinez les fichiers de l'espace de travail, y compris les vidéos enregistrées, les images, les captures et les PDF. 
- **Chat** – Envoyez des messages à tous les participants de la réunion.  
- **Caméra** – Activez ou désactivez votre webcam.  
- **Microphone** – Activez ou désactivez votre micro.  
- **Présenter** – Présentez une ressource, un bureau ou un flux webcam (voir la section Présenter ci-dessous).  
- **Outils de l'hôte** (hôtes uniquement) :  
  - **Verrouiller la mise au point** – Verrouillez la vue pour tous les participants.  
  - **Couper le son de tous** – Coupez le son de tous les participants.  
- **Activer le plein écran** – Mettez l'onglet de la réunion en plein écran.  
- **Quitter la réunion** – Quittez la réunion.  
- **Démarrer l'enregistrement** – Utilisez ce bouton pour démarrer et arrêter l'enregistrement manuellement pendant une réunion. Alternativement, les réunions peuvent être enregistrées automatiquement si le **démarrage automatique de l'enregistrement** est activé dans les paramètres de l'espace de travail. Dans les deux cas, les enregistrements sont sauvegardés dans les ressources de l'espace de travail.
- **Carte** – Ouvrez ou fermez le panneau de carte pour les ressources avec une trace GPS. Cliquer sur un emplacement vous amène au point exact dans la vidéo. La carte se met à jour en direct pendant la lecture de la vidéo.
- **Participants** – Ouvrez ou fermez le panneau des participants.  
- **Infos de la réunion** – Consultez le code de réunion, le lien d'invitation et accédez aux tutoriels associés.  

![Infos de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panneau latéral d'informations de réunion Avatour*

- **Paramètres** – Ajustez les paramètres de langue, audio et vidéo. Pour les réunions vidéo 360° en direct, utilisez **Afficher le débit binaire** pour surveiller les statistiques de connectivité.

> Astuce : Envoyez le lien de la réunion ou ajoutez-le à un élément de calendrier pour inviter des participants.

---

##### Menu Présenter

L'option **Présenter** dans le menu inférieur de la réunion vous permet de partager du contenu avec tous les participants.

- **Caméra** – Partagez la caméra de votre smartphone/tablette. Cela peut également être utilisé pendant une réunion vidéo 360° en direct pour superposer une vue secondaire pour des gros plans ou des détails spécifiques. 
- **Bureau** – Partagez l'écran de votre bureau avec tous les participants.  
- **Ressource** – Présentez une ressource de l'espace de travail. Sélectionner une ressource ouvre la **barre d'outils de ressource**, qui fournit des contrôles de lecture et des outils de collaboration spécifiques à la ressource présentée.

##### Barre d'outils de ressource (Réunion)

Lors de la présentation d'une ressource dans une réunion, la **barre d'outils de ressource** apparaît au-dessus du canevas. Voici les outils et éléments de menu disponibles lors de la <u>présentation d'une ressource dans une réunion</u> - expliqués de gauche à droite.

![Menu Avatour lors de la présentation d'une ressource dans une réunion](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour lors de la présentation d'une ressource dans une réunion*


- **Chronologie vidéo / Barre de progression** – Affiche la progression de la vidéo avec des notes et des sujets clés extraits de l'audio. Cliquez sur une note ou un sujet pour accéder à ce moment et ouvrir la note. Comprend des contrôles de **lecture / pause**.   
- **Capture** – Capturez une image 360° ou 2D de la ressource.  
- **Projecteur** – Mettez en évidence une zone spécifique pour tous les participants pendant les sessions en direct.  
- **Afficher/Masquer le point de vue (POV)** – Affichez où chaque participant regarde dans la vidéo 360°.  
- **Notes** – Créez des notes ancrées à des moments spécifiques de la ressource. Les notes peuvent être catégorisées (Observation, Problème, Action, Recommandation), suivies par statut (Ouvert → En cours → Résolu), et partagées via des liens directs.  

  ![Note Avatour et filtre de notes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Note Avatour et filtres de notes*

  - **Notes par commande vocale** – Ce sont des espaces réservés générés automatiquement lorsque l'enregistrement détecte des mentions comme « insérer une note », « prendre une note » ou « faire une note ». Ces notes apparaissent sur la chronologie et doivent être **positionnées et finalisées** par l'utilisateur. 

  ![Notes Avatour - Générées par commande vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notes Avatour - Générées par commande vocale*

- **Panneau Notes et résumé** – Ouvre un panneau latéral qui affiche toutes les notes, les sujets clés et un résumé exécutif de la ressource. Cliquer sur un élément vous amène à ce moment dans## 4. Pour les utilisateurs Hôte et Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}

Lorsque vous vous connectez à votre compte utilisateur Avatour, vous accédez à la **Console Web**.  

### 4.1 Console Web - Aperçu du menu principal {#web-console-overview-main-menu}

Sur le côté gauche, vous verrez les éléments de menu suivants :

![Console Web Avatour - Menu Principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu Principal*

- **Espaces de travail** – Organisez efficacement votre contenu. Chaque espace de travail contient des **Ressources**, des **Collaborateurs**, des **Réunions** et des **Paramètres**.  
- **Ressources** – Accédez et gérez toutes vos ressources (vidéos, images, PDF). Les administrateurs peuvent voir toutes les ressources du compte, et les ressources partagées sont visibles par tous les utilisateurs.  
- **Profil** – Gérez votre langue et votre mot de passe.  
- **Analytique** – Suivez l'activité des sessions, l'utilisation des espaces de travail et les indicateurs de ROI.  
- **Paramètres** *(Admin uniquement)* – Configurez les paramètres par défaut des espaces de travail, réunions et ressources dans toute l'organisation. Les administrateurs peuvent également personnaliser l'image de marque (logo, couleurs, arrière-plans).  
- **Compte** *(Admin uniquement)* – Gérez les utilisateurs enregistrés et les caméras 360°.  
- **Connexion appareil** – Entrez le code affiché sur votre caméra 360° pour l'associer à votre compte.  
- **Tutoriels** – Accédez aux tutoriels guidés.  
- **Déconnexion** – Déconnectez-vous de la console.

> Les sections comme Profil, Connexion appareil, Tutoriels et Déconnexion sont explicites et n'ont pas de sous-sections détaillées.

---

### 4.2 Console Web - Détails par élément de menu (avec images) {#web-console-details-by-menu-item}

#### 4.2.1 Espaces de travail

Les espaces de travail sont des unités organisationnelles flexibles qui vous permettent de gérer les ressources, les collaborateurs et les réunions en un seul endroit. Vous pouvez créer un nouvel espace de travail avec le bouton **Nouvel espace de travail** dans le coin supérieur droit.

![Console Web Avatour - Élément de menu principal Espaces de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Élément de menu principal Espaces de travail*

Cliquez sur l'icône de cloche pour voir un résumé de l'activité de l'espace de travail des 7 derniers jours.

![Console Web Avatour - Activités récentes de l'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Activités récentes de l'espace de travail*

À l'intérieur d'un espace de travail :

![Espace de travail Avatour avec panneau Ressources, Canevas vierge et panneau Réunions](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espace de travail avec Ressources (gauche), Canevas (centre), Réunions (droite)*

- **Ressources** – Gérez les fichiers alloués à cet espace de travail.  
- **Collaborateurs** – 
  Contrôlez l'accès aux espaces de travail par 
  - **Lecteur** – Peut voir les ressources. L'invitation crée un utilisateur Invité si nécessaire.  
  - **Éditeur** – Contrôle total de l'espace de travail, mêmes droits qu'un Hôte. L'invitation met à niveau l'utilisateur en Hôte si nécessaire.  
> Plusieurs utilisateurs peuvent accéder à un espace de travail simultanément sans réunion. Les espaces de travail publics et les paramètres d'accès aux réunions offrent un accès alternatif.  
- **Rapport** – Générez un rapport en utilisant un modèle de checklist sur les ressources sélectionnées de l'espace de travail.  

![Rapport d'espace de travail Avatour et sélection de ressources](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Rapport d'espace de travail et sélection de ressources*

- **Carte** – Affichez les emplacements des ressources avec GPS sur une carte.  
- **Réunions** – Organisez des réunions dans l'espace de travail.  
- **Paramètres** – Configurez les paramètres par défaut de l'espace de travail et des réunions :

![Paramètres Avatour - Vue Espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Paramètres de l'espace de travail*

**Paramètres de l'espace de travail**

- **Modèle de rapport** – Sélectionnez le modèle de checklist pour les rapports IA.  
- **Activer les notifications** – E-mails de synthèse quotidiens pour les changements de statut des notes.  

![Notifications par e-mail - Exemple](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Exemple de notifications par e-mail*

- **Espace de travail public** – Toute personne disposant du lien peut voir les ressources directement.

**Paramètres de réunion**
  
* **Authentification requise** – Les participants doivent se connecter.  
* **Autoriser l'accès invité** – Permettre aux utilisateurs non enregistrés de voir les ressources.  
* **Démarrage automatique de l'enregistrement / Démarrage manuel** – Choisissez si les réunions s'enregistrent automatiquement ou sont démarrées manuellement.  
* **Hôte requis** – L'hôte doit admettre les participants ; la réunion se termine lorsque l'hôte part.  
* **Autoriser l'accès spectateur** – Rejoindre sans micro ni caméra ; communiquer via le chat.  
* **Réunions protégées par mot de passe** – Exiger un mot de passe pour rejoindre.  
* **Afficher la question sur les économies de déplacement** – Demander aux participants si la réunion a réduit les déplacements.  

> Les paramètres peuvent être combinés (par ex., pas d'hôte requis mais protégé par mot de passe).

---

#### 4.2.2 Ressources

Gérez toutes les vidéos 360°/2D, images et PDF. Téléchargez/téléversez des ressources, allouez-les aux espaces de travail, partagez avec d'autres utilisateurs, renommez, imprimez/téléchargez des rapports, activez le floutage des visages et la synthèse IA.

![Console Web Avatour - Élément de menu principal Ressources](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Élément de menu principal Ressources*

---

#### 4.2.3 Analytique

Fournit des informations sur les réunions, l'utilisation des espaces de travail et les indicateurs de ROI.

![Console Web Avatour - Élément de menu principal Analytique (1 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Aperçu Analytique*

![Console Web Avatour - Élément de menu principal Analytique (2 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Activité des réunions et utilisation des espaces de travail*

![Console Web Avatour - Élément de menu principal Analytique (3 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilisation des licences d'appareils et ROI*## 5. Sur site - Comment utiliser le kit clé en main Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Premiers pas
[Guide de démarrage rapide – Kit clé en main Avatour 3.1 (configuration Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Suivez le guide pour déballer, assembler et allumer votre caméra.

---

### 5.2 Conseils utiles

#### Batterie externe – Réunions en direct plus longues et meilleure gestion thermique

- **Si votre kit comprend une batterie Ulanzi :** Fixez-la entre la base du trépied et la perche extensible, puis connectez la batterie à la caméra via USB-C.

- **Si votre kit comprend une perche batterie Telesin :** Montez la caméra directement sur la perche batterie extensible Telesin et connectez-la via USB-C.

Utilisation de la batterie externe :

1. Prolonge l'autonomie totale d'environ 40 minutes (batterie de la caméra seule) à environ 3 heures.
2. Ajoute de la stabilité à l'installation de la caméra.
3. Aide à prévenir une éventuelle surchauffe.

> Nous recommandons de toujours utiliser la batterie externe dès le départ, particulièrement pour les réunions en direct.

#### Considérations audio pour les réunions en direct et les enregistrements

- **Environnements bruyants :**
  Utilisez les écouteurs Shokz inclus dans votre kit pour une capture audio claire.
  - **Marche/Arrêt :** Maintenez le bouton "+" pendant 3 secondes (LED bleue = allumé, LED rouge = éteint).
  - **Mode appairage Bluetooth :** Lorsque le casque est éteint, maintenez le bouton "+" pendant 5 secondes (la LED clignote bleu/rouge).
  - **Volume :** Utilisez les boutons "+" et "-".

- **Environnements plus calmes / plusieurs participants près de la caméra :**
  Utilisez l'enceinte à clip NoxGear. Elle n'est pas aussi haute fidélité que les enceintes de conférence (par ex., Jabra Speak), mais elle se clippe facilement sur votre chemise et capture efficacement les voix à proximité.
  - **Marche/Arrêt :** Maintenez le bouton Lecture/Pause pendant 2 secondes.
  - **Mode appairage Bluetooth :** Entre automatiquement en mode appairage à l'allumage (la LED clignote bleu/rouge ; bleu fixe une fois appairé).
  - **Volume :** Utilisez les boutons "+" et "-".

- **Utilisation de votre propre appareil :** Si vous préférez une alternative (par ex., une enceinte de conférence ou un casque personnel), vous pouvez l'appairer via la caméra : Paramètres → Bluetooth.

#### Connectivité, connectivité, connectivité
**Avant de commencer :** Assurez-vous de la connexion internet via :

- **WiFi local** (préféré)
- **Réseau mobile** (si hors de portée WiFi)

**Bande passante recommandée :** 10 Mbps en montée/descente pour le streaming 360° complet (~5 Mbps). Une bande passante plus faible (1–2 Mbps) fonctionne uniquement en restant immobile.

##### Tester la vitesse du réseau
- **Test en un seul endroit :** N'importe quel testeur de vitesse que vous utilisez habituellement (par ex., [Speedtest](https://www.speedtest.net)) pour vérifier la bande passante en upload.
- **Test en marchant sur le site :** Depuis la caméra : Paramètres → Réseau → Test de connexion. Parcourez l'ensemble de l'espace pour confirmer la couverture et la bande passante.

##### WiFi local
- Fortement recommandé pour des connexions stables.
- Si le service informatique exige une liste blanche, trouvez l'adresse MAC : Paramètres → À propos → Adresse WiFi.

##### Réseau mobile
**Option A : Hotspot et SIM fournis avec le kit**

- Fixez le hotspot GlocalMe sur la perche batterie Telesin (aimant).
- Garantit l'absence d'interférences et maintient la connexion si vous vous éloignez de la caméra.
- Dépannage :
  - Confirmez la SIM pré-installée (pas Cloud SIM).
  - Activez la 5G dans le Gestionnaire de carte SIM.
  - Vérifiez l'APN correct pour votre région ([guide de configuration APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B : Hotspot personnel / SIM**
- Utilisez votre propre smartphone ou hotspot dédié.

**Note importante :**
> Gardez le hotspot éteint lorsque vous êtes connecté au WiFi ; activez-le uniquement hors de portée. Le système d'exploitation de la caméra bascule dynamiquement entre les réseaux WiFi en fonction de la puissance du signal et peut basculer par inadvertance vers le hotspot même lorsque le WiFi est disponible.

> Les réseaux mobiles peuvent limiter la bande passante de manière inattendue. Vérifiez auprès de votre opérateur les limites de votre forfait data, ou contactez le support Avatour si vous utilisez notre hotspot et SIM.

##### Situations de faible bande passante
- Pré-enregistrez des vidéos de localisation pour une lecture ultérieure ([guide d'enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Partagez un flux de caméra smartphone pour compléter les zones à faible bande passante (0,1–0,3 Mbps en upload).

##### Aucune connectivité
- Seules les vidéos pré-enregistrées peuvent être utilisées ([guide d'enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Autres participants sur site – Bonnes pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même endroit que la caméra 360°, une gestion attentive de **l'audio et de la bande passante** est cruciale :

- Chaque smartphone, tablette ou ordinateur portable connecté sur site consomme de la bande passante réseau et peut impacter négativement le flux de la caméra 360°.
- Plusieurs microphones et haut-parleurs dans le même espace peuvent provoquer un **retour audio**, rendant l'expérience de réunion désagréable pour tous les participants.

#### Autres participants sur site – Bonnes pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même endroit que la caméra 360°, une gestion attentive de **l'audio et de la bande passante** est cruciale :

- Chaque smartphone, tablette ou ordinateur portable connecté sur site consomme de la bande passante réseau et peut impacter négativement le flux de la caméra 360°.
- Plusieurs microphones et haut-parleurs dans le même espace peuvent provoquer un **retour audio**, rendant l'expérience de réunion désagréable pour tous les participants.

Pour répondre à ces défis, suivez ces **bonnes pratiques** :

- **Utilisez des écouteurs filaires ou sans fil :** De préférence avec réduction de bruit pour éviter l'écho et le retour audio.
- **Mode sur site :** Rejoignez la réunion en mode Sur site lorsque vous êtes physiquement présent près de la caméra 360°.
  - Ce mode est optimisé pour une utilisation sur site :
    - Coupe le micro et le haut-parleur du participant par défaut.
    - N'envoie **pas** le flux caméra du participant.
    - N'affiche **pas** le flux de la caméra 360° dans le navigateur du participant.
    - Économise la bande passante réseau, garantissant que la caméra 360° dispose du maximum d'upload disponible pour le flux en direct.
    - Utile lorsqu'un utilisateur souhaite partager des détails spécifiques ; vous **pouvez partager votre caméra** pour des vues ciblées.
- **Coupez le micro lorsque vous ne parlez pas activement :** Évite les retours audio indésirables et les distractions.
- **Utilisez un réseau séparé si possible :** Connectez votre smartphone à un réseau différent de celui de la caméra pour réduire les interférences.

Suivre ces directives garantit une visite en direct fluide et de haute qualité pour les participants sur site comme à distance.

### 5.3 Application Avatour Camera

Voici (1) le niveau supérieur, (2) les Paramètres et (3) les menus Paramètres réseau.

![Application Avatour Caméra 360° - Trois menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Application Avatour Caméra 360° - 3 menus*

**Capture rapide** - Pour l'enregistrement vidéo 360° hors ligne. - Pour une description détaillée, voir [Comment enregistrer et télécharger des vidéos 360 avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Nous recommandons d'utiliser un appareil audio externe (connecté via Bluetooth). N.B. Vous pouvez également faire des vidéos et photos 2D standard - changez simplement le mode entre 360° et 2D dans le coin inférieur droit une fois dans l'écran CR.

**Réunion en direct** - Pour la visioconférence 360° en direct. Vous verrez vos espaces de travail et cliquer sur l'un d'eux initiera le flux vidéo en direct depuis la caméra 360°. Avant de pouvoir rejoindre la réunion avec votre caméra 360°, vous devez connecter un appareil audio via Bluetooth. Pour une description détaillée, voir [Comment démarrer une réunion Live Capture avec votre caméra Pilot ?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Lors de l'hébergement d'une réunion Live Capture avec votre caméra 360, vous disposerez d'outils de réunion similaires à ceux de l'expérience web. Voici un lien vers notre article de base de connaissances qui explique ces outils plus en détail : [Outils de l'application Opérateur](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galerie** - Retrouvez ici toutes vos vidéos et photos 360° pour les télécharger vers la console web Avatour.

**Paramètres** - Dans Paramètres, vous avez les options suivantes :

- **Réseau** : Cette option vous permet de changer le réseau WiFi auquel la caméra est connectée ou d'exécuter un test de connexion réseau pour voir votre débit de streaming
- **Live Capture** : Ajustez vos paramètres Live Capture en fonction de la bande passante disponible, de la sensibilité VR des invités, ou si les lentilles de protection de votre caméra sont installées :
  - **Fréquence d'images cible** : Ajustez la fréquence d'images pour votre vidéo Live Capture entre 15 fps, 24 fps et 30 fps. Des fréquences d'images plus élevées produisent une vidéo plus fluide, mais nécessiteront plus de bande passante en upload. Par défaut : 15 fps
  - **Débit cible** : Vous permet d'augmenter ou de diminuer le débit de streaming maximum pour votre Live Capture. Vous pouvez définir votre débit cible entre 1 Mbps et 10 Mbps. Des débits plus élevés donneront une résolution vidéo plus élevée, mais nécessiteront plus de bande passante en upload. Par défaut : 5 Mbps
  - **Optimiser le mouvement** : Cela diminuera la fréquence d'images vidéo, générant moins de charge sur la bande passante upload de votre réseau, et augmentera votre débit de streaming. De plus, cette option aide à réduire le mal des transports pour les participants VR. Par défaut : Désactivé
  - **Lentilles de protection** : Cela affectera la façon dont la vidéo 360° est assemblée selon que des lentilles de protection ont été installées sur votre caméra. Si vous n'avez pas de lentilles de protection, réglez ceci sur "Non". Si vous avez reçu un Kit 3.0, vous avez des lentilles de protection pré-installées et devez régler ceci sur "Oui". Par défaut : Oui

- **Capture rapide** : Ajustez vos paramètres de Capture rapide en fonction de votre fréquence d'images vidéo préférée, de la bande passante disponible pour les téléchargements de vidéos enregistrées, ou si les lentilles de protection de votre caméra sont installées. La Capture rapide a une résolution fixe de 4K qui offre généralement un bon équilibre entre qualité vidéo et taille de fichier. (Pour des résolutions plus élevées, vous pouvez utiliser les applications natives de la caméra, également sur le PanoX V2, pour plus de détails voir [Comment enregistrer et télécharger des vidéos 360 avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)) :
  - **Fréquence d'images cible** : Ajustez la fréquence d'images pour vos enregistrements vidéo Capture rapide entre 15 fps, 24 fps et 30 fps. Des fréquences d'images plus élevées produisent une vidéo plus fluide, mais augmenteront la taille du fichier vidéo et le temps de téléchargement. Recommandé : 30 fps
  - **Débit cible** : Définissez le débit cible pour les téléchargements Capture rapide entre 5 Mbps et 20 Mbps. Des débits plus faibles augmentent les vitesses de téléchargement, mais diminueront la qualité vidéo. Recommandé : 20 Mbps
  - **Lentilles de protection** : *Voir la section Lentilles de protection pour Live Capture ci-dessus*
- **À propos** : Afficher le numéro de série de l'appareil et la version du logiciel

**Compte** - Pour vous connecter avec votre compte hôte ou administrateur Avatour.## 6. Conseils de bonnes pratiques {#best-practice-advice}

### 6.1 Premières utilisations (informelles) et familiarisation

Pour vos premières utilisations et votre familiarisation avec la console Web Avatour et le kit clé en main Avatour, nous recommandons les étapes suivantes :

1. Emportez le kit chez vous et testez-le avec votre famille et vos amis en utilisant votre connexion internet domestique.
2. Apportez le kit au bureau et connectez-le à un réseau d'entreprise (des problèmes liés à l'entreprise peuvent survenir, par exemple les pare-feu d'entreprise - mais vous savez grâce à l'étape précédente qu'Avatour fonctionne et c'est un sujet à résoudre par votre équipe informatique avec l'aide d'Avatour).
3. Commencez à utiliser Avatour sur site (en dehors de votre bureau) sur le lieu de réunion où les participants distants devraient normalement se déplacer. D'autres problèmes de connectivité peuvent survenir. Avatour peut vous aider en coopération avec votre équipe informatique.
4. Commencez à utiliser avec des participants distants internes et externes.

### 6.2 Avant une réunion en direct avec vidéo 360°

- Nous recommandons de réaliser une visite vidéo 360° enregistrée avant toute visite en direct si le temps le permet, pour trois raisons : (1) Avoir une solution de secours pour la visite en direct, (2) avoir du contenu pour la documentation et une révision ultérieure (en plus de la visite en direct enregistrée) et (3) commencer à créer une bibliothèque de vidéos 360° de tous vos sites, ce qui peut être utile pour de nombreux cas d'usage.
- Tous les composants du kit doivent être chargés pendant au moins 90 minutes avant la réunion en direct. Nous recommandons de toute façon de garder tous les appareils en charge continue lorsqu'ils ne sont pas utilisés. Ainsi, tous les appareils seront toujours prêts, y compris pour des réunions ad hoc imprévues.
- Ayez le kit entièrement assemblé (1. base du trépied + 2. batterie Ulanzi + 3. perche extensible + 4. caméra 360°).

- Confirmez qu'un espace de travail est créé pour héberger une réunion en direct et incluez tous les éléments pertinents.

- Invitez tous les participants à la réunion via votre espace de travail. Cela crée une invitation dans les calendriers de tous les participants et inclut le lien d'invitation à la réunion.

- Appairez et connectez vos écouteurs ou haut-parleurs Bluetooth que vous prévoyez d'utiliser pour votre visite à la caméra.

- Tous les utilisateurs de smartphones sur site doivent se connecter depuis un réseau différent de celui de la caméra. Cela réduira la charge sur la bande passante du réseau de la caméra.

- Si vous êtes seul en tant qu'opérateur de caméra, emportez un smartphone avec vous au cas où vous voudriez partager la caméra du smartphone et montrer des détails fins.

- Confirmez que la caméra 360° peut se connecter à votre WiFi local.

- Avant une réunion Avatour, planifiez l'itinéraire que vous emprunterez dans l'installation. Faites une réunion Avatour de test avec la caméra et vérifiez que toutes les zones ont des débits supérieurs à 1 Mbps de bande passante. Cela peut être vu sur l'écran de la caméra elle-même, ou en tant que participant distant en allant dans Paramètres et en activant Afficher le débit.

- Si vous remarquez que certaines zones ont peu ou pas de bande passante, il est préférable de prendre des images ou un enregistrement. Ceux-ci peuvent ensuite être présentés pendant la réunion pour que les participants distants les examinent. Vous pouvez suivre le guide ici qui explique notre Capture rapide pour enregistrer et télécharger des vidéos/images : [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si des participants distants rejoignant la réunion n'ont jamais utilisé Avatour auparavant, fournissez-leur un bref résumé de la plateforme, de ses fonctionnalités (vidéo 360° en direct, éléments, captures d'écran, annotations, mise en évidence) et des outils de réunion.

- Vous pouvez commencer dans une autre solution de visioconférence (par exemple Teams, Zoom, Google Meet) mais avant de passer à Avatour, fermez complètement l'autre application de visioconférence. Dans certains cas, ces autres applications prioriseront le microphone/les haut-parleurs/la webcam de votre appareil, les rendant désactivés pour Avatour. De plus, n'exécutez PAS Avatour ET une autre visioconférence en même temps car cela réduira la bande passante disponible.

- Si vous prévoyez d'utiliser la caméra 360° dans un environnement à haute température, il est recommandé d'utiliser le module de refroidissement (Pilot Pano uniquement). Cela aidera à réduire les risques de surchauffe de la caméra et d'arrêt automatique.

### 6.3 Lors de l'utilisation de la caméra sur site pour une réunion en direct avec vidéo 360°

- Lorsque vous utilisez la caméra, assurez-vous de marcher lentement. Cela améliore la qualité vidéo et réduit toute interruption vidéo potentielle lorsque la connexion réseau de la caméra bascule entre les points d'accès WiFi.

- Tenez la caméra devant vous et au-dessus du niveau des yeux. Cela permet à tous les participants distants de voir la majorité de votre environnement.

- Pour les situations où la caméra doit rester stable, utilisez le support trépied et étendez la caméra à la bonne hauteur, idéalement au niveau des yeux.

- Connectez toujours la caméra à votre réseau WiFi local lorsque c'est possible. Pour les zones sans accès WiFi, utilisez le hotspot fourni. Le hotspot dispose d'une carte SIM qui se connectera à un réseau cellulaire fiable près de vous. Gardez toujours le hotspot éteint lorsqu'il n'est pas utilisé à l'intérieur car sinon la caméra 360° pourrait se connecter au hotspot, ce que nous ne souhaitons pas à l'intérieur. À l'extérieur, gardez le hotspot près de la caméra 360°.

- Lorsque le débit sur la caméra commence à descendre en dessous de 2 Mbps, marchez plus lentement ou arrêtez-vous complètement jusqu'à ce que le signal se stabilise à nouveau. Cela se produit généralement lorsque vous passez d'un point d'accès WiFi à un autre.

- Si vous savez que la connectivité et la vidéo seront interrompues lors du déplacement vers un endroit spécifique (Exemple : passage d'une zone de production intérieure à une zone extérieure), prévenez les participants distants à l'avance.

- Si vous devez montrer quelque chose en haute définition ou de petits textes, utilisez votre smartphone ou celui d'un participant sur site pour rejoindre la réunion et présenter la caméra (arrière) de votre téléphone / du leur.

- Si possible, nous recommandons qu'une personne supplémentaire soit sur site pour aider avec le partage de caméra de smartphone décrit ci-dessus car cela s'avère souvent utile / nécessaire.

- Idéalement, les utilisateurs de smartphones sur site devraient rejoindre la réunion (1) en mode sur site et (2) sur un réseau différent de celui utilisé par la caméra afin de ne pas prendre de bande passante de téléchargement cruciale à la caméra 360°.

- Tous les participants sur site rejoignant depuis leur smartphone doivent être en sourdine, sauf s'ils parlent activement.