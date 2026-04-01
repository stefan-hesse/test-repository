# Avatour User and Best Practices Guide

## 1. Pour tous les utilisateurs d'Avatour {#for-all-avatour-users}

Si vous découvrez Avatour, les ressources suivantes offrent une introduction utile à la plateforme et à ses fonctionnalités :

1. [Vidéo Avatour Comment ça marche](https://avatour.com/how-it-works)  
Un bref aperçu des principales fonctionnalités d'Avatour et de la façon dont la plateforme permet une collaboration à distance immersive.
2. [FAQ](https://avatour.com/faqs)  
Réponses aux questions fréquemment posées.
3. [Glossaire](https://avatour.com/glossary)  
Définitions des termes et concepts clés d'Avatour fréquemment utilisés.
4. Site web  
Consultez notamment la page [Fonctionnalités d'Avatour](https://avatour.com/features) ainsi que les sections dédiées aux Cas d'utilisation et aux Industries pour découvrir comment Avatour peut répondre à vos besoins spécifiques.

## 2. Types d'utilisateurs Avatour  {#avatour-user-types}

### 2.1 Participants aux réunions (Aucun compte requis)
Les utilisateurs peuvent rejoindre la réunion sans créer de compte Avatour.
Exception : Si l'hôte a restreint la réunion aux utilisateurs enregistrés — par exemple, pour n'autoriser que les employés internes à rejoindre via l'authentification unique (SSO) — l'invitation du calendrier indiquera que les participants doivent se connecter pour s'authentifier.

Les utilisateurs accèdent à la réunion comme suit :

- Recevoir une invitation de calendrier de l'hôte.
- Utiliser le lien de réunion dans l'invitation pour rejoindre.
- Entrer un mot de passe de réunion si l'hôte en a activé un.
- Les participants peuvent rejoindre sans compte Avatour sauf si la réunion est restreinte et nécessite une connexion pour s'authentifier.

#### 2.1.1 Participant 

- Peut rejoindre et interagir pleinement (webcam, microphone, chat et fonctionnalité Présenter).
- Maximum de 20 participants interactifs par réunion.

#### 2.1.2 Spectateur

- Peut visualiser la réunion et participer uniquement via le chat.
- Ne peut pas partager de vidéo, utiliser un microphone, présenter, lire/mettre en pause les Assets, ou capturer des Snapshots.
- Maximum de 10 Spectateurs par réunion.
- Avec les Participants, une réunion peut accueillir jusqu'à 30 participants.

### 2.2 Utilisateurs enregistrés

Les Utilisateurs enregistrés disposent d'un compte Avatour. Les comptes sont créés de l'une des manières suivantes :

- **Invité par un Admin :** Lors de l'intégration, Avatour configure un **tenant dédié** pour l'organisation et crée un ou plusieurs **comptes Admin**. Les Admins peuvent ensuite **inviter des utilisateurs** au sein de l'organisation et les assigner à des **groupes**, qui définissent leur rôle sur la plateforme (Invité, Hôte ou Admin). Les utilisateurs invités reçoivent un **lien d'inscription** pour finaliser la configuration du compte et définir un mot de passe.  
- **Invité par un Hôte :** Les Hôtes peuvent ajouter des utilisateurs comme **collaborateurs Éditeur** à un Workspace. Cela consomme une **licence Hôte** et garantit que l'utilisateur dispose d'un accès de niveau Hôte.  
- **Provisionnement automatique SSO (niveau Enterprise/Business uniquement) :** Les comptes peuvent être automatiquement créés par l'IdP. Par défaut, les comptes provisionnés par SSO sont ajoutés au **groupe Invité**, sauf si cela est remplacé via les **mappages de groupes SAML**. Les Admins peuvent toujours inviter des utilisateurs et assigner l'appartenance aux groupes directement même lorsque le SSO est activé.

**Résumé :**  

Les utilisateurs enregistrés et leur appartenance aux groupes peuvent être gérés de plusieurs manières :

- **Gestion par Admin :** Un Admin dans la console Avatour peut créer des utilisateurs et les assigner à des groupes, qui définissent leur rôle sur la plateforme (Invité, Hôte ou Admin).  
- **Provisionnement SSO :** Pour les clients de niveau Enterprise ou Business avec SSO activé, l'IdP peut automatiquement provisionner les comptes et assigner l'appartenance aux groupes, ce qui définit le rôle de l'utilisateur sur la plateforme.  
- **Utilisateurs invités par un Hôte :** Les Hôtes peuvent inviter d'autres utilisateurs comme collaborateurs Éditeur à des Workspaces spécifiques. L'attribution du rôle de collaborateur Éditeur consomme une licence Hôte.

**Bonne pratique recommandée (Clients Enterprise) :**  
Pour les organisations qui prévoient un grand nombre d'utilisateurs ayant besoin d'accéder à Avatour, il est recommandé d'**intégrer l'authentification unique (SSO)** et de gérer les utilisateurs et les appartenances aux groupes depuis l'**IdP**. Cette approche simplifie le provisionnement des comptes, l'attribution des groupes et la gestion des licences, réduisant la charge administrative et assurant un contrôle d'accès cohérent.

#### 2.2.1 Utilisateurs Invités

- Ajoutés au **groupe Invité**.  
- Peuvent **visualiser les Assets** dans les Workspaces où ils ont été ajoutés comme **collaborateurs Lecteur**.  
- Ne peuvent pas créer de workspaces, héberger de réunions ou télécharger de contenu.  
- Les comptes Invité provisionnés par SSO **s'authentifient via l'IdP** ; aucun mot de passe géré par Avatour n'est requis.

---

#### 2.2.2 Utilisateurs sous licence (Accès à la console Web)

##### Utilisateurs Hôte (Groupe : Hôte)

- Peuvent créer/gérer des Workspaces, inviter des collaborateurs à un workspace, **héberger des réunions en direct**, télécharger des **Quick Captures**.  
- Ont accès au **Tableau de bord Hôte** et à l'**Application Opérateur** sur les caméras 360° compatibles.  

##### Utilisateurs Admin (Groupe : Admin)

- Incluent toutes les capacités Hôte plus l'administration complète du compte.

**Les privilèges Admin supplémentaires incluent :**

**Gestion des comptes**  

- Créer de nouveaux utilisateurs et les assigner à des groupes.
- Réinitialiser les mots de passe lorsqu'ils sont gérés par Avatour (non applicable lorsque le SSO est activé). 
- Promouvoir les utilisateurs Invités en Hôte.  
- Désactiver des utilisateurs (les comptes Admin doivent d'abord être convertis en Hôte avant suppression).  
- Transférer les assets d'un utilisateur Hôte à un autre lors de la suppression.

**Paramètres**  

- Configurer les **paramètres de sécurité à l'échelle de l'organisation** pour les assets, les workspaces et les réunions hébergées sur la plateforme (par ex., si un Hôte doit être présent pour démarrer une réunion, si les visages doivent être floutés sur toutes les vidéos téléchargées sur la plateforme).  
- Activer ou désactiver les **fonctionnalités IA** ou l'**enregistrement**.  
- Appliquer l'image de marque de l'entreprise de manière cohérente sur la plateforme si un **domaine personnalisé** est configuré.
  

**Assets et Analytiques** 
 
- Visualiser tous les Assets téléchargés par n'importe quel utilisateur de l'organisation.  
- Examiner l'utilisation de la plateforme à travers l'organisation.

---

#### 2.2.3 Permissions des collaborateurs de Workspace

Les permissions de Workspace définissent ce qu'un utilisateur peut faire **au sein d'un Workspace spécifique**. Celles-ci sont distinctes de l'appartenance aux groupes au niveau de la plateforme (Invité, Hôte, Admin).

- **Collaborateur Éditeur :** Les utilisateurs avec cette permission peuvent :
  - Gérer les Assets (télécharger, supprimer, flouter les visages, générer des résumés)  
  - Gérer les paramètres de réunion (activer/désactiver l'enregistrement, autoriser ou retirer des participants)  
  - Planifier et héberger des réunions en direct  
  - Générer des rapports basés sur des modèles prédéfinis  
  - Ajouter ou retirer des collaborateurs du Workspace  

- **Collaborateur Lecteur :** Les utilisateurs avec cette permission ont un accès en lecture seule aux Assets du Workspace. Ils **ne peuvent pas modifier les Assets, gérer les réunions ou gérer les collaborateurs**, mais ils **peuvent créer des Notes sur les Assets**. 
  
## 3. Pour les participants aux réunions à distance et les visiteurs de l'espace de travail {#for-remote-meeting-participants-and-workspace-visitors}
Avatour permet aux utilisateurs de collaborer de deux façons principales :

- **Rejoindre une réunion Avatour (Collaboration Synchrone) :**  
  Vous pouvez recevoir une **invitation de calendrier** pour rejoindre une réunion Avatour. Pendant la réunion, les participants peuvent mener une **visite de site distante en direct** ou examiner ensemble les ressources de manière synchrone.

- **Visiter un Workspace (Collaboration Asynchrone) :**  
  Vous pouvez également être invité en tant que **collaborateur à un Workspace** pour examiner les ressources **de manière asynchrone** (à votre propre rythme).### 3.1 Comment rejoindre une réunion Avatour et visiter un espace de travail Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 N'importe quel appareil « écran plat » avec navigateur Web {#any-flat-screen}
Vous pouvez rejoindre une réunion Avatour à partir de **n'importe quel ordinateur de bureau ou portable, smartphone ou tablette** en utilisant un navigateur Web.  

##### Rejoindre une réunion Avatour

> **Remarque :** Rejoindre une réunion Avatour nécessite que vous **accordiez les autorisations du microphone**. Veuillez accepter les invites d'autorisation de votre navigateur.

1. **Via invitation de calendrier (recommandé) :**  
   - Vous recevrez généralement une **invitation de calendrier** avec un **lien de participation directe** (par exemple : `https://avatour.live/join?s=xxxxx`).  
   - Cliquer sur le lien remplira automatiquement le **code de réunion à 5 caractères** et vous accèdera à la réunion.
   - **Authentification requise :** Certaines réunions sont réservées aux utilisateurs enregistrés. Dans ce cas, l'invitation indiquera que vous devez **vous connecter pour accéder à la réunion**.  
   - **Réunions protégées par mot de passe :** Certaines réunions peuvent nécessiter un mot de passe. Dans ce cas, l'invitation comprendra le mot de passe que vous devez entrer pour rejoindre.

2. **Via code de réunion :**  
   - Si l'hôte partage un **code de réunion à 5 caractères** séparément, allez à [https://avatour.live/join](https://avatour.live/join), entrez votre **nom** et le **code de réunion**, et rejoignez la réunion.  
   - Si la réunion est **protégée par mot de passe**, entrez le mot de passe fourni par l'hôte.  
   - Si la réunion nécessite une **authentification**, vous devrez **vous connecter avec votre compte Avatour** avant de rejoindre.

> **Conseil 1 :** Si votre caméra ou microphone ne fonctionne pas, il se peut qu'il soit utilisé par une autre application (par exemple Microsoft Teams ou Zoom). Fermez les applications qui pourraient utiliser votre caméra ou microphone, puis quittez et rejoignez la réunion Avatour.  

> **Conseil 2 :** Si vous ne pouvez toujours pas rejoindre la réunion, exécutez ce test : [https://avatour.live/test](https://avatour.live/test).  
> Le test peut identifier si votre **pare-feu ou réseau d'entreprise** bloque l'accès, et fournira des informations pour guider les discussions avec votre équipe informatique.  

> **Conseil 3 :** N'utilisez **pas** les applications Avatour iOS ou Android pour rejoindre des réunions. Ces applications sont nécessaires uniquement lorsque vous **diffusez une réunion en direct à partir d'une caméra Insta360**, car ces caméras ne peuvent pas exécuter directement le logiciel Avatour 360° et nécessitent un smartphone pour l'assistance.

##### Visiter un espace de travail Avatour (sans rejoindre une réunion Avatour)

Vous pouvez accéder à un espace de travail de l'une des manières suivantes :

- **Espace de travail public :**  
  Si l'espace de travail est public, le lien peut être consulté directement — aucune connexion requise.

- **Espace de travail restreint :**  
  Si l'espace de travail est restreint, vous devez être ajouté en tant que **collaborateur** avec les autorisations **Éditeur** ou **Lecteur**.

  1. Lorsque vous êtes ajouté en tant que collaborateur, vous recevrez une **notification par e-mail** avec un lien vers l'espace de travail.
  2. Cliquez sur le lien dans l'e-mail pour ouvrir l'espace de travail. Si vous n'êtes pas déjà connecté, vous serez invité à **vous connecter ou à terminer l'inscription**.
  3. Une fois connecté, l'espace de travail s'ouvrira automatiquement.

  Vous pouvez également vous connecter à [https://avatour.live/login](https://avatour.live/login) et accéder à l'espace de travail à partir de votre **liste d'espaces de travail**.

#### 3.1.2 Casque VR {#vr-headset}
Vous pouvez rejoindre une réunion et visiter un espace de travail à partir d'une gamme de casques Meta et Pico compatibles. Pour ce faire : 

1. Installez notre application Avatour à partir de votre boutique d'applications VR respective : [Comment installer l'application Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Chargez notre application et entrez le code de réunion ou sélectionnez un espace de travail pour rejoindre une réunion. Pour plus d'informations sur comment utiliser notre application VR, consultez notre article de la base de connaissances [ici](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Outils de réunion et de collaboration d'espace de travail {#meeting-tools}

Avatour permet la collaboration dans deux contextes principaux :

1. **Réunions (synchrone) :** Collaborez en temps réel avec d'autres participants, y compris les visites de site en direct ou l'examen ensemble des actifs enregistrés.  
2. **Espaces de travail (asynchrone) :** Examinez et interagissez avec les actifs selon votre propre calendrier, 24h/24, 7j/7.

Les **outils de collaboration sont largement similaires** entre les réunions et les espaces de travail, avec quelques différences dues au contexte synchrone par rapport asynchrone.

#### 3.2.1 Disposition de l'interface

L'interface Avatour est organisée autour de trois zones principales :

- **Panneau gauche** – Actifs de l'espace de travail et outils de support  
- **Canevas central** – Zone d'affichage principale pour la vidéo en direct ou les actifs  
- **Panneau droit** – Informations contextuelles, telles que les participants, les réunions ou le chat  

La plupart des interactions sont initiées à partir du **menu inférieur**.  
En cliquant sur une option de menu, un **panneau latéral** s'ouvre sur le côté gauche ou droit de l'écran, tandis que le **canevas central** reste la zone d'affichage principale.

---
#### 3.2.2 Exemple de vue de réunion

Voici un exemple de vue dans une réunion Avatour :

![Interface de réunion Avatour avec panneau des actifs, canevas vierge et panneau des participants](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Réunion Avatour avec panneau des actifs (gauche), canevas (centre) et panneau des participants (droite)*

---

#### 3.2.3 Exemple de vue d'espace de travail

Voici un exemple de vue d'espace de travail :

![Espace de travail Avatour avec panneau des actifs, canevas vierge et panneau des réunions](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espace de travail Avatour avec panneau des actifs (gauche), canevas (centre) et panneau des réunions (droite)*

---

#### 3.2.4 Aperçu du menu inférieur

Le menu inférieur donne accès aux commandes d'interface principales et aux panneaux :

**Menu inférieur de réunion**  

![Menu inférieur de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu inférieur de réunion Avatour*

- **Actifs** – Examinez les fichiers de l'espace de travail, y compris les vidéos enregistrées, les images, les captures d'écran et les fichiers PDF. 
- **Chat** – Envoyez des messages à tous les participants de la réunion.  
- **Caméra** – Activez ou désactivez votre webcam.  
- **Microphone** – Sourdinez ou réactivez votre son.  
- **Présenter** – Présentez un actif, un bureau ou un flux webcam (voir la section Présenter ci-dessous).  
- **Outils d'animateur** (animateurs uniquement) :  
  - **Verrouiller la vue** – Verrouillez la vue pour tous les participants.  
  - **Rendre tout muet** – Sourdinez tous les participants.  
- **Activer le plein écran** – Rendez l'onglet de réunion en plein écran.  
- **Quitter la réunion** – Quittez la réunion.  
- **Démarrer l'enregistrement** – Utilisez ce bouton pour démarrer et arrêter manuellement l'enregistrement lors d'une réunion. Vous pouvez également enregistrer les réunions automatiquement si **l'enregistrement automatique** est activé dans les paramètres de l'espace de travail. Dans les deux cas, les enregistrements sont sauvegardés dans les actifs de l'espace de travail.
- **Carte** – Ouvrez ou fermez le panneau de carte pour les actifs avec une piste GPS. En cliquant sur un emplacement, vous accédez au moment exact dans la vidéo. La carte se met à jour en temps réel à mesure que la vidéo se lit.
- **Participants** – Ouvrez ou fermez le panneau des participants.  
- **Informations de réunion** – Consultez le code de réunion, le lien d'invitation et accédez aux tutoriels connexes.  

![Informations de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panneau latéral d'informations de réunion Avatour*

- **Paramètres** – Ajustez les paramètres de langue, audio et vidéo. Pour les réunions vidéo en direct à 360°, utilisez **Afficher le débit** pour surveiller les statistiques de connectivité.

> Conseil : Envoyez le lien de réunion ou ajoutez-le à un élément de calendrier pour inviter des participants.

---

##### Menu Présenter

L'option **Présenter** dans le menu inférieur de réunion vous permet de partager du contenu avec tous les participants.

- **Caméra** – Partagez votre caméra de smartphone/tablette. Ceci peut également être utilisé lors d'une réunion vidéo en direct à 360° pour superposer une vue secondaire pour les gros plans ou les détails spécifiques. 
- **Bureau** – Partagez votre écran de bureau avec tous les participants.  
- **Actif** – Présentez un actif de l'espace de travail. La sélection d'un actif ouvre la **barre d'outils des actifs**, qui fournit des commandes de lecture et des outils de collaboration spécifiques à l'actif en cours de présentation.

##### Barre d'outils des actifs (Réunion)

Lors de la présentation d'un actif lors d'une réunion, la **barre d'outils des actifs** apparaît au-dessus du canevas. Voici les outils et éléments de menu disponibles lors de <u>la présentation d'un actif lors d'une réunion</u> - expliqués de gauche à droite.

![Menu Avatour lors de la présentation d'un actif lors d'une réunion](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour lors de la présentation d'un actif lors d'une réunion*


- **Chronologie vidéo / Barre de progression** – Affiche la progression vidéo avec les notes et les sujets clés extraits de l'audio. Cliquez sur une note ou un sujet pour accéder à ce moment-là et ouvrir la note. Inclut les commandes **Lecture / Pause**.   
- **Capture d'écran** – Capturez une image à 360° ou 2D à partir de l'actif.  
- **Projecteur** – Mettez en évidence une zone spécifique pour tous les participants lors des sessions en direct.  
- **Afficher/Masquer le point de vue (POV)** – Affichez où chaque participant regarde dans la vidéo à 360°.  
- **Notes** – Créez des notes ancrées à des moments spécifiques dans l'actif. Les notes peuvent être catégorisées (Observation, Problème, Action, Recommandation), suivies par statut (Ouvert → En cours → Résolu) et partagées via des liens directs.  

  ![Note et filtres de notes Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Note et filtres de notes Avatour*

  - **Notes par commande vocale** – Il s'agit de textes d'espace réservé générés automatiquement lorsque l'enregistrement détecte des mentions telles que « insérer une note », « prendre une note » ou « faire une note ». Ces notes apparaissent sur la chronologie et doivent être **positionnées et finalisées** par l'utilisateur. 

  ![Notes Avatour - Générées par commande vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notes Avatour - Générées par commande vocale*

- **Panneau des notes et du résumé** – Ouvre un panneau latéral qui affiche toutes les notes, les sujets clés et un résumé exécutif pour l'actif. En cliquant sur un élément, vous accédez à ce moment-là dans la vidéo.  

  ![Résumé exécutif des actifs Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Résumé exécutif Avatour lors de la présentation d'un actif lors d'une réunion*

  ![Sujets Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Sujets Avatour lors de la présentation d'un actif lors d'une réunion*

  À partir du **panneau latéral**, vous pouvez **imprimer un rapport d'actif** ou le **télécharger en TXT ou CSV**. Les rapports peuvent inclure des notes, des sujets générés par l'IA et des transcriptions complètes. Vous pouvez également **choisir quels éléments inclure** avant l'exportation.  

  ![Menus d'impression de rapport d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menus d'impression / téléchargement de rapport d'actif Avatour*  

  ![Menu de sélection des éléments du rapport d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menu de sélection des éléments du rapport d'actif Avatour*

- **Lien de partage** – Partagez un lien vers une note ou une scène spécifique dans l'actif.  
- **Sous-titres codés (CC)** – Affichez la transcription textuelle à l'écran lors de la lecture vidéo.

##### Barre d'outils des actifs (Espace de travail)

Lors de l'examen d'un actif dans un espace de travail, la barre d'outils est similaire mais optimisée pour un usage individuel :

![Menu Avatour lors de la présentation d'un actif en dehors d'une réunion, par exemple lors de la visite d'un espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour lors de la présentation d'un actif dans un espace de travail*

- **Chronologie vidéo / Barre de progression** – Affiche la progression vidéo avec les notes et les sujets clés extraits de la piste audio. Cliquez n'importe où sur la chronologie pour scrubber dans la vidéo. Cliquez sur une note ou un sujet pour accéder à ce moment-là et ouvrir la note. Inclut les commandes **Lecture / Pause**.  
- **Capture d'écran, Notes, Panneau Notes et résumé, Lien de partage, Sous-titres codés**  
- Non disponible : **Projecteur, POV** (ces éléments nécessitent des participants en direct)  
- Commandes supplémentaires :
  - **Étapes de 10 secondes** – Avancez/reculez  
  - **Vitesse de lecture** – Ajustez la vitesse (0,5× à 2×)  
  - **Rogner la vidéo** – Rognez le début ou la fin de l'actif## 4. Pour les utilisateurs Host et Admin - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}
Lorsque vous vous connectez à votre compte utilisateur Avatour, vous accédez à la **Console Web**.### 4.1 Console Web - Aperçu du menu principal {#web-console-overview-main-menu}

Sur le côté gauche, vous verrez les éléments de menu suivants :

![Console Web Avatour - Menu principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu principal*

- **Espaces de travail** – Organisez votre contenu efficacement. Chaque espace de travail contient **Ressources**, **Collaborateurs**, **Réunions** et **Paramètres**.  
- **Ressources** – Accédez et gérez toutes vos ressources (vidéos, images, PDF). Les administrateurs peuvent voir toutes les ressources du compte, et les ressources partagées sont visibles par tous les utilisateurs.  
- **Profil** – Gérez votre langue et votre mot de passe.  
- **Analytique** – Suivez l'activité des sessions, l'utilisation de l'espace de travail et les métriques de retour sur investissement.  
- **Paramètres** *(Administrateur uniquement)* – Configurez les paramètres par défaut de l'espace de travail, des réunions et des ressources dans toute l'organisation. Les administrateurs peuvent également personnaliser la marque (logo, couleurs, arrière-plans).  
- **Compte** *(Administrateur uniquement)* – Gérez les utilisateurs enregistrés et les caméras 360°.  
- **Connexion d'appareil** – Entrez le code affiché sur votre caméra 360° pour l'associer à votre compte.  
- **Tutoriels** – Accédez aux tutoriels guidés.  
- **Se déconnecter** – Quittez la console.

> Les sections telles que Profil, Connexion d'appareil, Tutoriels et Se déconnecter sont explicites et n'ont pas de sous-sections détaillées.

---### 4.2 Console Web - Détails par élément de menu (avec images) {#web-console-details-by-menu-item}

#### 4.2.1 Espaces de travail

Les espaces de travail sont des unités organisationnelles flexibles qui vous permettent de gérer les ressources, les collaborateurs et les réunions en un seul endroit. Vous pouvez créer un nouvel espace de travail avec le bouton **Nouvel espace de travail** dans le coin supérieur droit.

![Avatour Web Console - Élément de menu principal Espaces de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Élément de menu principal Espaces de travail*

Cliquez sur l'icône de cloche pour voir un résumé de l'activité de l'espace de travail au cours des 7 derniers jours.

![Avatour Web Console - Activités récentes de l'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Activités récentes de l'espace de travail*

À l'intérieur d'un espace de travail :

![Avatour Espace de travail avec panneau Ressources, canevas vierge et panneau Réunions](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espace de travail avec Ressources (gauche), Canevas (centre), Réunions (droite)*

- **Ressources** – Gérez les fichiers alloués à cet espace de travail.  
- **Collaborateurs** – 
  Contrôlez l'accès aux espaces de travail par 
  - **Observateur** – Peut afficher les ressources. L'invitation crée un utilisateur Invité si nécessaire.  
  - **Éditeur** – Contrôle complet de l'espace de travail, mêmes droits que l'Hôte. L'invitation élève l'utilisateur à Hôte si nécessaire.  
> Plusieurs utilisateurs peuvent accéder à un espace de travail simultanément sans réunion. Les espaces de travail publics et les paramètres d'accès aux réunions offrent un accès alternatif.  
- **Rapport** – Générez un rapport en utilisant un modèle de liste de contrôle sur les ressources de l'espace de travail sélectionné.  

![Rapport d'espace de travail Avatour et sélection de ressources](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Rapport d'espace de travail et sélection de ressources*

- **Carte** – Affichage des emplacements des ressources compatibles GPS sur une carte.  
- **Réunions** – Organisez des réunions dans l'espace de travail.  
- **Paramètres** – Configurez les paramètres par défaut de l'espace de travail et des réunions :

![Avatour Paramètres - Vue d'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Paramètres d'espace de travail*

**Paramètres d'espace de travail**

- **Modèle de rapport** – Sélectionnez le modèle de liste de contrôle pour les rapports IA.  
- **Activer les notifications** – E-mails quotidiens récapitulatifs pour les changements de statut des notes.  

![Notifications par courrier électronique - Exemple](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Exemple de notifications par courrier électronique*

- **Espace de travail public** – Toute personne disposant du lien peut afficher les ressources directement.

**Paramètres de réunion**
  
* **Authentification requise** – Les participants doivent se connecter.  
* **Autoriser l'accès en tant qu'invité** – Permettre aux utilisateurs non enregistrés d'afficher les ressources.  
* **Enregistrement automatique / Démarrage manuel** – Choisissez si les réunions s'enregistrent automatiquement ou sont démarrées manuellement.  
* **Hôte requis** – L'hôte doit admettre les participants ; la réunion se termine lorsque l'hôte part.  
* **Autoriser l'accès spectateur** – Rejoindre sans micro ni caméra ; communiquer via le chat.  
* **Réunions protégées par mot de passe** – Exiger un mot de passe pour participer.  
* **Afficher la question sur les économies de déplacement** – Demander aux participants si la réunion a réduit les déplacements.  

> Les paramètres peuvent être combinés (par exemple, aucun hôte requis mais protégé par mot de passe).

---

#### 4.2.2 Ressources

Gérez toutes les vidéos 360°/2D, les images et les fichiers PDF. Téléchargez/téléchargez des ressources, allouez-les à des espaces de travail, partagez avec d'autres utilisateurs, renommez, imprimez/téléchargez des rapports, activez le flou facial et le résumé IA.

![Avatour Web Console - Élément de menu principal Ressources](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Élément de menu principal Ressources*

---

#### 4.2.3 Analyse

Fournit des informations sur les réunions, l'utilisation de l'espace de travail et les métriques de ROI.

![Avatour Web Console - Élément de menu principal Analyse (1 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Aperçu de l'analyse*

![Avatour Web Console - Élément de menu principal Analyse (2 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Activité des réunions et utilisation de l'espace de travail*

![Avatour Web Console - Élément de menu principal Analyse (3 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilisation des licences d'appareils et ROI*## 5. Onsite - How to Use the Avatour Turnkey Kit {#onsite-how-to-use-the-avatour-turnkey-kit}

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
