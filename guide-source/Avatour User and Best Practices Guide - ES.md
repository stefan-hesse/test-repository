# Avatour User and Best Practices Guide

## 1. Para Todos los Usuarios de Avatour {#for-all-avatour-users}
Si es nuevo en Avatour, los siguientes recursos proporcionan una introducción útil a la plataforma y sus capacidades:

1. [Video Cómo funciona Avatour](https://avatour.com/how-it-works)  
Una descripción general breve de las características principales de Avatour y cómo la plataforma permite la colaboración remota inmersiva.
2. [Preguntas frecuentes](https://avatour.com/faqs)  
Respuestas a preguntas frecuentes.
3. [Glosario](https://avatour.com/glossary)  
Definiciones de términos y conceptos clave de Avatour utilizados frecuentemente.
4. Sitio web  
Asegúrese de consultar especialmente la página [Características de Avatour](https://avatour.com/features) junto con las secciones dedicadas a Casos de uso e Industrias para aprender cómo Avatour puede satisfacer sus necesidades específicas.## 2. Tipos de Usuarios de Avatour  {#avatour-user-types}

### 2.1 Asistentes a la reunión (No se requiere cuenta)
Los usuarios pueden unirse a la reunión sin registrarse en una cuenta de Avatour.
Excepción: Si el anfitrión ha restringido la reunión a usuarios registrados — por ejemplo, para permitir que solo empleados internos se unan a través de Inicio de sesión único (SSO) — la invitación del calendario indicará que los participantes deben iniciar sesión para autenticarse.

Los usuarios acceden a la reunión de la siguiente manera:

- Reciben una invitación del calendario del anfitrión.
- Utilizan el enlace de la reunión en la invitación para unirse.
- Ingresan una contraseña de la reunión si el anfitrión ha habilitado una.
- Los participantes pueden unirse sin una cuenta de Avatour a menos que la reunión esté restringida y requiera iniciar sesión para autenticarse.

#### 2.1.1 Participante

- Pueden unirse e interactuar completamente (cámara web, micrófono, chat y funcionalidad de Presentar).
- Máximo de 20 participantes interactivos por reunión.

#### 2.1.2 Espectador

- Pueden ver la reunión y participar solo a través del chat.
- No pueden compartir video, usar micrófono, presentar, reproducir/pausar Assets o capturar Snapshots.
- Máximo de 10 espectadores por reunión.
- Junto con los participantes, una reunión puede albergar hasta 30 asistentes.### 2.2 Usuarios Registrados

Los Usuarios Registrados tienen una cuenta de Avatour. Las cuentas se crean de una de las siguientes formas:

- **Invitados por Admin:** Durante la incorporación, Avatour configura un **inquilino dedicado** para la organización y crea una o más **cuentas de Admin**. Los Admins pueden entonces **invitar usuarios** dentro de la organización y asignarlos a **grupos**, que definen su rol en la plataforma (Guest, Host o Admin). Los usuarios invitados reciben un **enlace de registro** para completar la configuración de la cuenta y establecer una contraseña.  
- **Invitados por Host:** Los Hosts pueden añadir usuarios como **colaboradores de Editor** a un Workspace. Esto consume una **licencia de Host** y garantiza que el usuario tenga acceso a nivel de Host.  
- **Aprovisionamiento automático de SSO (solo nivel Enterprise/Business):** Las cuentas pueden ser creadas automáticamente por el IdP. Por defecto, las cuentas aprovisionadas por SSO se añaden al **grupo Guest**, a menos que se sobrescriba mediante **asignaciones de grupos SAML**. Los Admins pueden seguir invitando usuarios y asignando pertenencia a grupos directamente incluso cuando SSO está habilitado.

**Resumen:**  

Los usuarios registrados y su pertenencia a grupos pueden gestionarse de varias formas:

- **Gestión por Admin:** Un Admin en la consola de Avatour puede crear usuarios y asignarlos a grupos, que definen su rol en la plataforma (Guest, Host o Admin).  
- **Aprovisionamiento de SSO:** Para clientes de nivel Enterprise o Business con SSO habilitado, el IdP puede aprovisionar cuentas automáticamente y asignar pertenencia a grupos, que define el rol de la plataforma del usuario.  
- **Usuarios invitados por Host:** Los Hosts pueden invitar a otros usuarios como colaboradores de Editor a Workspaces específicos. Asignar el rol de colaborador de Editor consume una licencia de Host.

**Práctica Recomendada (Clientes Enterprise):**  
Para organizaciones que esperan un gran número de usuarios que necesitan acceso a Avatour, se recomienda **integrar Single Sign-On (SSO)** y gestionar usuarios y pertenencia a grupos desde el **IdP**. Este enfoque simplifica el aprovisionamiento de cuentas, la asignación de grupos y la gestión de licencias, reduciendo la sobrecarga administrativa y garantizando un control de acceso consistente.

#### 2.2.1 Usuarios Guest

- Añadidos al **grupo Guest**.  
- Pueden **ver Assets** dentro de Workspaces donde han sido añadidos como **colaboradores de Viewer**.  
- No pueden crear workspaces, organizar reuniones ni subir contenido.  
- Las cuentas Guest aprovisionadas por SSO **se autentican a través del IdP**; no se requiere contraseña gestionada por Avatour.

---

#### 2.2.2 Usuarios Licenciados (Acceso a Consola Web)

##### Usuarios Host (Grupo: Host)

- Pueden crear/gestionar Workspaces, invitar colaboradores a un workspace, **organizar reuniones en directo**, subir **Quick Captures**.  
- Tienen acceso al **Panel de Control de Host** y **Aplicación de Operador** en cámaras 360° compatibles.  

##### Usuarios Admin (Grupo: Admin)

- Incluye todas las capacidades de Host más administración completa de la cuenta.

**Los privilegios adicionales de Admin incluyen:**

**Gestión de Cuentas**  

- Crear nuevos usuarios y asignarlos a grupos.
- Restablecer contraseñas cuando son gestionadas por Avatour (no aplicable cuando SSO está habilitado). 
- Actualizar usuarios Guest a Host.  
- Desactivar usuarios (las cuentas de Admin deben convertirse primero a Host antes de su eliminación).  
- Transferir assets de un usuario Host a otro durante la eliminación.

**Configuración**  

- Configurar **ajustes de seguridad en toda la organización** para assets, workspaces y reuniones alojadas en la plataforma (por ejemplo, si un Host debe estar presente para iniciar una reunión, si las caras deben borrarse en todos los vídeos subidos a la plataforma).  
- Habilitar o deshabilitar **características de IA** o **grabación**.  
- Aplicar marca de empresa de forma consistente en toda la plataforma si se configura un **dominio personalizado**.
  

**Assets y Análisis** 
 
- Ver todos los Assets subidos por cualquier usuario en la organización.  
- Revisar el uso de la plataforma en toda la organización.

---

#### 2.2.3 Permisos de Colaboradores en Workspace

Los permisos de Workspace definen qué puede hacer un usuario **dentro de un Workspace específico**. Estos son independientes de la pertenencia a grupos a nivel de plataforma (Guest, Host, Admin).

- **Colaborador de Editor:** Los usuarios con este permiso pueden:
  - Gestionar Assets (subir, eliminar, desenfocar caras, generar resúmenes)  
  - Gestionar configuración de reuniones (habilitar/deshabilitar grabación, permitir o eliminar participantes)  
  - Programar y organizar reuniones en directo  
  - Generar reportes basados en plantillas predefinidas  
  - Añadir o eliminar colaboradores del Workspace  

- **Colaborador de Viewer:** Los usuarios con este permiso tienen acceso de solo lectura a los Assets del Workspace. **No pueden modificar Assets, gestionar reuniones ni gestionar colaboradores**, pero **pueden crear Notas en Assets**.## 3. Para Participantes de Reuniones Remotas y Visitantes del Espacio de Trabajo {#for-remote-meeting-participants-and-workspace-visitors}
Avatour permite a los usuarios colaborar de dos formas principales:

- **Unirse a una reunión de Avatour (Colaboración síncrona):**  
  Puede recibir una **invitación de calendario** para unirse a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota en vivo del sitio** o revisar recursos de forma sincrónica juntos.

- **Visitar un Espacio de trabajo (Colaboración asincrónica):**  
  También puede ser invitado como **colaborador a un Espacio de trabajo** para revisar recursos de **forma asincrónica** (según su propio horario).### 3.1 Cómo unirse a una reunión de Avatour y visitar un espacio de trabajo de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Cualquier dispositivo de "pantalla plana" con navegador web {#any-flat-screen}
Puede unirse a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, smartphone o tableta** usando un navegador web.  

##### Unirse a una reunión de Avatour

> **Nota:** Unirse a una reunión de Avatour requiere que **otorgue permisos de micrófono**. Por favor, acepte cualquier solicitud de permiso de su navegador.

1. **A través de invitación de calendario (recomendado):**  
   - Normalmente recibirá una **invitación de calendario** con un **enlace de acceso directo** (por ejemplo: `https://avatour.live/join?s=xxxxx`).  
   - Al hacer clic en el enlace, se completará automáticamente el **código de reunión de 5 caracteres** y lo llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que debe **iniciar sesión para acceder a la reunión**.  
   - **Reuniones protegidas por contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debe ingresar para unirse.

2. **A través del código de reunión:**  
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, vaya a [https://avatour.live/join](https://avatour.live/join), ingrese su **nombre** y el **código de reunión**, y únase a la reunión.  
   - Si la reunión está **protegida por contraseña**, ingrese la contraseña proporcionada por el anfitrión.  
   - Si la reunión requiere **autenticación**, deberá **iniciar sesión con su cuenta de Avatour** antes de unirse.

> **Consejo 1:** Si su cámara o micrófono no funciona, es posible que esté siendo utilizado por otra aplicación (por ejemplo, Microsoft Teams o Zoom). Cierre cualquier aplicación que pueda estar usando su cámara o micrófono, luego salga y vuelva a unirse a la reunión de Avatour.  

> **Consejo 2:** Si aún no puede unirse a la reunión, ejecute esta prueba: [https://avatour.live/test](https://avatour.live/test).  
> La prueba puede identificar si su **cortafuegos corporativo o red** está bloqueando el acceso, y proporcionará información para guiar las discusiones con su equipo de TI.  

> **Consejo 3:** **No** use las aplicaciones de Avatour para iOS o Android para unirse a reuniones. Estas aplicaciones solo son necesarias cuando **se transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar el software Avatour 360° directamente y requieren un smartphone para asistir.

##### Visitar un espacio de trabajo de Avatour (sin unirse a una reunión de Avatour)

Puede acceder a un espacio de trabajo de las siguientes formas:

- **Espacio de trabajo público:**  
  Si el espacio de trabajo es público, se puede acceder al enlace directamente — no se requiere inicio de sesión.

- **Espacio de trabajo restringido:**  
  Si el espacio de trabajo está restringido, debe ser agregado como **colaborador** con permisos de **Editor** o **Visualizador**.

  1. Cuando sea agregado como colaborador, recibirá una **notificación por correo electrónico** con un enlace al espacio de trabajo.
  2. Haga clic en el enlace del correo electrónico para abrir el espacio de trabajo. Si aún no ha iniciado sesión, se le pedirá que **inicie sesión o complete el registro**.
  3. Una vez conectado, el espacio de trabajo se abrirá automáticamente.

  Alternativamente, puede iniciar sesión en [https://avatour.live/login](https://avatour.live/login) y acceder al espacio de trabajo desde su **lista de espacios de trabajo**.

#### 3.1.2 Casco de realidad virtual {#vr-headset}
Puede unirse a una reunión y visitar un espacio de trabajo desde una variedad de cascos Meta y Pico compatibles. Para hacer esto: 

1. Instale nuestra aplicación Avatour desde su respectiva tienda de aplicaciones de realidad virtual: [Cómo instalar la aplicación Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Cargue nuestra aplicación e ingrese el código de reunión o seleccione un espacio de trabajo para unirse a una reunión. Para obtener más información sobre cómo usar nuestra aplicación de realidad virtual, consulte nuestro artículo de la base de conocimientos [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Herramientas de Reunión y Colaboración en Espacios de Trabajo {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (sincrónicas):** Colabora en tiempo real con otros participantes, incluyendo visitas en vivo al sitio o revisión de activos grabados juntos.  
2. **Espacios de trabajo (asincrónicas):** Revisa e interactúa con activos a tu propio ritmo, 24/7.

Las **herramientas de colaboración son mayormente similares** entre reuniones y espacios de trabajo, con algunas diferencias debido al contexto sincrónico vs asincrónico.

#### 3.2.1 Diseño de la Interfaz

La interfaz de Avatour se organiza alrededor de tres áreas principales:

- **Panel izquierdo** – Activos del espacio de trabajo y herramientas de apoyo  
- **Lienzo central** – Área principal de visualización para video en vivo o activos  
- **Panel derecho** – Información contextual, como participantes, reuniones o chat  

La mayoría de las interacciones se inician desde el **menú inferior**.  
Al hacer clic en una opción del menú se abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **lienzo central** permanece como el área de visualización principal.

---
#### 3.2.2 Ejemplo de Vista de Reunión

Aquí hay un ejemplo de una vista en una Reunión de Avatour:

![Interfaz de Reunión de Avatour con Panel de Activos, Lienzo en blanco y Panel de Participantes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Reunión de Avatour con Panel de Activos (izquierda), Lienzo (centro) y Panel de Participantes (derecha)*

---

#### 3.2.3 Ejemplo de Vista de Espacio de Trabajo

Aquí hay un ejemplo de una vista de Espacio de Trabajo:

![Espacio de Trabajo de Avatour con Panel de Activos, Lienzo en blanco y Panel de Reuniones](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espacio de Trabajo de Avatour con Panel de Activos (izquierda), Lienzo (centro) y Panel de Reuniones (derecha)*

---

#### 3.2.4 Descripción General del Menú Inferior

El menú inferior proporciona acceso a los controles de interfaz principales y paneles:

**Menú Inferior de Reunión**  

![Menú Inferior de Reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menú Inferior de Reunión de Avatour*

- **Activos** – Revisa archivos del espacio de trabajo, incluyendo videos grabados, imágenes, capturas de pantalla y PDFs. 
- **Chat** – Envía mensajes a todos los participantes de la reunión.  
- **Cámara** – Enciende o apaga tu cámara web.  
- **Micrófono** – Silencia o activa el sonido.  
- **Presentar** – Presenta un activo, escritorio o feed de cámara web (ver sección Presentar a continuación).  
- **Herramientas del Host** (solo para hosts):  
  - **Bloquear Enfoque** – Bloquea la vista para todos los participantes.  
  - **Silenciar Todo** – Silencia a todos los participantes.  
- **Habilitar Pantalla Completa** – Pone la pestaña de reunión en pantalla completa.  
- **Salir de la Reunión** – Sal de la reunión.  
- **Iniciar Grabación** – Usa este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones se pueden grabar automáticamente si la **grabación automática** está habilitada en la configuración del espacio de trabajo. En ambos casos, las grabaciones se guardan en los activos del espacio de trabajo.
- **Mapa** – Abre o cierra el panel de mapa para activos con una pista GPS. Al hacer clic en una ubicación, se salta al punto exacto del video. El mapa se actualiza en vivo a medida que se reproduce el video.
- **Participantes** – Abre o cierra el panel de participantes.  
- **Información de la Reunión** – Ver el código de la reunión, enlace de invitación y acceder a tutoriales relacionados.  

![Información de Reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panel Lateral de Información de Reunión de Avatour*

- **Configuración** – Ajusta idioma, audio y configuración de video. Para reuniones de video en vivo 360°, usa **Mostrar Velocidad de Bits** para monitorear estadísticas de conectividad.

> Consejo: Envía el enlace de la reunión o agrégalo a un elemento del calendario para invitar participantes.

---

##### Menú Presentar

La opción **Presentar** en el menú inferior de reunión te permite compartir contenido con todos los participantes.

- **Cámara** – Comparte la cámara de tu smartphone/tablet. Esto también se puede usar durante una reunión de video 360° en vivo para superponer una vista secundaria para primeros planos o detalles específicos. 
- **Escritorio** – Comparte tu pantalla de escritorio con todos los participantes.  
- **Activo** – Presenta un activo del espacio de trabajo. Al seleccionar un activo se abre la **Barra de Herramientas del Activo**, que proporciona controles de reproducción y herramientas de colaboración específicas del activo que se está presentando.

##### Barra de Herramientas del Activo (Reunión)

Al presentar un activo en una reunión, la **Barra de Herramientas del Activo** aparece encima del lienzo. Aquí están las herramientas y elementos del menú disponibles cuando <u>presentas un Activo en una Reunión</u> - explicadas de izquierda a derecha.

![Menú de Avatour al Presentar un Activo en una Reunión](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour al presentar un Activo en una Reunión*


- **Cronología de Video / Barra de Progreso** – Muestra el progreso del video con notas y temas clave extraídos del audio. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausa**.   
- **Captura de Pantalla** – Captura una imagen 360° o 2D del activo.  
- **Foco** – Destaca un área específica para todos los participantes durante sesiones en vivo.  
- **Mostrar/Ocultar Punto de Vista (POV)** – Muestra dónde está mirando cada participante en el video 360°.  
- **Notas** – Crea notas ancladas a momentos específicos del activo. Las notas se pueden categorizar (Observación, Problema, Acción, Recomendación), rastrear por estado (Abierto → En Progreso → Resuelto) y compartir a través de enlaces directos.  

  ![Nota de Avatour y Filtro de Notas](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota de Avatour y Filtros de Notas*

  - **Notas por Comando de Voz** – Estos son marcadores de posición generados automáticamente cuando la grabación detecta menciones como "insertar nota", "tomar una nota" o "hacer una nota". Estas notas aparecen en la cronología y deben ser **posicionadas y finalizadas** por el usuario. 

  ![Notas de Avatour - Generadas por Comando de Voz](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por Comando de Voz*

- **Panel de Notas y Resumen** – Abre un panel lateral que muestra todas las notas, temas clave y un resumen ejecutivo del activo. Al hacer clic en un elemento, te lleva a ese momento en el video.  

  ![Resumen Ejecutivo de Activo de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen Ejecutivo de Avatour al presentar un Activo en una Reunión*

  ![Temas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Temas de Avatour al presentar un Activo en una Reunión*

  Desde el **Panel Lateral**, puedes **imprimir un informe del activo** o **descargarlo como TXT o CSV**. Los informes pueden incluir notas, temas generados por IA y transcripciones completas. También puedes **elegir qué elementos incluir** antes de exportar.  

  ![Menús de Impresión de Informe de Activo de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menús de Impresión/Descarga de Informe de Activo de Avatour*  

  ![Menú de Selección de Elementos de Informe de Activo de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menú de Selección de Elementos de Informe de Activo de Avatour*

- **Enlace Compartido** – Comparte un enlace a una nota específica o escena en el activo.  
- **Subtítulos Cerrados (CC)** – Muestra transcripción de texto en pantalla durante la reproducción del video.

##### Barra de Herramientas del Activo (Espacio de Trabajo)

Al revisar un activo en un espacio de trabajo, la barra de herramientas es similar pero optimizada para uso individual:

![Menú de Avatour al Presentar un Activo fuera de una reunión, p. ej. al visitar un espacio de trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menú de Avatour al presentar un Activo en un Espacio de Trabajo*

- **Cronología de Video / Barra de Progreso** – Muestra el progreso del video con notas y temas clave extraídos de la pista de audio. Haz clic en cualquier lugar de la cronología para avanzar o retroceder en el video. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausa**.  
- **Captura de Pantalla, Notas, Panel de Notas y Resumen, Enlace Compartido, Subtítulos Cerrados**  
- No disponibles: **Foco, POV** (estos requieren participantes en vivo)  
- Controles adicionales:
  - **Saltos de 10 segundos** – Avanza/retrocede  
  - **Velocidad de Reproducción** – Ajusta la velocidad (0.5×–2×)  
  - **Recortar Video** – Recorta el principio o final del activo## 4. Para Usuarios Host y Admin - Consola Web Avatour {#for-host-and-admin-users-avatour-web-console}
Cuando inicia sesión en su Cuenta de Usuario de Avatour, accederá a la **Consola Web**.### 4.1 Consola Web - Menú Principal General {#web-console-overview-main-menu}

En el lado izquierdo, verá los siguientes elementos del menú:

![Consola Web Avatour - Menú Principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Consola Web Avatour - Menú Principal*

- **Espacios de trabajo** – Organice su contenido de manera eficiente. Cada espacio de trabajo contiene **Activos**, **Colaboradores**, **Reuniones** y **Configuración**.  
- **Activos** – Acceda y gestione todos sus activos (videos, imágenes, PDFs). Los administradores pueden ver todos los activos de la cuenta, y los activos compartidos son visibles para todos los usuarios.  
- **Perfil** – Gestione su idioma y contraseña.  
- **Analytics** – Realice un seguimiento de la actividad de sesiones, el uso del espacio de trabajo y las métricas de ROI.  
- **Configuración** *(Solo administrador)* – Configure los valores predeterminados del espacio de trabajo, reuniones y activos en toda la organización. Los administradores también pueden personalizar la marca (logo, colores, fondos).  
- **Cuenta** *(Solo administrador)* – Gestione usuarios registrados y cámaras 360°.  
- **Inicio de sesión en dispositivo** – Ingrese el código que se muestra en su cámara 360° para emparejarla con su cuenta.  
- **Tutoriales** – Acceda a tutoriales guiados.  
- **Cerrar sesión** – Cierre sesión en la consola.

> Las secciones como Perfil, Inicio de sesión en dispositivo, Tutoriales y Cerrar sesión son autoexplicativas y no tienen subsecciones detalladas.

---### 4.2 Consola Web - Detalles por Elemento del Menú (con imágenes) {#web-console-details-by-menu-item}

#### 4.2.1 Espacios de Trabajo

Los espacios de trabajo son unidades organizativas flexibles que le permiten administrar activos, colaboradores y reuniones en un solo lugar. Puede crear un nuevo espacio de trabajo con el botón **Nuevo Espacio de Trabajo** en la esquina superior derecha.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web Avatour - Elemento de Menú Principal Espacios de Trabajo*

Haga clic en el icono de campana para ver un resumen de la actividad del espacio de trabajo durante los últimos 7 días.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Actividades Recientes del Espacio de Trabajo*

Dentro de un espacio de trabajo:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espacio de Trabajo con Activos (izquierda), Lienzo (centro), Reuniones (derecha)*

- **Activos** – Administre archivos asignados a este espacio de trabajo.  
- **Colaboradores** – 
  Controle el acceso a espacios de trabajo por 
  - **Visualizador** – Puede ver activos. La invitación crea un usuario invitado si es necesario.  
  - **Editor** – Control total del espacio de trabajo, mismos derechos que Anfitrión. La invitación actualiza el usuario a Anfitrión si es necesario.  
> Varios usuarios pueden acceder a un espacio de trabajo simultáneamente sin una reunión. Los espacios de trabajo públicos y la configuración de acceso a reuniones proporcionan acceso alternativo.  
- **Informe** – Genere un informe utilizando una plantilla de lista de verificación en los activos del espacio de trabajo seleccionado.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe del Espacio de Trabajo y Selección de Activos*

- **Mapa** – Muestre las ubicaciones de activos habilitadas con GPS en un mapa.  
- **Reuniones** – Organice reuniones en el espacio de trabajo.  
- **Configuración** – Configure los valores predeterminados del espacio de trabajo y la reunión:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Configuración del Espacio de Trabajo*

**Configuración del Espacio de Trabajo**

- **Plantilla de Informe** – Seleccione la plantilla de lista de verificación para informes de IA.  
- **Habilitar Notificaciones** – Correos electrónicos de resumen diario para cambios de estado de notas.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Ejemplo de Notificaciones por Correo Electrónico*

- **Espacio de Trabajo Público** – Cualquiera con el enlace puede ver los activos directamente.

**Configuración de Reuniones**
  
* **Autenticación requerida** – Los participantes deben iniciar sesión.  
* **Permitir acceso de invitado** – Permitir que usuarios no registrados vean activos.  
* **Grabación Automática / Inicio Manual** – Elija si las reuniones se graban automáticamente o se inician manualmente.  
* **Requerir anfitrión** – El anfitrión debe admitir participantes; la reunión termina cuando el anfitrión se va.  
* **Permitir acceso de espectador** – Únase sin micrófono ni cámara; comuníquese a través del chat.  
* **Reuniones protegidas con contraseña** – Requiera una contraseña para unirse.  
* **Mostrar Pregunta de Ahorro de Viaje** – Pregunte a los participantes si la reunión redujo viajes.  

> La configuración se puede combinar (por ejemplo, sin anfitrión requerido pero protegido con contraseña).

---

#### 4.2.2 Activos

Administre todos los vídeos 360°/2D, imágenes y PDF. Cargue/descargue activos, asigne a espacios de trabajo, comparta con otros usuarios, renombre, imprima/descargue informes, active desenfoque de rostro y resumen de IA.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Elemento de Menú Principal Activos*

---

#### 4.2.3 Análisis

Proporciona información sobre reuniones, uso del espacio de trabajo y métricas de ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Descripción General de Análisis*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Actividad de Reuniones y Uso del Espacio de Trabajo*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de Licencia de Dispositivo y ROI*## 5. En el Sitio - Cómo Usar el Kit Llave en Mano de Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Primeros pasos
[Guía de inicio rápido – Kit llave en mano Avatour 3.1 (configuración de Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Siga la guía para desempacar, ensamblar y encender su cámara.

---### 5.2 Consejos útiles

#### Batería externa – Reuniones más largas y mejor regulación térmica

- **Si tu kit incluye una batería Ulanzi:** Conéctala entre la base del trípode y el palo extensible, luego conecta la batería a la cámara mediante USB-C.

- **Si tu kit incluye un palo de batería Telesin:** Monta la cámara directamente en el palo de batería extensible Telesin y conéctalo mediante USB-C.

Usando la batería externa:

1. Extiende la duración total de la batería de ~40 minutos (solo batería de cámara) a ~3 horas.
2. Añade estabilidad a la configuración de la cámara.
3. Ayuda a prevenir posibles sobrecalentamientos.

> Recomendamos usar siempre la batería externa desde el principio, especialmente para reuniones en directo.

#### Consideraciones de audio para reuniones en directo y grabaciones

- **Entornos ruidosos:**
  Utiliza los auriculares Shokz incluidos en tu kit para una captura de audio clara.
  - **Encender/Apagar:** Mantén presionado el botón "+" durante 3 segundos (LED azul = encendido, LED rojo = apagado).
  - **Modo de emparejamiento Bluetooth:** Con los auriculares apagados, mantén presionado el botón "+" durante 5 segundos (LED parpadea azul/rojo).
  - **Volumen:** Usa los botones "+" y "-".

- **Entornos más tranquilos / múltiples participantes cerca de la cámara:**
  Utiliza el altavoz con clip NoxGear. No tiene la misma alta fidelidad que los altavoces de conferencia (p. ej., Jabra Speak), pero es fácil de enganchar en tu camisa y captura las voces cercanas de manera efectiva.
  - **Encender/Apagar:** Mantén presionado el botón Reproducir/Pausa durante 2 segundos.
  - **Modo de emparejamiento Bluetooth:** Entra automáticamente en modo de emparejamiento al encenderse (LED parpadea azul/rojo; azul sólido cuando está emparejado).
  - **Volumen:** Usa los botones "+" y "-".

- **Usar tu propio dispositivo:** Si prefieres una alternativa (p. ej., un altavoz de conferencia o un auricular personal), puedes emparejarla a través de la cámara: Configuración → Bluetooth.

#### Conectividad, conectividad, conectividad
**Antes de comenzar:** Asegúrate de tener conexión a internet a través de:

- **WiFi local** (recomendado)
- **Red móvil** (si estás fuera del rango de WiFi)

**Ancho de banda recomendado:** 10 Mbps de subida/bajada para transmisión 360° completa (~5 Mbps). El ancho de banda más bajo (1–2 Mbps) solo funciona cuando estás inmóvil.

##### Prueba de velocidad de red
- **Prueba de ubicación única:** Cualquier verificador de velocidad que normalmente uses (p. ej., [Speedtest](https://www.speedtest.net)) para verificar el ancho de banda de subida.
- **Prueba de caminata en todo el sitio:** Desde la cámara: Configuración → Red → Prueba de conexión. Camina por todo el espacio para confirmar cobertura y ancho de banda.

##### WiFi local
- Altamente recomendado para conexiones estables.
- Si TI requiere whitelist, encuentra la dirección MAC: Configuración → Acerca de → Dirección WiFi.

##### Red móvil
**Opción A: Hotspot y SIM proporcionados en el kit**

- Conecta el hotspot GlocalMe al palo de batería Telesin (imán).
- Asegura que no haya interferencia y mantiene la conexión si te alejas de la cámara.
- Solución de problemas:
  - Confirma que la SIM preinstalada (no Cloud SIM).
  - Habilita 5G en SIM Card Manager.
  - Verifica que el APN sea correcto para tu región ([guía de configuración de APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opción B: Hotspot personal / SIM**
- Usa tu propio smartphone o un hotspot dedicado.

**Nota importante:**
> Mantén el hotspot apagado mientras estés conectado a WiFi; actívalo solo cuando estés fuera de rango. El sistema operativo de la cámara cambia dinámicamente entre redes WiFi según la intensidad de la señal y puede cambiar inadvertidamente al hotspot incluso cuando WiFi está disponible.

> Las redes móviles pueden limitar el ancho de banda de manera inesperada. Consulta con tu operador sobre los límites del plan de datos, o contacta al soporte de Avatour si usas nuestro hotspot y SIM.

##### Situaciones de bajo ancho de banda
- Pregrabación de videos de ubicación para reproducción posterior ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Comparte una transmisión de cámara de smartphone para complementar áreas con bajo ancho de banda (subida de 0,1–0,3 Mbps).

##### Sin conectividad
- Solo se puede usar video pregrabado ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Otros participantes en el sitio – Mejores prácticas

Cuando múltiples participantes se unen a una reunión en directo de Avatour desde la misma ubicación que la cámara 360°, el manejo cuidadoso del **audio y el ancho de banda** es crucial:

- Cada smartphone, tablet u ordenador portátil conectado en el sitio consume ancho de banda de red y puede afectar negativamente la transmisión de la cámara 360°.
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo que la experiencia de reunión sea desagradable para todos los participantes.

#### Otros participantes en el sitio – Mejores prácticas

Cuando múltiples participantes se unen a una reunión en directo de Avatour desde la misma ubicación que la cámara 360°, el manejo cuidadoso del **audio y el ancho de banda** es crucial:

- Cada smartphone, tablet u ordenador portátil conectado en el sitio consume ancho de banda de red y puede afectar negativamente la transmisión de la cámara 360°.
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo que la experiencia de reunión sea desagradable para todos los participantes.

Para abordar estos desafíos, sigue estas **mejores prácticas**:

- **Usa auriculares con cable o inalámbricos:** Preferiblemente con cancelación de ruido para prevenir eco y retroalimentación.
- **Modo en el sitio:** Únete a la reunión en modo En el sitio cuando estés físicamente cerca de la cámara 360°.
  - Este modo está optimizado para uso en el sitio:
    - Silencia el micrófono y el altavoz del participante por defecto.
    - **No** envía la transmisión de cámara del participante.
    - **No** muestra la transmisión de la cámara 360° en el navegador del participante.
    - Conserva ancho de banda de red, asegurando que la cámara 360° tenga el máximo disponible para la transmisión en directo.
    - Útil cuando un usuario quiere compartir detalles específicos; **puedes compartir tu cámara** para vistas dirigidas.
- **Silencia cuando no estés hablando activamente:** Previene retroalimentación de audio no deseada y distracciones.
- **Usa una red separada si es posible:** Ten tu smartphone conectado a una red diferente a la de la cámara para reducir interferencias.

Seguir estas directrices asegura un tour en directo suave y de alta calidad tanto para participantes en el sitio como remotos.### 5.3 Aplicación de Cámara Avatour

Aquí se encuentran (1) el menú de Nivel Superior, (2) Configuración y (3) menús de Configuración de Red.

![Avatour 360° Camera App - Three Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Aplicación de Cámara Avatour 360° - 3 Menús*

**Captura Rápida** - Para grabación de video 360° sin conexión. - Para una descripción detallada, consulte [¿Cómo se graban y cargan videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Recomendamos usar un dispositivo de audio externo (conectado vía bluetooth). Nota: También puede hacer videos y fotos estándar en 2D - simplemente cambie el modo entre 360° y 2D en la esquina inferior derecha una vez en la pantalla QC.

**Reunión en Directo** - Para videoconferencia en directo 360°. Verá sus espacios de trabajo y hacer clic en uno iniciará la transmisión de video en directo desde la cámara 360°. Antes de poder unirse a la reunión con su cámara 360°, debe conectar un dispositivo de audio vía bluetooth. Para una descripción detallada, consulte [¿Cómo iniciar una reunión de Captura en Directo con su cámara Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Al alojar una reunión de Captura en Directo con su cámara 360, tendrá herramientas de reunión similares disponibles que reflejan la experiencia web. Aquí hay un enlace a nuestro artículo de la Base de Conocimientos que explica estas herramientas con más detalle: [Herramientas de la Aplicación del Operador](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galería** - Encuentre aquí todos sus videos y fotos 360° para cargar en la Consola Web de Avatour.

**Configuración** - Dentro de Configuración, tiene las siguientes opciones:

- **Red**: Esta opción le permite cambiar a qué red WiFi está conectada la cámara o ejecutar una prueba de conexión de red para ver su rendimiento de transmisión
- **Captura en Directo**: Ajuste la configuración de Captura en Directo según el ancho de banda disponible, la sensibilidad de VR del invitado, o si los lentes protectores de su cámara están instalados:
  - **Velocidad de Fotogramas Objetivo**: Ajuste la velocidad de fotogramas para su video de Captura en Directo entre 15 fps, 24 fps y 30 fps. Las velocidades de fotogramas más altas producen un video más suave, pero requerirán más ancho de banda de carga. Predeterminado: 15 fps
  - **Velocidad de Bits Objetivo**: Le permite aumentar o disminuir la velocidad de bits de transmisión máxima para su Captura en Directo. Puede establecer su velocidad de bits objetivo entre 1 Mbps y 10 Mbps. Las velocidades de bits más altas resultarán en una resolución de video más alta, pero requerirán más ancho de banda de carga. Predeterminado: 5 Mbps
  - **Optimizar Movimiento**: Esto disminuirá la velocidad de fotogramas del video, generando menos carga en el ancho de banda de carga de su red, y aumentará su velocidad de bits de transmisión. Además, esta opción ayuda a reducir el mareo por movimiento para los participantes en VR. Predeterminado: Desactivado
  - **Lentes Protectores**: Esto afectará cómo se cose el video 360° dependiendo de si se han instalado lentes protectores en su cámara. Si no tiene lentes protectores, establezca esto en "No". Si recibió un Kit 3.0, tiene lentes protectores preinstalados y debe establecer esto en "Sí". Predeterminado: Sí

- **Captura Rápida**: Ajuste la configuración de Captura Rápida según su velocidad de fotogramas de video preferida, ancho de banda disponible para cargas de video grabadas, o si los lentes protectores de su cámara están instalados. Captura Rápida tiene una resolución establecida de 4k que generalmente logra un buen equilibrio entre calidad de video y tamaño de archivo. (Para resoluciones más altas, puede usar las aplicaciones nativas de la cámara, también en PanoX V2, para más detalles, consulte [¿Cómo se graban y cargan videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Velocidad de Fotogramas Objetivo**: Ajuste la velocidad de fotogramas para sus grabaciones de video de Captura Rápida entre 15 fps, 24 fps y 30 fps. Las velocidades de fotogramas más altas producen un video más suave, pero aumentarán el tamaño del archivo de video y el tiempo de carga. Recomendado: 30 fps
  - **Velocidad de Bits Objetivo**: Establezca la velocidad de bits objetivo para cargas de Captura Rápida entre 5 Mbps y 20 Mbps. Las velocidades de bits más bajas aumentan las velocidades de carga, pero disminuirán la calidad del video. Recomendado: 20 Mbps
  - **Lentes Protectores**: *Ver sección Lentes Protectores para Captura en Directo arriba*
- **Acerca de**: Ver número de serie del dispositivo y versión del software

**Cuenta** - Para iniciar sesión con su cuenta de host o administrador de Avatour.## 6. Consejo de Mejores Prácticas {#best-practice-advice}

### 6.1 Primeros usos (informales) y familiarización

Para sus primeros usos y familiarización con la Consola Web de Avatour y el Kit Llave en Mano de Avatour recomendamos los siguientes pasos:

1. Lleve el kit a casa y juegue con él con familia y amigos usando su conexión a internet del hogar.
2. Lleve el kit a la oficina y conéctese a una red corporativa (podrían surgir problemas corporativos, p. ej. firewalls corporativos - pero ya sabe del paso uno que Avatour está funcionando y este es un tema a resolver por su equipo de TI con la ayuda de Avatour).
3. Comience a usar Avatour en el lugar (fuera de su oficina) en la ubicación de la reunión a la que los participantes remotos generalmente necesitarían viajar. Podrían surgir más temas de conectividad. Avatour ayudará en cooperación con su equipo de TI.
4. Comience a usar con participantes remotos internos y externos.### 6.2 Antes de una reunión de video en directo en 360°

- Recomendamos hacer un recorrido de video en 360° grabado antes de cualquier recorrido en directo si el tiempo lo permite, por tres razones: (1) Tener una solución de respaldo para el recorrido en directo, (2) tener algo para documentación y revisión posterior (además del recorrido en directo grabado) y (3) comenzar a crear una biblioteca de videos en 360° de todos sus sitios que puede ser útil para muchos casos de uso.
- Todos los componentes del kit deben estar cargados durante al menos 90 minutos antes de la reunión en directo. De todas formas, recomendamos tener todos los dispositivos en carga continua cuando no estén en uso. De esta manera, todos los dispositivos siempre estarán listos, también para reuniones ad hoc no planificadas.
- Tener el kit completamente ensamblado (1. base del trípode + 2. batería Ulanzi + 3. palo extensible + 4. cámara 360°).

- Confirmar que se ha creado un Workspace para albergar una reunión en directo e incluir todos los Assets relevantes.

- Invitar a todos los participantes a la reunión a través de su Workspace. Esto crea una invitación en los calendarios de todos los participantes e incluye el enlace de invitación a la reunión.

- Emparejar y conectar los auriculares Bluetooth o altavoz que planea usar para su recorrido a la cámara.

- Todos los usuarios de smartphone en el sitio deben conectarse desde una red diferente a la red de la cámara. Esto reducirá la carga en el ancho de banda de la red de la cámara.

- Si es el único operador de cámara, lleve un smartphone con usted en caso de que desee compartir la cámara del smartphone y mostrar detalles finos.

- Confirmar que la cámara 360 pueda conectarse a su WiFi local.

- Antes de una reunión Avatour, planifique la ruta que seguirá a través de la instalación. Realice una reunión Avatour de prueba con la cámara y verifique que todas las áreas tengan tasas de bits superiores a 1 Mbps de ancho de banda. Esto se puede ver en la pantalla de la cámara en sí, o como participante remoto yendo a Configuración y activando Mostrar tasa de bits.

- Si observa que algunas áreas tienen poco o ningún ancho de banda, es mejor tomar imágenes o una grabación. Estas se pueden presentar durante la reunión para que los participantes remotos las revisen. Puede seguir la guía aquí que explica nuestra Captura rápida para grabar y cargar videos/imágenes: [¿Cómo graba y carga videos en 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si tiene participantes remotos que se unan a la reunión que no hayan usado Avatour antes, proporcióneles un breve resumen de la plataforma, su funcionalidad (video en directo en 360°, assets, capturas de pantalla, anotaciones, spotlight) y las herramientas de reunión.

- Puede comenzar en otra solución de videoconferencia (p. ej., Teams, Zoom, Google Meet), pero antes de cambiar a Avatour, cierre completamente la otra aplicación de videoconferencia. En algunos casos, estas otras aplicaciones priorizarán el micrófono/altavoces/cámara web de su dispositivo, haciendo que se deshabiliten para Avatour. Además, NO ejecute Avatour Y otra videoconferencia al mismo tiempo, ya que esto reducirá el ancho de banda disponible.

- Si planea usar la cámara 360 en un entorno de alta temperatura, se recomienda usar el módulo de enfriamiento (solo Pilot Pano). Esto ayudará a reducir las posibilidades de que la cámara se sobrecaliente y se apague automáticamente.### 6.3 Al Operar la Cámara en el Sitio para una Reunión de Video en Vivo de 360°

- Al operar la cámara, asegúrate de caminar lentamente. Esto ayuda con la calidad del video y reduce cualquier posible tiempo de inactividad de video cuando la conexión de red de la cámara cambia entre puntos de acceso WiFi.

- Sostén la cámara frente a ti y por encima del nivel de los ojos. Esto permite que todos los participantes remotos vean la mayoría de tu área circundante.

- Para casos en los que la cámara necesite permanecer estable, utiliza el soporte de trípode y extiende la cámara a la altura correcta, preferiblemente a la altura de los ojos.

- Siempre conecta la cámara a tu red WiFi local cuando sea posible. Para áreas sin acceso a WiFi, utiliza el punto de acceso proporcionado. El punto de acceso tiene una tarjeta SIM que se conectará a una red celular confiable cerca de ti. Siempre mantén el punto de acceso apagado cuando no esté en uso en interiores, de lo contrario la cámara de 360° podría conectarse al punto de acceso, lo cual no queremos en interiores. Cuando estés en exteriores, mantén el punto de acceso cerca de la cámara de 360°.

- Cuando la velocidad de bits en cámara comienza a caer por debajo de 2 Mbps, camina más lentamente o detente completamente hasta que la señal se estabilice nuevamente. Esto generalmente sucede cuando cambias de un Punto de Acceso WiFi a otro.

- Si sabes que la conectividad y el video se perderán al moverse a una ubicación específica (Ejemplo: cambiar de un área de producción interior a un área exterior), notifica a los participantes remotos con anticipación.

- Si necesitas mostrar algo con alto detalle o texto pequeño, utiliza tu propio smartphone o el de un participante en el sitio para unirte a la reunión y presenta tu / su cámara trasera del teléfono.

- Si es posible, recomendamos que una persona adicional esté en el sitio para ayudar con el uso compartido de cámara de smartphone descrito anteriormente, ya que esto a menudo resulta ser útil / necesario.

- Idealmente, los usuarios de smartphone en el sitio deben unirse a la reunión (1) en modo en el sitio y (2) en una red diferente a la que utiliza la cámara para no quitarle ancho de banda de carga crucial a la cámara de 360°.

- Todos los participantes en el sitio que se unan desde su smartphone deben estar silenciados, a menos que estén hablando activamente.