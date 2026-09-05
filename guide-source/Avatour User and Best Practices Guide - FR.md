# Avatour User and Best Practices Guide

## 1. À l'attention de tous les utilisateurs d'Avatour {#for-all-avatour-users}

Si vous découvrez Avatour, les ressources suivantes vous offrent une introduction utile à la plateforme et à ses fonctionnalités :

1. [Vidéo « Comment fonctionne Avatour »](https://avatour.com/how-it-works)  
Un bref aperçu des principales fonctionnalités d'Avatour et de la manière dont la plateforme permet une collaboration à distance immersive.
2. [FAQ](https://avatour.com/faqs)  
Réponses aux questions fréquemment posées.
3. [Glossaire](https://avatour.com/glossary)  
Définitions des termes et concepts clés d'Avatour fréquemment utilisés.
4. Site web  
Consultez en particulier la page [Fonctionnalités d'Avatour](https://avatour.com/features) ainsi que les sections dédiées aux cas d'utilisation et aux secteurs d'activité pour découvrir comment Avatour peut répondre à vos besoins spécifiques.

## 2. Types d'utilisateurs d'Avatour  {#avatour-user-types}

### 2.1 Participants à la réunion (aucun compte requis)
Les utilisateurs peuvent rejoindre la réunion sans créer de compte Avatour. Exception : si l’organisateur a coché le paramètre de réunion « Authentification requise » (voir également 4.2.1 Paramètres des espaces de travail et des réunions) — par exemple, pour autoriser uniquement les collaborateurs internes à se connecter via l’authentification unique (SSO) —, l’invitation du calendrier indiquera que les participants doivent se connecter pour s’authentifier.

Les utilisateurs accèdent à la réunion comme suit :

- Recevoir un lien vers la réunion de la part de l’organisateur.
- Saisir un mot de passe de réunion si l’organisateur en a défini un.
- Les participants peuvent rejoindre la réunion sans compte Avatour, sauf si celle-ci est restreinte et nécessite une connexion pour s’authentifier.

#### 2.1.1 Participant 

- Peut rejoindre la réunion et interagir pleinement (webcam, microphone, chat et fonctionnalité « Présenter »).
- 20 participants interactifs maximum par réunion.

#### 2.1.2 Spectateur

- Peut suivre la réunion et participer uniquement via le chat.
- Ne peut pas partager de vidéo, utiliser un microphone, faire une présentation, lire/mettre en pause des ressources ni capturer d’instantanés.
- Maximum de 10 spectateurs par réunion.
- En comptant les participants, une réunion peut accueillir jusqu’à 30 personnes.

### 2.2 Utilisateurs enregistrés

Les utilisateurs enregistrés disposent d’un compte Avatour. Les comptes sont créés de l’une des manières suivantes :

- **Invitation par un administrateur :** lors de la mise en route, Avatour configure un **tenant dédié** pour l’organisation et crée un ou plusieurs **comptes d’administrateur**. Les administrateurs peuvent ensuite **inviter des utilisateurs** au sein de l’organisation et les affecter à des **groupes**, qui définissent leur rôle sur la plateforme (Invité, Hôte ou Administrateur). Les utilisateurs invités reçoivent un **lien d’inscription** pour finaliser la configuration de leur compte et définir un mot de passe.  
- **Invitation par un hôte :** Les hôtes peuvent ajouter des utilisateurs en tant que **collaborateurs éditeurs** à un espace de travail. Cela utilise une **licence d’hôte** et garantit à l’utilisateur un accès de niveau hôte.  
- **Provisionnement automatique via SSO (niveaux Entreprise/Business uniquement) :** Les comptes peuvent être créés automatiquement par le fournisseur d’identité (IdP). Par défaut, les comptes provisionnés via l’authentification unique (SSO) sont ajoutés au **groupe Invité**, sauf si cela est contourné via les **mappages de groupes SAML**. Les administrateurs peuvent toujours inviter des utilisateurs et leur attribuer une appartenance à un groupe directement, même lorsque l’authentification unique (SSO) est activée.

**Résumé :**  

Les utilisateurs enregistrés et leur appartenance à des groupes peuvent être gérés de plusieurs façons :

- **Gestion par l’administrateur :** un administrateur de la console Avatour peut créer des utilisateurs et les affecter à des groupes, ce qui définit leur rôle sur la plateforme (Invité, Hôte ou Administrateur).  
- **Provisionnement SSO :** pour les clients des niveaux Entreprise ou Business ayant activé le SSO, le fournisseur d’identité (IdP) peut automatiquement provisionner des comptes et attribuer des appartenances à des groupes, ce qui définit le rôle de l’utilisateur sur la plateforme.  
- **Utilisateurs invités par un hôte :** les hôtes peuvent inviter d’autres utilisateurs en tant que collaborateurs « Éditeur » dans des espaces de travail spécifiques. L’attribution du rôle de collaborateur « Éditeur » consomme une licence d’hôte.

**Meilleure pratique recommandée (clients Enterprise) :**  
Pour les organisations anticipant un grand nombre d’utilisateurs devant accéder à Avatour, il est recommandé d’**intégrer l’authentification unique (SSO)** et de gérer les utilisateurs et les appartenances à des groupes depuis l’**IdP**. Cette approche rationalise la création de comptes, l’affectation aux groupes et la gestion des licences, ce qui réduit la charge administrative et garantit un contrôle d’accès cohérent.

#### 2.2.1 Utilisateurs invités

- Ajoutés au **groupe Invité**.  
- Peuvent **consulter les ressources** au sein des espaces de travail où ils ont été ajoutés en tant que **collaborateurs « Viewer »**.  
- Ne peuvent pas créer d’espaces de travail, animer de réunions ni mettre en ligne de contenu.  
- Les comptes invités provisionnés via le SSO **s’authentifient via l’IdP** ; aucun mot de passe géré par Avatour n’est requis.

---

#### 2.2.2 Utilisateurs sous licence (accès à la console Web)

##### Utilisateurs hôtes (groupe : Hôte)

- Peuvent créer/gérer des espaces de travail, inviter des collaborateurs dans un espace de travail, **animer des réunions en direct** et mettre en ligne des **captures rapides**.  
- Ont accès au **tableau de bord de l’animateur** et à l’**application opérateur** sur les caméras à 360° prises en charge.  

##### Utilisateurs administrateurs (groupe : Admin)

- Dispose de toutes les fonctionnalités de l’hôte, ainsi que de l’administration complète des comptes.

**Les privilèges supplémentaires de l’administrateur incluent :**

**Gestion des comptes**  

- Créer de nouveaux utilisateurs et les affecter à des groupes.
- Réinitialiser les mots de passe lorsqu’ils sont gérés par Avatour (non applicable lorsque l’authentification unique (SSO) est activée). 
- Promouvoir des utilisateurs « Invités » au statut d’« Hôte ».  
- Désactiver des utilisateurs (les comptes « Admin » doivent d’abord être convertis en comptes « Hôte » avant leur suppression).  
- Transférer des ressources d’un utilisateur « Hôte » à un autre lors de la suppression.

**Paramètres**  

- Configurer les **paramètres de sécurité à l'échelle de l'organisation** pour les ressources, les espaces de travail et les réunions hébergés sur la plateforme (par exemple, si un « hôte » doit être présent pour démarrer une réunion, si les visages doivent être floutés sur toutes les vidéos mises en ligne sur la plateforme).  
- Activer ou désactiver les **fonctionnalités d’IA** ou l’**enregistrement**.  
- Appliquer l’identité visuelle de l’entreprise de manière cohérente sur l’ensemble de la plateforme si un **domaine personnalisé** est configuré.
  

**Ressources et analyses** 
 
- Afficher toutes les ressources mises en ligne par n’importe quel utilisateur de l’organisation.  
- Analyser l'utilisation de la plateforme au sein de l'organisation.

---

#### 2.2.3 Autorisations des collaborateurs d'un espace de travail

Les autorisations d'un espace de travail définissent ce qu'un utilisateur peut faire **au sein d'un espace de travail spécifique**. Elles sont distinctes de l'appartenance à un groupe au niveau de la plateforme (Invité, Hôte, Administrateur).

- **Collaborateur « Éditeur » :** les utilisateurs disposant de cette autorisation peuvent :
    - Gérer les ressources (téléverser, supprimer, flouter des visages, générer des résumés)  
    - Gérer les paramètres des réunions (activer/désactiver l’enregistrement, autoriser ou supprimer des participants) 
 - Planifier et animer des réunions en direct 
 - Générer des rapports à partir de modèles prédéfinis 
 - Ajouter ou supprimer des collaborateurs de l’espace de travail  

- **Collaborateur « spectateur » :** les utilisateurs disposant de cette autorisation ont un accès en lecture seule aux ressources de l’espace de travail. Ils **ne peuvent pas modifier les ressources, gérer les réunions ni gérer les collaborateurs**, mais ils **peuvent créer des notes sur les ressources**. 
  
## 3. Pour les participants aux réunions à distance et les visiteurs de l'espace de travail {#for-remote-meeting-participants-and-workspace-visitors}

Avatour permet aux utilisateurs de collaborer de deux manières principales :

- **Rejoindre une réunion Avatour (collaboration synchrone) :**  
  Vous pouvez recevoir une **invitation via l’agenda** pour rejoindre une réunion Avatour. Pendant la réunion, les participants peuvent effectuer une **visite à distance en direct** ou examiner des ressources ensemble de manière synchrone.

- **Visiter un espace de travail (collaboration asynchrone) :**  
  Vous pouvez également être invité en tant que **collaborateur d’un espace de travail** pour examiner des ressources **de manière asynchrone** (à votre convenance).

### 3.1 Comment rejoindre une réunion Avatour et visiter un espace de travail Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Tout appareil à « écran plat » équipé d’un navigateur Web {#any-flat-screen}
Vous pouvez rejoindre une réunion Avatour depuis **n’importe quel ordinateur de bureau ou portable, smartphone ou tablette** à l’aide d’un navigateur Web.  

##### Rejoindre une réunion Avatour

> **Remarque :** pour rejoindre une réunion Avatour, vous devez **accorder l’autorisation d’utiliser le microphone**. Veuillez accepter toutes les demandes d’autorisation de votre navigateur.

1. **Via une invitation de calendrier (recommandé) :** 
 - Vous recevrez généralement une **invitation de calendrier** contenant un **lien d’accès direct** (par exemple : `https://avatour.live/join?s=xxxxx`).  
    - En cliquant sur ce lien, le **code de réunion à 5 caractères** s’affichera automatiquement et vous serez redirigé vers la réunion.
    - **Authentification requise :** certaines réunions sont réservées aux utilisateurs enregistrés. Dans ce cas, l’invitation indiquera que vous devez **vous connecter pour accéder à la réunion**. 
 - **Réunions protégées par mot de passe :** certaines réunions peuvent nécessiter un mot de passe. Dans ce cas, l’invitation inclura le mot de passe que vous devrez saisir pour participer.

2. **Via le code de réunion :**  
    - Si l’organisateur vous communique séparément un **code de réunion à 5 caractères**, rendez-vous sur [https://avatour.live/join](https://avatour.live/join), saisissez votre **nom** et le **code de réunion**, puis rejoignez la réunion.  
    - Si la réunion est **protégée par un mot de passe**, saisissez le mot de passe fourni par l’organisateur. 
 - Si la réunion nécessite une **authentification**, vous devrez **vous connecter à votre compte Avatour** avant de rejoindre la réunion.

> **Astuce n° 1 :** si votre caméra ou votre micro ne fonctionne pas, il se peut qu’ils soient utilisés par une autre application (par exemple Microsoft Teams ou Zoom). Fermez toutes les applications susceptibles d’utiliser votre caméra ou votre micro, puis quittez la réunion Avatour et rejoignez-la à nouveau.  

> **Astuce n° 2 :** Si vous ne parvenez toujours pas à rejoindre la réunion, effectuez ce test : [https://avatour.live/test](https://avatour.live/test).  
> Ce test permet de déterminer si votre **pare-feu d’entreprise ou votre réseau** bloque l’accès, et vous fournira des informations utiles pour orienter vos échanges avec votre équipe informatique.  

> **Conseil n° 3 :** N’utilisez **pas** les applications Avatour pour iOS ou Android pour rejoindre des réunions. Ces applications ne sont nécessaires que pour **diffuser en direct une réunion à partir d’une caméra Insta360**, car ces caméras ne peuvent pas exécuter directement le logiciel Avatour 360° et nécessitent l’aide d’un smartphone.

##### Visiter un espace de travail Avatour (sans rejoindre une réunion Avatour)

Vous pouvez accéder à un espace de travail de différentes manières :

- **Espace de travail public :**  
  Si l’espace de travail est public, le lien est accessible directement — aucune connexion n’est requise.

- **Espace de travail restreint :**  
  Si l’espace de travail est restreint, vous devez être ajouté en tant que **collaborateur** disposant des droits d’**éditeur** ou de **visiteur**.

    1. Lorsque vous serez ajouté en tant que collaborateur, vous recevrez une **notification par e-mail** contenant un lien vers l’espace de travail.
    2. Cliquez sur le lien figurant dans l’e-mail pour ouvrir l’espace de travail. Si vous n’êtes pas encore connecté, vous serez invité à **vous connecter ou à vous inscrire**.
    3. Une fois connecté, l’espace de travail s’ouvrira automatiquement.

  Vous pouvez également vous connecter à l’adresse [https://avatour.live/login](https://avatour.live/login) et accéder à l’espace de travail depuis votre **liste d’espaces de travail**.

#### 3.1.2 Casque VR {#vr-headset}
Vous pouvez rejoindre une réunion et visiter un espace de travail à partir d'une gamme de casques Meta et Pico compatibles. Pour ce faire : 

1. Installez notre application Avatour depuis la boutique d’applications VR de votre choix : [Comment installer l’application Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Lancez notre application et saisissez le code de la réunion ou sélectionnez un espace de travail pour rejoindre une réunion. Pour plus d’informations sur l’utilisation de notre application VR, consultez notre article de la base de connaissances [ici](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Outils de collaboration pour les réunions et les espaces de travail {#meeting-tools}

Avatour permet la collaboration dans deux contextes principaux :

1. **Réunions (synchrones) :** collaborez en temps réel avec d’autres participants, notamment lors de visites de sites en direct ou pour examiner ensemble des contenus enregistrés.  
2. **Espaces de travail (asynchrones) :** examinez les ressources et interagissez avec elles selon votre propre emploi du temps, 24 h/24 et 7 j/7.

Les **outils de collaboration sont pour l’essentiel similaires** entre les réunions et les espaces de travail, avec quelques différences liées au contexte synchrone ou asynchrone.

#### 3.2.1 Organisation de l’interface

L’interface d’Avatour s’articule autour de trois zones principales :

- **Panneau de gauche** – Ressources de l’espace de travail et outils d’accompagnement  
- **Zone centrale** – Zone d’affichage principale pour la vidéo en direct, les ressources et le tableau de bord de l’espace de travail  
- **Panneau de droite** – Informations contextuelles, telles que les participants, les réunions ou le chat  

La plupart des interactions sont lancées à partir du **menu du bas**.  
Cliquer sur une option du menu ouvre un **panneau latéral** à gauche ou à droite de l’écran, tandis que le **canevas central** reste la zone d’affichage principale.

---
#### 3.2.2 Exemple d’affichage d’une réunion

Voici un exemple d’affichage dans une réunion Avatour :

![Interface utilisateur d’une réunion Avatour avec le panneau des ressources, le canevas vide et le panneau des participants](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Réunion Avatour avec le panneau des ressources (à gauche), le canevas (au centre) et le panneau des participants (à droite)*

---

#### 3.2.3 Exemple d'affichage de l'espace de travail

Voici un exemple d'affichage de l'espace de travail :

![Espace de travail Avatour avec le panneau « Ressources », un canevas vierge et le panneau « Réunions »](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espace de travail Avatour avec le panneau « Ressources » (à gauche), le canevas (au centre) et le panneau « Réunions » (à droite)*

---

#### 3.2.4 Présentation du menu inférieur

Le menu inférieur permet d’accéder aux commandes et aux panneaux principaux de l’interface :

**Menu inférieur « Réunion »**  

![Menu inférieur de réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu inférieur de réunion Avatour*

- **Ressources** – Consultez les fichiers de l'espace de travail, notamment les vidéos enregistrées, les images, les captures d'écran et les PDF. 
- **Chat** – Envoyez des messages à tous les participants à la réunion.  
- **Caméra** – Activez ou désactivez votre webcam.  
- **Microphone** – Activez ou désactivez votre micro.  
- **Présenter** – Présentez un élément, votre bureau ou le flux de votre webcam (voir la section « Présenter » ci-dessous).  
- **Outils de l’animateur** (animateurs uniquement) :  
    - **Verrouiller la vue** – Verrouiller la vue pour tous les participants. 
 - **Couper le son de tous** – Couper le son de tous les participants.  
- **Passer en plein écran** – Afficher l’onglet de la réunion en plein écran.  
- **Quitter la réunion** – Quitter la réunion.  
- **Démarrer l'enregistrement** – Utilisez ce bouton pour démarrer et arrêter manuellement l'enregistrement pendant une réunion. Les réunions peuvent également être enregistrées automatiquement si l'option **« Démarrer automatiquement l'enregistrement »** est activée dans les paramètres de l'espace de travail. Dans les deux cas, les enregistrements sont sauvegardés dans les ressources de l'espace de travail.
- **Carte** – Ouvrez ou fermez le panneau de carte pour visualiser le déplacement de la caméra pour les ressources dotées d’un tracé GPS. Cliquer sur un emplacement permet d’accéder directement à ce point précis dans la vidéo. La carte se met à jour en temps réel au fur et à mesure de la lecture de la vidéo. Les notes s’affichent également sur la carte.
- **Participants** – Ouvrez ou fermez le panneau des participants.  
- **Infos sur la réunion** – Affichez le code de la réunion, le lien vers la réunion et accédez aux tutoriels associés.  

![Informations sur la réunion Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panneau latéral « Informations sur la réunion Avatour »*

- **Paramètres** – Réglez les paramètres de langue, d’audio et de vidéo. Pour les réunions vidéo en direct à 360°, utilisez **Afficher le débit binaire** pour surveiller les statistiques de connexion.

> Astuce : envoyez le lien de la réunion ou ajoutez-le à un événement de calendrier pour inviter les participants.

---

##### Menu « Présenter »

L’option **Présenter** dans le menu inférieur de la réunion vous permet de partager du contenu avec tous les participants.

- **Caméra** – Partagez la caméra de votre appareil (ordinateur portable, smartphone, etc.). Cette fonction peut également être utilisée lors d’une réunion vidéo en direct à 360° pour superposer une vue secondaire afin de montrer des gros plans ou des détails spécifiques. Lorsque vous partagez la caméra d’un smartphone (avant ou arrière), les participants à distance peuvent utiliser le zoom du smartphone et activer ou désactiver la lampe torche.
- **Bureau** – Partagez l’écran de votre bureau avec tous les participants.  
- **Ressource** – Présentez une ressource depuis l’espace de travail. La sélection d’une ressource ouvre la **barre d’outils Ressource**, qui fournit des commandes de lecture et des outils de collaboration spécifiques à la ressource présentée.

##### Barres d’outils « Ressource » et « Live 360° » lors des réunions

Lors de la présentation d’une ressource au cours d’une réunion, la **barre d’outils « Ressource »** apparaît au-dessus du canevas. Voici les outils et les éléments de menu disponibles lors de la <u>présentation d’une ressource au cours d’une réunion</u> – expliqués de gauche à droite.

![Menu Avatour lors de la présentation d’un élément dans une réunion](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu Avatour lors de la présentation d’un élément dans une réunion*

Lorsqu’une vidéo 360° en direct est diffusée lors d’une réunion, ce menu s’affiche au bas de la zone de travail.

<img src="https://res.cloudinary.com/avatour/image/upload/c_fill,g_auto,w_600,h_120/avatour-screenshot-live360video-menu-meeting_cguwzb.png" alt="Menu Avatour avec vidéo 360° en direct lors d’une réunion" style="width:50%; display:block; border:1px solid #DDE5EA; border-radius:6px; margin:20px 0 4px;"> *Menu Avatour avec vidéo en direct à 360° lors d’une réunion*

Voici une description de tous les éléments affichés dans les menus ci-dessus.

- **Chronologie vidéo / Barre de progression** – Affiche la progression de la vidéo avec des notes et des thèmes clés extraits de l’audio. Cliquez sur une note ou un thème pour passer à ce moment précis et ouvrir la note. Comprend des commandes **Lecture / Pause**.   
- **Instantané** – Permet de capturer une image à 360° ou en 2D à partir de la ressource.  
- **Pleins feux** – Met en évidence une zone spécifique pour tous les participants pendant les sessions en direct.  
- **Afficher/Masquer le point de vue (POV)** – Affiche la direction du regard de chaque participant dans la vidéo à 360°.  
- **Notes** – Créez des notes associées à des moments spécifiques d’un contenu ou pendant un flux vidéo en direct. (N.B. : lors d’un streaming en direct, un élément = instantané sera automatiquement créé pour capturer la note). Chaque note possède un auteur et peut être classée par catégorie (Observation, Problème, Action, Recommandation), suivie par statut (Ouverte → En cours → Résolue), attribuée à un responsable et partagée via des liens directs. Si le fichier dispose d’un tracé GPS, les notes affichent également les coordonnées GPS. Les notes peuvent également être déplacées vers un autre emplacement (glisser pour changer la position) et déplacées dans la chronologie (avancer ou reculer dans la chronologie).

  ![Note Avatour et filtre de notes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-notes-and-filters_g181oc.png) *Notes Avatour et filtres de notes*

- **Notes de commande vocale** – Il s’agit de marqueurs de position générés automatiquement lorsque des expressions telles que « insérer une note », « prendre une note » ou « faire une note » sont détectées dans une vidéo enregistrée. Ces notes apparaissent sur la timeline et doivent être **positionnées et finalisées** par l’utilisateur. 

  ![Notes Avatour – générées par commande vocale](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notes Avatour – générées par commande vocale*

- **Notes générées par l’IA** – Il s’agit de marqueurs de position générés automatiquement lorsque l’enregistrement détecte, dans la piste audio de la vidéo, des mentions qui semblent correspondre à des problèmes devant être consignés pour un suivi ultérieur. Les notes générées par l’IA doivent d’abord être validées par leur propriétaire (voir le tableau de bord de l’espace de travail ci-dessous). Une fois validées, elles s’apparentent aux notes issues de commandes vocales, dans la mesure où elles apparaissent sur la timeline et doivent être **positionnées et finalisées** par l’utilisateur. 

- **Panneau « Notes et résumé »** – Ouvre un panneau latéral affichant toutes les notes, les thèmes clés et un résumé exécutif de la ressource. Cliquer sur un élément vous amène à ce moment précis de la vidéo.  

  ![Résumé exécutif d’un élément Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Résumé d’Avatour lors de la présentation d’un élément lors d’une réunion*

  ![Thèmes Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Thèmes Avatour lors de la présentation d’un élément lors d’une réunion*

  Depuis le **panneau latéral**, vous pouvez **imprimer un rapport sur un élément** ou **le télécharger au format TXT ou CSV**. Les rapports peuvent inclure plusieurs éléments que vous pouvez **sélectionner avant l'exportation**. 

  ![Menus d’impression du rapport sur les ressources Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png) 
 *Menus d’impression et de téléchargement du rapport sur les ressources Avatour*  

  ![Sélection des éléments du rapport sur les ressources Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png) 
 *Menu de sélection des éléments du rapport sur les ressources Avatour*

- **Partager le lien** – Partagez un lien vers une note ou une scène spécifique de la ressource.  
- **Sous-titres (CC)** – Affichez la transcription du texte à l’écran pendant la lecture de la vidéo.

##### Barre d’outils de la ressource (Espace de travail)

Lors de la consultation d’un élément dans un espace de travail, la barre d’outils est similaire mais optimisée pour une utilisation individuelle :

![Menu Avatour lors de la présentation d’un élément en dehors d’une réunion, par exemple lors de la consultation d’un espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu Avatour lors de la présentation d’un élément dans un espace de travail*

- **Timeline vidéo / Barre de progression** – Affiche la progression de la vidéo avec des notes et des thèmes clés extraits de la piste audio. Cliquez n’importe où sur la timeline pour parcourir la vidéo. Cliquez sur une note ou un thème pour accéder à ce moment précis et ouvrir la note. Comprend les commandes **Lecture / Pause**.  
- **Instantané, Notes, Panneau des notes et du résumé, Lien de partage, Sous-titres**  
- Non disponible : **Spotlight, POV** (ces fonctionnalités nécessitent la présence de participants en direct)  
- Commandes supplémentaires :
    - **Par pas de 10 secondes** – Avance/retour rapide 
 - **Vitesse de lecture** – Réglage de la vitesse (0,5×–2×) 
 - **Découper la vidéo** – Découper le début ou la fin de la ressource


## 4. Pour les utilisateurs « Host » et « Admin » - Console Web Avatour {#for-host-and-admin-users-avatour-web-console}

Lorsque vous vous connectez à votre compte utilisateur Avatour, vous accédez à la **console Web**.  

### 4.1 Console Web - Présentation du menu principal {#web-console-overview-main-menu}

Sur le côté gauche, vous verrez les éléments de menu suivants :

![Console Web Avatour - Menu principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web Avatour - Menu principal*

- **Espaces de travail** – Organisez efficacement votre contenu. Chaque espace de travail contient des **Ressources**, des **Collaborateurs**, des **Réunions** et des **Paramètres**.  
- **Ressources** – Accédez à toutes vos ressources (vidéos, images, PDF) et gérez-les. Les administrateurs peuvent consulter toutes les ressources du compte, et les ressources partagées sont visibles par tous les utilisateurs.  
- **Profil** – Gérez votre langue et votre mot de passe.  
- **Analyses** – Suivez l’activité des sessions, l’utilisation des espaces de travail et les indicateurs de retour sur investissement.  
- **Paramètres** *(administrateurs uniquement)* – Configurez les paramètres par défaut des espaces de travail, des réunions et des ressources à l’échelle de l’organisation. Les administrateurs peuvent également personnaliser l’identité visuelle (logo, couleurs, arrière-plans).  
- **Compte** *(administrateurs uniquement)* – Gérez les utilisateurs enregistrés et les caméras à 360°.  
- **Connexion de l'appareil** – Saisissez le code affiché sur votre caméra à 360° pour l'associer à votre compte.  
- **Tutoriels** – Accédez à des tutoriels guidés.  
- **Déconnexion** – Déconnectez-vous de la console.

> Les sections telles que Profil, Connexion de l’appareil, Tutoriels et Déconnexion sont intuitives et ne comportent pas de sous-sections détaillées.

---

### 4.2 Console Web – Détails par élément de menu (avec images) {#web-console-details-by-menu-item}

#### 4.2.1 Espaces de travail

Les espaces de travail sont des unités organisationnelles flexibles qui vous permettent de gérer vos ressources, vos collaborateurs et vos réunions en un seul endroit. Vous pouvez créer un nouvel espace de travail à l’aide du bouton **Nouvel espace de travail** situé dans le coin supérieur droit.

![Console Web Avatour - Rubrique du menu principal « Espaces de travail »](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web Avatour - Rubrique du menu principal « Espaces de travail »*

Cliquez sur l'icône en forme de cloche pour afficher un résumé de l'activité de l'espace de travail au cours des 7 derniers jours.

![Console Web Avatour - Activités récentes de l'espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Activités récentes de l'espace de travail*

À l'intérieur d'un espace de travail :

![Espace de travail Avatour avec le panneau des ressources, le tableau de bord et le panneau des réunions](https://res.cloudinary.com/avatour/image/upload/v1785929001/avatour-screenshot-workspace-dashboard_dqp5ff.png) *Espace de travail avec les ressources (à gauche), tableau de bord de l’espace de travail (au centre), réunions (à droite)*

Au centre, vous voyez le tableau de bord de l’espace de travail qui vous offre une vue d’ensemble de toutes les notes contenues dans les ressources attribuées à cet espace de travail, avec plusieurs menus déroulants permettant de filtrer les notes selon divers attributs. Vous pouvez également accepter ou supprimer les notes suggérées par l’IA. Vous pouvez aussi exporter toutes les notes à partir de cette vue.

Dans les menus du bas, vous trouverez :

- **Ressources** – Gérer les fichiers attribués à cet espace de travail.  
- **Collaborateurs** – 
  Contrôlez l’accès aux espaces de travail via 
 - **Lecteur** – Peut consulter les ressources. L’invitation crée un utilisateur « Invité » si nécessaire. 
 - **Éditeur** – Contrôle total de l’espace de travail, mêmes droits que l’Hôte. L’invitation élève l’utilisateur au rang d’Hôte si nécessaire.  
> Plusieurs utilisateurs peuvent accéder simultanément à un espace de travail sans réunion. Les espaces de travail publics et les paramètres d’accès aux réunions offrent d’autres possibilités d’accès.  
- **Rapport** – Génère un rapport à l’aide d’un modèle d’inspection sur les ressources sélectionnées de l’espace de travail. Les réponses sont générées par l’IA à partir des pistes audio des vidéos sélectionnées.  

![Rapport sur l’espace de travail Avatour et sélection des éléments](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Rapport sur l’espace de travail et sélection des éléments*

- **Carte** – Affichez les emplacements des éléments équipés d’un GPS sur une carte, comme décrit ci-dessus pour les réunions. 
- **Réunions** – Organisez des réunions dans l’espace de travail.  
- **Paramètres** – Configurez les paramètres par défaut de l’espace de travail et des réunions :

![Paramètres Avatour - Vue de l’espace de travail](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Paramètres de l’espace de travail*

**Paramètres de l'espace de travail**

- **Modèle de rapport** – Sélectionnez un modèle d'inspection pour les rapports générés par l'IA. Vous pouvez les importer depuis votre compte (voir ci-dessous).  
- **Activer les notifications** – E-mails récapitulatifs quotidiens concernant les changements de statut des notes.  

![Notifications par e-mail - Exemple](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Exemple de notifications par e-mail*

- **Espace de travail public** – Toute personne disposant du lien peut consulter directement les ressources.

**Paramètres de la réunion**
  
* **Authentification requise** – Les participants doivent se connecter.  
* **Autoriser l'accès en tant qu'invité** – Permet aux utilisateurs non enregistrés de consulter les ressources.  
* **Démarrage automatique de l’enregistrement / Démarrage manuel** – Choisissez si les réunions sont enregistrées automatiquement ou si l’enregistrement est lancé manuellement.  
* **Organisateur requis** – L’organisateur doit accepter les participants ; la réunion prend fin lorsque l’organisateur quitte la session.  
* **Autoriser l’accès en tant que spectateur** – Participer sans micro ni caméra ; communiquer via le chat.  
* **Réunions protégées par mot de passe** – Exiger un mot de passe pour rejoindre la réunion.  
* **Afficher la question sur les économies de déplacement** – Demander aux participants si la réunion a permis de réduire les déplacements.  

> Les paramètres peuvent être combinés (par exemple, aucun animateur requis mais protection par mot de passe).

---

#### 4.2.2 Ressources

Gérez toutes les vidéos à 360°/2D, les images et les fichiers PDF. Importez/téléchargez des ressources, affectez-les à des espaces de travail, partagez-les avec d’autres utilisateurs, renommez-les, imprimez/téléchargez des rapports, activez le floutage des visages et la synthèse par IA.

![Console Web Avatour - Élément du menu principal « Ressources »](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Élément du menu principal « Ressources »*

Vous pouvez également générer le code HTML permettant l’intégration publique d’un élément, par exemple sur votre site web. Il suffit de cocher la case « Activer l’intégration publique », puis de cliquer sur « Enregistrer » pour obtenir le code.

![Console Web Avatour - Élément du menu principal « Ressources »](https://res.cloudinary.com/avatour/image/upload/v1785921604/avatour-screenshot-main-menu-assets-embed-code_mtau8g.png) *Éléments du menu principal : Ressources*

#### 4.2.3 Paramètres

Les utilisateurs administrateurs ont accès à ce menu pour gérer de manière centralisée les paramètres de l’ensemble de la plateforme Avatour. Chaque paramètre peut être coché ou décoché pour devenir le paramètre par défaut sur l’ensemble de la plateforme. Chaque paramètre peut également être verrouillé, ce qui signifie que le paramètre par défaut ne peut pas être modifié par les autres utilisateurs de la plateforme. Vous pouvez également y effectuer des personnalisations marketing concernant votre image de marque (logo, couleurs, etc.).

![Console Web Avatour - Paramètres du menu principal](https://res.cloudinary.com/avatour/image/upload/v1781172727/avatour-screenshot-main-menu-settings-1-of-2_fsaatf.jpg) *Section Paramètres*

#### 4.2.4 Compte

Vous pouvez ici consulter les détails de votre compte et gérer les comptes d’utilisateurs enregistrés (Hôte, Admin, Invité), y compris leurs droits d’accès à l’espace de travail, ainsi que télécharger des modèles d’inspection pour générer des rapports sur l’espace de travail (voir ci-dessus).

![Console Web Avatour - Élément de menu principal « Compte »](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-account-1-of-3_oq5amr.png) *Aperçu du compte - Sections supérieures*

![Console Web Avatour - Rubrique « Compte » du menu principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-account-2-of-3_oq5amr.png) *Aperçu du compte - Gestion des accès à l'espace de travail*

![Console Web Avatour - Élément de menu principal « Compte »](https://res.cloudinary.com/avatour/image/upload/v1772360316/avatour-screenshot-main-menu-account-3-of-3_udgyjz.png) *Aperçu du compte - Sections inférieures*

#### 4.2.5 Analyses

Fournit des informations sur les réunions, l'utilisation de l'espace de travail et les indicateurs de retour sur investissement.

![Console Web Avatour - Rubrique du menu principal « Analyses » (1 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Aperçu des analyses*

![Console Web Avatour - Rubrique du menu principal « Analyses » (2 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Activité des réunions et utilisation de l'espace de travail*

![Console Web Avatour - Rubrique « Analytics » du menu principal (3 sur 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Économies et utilisation des licences des appareils* 

## 5. Sur place - Comment utiliser le kit clé en main Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Pour commencer
Vous trouverez ici un guide en ligne très complet pour vos premiers pas avec le kit clé en main Avatour : [Guide de démarrage rapide – Kit clé en main Avatour 3.1 (configuration du Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Voici également l'image accompagnée d'instructions que vous trouverez à l'intérieur du couvercle du coffret du kit 3.1.
![Image à l'intérieur du couvercle du coffret du kit Avatour](https://res.cloudinary.com/avatour/image/upload/v1775994773/avatour-turnkey-kit-3.1-inside-lid-picture_dq4ipl.png) *Image à l'intérieur du couvercle de la mallette du kit Avatour* 

Suivez le guide et les instructions pour déballer, assembler et mettre en marche votre caméra.

---

### 5.2 Conseils utiles

#### Batterie externe – Des réunions en direct plus longues et une meilleure gestion thermique 

La batterie interne de la caméra a une autonomie d'environ 30 à 45 minutes. Une alerte s'affiche lorsque la batterie est faible. Grâce à une batterie externe, vous pouvez prolonger l'autonomie, voire la rendre illimitée, car vous pouvez changer de batterie pendant l'utilisation.

- **Si votre kit comprend une batterie Ulanzi :** fixez-la entre la base du trépied et la perche télescopique, puis connectez la batterie à la caméra via USB-C.  

- **Si votre kit comprend une perche avec batterie Telesin :** fixez la caméra directement sur la perche télescopique Telesin équipée d’une batterie et connectez-la via USB-C.  

Utilisation de la batterie externe :

1. Prolonge l’autonomie totale de ~40 minutes (batterie de la caméra uniquement) à ~3 heures.  
2. Renforce la stabilité de l’installation de la caméra.  
3. Contribue à prévenir tout risque de surchauffe.  

> Nous vous recommandons d’utiliser systématiquement la batterie externe dès le début, en particulier pour les réunions en direct.

#### Considérations audio pour les réunions en direct et les enregistrements

- **Environnements bruyants :** 
  Utilisez le casque Shokz fourni dans votre kit pour une capture audio claire. 
 - **Mise en marche/arrêt :** Maintenez le bouton « + » enfoncé pendant 3 secondes (LED bleue = allumé, LED rouge = éteint). 
 - **Mode d’appairage Bluetooth :** Lorsque le casque est éteint, maintenez le bouton « + » enfoncé pendant 5 secondes (la LED clignote en bleu/rouge). 
 - **Volume :** utilisez les boutons « + » et « - ».  

- **Environnements plus calmes / plusieurs participants près de la caméra :** 
  Utilisez le haut-parleur à clipser NoxGear. Il n’offre pas la même qualité audio que les haut-parleurs de conférence (par exemple, le Jabra Speak), mais il se fixe facilement à votre chemise et capte efficacement les voix à proximité. 
 - **Mise en marche/arrêt :** maintenez le bouton Lecture/Pause enfoncé pendant 2 secondes.  
    - **Mode d’appairage Bluetooth :** Passe automatiquement en mode d’appairage à la mise sous tension (la LED clignote en bleu/rouge ; elle reste allumée en bleu une fois l’appairage effectué). 
 - **Volume :** Utilisez les boutons « + » et « - ».  

- **Utilisation de votre propre appareil :** si vous préférez une autre solution (par exemple, un haut-parleur de conférence ou un casque personnel), vous pouvez l’appairer via la caméra : Paramètres → Bluetooth.  

#### Connectivité
**Avant de commencer :** assurez-vous de disposer d’une connexion Internet via :

- **Wi-Fi local** (de préférence)
- **Réseau mobile** (si vous êtes hors de portée du Wi-Fi)

**Débit recommandé :** 10 Mbps en upload/download pour un streaming à 360° complet (~5 Mbps). Un débit inférieur (1 à 2 Mbps) ne fonctionne que lorsque vous restez immobile.

##### Tester la vitesse du réseau
- **Test sur un seul emplacement :** Utilisez n’importe quel outil de mesure de débit que vous utilisez habituellement (par exemple, [Speedtest](https://www.speedtest.net)) pour vérifier à la fois le débit montant et descendant.   
- **Test en se déplaçant sur le site :** Depuis la caméra : Paramètres → Réseau → Test de connexion. Parcourez l’ensemble de l’espace pour vérifier la couverture et la bande passante.

##### Wi-Fi local
- Fortement recommandé pour des connexions stables.  
- Si le service informatique exige une liste blanche, retrouvez l’adresse MAC : Paramètres → À propos → Adresse Wi-Fi.

##### Réseau mobile
**Option A : hotspot et carte SIM fournis avec le kit**  

- Fixez le hotspot GlocalMe à la batterie Telesin (aimant).  
- Cela évite les interférences et maintient la connexion si vous vous éloignez de la caméra.  
- Dépannage :
    - Vérifiez que la carte SIM préinstallée est bien celle fournie (et non une carte SIM Cloud).  
    - Activez la 5G dans le gestionnaire de carte SIM. 
 - Vérifiez que l’APN correspondant à votre région est correctement configuré ([Guide de configuration de l’APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Option B : Point d'accès personnel / carte SIM**
- Utilisez votre propre smartphone ou un point d'accès dédié.  

**Remarque importante :**  
> Laissez le point d'accès désactivé lorsque vous êtes connecté au Wi-Fi ; n'activez-le que lorsque vous êtes hors de portée. Le système d’exploitation de la caméra bascule dynamiquement entre les réseaux Wi-Fi en fonction de la puissance du signal et peut passer par inadvertance au point d’accès même lorsqu’une connexion Wi-Fi est disponible.

> Les réseaux mobiles peuvent limiter la bande passante de manière inattendue. Vérifiez auprès de votre opérateur les limites de votre forfait de données, ou contactez l’assistance Avatour si vous utilisez notre point d’accès et notre carte SIM.

##### Situations de faible bande passante
- Enregistrez à l’avance des vidéos de lieux pour les visionner ultérieurement ([guide d’enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Partagez le flux vidéo de la caméra d’un smartphone pour pallier les zones à faible bande passante (0,1 à 0,3 Mbps en upload).

##### Absence de connexion
- Seules les vidéos préenregistrées peuvent être utilisées ([guide d’enregistrement](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Autres participants sur place – Bonnes pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même lieu que la caméra à 360°, une gestion rigoureuse de l’**audio et de la bande passante** est essentielle :  

- Chaque smartphone, tablette ou ordinateur portable connecté sur place consomme de la bande passante et peut nuire à la qualité du flux vidéo de la caméra à 360°.  
- La présence de plusieurs microphones et haut-parleurs dans le même espace peut provoquer un **retour audio**, rendant l’expérience de la réunion désagréable pour tous les participants.

#### Autres participants sur place – Bonnes pratiques

Lorsque plusieurs participants rejoignent une réunion Avatour en direct depuis le même lieu que la caméra à 360°, une gestion rigoureuse de l’**audio et de la bande passante** est cruciale :  

- Chaque smartphone, tablette ou ordinateur portable connecté sur place consomme de la bande passante réseau et peut nuire à la qualité du flux vidéo de la caméra à 360°.  
- La présence de plusieurs microphones et haut-parleurs dans le même espace peut provoquer un **retour audio**, rendant l’expérience de réunion désagréable pour tous les participants.

Pour remédier à ces problèmes, suivez ces **bonnes pratiques** :

- **Utilisez des écouteurs filaires ou sans fil :** de préférence avec une fonction de réduction du bruit pour éviter l’écho et le larsen.  
- **Mode « Sur place » :** rejoignez la réunion en mode « Sur place » lorsque vous êtes physiquement présent à proximité de la caméra à 360°, car ce mode est optimisé pour une utilisation sur site :

 - Il coupe par défaut le micro et les haut-parleurs du participant.
    - Il **ne** diffuse **pas** le flux vidéo du participant.
    - N’affiche **pas** le flux de la caméra à 360° dans le navigateur du participant.
    - Économise la bande passante du réseau, garantissant ainsi que la caméra à 360° dispose d’une capacité de téléchargement maximale pour la diffusion en direct.
    - Utile lorsqu’un utilisateur souhaite partager des détails spécifiques ; vous **pouvez partager à votre tour le flux de votre caméra** pour offrir des vues ciblées.
- **Coupez le son lorsque vous ne parlez pas :** cela évite les retours audio indésirables et les distractions.
- **Utilisez un réseau distinct si possible :** connectez votre smartphone à un réseau différent de celui de la caméra afin de réduire les interférences.

Le respect de ces consignes garantit une visite en direct fluide et de haute qualité, tant pour les participants sur place que pour ceux à distance.

### 5.3 Application Avatour Camera

Voici les menus (1) Niveau supérieur, (2) Paramètres et (3) Paramètres réseau.

![Application Avatour 360° Camera - Les trois menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Application Avatour 360° Camera - 3 menus*

**Capture rapide** - Pour l’enregistrement hors ligne de vidéos à 360° sur la carte mémoire SD de la caméra 360°. - Pour une description détaillée, consultez [Comment enregistrer et mettre en ligne des vidéos à 360° avec l'application Avatour ?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Nous vous recommandons d’utiliser un périphérique audio externe (connecté via Bluetooth). N.B. : Vous pouvez également modifier l’angle de prise de vue de 360° à 270°, 180° ainsi qu’en vidéos et photos 2D standard, par exemple pour mettre l’accent sur certains éléments ou masquer des zones confidentielles — il suffit de changer de mode dans le coin inférieur droit une fois sur l’écran de capture rapide (*ceci n’est toutefois possible que si une résolution 4K est sélectionnée dans les paramètres de la capture rapide — voir ci-dessous*)

**Réunion en direct** – Pour les visioconférences en direct à 360°. Vous verrez vos espaces de travail et, en cliquant sur l’un d’entre eux, vous lancerez le flux vidéo en direct depuis la caméra à 360°. Avant de pouvoir rejoindre la réunion avec votre caméra à 360°, vous devez connecter un périphérique audio via Bluetooth. Pour une description détaillée, consultez [Comment démarrer une réunion Live Capture avec votre caméra Pilot ?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Lorsque vous organisez une réunion Live Capture avec votre caméra à 360°, vous disposez d’outils de réunion similaires à ceux de l’expérience Web. Voici un lien vers notre article de la base de connaissances qui explique ces outils plus en détail : [Outils de l’application opérateur](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galerie** - Retrouvez ici toutes vos vidéos et photos à 360° à importer dans la console Web Avatour. Vous pouvez importer et supprimer des ressources en masse : appuyez sur « Sélectionner » en haut de l’écran. Avant l’importation, vous pouvez choisir plusieurs étapes de traitement telles que « Flouter les visages », générer un « résumé par IA » et optimiser le signal audio avec « Améliorer la parole ». Vous pouvez même choisir un espace de travail auquel attribuer le fichier – celui-ci figurera bien sûr également dans la section des fichiers généraux de la console Web.

**Paramètres** – Dans les Paramètres, vous disposez des options suivantes :

- **Réseau** : cette option vous permet de changer le réseau Wi-Fi auquel la caméra est connectée ou d’effectuer un test de connexion réseau pour vérifier votre débit de streaming
- **Capture en direct** : ajustez vos paramètres de capture en direct en fonction de la bande passante disponible, de la sensibilité VR de l’invité ou de la présence ou non des lentilles de protection sur votre caméra :

    - **Fréquence d’images cible (facultatif)** : réglez la fréquence d’images de votre vidéo de capture en direct entre 15 ips, 24 ips et 30 ips. Des fréquences d’images plus élevées produisent une vidéo plus fluide, mais nécessitent davantage de bande passante en envoi. Par défaut : 15 ips
    - **Débit binaire cible** : vous permet d’augmenter ou de réduire le débit binaire maximal de diffusion en continu pour votre capture en direct. Vous pouvez définir votre débit binaire cible entre 1 Mbps et 10 Mbps. Des débits binaires plus élevés se traduisent par une meilleure résolution vidéo, mais nécessitent davantage de bande passante en upload. Par défaut : 5 Mbps
    - **Optimiser le mouvement** : cette option réduit la fréquence d’images de la vidéo, ce qui allège la charge sur la bande passante de téléchargement de votre réseau et augmente votre débit binaire de diffusion. De plus, elle contribue à réduire le mal des transports chez les participants en réalité virtuelle. Par défaut : Désactivé
    - **Verrouillage de la direction** : cette option « verrouille » la vue à 360°, quel que soit le mouvement que vous effectuez avec la caméra 360°. Si vous souhaitez que la vidéo à 360° suive les mouvements de la caméra, par exemple si vous souhaitez « pointer » l’objectif avant vers un objet, réglez le verrouillage de direction sur Non. La caméra se comportera alors comme une caméra traditionnelle, ce qui peut s’avérer plus utile pour les visites guidées. Par défaut : Oui
    - **Orientation initiale** : Lorsque vous réglez le verrouillage de direction sur « Non », vous pouvez choisir quelle caméra (avant ou arrière) doit servir d’orientation initiale au démarrage de la vidéo en direct. Par défaut : la caméra est orientée vers l’opérateur, car c’est la manière la plus naturelle de démarrer une réunion en direct (= caméra arrière). La capture rapide fonctionne différemment (la caméra avant est l’orientation initiale par défaut – voir ci-dessous).

- **Capture rapide** : ajustez vos paramètres de « Capture rapide » en fonction de la fréquence d’images vidéo souhaitée, de la bande passante disponible pour le téléchargement des vidéos enregistrées et d’autres préférences. Les fonctionnalités liées à la carte, telles qu’expliquées ci-dessus (par exemple, l’affichage de la carte, les notes sur une carte), sont disponibles lorsqu’un signal GPS est reçu et que le paramètre de localisation dans les réglages natifs de l’appareil photo est activé (ce qui devrait être le cas par défaut). L’icône de localisation / GPS située dans le coin supérieur droit de la fenêtre « Capture rapide » doit être verte. La réception du signal GPS et l’établissement de la connexion peuvent prendre quelques instants.
    - **Résolution** : vous pouvez modifier la résolution ici. *(Les résolutions 6k sont expérimentales et nécessitent une étape d’assemblage manuel dans la Galerie avant le téléchargement vers la console Web Avatour.)*

        - **4k** - Il s'agit de la résolution standard, qui offre un bon compromis entre qualité vidéo et taille de fichier.
 - **6k à 30 images par seconde** *(nécessite une étape supplémentaire d'assemblage dans la Galerie)*
        - **6k à 10 images par seconde** *(nécessite une étape d’assemblage supplémentaire dans la Galerie)* - Cette option est utile si vous souhaitez réduire la taille du fichier par rapport à celle obtenue avec 30 images par seconde, lorsque la fluidité du mouvement est moins importante.
        - Pour d’autres résolutions, vous pouvez également utiliser les applications natives de l’appareil photo, y compris sur le PanoX V2. Pour plus de détails, consultez [Comment enregistrer et mettre en ligne des vidéos à 360° avec l’application Avatour ?](https://avatour.com/support/comment-enregistrer-et-publier-des-vidéos-à-360°-avec-l'application-Avatour)
    - **Fréquence d’images cible** *(disponible uniquement pour la résolution 4K)* - Réglez la fréquence d’images de vos enregistrements vidéo en mode « Quick Capture » entre 15 ip, 24 ip et 30 ip. Des fréquences d’images plus élevées produisent une vidéo plus fluide, mais augmentent la taille du fichier vidéo et le temps de mise en ligne. Recommandé : 30 images par seconde
    - **Débit binaire cible** *(disponible uniquement pour la résolution 4K)* Définissez le débit binaire cible pour les téléchargements en « Quick Capture » entre 5 Mbps et 20 Mbps. Des débits binaires plus faibles augmentent la vitesse de téléchargement, mais réduisent la qualité vidéo. Recommandé : 20 Mbps
    - **Verrouillage de l’orientation** : identique à ce qui précède dans la section « Capture en direct ». L’orientation initiale par défaut est toujours l’objectif avant pour la « Capture rapide ».

  > Consultez également notre [Calculateur de taille de fichiers vidéo Avatour 360°](https://avatour.com/support/avatour-360deg-video-file-size-calculator) pour obtenir des conseils supplémentaires sur les paramètres ci-dessus et la taille des fichiers vidéo. Pour éviter d’épuiser l’espace de stockage, une alerte s’affichera afin que vous puissiez arrêter l’enregistrement et libérer de l’espace (par exemple en transférant des vidéos de la Galerie vers les ressources de la console Web Avatour).

- **À propos** : affiche le numéro de série de l’appareil et la version du logiciel

**Compte** - Permet de vous connecter avec votre compte hôte ou administrateur Avatour.

## 6. Conseils sur les meilleures pratiques {#best-practice-advice}

### 6.1 Premières utilisations (informelles) et prise en main

Pour vos premières utilisations et pour vous familiariser avec la console Web Avatour et le kit clé en main Avatour, nous vous recommandons de suivre les étapes suivantes :

1. Emportez le kit chez vous et testez-le avec votre famille et vos amis en utilisant votre connexion Internet domestique.
2. Apportez le kit au bureau et connectez-vous au réseau de l’entreprise (des problèmes spécifiques à l’entreprise peuvent survenir, par exemple liés aux pare-feu d’entreprise, mais vous savez déjà, grâce à la première étape, qu’Avatour fonctionne et qu’il s’agit d’un sujet à régler par votre équipe informatique avec l’aide d’Avatour).
3. Commencez à utiliser Avatour sur place (en dehors de vos bureaux), sur le lieu de réunion où les participants à distance devraient normalement se rendre. D’autres problèmes de connectivité pourraient apparaître ; Avatour vous aidera en collaboration avec votre équipe informatique.
4. Commencez à utiliser la solution avec des participants à distance, tant internes qu’externes.

### 6.2 Avant une réunion en direct avec vidéo à 360°

- Nous vous recommandons de réaliser une visite guidée enregistrée en vidéo à 360° avant toute visite en direct si le temps le permet, et ce pour trois raisons : (1) Disposer d’une solution de secours pour la visite en direct, (2) disposer d’un support de documentation et de révision ultérieure (en plus de la visite en direct enregistrée) et (3) commencer à créer une bibliothèque de vidéos à 360° de tous vos sites, ce qui peut s’avérer utile dans de nombreux cas de figure. 

- Chargez tous les composants du kit pendant au moins 90 minutes avant la réunion en direct. Nous vous recommandons de laisser tous les appareils en charge continue lorsqu’ils ne sont pas utilisés. Ainsi, tous les appareils seront toujours prêts, même pour des réunions imprévues et ponctuelles.

- Assurez-vous que le kit est entièrement assemblé (1. socle du trépied + 2. batterie Ulanzi + 3. perche télescopique + 4. caméra à 360°).

- Vérifiez qu’un espace de travail a bien été créé pour accueillir une réunion en direct et incluez-y toutes les ressources pertinentes.

- Invitez tous les participants à la réunion via votre espace de travail. Cela génère une invitation sur les agendas de tous les participants et inclut le lien d’invitation à la réunion.

- Appairez et connectez à la caméra le casque ou l’enceinte Bluetooth que vous prévoyez d’utiliser pour votre visite guidée.

- Tous les utilisateurs de smartphones présents sur place doivent se connecter à un réseau différent de celui de la caméra. Cela permettra de réduire la charge sur la bande passante du réseau de la caméra.

- Si vous êtes seul en tant qu’opérateur caméra, emportez un smartphone avec vous au cas où vous souhaiteriez partager l’écran de votre smartphone pour montrer des détails précis.

- Vérifiez que la caméra à 360° peut se connecter à votre réseau Wi-Fi local.

- Avant une réunion Avatour, planifiez l’itinéraire que vous emprunterez dans les locaux. Effectuez une réunion Avatour test avec la caméra et vérifiez que toutes les zones disposent d’un débit supérieur à 1 Mbps. Vous pouvez consulter cette information directement sur l’écran de la caméra ou, en tant que participant à distance, en accédant aux Paramètres et en activant l’option « Afficher le débit ».

- Si vous constatez que certaines zones disposent d’une bande passante faible, voire inexistante, il est préférable de prendre des photos ou d’effectuer un enregistrement. Ceux-ci pourront ensuite être présentés pendant la réunion afin que les participants à distance puissent les examiner. Vous pouvez suivre le guide ci-dessus qui explique notre fonctionnalité « Quick Capture » pour l’enregistrement hors ligne et le téléchargement de vidéos/images.

- Si des participants à distance qui n’ont jamais utilisé Avatour auparavant rejoignent la réunion, fournissez-leur un bref résumé de la plateforme, de ses fonctionnalités (vidéo 360° en direct, ressources, instantanés, annotations, mise en avant) et des outils de réunion.

- Vous pouvez commencer par une autre solution de visioconférence (par exemple Teams, Zoom, Google Meet), mais avant de basculer vers Avatour, fermez complètement l’autre application de visioconférence. Dans certains cas, ces autres applications donneront la priorité au microphone, aux haut-parleurs ou à la webcam de votre appareil, ce qui les désactivera pour Avatour. De plus, n’utilisez PAS Avatour ET une autre solution de visioconférence en même temps, car cela réduirait la bande passante disponible.

- Si vous prévoyez d’utiliser la caméra 360° dans un environnement à haute température, il est recommandé d’utiliser le module de refroidissement (Pilot Pano uniquement). Cela permettra de réduire les risques de surchauffe de la caméra et de son arrêt automatique.

### 6.3 Utilisation de la caméra sur place pour une réunion vidéo en direct à 360°

- Lorsque vous utilisez la caméra, veillez à **marcher lentement** et à **vous arrêter fréquemment pour poser la caméra sur son trépied**. Cela permet (1) d’améliorer la qualité vidéo, car vous générez moins de données vidéo en évitant de déplacer inutilement la caméra, et (2) de réduire les éventuels temps d’interruption vidéo lorsque la connexion réseau de la caméra bascule d’un point d’accès Wi-Fi à un autre.

- Tenez la caméra devant vous, au-dessus du niveau des yeux. Cela permet à tous les participants à distance de voir la majeure partie de votre environnement.

- Lorsque la caméra doit rester stable, utilisez le trépied et réglez-la à la bonne hauteur, de préférence à hauteur des yeux.

- Connectez toujours la caméra à votre réseau Wi-Fi local lorsque cela est possible. Dans les zones sans accès Wi-Fi, utilisez le hotspot fourni. Le hotspot est équipé d’une carte SIM qui se connectera à un réseau mobile fiable à proximité. Veillez à toujours éteindre le hotspot lorsqu’il n’est pas utilisé à l’intérieur, car sinon la caméra à 360° pourrait s’y connecter, ce que nous souhaitons éviter en intérieur. À l’extérieur, gardez le hotspot à proximité de la caméra à 360°.

- Lorsque le débit de la caméra commence à descendre en dessous de 2 Mbps, marchez plus lentement ou arrêtez-vous complètement jusqu’à ce que le signal se stabilise à nouveau. Cela se produit généralement lorsque vous passez d’un point d’accès Wi-Fi à un autre. 

- Si vous savez que la connexion et la qualité vidéo vont se dégrader lorsque vous vous déplacez vers un endroit précis (par exemple : en passant d’une zone de production intérieure à une zone extérieure), prévenez les participants à distance à l’avance.

- Si vous devez montrer un élément très détaillé ou comportant du texte en petits caractères, vous pouvez vous approcher très près avec la caméra à 360° ; vous pouvez également utiliser votre propre smartphone ou celui d’un participant sur place pour rejoindre la réunion et présenter la caméra (arrière) de votre téléphone ou du sien.

- Si possible, nous recommandons qu’une personne supplémentaire soit présente sur place pour aider au partage de la caméra du smartphone décrit ci-dessus, car cela s’avère souvent utile, voire nécessaire.

- Idéalement, les utilisateurs de smartphones présents sur place devraient rejoindre la réunion (1) en mode « sur place » et (2) sur un réseau différent de celui utilisé par la caméra, afin de ne pas priver la caméra à 360° d’une bande passante de téléchargement essentielle.

- Tous les participants présents sur place qui se connectent depuis leur smartphone doivent avoir le son coupé, sauf s’ils prennent activement la parole.

### 6.4 Utilisation de la caméra sur place pour une capture rapide (enregistrement vidéo à 360° hors ligne)

- Les conseils ci-dessus, qui ne concernent pas la connectivité, s’appliquent également de manière générale à l’enregistrement hors ligne (par exemple, procédez lentement).

- Utilisez toujours un casque audio Bluetooth externe.

- Vérifiez que le GPS fonctionne lorsque cela est nécessaire.

- Anticipez ce que les spectateurs voudront voir, par exemple des détails : approchez-vous au plus près avec la caméra à 360° et attendez quelques instants.

- Posez la caméra et pointez-la vers les éléments que vous souhaitez mettre en avant. Si vous réglez le verrouillage de direction sur « Non », vous pouvez même pointer vers un élément avec la caméra à 360° (par exemple en utilisant l’objectif avant).  

- Si vous effectuez un enregistrement en vue d’obtenir un rapport généré par l’IA et que vous utilisez également des commandes vocales, parlez fort et clairement. Pour aider l’IA à identifier les emplacements, les mesures et les problèmes, et pour remplir vos modèles d’inspection, mentionnez-les explicitement et utilisez la même terminologie que celle employée dans votre modèle.


> N.B. : La plupart des fonctionnalités d’Avatour sont également disponibles pour les vidéos 2D.
