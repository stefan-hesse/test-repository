# Guía del Usuario y Mejores Prácticas de Avatour

## 1. Para Todos los Usuarios de Avatour {#for-all-avatour-users}

Si eres nuevo en Avatour, los siguientes recursos ofrecen una útil introducción a la plataforma y sus capacidades:

1. [Video de Cómo Funciona Avatour](https://avatour.com/how-it-works)  
   Una breve descripción general de las principales funciones de Avatour y cómo la plataforma permite la colaboración remota inmersiva.
2. [Preguntas Frecuentes](https://avatour.com/faqs)  
   Respuestas a las preguntas más frecuentes
3. [Glosario](https://avatour.com/glossary)  
   Definiciones de los principales términos y conceptos de Avatour.
4. Sitio Web  
   Consulta la página de [Funcionalidades de Avatour](https://avatour.com/features) junto con las secciones dedicadas a Casos de Uso e Industrias para conocer cómo Avatour puede apoyar tus necesidades específicas.

## 2. Tipos de Usuarios de Avatour {#avatour-user-types}

### 2.1 Asistentes a la Reunión (Sin Cuenta Requerida)
Los usuarios pueden unirse a la reunión sin registrarse en una cuenta de Avatour. Excepción: Si el anfitrión ha restringido la reunión a usuarios registrados — por ejemplo, para permitir que solo los empleados internos se unan mediante Single Sign-On (SSO) — la invitación del calendario indicará que los participantes deben iniciar sesión para autenticarse.

Los usuarios acceden a la reunión de la siguiente manera:

- Reciben una invitación del calendario del anfitrión.
- Usan el enlace de la reunión en la invitación para unirse.
- Introducen una contraseña de reunión si el anfitrión ha habilitado una.
- Los participantes pueden unirse sin una cuenta de Avatour a menos que la reunión esté restringida y requiera inicio de sesión para autenticarse.

#### 2.1.1 Participante

- Puede unirse e interactuar completamente (cámara web, micrófono, chat y funcionalidad Presentar).
- Máximo de 20 participantes interactivos por reunión.

#### 2.1.2 Espectador

- Puede ver la reunión y participar solo mediante chat.
- No puede compartir video, usar micrófono, presentar, reproducir/pausar Assets ni capturar Snapshots.
- Máximo de 10 Espectadores por reunión.
- Junto con los Participantes, una reunión puede albergar hasta 30 asistentes.

### 2.2 Usuarios Registrados

Los Usuarios Registrados tienen una cuenta de Avatour. Las cuentas se crean de una de las siguientes maneras:

- **Invitado por Admin:** Durante la incorporación, Avatour configura un **tenant dedicado** para la organización y crea una o más **cuentas Admin**. Los Admins pueden entonces **invitar usuarios** dentro de la organización y asignarlos a **grupos**, que definen su rol en la plataforma (Guest, Host o Admin). Los usuarios invitados reciben un **enlace de registro** para completar la configuración de la cuenta y establecer una contraseña.
- **Invitado por Host:** Los Hosts pueden agregar usuarios como **colaboradores Editor** a un Workspace. Esto consume una **licencia Host** y garantiza que el usuario tenga acceso de nivel Host.
- **Aprovisionamiento automático SSO (solo nivel Enterprise/Business):** Las cuentas pueden crearse automáticamente mediante el IdP. Por defecto, las cuentas aprovisionadas por SSO se agregan al **grupo Guest**, a menos que se sobrescriban mediante **asignaciones de grupo SAML**. Los Admins aún pueden invitar usuarios y asignar membresías de grupo directamente incluso cuando SSO está habilitado.

**Resumen:**

Los usuarios registrados y su membresía de grupo pueden gestionarse de múltiples formas:

- **Gestión Admin:** Un Admin en la consola de Avatour puede crear usuarios y asignarlos a grupos, que definen su rol en la plataforma (Guest, Host o Admin).
- **Aprovisionamiento SSO:** Para clientes de nivel Enterprise o Business con SSO habilitado, el IdP puede aprovisionar automáticamente cuentas y asignar membresías de grupo, que definen el rol del usuario en la plataforma.
- **Usuarios invitados por Host:** Los Hosts pueden invitar a otros usuarios como colaboradores Editor a Workspaces específicos. Asignar el rol de colaborador Editor consume una licencia Host.

**Práctica Recomendada (Clientes Enterprise):**
Para organizaciones que esperan un gran número de usuarios que necesitan acceso a Avatour, se recomienda **integrar Single Sign-On (SSO)** y gestionar usuarios y membresías de grupo desde el **IdP**. Este enfoque agiliza el aprovisionamiento de cuentas, la asignación de grupos y la gestión de licencias, reduciendo la carga administrativa y garantizando un control de acceso coherente.

#### 2.2.1 Usuarios Guest

- Agregados al **grupo Guest**.
- Pueden **ver Assets** dentro de los Workspaces donde han sido agregados como **colaboradores Viewer**.
- No pueden crear workspaces, organizar reuniones ni cargar contenido.
- Las cuentas Guest aprovisionadas por SSO **se autentican mediante el IdP**; no se requiere contraseña gestionada por Avatour.

---

#### 2.2.2 Usuarios con Licencia (Acceso a la Consola Web)

##### Usuarios Host (Grupo: Host)

- Pueden crear/gestionar Workspaces, invitar colaboradores a un workspace, **organizar reuniones en vivo**, cargar **Quick Captures**.
- Tienen acceso al **Panel del Host** y a la **App de Operador** en cámaras 360° compatibles.

##### Usuarios Admin (Grupo: Admin)

- Incluye todas las capacidades Host más la administración completa de la cuenta.

**Los privilegios adicionales de Admin incluyen:**

**Gestión de Cuenta**

- Crear nuevos usuarios y asignarlos a grupos.
- Restablecer contraseñas cuando son gestionadas por Avatour (no aplica cuando SSO está habilitado).
- Actualizar usuarios Guest a Host.
- Desactivar usuarios (las cuentas Admin deben convertirse primero a Host antes de la eliminación).
- Transferir assets de un usuario Host a otro durante la eliminación.

**Configuración**

- Configurar los **ajustes de seguridad a nivel organizacional** para assets, workspaces y reuniones alojadas en la plataforma (p. ej., si un Host debe estar presente para iniciar una reunión, si los rostros deben difuminarse en todos los videos cargados en la plataforma).
- Habilitar o deshabilitar las **funciones de IA** o la **grabación**.
- Aplicar la marca corporativa de forma coherente en toda la plataforma si se configura un **dominio personalizado**.

**Assets y Analytics**

- Ver todos los Assets cargados por cualquier usuario en la organización.
- Revisar el uso de la plataforma en toda la organización.

---

#### 2.2.3 Permisos de Colaboradores del Workspace

Los permisos del Workspace definen lo que un usuario puede hacer **dentro de un Workspace específico**. Estos son independientes de la membresía de grupo a nivel de plataforma (Guest, Host, Admin).

- **Colaborador Editor:** Los usuarios con este permiso pueden:
  - Gestionar Assets (cargar, eliminar, difuminar rostros, generar resúmenes)
  - Gestionar la configuración de la reunión (habilitar/deshabilitar grabación, permitir o eliminar participantes)
  - Programar y organizar reuniones en vivo
  - Generar informes basados en plantillas predefinidas
  - Agregar o eliminar colaboradores del Workspace

- **Colaborador Viewer:** Los usuarios con este permiso tienen acceso de solo lectura a los Assets del Workspace. **No pueden modificar Assets, gestionar reuniones ni gestionar colaboradores**, pero **pueden crear Notas en los Assets**.

## 3. Para Participantes de Reuniones Remotas y Visitantes del Workspace {#for-remote-meeting-participants-and-workspace-visitors}

Avatour permite a los usuarios colaborar de dos formas principales:

- **Unirse a una reunión en vivo:**
  Puedes recibir una **invitación del calendario** para unirte a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota en vivo al sitio** o revisar assets juntos de forma sincrónica.

- **Visitar un Workspace:**
  También puedes ser invitado como **colaborador a un Workspace** para revisar assets **de forma asincrónica** (según tu propio horario).

### 3.1 Cómo Unirse a una Reunión de Avatour y Visitar un Workspace de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Cualquier Dispositivo de "Pantalla Plana" con un Navegador Web {#any-flat-screen}
Puedes unirte a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, smartphone o tableta** usando un navegador web.

##### Unirse a una Reunión

> **Nota:** Unirse a una reunión de Avatour requiere que **concedas permisos de micrófono**. Por favor acepta las solicitudes de permisos de tu navegador.

1. **Mediante invitación del calendario (recomendado):**
   - Normalmente recibirás una **invitación del calendario** con un **enlace directo para unirte** (por ejemplo: `https://avatour.live/join?s=xxxxx`).
   - Al hacer clic en el enlace se completará automáticamente el **código de reunión de 5 caracteres** y te llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que necesitas **iniciar sesión para acceder a la reunión**.
   - **Reuniones protegidas con contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debes introducir para unirte.

2. **Mediante código de reunión:**
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, ve a [https://avatour.live/join](https://avatour.live/join), introduce tu **nombre** y el **código de reunión**, y únete a la reunión.
   - Si la reunión está **protegida con contraseña**, introduce la contraseña proporcionada por el anfitrión.
   - Si la reunión requiere **autenticación**, deberás **iniciar sesión con tu cuenta de Avatour** antes de unirte.

> **Consejo 1:** Si tu cámara o micrófono no funcionan, puede que estén siendo utilizados por otra aplicación (por ejemplo, Microsoft Teams o Zoom). Cierra cualquier aplicación que pueda estar usando tu cámara o micrófono, luego sal y vuelve a unirte a la reunión de Avatour.

> **Consejo 2:** Si aún no puedes unirte a la reunión, ejecuta esta prueba: [https://avatour.live/test](https://avatour.live/test).
> La prueba puede identificar si tu **firewall corporativo o red** está bloqueando el acceso, y proporcionará información para orientar las discusiones con tu equipo de TI.

> **Consejo 3:** **No** uses las aplicaciones de Avatour para iOS o Android para unirte a reuniones. Estas aplicaciones solo son necesarias cuando se **transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar el software Avatour 360° directamente y requieren un smartphone como asistencia.

##### Visitar un Workspace Sin Unirse a una Reunión

Puedes acceder a un Workspace sin unirte a una reunión en vivo de las siguientes formas:

- **Workspace Público:**
  Si el Workspace es público, se puede acceder al enlace directamente — sin necesidad de inicio de sesión.

- **Workspace Restringido:**
  Si el Workspace está restringido, debes ser agregado como **colaborador** con permisos **Editor** o **Viewer**.

  1. Cuando seas agregado como colaborador, recibirás una **notificación por correo electrónico** con un enlace al Workspace.
  2. Haz clic en el enlace del correo electrónico para abrir el Workspace. Si aún no has iniciado sesión, se te pedirá que **inicies sesión o completes el registro**.
  3. Una vez iniciada la sesión, el Workspace se abrirá automáticamente.

  Alternativamente, puedes iniciar sesión en
  https://avatour.live/login
  y acceder al Workspace desde tu **lista de Workspaces**.

#### 3.1.2 Visor VR {#vr-headset}
Puedes unirte a una reunión y visitar un workspace desde una variedad de visores Meta y Pico compatibles. Para hacerlo:

1. Instala nuestra aplicación Avatour desde tu respectiva tienda de aplicaciones VR: [Cómo instalar la aplicación Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carga nuestra aplicación e introduce el código de reunión o selecciona un Workspace para unirte a una reunión. Para más información sobre cómo usar nuestra aplicación VR, consulta nuestro artículo de la Base de Conocimiento [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Herramientas de Colaboración para Reuniones y Workspace {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (sincrónicas):** Colabora en tiempo real con otros participantes, incluyendo visitas en vivo al sitio o revisión de assets grabados juntos.
2. **Workspaces (asincrónicos):** Revisa e interactúa con los assets según tu propio horario, 24/7.

Las **herramientas de colaboración son principalmente similares** entre reuniones y workspaces, con algunas diferencias debido al contexto sincrónico vs asincrónico.

#### 3.2.1 Diseño de la Interfaz

La interfaz de Avatour está organizada en torno a tres áreas principales:

- **Panel izquierdo** – Assets del Workspace y herramientas de apoyo
- **Lienzo central** – Área de visualización principal para video en vivo o assets
- **Panel derecho** – Información contextual, como participantes, reuniones o chat

La mayoría de las interacciones se inician desde el **menú inferior**.
Al hacer clic en una opción del menú se abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **lienzo central** sigue siendo el área de visualización principal.

---
#### 3.2.2 Ejemplo de Vista de Reunión

Aquí hay un ejemplo de una vista en una Reunión de Avatour:

![Avatour Meeting UI with Assets Panel, blank Canvas and Participants Panel](https://res.cloudinary.com/avatour/image/upload/v1772362400/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)
*Reunión de Avatour con Panel de Assets (izquierda), Lienzo (centro) y Panel de Participantes (derecha)*

---

#### 3.2.3 Ejemplo de Vista de Workspace

Aquí hay un ejemplo de una vista de Workspace:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)
*Workspace de Avatour con Panel de Assets (izquierda), Lienzo (centro) y Panel de Reuniones (derecha)*

---

#### 3.2.4 Descripción General del Menú Inferior

El menú inferior proporciona acceso a los principales controles de la interfaz y paneles:

**Menú Inferior de la Reunión**

![Avatour Meeting Bottom Menu](https://res.cloudinary.com/avatour/image/upload/v1772300383/avatour-screenshot-meeting-bottom-menu_bflaor.png)
*Menú Inferior de la Reunión de Avatour*

- **Assets** – Revisa los archivos del workspace, incluyendo videos grabados, imágenes, snapshots y PDFs.
- **Chat** – Envía mensajes a todos los participantes de la reunión.
- **Cámara** – Activa o desactiva tu cámara web.
- **Micrófono** – Silencia o reactiva el audio.
- **Presentar** – Presenta un asset, escritorio o feed de cámara web (ver sección Presentar más abajo).
- **Herramientas del Anfitrión** (solo anfitriones):
  - **Bloquear Foco** – Bloquea la vista para todos los participantes.
  - **Silenciar Todos** – Silencia a todos los participantes.
- **Activar Pantalla Completa** – Hace que la pestaña de la reunión sea a pantalla completa.
- **Salir de la Reunión** – Abandona la reunión.
- **Iniciar Grabación** – Usa este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones pueden grabarse automáticamente si la **grabación automática** está habilitada en la configuración del workspace. En ambos casos, las grabaciones se guardan en los assets del workspace.
- **Mapa** – Abre o cierra el panel del mapa para assets con una pista GPS. Al hacer clic en una ubicación se salta al punto exacto en el video. El mapa se actualiza en tiempo real mientras se reproduce el video.
- **Participantes** – Abre o cierra el panel de participantes.
- **Información de la Reunión** – Ve el código de reunión, el enlace de invitación y accede a tutoriales relacionados.

![Avatour Meeting Info](https://res.cloudinary.com/avatour/image/upload/v1772547439/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)
*Panel Lateral de Información de la Reunión de Avatour*

- **Configuración** – Ajusta los ajustes de idioma, audio y video. Para reuniones de video 360° en vivo, usa **Mostrar Bitrate** para monitorear las estadísticas de conectividad.

> Consejo: Envía el enlace de la reunión o agrégalo a un elemento del calendario para invitar a participantes.

---

##### Menú Presentar

La opción **Presentar** en el menú inferior de la reunión te permite compartir contenido con todos los participantes.

- **Cámara** – Comparte la cámara de tu smartphone/tableta. También puede usarse durante una reunión de video 360° en vivo para superponer una vista secundaria para primeros planos o detalles específicos.
- **Escritorio** – Comparte la pantalla de tu escritorio con todos los participantes.
- **Asset** – Presenta un asset del workspace. Al seleccionar un asset se abre la **barra de herramientas de Asset**, que proporciona controles de reproducción y herramientas de colaboración específicas para el asset que se está presentando.

##### Barra de Herramientas de Asset (Reunión)

Al presentar un asset en una reunión, la **Barra de Herramientas de Asset** aparece sobre el lienzo. Aquí están las herramientas y elementos del menú disponibles cuando se <u>presenta un Asset en una Reunión</u> - explicados de izquierda a derecha.

![Avatour Menu while Presenting an Asset in a Meeting](https://res.cloudinary.com/avatour/image/upload/v1772303706/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour al presentar un Asset en una Reunión*

- **Línea de Tiempo / Barra de Progreso** – Muestra el progreso del video con notas y temas clave extraídos del audio. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.
- **Snapshot** – Captura una imagen 360° o 2D del asset.
- **Spotlight** – Destaca un área específica para todos los participantes durante las sesiones en vivo.
- **Mostrar/Ocultar Punto de Vista (POV)** – Muestra dónde está mirando cada participante en el video 360°.
- **Notas** – Crea notas ancladas a momentos específicos en el asset. Las notas pueden categorizarse (Observación, Problema, Acción, Recomendación), rastrearse por estado (Abierto → En Progreso → Resuelto) y compartirse mediante enlaces directos.

  ![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/v1772374822/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota de Avatour y Filtros de Notas*

  - **Notas por Comandos de Voz** – Son marcadores de posición generados automáticamente cuando la grabación detecta menciones como "insertar nota", "tomar nota" o "hacer una nota". Estas notas aparecen en la línea de tiempo y el usuario debe **posicionarlas y finalizarlas**.

  ![Avatour Notes - Voice Command Generated](https://res.cloudinary.com/avatour/image/upload/v1772921944/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por Comandos de Voz*

- **Panel de Notas y Resumen** – Abre un panel lateral que muestra todas las notas, temas clave y un resumen ejecutivo del asset. Al hacer clic en un elemento se salta a ese momento en el video.

  ![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen Ejecutivo de Avatour al presentar un Asset en una Reunión*

  ![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Temas de Avatour al presentar un Asset en una Reunión*

  Desde el **Panel Lateral**, puedes **imprimir un informe del asset** o **descargarlo como TXT o CSV**. Los informes pueden incluir notas, temas generados por IA y transcripciones completas. También puedes **elegir qué elementos incluir** antes de exportar.

  ![Avatour Asset Report Print Menus](https://res.cloudinary.com/avatour/image/upload/v1773496969/avatour-screenshot-asset-report-print-menus_kn0syn.png)
  *Menús de Impresión / Descarga del Informe de Asset de Avatour*

  ![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/v1772376570/avatour-screenshot-asset-report-element-selection_ud8c5k.png)
  *Menú de Selección de Elementos del Informe de Asset de Avatour*

- **Enlace para Compartir** – Comparte un enlace a una nota específica o escena en el asset.
- **Subtítulos (CC)** – Muestra la transcripción de texto en pantalla durante la reproducción de video.

##### Barra de Herramientas de Asset (Workspace)

Al revisar un asset en un workspace, la barra de herramientas es similar pero optimizada para uso individual:

![Avatour Menu while Presenting an Asset outside a meeting, e.g. when visiting a workspace](https://res.cloudinary.com/avatour/image/upload/v1772303705/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menú de Avatour al presentar un Asset en un Workspace*

- **Línea de Tiempo / Barra de Progreso** – Muestra el progreso del video con notas y temas clave extraídos del audio. Haz clic en cualquier punto de la línea de tiempo para desplazarte por el video. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.
- **Snapshot, Notas, Panel de Notas y Resumen, Enlace para Compartir, Subtítulos**
- No disponibles: **Spotlight, POV** (requieren participantes en vivo)
- Controles adicionales:
  - **Pasos de 10 segundos** – Salta hacia adelante/atrás
  - **Velocidad de Reproducción** – Ajusta la velocidad (0,5×–2×)
  - **Recortar Video** – Recorta el inicio o el final del asset


## 4. Para Usuarios Host y Admin - Consola Web de Avatour {#for-host-and-admin-users-avatour-web-console}

Cuando inicias sesión en tu Cuenta de Usuario de Avatour, accederás a la **Consola Web**.

### 4.1 Consola Web - Descripción General del Menú Principal {#web-console-overview-main-menu}

En el lado izquierdo verás los siguientes elementos del menú:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/v1772366766/avatour-screenshot-main-menu_qwpthq.png) *Consola Web de Avatour - Menú Principal*

- **Workspaces** – Organiza tu contenido de manera eficiente. Cada workspace contiene **Assets**, **Colaboradores**, **Reuniones** y **Configuración**.
- **Assets** – Accede y gestiona todos tus assets (videos, imágenes, PDFs). Los Admins pueden ver todos los assets de la cuenta y los assets compartidos son visibles para todos los usuarios.
- **Perfil** – Gestiona tu idioma y contraseña.
- **Analytics** – Rastrea la actividad de las sesiones, el uso del workspace y las métricas de ROI.
- **Configuración** *(solo Admin)* – Configura los valores predeterminados de workspace, reunión y asset en toda la organización. Los Admins también pueden personalizar la marca (logo, colores, fondos).
- **Cuenta** *(solo Admin)* – Gestiona usuarios registrados y cámaras 360°.
- **Inicio de Sesión de Dispositivo** – Introduce el código que aparece en tu cámara 360° para vincularla con tu cuenta.
- **Tutoriales** – Accede a tutoriales guiados.
- **Cerrar sesión** – Cierra sesión en la consola.

> Las secciones como Perfil, Inicio de Sesión de Dispositivo, Tutoriales y Cerrar sesión son autoexplicativas y no tienen subsecciones detalladas.

---

### 4.2 Consola Web - Detalles por Elemento del Menú (con imágenes)  {#web-console-details-by-menu-item}

#### 4.2.1 Workspaces

Los Workspaces son unidades organizativas flexibles que te permiten gestionar assets, colaboradores y reuniones en un solo lugar. Puedes crear un nuevo workspace con el botón **Nuevo Workspace** en la esquina superior derecha.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/v1772360323/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web de Avatour - Elemento del Menú Principal Workspaces*

Haz clic en el ícono de campana para ver un resumen de la actividad del workspace en los últimos 7 días.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/v1772919758/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Actividades Recientes del Workspace*

Dentro de un workspace:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace con Assets (izquierda), Lienzo (centro), Reuniones (derecha)*

- **Assets** – Gestiona los archivos asignados a este workspace.
- **Colaboradores** –
  Controla el acceso a los workspaces mediante
  - **Viewer** – Puede ver assets. La invitación crea un usuario Guest si es necesario.
  - **Editor** – Control total del workspace, mismos derechos que el Host. La invitación actualiza al usuario a Host si es necesario.
> Múltiples usuarios pueden acceder a un workspace simultáneamente sin una reunión. Los workspaces públicos y la configuración de acceso a reuniones proporcionan acceso alternativo.
- **Informe** – Genera un informe utilizando una plantilla de lista de verificación en los assets del workspace seleccionados.

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/v1772924118/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe del Workspace y Selección de Assets*

- **Mapa** – Muestra las ubicaciones de los assets con GPS habilitado en un mapa.
- **Reuniones** – Organiza reuniones en el workspace.
- **Configuración** – Configura los valores predeterminados del workspace y la reunión:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/v1772387752/avatour-screenshot-workspace-settings_llcei3.png) *Configuración del Workspace*

**Configuración del Workspace**

- **Plantilla de Informe** – Selecciona la plantilla de lista de verificación para informes de IA.
- **Habilitar Notificaciones** – Correos electrónicos de resumen diario para cambios de estado de notas.

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/v1772804314/Screenshot_2026-03-05_140654_bjk0xk.png) *Ejemplo de Notificaciones por Correo Electrónico*

- **Workspace Público** – Cualquier persona con el enlace puede ver los assets directamente.

**Configuración de Reunión**

- **Autenticación requerida** – Los participantes deben iniciar sesión.
- **Permitir acceso de invitado** – Permite que usuarios no registrados vean los assets.
- **Inicio Automático de Grabación / Inicio Manual** – Elige si las reuniones se graban automáticamente o se inician manualmente.
- **Requerir anfitrión** – El anfitrión debe admitir a los participantes; la reunión termina cuando el anfitrión se va.
- **Permitir acceso de espectador** – Únete sin micrófono ni cámara; comunícate mediante chat.
- **Reuniones protegidas con contraseña** – Requiere una contraseña para unirse.
- **Mostrar Pregunta sobre Ahorro de Viaje** – Pregunta a los participantes si la reunión redujo los viajes.

> Los ajustes pueden combinarse (p. ej., no se requiere anfitrión pero protegido con contraseña).

---

#### 4.2.2 Assets

Gestiona todos los videos 360°/2D, imágenes y PDFs. Carga/descarga assets, asígnalos a workspaces, compártelos con otros usuarios, renómbralos, imprime/descarga informes, activa el desenfoque de rostros y la summarización de IA.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/v1772360326/avatour-screenshot-main-menu-assets_ky5emz.png) *Elemento del Menú Principal Assets*

---

#### 4.2.3 Analytics

Proporciona información sobre reuniones, uso del workspace y métricas de ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360315/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Descripción General de Analytics*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360313/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Actividad de Reuniones y Uso del Workspace*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360312/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de Licencias de Dispositivo y ROI*

## 5. En el Sitio - Cómo Usar el Kit Turnkey de Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Primeros Pasos
[Guía de Inicio Rápido – Kit Turnkey de Avatour 3.1 (configuración Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Sigue la guía para desempacar, ensamblar y encender la cámara.

---

### 5.2 Consejos Útiles

#### Batería Externa – Reuniones en Vivo más Largas y Mejor Gestión Térmica

- **Si tu kit incluye una batería Ulanzi:** Adjúntala entre la base del trípode y el palo extensible, luego conecta la batería a la cámara mediante USB-C.

- **Si tu kit incluye un palo de batería Telesin:** Monta la cámara directamente en el palo de batería extensible Telesin y conéctala mediante USB-C.

Usar la batería externa:

1. Extiende la duración total de la batería de ~40 minutos (solo batería de la cámara) a ~3 horas.
2. Agrega estabilidad a la configuración de la cámara.
3. Ayuda a prevenir el posible sobrecalentamiento.

> Recomendamos usar siempre la batería externa desde el principio, especialmente para reuniones en vivo.

#### Consideraciones de Audio para Reuniones en Vivo y Grabaciones

- **Entornos ruidosos:**
  Usa los auriculares Shokz incluidos en tu kit para una captura de audio clara.
  - **Encendido/Apagado:** Mantén presionado el botón "+" durante 3 segundos (LED azul = encendido, LED rojo = apagado).
  - **Modo de Emparejamiento Bluetooth:** Con los auriculares apagados, mantén presionado el botón "+" durante 5 segundos (LED parpadea azul/rojo).
  - **Volumen:** Usa los botones "+" y "-".

- **Entornos más tranquilos / múltiples participantes cerca de la cámara:**
  Usa el altavoz de clip NoxGear. No tiene la misma fidelidad que los altavoces de conferencia (p. ej., Jabra Speak), pero es fácil de enganchar a la camisa y captura las voces cercanas de manera efectiva.
  - **Encendido/Apagado:** Mantén presionado el botón Reproducir/Pausar durante 2 segundos.
  - **Modo de Emparejamiento Bluetooth:** Entra automáticamente en modo de emparejamiento al encenderse (LED parpadea azul/rojo; azul sólido cuando está emparejado).
  - **Volumen:** Usa los botones "+" y "-".

- **Usar tu propio dispositivo:** Si prefieres una alternativa (p. ej., un altavoz de conferencia o auricular personal), puedes emparejarlo a través de la cámara: Configuración → Bluetooth.

#### Conectividad, Conectividad, Conectividad
**Antes de comenzar:** Asegura la conexión a Internet mediante:

- **WiFi local** (preferido)
- **Red Móvil** (si está fuera del alcance del WiFi)

**Ancho de banda recomendado:** 10 Mbps de subida/bajada para transmisión 360° completa (~5 Mbps). El ancho de banda inferior (1–2 Mbps) solo funciona cuando se está quieto.

##### Prueba de Velocidad de Red
- **Prueba en una sola ubicación:** Cualquier verificador de velocidad que uses normalmente (p. ej., [Speedtest](https://www.speedtest.net)) para verificar el ancho de banda de subida.
- **Prueba caminando por el sitio:** Desde la cámara: Configuración → Red → Prueba de Conexión. Camina por todo el espacio para confirmar la cobertura y el ancho de banda.

##### WiFi Local
- Muy recomendado para conexiones estables.
- Si TI requiere inclusión en lista blanca, encuentra la dirección MAC: Configuración → Acerca de → Dirección WiFi.

##### Red Móvil

**Opción A: Hotspot y SIM proporcionados con el kit**
- Adjunta el hotspot GlocalMe al palo de batería Telesin (imán).
- Garantiza sin interferencias y mantiene la conexión si se aleja de la cámara.
- Solución de problemas:
  - Confirma la SIM preinstalada (no Cloud SIM).
  - Habilita 5G en el Administrador de Tarjetas SIM.
  - Verifica el APN correcto para tu región ([guía de configuración APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opción B: Hotspot personal / SIM**
- Usa tu propio smartphone o hotspot dedicado.

**Nota Importante:**
> Mantén el hotspot apagado mientras estés conectado al WiFi; actívalo solo cuando estés fuera del alcance. El sistema operativo de la cámara cambia dinámicamente entre redes WiFi según la intensidad de la señal y puede cambiar involuntariamente al hotspot incluso cuando el WiFi está disponible.

> Las redes móviles pueden limitar el ancho de banda de forma inesperada. Consulta con tu operador sobre los límites del plan de datos, o contacta con el soporte de Avatour si usas nuestro hotspot y SIM.

##### Situaciones de Bajo Ancho de Banda
- Pregrabar videos de ubicaciones para reproducción posterior ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Compartir un stream de cámara de smartphone para complementar áreas de bajo ancho de banda (0,1–0,3 Mbps de subida).

##### Sin Conectividad
- Solo se pueden usar videos pregrabados ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Otros Participantes en el Sitio – Mejores Prácticas

Cuando múltiples participantes se unen a una reunión en vivo de Avatour desde la misma ubicación que la cámara 360°, es crucial gestionar cuidadosamente el **audio y el ancho de banda**:

- Cada smartphone, tableta o portátil conectado en el sitio consume ancho de banda de red y puede afectar negativamente al feed de la cámara 360°.
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo que la experiencia de la reunión sea desagradable para todos los participantes.

Para abordar estos desafíos, sigue estas **mejores prácticas**:

- **Usa auriculares con cable o inalámbricos:** Preferiblemente con cancelación de ruido para prevenir eco y retroalimentación.
- **Modo En el Sitio:** Únete a la reunión en modo En el Sitio cuando estés físicamente presente cerca de la cámara 360°.
  - Este modo está optimizado para uso en el sitio:
    - Silencia el micrófono y el altavoz del participante por defecto.
    - **No** envía el feed de la cámara del participante.
    - **No** muestra el feed de la cámara 360° en el navegador del participante.
    - Conserva el ancho de banda de red, asegurando que la cámara 360° tenga la máxima subida disponible para la transmisión en vivo.
    - Útil cuando un usuario quiere compartir detalles específicos; **puedes compartir tu cámara** para vistas específicas.
- **Silenciar cuando no se está hablando activamente:** Previene retroalimentación de audio no deseada y distracciones.
- **Usar una red separada si es posible:** Tener el smartphone conectado a una red diferente a la de la cámara para reducir interferencias.

Seguir estas pautas garantiza un tour en vivo fluido y de alta calidad tanto para los participantes en el sitio como para los remotos.

### 5.3 App de Cámara de Avatour

Aquí están los menús (1) Nivel Superior, (2) Configuración y (3) Configuración de Red.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/v1772918698/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App de Cámara 360° de Avatour - 3 Menús*

**Quick Capture** - Para grabación de video 360° sin conexión. - Para una descripción detallada consulta [¿Cómo grabar y subir videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Recomendamos usar un dispositivo de audio externo (conectado mediante bluetooth). N.B. También puedes hacer videos 2D estándar e imágenes - simplemente cambia el modo entre 360° y 2D en la esquina inferior derecha una vez en la pantalla QC.

**Reunión en Vivo** - Para Videoconferencia en vivo 360°. Verás tus workspaces y al hacer clic en uno se iniciará el streaming de video en vivo desde la cámara 360°. Antes de poder unirte a la reunión con tu cámara 360° necesitas conectar un dispositivo de audio mediante bluetooth. Para una descripción detallada consulta [¿Cómo iniciar una reunión Live Capture con tu cámara Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Al organizar una reunión Live Capture con tu cámara 360°, tendrás herramientas de reunión similares disponibles que reflejan la experiencia web. Aquí hay un enlace a nuestro artículo de la Base de Conocimiento que explica estas herramientas con más detalle: [Herramientas de la App de Operador](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galería** - Encuentra aquí todos tus videos e imágenes 360° para subir a la Consola Web de Avatour.

**Configuración** - Dentro de Configuración, tienes las siguientes opciones:

- **Red**: Esta opción te permite cambiar a qué red WiFi está conectada la cámara o ejecutar una prueba de conexión de red para ver el rendimiento de streaming
- **Live Capture**: Ajusta la configuración de Live Capture según el ancho de banda disponible, la sensibilidad VR de los invitados o si las lentes protectoras de tu cámara están instaladas:
  - **Frame Rate objetivo**: Ajusta la velocidad de fotogramas para tu video Live Capture entre 15 fps, 24 fps y 30 fps. Las velocidades de fotogramas más altas producen un video más fluido, pero requerirán más ancho de banda de subida. Predeterminado: 15 fps
  - **Bitrate objetivo**: Te permite aumentar o disminuir el bitrate máximo de streaming para tu Live Capture. Puedes establecer tu bitrate objetivo entre 1 Mbps y 10 Mbps. Los bitrates más altos darán como resultado una mayor resolución de video, pero requerirán más ancho de banda de subida. Predeterminado: 5 Mbps
  - **Optimizar Movimiento**: Esto disminuirá la velocidad de fotogramas del video, generando menos carga en el ancho de banda de subida de tu red, y aumentará tu bitrate de streaming. Además, esta opción ayuda a reducir el mareo para los participantes de VR. Predeterminado: Desactivado
  - **Lentes Protectoras**: Esto afectará cómo se une el video 360° dependiendo de si se han instalado lentes protectoras en tu cámara. Si no tienes lentes protectoras, configúralo en "No". Si recibiste un Kit 3.0, tienes lentes protectoras preinstaladas y deberías configurarlo en "Sí". Predeterminado: Sí

- **Quick Capture**: Ajusta la configuración de Quick Capture según tu velocidad de fotogramas de video preferida, el ancho de banda disponible para subidas de videos grabados o si las lentes protectoras de tu cámara están instaladas. Quick Capture tiene una resolución fija de 4k que generalmente logra un buen equilibrio entre la calidad del video y el tamaño del archivo. (Para resoluciones más altas puedes usar las aplicaciones nativas de la cámara, también en el PanoX V2, para más detalles consulta [¿Cómo grabar y subir videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Frame Rate objetivo**: Ajusta la velocidad de fotogramas para las grabaciones de video Quick Capture entre 15 fps, 24 fps y 30 fps. Las velocidades de fotogramas más altas producen un video más fluido, pero aumentarán el tamaño del archivo de video y el tiempo de subida. Recomendado: 30 fps
  - **Bitrate objetivo**: Establece el bitrate objetivo para las subidas de Quick Capture entre 5 Mbps y 20 Mbps. Los bitrates más bajos aumentan las velocidades de subida, pero disminuirán la calidad del video. Recomendado: 20 Mbps
  - **Lentes Protectoras**: *Ver la sección de Lentes Protectoras para Live Capture arriba*
- **Acerca de**: Ver el número de serie del dispositivo y la versión del software

**Cuenta** - Para iniciar sesión con tu cuenta de host o admin de Avatour.

## 6. Consejos de Mejores Prácticas {#best-practice-advice}

### 6.1 Primeros Usos (Informales) y Familiarización

Para tus primeros usos y para familiarizarte con la Consola Web de Avatour y el Kit Turnkey de Avatour recomendamos los siguientes pasos:

1. Lleva el kit a casa y juega con él con familiares y amigos usando tu conexión a Internet doméstica.
2. Lleva el kit a la oficina y conéctate a una red corporativa (pueden surgir problemas corporativos, p. ej. firewalls corporativos - pero sabes desde el paso uno que Avatour funciona y este es un tema a resolver por tu equipo de TI con la ayuda de Avatour).
3. Empieza a usar Avatour en el sitio (fuera de tu oficina) en la ubicación de la reunión a la que los participantes remotos normalmente tendrían que viajar. Pueden surgir más temas de conectividad. Avatour ayudará en cooperación con tu equipo de TI.
4. Empieza a usar con participantes remotos internos y externos.

### 6.2 Antes de una Reunión en Vivo con Video 360°

- Recomendamos hacer un tour de video 360° grabado antes de cualquier tour en vivo si el tiempo lo permite por tres razones: (1) Tener una solución de respaldo para el tour en vivo, (2) tener algo para documentación y revisión posterior (además del tour en vivo grabado) y (3) empezar a crear una biblioteca de videos 360° de todos tus sitios que puede ser útil para muchos casos de uso.
- Todos los componentes del kit cargados durante al menos 90 minutos antes de la reunión en vivo. De todas formas recomendamos tener todos los dispositivos en carga continua cuando no estén en uso. Así todos los dispositivos estarán siempre listos, también para reuniones ad hoc no planificadas.
- Tener el kit completamente ensamblado (1. base del trípode + 2. batería Ulanzi + 3. palo extensible + 4. cámara 360°).

- Confirmar que se ha creado un Workspace para organizar una reunión en vivo e incluir todos los Assets relevantes.

- Invitar a todos los participantes a la reunión a través de tu Workspace. Esto crea una invitación en los calendarios de todos los participantes, e incluye el enlace de invitación a la reunión.

- Emparejar y conectar tus auriculares bluetooth o altavoz que planeas usar para tu tour a la cámara.

- Todos los usuarios de smartphones en el sitio deben conectarse desde una red diferente a la de la cámara. Esto reducirá la carga en el ancho de banda de red de la cámara.

- Si estás solo como operador de cámara, lleva un smartphone contigo en caso de que quieras compartir la cámara del smartphone y mostrar detalles finos.

- Confirmar que la cámara 360° puede conectarse a tu WiFi local.

- Antes de una reunión de Avatour, planifica la ruta que tomarás por las instalaciones. Haz una reunión de prueba de Avatour con la cámara y comprueba que todas las áreas tengan bitrates superiores a 1 Mbps de ancho de banda. Esto puede verse en la pantalla de la cámara misma, o como participante remoto yendo a Configuración y activando Mostrar Bitrate.

- Si notas que algunas áreas tienen poco o ningún ancho de banda, es mejor tomar imágenes o hacer una grabación. Estas pueden presentarse durante la reunión para que los participantes remotos las revisen. Puedes seguir la guía aquí que explica nuestro Quick Capture para grabar y subir videos/imágenes: [¿Cómo grabar y subir videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si tienes participantes remotos uniéndose a la reunión que no han usado Avatour antes, proporciónales un breve resumen de la plataforma, su funcionalidad (video en vivo 360°, assets, snapshots, anotaciones, spotlight) y las herramientas de la reunión.

- Puedes empezar en otra solución de videoconferencia (p. ej. Teams, Zoom, Google Meet) pero antes de pasar a Avatour, cierra completamente la otra aplicación de videoconferencia. En algunos casos, estas otras aplicaciones priorizarán el micrófono/altavoces/cámara web de tu dispositivo, causando que se deshabiliten para Avatour. Además, NO ejecutes Avatour Y otra videoconferencia al mismo tiempo ya que esto reducirá el ancho de banda disponible.

- Si planeas usar la cámara 360° en un entorno de alta temperatura, se recomienda usar el módulo de enfriamiento (solo Pilot Pano). Esto ayudará a reducir las posibilidades de que la cámara se sobrecaliente y se apague automáticamente.

### 6.3 Durante la Operación de la Cámara en el Sitio para una Reunión en Vivo con Video 360°

- Al operar la cámara, asegúrate de caminar lentamente. Esto ayuda con la calidad del video y reduce cualquier posible tiempo de inactividad del video cuando la conexión de red de la cámara cambia entre puntos de acceso WiFi.

- Mantén la cámara frente a ti y por encima del nivel de los ojos. Esto permite que todos los participantes remotos vean la mayor parte del área circundante.

- Para los casos en que la cámara necesita permanecer estable, usa el trípode y extiende la cámara a la altura correcta, preferiblemente al nivel de los ojos.

- Conecta siempre la cámara a tu red WiFi local cuando sea posible. Para áreas sin acceso WiFi, usa el hotspot proporcionado. El hotspot tiene una tarjeta SIM que se conectará a una red celular confiable cerca de ti. Mantén siempre el hotspot apagado cuando no esté en uso en interiores ya que de lo contrario la cámara 360° podría conectarse al hotspot lo cual no queremos en interiores. Cuando estés en exteriores, mantén el hotspot cerca de la cámara 360°.

- Cuando el bitrate en la cámara empieza a caer por debajo de 2 Mbps, camina más lento o detente completamente hasta que la señal se estabilice nuevamente. Esto suele ocurrir cuando cambias de un Punto de Acceso WiFi a otro.

- Si sabes que la conectividad y el video caerán al moverte a una ubicación específica (Ejemplo: moviéndote de un área de producción interior a un área exterior), informa a los participantes remotos con anticipación.

- Si necesitas mostrar algo con mucho detalle o letra pequeña, usa tu smartphone o el de un participante en el sitio para unirse a la reunión y presentar la cámara (trasera) del teléfono.

- Si es posible recomendamos que una persona adicional esté en el sitio para ayudar con la compartición de cámara del smartphone descrita anteriormente ya que a menudo resulta ser útil/necesaria.

- Idealmente los usuarios de smartphones en el sitio deben unirse a la reunión (1) en modo en el sitio y (2) en una red diferente a la que usa la cámara para no quitarle ancho de banda de subida crucial a la cámara 360°.

- Todos los participantes en el sitio que se unan desde su smartphone deben estar silenciados, a menos que estén hablando activamente.
