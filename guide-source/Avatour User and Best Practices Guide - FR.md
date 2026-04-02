# Avatour User and Best Practices Guide

## Pour tous les utilisateurs d'Avatour {#for-all-avatour-users}
Si vous êtes nouveau chez Avatour, les ressources suivantes fournissent une introduction utile à la plateforme et ses capacités :

1. [Vidéo Avatour Comment ça marche](https://avatour.com/how-it-works)  
Un court aperçu des principales fonctionnalités d'Avatour et de la façon dont la plateforme permet la collaboration à distance immersive.
2. [FAQ](https://avatour.com/faqs)  
Réponses aux questions fréquemment posées.
3. [Glossaire](https://avatour.com/glossary)  
Définitions des termes et concepts clés d'Avatour fréquemment utilisés.
4. Site Web  
Consultez en particulier la page [Fonctionnalités d'Avatour](https://avatour.com/features) ainsi que les sections dédiées Cas d'usage et Secteurs d'activité pour découvrir comment Avatour peut soutenir vos besoins spécifiques.## 2. Types d'utilisateurs Avatour  {#avatour-user-types}

### 2.1 Participants à la réunion (Aucun compte requis)
Les utilisateurs peuvent rejoindre la réunion sans s'inscrire à un compte Avatour.
Exception : Si l'hôte a limité la réunion aux utilisateurs enregistrés — par exemple, pour permettre uniquement aux employés internes de rejoindre via Single Sign-On (SSO) — l'invitation du calendrier indiquera que les participants doivent se connecter pour s'authentifier.

Les utilisateurs accèdent à la réunion comme suit :

- Recevoir une invitation du calendrier de la part de l'hôte.
- Utiliser le lien de réunion dans l'invitation pour rejoindre.
- Entrer un mot de passe de réunion si l'hôte en a activé un.
- Les participants peuvent rejoindre sans compte Avatour sauf si la réunion est limitée et nécessite une connexion pour s'authentifier.

#### 2.1.1 Participant

- Peut rejoindre et interagir pleinement (webcam, microphone, chat et fonctionnalité Présent).
- Maximum de 20 participants interactifs par réunion.

#### 2.1.2 Spectateur

- Peut regarder la réunion et participer via le chat uniquement.
- Ne peut pas partager vidéo, utiliser un microphone, présenter, lire/mettre en pause les Ressources ou capturer des Instantanés.
- Maximum de 10 spectateurs par réunion.
- Avec les participants, une réunion peut accueillir jusqu'à 30 participants.### 2.2 Utilisateurs enregistrés

Les utilisateurs enregistrés disposent d'un compte Avatour. Les comptes sont créés de l'une des façons suivantes :

- **Invitation par Admin :** Lors de l'intégration, Avatour configure un **locataire dédié** pour l'organisation et crée un ou plusieurs **comptes Admin**. Les Admins peuvent ensuite **inviter des utilisateurs** au sein de l'organisation et les affecter à des **groupes**, qui définissent leur rôle sur la plateforme (Invité, Hôte ou Admin). Les utilisateurs invités reçoivent un **lien d'inscription** pour terminer la configuration du compte et définir un mot de passe.  
- **Invitation par Hôte :** Les Hôtes peuvent ajouter des utilisateurs en tant que **collaborateurs Éditeur** à un Workspace. Cela consomme une **licence Hôte** et garantit que l'utilisateur a accès au niveau Hôte.  
- **Auto-provisionnement SSO (niveaux Enterprise/Business uniquement) :** Les comptes peuvent être créés automatiquement par l'IdP. Par défaut, les comptes provisionés par SSO sont ajoutés au **groupe Invité**, sauf s'ils sont remplacés via des **mappages de groupes SAML**. Les Admins peuvent toujours inviter des utilisateurs et affecter l'appartenance à un groupe directement même lorsque SSO est activé.

**Résumé :**  

Les utilisateurs enregistrés et leur appartenance à un groupe peuvent être gérés de plusieurs façons :

- **Gestion par Admin :** Un Admin dans la console Avatour peut créer des utilisateurs et les affecter à des groupes, qui définissent leur rôle sur la plateforme (Invité, Hôte ou Admin).  
- **Provisionnement SSO :** Pour les clients de niveau Enterprise ou Business avec SSO activé, l'IdP peut provisionner automatiquement des comptes et affecter l'appartenance à un groupe, ce qui définit le rôle de la plateforme de l'utilisateur.  
- **Utilisateurs invités par Hôte :** Les Hôtes peuvent inviter d'autres utilisateurs en tant que collaborateurs Éditeur à des Workspaces spécifiques. L'affectation du rôle de collaborateur Éditeur consomme une licence Hôte.

**Bonne pratique recommandée (clients Enterprise) :**  
Pour les organisations s'attendant à un grand nombre d'utilisateurs qui ont besoin d'accès à Avatour, il est recommandé d'**intégrer l'authentification unique (SSO)** et de gérer les utilisateurs et l'appartenance à un groupe à partir de l'**IdP**. Cette approche rationalise le provisionnement des comptes, l'affectation des groupes et la gestion des licences, réduisant la charge administrative et garantissant un contrôle d'accès cohérent.

#### 2.2.1 Utilisateurs invités

- Ajoutés au **groupe Invité**.  
- Peuvent **afficher les Assets** dans les Workspaces où ils ont été ajoutés en tant que **collaborateurs Observateur**.  
- Ne peuvent pas créer de workspaces, animer de réunions ou télécharger du contenu.  
- Les comptes Invités provisionés par SSO **s'authentifient via l'IdP** ; aucun mot de passe géré par Avatour n'est requis.

---

#### 2.2.2 Utilisateurs licenciés (accès à la console Web)

##### Utilisateurs Hôte (Groupe : Hôte)

- Peuvent créer/gérer des Workspaces, inviter des collaborateurs à un workspace, **animer des réunions en direct**, télécharger des **Captures rapides**.  
- Ont accès au **Tableau de bord Hôte** et à l'**Application Opérateur** sur les caméras 360° compatibles.  

##### Utilisateurs Admin (Groupe : Admin)

- Incluent toutes les capacités Hôte plus l'administration complète du compte.

**Les privilèges Admin supplémentaires incluent :**

**Gestion des comptes**  

- Créer de nouveaux utilisateurs et les affecter à des groupes.
- Réinitialiser les mots de passe lorsqu'ils sont gérés par Avatour (ne s'applique pas lorsque SSO est activé). 
- Passer les utilisateurs Invité à Hôte.  
- Désactiver des utilisateurs (les comptes Admin doivent d'abord être convertis en Hôte avant la suppression).  
- Transférer des assets d'un utilisateur Hôte à un autre lors de la suppression.

**Paramètres**  

- Configurer les **paramètres de sécurité à l'échelle de l'organisation** pour les assets, les workspaces et les réunions hébergés sur la plateforme (par exemple, si un Hôte doit être présent pour démarrer une réunion, si les visages doivent être floutés dans toutes les vidéos téléchargées sur la plateforme).  
- Activer ou désactiver les **fonctionnalités IA** ou **l'enregistrement**.  
- Appliquer la marque de l'entreprise de façon cohérente sur la plateforme si un **domaine personnalisé** est configuré.
  

**Assets et Analyses** 
 
- Afficher tous les Assets téléchargés par n'importe quel utilisateur de l'organisation.  
- Examiner l'utilisation de la plateforme dans l'ensemble de l'organisation.

---

#### 2.2.3 Permissions des collaborateurs Workspace

Les permissions Workspace définissent ce qu'un utilisateur peut faire **au sein d'un Workspace spécifique**. Elles sont distinctes de l'appartenance à un groupe au niveau de la plateforme (Invité, Hôte, Admin).

- **Collaborateur Éditeur :** Les utilisateurs disposant de cette permission peuvent :
  - Gérer les Assets (télécharger, supprimer, flouter les visages, générer des résumés)  
  - Gérer les paramètres de réunion (activer/désactiver l'enregistrement, autoriser ou supprimer des participants)  
  - Planifier et animer des réunions en direct  
  - Générer des rapports basés sur des modèles prédéfinis  
  - Ajouter ou supprimer des collaborateurs du Workspace  

- **Collaborateur Observateur :** Les utilisateurs disposant de cette permission ont un accès en lecture seule aux Assets du Workspace. Ils **ne peuvent pas modifier les Assets, gérer les réunions ou gérer les collaborateurs**, mais ils **peuvent créer des Notes sur les Assets**.## 3. Pour les participants aux réunions à distance et les visiteurs de l'espace de travail {#for-remote-meeting-participants-and-workspace-visitors}
Avatour permet aux utilisateurs de collaborer de deux manières principales :

- **Rejoindre une réunion Avatour (Collaboration synchrone) :**  
  Vous pouvez recevoir une **invitation calendrier** pour rejoindre une réunion Avatour. Pendant la réunion, les participants peuvent effectuer une **visite de site distante en direct** ou examiner les ressources de manière synchrone ensemble.

- **Visiter un Workspace (Collaboration asynchrone) :**  
  Vous pouvez également être invité en tant que **collaborateur à un Workspace** pour examiner les ressources **de manière asynchrone** (selon votre propre horaire).### 3.1 Comment rejoindre une réunion Avatour et visiter un espace de travail Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 N'importe quel appareil « Écran plat » avec navigateur Web {#any-flat-screen}
Vous pouvez rejoindre une réunion Avatour à partir de **n'importe quel ordinateur de bureau ou portable, smartphone ou tablette** en utilisant un navigateur Web.  

##### Rejoindre une réunion Avatour

> **Remarque :** Rejoindre une réunion Avatour nécessite que vous **accordiez les autorisations de microphone**. Veuillez accepter les invites d'autorisation de votre navigateur.

1. **Via invitation calendrier (recommandé) :**  
   - Vous recevrez généralement une **invitation calendrier** avec un **lien de connexion direct** (par exemple : `https://avatour.live/join?s=xxxxx`).  
   - En cliquant sur le lien, le **code de réunion à 5 caractères** sera automatiquement renseigné et vous serez dirigé vers la réunion.
   - **Authentification requise :** Certaines réunions sont réservées aux utilisateurs enregistrés. Dans ce cas, l'invitation indiquera que vous devez **vous connecter pour accéder à la réunion**.  
   - **Réunions protégées par mot de passe :** Certaines réunions peuvent nécessiter un mot de passe. Dans ce cas, l'invitation comprendra le mot de passe que vous devez entrer pour rejoindre la réunion.

2. **Via code de réunion :**  
   - Si l'hôte partage un **code de réunion à 5 caractères** séparément, allez à [https://avatour.live/join](https://avatour.live/join), entrez votre **nom** et le **code de réunion**, et rejoignez la réunion.  
   - Si la réunion est **protégée par mot de passe**, entrez le mot de passe fourni par l'hôte.  
   - Si la réunion nécessite une **authentification**, vous devrez **vous connecter avec votre compte Avatour** avant de rejoindre la réunion.

> **Conseil 1 :** Si votre caméra ou votre microphone ne fonctionne pas, il se peut qu'il soit utilisé par une autre application (par exemple Microsoft Teams ou Zoom). Fermez les applications qui pourraient utiliser votre caméra ou votre microphone, puis quittez et rejoignez la réunion Avatour.  

> **Conseil 2 :** Si vous ne pouvez toujours pas rejoindre la réunion, exécutez ce test : [https://avatour.live/test](https://avatour.live/test).  
> Le test peut identifier si votre **pare-feu d'entreprise ou réseau** bloque l'accès, et fournira des informations pour guider les discussions avec votre équipe informatique.  

> **Conseil 3 :** N'utilisez **pas** les applications Avatour iOS ou Android pour rejoindre les réunions. Ces applications ne sont nécessaires que lorsque vous **diffusez une réunion en direct depuis une caméra Insta360**, car ces caméras ne peuvent pas exécuter le logiciel Avatour 360° directement et nécessitent un smartphone pour vous aider.

##### Visiter un espace de travail Avatour (sans rejoindre une réunion Avatour)

Vous pouvez accéder à un espace de travail des manières suivantes :

- **Espace de travail public :**  
  Si l'espace de travail est public, le lien peut être consulté directement — aucune connexion requise.

- **Espace de travail restreint :**  
  Si l'espace de travail est restreint, vous devez être ajouté en tant que **collaborateur** avec des autorisations **Éditeur** ou **Lecteur**.

  1. Lorsque vous êtes ajouté en tant que collaborateur, vous recevrez une **notification par e-mail** avec un lien vers l'espace de travail.
  2. Cliquez sur le lien dans l'e-mail pour ouvrir l'espace de travail. Si vous n'êtes pas déjà connecté, vous serez invité à **vous connecter ou à terminer votre inscription**.
  3. Une fois connecté, l'espace de travail s'ouvrira automatiquement.

  Alternativement, vous pouvez vous connecter à [https://avatour.live/login](https://avatour.live/login) et accéder à l'espace de travail à partir de votre **liste d'espaces de travail**.

#### 3.1.2 Casque de réalité virtuelle {#vr-headset}
Vous pouvez rejoindre une réunion et visiter un espace de travail à partir d'une gamme de casques Meta et Pico compatibles. Pour ce faire : 

1. Installez notre application Avatour à partir de votre boutique d'applications VR respective : [Comment installer l'application Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Lancez notre application et entrez le code de réunion ou sélectionnez un espace de travail pour rejoindre une réunion. Pour plus d'informations sur la façon d'utiliser notre application VR, consultez notre article de la base de connaissances [ici](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Outils de réunion et de collaboration d'espace de travail {#meeting-tools}

Avatour permet la collaboration dans deux contextes principaux :

1. **Réunions (synchrone) :** Collaborez en temps réel avec d'autres participants, y compris des visites de site en direct ou l'examen d'actifs enregistrés ensemble.  
2. **Espaces de travail (asynchrone) :** Examinez et interagissez avec les actifs selon votre propre horaire, 24/7.

Les **outils de collaboration sont très similaires** entre les réunions et les espaces de travail, avec quelques différences dues au contexte synchrone par rapport au contexte asynchrone.

#### 3.2.1 Disposition de l'interface

L'interface Avatour est organisée autour de trois zones principales :

- **Panneau gauche** – Actifs de l'espace de travail et outils d'assistance  
- **Canevas central** – Zone de visualisation principale pour la vidéo en direct ou les actifs  
- **Panneau droit** – Informations contextuelles, telles que les participants, les réunions ou le chat  

La plupart des interactions sont lancées à partir du **menu inférieur**.  
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

Le menu inférieur permet d'accéder aux contrôles d'interface principaux et aux panneaux :

**Menu inférieur de réunion**  

![Menu inférieur de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu inférieur de réunion Avatour*

- **Actifs** – Examinez les fichiers de l'espace de travail, y compris les vidéos enregistrées, les images, les instantanés et les PDF. 
- **Chat** – Envoyez des messages à tous les participants à la réunion.  
- **Caméra** – Activez ou désactivez votre webcam.  
- **Microphone** – Sourdine ou désactivez la sourdine.  
- **Présenter** – Présentez un actif, un bureau ou un flux de webcam (voir la section Présenter ci-dessous).  
- **Outils d'hôte** (hôtes uniquement) :  
  - **Verrouiller la vue** – Verrouillez la vue pour tous les participants.  
  - **Rendre muet tout le monde** – Rendez muets tous les participants.  
- **Activer le plein écran** – Mettez l'onglet de réunion en plein écran.  
- **Quitter la réunion** – Quittez la réunion.  
- **Démarrer l'enregistrement** – Utilisez ce bouton pour démarrer et arrêter l'enregistrement manuellement pendant une réunion. Vous pouvez également enregistrer les réunions automatiquement si l'**enregistrement automatique** est activé dans les paramètres de l'espace de travail. Dans les deux cas, les enregistrements sont sauvegardés dans les actifs de l'espace de travail.
- **Carte** – Ouvrez ou fermez le panneau de la carte pour les actifs ayant une piste GPS. Cliquer sur un emplacement accède au point exact de la vidéo. La carte se met à jour en direct lors de la lecture de la vidéo.
- **Participants** – Ouvrez ou fermez le panneau des participants.  
- **Informations de réunion** – Affichez le code de réunion, le lien d'invitation et accédez aux tutoriels connexes.  

![Informations de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panneau latéral d'informations de réunion Avatour*

- **Paramètres** – Ajustez la langue, l'audio et les paramètres vidéo. Pour les réunions vidéo 360° en direct, utilisez **Afficher le débit** pour surveiller les statistiques de connectivité.

> Conseil : Envoyez le lien de réunion ou ajoutez-le à un élément de calendrier pour inviter les participants.

---

##### Menu Présenter

L'option **Présenter** dans le menu inférieur de réunion vous permet de partager du contenu avec tous les participants.

- **Caméra** – Partagez votre caméra de smartphone/tablette. Cela peut également être utilisé lors d'une réunion vidéo 360° en direct pour superposer une vue secondaire pour les gros plans ou des détails spécifiques. 
- **Bureau** – Partagez votre écran de bureau avec tous les participants.  
- **Actif** – Présentez un actif de l'espace de travail. La sélection d'un actif ouvre la **barre d'outils d'actif**, qui fournit des contrôles de lecture et des outils de collaboration spécifiques à l'actif présenté.

##### Barre d'outils d'actif (Réunion)

Lors de la présentation d'un actif dans une réunion, la **barre d'outils d'actif** apparaît au-dessus du canevas. Voici les outils et les éléments de menu disponibles lors de la <u>présentation d'un actif dans une réunion</u> - expliqués de gauche à droite.

![Menu Avatour lors de la présentation d'un actif dans une réunion](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour lors de la présentation d'un actif dans une réunion*


- **Chronologie vidéo / barre de progression** – Affiche la progression vidéo avec des notes et des sujets clés extraits de l'audio. Cliquez sur une note ou un sujet pour accéder à ce moment et ouvrir la note. Inclut les contrôles **Lecture / Pause**.   
- **Instantané** – Capturez une image 360° ou 2D à partir de l'actif.  
- **Projecteur** – Mettez en évidence une zone spécifique pour tous les participants lors des sessions en direct.  
- **Afficher/Masquer le point de vue (POV)** – Affichez où chaque participant regarde dans la vidéo 360°.  
- **Notes** – Créez des notes ancrées à des moments spécifiques de l'actif. Les notes peuvent être catégorisées (Observation, Problème, Action, Recommandation), suivies par statut (Ouvert → En cours → Résolu) et partagées via des liens directs.  

  ![Note Avatour et filtres de notes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Note Avatour et filtres de notes*

  - **Notes de commande vocale** – Ce sont des espaces réservés générés automatiquement lorsque l'enregistrement détecte des mentions comme « insérer une note », « prendre une note » ou « créer une note ». Ces notes apparaissent sur la chronologie et doivent être **positionnées et finalisées** par l'utilisateur. 

  ![Notes Avatour - Générées par commande vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notes Avatour - Générées par commande vocale*

- **Notes et panneau de synthèse** – Ouvre un panneau latéral qui affiche toutes les notes, les sujets clés et un résumé exécutif de l'actif. Cliquer sur un élément vous amène à ce moment de la vidéo.  

  ![Résumé exécutif d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Résumé exécutif Avatour lors de la présentation d'un actif dans une réunion*

  ![Sujets Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Sujets Avatour lors de la présentation d'un actif dans une réunion*

  À partir du **panneau latéral**, vous pouvez **imprimer un rapport d'actif** ou le **télécharger en TXT ou CSV**. Les rapports peuvent inclure des notes, des sujets générés par l'IA et des transcriptions complètes. Vous pouvez également **choisir les éléments à inclure** avant d'exporter.  

  ![Menus d'impression de rapport d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menus d'impression/téléchargement de rapport d'actif Avatour*  

  ![Menu de sélection d'éléments de rapport d'actif Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menu de sélection d'éléments de rapport d'actif Avatour*

- **Lien de partage** – Partagez un lien vers une note ou une scène spécifique dans l'actif.  
- **Sous-titres codés (CC)** – Affichez la transcription textuelle à l'écran lors de la lecture vidéo.

##### Barre d'outils d'actif (Espace de travail)

Lors de l'examen d'un actif dans un espace de travail, la barre d'outils est similaire mais optimisée pour un usage individuel :

![Menu Avatour lors de la présentation d'un actif en dehors d'une réunion, par exemple lors de la visite d'un espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour lors de la présentation d'un actif dans un espace de travail*

- **Chronologie vidéo / barre de progression** – Affiche la progression vidéo avec des notes et des sujets clés extraits de la piste audio. Cliquez n'importe où sur la chronologie pour parcourir la vidéo. Cliquez sur une note ou un sujet pour accéder à ce moment et ouvrir la note. Inclut les contrôles **Lecture / Pause**.  
- **Instantané, Notes, Notes et panneau de synthèse, Lien de partage, Sous-titres codés**  
- Non disponible : **Projecteur, POV** (nécessitent des participants en direct)  
- Contrôles supplémentaires :
  - **Sauts de 10 secondes** – Avancez/reculez  
  - **Vitesse de lecture** – Ajustez la vitesse (0,5× à 2×)  
  - **Couper la vidéo** – Coupez le début ou la fin de l'actif## 4. Pour les utilisateurs hôtes et administrateurs - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}
Lorsque vous vous connectez à votre compte utilisateur Avatour, vous accédez à la **Console Web**.### 4.1 Console Web - Aperçu du menu principal {#web-console-overview-main-menu}

Sur le côté gauche, vous verrez les éléments de menu suivants :

![Avatour Web Console - Menu principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Avatour Web Console - Menu principal*

- **Espaces de travail** – Organisez votre contenu efficacement. Chaque espace de travail contient **Ressources**, **Collaborateurs**, **Réunions** et **Paramètres**.  
- **Ressources** – Accédez et gérez toutes vos ressources (vidéos, images, PDF). Les administrateurs peuvent afficher toutes les ressources du compte, et les ressources partagées sont visibles par tous les utilisateurs.  
- **Profil** – Gérez votre langue et votre mot de passe.  
- **Analyse** – Suivez l'activité des sessions, l'utilisation de l'espace de travail et les métriques de retour sur investissement.  
- **Paramètres** *(Administrateur uniquement)* – Configurez les paramètres par défaut de l'espace de travail, des réunions et des ressources dans toute l'organisation. Les administrateurs peuvent également personnaliser la marque (logo, couleurs, arrière-plans).  
- **Compte** *(Administrateur uniquement)* – Gérez les utilisateurs enregistrés et les caméras 360°.  
- **Connexion d'appareil** – Entrez le code affiché sur votre caméra 360° pour l'associer à votre compte.  
- **Tutoriels** – Accédez aux tutoriels guidés.  
- **Déconnexion** – Déconnectez-vous de la console.

> Les sections comme Profil, Connexion d'appareil, Tutoriels et Déconnexion sont explicites et n'ont pas de sous-sections détaillées.

---### 4.2 Console Web - Détails par élément de menu (avec images) {#web-console-details-by-menu-item}

#### 4.2.1 Espaces de travail

Les espaces de travail sont des unités organisationnelles flexibles qui vous permettent de gérer les ressources, les collaborateurs et les réunions au même endroit. Vous pouvez créer un nouvel espace de travail avec le bouton **Nouvel espace de travail** dans le coin supérieur droit.

![Avatour Web Console - Élément de menu principal Espaces de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Avatour Web Console - Élément de menu principal Espaces de travail*

Cliquez sur l'icône de cloche pour voir un résumé de l'activité de l'espace de travail au cours des 7 derniers jours.

![Avatour Web Console - Activités récentes de l'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Activités récentes de l'espace de travail*

À l'intérieur d'un espace de travail :

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espace de travail avec Ressources (gauche), Canevas (centre), Réunions (droite)*

- **Ressources** – Gérez les fichiers alloués à cet espace de travail.  
- **Collaborateurs** – 
  Contrôlez l'accès aux espaces de travail par 
  - **Lecteur** – Peut afficher les ressources. L'invitation crée un utilisateur Invité si nécessaire.  
  - **Éditeur** – Contrôle complet de l'espace de travail, mêmes droits que l'hôte. L'invitation met à niveau l'utilisateur en hôte si nécessaire.  
> Plusieurs utilisateurs peuvent accéder à un espace de travail simultanément sans réunion. Les espaces de travail publics et les paramètres d'accès aux réunions offrent un accès alternatif.  
- **Rapport** – Générez un rapport à l'aide d'un modèle de liste de contrôle sur les ressources de l'espace de travail sélectionné.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Rapport de l'espace de travail et sélection des ressources*

- **Carte** – Affichez les emplacements des ressources compatibles GPS sur une carte.  
- **Réunions** – Organisez les réunions dans l'espace de travail.  
- **Paramètres** – Configurez les valeurs par défaut de l'espace de travail et de la réunion :

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Paramètres de l'espace de travail*

**Paramètres de l'espace de travail**

- **Modèle de rapport** – Sélectionnez le modèle de liste de contrôle pour le rapport IA.  
- **Activer les notifications** – E-mails de synthèse quotidienne pour les changements d'état des notes.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Exemple de notifications par e-mail*

- **Espace de travail public** – Toute personne disposant du lien peut afficher directement les ressources.

**Paramètres de la réunion**
  
* **Authentification requise** – Les participants doivent se connecter.  
* **Autoriser l'accès des invités** – Permettre aux utilisateurs non enregistrés d'afficher les ressources.  
* **Enregistrement automatique / Démarrage manuel** – Choisissez si les réunions s'enregistrent automatiquement ou sont démarrées manuellement.  
* **Exiger l'hôte** – L'hôte doit admettre les participants ; la réunion se termine quand l'hôte part.  
* **Autoriser l'accès des spectateurs** – Rejoindre sans micro ni caméra ; communiquer via le chat.  
* **Réunions protégées par mot de passe** – Exiger un mot de passe pour participer.  
* **Afficher la question d'économies de déplacements** – Demander aux participants si la réunion a réduit les déplacements.  

> Les paramètres peuvent être combinés (par exemple, pas d'hôte requis mais protégé par mot de passe).

---

#### 4.2.2 Ressources

Gérez toutes les vidéos 360°/2D, images et PDF. Téléchargez/téléchargez les ressources, allouez-les aux espaces de travail, partagez-les avec d'autres utilisateurs, renommez-les, imprimez/téléchargez les rapports, activez le floutage des visages et le résumé IA.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Élément du menu principal Ressources*

---

#### 4.2.3 Analyse

Fournit des informations sur les réunions, l'utilisation de l'espace de travail et les métriques de ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Aperçu de l'analyse*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Activité de la réunion et utilisation de l'espace de travail*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Utilisation des licences de périphérique et ROI*## 5. Sur place - Comment utiliser le kit clé en main Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Premiers pas
[Guide de démarrage rapide – Kit clé en main Avatour 3.1 (Configuration Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Suivez le guide pour déballer, assembler et allumer votre caméra.

---### 5.2 Conseils utiles

#### Batterie externe – Réunions plus longues et thermalique améliorée

- **Si votre kit inclut une batterie Ulanzi :** Attachez-la entre la base du trépied et le bâton extensible, puis connectez la batterie à la caméra via USB-C.

- **Si votre kit inclut un bâton de batterie Telesin :** Montez la caméra directement sur le bâton de batterie extensible Telesin et connectez-le via USB-C.

Utilisation de la batterie externe :

1. Prolonge la durée de vie totale de la batterie d'environ 40 minutes (batterie de caméra uniquement) à environ 3 heures.
2. Ajoute de la stabilité au configuration de la caméra.
3. Aide à prévenir une surchauffe potentielle.

> Nous recommandons d'utiliser toujours la batterie externe dès le départ, en particulier pour les réunions en direct.

#### Considérations audio pour les réunions en direct et les enregistrements

- **Environnements bruyants :**
  Utilisez les écouteurs Shokz inclus dans votre kit pour une capture audio claire.
  - **Marche/Arrêt :** Maintenez le bouton « + » enfoncé pendant 3 secondes (LED bleue = activée, LED rouge = désactivée).
  - **Mode d'appairage Bluetooth :** Alors que le casque est éteint, maintenez le bouton « + » enfoncé pendant 5 secondes (LED clignote bleu/rouge).
  - **Volume :** Utilisez les boutons « + » et « - ».

- **Environnements plus calmes / plusieurs participants près de la caméra :**
  Utilisez le haut-parleur clip-on NoxGear. Il n'a pas la même fidélité que les haut-parleurs de conférence (par exemple, Jabra Speak), mais il est facile à clipser sur votre chemise et capture efficacement les voix à proximité.
  - **Marche/Arrêt :** Maintenez le bouton Lecture/Pause enfoncé pendant 2 secondes.
  - **Mode d'appairage Bluetooth :** Entre automatiquement en mode d'appairage lorsqu'il est allumé (LED clignote bleu/rouge ; bleu uni une fois appairé).
  - **Volume :** Utilisez les boutons « + » et « - ».

- **Utilisation de votre propre appareil :** Si vous préférez une alternative (par exemple, un haut-parleur de conférence ou un casque personnel), vous pouvez l'appairer via la caméra : Paramètres → Bluetooth.

#### Connectivité, connectivité, connectivité
**Avant de commencer :** Assurez la connexion Internet via :

- **WiFi local** (recommandé)
- **Réseau mobile** (si hors de portée WiFi)

**Bande passante recommandée :** 10 Mbps en montée/descente pour la diffusion en direct 360° complète (environ 5 Mbps). Une bande passante inférieure (1–2 Mbps) ne fonctionne que si vous êtes immobile.

##### Test de la vitesse du réseau
- **Test à un seul endroit :** N'importe quel vérificateur de vitesse que vous utilisez normalement (par exemple, [Speedtest](https://www.speedtest.net)) pour vérifier la bande passante de montée et de descente.
- **Test de marche sur le site :** Depuis la caméra : Paramètres → Réseau → Test de connexion. Parcourez l'ensemble de l'espace pour confirmer la couverture et la bande passante.

##### WiFi local
- Fortement recommandé pour les connexions stables.
- Si l'informatique nécessite une liste blanche, trouvez l'adresse MAC : Paramètres → À propos → Adresse WiFi.

##### Réseau mobile
**Option A : Point d'accès fourni par le kit et carte SIM**

- Attachez le point d'accès GlocalMe au bâton de batterie Telesin (aimant).
- Assure aucune interférence et maintient la connexion en cas d'éloignement de la caméra.
- Dépannage :
  - Confirmez la carte SIM pré-installée (pas Cloud SIM).
  - Activez la 5G dans le gestionnaire de carte SIM.
  - Vérifiez l'APN correct pour votre région ([guide de configuration APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B : Point d'accès personnel / Carte SIM**
- Utilisez votre propre smartphone ou point d'accès dédié.

**Remarque importante :**
> Gardez le point d'accès éteint lors de la connexion à WiFi ; activez-le uniquement hors de portée. Le système d'exploitation de la caméra bascule dynamiquement entre les réseaux WiFi en fonction de la force du signal et peut basculer involontairement vers le point d'accès même si WiFi est disponible.

> Les réseaux mobiles peuvent limiter la bande passante de manière inattendue. Vérifiez auprès de votre opérateur les limites de votre plan de données, ou contactez le support Avatour si vous utilisez notre point d'accès et notre carte SIM.

##### Situations de faible bande passante
- Pré-enregistrez les vidéos de localisation pour une lecture ultérieure ([guide d'enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Partagez un flux de caméra smartphone pour compléter les zones de faible bande passante (0,1–0,3 Mbps de montée).

##### Pas de connectivité
- Seule la vidéo pré-enregistrée peut être utilisée ([guide d'enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Autres participants sur site – Meilleures pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même endroit que la caméra 360°, une gestion prudente de **l'audio et de la bande passante** est cruciale :

- Chaque smartphone, tablette ou ordinateur portable connecté sur site consomme de la bande passante réseau et peut affecter négativement le flux de caméra 360°.
- Plusieurs microphones et haut-parleurs dans le même espace peuvent causer des **retours d'audio**, rendant l'expérience de la réunion désagréable pour tous les participants.

#### Autres participants sur site – Meilleures pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même endroit que la caméra 360°, une gestion prudente de **l'audio et de la bande passante** est cruciale :

- Chaque smartphone, tablette ou ordinateur portable connecté sur site consomme de la bande passante réseau et peut affecter négativement le flux de caméra 360°.
- Plusieurs microphones et haut-parleurs dans le même espace peuvent causer des **retours d'audio**, rendant l'expérience de la réunion désagréable pour tous les participants.

Pour résoudre ces défis, suivez ces **meilleures pratiques** :

- **Utilisez des écouteurs filaires ou sans fil :** De préférence avec suppression du bruit pour éviter l'écho et les retours.
- **Mode sur site :** Rejoignez la réunion en mode Sur site lorsque vous êtes physiquement près de la caméra 360°.
  - Ce mode est optimisé pour une utilisation sur site :
    - Désactive le micro et le haut-parleur du participant par défaut.
    - N'envoie **pas** le flux caméra du participant.
    - N'affiche **pas** le flux de caméra 360° dans le navigateur du participant.
    - Économise la bande passante du réseau, assurant que la caméra 360° a une montée maximale disponible pour la diffusion en direct.
    - Utile lorsqu'un utilisateur souhaite partager des détails spécifiques ; vous **pouvez partager votre caméra en retour** pour des vues ciblées.
- **Désactivez le son lorsque vous ne parlez pas activement :** Prévient les retours audio indésirables et les distractions.
- **Utilisez un réseau séparé si possible :** Connectez votre smartphone à un réseau différent de celui de la caméra pour réduire les interférences.

Le respect de ces directives assure une visite en direct fluide et de haute qualité pour les participants sur site et à distance.### 5.3 Application Avatour Camera

Voici (1) le menu de niveau supérieur, (2) Paramètres et (3) menus Paramètres réseau.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Avatour 360° Camera App - 3 Menus*

**Capture rapide** - Pour l'enregistrement vidéo 360° hors ligne. - Pour une description détaillée, voir [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Nous recommandons d'utiliser un appareil audio externe (connecté via Bluetooth). N.B. Vous pouvez également faire des vidéos et des images 2D standard - changez simplement le mode entre 360° et 2D dans le coin inférieur droit une fois sur l'écran QC.

**Live Meeting** - Pour la vidéoconférence 360° en direct. Vous verrez vos espaces de travail et cliquer sur l'un d'eux lancera le flux vidéo en direct de la caméra 360°. Avant de pouvoir rejoindre la réunion avec votre caméra 360°, vous devez connecter un appareil audio via Bluetooth. Pour une description détaillée, voir [How to start a Live Capture meeting with your Pilot camera?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Lors de l'hébergement d'une réunion Live Capture avec votre caméra 360, vous aurez des outils de réunion similaires à votre disposition qui reflètent l'expérience Web. Voici un lien vers notre article de la base de connaissances qui explique ces outils plus en détail : [Operator App Tools](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galerie** - Trouvez ici toutes vos vidéos et images 360° pour upload vers la console Web Avatour.

**Paramètres** - Dans Paramètres, vous avez les options suivantes :

- **Réseau** : Cette option vous permet de modifier le réseau WiFi auquel la caméra est connectée ou d'exécuter un test de connexion réseau pour afficher votre débit de diffusion
- **Live Capture** : Ajustez vos paramètres Live Capture en fonction de la bande passante disponible, de la sensibilité VR des invités, ou si les lentilles de protection de votre caméra sont installées :
  - **Fréquence d'images cible** : Ajustez la fréquence d'images de votre vidéo Live Capture entre 15 fps, 24 fps et 30 fps. Les fréquences d'images plus élevées produisent une vidéo plus fluide, mais nécessiteront une plus grande bande passante de téléchargement. Par défaut : 15 fps
  - **Débit cible** : Vous permet d'augmenter ou de diminuer le débit de diffusion maximal pour votre Live Capture. Vous pouvez définir votre débit cible entre 1 Mbps et 10 Mbps. Des débits plus élevés entraîneront une meilleure résolution vidéo, mais nécessiteront une plus grande bande passante de téléchargement. Par défaut : 5 Mbps
  - **Optimiser le mouvement** : Cela diminuera la fréquence d'images vidéo, générant moins de charge sur la bande passante de téléchargement de votre réseau et augmentant votre débit de diffusion. De plus, cette option aide à réduire le mal des transports pour les participants en RV. Par défaut : Désactivé
  - **Lentilles de protection** : Cela affectera la manière dont la vidéo 360° est assemblée selon que des lentilles de protection ont été installées sur votre caméra. Si vous n'avez pas de lentilles de protection, définissez ceci sur « Non ». Si vous avez reçu un Kit 3.0, vous avez des lentilles de protection pré-installées et devriez définir ceci sur « Oui ». Par défaut : Oui

- **Quick Capture** : Ajustez vos paramètres Quick Capture en fonction de votre fréquence d'images vidéo préférée, de la bande passante disponible pour les téléchargements de vidéos enregistrées, ou si les lentilles de protection de votre caméra sont installées. Quick Capture a une résolution fixe de 4k qui offre généralement un bon équilibre entre la qualité vidéo et la taille du fichier. (Pour des résolutions plus élevées, vous pouvez utiliser les applications caméra natives, également sur le PanoX V2, pour plus de détails, voir [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)) :
  - **Fréquence d'images cible** : Ajustez la fréquence d'images pour vos enregistrements vidéo Quick Capture entre 15 fps, 24 fps et 30 fps. Les fréquences d'images plus élevées produisent une vidéo plus fluide, mais augmentent la taille du fichier vidéo et le temps de téléchargement. Recommandé : 30 fps
  - **Débit cible** : Définissez le débit cible pour les téléchargements Quick Capture entre 5 Mbps et 20 Mbps. Les débits plus faibles augmentent les vitesses de téléchargement, mais diminuent la qualité vidéo. Recommandé : 20 Mbps
  - **Lentilles de protection** : *Voir la section Lentilles de protection pour Live Capture ci-dessus*
- **À propos** : Afficher le numéro de série de l'appareil et la version du logiciel

**Compte** - Pour vous connecter avec votre compte hôte ou administrateur Avatour.## 6. Conseils de bonnes pratiques {#best-practice-advice}

### 6.1 Premiers usages (informels) et prise en main

Pour vos premiers usages et votre prise en main de la console Web Avatour et du kit Avatour Turnkey, nous recommandons les étapes suivantes :

1. Ramenez le kit chez vous et testez-le en famille et entre amis en utilisant votre connexion Internet domestique.
2. Apportez le kit au bureau et connectez-vous à un réseau d'entreprise (des problèmes d'entreprise pourraient survenir, par exemple des pare-feu d'entreprise - mais vous savez à partir de l'étape un qu'Avatour fonctionne et c'est un sujet à résoudre par votre équipe IT avec l'aide d'Avatour).
3. Commencez à utiliser Avatour sur site (en dehors de votre bureau) au lieu de réunion où les participants à distance devraient généralement se déplacer. D'autres problèmes de connectivité pourraient survenir. Avatour pour vous aider en coopération avec votre équipe IT.
4. Commencez à utiliser avec des participants à distance internes et externes.### 6.2 Avant une réunion en direct avec vidéo à 360°

- Nous recommandons de faire une visite vidéo à 360° enregistrée avant toute visite en direct si le temps le permet, pour trois raisons : (1) Avoir une solution de secours pour la visite en direct, (2) avoir quelque chose pour la documentation et l'examen ultérieur (en plus de la visite en direct enregistrée) et (3) commencer à créer une bibliothèque de vidéos à 360° de tous vos sites, ce qui peut être utile pour de nombreux cas d'usage.
- Tous les composants du kit doivent être chargés pendant au moins 90 minutes avant la réunion en direct. Nous recommandons quand même d'avoir tous les appareils en charge continue lorsqu'ils ne sont pas utilisés. De cette façon, tous les appareils seront toujours prêts, même pour les réunions ad hoc imprévues.
- Avoir le kit complètement assemblé (1. base de trépied + 2. batterie Ulanzi + 3. bâton extensible + 4. caméra 360°).

- Confirmez qu'un Workspace est créé pour accueillir une réunion en direct et incluez tous les Assets pertinents.

- Invitez tous les participants à la réunion via votre Workspace. Cela crée une invitation sur le calendrier de tous les participants et inclut le lien d'invitation à la réunion.

- Associez et connectez vos écouteurs Bluetooth ou votre haut-parleur que vous prévoyez d'utiliser pour votre visite à la caméra.

- Tous les utilisateurs de smartphone sur site doivent se connecter à partir d'un réseau différent de celui de la caméra. Cela réduira la charge sur la bande passante du réseau de la caméra.

- Si vous êtes seul en tant qu'opérateur de caméra, apportez un smartphone avec vous au cas où vous voudriez partager la caméra du smartphone et montrer des détails fins.

- Confirmez que la caméra 360 peut se connecter à votre WiFi local.

- Avant une réunion Avatour, planifiez l'itinéraire que vous emprunterez dans l'établissement. Faites une réunion Avatour de test avec la caméra et vérifiez que toutes les zones ont des débits supérieurs à 1 Mbps de bande passante. Cela peut être vu sur l'écran de la caméra elle-même, ou en tant que participant distant en allant à Paramètres et en activant Afficher le débit.

- Si vous remarquez que certaines zones ont peu ou pas de bande passante, il est préférable de prendre des images ou d'enregistrer. Celles-ci peuvent ensuite être présentées pendant la réunion pour que les participants distants les examinent. Vous pouvez suivre le guide ici qui explique notre Capture rapide pour enregistrer et télécharger des vidéos/images à 360° : [Comment enregistrer et télécharger des vidéos à 360° avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si vous avez des participants distants rejoignant la réunion qui n'ont pas utilisé Avatour auparavant, fournissez-leur un bref résumé de la plateforme, de ses fonctionnalités (vidéo en direct à 360°, assets, captures d'écran, annotations, spotlight) et des outils de réunion.

- Vous pouvez commencer dans une autre solution de vidéoconférence (par exemple Teams, Zoom, Google Meet), mais avant de passer à Avatour, fermez complètement l'autre application de vidéoconférence. Dans certains cas, ces autres applications prioriseront le microphone/les haut-parleurs/la webcam de votre appareil, les désactivant pour Avatour. De plus, N'EXÉCUTEZ PAS Avatour ET une autre vidéoconférence en même temps car cela réduira la bande passante disponible.

- Si vous prévoyez d'utiliser la caméra 360 dans un environnement à haute température, il est recommandé d'utiliser le module de refroidissement (Pilot Pano uniquement). Cela aidera à réduire le risque que la caméra surchauffe et s'éteigne automatiquement.### 6.3 Lors de l'utilisation de la caméra sur site pour une réunion vidéo en direct 360°

- Lors de l'utilisation de la caméra, assurez-vous de marcher lentement. Cela contribue à la qualité vidéo et réduit tout temps d'arrêt vidéo potentiel lorsque la connexion réseau de la caméra bascule entre les points d'accès WiFi.

- Tenez la caméra devant vous et au-dessus du niveau des yeux. Cela permet à tous les participants à distance de voir la majorité de votre environnement.

- Dans les cas où la caméra doit rester stable, utilisez le trépied et étendez la caméra à la bonne hauteur, de préférence au niveau des yeux.

- Connectez toujours la caméra à votre réseau WiFi local si possible. Pour les zones sans accès WiFi, utilisez le point d'accès fourni. Le point d'accès dispose d'une carte SIM qui se connectera à un réseau cellulaire fiable à proximité. Gardez toujours le point d'accès éteint lorsqu'il n'est pas utilisé à l'intérieur, sinon la caméra 360° pourrait se connecter au point d'accès, ce que nous ne voulons pas à l'intérieur. En extérieur, gardez le point d'accès près de la caméra 360°.

- Lorsque le débit binaire en direct commence à chuter en dessous de 2 Mbps, ralentissez ou arrêtez-vous complètement jusqu'à ce que le signal se stabilise à nouveau. Cela se produit généralement lorsque vous passez d'un point d'accès WiFi à un autre.

- Si vous savez que la connectivité et la vidéo seront interrompues lors du déplacement vers un endroit spécifique (exemple : passage d'une zone de production intérieure à une zone extérieure), informez les participants à distance à l'avance.

- Si vous avez besoin de montrer quelque chose avec beaucoup de détails ou une petite écriture, utilisez votre propre smartphone ou celui d'un participant sur site pour rejoindre la réunion et présentez la caméra (orientée vers l'arrière) de votre téléphone / de leur téléphone.

- Si possible, nous recommandons qu'une personne supplémentaire soit sur site pour aider avec le partage de caméra smartphone décrit ci-dessus, car cela s'avère souvent utile / nécessaire.

- Idéalement, les utilisateurs de smartphones sur site doivent rejoindre la réunion (1) en mode sur site et (2) sur un réseau différent de celui utilisé par la caméra pour ne pas réduire la bande passante de téléchargement crucial de la caméra 360°.

- Tous les participants sur site qui rejoignent depuis leur smartphone doivent être en sourdine, sauf s'ils parlent activement.