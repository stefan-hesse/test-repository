# Guía del Usuario y Mejores Prácticas de Avatour

## 1. Para Todos los Usuarios de Avatour {#for-all-avatour-users}

Si eres nuevo en Avatour, los siguientes recursos proporcionan una útil introducción a la plataforma y sus capacidades:

1. [Video "Cómo Funciona Avatour"](https://avatour.com/how-it-works) 
   Una breve descripción general de las principales características de Avatour y cómo la plataforma permite la colaboración remota inmersiva.
2. [Preguntas Frecuentes](https://avatour.com/faqs) 
   Respuestas a preguntas frecuentes
3. [Glosario](https://avatour.com/glossary) 
   Definiciones de los principales términos y conceptos de Avatour.
4. Sitio Web
   Echa un vistazo a la página de [Características de Avatour](https://avatour.com/features) junto con las secciones dedicadas a Casos de Uso e Industrias para aprender cómo Avatour puede apoyar tus necesidades específicas.

## 2. Tipos de Usuarios de Avatour

### 2.1 Asistentes a la Reunión (Sin Cuenta Requerida)
Los usuarios pueden unirse a la reunión sin registrarse en una cuenta de Avatour.
Excepción: Si el anfitrión ha restringido la reunión a usuarios registrados — por ejemplo, para permitir que solo los empleados internos se unan mediante Single Sign-On (SSO) — la invitación del calendario indicará que los participantes deben iniciar sesión para autenticarse.

Los usuarios acceden a la reunión de la siguiente manera:
- Reciben una invitación del calendario del anfitrión.
- Usan el enlace de la reunión en la invitación para unirse.
- Ingresan una contraseña de reunión si el anfitrión ha habilitado una.
- Los participantes pueden unirse sin una cuenta de Avatour a menos que la reunión esté restringida y requiera inicio de sesión para autenticarse.

#### 2.1.1 Participante 

- Puede unirse e interactuar completamente (cámara web, micrófono, chat y funcionalidad Presentar).
- Máximo de 20 participantes interactivos por reunión.

#### 2.1.2 Espectador

- Puede ver la reunión y participar solo a través del chat.
- No puede compartir video, usar micrófono, presentar, reproducir/pausar Assets o capturar Snapshots.
- Máximo de 10 Espectadores por reunión.
- Junto con los Participantes, una reunión puede albergar hasta 30 asistentes.

## 2.2 Usuarios Registrados

Los Usuarios Registrados tienen una cuenta de Avatour. Las cuentas se crean de una de las siguientes maneras:

- **Invitado por Admin:** Durante la incorporación, Avatour configura un **tenant dedicado** para la organización y crea una o más **cuentas Admin**. Los Admins pueden entonces **invitar usuarios** dentro de la organización y asignarlos a **grupos**, que definen su rol en la plataforma (Guest, Host o Admin). Los usuarios invitados reciben un **enlace de registro** para completar la configuración de la cuenta y establecer una contraseña.  
- **Invitado por Host:** Los Hosts pueden agregar usuarios como **colaboradores Editor** a un Workspace. Esto consume una **licencia Host** y garantiza al usuario acceso de nivel Host.  
- **Aprovisionamiento automático SSO (solo nivel Enterprise/Business):** Las cuentas pueden crearse automáticamente por el IdP. De forma predeterminada, las cuentas aprovisionadas por SSO se agregan al **grupo Guest**, a menos que se anulen mediante **mapeos de grupo SAML**. Los Admins aún pueden invitar usuarios y asignar membresía de grupo directamente incluso cuando SSO está habilitado.

**Resumen:**  

Los usuarios registrados y su membresía de grupo pueden gestionarse de múltiples maneras:

- **Gestión Admin:** Un Admin en la consola de Avatour puede crear usuarios y asignarlos a grupos, que definen su rol en la plataforma (Guest, Host o Admin).  
- **Aprovisionamiento SSO:** Para clientes de nivel Enterprise o Business con SSO habilitado, el IdP puede aprovisionar automáticamente cuentas y asignar membresía de grupo, que define el rol del usuario en la plataforma.  
- **Usuarios invitados por Host:** Los Hosts pueden invitar a otros usuarios como colaboradores Editor a Workspaces específicos. Asignar el rol de colaborador Editor consume una licencia Host.

**Mejor Práctica Recomendada (Clientes Enterprise):**  
Para organizaciones que esperan un gran número de usuarios que necesitan acceso a Avatour, se recomienda **integrar el Single Sign-On (SSO)** y gestionar usuarios y membresías de grupo desde el **IdP**. Este enfoque agiliza el aprovisionamiento de cuentas, la asignación de grupos y la gestión de licencias, reduciendo la carga administrativa y garantizando un control de acceso coherente.

---

### 2.2.1 Usuarios Guest

- Agregados al **grupo Guest**.  
- Pueden **ver Assets** en Workspaces donde han sido agregados como **colaboradores Viewer**.  
- No pueden crear workspaces, organizar reuniones ni cargar contenido.  
- Las cuentas Guest aprovisionadas por SSO **se autentican a través del IdP**; no se requiere una contraseña gestionada por Avatour.

---

### 2.2.2 Usuarios con Licencia (Acceso a la Consola Web)

#### Usuarios Host (Grupo: Host)

- Pueden crear/gestionar Workspaces, invitar colaboradores a un workspace, **organizar reuniones en vivo**, cargar **Quick Captures**.  
- Tienen acceso al **Panel de Host** y a la **App de Operador** en cámaras 360° compatibles.  

#### Usuarios Admin (Grupo: Admin)

- Incluye todas las capacidades de Host más la administración completa de la cuenta.

**Los privilegios adicionales de Admin incluyen:**

**Gestión de Cuenta**  
- Crear nuevos usuarios y asignarlos a grupos.
- Restablecer contraseñas cuando son gestionadas por Avatour (no aplicable cuando SSO está habilitado). 
- Actualizar usuarios Guest a Host.  
- Desactivar usuarios (las cuentas Admin deben primero convertirse a Host antes de la eliminación).  
- Transferir assets de un usuario Host a otro durante la eliminación.

**Configuración**  
- Configurar los **ajustes de seguridad a nivel de organización** para assets, workspaces y reuniones alojadas en la plataforma (por ejemplo, si un Host debe estar presente para iniciar una reunión, si los rostros deben difuminarse en todos los videos cargados en la plataforma).  
- Habilitar o deshabilitar las **funciones de IA** o la **grabación**.  
- Aplicar la marca corporativa de manera coherente en toda la plataforma si se configura un **dominio personalizado**.

**Assets y Analytics**  
- Ver todos los Assets cargados por cualquier usuario en la organización.  
- Revisar el uso de la plataforma en toda la organización.

---

### 2.2.3 Permisos de Colaboradores del Workspace

Los permisos del Workspace definen lo que un usuario puede hacer **dentro de un Workspace específico**. Estos son independientes de la membresía de grupo a nivel de plataforma (Guest, Host, Admin).

- **Colaborador Editor:** Los usuarios con este permiso pueden:
  - Gestionar Assets (cargar, eliminar, difuminar rostros, generar resúmenes)  
  - Gestionar configuraciones de reunión (habilitar/deshabilitar grabación, permitir o eliminar participantes)  
  - Programar y organizar reuniones en vivo  
  - Generar informes basados en plantillas predefinidas  
  - Agregar o eliminar colaboradores del Workspace  

- **Colaborador Viewer:** Los usuarios con este permiso tienen acceso de solo lectura a los Assets del Workspace. **No pueden modificar Assets, gestionar reuniones ni gestionar colaboradores**, pero **pueden crear Notas en Assets**. 
  
## 3. Para Participantes de Reuniones Remotas y Visitantes del Workspace {#for-remote-meeting-participants-and-workspace-visitors}

Avatour permite a los usuarios colaborar de dos formas principales:

- **Unirse a una reunión en vivo:**  
  Puede que recibas una **invitación del calendario** para unirte a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota al sitio en vivo** o revisar assets juntos de forma sincrónica.

- **Visitar un Workspace:**  
  También puedes ser invitado como **colaborador a un Workspace** para revisar assets **de forma asincrónica** (según tu propio horario).

### 3.1 Cómo Unirse a una Reunión de Avatour y Visitar un Workspace de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### Cualquier Dispositivo de "Pantalla Plana" con un Navegador Web {#any-flat-screen}
Puedes unirte a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, smartphone o tablet** usando un navegador web.  

> **Nota:** Unirse a una reunión de Avatour requiere que **concedas permisos de micrófono**. Por favor, acepta cualquier solicitud de permiso de tu navegador.

1. **A través de invitación del calendario (recomendado):**  
   - Normalmente recibirás una **invitación del calendario** con un **enlace directo para unirte** (por ejemplo: `https://avatour.live/join?s=xxxxx`).  
   - Al hacer clic en el enlace se completará automáticamente el **código de reunión de 5 caracteres** y te llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que necesitas **iniciar sesión para acceder a la reunión**.  
   - **Reuniones protegidas con contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debes ingresar para unirte.

2. **A través del código de reunión:**  
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, ve a [https://avatour.live/join](https://avatour.live/join), ingresa tu **nombre** y el **código de reunión** y únete a la reunión.  
   - Si la reunión está **protegida con contraseña**, ingresa la contraseña proporcionada por el anfitrión.  
   - Si la reunión requiere **autenticación**, necesitarás **iniciar sesión con tu cuenta de Avatour** antes de unirte.

> **Consejo 1:** Si tu cámara o micrófono no funciona, puede que esté siendo utilizado por otra aplicación (por ejemplo, Microsoft Teams o Zoom). Cierra cualquier aplicación que pueda estar usando tu cámara o micrófono, luego sal y vuelve a unirte a la reunión de Avatour.  

> **Consejo 2:** Si aún no puedes unirte a la reunión, ejecuta esta prueba: [https://avatour.live/test](https://avatour.live/test).  
> La prueba puede identificar si tu **firewall corporativo o red** está bloqueando el acceso y proporcionará información para guiar las conversaciones con tu equipo de TI.  

> **Consejo 3:** **No** uses las apps de Avatour para iOS o Android para unirte a reuniones. Estas apps solo son necesarias cuando se **transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar directamente el software Avatour 360° y requieren un smartphone como asistencia.

### Visitar un Workspace Sin Unirse a una Reunión

Puedes acceder a un Workspace sin unirte a una reunión en vivo de las siguientes maneras:

- **Workspace Público:**  
  Si el Workspace es público, se puede acceder al enlace directamente, sin necesidad de inicio de sesión.

- **Workspace Restringido:**  
  Si el Workspace está restringido, debes ser agregado como **colaborador** con permisos **Editor** o **Viewer**.

  1. Cuando seas agregado como colaborador, recibirás una **notificación por correo electrónico** con un enlace al Workspace.
  2. Haz clic en el enlace del correo electrónico para abrir el Workspace. Si aún no has iniciado sesión, se te pedirá que **inicies sesión o completes el registro**.
  3. Una vez que hayas iniciado sesión, el Workspace se abrirá automáticamente.

  Alternativamente, puedes iniciar sesión en  
  https://avatour.live/login  
  y acceder al Workspace desde tu **lista de Workspaces**.

#### Visor VR {#vr-headset}
Puedes unirte a una reunión y visitar un workspace desde una variedad de auriculares Meta y Pico compatibles. Para hacerlo: 

1. Instala nuestra app de Avatour desde la tienda de apps VR correspondiente: [Cómo instalar la app VR de Avatour](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Carga nuestra app e ingresa el código de reunión o selecciona un Workspace para unirte a una reunión. Para más información sobre cómo usar nuestra app VR, consulta nuestro artículo de la Base de Conocimiento [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Herramientas de Colaboración para Reuniones y Workspace {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (sincrónicas):** Colabora en tiempo real con otros participantes, incluidas visitas al sitio en vivo o revisión de assets grabados juntos.  
2. **Workspaces (asincrónicos):** Revisa e interactúa con los assets según tu propio horario, 24/7.

Las **herramientas de colaboración son en su mayoría similares** entre reuniones y workspaces, con algunas diferencias debido al contexto sincrónico vs asincrónico.

### 3.2.1 Diseño de la Interfaz

La interfaz de Avatour está organizada alrededor de tres áreas principales:

- **Panel izquierdo** – Assets del Workspace y herramientas de apoyo  
- **Canvas central** – Área de visualización principal para video en vivo o assets  
- **Panel derecho** – Información contextual, como participantes, reuniones o chat  

La mayoría de las interacciones se inician desde el **menú inferior**.  
Al hacer clic en una opción del menú se abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **canvas central** permanece como el área de visualización principal.

---
### 3.2.2 Ejemplo de Vista de Reunión

Aquí hay un ejemplo de vista en una Reunión de Avatour:

![Avatour Meeting UI with Assets Panel, blank Canvas and Participants Panel](https://res.cloudinary.com/avatour/image/upload/v1772362400/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Reunión de Avatour con Panel de Assets (izquierda), Canvas (centro) y Panel de Participantes (derecha)*

---

### 3.2.3 Ejemplo de Vista de Workspace

Aquí hay un ejemplo de vista de Workspace:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Workspace de Avatour con Panel de Assets (izquierda), Canvas (centro) y Panel de Reuniones (derecha)*

---

### 3.2.4 Descripción General del Menú Inferior

El menú inferior proporciona acceso a los principales controles de la interfaz y paneles:

**Menú Inferior de la Reunión**  

![Avatour Meeting Bottom Menu](https://res.cloudinary.com/avatour/image/upload/v1772300383/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menú Inferior de la Reunión de Avatour*

- **Assets** – Revisa los archivos del workspace, incluidos videos grabados, imágenes, snapshots y PDFs. 
- **Chat** – Envía mensajes a todos los participantes de la reunión.  
- **Cámara** – Enciende o apaga tu cámara web.  
- **Micrófono** – Silenciate o reactiva tu micrófono.  
- **Presentar** – Presenta un asset, escritorio o feed de cámara web (ver sección Presentar a continuación).  
- **Herramientas de Host** (solo anfitriones):  
  - **Bloquear Enfoque** – Bloquea la vista para todos los participantes.  
  - **Silenciar Todos** – Silencia a todos los participantes.  
- **Activar Pantalla Completa** – Pone la pestaña de reunión en pantalla completa.  
- **Salir de la Reunión** – Abandona la reunión.  
- **Iniciar Grabación** – Usa este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones pueden grabarse automáticamente si la **grabación automática** está habilitada en la configuración del workspace. En ambos casos, las grabaciones se guardan en los assets del workspace.
- **Mapa** – Abre o cierra el panel del mapa para assets con una pista GPS. Al hacer clic en una ubicación se salta al punto exacto en el video. El mapa se actualiza en vivo mientras se reproduce el video.
- **Participantes** – Abre o cierra el panel de participantes.  
- **Info de Reunión** – Ve el código de reunión, el enlace de invitación y accede a tutoriales relacionados.  

![Avatour Meeting Info](https://res.cloudinary.com/avatour/image/upload/v1772547439/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panel Lateral de Información de Reunión de Avatour*

- **Configuración** – Ajusta la configuración de idioma, audio y video. Para reuniones de video en vivo 360°, usa **Mostrar Bitrate** para monitorear estadísticas de conectividad.

> Consejo: Envía el enlace de la reunión o agrégalo a un elemento del calendario para invitar a los participantes.

---

**Menú Presentar**

**Cámara** - Te permite compartir tu cámara web o la cámara de tu smartphone/tablet. También se puede usar como Video-dentro-de-Video mientras se presenta un asset o en una reunión de video en vivo 360°, por ejemplo para mostrar un detalle en el sitio (aunque acercarse con la cámara 360° también proporciona una buena vista detallada, por ejemplo de un código de barras, letras pequeñas en una etiqueta).

**Escritorio** - Te permite compartir la pantalla de tu escritorio

**Asset** - Muestra uno de los assets de la sección de assets - ver arriba. Mientras se presenta un asset aparecerá el menú Asset - ver siguiente punto.



**Menú Presentar Asset** 

Hay ligeras diferencias en los elementos del Menú cuando se presenta un Asset en una <u>Reunión</u> y cuando se presenta en un <u>Workspace</u> (asincrónico).

Aquí están las herramientas y elementos del menú disponibles cuando se <u>presenta un Asset en una Reunión</u> - explicados de izquierda a derecha.

![Avatour Menu while Presenting an Asset in a Meeting](https://res.cloudinary.com/avatour/image/upload/v1772303706/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour al presentar un Asset en una Reunión*

**Snapshot** - Toma una foto 360° o 2D dentro de una Live Capture o un Asset presentado. Todos los snapshots pueden guardarse en los Assets de la reunión/workspace. Un snapshot 360° SuperFreeze tiene una resolución más alta (aprox. 6k) y pausará el stream en vivo por unos segundos.

**Spotlight** - Disponible durante una live capture 360 o si se está presentando un Asset. Esto crea un puntero visible para todos los participantes de la reunión y el operador de la cámara, permitiendo llamar la atención del grupo a un objeto o área específica en pantalla.

**Mostrar/Ocultar Punto de Vista (POV)** - Esta opción muestra el enfoque de cada participante - Punto de Vista - en el video 360° - grabado o en vivo (círculos con el nombre del participante debajo)

**Notas** - crea notas (= cuadros de diálogo) en ciertas posiciones en snapshots y videos grabados. Cualquier participante de la reunión puede crear una nota. Solo el creador de la nota puede editar y eliminar una nota. Al crear una nota, puedes establecer un Tipo: Observación, Problema, Acción o Recomendación (los últimos tres solo pueden ser realizados por Hosts, Viewers y Editores Colaboradores de Avatour). 

![Avatour Note and Notes Filter](https://res.cloudinary.com/avatour/image/upload/v1772374822/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota de Avatour y Filtros de Notas*

Esto aclara si una nota es informativa o requiere seguimiento. En la línea de tiempo de un video las notas están ancladas al momento preciso en la captura.

Los colaboradores principales (Host, Viewers y Editores Colaboradores de Avatour) pueden actualizar el Estado de una nota a medida que avanza el trabajo: Abierto → En Progreso → Resuelto.

Puedes compartir un enlace que lleva directamente a la nota. Copia el enlace y úsalo/incrústalo donde quieras.

<u>Notas Generadas por Comandos de Voz</u> - Ahora también es posible generar notas a través de comandos de voz (por ejemplo, diciendo "tomar nota") desde una pista de audio en cualquier video (en vivo/grabado, 360°/2D). Los marcadores de posición se muestran en la línea de tiempo del video y la posición de la nota puede arrastrarse en el video a la posición exacta y por supuesto también editarse con más contenido.

![Avatour Notes - Voice Command Generated](https://res.cloudinary.com/avatour/image/upload/v1772921944/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por Comandos de Voz*

**Panel Lateral con Notas, Resumen Ejecutivo, Temas, etc. e Informes** - muestra todas las notas y temas de un asset en un panel lateral (haz clic en el icono de lista junto al icono de nota en el menú anterior). Haz clic en el panel lateral en las notas/temas para ir a la nota/tema en el video. En el panel de Notas puedes aplicar filtros de Notas.

![Avatour Asset Executive Summary](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen Ejecutivo de Avatour al presentar un Asset en una Reunión*

Los Temas también están resaltados bajo la línea de tiempo del video. Los Temas son generados por IA basándose en el audio de un asset y pueden iniciarse durante la Carga desde la app de cámara de Avatour o en la sección de Assets en la Consola Web.

![Avatour Topics](https://res.cloudinary.com/avatour/image/upload/v1772377209/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Temas de Avatour al presentar un Asset en una Reunión*

También puedes imprimir un informe del asset - o descargarlo como archivo TXT/CSV...

![Avatour Asset Report Print Menus](https://res.cloudinary.com/avatour/image/upload/v1773496969/avatour-screenshot-asset-report-print-menus_kn0syn.png) *Menús de Impresión/Descarga de Informes de Assets de Avatour*

...con todas las notas, temas, etc. incluso una transcripción completa para un asset y selecciona qué incluir:

![Avatour Print Asset Report Element Selection](https://res.cloudinary.com/avatour/image/upload/v1772376570/avatour-screenshot-asset-report-element-selection_ud8c5k.png) *Menú de Selección de Elementos del Informe de Asset de Avatour*

**Enlace para Compartir** - Comparte enlaces a notas y escenas específicas (=ángulos de visión) en un video/snapshot ya sea por correo electrónico o copia directamente el enlace y úsalo/incrústalo donde quieras.

**Subtítulos (CC)** - Aquí puedes activar para mostrar transcripciones de texto en pantalla mientras se presenta un video.



Y aquí están las herramientas de colaboración y elementos del menú disponibles cuando se presenta un Asset en un <u>Workspace</u>. La mayoría de las herramientas son como en una reunión, pero algunas faltan ya que solo tienen sentido cuando otros están presentes (POV y Spotlight) y algunas solo están disponibles en workspaces - principalmente relacionadas con operaciones de video, que se explican a continuación.

![Avatour Menu while Presenting an Asset outside a meeting, e.g. when visiting a workspace](https://res.cloudinary.com/avatour/image/upload/v1772303705/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menú de Avatour al presentar un Asset en un Workspace*

**Pasos de 10 segundos** - Avanza o retrocede en el video en pasos de 10 segundos.

**Velocidad de Reproducción** - Aquí puedes elegir un factor de velocidad de reproducción (0.5-2)

**Recorte de video (tijeras)** - Con las tijeras puedes recortar un video al principio y al final.



## 4. Para Usuarios Host y Admin - Consola Web de Avatour{#for-registered-users}

Cuando inicias sesión en tu Cuenta de Usuario de Avatour accederás a la Consola Web. 

### 4.1 Consola Web - Descripción General del Menú Principal

En el lado izquierdo verás los siguientes elementos del menú.

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/v1772366766/avatour-screenshot-main-menu_qwpthq.png) *Consola Web de Avatour - Menú Principal*

**Workspaces** - Los Workspaces pueden configurarse para muchos propósitos (por ejemplo, sitios, proyectos, clientes, proveedores) y son unidades organizativas que te ayudan a trabajar eficientemente en un entorno controlado que comprende los siguientes elementos.

**Assets** - Todos tus assets (videos, imágenes, pdfs) en un solo lugar bajo <u>Mis Assets</u>. Los usuarios Admin pueden ver todos los <u>Assets de la Cuenta</u> de todos los usuarios host. Los <u>Assets Compartidos</u> son aquellos que los hosts comparten con todos los demás usuarios en la plataforma de Avatour. Aquí puedes renombrar assets, activar el desenfoque de rostros y generar temas.

**Perfil** - Gestiona tu idioma y restablece tu contraseña.

**Analytics** - Obtén información sobre sesiones y uso

**Configuración** - Solo para Usuarios Admin. Gestiona algunas configuraciones generales y personaliza tu marca.

**Cuenta** - Solo para Usuarios Admin. Gestiona usuarios y dispositivos (= cámaras 360° asignadas a tu instancia de la plataforma de Avatour).

**Inicio de Sesión de Dispositivo** - Ingresa aquí el número que se muestra en la app de Avatour en tu cámara 360° para iniciar sesión como usuario en la cámara 360°. También puedes iniciar sesión en tu cámara 360° con el correo electrónico y la contraseña de tu cuenta host de Avatour, pero simplemente ingresar el código de dispositivo en la Consola Web de Avatour puede ser más fácil.

**Cerrar sesión** de tu cuenta.

 

### 4.2 Consola Web - Detalles por Elemento del Menú

### 4.2.1 Workspaces

Los Workspaces pueden configurarse para muchos propósitos (por ejemplo, sitios, proyectos, clientes, proveedores) y son unidades organizativas que te ayudan a trabajar eficientemente en un entorno controlado. Puedes crear uno nuevo con el botón "Nuevo Workspace" en la esquina superior derecha de la pantalla.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/v1772360323/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web de Avatour - Elemento del Menú Principal Workspaces*

Haz clic en las notificaciones (el icono de campana) para obtener un resumen de las actividades en un workspace durante los últimos 7 días.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/v1772919758/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Consola Web de Avatour - Actividades Recientes del Workspace*

Puedes ingresar a un workspace haciendo clic en él. Aquí hay una vista de la estructura en un workspace.

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/v1772198701/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Workspace de Avatour con Panel de Assets (izquierda), Canvas en blanco (centro) y Panel de Reuniones (derecha)*

Cada workspace comprende los siguientes elementos (explicados de izquierda a derecha).

**Assets** - Gestiona los assets asignados a ese workspace 

**Colaboradores** - Gestiona el Acceso al Workspace

- **Viewer** - puede ver los assets en el workspace. Agregar un Colaborador Viewer enviará una invitación para convertirse en usuario Guest registrado de Avatour.
- **Editor** - tiene los mismos derechos que el Host (propietario del workspace) y con esto control total del workspace. Agregar un Colaborador Editor enviará una invitación para convertirse en usuario Host registrado de Avatour.

> N.B.: Varios usuarios pueden acceder a un workspace al mismo tiempo sin "reunirse". Esto hace que un "workspace" sea diferente de una "reunión". Además de usar los roles de Colaborador, también puedes hacer el Workspace Público y dar acceso a través de las diversas configuraciones de Acceso a la Reunión - para ambos ver a continuación en "Configuración".

**Informe** - Crea un informe contra la lista de verificación seleccionada en la configuración del workspace basándose en los assets del workspace que elijas. Puedes editar las respuestas propuestas.

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/v1772924118/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe del Workspace de Avatour y Selección de Assets*

**Mapa** - Para assets con metadatos GPS muestra la ubicación en el mapa/imagen satelital.

**Reuniones** - Los Hosts y Colaboradores Editores pueden organizar reuniones en el workspace

**Configuración**

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/v1772387752/avatour-screenshot-workspace-settings_llcei3.png) *Avatour Configuración - Vista del Workspace*

**(1) Configuración del Workspace**

<u>Plantilla de Informe</u> - selecciona una plantilla de lista de verificación contra la cual nuestra IA informará basándose en los assets del workspace elegidos (ver también Informe arriba)

<u>Habilitar Notificaciones</u> - Recibe correos electrónicos de resumen diario para notificar a los colaboradores cuando los Problemas y Acciones de las Notas cambian de estado (por ejemplo, En Progreso → Resuelto).

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/v1772804314/Screenshot_2026-03-05_140654_bjk0xk.png) *Notificaciones por Correo Electrónico - Ejemplo*

<u>Workspace Público</u> - El workspace es como un sitio web - cualquier persona con el enlace del workspace puede ver todos los assets y tiene acceso directo a los assets a través de enlaces de assets. Los enlaces directos a assets solo funcionan con la configuración de Workspace Público (Nota: Los no colaboradores no verán la información de la reunión / botón de unirse).

**(2) Configuración de Reunión**

<u>Autenticación requerida</u> - Cuando está habilitada, los participantes necesitan iniciar sesión con su cuenta de usuario registrado de Avatour (Guest, Host o Admin) para unirse a la reunión.

<u>Permitir acceso de invitado</u> a los assets del workspace

<u>Inicio Automático de Grabación</u> y Requerir consentimiento para reuniones grabadas

<u>Requerir anfitrión</u> - Cuando está habilitado, el anfitrión debe admitir a cada participante en la reunión y la reunión termina cuando el anfitrión se va. Cuando está deshabilitado, los participantes de la reunión pueden iniciar/unirse a una reunión sin un anfitrión en cualquier momento. 

<u>Permitir acceso de espectador</u> - Cuando está habilitado, los participantes pueden usar el código de espectador para unirse a una reunión sin micrófono o cámara web. Los espectadores usan el chat para comunicarse con otros en la reunión.

<u>Reuniones protegidas con contraseña</u> - Cuando está habilitado, los participantes deben ingresar una contraseña para unirse a la reunión que es definida por el anfitrión en la configuración de la reunión.

<u>Mostrar Pregunta de Ahorro de Viaje</u> - Pregunta si la reunión de Avatour ahorra viajes.

> N.B.: Por supuesto es posible usar las configuraciones anteriores en combinación (por ejemplo, no requerir un anfitrión pero sí una contraseña).

### 4.2.2 Assets

Aquí gestionas todos tus assets (videos 360°/2D, imágenes y archivos pdf). Puedes cargar y descargar assets, asignar assets a workspaces, compartir assets con otros usuarios en la plataforma de Avatour. También puedes renombrar assets, imprimir/descargar informes de assets, activar el desenfoque de rostros y la resumización por IA. Para editar un Asset haz clic en el nombre o selecciónalo.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/v1772360326/avatour-screenshot-main-menu-assets_ky5emz.png) *Consola Web de Avatour - Elemento del Menú Principal Assets*

### 4.2.3 Perfil

Aquí puedes gestionar los detalles de tu perfil como tu contraseña.

![Avatour Web Console - Main Menu Item Profile](https://res.cloudinary.com/avatour/image/upload/v1772360324/avatour-screenshot-main-menu-profile_j934va.png) *Consola Web de Avatour - Elemento del Menú Principal Perfil*

### 4.2.4 Configuración

Este elemento del menú solo está disponible para Usuarios Admin. Aquí puedes (1) gestionar la configuración predeterminada para tu cuenta e incluso bloquear esas configuraciones para que otros usuarios no puedan cambiarlas y (2) personalizar algunos elementos de marca (por ejemplo, tu logotipo. Para más información ver [¿Cómo agrego la marca de mi empresa a la experiencia de Avatour?](https://avatour.com/support/how-do-i-add-my-company-branding-to-the-avatour-experience)).

![Avatour Web Console - Main Menu Item Settings (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360321/avatour-screenshot-main-menu-settings-1-of-2_fsaatf.png) *Consola Web de Avatour - Elemento del Menú Principal Configuración (1 de 2)*

![Avatour Web Console - Main Menu Item Settings (2 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772360320/avatour-screenshot-main-menu-settings-2-of-2_qimc09.png) *Consola Web de Avatour - Elemento del Menú Principal Configuración (2 de 2)*

### 4.2.5 Cuenta

Aquí los Usuarios Admin pueden gestionar tus usuarios registrados (host, guest, admin) y dispositivos de captura (cámaras 360° asignadas a tu instancia de la plataforma de Avatour).

![Avatour Web Console - Main Menu Item Account (1 of 2)](https://res.cloudinary.com/avatour/image/upload/v1772803328/avatour-screenshot-main-menu-account-1-of-2_oq5amr.png) *Consola Web de Avatour - Elemento del Menú Principal Cuenta*

### 4.2.6 Analytics

Esta sección te da información sobre tus reuniones y ahorros.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360315/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Consola Web de Avatour - Elemento del Menú Principal Analytics (1 de 3)*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360313/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Consola Web de Avatour - Elemento del Menú Principal Analytics (2 de 3)*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/v1772360312/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Consola Web de Avatour - Elemento del Menú Principal Analytics (3 de 3)*

### 4.2.7 Inicio de Sesión de Dispositivo

Usa esta sección para ingresar el código de 6 dígitos que se muestra en tu cámara 360° (por ejemplo, cuando necesitas iniciar sesión nuevamente o a veces necesita actualizarse). Esta es una forma más conveniente que ingresar tus credenciales de inicio de sesión a través del pequeño teclado en la pantalla de la cámara 360°.

![Avatour Web Console - Main Menu Item Device Login](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-device-login_vlymhj.png) *Consola Web de Avatour - Elemento del Menú Principal Inicio de Sesión de Dispositivo*

### 4.2.8 Tutoriales

Aquí puedes iniciar tutoriales sobre ciertos temas.

![Avatour Web Console - Main Menu Item Tutorials](https://res.cloudinary.com/avatour/image/upload/v1772360310/avatour-screenshot-main-menu-tutorials_nr9hme.png) *Consola Web de Avatour - Elemento del Menú Principal Tutoriales*

 

## 5. En el Sitio - **Cómo Usar el Kit Turnkey de Avatour**{#for-camera-operators}

### 5.1 Kit Turnkey de Avatour 3.1 [(configuración Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2) 

Asegúrate de conectar la batería externa Ulanzi entre la base del trípode y el palo extensible o montar la cámara directamente en el palo de batería extensible Telesin. Además de (1) extender la duración total de la batería de aprox. 1 hora (solo batería de la cámara) a aprox. 3 horas, también ayudará (2) a extender la altura de la configuración de la cámara, (3) añadir peso en la parte inferior para una mejor estabilidad y (4) ayudar a prevenir cualquier posible sobrecalentamiento de la cámara. Recomendamos usar siempre las baterías externas desde el principio, especialmente para reuniones en vivo. 

*Para modelos de cámara anteriores ver Kit 2.1:* [*configuración Pilot One*](https://avatour.com/quickstart-pilot-one/) *y Kits 3.0* [*configuración Pilot Pano*](https://avatour.com/quickstart-labpano-pilot-pano/)*)*

- *Kit 2.1: Conecta un cable USB desde la batería al puerto USB-C del hub USB-C. Luego, conecta la cámara directamente al hub.*
- *Kit 3.0 / 3.1: Conecta un cable USB desde la batería a la cámara.*
- Solo Kit 3.0 / cámara Pilot Pano: Instalación del módulo de enfriamiento (accesorio opcional):
  - *(1) Retira la batería del Pilot Pano abriendo el panel lateral y extrayendo la batería*
  - (2) Inserta el módulo de enfriamiento donde estaba la batería
  - *(3) Conecta la batería externa Ulanzi al módulo de enfriamiento mediante cable USB-A a USB-C. Este cable habría sido incluido con el módulo de enfriamiento.*

### 5.2 Conectividad

<u>**Antes de comenzar:**</u> Para tours en vivo necesitas estar conectado a Internet usando (1) un WiFi local o (2) una Red Móvil. Deberías tener al menos 10 Mbps de ancho de banda de Subida y Bajada. Esto permite suficiente ancho de banda disponible para que la cámara transmita en vivo a nuestros 5 Mbps recomendados. Aún puedes transmitir a anchos de banda menores (1-2 Mbps), lo que funciona mejor cuando estás quieto (ver también a continuación e. Mejores Prácticas: Durante una Reunión). Para probar la velocidad y calidad de conectividad puedes usar los siguientes métodos:

Prueba en una ubicación: Cualquier medidor de velocidad que ya uses (por ejemplo, https://www.speedtest.net/)

**Herramientas de prueba de Avatour (recomendadas):**

1. Prueba en una ubicación: Abre https://avatour.live/test desde cualquier dispositivo en cualquier navegador (debería tomar menos de un minuto) ingresa tu dirección de correo electrónico y una breve razón para la prueba - mide en diferentes ubicaciones en el sitio. Para la evaluación de los resultados, ver [¿Cómo interpreto los resultados de la Prueba de Red de Avatour?](https://avatour.com/support/how-do-i-interpret-the-results-of-the-avatour-network-test)
2. Prueba mientras caminas (¡mejor para verificar todo el recorrido!): Prueba de red con nuestra app Host de Avatour para smartphones (Android: disponible, iOS: prev. Feb. 2024). Cuando estés conectado a la app, selecciona un Workspace y elige "Ejecutar Prueba de Conectividad". Observa el gráfico de conectividad mientras caminas por el sitio y confirma que el ancho de banda de tu red cumple con nuestros 10 Mbps recomendados
3. Prueba mientras caminas (¡mejor para verificar todo el recorrido!): Ejecuta una prueba de red con tu cámara Avatour 360°. Inicia sesión en la app de Avatour desde la pantalla de inicio de la cámara y ve al Menú (las tres líneas rojas en la esquina superior derecha) Configuración → Red → Prueba de Conexión. Observa el gráfico de conectividad mientras caminas por el sitio y confirma que el ancho de banda de tu red cumple con nuestros 10 Mbps recomendados

**WiFi Local**: 

> **<u>Se recomienda encarecidamente conectar tu cámara a una red WiFi local.</u>**

Si tu equipo de TI requiere que la dirección MAC de nuestro dispositivo esté en la lista blanca, puedes encontrar en las cámaras Pilot la dirección MAC aquí: App de Configuración (pantalla de inicio de la cámara) --> Acerca de --> desplázate hacia abajo hasta Dirección WiFi

**Red Móvil:** Para áreas fuera del alcance del WiFi local, conecta la cámara a una red móvil

<u>Opción A: Usa el hotspot y la tarjeta SIM proporcionados con el kit</u>

**Kits 3.0 / 3.1**: Coloca el hotspot GlocalMe en tu bolsillo o mantenlo contigo.

- *Nota de solución de problemas*: Si tu hotspot GlocalMe muestra el mensaje "La conexión de datos no está habilitada", debes verificar que el hotspot esté configurado para usar la tarjeta SIM preinstalada en lugar de una Cloud SIM. Para confirmar esto, desliza hacia la derecha hasta la tercera pantalla en el hotspot, elige "Administrador de Tarjeta SIM" y selecciona "Tarjeta SIM".
- *Nota de solución de problemas*: También asegúrate de que la "red 5G" esté habilitada en el Administrador de Tarjeta SIM
- *Nota de solución de problemas*: Si aún no puedes conectarte a la red de un operador, confirma que tienes el APN correcto seleccionado para tu región. Revisa el artículo [aquí](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot) para crear/gestionar los APN de tu hotspot.

***Kit 2.1**: Usa el hotspot conectado con imán al palo extensible. Puedes conectarte al hotspot a través de WiFi o conexión ethernet cableada (hotspot al hub USB-C)*

Se recomienda usar primero la tarjeta SIM preinstalada en el hotspot proporcionado con tu kit. Esta es una tarjeta SIM "global" que funciona en más de 200 países, generalmente conectándose automáticamente a una red móvil disponible localmente. Podemos implementar Perfiles de Roaming con proveedores de redes móviles preferidos por país. Después de probar más la conectividad y si la calidad de la conexión sigue siendo deficiente, recomendamos obtener tu propia tarjeta SIM local del Operador de Red Móvil con la señal más fuerte en tu(s) ubicación(es).

<u>Opción B: Usa tu propio equipo</u> - hotspot (smartphone o dispositivo hotspot dedicado) y tarjeta de datos SIM

**Notas Importantes**: 

- Mantén el hotspot apagado mientras estés conectado a tu red WiFi local. Una vez que estés fuera del alcance de esta red, conecta la cámara a tus datos SIM.
- Lleva el hotspot contigo idealmente en el bolsillo delantero de tu camisa. Los bolsillos traseros, por ejemplo de los pantalones, son menos ideales porque tu cuerpo bloqueará parte de la señal WiFi entre el hotspot y la cámara 360°.
- Los Operadores de Red Móvil a veces limitan el ancho de banda sin razón aparente ("throttling") para gestionar su red general. Esto puede tener un impacto negativo en la experiencia de Avatour. Ponte en contacto con tu CSM de Avatour o con nuestro equipo de soporte ([support@avatour.live](mailto:support@avatour.live)) si crees que eso está sucediendo.
- Si usas el hotspot GlocalMe, puedes encontrar el nombre WiFi y la contraseña deslizando una pantalla hacia la izquierda. La primera pantalla que aparece puede ignorarse.

**Situaciones de bajo ancho de banda**

- Graba un video de la ubicación con anticipación - para más detalles ver [¿Cómo se graban y cargan videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app) Esto luego puede presentarse durante tu reunión.
- El operador u otros miembros del equipo en el sitio pueden optar por compartir la cámara de su smartphone para transmitir en vivo la ubicación. Esto solo requerirá un ancho de banda de carga de red de 0,1 - 0,3 Mbps.

**Sin conectividad** - Solo video grabado - ver [¿Cómo se graban y cargan videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

### 5.3 Audio

#### Cámara 360° y Operador

En principio, puedes conectar cualquier dispositivo de audio bluetooth incluyendo tus auriculares de EPP si soportan bluetooth.

Si planeas organizar una reunión de Avatour en un entorno al aire libre o ruidoso, recomendamos conectar los **auriculares Shokz** proporcionados en tu kit: 

- **Encendido/Apagado**: Mantén presionado el botón "+" durante 3 segundos. Verás una luz LED azul cuando los auriculares estén encendidos y una luz LED roja cuando estén apagados
- **Modo de Emparejamiento Bluetooth**: Mientras los auriculares estén apagados, mantén presionado el botón "+" durante 5 segundos. Una luz LED parpadeará en azul y rojo cuando esté en modo de emparejamiento
- **Subir/Bajar Volumen**: Usa los botones "+" y "-" para aumentar o disminuir el volumen de escucha

En un entorno más tranquilo, puedes optar por conectar un altavoz bluetooth, como el **altavoz NoxGear** de clip:

- **Encendido/Apagado**: Mantén presionado el botón Reproducir/Pausa en el centro del dispositivo durante 2 segundos
- **Modo de Emparejamiento Bluetooth:** Una vez que el dispositivo esté encendido, entrará en modo de emparejamiento (LEDs azul y rojo parpadeantes). Una vez emparejado, mostrará un LED azul
- **Subir/Bajar Volumen**: Usa los botones "+" y "-" para aumentar o disminuir el volumen de escucha

**Kits 3.0 / 3.1:** Puedes emparejar/conectar cualquier dispositivo bluetooth desde la pantalla de inicio de la cámara a través de la app de Configuración. Ve a Configuración → Bluetooth.

***Kit 2.1**: Para emparejar/conectar un auricular/altavoz bluetooth, primero debes tener una conexión cableada entre el hub USB-C (con dongle bluetooth Jabra) y la cámara. Si usas los auriculares Shokz o el altavoz NoxGear, estos se conectarán tan pronto como se enciendan.*



#### Otros Participantes en el Sitio

Conéctate a la reunión usando el navegador de tu smartphone/tablet/portátil y usa auriculares con cable o inalámbricos (preferiblemente con cancelación de ruido habilitada). **Ten en cuenta que cada smartphone en el sitio reducirá el ancho de banda de la cámara 360°** y puede tener un impacto negativo en la reunión de Avatour para todos los participantes. Por lo tanto **recomendamos unirse en**

- **Modo En el Sitio** - Únete a la reunión en modo En el Sitio cuando estés físicamente presente en el mismo lugar que la cámara 360°. El Modo En el Sitio es perfecto para usuarios que desean usar sus teléfonos principalmente para primeros planos detallados. El Modo En el Sitio silencia el micrófono y el altavoz de forma predeterminada para eliminar el eco de audio

  ***Captura de Pantalla Modo En el Sitio POR HACER !!!***

**Nota Importante**: 

- Asegúrate de estar en silencio cuando no estés hablando activamente
- Si es posible, ten tu smartphone conectado a una red diferente a la red de la cámara.



### 5.4 App de Cámara de Avatour

Aquí están los menús (1) Nivel Superior, (2) Configuración y (3) Configuración de Red.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/v1772918698/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *App de Cámara 360° de Avatour - 3 Menús*

**Quick Capture** - Para grabación de video 360° sin conexión. - Para una descripción detallada ver [¿Cómo se graban y cargan videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Recomendamos usar un dispositivo de audio externo (conectado vía bluetooth). N.B. También puedes hacer videos e imágenes estándar 2D - simplemente cambia el modo entre 360° y 2D en la esquina inferior derecha una vez en la pantalla QC.

**Reunión en Vivo** - Para Videoconferencia en vivo 360°. Verás tus workspaces y al hacer clic en uno se iniciará el stream de video en vivo desde la cámara 360°. Antes de poder unirte a la reunión con tu cámara 360°, necesitas conectar un dispositivo de audio vía bluetooth. Para una descripción detallada ver [¿Cómo iniciar una reunión Live Capture con tu cámara Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Al organizar una reunión Live Capture con tu cámara 360°, tendrás herramientas de reunión similares disponibles que reflejan la experiencia web. Aquí hay un enlace a nuestro artículo de la Base de Conocimiento que explica estas herramientas con más detalle: [Herramientas de la App de Operador](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galería** - Aquí encuentras todos tus videos e imágenes 360° para cargar a la Consola Web de Avatour.

**Configuración** - En Configuración tienes las siguientes opciones:

- **Red**: Esta opción te permite cambiar a qué red WiFi está conectada la cámara o ejecutar una prueba de conexión de red para ver el rendimiento de streaming
- **Live Capture**: Ajusta tu configuración de Live Capture según el ancho de banda disponible, la sensibilidad VR de los invitados o si las lentes protectoras de tu cámara están instaladas:
  - **Tasa de Fotogramas Objetivo**: Ajusta la tasa de fotogramas para tu video Live Capture entre 15 fps, 24 fps y 30 fps. Las tasas de fotogramas más altas producen un video más fluido, pero requerirán más ancho de banda de subida. Predeterminado: 15 fps
  - **Bitrate Objetivo**: Te permite aumentar o disminuir el bitrate máximo de streaming para tu Live Capture. Puedes establecer tu bitrate objetivo entre 1 Mbps y 10 Mbps. Los bitrates más altos resultarán en una resolución de video más alta, pero requerirán más ancho de banda de subida. Predeterminado: 5 Mbps
  - **Optimizar Movimiento**: Esto disminuirá la tasa de fotogramas del video, generando menos carga en el ancho de banda de subida de tu red, y aumentará tu bitrate de streaming. Además, esta opción ayuda a reducir el mareo por movimiento para los participantes VR. Predeterminado: Desactivado
  - **Lentes Protectoras**: Esto afectará cómo se une el video 360° dependiendo de si se han instalado lentes protectoras en tu cámara. Si no tienes lentes protectoras, establece esto en "No". Si recibiste un Kit 3.0, tienes lentes protectoras preinstaladas y debes establecer esto en "Sí". Predeterminado: Sí

- **Quick Capture**: Ajusta tu configuración de Quick Capture según tu tasa de fotogramas de video preferida, el ancho de banda disponible para cargas de video grabado o si las lentes protectoras de tu cámara están instaladas. Quick Capture tiene una resolución fija de 4k que generalmente logra un buen equilibrio entre calidad de video y tamaño de archivo. (Para resoluciones más altas puedes usar las apps nativas de la cámara, también en el PanoX V2, para más detalles ver [¿Cómo se graban y cargan videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Tasa de Fotogramas Objetivo**: Ajusta la tasa de fotogramas para las grabaciones de video Quick Capture entre 15 fps, 24 fps y 30 fps. Las tasas de fotogramas más altas producen un video más fluido, pero aumentarán el tamaño del archivo de video y el tiempo de carga. Recomendado: 30 fps
  - **Bitrate Objetivo**: Establece el bitrate objetivo para las cargas de Quick Capture entre 5 Mbps y 20 Mbps. Los bitrates más bajos aumentan las velocidades de carga, pero disminuirán la calidad del video. Recomendado: 20 Mbps
  - **Lentes Protectoras**: *Ver sección de Lentes Protectoras para Live Capture arriba*
- **Acerca de**: Ver el número de serie del dispositivo y la versión del software

**Cuenta** - Para iniciar sesión con tu cuenta host o admin de Avatour.

## 6. Consejos de Mejores Prácticas

### 6.1 Primeros Usos (Informales) y Familiarización

Para tus primeros usos y para familiarizarte con la Consola Web de Avatour y el Kit Turnkey de Avatour, recomendamos los siguientes pasos:

1. Lleva el kit a casa y úsalo con familiares y amigos usando tu conexión a Internet doméstica.
2. Lleva el kit a la oficina y conéctalo a una red corporativa (pueden surgir problemas corporativos, por ejemplo, firewalls corporativos - pero sabes del paso uno que Avatour funciona y este es un tema a resolver por tu equipo de TI con la ayuda de Avatour).
3. Comienza a usar Avatour en el sitio (fuera de tu oficina) en el lugar de la reunión al que los participantes remotos normalmente tendrían que viajar. Pueden surgir más problemas de conectividad. Avatour ayudará en cooperación con tu equipo de TI.
4. Comienza a usar con participantes remotos internos y externos.

### 6.2 Antes de una Reunión en Vivo con Video 360°

- Recomendamos hacer un tour de video 360° grabado antes de cualquier tour en vivo si el tiempo lo permite por tres razones: (1) Tener una solución de respaldo para el tour en vivo, (2) tener algo para documentación y revisión posterior (además del tour en vivo grabado) y (3) comenzar a crear una biblioteca de videos 360° de todos tus sitios que puede ser útil para muchos casos de uso. 
- Todos los componentes del kit cargados durante al menos 90 minutos antes de la reunión en vivo. De todos modos recomendamos tener todos los dispositivos en carga continua cuando no estén en uso. De esa manera todos los dispositivos estarán siempre listos, también para reuniones ad hoc no planificadas.
- Tener el kit completamente ensamblado (1. base del trípode + 2. batería Ulanzi + 3. palo extensible + 4. cámara 360°).

- Confirmar que se ha creado un Workspace para organizar una reunión en vivo e incluir todos los Assets relevantes.

- Invitar a todos los participantes a la reunión a través de tu Workspace. Esto crea una invitación en los calendarios de todos los participantes e incluye el enlace de invitación a la reunión.

- Emparejar y conectar los auriculares o altavoz bluetooth que planeas usar para el tour a la cámara.

- Todos los usuarios de smartphones en el sitio deben conectarse desde una red diferente a la de la cámara. Esto reducirá la carga en el ancho de banda de red de la cámara.

- Si estás solo como operador de la cámara, lleva un smartphone contigo en caso de que quieras compartir la cámara del smartphone y mostrar detalles finos.

- Confirmar que la cámara 360° puede conectarse a tu WiFi local.

- Antes de una reunión de Avatour, planifica la ruta que tomarás a través de las instalaciones. Haz una reunión de prueba de Avatour con la cámara y verifica que todas las áreas tengan bitrates superiores a 1 Mbps de ancho de banda. Esto se puede ver en la propia pantalla de la cámara, o como participante remoto yendo a Configuración y activando Mostrar Bitrate.

- Si notas que algunas áreas tienen poco o ningún ancho de banda, lo mejor es tomar imágenes o hacer una grabación. Estas pueden luego presentarse durante la reunión para que los participantes remotos las revisen. Puedes seguir la guía aquí que explica nuestro Quick Capture para grabar y cargar videos/imágenes: [¿Cómo se graban y cargan videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si tienes participantes remotos uniéndose a la reunión que nunca han usado Avatour antes, proporciónales un breve resumen de la plataforma, su funcionalidad (video en vivo 360°, assets, snapshots, anotaciones, spotlight) y las herramientas de la reunión.

- Puedes comenzar en otra solución de videoconferencia (por ejemplo, Teams, Zoom, Google Meet) pero antes de pasar a Avatour, cierra completamente la otra aplicación de videoconferencia. En algunos casos, estas otras aplicaciones priorizarán el micrófono/altavoces/cámara web de tu dispositivo, causando que se deshabiliten para Avatour. Además, NO ejecutes Avatour Y otra videoconferencia al mismo tiempo ya que esto reducirá el ancho de banda disponible.

- Si planeas usar la cámara 360° en un entorno de alta temperatura, se recomienda usar el módulo de enfriamiento (solo Pilot Pano). Esto ayudará a reducir las posibilidades de que la cámara se sobrecaliente y se apague automáticamente.

### 6.3 Durante la Operación de la Cámara en el Sitio para una Reunión en Vivo con Video 360°

- Al operar la cámara, asegúrate de caminar lentamente. Esto ayuda con la calidad del video y reduce cualquier posible tiempo de inactividad del video cuando la conexión de red de la cámara cambia entre puntos de acceso WiFi.

- Sostén la cámara frente a ti y por encima del nivel de los ojos. Esto permite a todos los participantes remotos ver la mayor parte del área que te rodea.

- Para los casos en que la cámara necesita permanecer estable, usa el trípode y extiende la cámara a la altura correcta, preferiblemente a nivel de los ojos.

- Conecta siempre la cámara a tu red WiFi local cuando sea posible. Para áreas sin acceso WiFi, usa el hotspot proporcionado. El hotspot tiene una tarjeta SIM que se conectará a una red celular confiable cerca de ti. Mantén siempre el hotspot apagado cuando no esté en uso en interiores ya que de lo contrario la cámara 360° podría conectarse al hotspot lo cual no queremos en interiores. Cuando estés en exteriores, mantén el hotspot cerca de la cámara 360°.

- Cuando el bitrate en la cámara comience a caer por debajo de 2 Mbps, camina más lento o detente completamente hasta que la señal se estabilice nuevamente. Esto generalmente ocurre cuando cambias de un Punto de Acceso WiFi a otro. 

- Si sabes que la conectividad y el video caerán cuando te muevas a una ubicación específica (Ejemplo: moviéndote de un área de producción interior a un área exterior), avisa a los participantes remotos con anticipación.

- Si necesitas mostrar algo en alto detalle o letras pequeñas, usa tu propio smartphone o el de un participante en el sitio para unirte a la reunión y presentar la cámara (trasera) del teléfono.

- Si es posible, recomendamos que una persona adicional esté en el sitio para ayudar con la compartición de cámara del smartphone descrita anteriormente, ya que a menudo resulta útil/necesaria.

- Idealmente los usuarios de smartphones en el sitio deben unirse a la reunión (1) en modo en el sitio y (2) en una red diferente a la que usa la cámara para no quitar ancho de banda de subida crucial a la cámara 360°.

- Todos los participantes en el sitio que se unan desde su smartphone deben estar silenciados, a menos que estén hablando activamente.
