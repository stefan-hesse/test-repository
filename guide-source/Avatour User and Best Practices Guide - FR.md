# Avatour User and Best Practices Guide

## 1. Pour tous les utilisateurs d'Avatour {#for-all-avatour-users}
Si vous découvrez Avatour, les ressources suivantes offrent une introduction utile à la plateforme et à ses capacités :

1. [Vidéo Avatour How it Works](https://avatour.com/how-it-works)  
Un aperçu rapide des fonctionnalités principales d'Avatour et comment la plateforme permet la collaboration à distance immersive.
2. [FAQ](https://avatour.com/faqs)  
Réponses aux questions fréquemment posées.
3. [Glossaire](https://avatour.com/glossary)  
Définitions des termes et concepts clés d'Avatour fréquemment utilisés.
4. Site Web  
Consultez notamment la page [Fonctionnalités d'Avatour](https://avatour.com/features) ainsi que les sections dédiées aux Cas d'usage et Secteurs d'activité pour apprendre comment Avatour peut répondre à vos besoins spécifiques.## 2. Types d'utilisateurs Avatour  {#avatour-user-types}

### 2.1 Participants à la réunion (aucun compte requis)
Les utilisateurs peuvent participer à la réunion sans s'inscrire à un compte Avatour.
Exception : Si l'hôte a restreint la réunion aux utilisateurs enregistrés — par exemple, pour permettre uniquement aux employés internes de se connecter via Single Sign-On (SSO) — l'invitation du calendrier indiquera que les participants doivent se connecter pour s'authentifier.

Les utilisateurs accèdent à la réunion de la manière suivante :

- Recevoir une invitation du calendrier de la part de l'hôte.
- Utiliser le lien de réunion dans l'invitation pour participer.
- Entrer un mot de passe de réunion si l'hôte en a activé un.
- Les participants peuvent participer sans compte Avatour à moins que la réunion ne soit restreinte et ne nécessite une connexion pour s'authentifier.

#### 2.1.1 Participant

- Peut participer et interagir pleinement (webcam, microphone, chat et fonctionnalité Présenter).
- Maximum de 20 participants interactifs par réunion.

#### 2.1.2 Spectateur

- Peut regarder la réunion et participer via le chat uniquement.
- Ne peut pas partager de vidéo, utiliser un microphone, présenter, lire/mettre en pause des Assets ou capturer des Snapshots.
- Maximum de 10 spectateurs par réunion.
- Avec les participants, une réunion peut accueillir jusqu'à 30 participants.### 2.2 Utilisateurs Enregistrés

Les utilisateurs enregistrés disposent d'un compte Avatour. Les comptes sont créés de l'une des manières suivantes :

- **Invitation par Admin :** Lors de l'intégration, Avatour configure un **tenant dédié** pour l'organisation et crée un ou plusieurs **comptes Admin**. Les Admins peuvent ensuite **inviter des utilisateurs** au sein de l'organisation et les assigner à des **groupes**, qui définissent leur rôle sur la plateforme (Invité, Animateur ou Admin). Les utilisateurs invités reçoivent un **lien d'inscription** pour terminer la configuration du compte et définir un mot de passe.  
- **Invitation par Animateur :** Les Animateurs peuvent ajouter des utilisateurs en tant que **collaborateurs Éditeur** à un Workspace. Cela consomme une **licence Animateur** et garantit à l'utilisateur un accès au niveau Animateur.  
- **Approvisionnement automatique SSO (niveaux Enterprise/Business uniquement) :** Les comptes peuvent être créés automatiquement par le fournisseur d'identité. Par défaut, les comptes configurés via SSO sont ajoutés au **groupe Invité**, sauf indication contraire via les **mappages de groupes SAML**. Les Admins peuvent toujours inviter des utilisateurs et assigner directement l'appartenance aux groupes, même lorsque SSO est activé.

**Résumé :**  

Les utilisateurs enregistrés et leur appartenance aux groupes peuvent être gérés de plusieurs façons :

- **Gestion par Admin :** Un Admin dans la console Avatour peut créer des utilisateurs et les assigner à des groupes, qui définissent leur rôle sur la plateforme (Invité, Animateur ou Admin).  
- **Approvisionnement SSO :** Pour les clients des niveaux Enterprise ou Business disposant de SSO activé, le fournisseur d'identité peut provisionner automatiquement les comptes et assigner l'appartenance aux groupes, qui définit le rôle de la plateforme de l'utilisateur.  
- **Utilisateurs invités par Animateur :** Les Animateurs peuvent inviter d'autres utilisateurs en tant que collaborateurs Éditeur à des Workspaces spécifiques. L'assignation du rôle de collaborateur Éditeur consomme une licence Animateur.

**Bonne Pratique Recommandée (Clients Enterprise) :**  
Pour les organisations s'attendant à un grand nombre d'utilisateurs ayant besoin d'accès à Avatour, il est recommandé d'**intégrer l'Authentification Unique (SSO)** et de gérer les utilisateurs et les appartenances aux groupes à partir du **fournisseur d'identité**. Cette approche rationalise l'approvisionnement des comptes, l'assignation des groupes et la gestion des licences, réduisant la charge administrative et assurant un contrôle d'accès cohérent.

#### 2.2.1 Utilisateurs Invités

- Ajoutés au **groupe Invité**.  
- Peuvent **afficher les Actifs** au sein des Workspaces où ils ont été ajoutés en tant que **collaborateurs Spectateur**.  
- Ne peuvent pas créer de workspaces, animer de réunions ni télécharger de contenu.  
- Les comptes Invité configurés via SSO **s'authentifient via le fournisseur d'identité** ; aucun mot de passe géré par Avatour n'est requis.

---

#### 2.2.2 Utilisateurs Sous Licence (Accès à la Console Web)

##### Utilisateurs Animateur (Groupe : Animateur)

- Peuvent créer/gérer des Workspaces, inviter des collaborateurs à un workspace, **animer des réunions en direct**, télécharger des **Captures Rapides**.  
- Ont accès au **Tableau de Bord Animateur** et à l'**Application Opérateur** sur les caméras 360° supportées.  

##### Utilisateurs Admin (Groupe : Admin)

- Incluent tous les droits Animateur plus l'administration complète du compte.

**Les privilèges Admin supplémentaires incluent :**

**Gestion des Comptes**  

- Créer de nouveaux utilisateurs et les assigner à des groupes.
- Réinitialiser les mots de passe lorsqu'ils sont gérés par Avatour (non applicable lorsque SSO est activé). 
- Promouvoir les utilisateurs Invité en Animateur.  
- Désactiver des utilisateurs (les comptes Admin doivent d'abord être convertis en Animateur avant suppression).  
- Transférer les actifs d'un utilisateur Animateur à un autre lors de la suppression.

**Paramètres**  

- Configurer les **paramètres de sécurité à l'échelle de l'organisation** pour les actifs, workspaces et réunions hébergés sur la plateforme (par ex., si un Animateur doit être présent pour démarrer une réunion, si les visages doivent être floutés sur toutes les vidéos téléchargées sur la plateforme).  
- Activer ou désactiver les **fonctionnalités IA** ou **l'enregistrement**.  
- Appliquer l'image de marque de l'entreprise de manière cohérente sur la plateforme si un **domaine personnalisé** est configuré.
  

**Actifs et Analyses** 
 
- Afficher tous les Actifs téléchargés par tout utilisateur de l'organisation.  
- Examiner l'utilisation de la plateforme dans toute l'organisation.

---

#### 2.2.3 Permissions de Collaborateur Workspace

Les permissions Workspace définissent ce qu'un utilisateur peut faire **au sein d'un Workspace spécifique**. Elles sont distinctes de l'appartenance au groupe au niveau de la plateforme (Invité, Animateur, Admin).

- **Collaborateur Éditeur :** Les utilisateurs disposant de cette permission peuvent :
  - Gérer les Actifs (télécharger, supprimer, flouter les visages, générer des résumés)  
  - Gérer les paramètres de réunion (activer/désactiver l'enregistrement, autoriser ou supprimer des participants)  
  - Planifier et animer des réunions en direct  
  - Générer des rapports basés sur des modèles prédéfinis  
  - Ajouter ou supprimer des collaborateurs du Workspace  

- **Collaborateur Spectateur :** Les utilisateurs disposant de cette permission ont un accès en lecture seule aux Actifs du Workspace. Ils **ne peuvent pas modifier les Actifs, gérer les réunions ou gérer les collaborateurs**, mais ils **peuvent créer des Notes sur les Actifs**.## 3. Pour les participants aux réunions à distance et les visiteurs de l'espace de travail {#for-remote-meeting-participants-and-workspace-visitors}
Avatour permet aux utilisateurs de collaborer de deux manières principales :

- **Rejoindre une réunion Avatour (Collaboration synchrone) :**  
  Vous pouvez recevoir une **invitation calendrier** pour rejoindre une réunion Avatour. Pendant la réunion, les participants peuvent effectuer une **visite de site à distance en direct** ou examiner les ressources de manière synchrone ensemble.

- **Visiter un Espace de travail (Collaboration asynchrone) :**  
  Vous pouvez également être invité en tant que **collaborateur à un Espace de travail** pour examiner les ressources **de manière asynchrone** (à votre convenance).### 3.1 Comment rejoindre une réunion Avatour et visiter un espace de travail Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 N'importe quel appareil « écran plat » avec un navigateur Web {#any-flat-screen}
Vous pouvez rejoindre une réunion Avatour depuis **n'importe quel ordinateur de bureau ou portable, smartphone ou tablette** en utilisant un navigateur Web.

##### Rejoindre une réunion Avatour

> **Remarque :** Rejoindre une réunion Avatour nécessite que vous **accordiez les autorisations du microphone**. Veuillez accepter toutes les invites d'autorisation de votre navigateur.

1. **Via invitation calendrier (recommandé) :**
   - Vous recevrez généralement une **invitation calendrier** avec un **lien de participation directe** (par exemple : `https://avatour.live/join?s=xxxxx`).
   - Cliquer sur le lien remplira automatiquement le **code de réunion à 5 caractères** et vous amènera à la réunion.
   - **Authentification requise :** Certaines réunions sont réservées aux utilisateurs enregistrés. Dans ce cas, l'invitation indiquera que vous devez **vous connecter pour accéder à la réunion**.
   - **Réunions protégées par mot de passe :** Certaines réunions peuvent nécessiter un mot de passe. Dans ce cas, l'invitation inclura le mot de passe que vous devez entrer pour rejoindre.

2. **Via code de réunion :**
   - Si l'hôte partage un **code de réunion à 5 caractères** séparément, accédez à [https://avatour.live/join](https://avatour.live/join), entrez votre **nom** et le **code de réunion**, et rejoignez la réunion.
   - Si la réunion est **protégée par mot de passe**, entrez le mot de passe fourni par l'hôte.
   - Si la réunion nécessite une **authentification**, vous devrez **vous connecter avec votre compte Avatour** avant de rejoindre.

> **Conseil 1 :** Si votre caméra ou microphone ne fonctionne pas, il se peut qu'il soit utilisé par une autre application (par exemple Microsoft Teams ou Zoom). Fermez toute application qui pourrait utiliser votre caméra ou microphone, puis quittez et rejoignez la réunion Avatour.

> **Conseil 2 :** Si vous ne pouvez toujours pas rejoindre la réunion, exécutez ce test : [https://avatour.live/test](https://avatour.live/test).
> Le test peut identifier si votre **pare-feu ou réseau d'entreprise** bloque l'accès, et fournira des informations pour guider les discussions avec votre équipe informatique.

> **Conseil 3 :** N'utilisez **pas** les applications Avatour iOS ou Android pour rejoindre les réunions. Ces applications ne sont requises que lors du **streaming d'une réunion en direct depuis une caméra Insta360**, car ces caméras ne peuvent pas exécuter le logiciel Avatour 360° directement et nécessitent un smartphone pour l'assistance.

##### Visiter un espace de travail Avatour (sans rejoindre une réunion Avatour)

Vous pouvez accéder à un espace de travail de la manière suivante :

- **Espace de travail public :**
  Si l'espace de travail est public, le lien peut être accédé directement — aucune connexion requise.

- **Espace de travail restreint :**
  Si l'espace de travail est restreint, vous devez être ajouté en tant que **collaborateur** avec des autorisations **Éditeur** ou **Lecteur**.

  1. Lorsque vous êtes ajouté en tant que collaborateur, vous recevrez une **notification par email** avec un lien vers l'espace de travail.
  2. Cliquez sur le lien dans l'email pour ouvrir l'espace de travail. Si vous n'êtes pas déjà connecté, vous serez invité à **vous connecter ou à terminer l'inscription**.
  3. Une fois connecté, l'espace de travail s'ouvrira automatiquement.

  Sinon, vous pouvez vous connecter à [https://avatour.live/login](https://avatour.live/login) et accéder à l'espace de travail depuis votre **liste d'espaces de travail**.

#### 3.1.2 Casque VR {#vr-headset}
Vous pouvez rejoindre une réunion et visiter un espace de travail à partir d'une gamme de casques Meta et Pico compatibles. Pour ce faire :

1. Installez notre application Avatour depuis votre magasin d'applications VR respectif : [Comment installer l'application Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Chargez notre application et entrez le code de réunion ou sélectionnez un espace de travail pour rejoindre une réunion. Pour plus d'informations sur la façon d'utiliser notre application VR, consultez notre article de la base de connaissances [ici](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Outils de réunion et de collaboration dans l'espace de travail {#meeting-tools}

Avatour permet la collaboration dans deux contextes principaux :

1. **Réunions (synchrone) :** Collaborez en temps réel avec d'autres participants, notamment lors de visites de site en direct ou d'examen d'actifs enregistrés ensemble.
2. **Espaces de travail (asynchrone) :** Examinez et interagissez avec les actifs selon votre propre calendrier, 24h/24, 7j/7.

Les **outils de collaboration sont principalement similaires** entre les réunions et les espaces de travail, avec certaines différences dues au contexte synchrone ou asynchrone.

#### 3.2.1 Disposition de l'interface

L'interface Avatour est organisée autour de trois domaines principaux :

- **Panneau de gauche** – Actifs de l'espace de travail et outils de support
- **Canevas central** – Zone de visualisation principale pour la vidéo en direct ou les actifs
- **Panneau de droite** – Informations contextuelles, telles que les participants, les réunions ou la discussion

La plupart des interactions sont initiées à partir du **menu inférieur**.
Cliquer sur une option du menu ouvre un **panneau latéral** sur le côté gauche ou droit de l'écran, tandis que le **canevas central** reste la zone de visualisation principale.

---
#### 3.2.2 Exemple de vue de réunion

Voici un exemple de vue dans une réunion Avatour :

![Interface de réunion Avatour avec panneau d'actifs, canevas vierge et panneau des participants](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)
*Réunion Avatour avec panneau d'actifs (gauche), canevas (centre) et panneau des participants (droite)*

---

#### 3.2.3 Exemple de vue d'espace de travail

Voici un exemple de vue d'espace de travail :

![Espace de travail Avatour avec panneau d'actifs, canevas vierge et panneau des réunions](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)
*Espace de travail Avatour avec panneau d'actifs (gauche), canevas (centre) et panneau des réunions (droite)*

---

#### 3.2.4 Aperçu du menu inférieur

Le menu inférieur donne accès aux commandes d'interface principale et aux panneaux :

**Menu inférieur de réunion**

![Menu inférieur de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)
*Menu inférieur de réunion Avatour*

- **Actifs** – Examinez les fichiers de l'espace de travail, notamment les vidéos enregistrées, les images, les captures d'écran et les PDF.
- **Discussion** – Envoyez des messages à tous les participants de la réunion.
- **Caméra** – Activez ou désactivez votre webcam.
- **Microphone** – Coupez ou restaurez le son.
- **Présentation** – Présentez un actif, un bureau ou un flux de webcam (voir la section Présentation ci-dessous).
- **Outils d'hôte** (hôtes uniquement) :
  - **Verrouiller la vue** – Verrouillez la vue pour tous les participants.
  - **Désactiver le son de tous** – Coupez le son de tous les participants.
- **Activer le mode plein écran** – Mettez l'onglet de réunion en mode plein écran.
- **Quitter la réunion** – Quittez la réunion.
- **Démarrer l'enregistrement** – Utilisez ce bouton pour démarrer et arrêter manuellement l'enregistrement pendant une réunion. Alternatively, les réunions peuvent être enregistrées automatiquement si **l'enregistrement automatique** est activé dans les paramètres de l'espace de travail. Dans les deux cas, les enregistrements sont enregistrés dans les actifs de l'espace de travail.
- **Carte** – Ouvrez ou fermez le panneau de la carte pour les actifs ayant une trace GPS. Cliquer sur un emplacement vous amène au point exact dans la vidéo. La carte se met à jour en direct lors de la lecture de la vidéo.
- **Participants** – Ouvrez ou fermez le panneau des participants.
- **Informations sur la réunion** – Consultez le code de réunion, le lien d'invitation et accédez aux tutoriels connexes.

![Informations sur la réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)
*Panneau latéral des informations de réunion Avatour*

- **Paramètres** – Ajustez les paramètres de langue, d'audio et de vidéo. Pour les réunions vidéo 360° en direct, utilisez **Afficher le débit** pour surveiller les statistiques de connectivité.

> Conseil : Envoyez le lien de réunion ou ajoutez-le à un élément de calendrier pour inviter les participants.

---

##### Menu de présentation

L'option **Présentation** dans le menu inférieur de réunion vous permet de partager du contenu avec tous les participants.

- **Caméra** – Partagez la caméra de votre smartphone/tablette. Cela peut également être utilisé lors d'une réunion vidéo 360° en direct pour superposer une vue secondaire pour des gros plans ou des détails spécifiques.
- **Bureau** – Partagez votre écran de bureau avec tous les participants.
- **Actif** – Présentez un actif de l'espace de travail. Sélectionner un actif ouvre la **barre d'outils d'actif**, qui fournit les contrôles de lecture et les outils de collaboration spécifiques à l'actif présenté.

##### Barre d'outils d'actif (Réunion)

Lors de la présentation d'un actif dans une réunion, la **barre d'outils d'actif** apparaît au-dessus du canevas. Voici les outils et les éléments de menu disponibles lors de <u>la présentation d'un actif dans une réunion</u> - expliqués de gauche à droite.

![Menu Avatour lors de la présentation d'un actif dans une réunion](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour lors de la présentation d'un actif dans une réunion*

- **Chronologie vidéo / Barre de progression** – Affiche la progression de la vidéo avec les notes et les sujets clés extraits de l'audio. Cliquez sur une note ou un sujet pour accéder à ce moment et ouvrir la note. Inclut les contrôles **Lire / Pause**.
- **Capture d'écran** – Capturez une image 360° ou 2D à partir de l'actif.
- **Spotlight** – Mettez en évidence une zone spécifique pour tous les participants lors des sessions en direct.
- **Afficher/Masquer le point de vue (PDV)** – Affichez où chaque participant regarde dans la vidéo 360°.
- **Notes** – Créez des notes ancrées à des moments spécifiques de l'actif. Les notes peuvent être catégorisées (Observation, Problème, Action, Recommandation), suivies par statut (Ouvert → En cours → Résolu) et partagées via des liens directs.

  ![Note Avatour et filtre de notes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Note Avatour et filtres de notes*

  - **Notes par commande vocale** – Ce sont des espaces réservés générés automatiquement lorsque l'enregistrement détecte des mentions comme « insérer une note », « prendre une note » ou « créer une note ». Ces notes apparaissent sur la chronologie et doivent être **positionnées et finalisées** par l'utilisateur.

  ![Notes Avatour - Générées par commande vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notes Avatour - Générées par commande vocale*

- **Panneau notes et résumé** – Ouvre un panneau latéral qui affiche toutes les notes, les sujets clés et un résumé exécutif de l'actif. Cliquer sur un élément vous amène à ce moment dans la vidéo.

  ![Résumé exécutif d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Résumé exécutif Avatour lors de la présentation d'un actif dans une réunion*

  ![Sujets Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Sujets Avatour lors de la présentation d'un actif dans une réunion*

  À partir du **panneau latéral**, vous pouvez **imprimer un rapport d'actif** ou **le télécharger en TXT ou CSV**. Les rapports peuvent inclure des notes, des sujets générés par l'IA et des transcriptions complètes. Vous pouvez également **choisir les éléments à inclure** avant d'exporter.

  ![Menus d'impression de rapport d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)
  *Menus d'impression/téléchargement de rapport d'actif Avatour*

  ![Menu de sélection d'éléments de rapport d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)
  *Menu de sélection d'éléments de rapport d'actif Avatour*

- **Lien de partage** – Partagez un lien vers une note ou une scène spécifique de l'actif.
- **Sous-titres (CC)** – Affichez la transcription textuelle à l'écran lors de la lecture de la vidéo.

##### Barre d'outils d'actif (Espace de travail)

Lors de l'examen d'un actif dans un espace de travail, la barre d'outils est similaire mais optimisée pour une utilisation individuelle :

![Menu Avatour lors de la présentation d'un actif en dehors d'une réunion, par exemple lors de la visite d'un espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour lors de la présentation d'un actif dans un espace de travail*

- **Chronologie vidéo / Barre de progression** – Affiche la progression de la vidéo avec les notes et les sujets clés extraits de la piste audio. Cliquez n'importe où sur la chronologie pour parcourir la vidéo. Cliquez sur une note ou un sujet pour accéder à ce moment et ouvrir la note. Inclut les contrôles **Lire / Pause**.
- **Capture d'écran, Notes, Panneau notes et résumé, Lien de partage, Sous-titres**
- Non disponible : **Spotlight, PDV** (ceux-ci nécessitent des participants en direct)
- Contrôles supplémentaires :
  - **Pas de 10 secondes** – Avancer/reculer
  - **Vitesse de lecture** – Ajustez la vitesse (0,5 × – 2 ×)
  - **Découper la vidéo** – Découpez le début ou la fin de l'actif## 4. Pour les utilisateurs Host et Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}
Lorsque vous vous connectez à votre compte utilisateur Avatour, vous accédez à la **Web Console**.### 4.1 Console Web - Aperçu du Menu Principal {#web-console-overview-main-menu}

Sur le côté gauche, vous verrez les éléments de menu suivants :

![Avatour Web Console - Menu Principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Avatour Web Console - Menu Principal*

- **Espaces de travail** – Organisez votre contenu efficacement. Chaque espace de travail contient **Ressources**, **Collaborateurs**, **Réunions** et **Paramètres**.  
- **Ressources** – Accédez et gérez toutes vos ressources (vidéos, images, PDF). Les administrateurs peuvent consulter toutes les ressources du compte, et les ressources partagées sont visibles par tous les utilisateurs.  
- **Profil** – Gérez votre langue et votre mot de passe.  
- **Analytique** – Suivez l'activité des sessions, l'utilisation de l'espace de travail et les métriques de ROI.  
- **Paramètres** *(Administrateur uniquement)* – Configurez les paramètres par défaut de l'espace de travail, des réunions et des ressources dans l'organisation. Les administrateurs peuvent également personnaliser la marque (logo, couleurs, arrière-plans).  
- **Compte** *(Administrateur uniquement)* – Gérez les utilisateurs enregistrés et les caméras 360°.  
- **Connexion d'appareil** – Entrez le code affiché sur votre caméra 360° pour l'associer à votre compte.  
- **Tutoriels** – Accédez aux tutoriels guidés.  
- **Déconnexion** – Quittez la console.

> Les sections comme Profil, Connexion d'appareil, Tutoriels et Déconnexion sont explicites et n'ont pas de sous-sections détaillées.

---### 4.2 Console Web - Détails par élément de menu (avec images) {#web-console-details-by-menu-item}

#### 4.2.1 Espaces de travail

Les espaces de travail sont des unités organisationnelles flexibles qui vous permettent de gérer les actifs, les collaborateurs et les réunions en un seul endroit. Vous pouvez créer un nouvel espace de travail avec le bouton **Nouvel espace de travail** dans le coin supérieur droit.

![Avatour Web Console - Élément du menu principal Espaces de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Élément du menu principal Espaces de travail*

Cliquez sur l'icône de la cloche pour voir un résumé de l'activité de l'espace de travail au cours des 7 derniers jours.

![Avatour Web Console - Activités récentes de l'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Activités récentes de l'espace de travail*

À l'intérieur d'un espace de travail :

![Espace de travail Avatour avec panneau Actifs, Canvas vierge et panneau Réunions](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espace de travail avec Actifs (gauche), Canvas (centre), Réunions (droite)*

- **Actifs** – Gérez les fichiers alloués à cet espace de travail.  
- **Collaborateurs** – 
  Contrôlez l'accès aux espaces de travail par 
  - **Lecteur** – Peut afficher les actifs. L'invitation crée un utilisateur invité si nécessaire.  
  - **Éditeur** – Contrôle complet de l'espace de travail, mêmes droits que l'hôte. L'invitation met à niveau l'utilisateur en hôte si nécessaire.  
> Plusieurs utilisateurs peuvent accéder à un espace de travail simultanément sans réunion. Les espaces de travail publics et les paramètres d'accès aux réunions offrent des accès alternatifs.  
- **Rapport** – Générez un rapport à l'aide d'un modèle de liste de contrôle sur les actifs de l'espace de travail sélectionné.  

![Rapport d'espace de travail Avatour et sélection d'actifs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Rapport d'espace de travail et sélection d'actifs*

- **Carte** – Affichage des emplacements des actifs compatibles GPS sur une carte.  
- **Réunions** – Organisez des réunions dans l'espace de travail.  
- **Paramètres** – Configurez les valeurs par défaut de l'espace de travail et de la réunion :

![Avatour Paramètres - Vue de l'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Paramètres de l'espace de travail*

**Paramètres de l'espace de travail**

- **Modèle de rapport** – Sélectionnez le modèle de liste de contrôle pour la création de rapports IA.  
- **Activer les notifications** – E-mails de synthèse quotidienne pour les modifications de statut des notes.  

![Notifications par e-mail - Exemple](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Exemple de notifications par e-mail*

- **Espace de travail public** – Toute personne disposant du lien peut afficher les actifs directement.

**Paramètres de réunion**
  
* **Authentification requise** – Les participants doivent se connecter.  
* **Autoriser l'accès invité** – Permettre aux utilisateurs non enregistrés de visualiser les actifs.  
* **Enregistrement automatique / Démarrage manuel** – Choisissez si les réunions s'enregistrent automatiquement ou sont démarrées manuellement.  
* **Hôte requis** – L'hôte doit admettre les participants ; la réunion se termine quand l'hôte part.  
* **Autoriser l'accès spectateur** – Rejoignez sans micro ni caméra ; communiquez via le chat.  
* **Réunions protégées par mot de passe** – Exigez un mot de passe pour accéder.  
* **Afficher la question sur les économies de déplacement** – Demandez aux participants si la réunion a réduit les déplacements.  

> Les paramètres peuvent être combinés (par exemple, aucun hôte requis mais protégé par mot de passe).

---

#### 4.2.2 Actifs

Gérez toutes les vidéos 360°/2D, images et PDF. Téléchargez/téléchargez les actifs, attribuez-les aux espaces de travail, partagez avec d'autres utilisateurs, renommez, imprimez/téléchargez les rapports, activez le flou du visage et la synthèse IA.

![Avatour Web Console - Élément du menu principal Actifs](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Élément du menu principal Actifs*

---

#### 4.2.3 Analyses

Fournit des informations sur les réunions, l'utilisation de l'espace de travail et les métriques de ROI.

![Avatour Web Console - Élément du menu principal Analyses (1 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Aperçu des analyses*

![Avatour Web Console - Élément du menu principal Analyses (2 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Activité des réunions et utilisation de l'espace de travail*

![Avatour Web Console - Élément du menu principal Analyses (3 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilisation des licences d'appareil et ROI*## 5. Sur site - Comment utiliser le kit clé en main Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Premiers pas
[Guide de démarrage rapide – Avatour Turnkey Kit 3.1 (Configuration Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Suivez le guide pour déballer, assembler et allumer votre caméra.

---### 5.2 Conseils utiles

#### Batterie externe – Réunions plus longues et amélioration thermique 

- **Si votre kit inclut une batterie Ulanzi :** Attachez-la entre la base du trépied et le bâton extensible, puis connectez la batterie à l'appareil photo via USB-C.  

- **Si votre kit inclut un bâton de batterie Telesin :** Montez l'appareil photo directement sur le bâton de batterie extensible Telesin et connectez-le via USB-C.  

Utilisation de la batterie externe :

1. Prolonge l'autonomie totale de ~40 minutes (batterie de l'appareil photo uniquement) à ~3 heures.  
2. Ajoute de la stabilité à la configuration de l'appareil photo.  
3. Aide à prévenir le surcharffement potentiel.  

> Nous recommandons toujours d'utiliser la batterie externe dès le départ, en particulier pour les réunions en direct.

#### Considérations audio pour les réunions et les enregistrements en direct

- **Environnements bruyants :** 
  Utilisez les écouteurs Shokz inclus dans votre kit pour une capture audio claire.  
  - **Mise sous/hors tension :** Maintenez le bouton « + » enfoncé pendant 3 secondes (LED bleue = activée, LED rouge = désactivée).  
  - **Mode d'appairage Bluetooth :** Alors que le casque est éteint, maintenez le bouton « + » enfoncé pendant 5 secondes (LED clignote bleu/rouge).  
  - **Volume :** Utilisez les boutons « + » et « - ».  

- **Environnements plus calmes / plusieurs participants près de l'appareil photo :** 
  Utilisez le haut-parleur clip NoxGear. Il n'offre pas une aussi haute fidélité que les conférenciers (par exemple, Jabra Speak), mais il est facile à clipser sur votre chemise et capture efficacement les voix à proximité.  
  - **Mise sous/hors tension :** Maintenez le bouton Lecture/Pause enfoncé pendant 2 secondes.  
  - **Mode d'appairage Bluetooth :** Entre automatiquement en mode d'appairage lors de la mise sous tension (LED clignote bleu/rouge ; bleu solide quand appairé).  
  - **Volume :** Utilisez les boutons « + » et « - ».  

- **Utiliser votre propre appareil :** Si vous préférez une alternative (par exemple, un conférencier ou un casque personnel), vous pouvez l'appairer via l'appareil photo : Paramètres → Bluetooth.  

#### Connectivité, connectivité, connectivité
**Avant de commencer :** Assurez la connexion Internet via :

- **WiFi local** (préféré)
- **Réseau mobile** (si hors de portée du WiFi)

**Bande passante recommandée :** 10 Mbps en montée/descente pour la diffusion complète à 360° (~5 Mbps). Une bande passante inférieure (1-2 Mbps) ne fonctionne que lorsque vous êtes immobile.

##### Test de vitesse réseau
- **Test à un seul endroit :** N'importe quel vérificateur de vitesse que vous utilisez normalement (par exemple, [Speedtest](https://www.speedtest.net)) pour vérifier la bande passante en montée.   
- **Test de marche sur site :** Depuis l'appareil photo : Paramètres → Réseau → Test de connexion. Parcourez tout l'espace pour confirmer la couverture et la bande passante.

##### WiFi local
- Hautement recommandé pour des connexions stables.  
- Si l'informatique exige une liste blanche, trouvez l'adresse MAC : Paramètres → À propos → Adresse WiFi.

##### Réseau mobile
**Option A : Hotspot kit fourni et SIM**  

- Attachez le hotspot GlocalMe au bâton de batterie Telesin (aimant).  
- Garantit aucune interférence et maintient la connexion en cas de déplacement loin de l'appareil photo.  
- Dépannage :
  - Confirmez la SIM pré-installée (pas Cloud SIM).  
  - Activez la 5G dans le Gestionnaire de carte SIM.  
  - Vérifiez l'APN correct pour votre région ([guide de configuration APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B : Hotspot personnel / SIM**
- Utilisez votre propre smartphone ou hotspot dédié.  

**Remarque importante :**  
> Gardez le hotspot désactivé lors de la connexion au WiFi ; activez-le uniquement hors de portée. Le système d'exploitation de l'appareil photo bascule dynamiquement entre les réseaux WiFi en fonction de la force du signal et peut accidentellement basculer vers le hotspot même lorsque le WiFi est disponible.

> Les réseaux mobiles peuvent réduire la bande passante de manière inattendue. Vérifiez auprès de votre opérateur les limites de votre plan de données, ou contactez l'assistance Avatour si vous utilisez notre hotspot et notre SIM.

##### Situations de faible bande passante
- Pré-enregistrez les vidéos d'emplacement pour une lecture ultérieure ([guide d'enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Partagez un flux de caméra smartphone pour compléter les zones à faible bande passante (0,1-0,3 Mbps en montée).

##### Pas de connectivité
- Seule la vidéo pré-enregistrée peut être utilisée ([guide d'enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Autres participants sur site – Meilleures pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même emplacement que l'appareil photo 360°, une gestion minutieuse de l'**audio et de la bande passante** est cruciale :  

- Chaque smartphone, tablette ou ordinateur portable connecté sur site consomme la bande passante réseau et peut affecter négativement le flux de l'appareil photo 360°.  
- Plusieurs microphones et haut-parleurs au même endroit peuvent causer une **rétroaction audio**, rendant l'expérience de la réunion désagréable pour tous les participants.

#### Autres participants sur site – Meilleures pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même emplacement que l'appareil photo 360°, une gestion minutieuse de l'**audio et de la bande passante** est cruciale :  

- Chaque smartphone, tablette ou ordinateur portable connecté sur site consomme la bande passante réseau et peut affecter négativement le flux de l'appareil photo 360°.  
- Plusieurs microphones et haut-parleurs au même endroit peuvent causer une **rétroaction audio**, rendant l'expérience de la réunion désagréable pour tous les participants.

Pour relever ces défis, suivez ces **meilleures pratiques** :

- **Utilisez des écouteurs filaires ou sans fil :** De préférence avec réduction du bruit pour prévenir l'écho et la rétroaction.  
- **Mode sur site :** Rejoignez la réunion en mode sur site lorsque vous êtes physiquement présent près de l'appareil photo 360°.  
  - Ce mode est optimisé pour une utilisation sur site :  
    - Désactive le micro et le haut-parleur du participant par défaut.  
    - N'envoie **pas** le flux de caméra du participant.  
    - N'affiche **pas** le flux de l'appareil photo 360° dans le navigateur du participant.  
    - Économise la bande passante réseau, en garantissant que l'appareil photo 360° dispose du maximum de bande passante en montée disponible pour la diffusion en direct.  
    - Utile lorsqu'un utilisateur veut partager des détails spécifiques ; vous **pouvez partager votre caméra en retour** pour des vues ciblées.  
- **Désactiver le micro lorsque vous ne parlez pas activement :** Prévient les rétroactions audio indésirables et les distractions.  
- **Utilisez un réseau séparé si possible :** Ayez votre smartphone connecté à un réseau différent de celui de l'appareil photo pour réduire les interférences.  

Suivre ces directives garantit une visite en direct fluide et de haute qualité pour les participants sur site et à distance.### 5.3 Application Avatour Camera

Voici (1) le menu de niveau supérieur, (2) les paramètres et (3) les menus des paramètres réseau.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Application Avatour Camera 360° - 3 menus*

**Capture rapide** - Pour l'enregistrement vidéo 360° hors ligne. - Pour une description détaillée, consultez [Comment enregistrer et télécharger des vidéos 360 avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Nous recommandons d'utiliser un appareil audio externe (connecté via Bluetooth). N.B. Vous pouvez également enregistrer des vidéos et des photos 2D standard - il suffit de changer le mode entre 360° et 2D dans le coin inférieur droit une fois sur l'écran QC.

**Réunion en direct** - Pour la vidéoconférence 360° en direct. Vous verrez vos espaces de travail et en cliquant sur l'un d'eux, vous lancerez le flux vidéo en direct à partir de la caméra 360°. Avant de pouvoir rejoindre la réunion avec votre caméra 360°, vous devez connecter un appareil audio via Bluetooth. Pour une description détaillée, consultez [Comment démarrer une réunion Live Capture avec votre caméra Pilot ?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Lors de l'organisation d'une réunion Live Capture avec votre caméra 360, vous aurez accès à des outils de réunion similaires à ceux de l'expérience web. Voici un lien vers notre article de la base de connaissances qui explique ces outils plus en détail : [Outils de l'application Opérateur](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galerie** - Retrouvez ici toutes vos vidéos et photos 360° à télécharger vers la console Web Avatour.

**Paramètres** - Dans les paramètres, vous avez les options suivantes :

- **Réseau** : Cette option vous permet de modifier le réseau WiFi auquel la caméra est connectée ou d'effectuer un test de connexion réseau pour vérifier votre débit de streaming
- **Live Capture** : Ajustez vos paramètres de Live Capture en fonction de la bande passante disponible, de la sensibilité VR de vos invités ou de l'installation des lentilles de protection de votre caméra :
  - **Fréquence d'images cible** : Ajustez la fréquence d'images pour votre vidéo Live Capture entre 15 fps, 24 fps et 30 fps. Des fréquences d'images plus élevées produisent une vidéo plus fluide, mais nécessitent une plus grande bande passante de téléchargement. Par défaut : 15 fps
  - **Débit binaire cible** : Vous permet d'augmenter ou de diminuer le débit binaire de streaming maximal pour votre Live Capture. Vous pouvez définir votre débit binaire cible entre 1 Mbps et 10 Mbps. Des débits binaires plus élevés entraîneront une résolution vidéo plus élevée, mais nécessiteront une plus grande bande passante de téléchargement. Par défaut : 5 Mbps
  - **Optimiser le mouvement** : Cela diminuera la fréquence d'images de la vidéo, générant une charge réduite sur la bande passante de téléchargement de votre réseau, et augmentera votre débit de streaming. De plus, cette option aide à réduire le mal des transports pour les participants en RV. Par défaut : Désactivé
  - **Lentilles de protection** : Cela affectera la manière dont la vidéo 360° est assemblée selon que des lentilles de protection ont été installées sur votre caméra. Si vous n'avez pas de lentilles de protection, définissez cette option sur « Non ». Si vous avez reçu un Kit 3.0, vous avez des lentilles de protection pré-installées et devez définir cette option sur « Oui ». Par défaut : Oui

- **Capture rapide** : Ajustez vos paramètres de Capture rapide en fonction de votre fréquence d'images vidéo préférée, de la bande passante disponible pour les téléchargements de vidéos enregistrées ou de l'installation des lentilles de protection de votre caméra. La Capture rapide a une résolution définie de 4K, ce qui offre généralement un bon équilibre entre la qualité vidéo et la taille du fichier. (Pour des résolutions plus élevées, vous pouvez utiliser les applications caméra natives, également sur le PanoX V2, pour plus de détails, consultez [Comment enregistrer et télécharger des vidéos 360 avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)) :
  - **Fréquence d'images cible** : Ajustez la fréquence d'images pour vos enregistrements vidéo de Capture rapide entre 15 fps, 24 fps et 30 fps. Des fréquences d'images plus élevées produisent une vidéo plus fluide, mais augmenteront la taille du fichier vidéo et le temps de téléchargement. Recommandé : 30 fps
  - **Débit binaire cible** : Définissez le débit binaire cible pour les téléchargements de Capture rapide entre 5 Mbps et 20 Mbps. Les débits binaires plus faibles augmentent les vitesses de téléchargement, mais diminueront la qualité vidéo. Recommandé : 20 Mbps
  - **Lentilles de protection** : *Voir la section Lentilles de protection pour Live Capture ci-dessus*
- **À propos** : Afficher le numéro de série de l'appareil et la version du logiciel

**Compte** - Pour vous connecter avec votre compte hôte ou administrateur Avatour.## 6. Conseils de bonnes pratiques {#best-practice-advice}

### 6.1 Premiers usages (informels) et familiarisation

Pour vos premiers usages et votre familiarisation avec la console web Avatour et le kit Avatour Turnkey, nous recommandons les étapes suivantes :

1. Ramenez le kit chez vous et jouez avec lui en famille et entre amis en utilisant votre connexion Internet domestique.
2. Apportez le kit au bureau et connectez-vous à un réseau d'entreprise (des problèmes d'entreprise pourraient émerger, par exemple les pare-feu d'entreprise - mais vous savez à partir de l'étape un qu'Avatour fonctionne et c'est un sujet à résoudre par votre équipe informatique avec l'aide d'Avatour).
3. Commencez à utiliser Avatour sur site (en dehors de votre bureau) au lieu de réunion auquel les participants distants devraient généralement se déplacer. D'autres questions de connectivité pourraient émerger. Avatour pour vous aider en coopération avec votre équipe informatique.
4. Commencez à utiliser avec des participants distants internes et externes.### 6.2 Avant une réunion en direct en vidéo 360°

- Nous recommandons de faire une visite vidéo 360° enregistrée avant toute visite en direct si le temps le permet, pour trois raisons : (1) Avoir une solution de secours pour la visite en direct, (2) avoir quelque chose pour la documentation et l'examen ultérieur (en plus de la visite en direct enregistrée) et (3) commencer à créer une bibliothèque de vidéos 360° de tous vos sites qui peut être utile pour de nombreux cas d'usage.
- Tous les composants du kit doivent être chargés pendant au moins 90 minutes avant la réunion en direct. Nous recommandons de toute façon d'avoir tous les appareils en charge continue quand ils ne sont pas utilisés. De cette façon, tous les appareils seront toujours prêts, aussi pour les réunions ad hoc non planifiées.
- Avoir le kit complètement assemblé (1. base de trépied + 2. batterie Ulanzi + 3. bâton extensible + 4. caméra 360°).

- Confirmez qu'un espace de travail est créé pour accueillir une réunion en direct et incluez tous les éléments pertinents.

- Invitez tous les participants à la réunion via votre espace de travail. Cela crée une invitation sur les calendriers de tous les participants et inclut le lien d'invitation à la réunion.

- Associez et connectez vos écouteurs Bluetooth ou votre haut-parleur que vous prévoyez d'utiliser pour votre visite à la caméra.

- Tous les utilisateurs de smartphones sur site doivent se connecter à partir d'un réseau différent du réseau de la caméra. Cela réduira la charge sur la bande passante du réseau de la caméra.

- Si vous êtes seul en tant qu'opérateur de caméra, apportez un smartphone avec vous au cas où vous voudriez partager la caméra du smartphone et montrer les détails fins.

- Confirmez que la caméra 360° peut se connecter à votre WiFi local.

- Avant une réunion Avatour, planifiez l'itinéraire que vous emprunterez dans l'établissement. Faites une réunion Avatour de test avec la caméra et vérifiez que toutes les zones ont des débits supérieurs à 1 Mbps de bande passante. Cela peut être vu sur l'écran de la caméra lui-même, ou en tant que participant distant en allant dans Paramètres et en activant Afficher le débit.

- Si vous remarquez que certaines zones ont peu ou pas de bande passante, il est préférable de prendre des images ou un enregistrement. Ceux-ci peuvent ensuite être présentés pendant la réunion pour que les participants distants les examinent. Vous pouvez suivre le guide ici qui explique notre Capture rapide pour l'enregistrement et le téléchargement de vidéos/images : [Comment enregistrer et télécharger des vidéos 360 avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si vous avez des participants distants rejoignant la réunion qui n'ont jamais utilisé Avatour, fournissez-leur un bref résumé de la plateforme, de ses fonctionnalités (vidéo en direct 360°, éléments, instantanés, annotations, spotlight) et des outils de réunion.

- Vous pouvez commencer par une autre solution de vidéoconférence (par exemple Teams, Zoom, Google Meet) mais avant de passer à Avatour, fermez complètement l'autre application de vidéoconférence. Dans certains cas, ces autres applications prioritaireront le microphone/les haut-parleurs/la webcam de votre appareil, ce qui les désactivera pour Avatour. De plus, ne lancez PAS Avatour ET une autre vidéoconférence en même temps, car cela réduira la bande passante disponible.

- Si vous prévoyez d'utiliser la caméra 360° dans un environnement à haute température, il est recommandé d'utiliser le module de refroidissement (Pilot Pano uniquement). Cela aidera à réduire les risques de surchauffe de la caméra et d'arrêt automatique.### 6.3 Lors du fonctionnement de la caméra sur site pour une réunion vidéo en direct 360°

- Lors du fonctionnement de la caméra, assurez-vous de marcher lentement. Cela aide à la qualité vidéo et réduit tout risque d'arrêt vidéo potentiel lorsque la connexion réseau de la caméra bascule entre les points d'accès WiFi.

- Tenez la caméra devant vous et au-dessus du niveau des yeux. Cela permet à tous les participants distants de voir la majorité de votre environnement.

- Pour les cas où la caméra doit rester stable, utilisez le trépied et étendez la caméra à la bonne hauteur, idéalement au niveau des yeux.

- Connectez toujours la caméra à votre réseau WiFi local si possible. Pour les zones sans accès WiFi, utilisez le point d'accès fourni. Le point d'accès dispose d'une carte SIM qui se connectera à un réseau cellulaire fiable près de vous. Maintenez toujours le point d'accès éteint lorsqu'il n'est pas utilisé à l'intérieur, sinon la caméra 360° pourrait se connecter au point d'accès, ce que nous ne voulons pas à l'intérieur. À l'extérieur, gardez le point d'accès près de la caméra 360°.

- Lorsque le débit binaire de la caméra commence à chuter en dessous de 2 Mbps, marchez plus lentement ou arrêtez-vous complètement jusqu'à ce que le signal se stabilise à nouveau. Cela se produit généralement lorsque vous passez d'un point d'accès WiFi à un autre.

- Si vous savez que la connectivité et la vidéo s'interrompront lors du déplacement vers un endroit spécifique (Exemple : passage d'une zone de production intérieure à une zone extérieure), informez à l'avance les participants distants.

- Si vous devez montrer quelque chose en détail ou avec une petite écriture, utilisez votre propre smartphone ou celui d'un participant sur site pour rejoindre la réunion et présenter votre / son caméra arrière du téléphone.

- Si possible, nous recommandons qu'une personne supplémentaire soit sur site pour aider au partage de caméra de smartphone décrit ci-dessus, car cela s'avère souvent utile / nécessaire.

- Idéalement, les utilisateurs de smartphones sur site doivent rejoindre la réunion (1) en mode sur site et (2) sur un réseau différent de celui utilisé par la caméra pour ne pas consommer la bande passante de téléchargement cruciale de la caméra 360°.

- Tous les participants sur site qui se connectent à partir de leur smartphone doivent être en sourdine, sauf s'ils parlent activement.