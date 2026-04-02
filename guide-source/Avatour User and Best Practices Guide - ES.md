# Avatour User and Best Practices Guide

## 1. Para todos los usuarios de Avatour {#for-all-avatour-users}
Si es nuevo en Avatour, los siguientes recursos proporcionan una introducción útil a la plataforma y sus capacidades:

1. [Video de cómo funciona Avatour](https://avatour.com/how-it-works)  
Una descripción general breve de las características principales de Avatour y cómo la plataforma permite la colaboración remota inmersiva.
2. [Preguntas frecuentes](https://avatour.com/faqs)  
Respuestas a preguntas frecuentes.
3. [Glosario](https://avatour.com/glossary)  
Definiciones de términos y conceptos clave de Avatour que se utilizan frecuentemente.
4. Sitio web  
Observe especialmente la página [Características de Avatour](https://avatour.com/features) junto con las secciones dedicadas de Casos de uso e Industrias para conocer cómo Avatour puede satisfacer sus necesidades específicas.## 2. Tipos de Usuario de Avatour  {#avatour-user-types}

### 2.1 Asistentes a la reunión (No se requiere cuenta)
Los usuarios pueden unirse a la reunión sin registrarse en una cuenta de Avatour.
Excepción: Si el anfitrión ha restringido la reunión a usuarios registrados, por ejemplo, para permitir que solo los empleados internos se unan a través del inicio de sesión único (SSO), la invitación del calendario indicará que los participantes deben iniciar sesión para autenticarse.

Los usuarios acceden a la reunión de la siguiente manera:

- Recibir una invitación del calendario del anfitrión.
- Usar el enlace de la reunión en la invitación para unirse.
- Ingresar una contraseña de reunión si el anfitrión ha habilitado una.
- Los participantes pueden unirse sin una cuenta de Avatour a menos que la reunión esté restringida y requiera iniciar sesión para autenticarse.

#### 2.1.1 Participante

- Puede unirse e interactuar completamente (cámara web, micrófono, chat y funcionalidad de presentación).
- Máximo de 20 participantes interactivos por reunión.

#### 2.1.2 Espectador

- Puede ver la reunión y participar solo a través del chat.
- No puede compartir video, usar micrófono, presentar, reproducir/pausar activos o capturar instantáneas.
- Máximo de 10 espectadores por reunión.
- Junto con los participantes, una reunión puede albergar hasta 30 asistentes.### 2.2 Usuarios Registrados

Los Usuarios Registrados tienen una cuenta de Avatour. Las cuentas se crean de una de las siguientes formas:

- **Invitación de Admin:** Durante la incorporación, Avatour configura un **inquilino dedicado** para la organización y crea una o más **cuentas de Admin**. Los Admins pueden **invitar usuarios** dentro de la organización y asignarlos a **grupos**, que definen su rol en la plataforma (Guest, Host o Admin). Los usuarios invitados reciben un **enlace de registro** para completar la configuración de la cuenta y establecer una contraseña.  
- **Invitación de Host:** Los Hosts pueden añadir usuarios como **colaboradores de Editor** a un Workspace. Esto consume una **licencia de Host** y asegura que el usuario tenga acceso de nivel Host.  
- **Aprovisionamiento automático de SSO (solo nivel Enterprise/Business):** Las cuentas pueden ser creadas automáticamente por el IdP. De forma predeterminada, las cuentas aprovisionadas por SSO se añaden al **grupo Guest**, a menos que se anulen mediante **asignaciones de grupos SAML**. Los Admins aún pueden invitar usuarios y asignar pertenencia a grupos directamente incluso cuando SSO está habilitado.

**Resumen:**  

Los usuarios registrados y su pertenencia a grupos se pueden gestionar de varias formas:

- **Gestión de Admin:** Un Admin en la consola de Avatour puede crear usuarios y asignarlos a grupos, que definen su rol en la plataforma (Guest, Host o Admin).  
- **Aprovisionamiento de SSO:** Para clientes de nivel Enterprise o Business con SSO habilitado, el IdP puede aprovisionar automáticamente cuentas y asignar pertenencia a grupos, lo que define el rol de plataforma del usuario.  
- **Usuarios invitados por Host:** Los Hosts pueden invitar a otros usuarios como colaboradores de Editor a Workspaces específicos. Asignar el rol de colaborador de Editor consume una licencia de Host.

**Práctica Recomendada (Clientes Enterprise):**  
Para organizaciones que esperan un gran número de usuarios que necesitan acceso a Avatour, se recomienda **integrar Single Sign-On (SSO)** y gestionar usuarios y pertenencias a grupos desde el **IdP**. Este enfoque simplifica el aprovisionamiento de cuentas, la asignación de grupos y la gestión de licencias, reduciendo la sobrecarga administrativa y garantizando un control de acceso consistente.

#### 2.2.1 Usuarios Guest

- Añadidos al **grupo Guest**.  
- Pueden **ver Assets** dentro de Workspaces donde han sido añadidos como **colaboradores Viewer**.  
- No pueden crear workspaces, alojar reuniones o cargar contenido.  
- Las cuentas Guest aprovisionadas por SSO **se autentican a través del IdP**; no se requiere contraseña gestionada por Avatour.

---

#### 2.2.2 Usuarios Licenciados (Acceso a Consola Web)

##### Usuarios Host (Grupo: Host)

- Pueden crear/gestionar Workspaces, invitar colaboradores a un workspace, **alojar reuniones en directo**, cargar **Quick Captures**.  
- Tienen acceso al **Host Dashboard** y **Operator App** en cámaras 360° compatibles.  

##### Usuarios Admin (Grupo: Admin)

- Incluye todas las capacidades de Host más administración completa de cuentas.

**Los privilegios de Admin adicionales incluyen:**

**Gestión de Cuentas**  

- Crear nuevos usuarios y asignarlos a grupos.
- Restablecer contraseñas cuando las gestiona Avatour (no aplicable cuando SSO está habilitado). 
- Actualizar usuarios Guest a Host.  
- Desactivar usuarios (las cuentas de Admin deben convertirse primero a Host antes de su eliminación).  
- Transferir assets de un usuario Host a otro durante la eliminación.

**Configuración**  

- Configurar **ajustes de seguridad de toda la organización** para assets, workspaces y reuniones alojadas en la plataforma (por ejemplo, si un Host debe estar presente para iniciar una reunión, si los rostros deben difuminarse en todos los vídeos cargados en la plataforma).  
- Habilitar o deshabilitar **funciones de IA** o **grabación**.  
- Aplicar marca corporativa de forma consistente en toda la plataforma si se configura un **dominio personalizado**.
  

**Assets y Análisis** 
 
- Ver todos los Assets cargados por cualquier usuario en la organización.  
- Revisar el uso de la plataforma en toda la organización.

---

#### 2.2.3 Permisos de Colaborador de Workspace

Los permisos de Workspace definen qué puede hacer un usuario **dentro de un Workspace específico**. Estos son independientes de la pertenencia a grupos de nivel de plataforma (Guest, Host, Admin).

- **Colaborador de Editor:** Los usuarios con este permiso pueden:
  - Gestionar Assets (cargar, eliminar, difuminar rostros, generar resúmenes)  
  - Gestionar ajustes de reuniones (habilitar/deshabilitar grabación, permitir o eliminar participantes)  
  - Programar y alojar reuniones en directo  
  - Generar informes basados en plantillas predefinidas  
  - Añadir o eliminar colaboradores del Workspace  

- **Colaborador de Viewer:** Los usuarios con este permiso tienen acceso de solo lectura a los Assets del Workspace. **No pueden modificar Assets, gestionar reuniones ni gestionar colaboradores**, pero **pueden crear Notas en Assets**.## 3. Para participantes de reuniones remotas y visitantes del espacio de trabajo {#for-remote-meeting-participants-and-workspace-visitors}
Avatour permite que los usuarios colaboren de dos formas principales:

- **Unirse a una reunión de Avatour (Colaboración síncrona):**  
  Puede recibir una **invitación de calendario** para unirse a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota en directo** o revisar conjuntamente los activos de forma síncrona.

- **Visitar un Workspace (Colaboración asíncrona):**  
  También puede ser invitado como **colaborador en un Workspace** para revisar activos de **forma asíncrona** (en su propio horario).### 3.1 Cómo unirse a una reunión de Avatour y visitar un espacio de trabajo de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Cualquier dispositivo "pantalla plana" con navegador web {#any-flat-screen}
Puede unirse a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, smartphone o tablet** utilizando un navegador web.

##### Unirse a una reunión de Avatour

> **Nota:** Unirse a una reunión de Avatour requiere que **otorgue permisos de micrófono**. Por favor, acepte cualquier solicitud de permisos de su navegador.

1. **A través de invitación de calendario (recomendado):**
   - Normalmente recibirá una **invitación de calendario** con un **enlace de acceso directo** (por ejemplo: `https://avatour.live/join?s=xxxxx`).
   - Hacer clic en el enlace completará automáticamente el **código de reunión de 5 caracteres** y lo llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que debe **iniciar sesión para acceder a la reunión**.
   - **Reuniones protegidas con contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debe ingresar para unirse.

2. **A través del código de reunión:**
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, vaya a [https://avatour.live/join](https://avatour.live/join), ingrese su **nombre** y el **código de reunión**, y únase a la reunión.
   - Si la reunión está **protegida con contraseña**, ingrese la contraseña proporcionada por el anfitrión.
   - Si la reunión requiere **autenticación**, deberá **iniciar sesión con su cuenta de Avatour** antes de unirse.

> **Consejo 1:** Si su cámara o micrófono no funciona, es posible que esté siendo utilizado por otra aplicación (por ejemplo, Microsoft Teams o Zoom). Cierre cualquier aplicación que pueda estar usando su cámara o micrófono, luego salga y vuelva a unirse a la reunión de Avatour.

> **Consejo 2:** Si aún no puede unirse a la reunión, ejecute esta prueba: [https://avatour.live/test](https://avatour.live/test).
> La prueba puede identificar si su **firewall corporativo o red** está bloqueando el acceso, y proporcionará información para guiar discusiones con su equipo de TI.

> **Consejo 3:** **No** use las aplicaciones Avatour para iOS o Android para unirse a reuniones. Estas aplicaciones solo son necesarias cuando **transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar el software Avatour 360° directamente y requieren un smartphone para asistir.

##### Visitar un espacio de trabajo de Avatour (sin unirse a una reunión de Avatour)

Puede acceder a un espacio de trabajo de las siguientes maneras:

- **Espacio de trabajo público:**
  Si el espacio de trabajo es público, el enlace se puede acceder directamente, sin necesidad de iniciar sesión.

- **Espacio de trabajo restringido:**
  Si el espacio de trabajo está restringido, debe ser agregado como **colaborador** con permisos de **Editor** o **Visualizador**.

  1. Cuando se le agregue como colaborador, recibirá una **notificación por correo electrónico** con un enlace al espacio de trabajo.
  2. Haga clic en el enlace en el correo para abrir el espacio de trabajo. Si aún no ha iniciado sesión, se le pedirá que **inicie sesión o complete el registro**.
  3. Una vez que haya iniciado sesión, el espacio de trabajo se abrirá automáticamente.

  Alternativamente, puede iniciar sesión en [https://avatour.live/login](https://avatour.live/login) y acceder al espacio de trabajo desde su **lista de espacios de trabajo**.

#### 3.1.2 Casco de realidad virtual {#vr-headset}
Puede unirse a una reunión y visitar un espacio de trabajo desde una variedad de cascos Meta y Pico compatibles. Para hacer esto:

1. Instale nuestra aplicación Avatour desde su respectiva tienda de aplicaciones de realidad virtual: [Cómo instalar la aplicación Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Cargue nuestra aplicación e ingrese el código de reunión o seleccione un espacio de trabajo para unirse a una reunión. Para obtener más información sobre cómo usar nuestra aplicación de realidad virtual, consulte nuestro artículo de la base de conocimientos [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Herramientas de Reunión y Colaboración en Espacios de Trabajo {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (síncronas):** Colabora en tiempo real con otros participantes, incluidas visitas en vivo o revisión conjunta de activos grabados.  
2. **Espacios de trabajo (asíncronos):** Revisa e interactúa con activos según tu horario, 24/7.

Las **herramientas de colaboración son mayormente similares** entre reuniones y espacios de trabajo, con algunas diferencias debido al contexto síncrono vs asíncrono.

#### 3.2.1 Diseño de la Interfaz

La interfaz de Avatour se organiza en torno a tres áreas principales:

- **Panel izquierdo** – Activos del espacio de trabajo y herramientas de apoyo  
- **Lienzo central** – Área de visualización principal para vídeo en vivo o activos  
- **Panel derecho** – Información contextual, como participantes, reuniones o chat  

La mayoría de las interacciones se inician desde el **menú inferior**.  
Hacer clic en una opción del menú abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **lienzo central** permanece como área de visualización principal.

---
#### 3.2.2 Ejemplo de Vista de Reunión

Aquí hay un ejemplo de una vista en una Reunión de Avatour:

![Interfaz de Usuario de Reunión de Avatour con Panel de Activos, Lienzo en Blanco y Panel de Participantes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Reunión de Avatour con Panel de Activos (izquierda), Lienzo (centro) y Panel de Participantes (derecha)*

---

#### 3.2.3 Ejemplo de Vista de Espacio de Trabajo

Aquí hay un ejemplo de una vista de Espacio de Trabajo:

![Espacio de Trabajo de Avatour con Panel de Activos, Lienzo en Blanco y Panel de Reuniones](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espacio de Trabajo de Avatour con Panel de Activos (izquierda), Lienzo (centro) y Panel de Reuniones (derecha)*

---

#### 3.2.4 Descripción General del Menú Inferior

El menú inferior proporciona acceso a los controles de interfaz principales y los paneles:

**Menú Inferior de Reunión**  

![Menú Inferior de Reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menú Inferior de Reunión de Avatour*

- **Activos** – Revisa archivos del espacio de trabajo, incluidos vídeos grabados, imágenes, capturas de pantalla y PDF. 
- **Chat** – Envía mensajes a todos los participantes de la reunión.  
- **Cámara** – Enciende o apaga tu cámara web.  
- **Micrófono** – Silencia o activa el micrófono.  
- **Presentar** – Presenta un activo, escritorio o feed de cámara web (ver sección Presentar abajo).  
- **Herramientas del Anfitrión** (solo para anfitriones):  
  - **Bloquear Enfoque** – Bloquea la vista para todos los participantes.  
  - **Silenciar a Todos** – Silencia a todos los participantes.  
- **Activar Pantalla Completa** – Pone la pestaña de reunión en pantalla completa.  
- **Salir de la Reunión** – Abandona la reunión.  
- **Iniciar Grabación** – Usa este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones se pueden grabar automáticamente si **auto-start recording** está habilitado en la configuración del espacio de trabajo. En ambos casos, las grabaciones se guardan en los activos del espacio de trabajo.
- **Mapa** – Abre o cierra el panel de mapa para activos con una pista GPS. Hacer clic en una ubicación salta al punto exacto en el vídeo. El mapa se actualiza en vivo mientras se reproduce el vídeo.
- **Participantes** – Abre o cierra el panel de participantes.  
- **Información de Reunión** – Ver el código de reunión, enlace de invitación y acceder a tutoriales relacionados.  

![Información de Reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panel Lateral de Información de Reunión de Avatour*

- **Configuración** – Ajusta la configuración de idioma, audio y vídeo. Para reuniones de vídeo 360° en vivo, utiliza **Show Bitrate** para monitorear estadísticas de conectividad.

> Consejo: Envía el enlace de la reunión o añádelo a un elemento del calendario para invitar a los participantes.

---

##### Menú Presentar

La opción **Presentar** en el menú inferior de la reunión te permite compartir contenido con todos los participantes.

- **Cámara** – Comparte la cámara de tu smartphone/tableta. Esto también se puede usar durante una reunión de vídeo 360° en vivo para superponer una vista secundaria para primeros planos o detalles específicos. 
- **Escritorio** – Comparte tu pantalla de escritorio con todos los participantes.  
- **Activo** – Presenta un activo del espacio de trabajo. Seleccionar un activo abre la **Barra de Herramientas de Activos**, que proporciona controles de reproducción y herramientas de colaboración específicas del activo que se está presentando.

##### Barra de Herramientas de Activos (Reunión)

Al presentar un activo en una reunión, la **Barra de Herramientas de Activos** aparece encima del lienzo. Aquí están las herramientas y elementos del menú disponibles cuando <u>presentas un Activo en una Reunión</u> - explicadas de izquierda a derecha.

![Menú de Avatour mientras se Presenta un Activo en una Reunión](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour al presentar un Activo en una Reunión*


- **Línea de Tiempo de Vídeo / Barra de Progreso** – Muestra el progreso del vídeo con notas y temas clave extraídos del audio. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.   
- **Captura de Pantalla** – Captura una imagen 360° o 2D del activo.  
- **Destacar** – Resalta un área específica para todos los participantes durante sesiones en vivo.  
- **Mostrar/Ocultar Punto de Vista (POV)** – Muestra hacia dónde está mirando cada participante en el vídeo 360°.  
- **Notas** – Crea notas ancladas a momentos específicos en el activo. Las notas se pueden categorizar (Observación, Problema, Acción, Recomendación), rastrear por estado (Abierto → En Progreso → Resuelto) y compartir mediante enlaces directos.  

  ![Nota de Avatour y Filtros de Notas](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota de Avatour y Filtros de Notas*

  - **Notas por Comando de Voz** – Estos son marcadores de posición generados automáticamente cuando la grabación detecta menciones como "insertar nota", "tomar una nota" o "hacer una nota". Estas notas aparecen en la línea de tiempo y necesitan ser **posicionadas y finalizadas** por el usuario. 

  ![Notas de Avatour - Generadas por Comando de Voz](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por Comando de Voz*

- **Panel de Notas y Resumen** – Abre un panel lateral que muestra todas las notas, temas clave y un resumen ejecutivo del activo. Hacer clic en un elemento te lleva a ese momento en el vídeo.  

  ![Resumen Ejecutivo de Activo de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen Ejecutivo de Avatour al presentar un Activo en una Reunión*

  ![Temas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Temas de Avatour al presentar un Activo en una Reunión*

  Desde el **Panel Lateral**, puedes **imprimir un informe de activos** o **descargarlo como TXT o CSV**. Los informes pueden incluir notas, temas generados por IA y transcripciones completas. También puedes **elegir qué elementos incluir** antes de exportar.  

  ![Menús de Impresión de Informe de Activos de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menús de Impresión / Descarga de Informe de Activos de Avatour*  

  ![Menú de Selección de Elementos de Informe de Activos de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menú de Selección de Elementos de Informe de Activos de Avatour*

- **Enlace Compartido** – Comparte un enlace a una nota o escena específica en el activo.  
- **Subtítulos Cerrados (CC)** – Muestra la transcripción de texto en pantalla durante la reproducción de vídeo.

##### Barra de Herramientas de Activos (Espacio de Trabajo)

Al revisar un activo en un espacio de trabajo, la barra de herramientas es similar pero optimizada para uso individual:

![Menú de Avatour al Presentar un Activo fuera de una reunión, p. ej. al visitar un espacio de trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menú de Avatour al presentar un Activo en un Espacio de Trabajo*

- **Línea de Tiempo de Vídeo / Barra de Progreso** – Muestra el progreso del vídeo con notas y temas clave extraídos de la pista de audio. Haz clic en cualquier lugar de la línea de tiempo para desplazarte por el vídeo. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.  
- **Captura de Pantalla, Notas, Panel de Notas y Resumen, Enlace Compartido, Subtítulos Cerrados**  
- No disponible: **Destacar, POV** (estos requieren participantes en vivo)  
- Controles adicionales:
  - **Pasos de 10 segundos** – Salta adelante/atrás  
  - **Velocidad de Reproducción** – Ajusta la velocidad (0.5×–2×)  
  - **Recortar Vídeo** – Recorta el principio o el final del activo## 4. Para Usuarios Host y Admin - Consola Web Avatour {#for-host-and-admin-users-avatour-web-console}
Cuando inicie sesión en su Cuenta de Usuario de Avatour, accederá a la **Consola Web**.### 4.1 Consola Web - Menú Principal de Descripción General {#web-console-overview-main-menu}

En el lado izquierdo, verá los siguientes elementos del menú:

![Consola Web Avatour - Menú Principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Consola Web Avatour - Menú Principal*

- **Espacios de trabajo** – Organice su contenido de manera eficiente. Cada espacio de trabajo contiene **Activos**, **Colaboradores**, **Reuniones** y **Configuración**.  
- **Activos** – Acceda y gestione todos sus activos (videos, imágenes, PDF). Los administradores pueden ver todos los activos de la cuenta, y los activos compartidos son visibles para todos los usuarios.  
- **Perfil** – Gestione su idioma y contraseña.  
- **Análisis** – Realice un seguimiento de la actividad de sesión, el uso del espacio de trabajo y las métricas de ROI.  
- **Configuración** *(Solo administrador)* – Configure los valores predeterminados de espacio de trabajo, reunión y activos en toda la organización. Los administradores también pueden personalizar la marca (logo, colores, fondos).  
- **Cuenta** *(Solo administrador)* – Gestione usuarios registrados y cámaras 360°.  
- **Inicio de sesión del dispositivo** – Ingrese el código mostrado en su cámara 360° para emparejarla con su cuenta.  
- **Tutoriales** – Acceda a tutoriales guiados.  
- **Cerrar sesión** – Cierre sesión en la consola.

> Las secciones como Perfil, Inicio de sesión del dispositivo, Tutoriales y Cerrar sesión son autoexplicativas y no tienen subsecciones detalladas.

---### 4.2 Consola Web - Detalles por Elemento de Menú (con imágenes) {#web-console-details-by-menu-item}

#### 4.2.1 Espacios de Trabajo

Los espacios de trabajo son unidades organizativas flexibles que te permiten gestionar activos, colaboradores y reuniones en un solo lugar. Puedes crear un nuevo espacio de trabajo con el botón **Nuevo Espacio de Trabajo** en la esquina superior derecha.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web Avatour - Elemento de Menú Principal Espacios de Trabajo*

Haz clic en el icono de campana para ver un resumen de la actividad del espacio de trabajo durante los últimos 7 días.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Actividades Recientes del Espacio de Trabajo*

Dentro de un espacio de trabajo:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espacio de Trabajo con Activos (izquierda), Lienzo (centro), Reuniones (derecha)*

- **Activos** – Gestiona archivos asignados a este espacio de trabajo.  
- **Colaboradores** – 
  Controla el acceso a espacios de trabajo mediante 
  - **Espectador** – Puede ver activos. La invitación crea un usuario Invitado si es necesario.  
  - **Editor** – Control total del espacio de trabajo, los mismos derechos que el Anfitrión. La invitación actualiza el usuario a Anfitrión si es necesario.  
> Múltiples usuarios pueden acceder a un espacio de trabajo simultáneamente sin una reunión. Los espacios de trabajo públicos y la configuración de acceso a reuniones proporcionan acceso alternativo.  
- **Informe** – Genera un informe usando una plantilla de lista de verificación en los activos del espacio de trabajo seleccionado.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe del Espacio de Trabajo y Selección de Activos*

- **Mapa** – Muestra las ubicaciones de los activos habilitados para GPS en un mapa.  
- **Reuniones** – Organiza reuniones en el espacio de trabajo.  
- **Configuración** – Configura valores predeterminados del espacio de trabajo y reuniones:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Configuración del Espacio de Trabajo*

**Configuración del Espacio de Trabajo**

- **Plantilla de Informe** – Selecciona plantilla de lista de verificación para informes de IA.  
- **Habilitar Notificaciones** – Correos electrónicos de resumen diario para cambios de estado de notas.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Ejemplo de Notificaciones por Correo Electrónico*

- **Espacio de Trabajo Público** – Cualquier persona con el enlace puede ver activos directamente.

**Configuración de Reuniones**
  
* **Se requiere autenticación** – Los participantes deben iniciar sesión.  
* **Permitir acceso de invitados** – Permite que usuarios no registrados vean activos.  
* **Grabación Automática / Inicio Manual** – Elige si las reuniones se graban automáticamente o se inician manualmente.  
* **Requerir anfitrión** – El anfitrión debe admitir participantes; la reunión termina cuando el anfitrión se va.  
* **Permitir acceso de espectador** – Únete sin micrófono ni cámara; comunícate a través del chat.  
* **Reuniones protegidas con contraseña** – Se requiere contraseña para unirse.  
* **Mostrar Pregunta sobre Ahorro de Viajes** – Pregunta a los participantes si la reunión redujo viajes.  

> La configuración se puede combinar (por ejemplo, sin anfitrión requerido pero protegida con contraseña).

---

#### 4.2.2 Activos

Gestiona todos los vídeos 360°/2D, imágenes y PDF. Carga/descarga activos, asigna a espacios de trabajo, comparte con otros usuarios, renombra, imprime/descarga informes, activa desenfoque de rostros y resumen de IA.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Elemento de Menú Principal Activos*

---

#### 4.2.3 Analítica

Proporciona información sobre reuniones, uso del espacio de trabajo y métricas de ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Descripción General de Analítica*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Actividad de Reuniones y Uso del Espacio de Trabajo*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de Licencias de Dispositivos y ROI*## 5. En el sitio - Cómo usar el kit llave en mano de Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Primeros pasos
[Guía de inicio rápido – Kit llave en mano Avatour 3.1 (Configuración de Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Sigue la guía para desempacar, ensamblar y encender tu cámara.

---### 5.2 Consejos Útiles

#### Batería Externa – Reuniones Más Largas y Mejor Térmica

- **Si tu kit incluye una batería Ulanzi:** Adjúntala entre la base del trípode y la varilla extensible, luego conecta la batería a la cámara mediante USB-C.

- **Si tu kit incluye una batería Telesin:** Monta la cámara directamente en la varilla extensible con batería Telesin y conéctala mediante USB-C.

Usando la batería externa:

1. Extiende la vida útil total de la batería de ~40 minutos (solo batería de la cámara) a ~3 horas.
2. Añade estabilidad a la configuración de la cámara.
3. Ayuda a prevenir posibles sobrecalentamientos.

> Recomendamos usar siempre la batería externa desde el inicio, especialmente para reuniones en directo.

#### Consideraciones de Audio para Reuniones en Directo y Grabaciones

- **Entornos ruidosos:**
  Usa los auriculares Shokz incluidos en tu kit para captura clara de audio.
  - **Encender/Apagar:** Mantén presionado el botón "+" durante 3 segundos (LED azul = encendido, LED rojo = apagado).
  - **Modo Emparejamiento Bluetooth:** Mientras los auriculares están apagados, mantén presionado el botón "+" durante 5 segundos (LED parpadea azul/rojo).
  - **Volumen:** Usa los botones "+" y "-".

- **Entornos más tranquilos / múltiples participantes cerca de la cámara:**
  Usa el altavoz NoxGear clip-on. No tiene la alta fidelidad de altavoces de conferencia (p. ej., Jabra Speak), pero es fácil de enganchar a tu camisa y captura voces cercanas de manera efectiva.
  - **Encender/Apagar:** Mantén presionado el botón Play/Pausa durante 2 segundos.
  - **Modo Emparejamiento Bluetooth:** Entra automáticamente en modo emparejamiento cuando se enciende (LED parpadea azul/rojo; azul sólido cuando está emparejado).
  - **Volumen:** Usa los botones "+" y "-".

- **Usando tu propio dispositivo:** Si prefieres una alternativa (p. ej., un altavoz de conferencia o auriculares personales), puedes emparejarla a través de la cámara: Configuración → Bluetooth.

#### Conectividad, Conectividad, Conectividad
**Antes de comenzar:** Asegúrate la conexión a internet a través de:

- **WiFi Local** (preferido)
- **Red Móvil** (si está fuera del rango de WiFi)

**Ancho de banda recomendado:** 10 Mbps de subida/descarga para transmisión completa en 360° (~5 Mbps). Menor ancho de banda (1–2 Mbps) solo funciona cuando estás quieto.

##### Prueba de Velocidad de Red
- **Prueba en una ubicación:** Cualquier comprobador de velocidad que uses normalmente (p. ej., [Speedtest](https://www.speedtest.net)) para verificar el ancho de banda de subida.
- **Prueba caminando por el sitio:** Desde la cámara: Configuración → Red → Prueba de Conexión. Camina por todo el espacio para confirmar cobertura y ancho de banda.

##### WiFi Local
- Altamente recomendado para conexiones estables.
- Si TI requiere lista blanca, encuentra la dirección MAC: Configuración → Acerca de → Dirección WiFi.

##### Red Móvil
**Opción A: Hotspot y SIM proporcionados en el kit**

- Adjunta el hotspot GlocalMe a la batería Telesin (imán).
- Asegura sin interferencias y mantiene la conexión si te alejas de la cámara.
- Solución de problemas:
  - Confirma SIM preinstalada (no Cloud SIM).
  - Habilita 5G en Administrador de Tarjeta SIM.
  - Verifica APN correcto para tu región ([guía de configuración APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opción B: Hotspot personal / SIM**
- Usa tu propio smartphone o hotspot dedicado.

**Nota Importante:**
> Mantén el hotspot apagado mientras estés conectado a WiFi; actívalo solo cuando estés fuera de rango. El sistema operativo de la cámara cambia dinámicamente entre redes WiFi según la intensidad de la señal y puede cambiar inadvertidamente al hotspot incluso cuando WiFi está disponible.

> Las redes móviles pueden reducir el ancho de banda inesperadamente. Consulta con tu operador sobre los límites del plan de datos, o contacta al soporte de Avatour si usas nuestro hotspot y SIM.

##### Situaciones de Bajo Ancho de Banda
- Pregrabación de vídeos de ubicación para reproducción posterior ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).
- Comparte una transmisión de cámara de smartphone para complementar áreas con bajo ancho de banda (0,1–0,3 Mbps de subida).

##### Sin Conectividad
- Solo se puede usar vídeo pregrabado ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Otros Participantes en Sitio – Mejores Prácticas

Cuando múltiples participantes se unen a una reunión en directo de Avatour desde la misma ubicación que la cámara 360°, la gestión cuidadosa del **audio y ancho de banda** es crucial:

- Cada smartphone, tablet u ordenador portátil conectado en sitio consume ancho de banda de red y puede afectar negativamente a la transmisión de la cámara 360°.
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo la experiencia de la reunión desagradable para todos los participantes.

#### Otros Participantes en Sitio – Mejores Prácticas

Cuando múltiples participantes se unen a una reunión en directo de Avatour desde la misma ubicación que la cámara 360°, la gestión cuidadosa del **audio y ancho de banda** es crucial:

- Cada smartphone, tablet u ordenador portátil conectado en sitio consume ancho de banda de red y puede afectar negativamente a la transmisión de la cámara 360°.
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo la experiencia de la reunión desagradable para todos los participantes.

Para abordar estos desafíos, sigue estas **mejores prácticas**:

- **Usa auriculares alámbricos o inalámbricos:** Preferiblemente con cancelación de ruido para evitar eco y retroalimentación.
- **Modo En Sitio:** Únete a la reunión en modo En Sitio cuando estés físicamente presente cerca de la cámara 360°.
  - Este modo está optimizado para uso en sitio:
    - Silencia el micrófono y altavoz del participante por defecto.
    - **No** envía la transmisión de cámara del participante.
    - **No** muestra la transmisión de la cámara 360° en el navegador del participante.
    - Conserva ancho de banda de red, asegurando que la cámara 360° tenga el máximo disponible para la transmisión en directo.
    - Útil cuando un usuario quiere compartir detalles específicos; **puedes compartir tu cámara** para vistas dirigidas.
- **Silencia cuando no estés hablando activamente:** Previene retroalimentación de audio no deseada y distracciones.
- **Usa una red separada si es posible:** Ten tu smartphone conectado a una red diferente a la de la cámara para reducir interferencias.

Seguir estas directrices asegura un recorrido en directo suave y de alta calidad tanto para participantes en sitio como remotos.### 5.3 Aplicación de Cámara Avatour

Aquí se encuentran (1) el menú de nivel superior, (2) Configuración y (3) menús de Configuración de red.

![Aplicación de Cámara Avatour 360° - Tres Menús](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Aplicación de Cámara Avatour 360° - 3 Menús*

**Captura Rápida** - Para grabación de video 360° sin conexión. - Para una descripción detallada, consulte [¿Cómo grabar y subir videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Recomendamos usar un dispositivo de audio externo (conectado vía bluetooth). Nota: También puede hacer videos y fotos estándar en 2D, simplemente cambie el modo entre 360° y 2D en la esquina inferior derecha una vez en la pantalla de Captura Rápida.

**Reunión en Vivo** - Para videoconferencia 360° en vivo. Verá sus espacios de trabajo y al hacer clic en uno iniciará la transmisión de video en vivo desde la cámara 360°. Antes de poder unirse a la reunión con su cámara 360°, debe conectar un dispositivo de audio vía bluetooth. Para una descripción detallada, consulte [¿Cómo iniciar una reunión de Captura en Vivo con su cámara Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Cuando aloja una reunión de Captura en Vivo con su cámara 360, tendrá herramientas de reunión similares disponibles que reflejan la experiencia web. Aquí hay un enlace a nuestro artículo de la Base de Conocimientos que explica estas herramientas con más detalle: [Herramientas de Aplicación del Operador](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galería** - Encuentre aquí todos sus videos y fotos 360° para subir a la Consola Web de Avatour.

**Configuración** - Dentro de Configuración, tiene las siguientes opciones:

- **Red**: Esta opción le permite cambiar a qué red WiFi está conectada la cámara o ejecutar una prueba de conexión de red para ver su rendimiento de transmisión
- **Captura en Vivo**: Ajuste la configuración de su Captura en Vivo según el ancho de banda disponible, la sensibilidad de realidad virtual del invitado, o si tiene instaladas las lentes protectoras de su cámara:
  - **Velocidad de Fotogramas Objetivo**: Ajuste la velocidad de fotogramas para su video de Captura en Vivo entre 15 fps, 24 fps y 30 fps. Las velocidades de fotogramas más altas producen un video más suave, pero requerirán más ancho de banda de carga. Predeterminado: 15 fps
  - **Velocidad de Bits Objetivo**: Le permite aumentar o disminuir la velocidad de bits máxima de transmisión para su Captura en Vivo. Puede establecer su velocidad de bits objetivo entre 1 Mbps y 10 Mbps. Las velocidades de bits más altas resultarán en una resolución de video más alta, pero requerirán más ancho de banda de carga. Predeterminado: 5 Mbps
  - **Optimizar Movimiento**: Esto disminuirá la velocidad de fotogramas del video, generando menos carga en el ancho de banda de carga de su red, e aumentará su velocidad de bits de transmisión. Además, esta opción ayuda a reducir el mareo en realidad virtual para los participantes. Predeterminado: Desactivado
  - **Lentes Protectoras**: Esto afectará cómo se cose el video 360° dependiendo de si se han instalado lentes protectoras en su cámara. Si no tiene lentes protectoras, establezca esto en "No". Si recibió un Kit 3.0, tiene lentes protectoras preinstaladas y debe establecer esto en "Sí". Predeterminado: Sí

- **Captura Rápida**: Ajuste la configuración de su Captura Rápida según su velocidad de fotogramas de video preferida, ancho de banda disponible para cargas de video grabado, o si tiene instaladas las lentes protectoras de su cámara. Captura Rápida tiene una resolución establecida de 4k que generalmente logra un buen equilibrio entre la calidad del video y el tamaño del archivo. (Para resoluciones más altas, puede usar las aplicaciones de cámara nativa, también en el PanoX V2, para detalles consulte [¿Cómo grabar y subir videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Velocidad de Fotogramas Objetivo**: Ajuste la velocidad de fotogramas para sus grabaciones de video de Captura Rápida entre 15 fps, 24 fps y 30 fps. Las velocidades de fotogramas más altas producen un video más suave, pero aumentarán el tamaño del archivo de video y el tiempo de carga. Recomendado: 30 fps
  - **Velocidad de Bits Objetivo**: Establezca la velocidad de bits objetivo para cargas de Captura Rápida entre 5 Mbps y 20 Mbps. Las velocidades de bits más bajas aumentan las velocidades de carga, pero disminuirán la calidad del video. Recomendado: 20 Mbps
  - **Lentes Protectoras**: *Consulte la sección Lentes Protectoras para Captura en Vivo anterior*
- **Acerca de**: Ver número de serie del dispositivo y versión del software

**Cuenta** - Para iniciar sesión con su cuenta de host o administrador de Avatour.## 6. Consejo de Mejores Prácticas {#best-practice-advice}

### 6.1 Primeros usos (informales) y familiarización

Para sus primeros usos y familiarización con la Consola Web de Avatour y el Kit Llave en Mano de Avatour recomendamos los siguientes pasos:

1. Lleve el kit a casa y juegue con él con familia y amigos usando su conexión a internet del hogar.
2. Lleve el kit a la oficina y conéctese a una red corporativa (podrían surgir problemas corporativos, p. ej. cortafuegos corporativos - pero ya sabe del paso uno que Avatour está funcionando y este es un tema a resolver por su equipo de TI con la ayuda de Avatour).
3. Comience a usar Avatour en el sitio (fuera de su oficina) en la ubicación de la reunión a la que los participantes remotos normalmente necesitarían viajar. Podrían surgir más temas de conectividad. Avatour ayudará en cooperación con su equipo de TI.
4. Comience a usar con participantes remotos internos y externos.### 6.2 Antes de una reunión en vivo de video 360°

- Recomendamos hacer un recorrido de video 360° grabado antes de cualquier recorrido en vivo si el tiempo lo permite por tres razones: (1) Tener una solución de respaldo para el recorrido en vivo, (2) tener algo para documentación y revisión posterior (además de la grabación del recorrido en vivo) y (3) comenzar a crear una biblioteca de videos 360° de todos sus sitios que puede ser útil para muchos casos de uso.
- Todos los componentes del kit cargados durante al menos 90 minutos antes de la reunión en vivo. De todas formas, recomendamos tener todos los dispositivos en carga continua cuando no estén en uso. De esta manera, todos los dispositivos siempre estarán listos, también para reuniones ad hoc no planificadas.
- Tener el kit completamente montado (1. base del trípode + 2. batería Ulanzi + 3. palo extensible + 4. cámara 360°).

- Confirme que se ha creado un Espacio de trabajo para alojar una reunión en vivo e incluya todos los Activos relevantes.

- Invite a todos los participantes a la reunión a través de su Espacio de trabajo. Esto crea una invitación en los calendarios de todos los participantes e incluye el enlace de invitación a la reunión.

- Empareje y conecte los auriculares Bluetooth o el altavoz que planea usar para su recorrido a la cámara.

- Todos los usuarios de smartphone en el sitio deben conectarse desde una red diferente a la red de la cámara. Esto reducirá la carga en el ancho de banda de la red de la cámara.

- Si está solo como operador de cámara, lleve consigo un smartphone en caso de que desee compartir la cámara del smartphone y mostrar detalles finos.

- Confirme que la cámara 360 puede conectarse a su WiFi local.

- Antes de una reunión de Avatour, planifique la ruta que recorrerá a través de la instalación. Realice una reunión de Avatour de prueba con la cámara y verifique que todas las áreas tengan velocidades de bits superiores a 1 Mbps de ancho de banda. Esto se puede ver en la pantalla de la cámara misma, o como participante remoto yendo a Configuración y activando Mostrar velocidad de bits.

- Si nota que algunas áreas tienen poco o ningún ancho de banda, es mejor tomar imágenes o hacer una grabación. Luego se pueden presentar durante la reunión para que los participantes remotos las revisen. Puede seguir la guía aquí que explica nuestra Captura rápida para grabar y cargar videos/imágenes: [¿Cómo grabar y cargar videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si tiene participantes remotos que se unen a la reunión que no han usado Avatour antes, proporcione un breve resumen de la plataforma, su funcionalidad (video en vivo 360, activos, capturas de pantalla, anotaciones, foco) y las herramientas de reunión.

- Puede comenzar en otra solución de videoconferencia (por ejemplo, Teams, Zoom, Google Meet) pero antes de cambiar a Avatour, cierre completamente la otra aplicación de videoconferencia. En algunos casos, estas otras aplicaciones priorizarán el micrófono/altavoces/cámara web de su dispositivo, lo que los deshabilitará para Avatour. Además, NO ejecute Avatour Y otra videoconferencia al mismo tiempo, ya que esto reducirá el ancho de banda disponible.

- Si planea usar la cámara 360 en un ambiente de alta temperatura, se recomienda usar el módulo de enfriamiento (solo Pilot Pano). Esto ayudará a reducir las posibilidades de que la cámara se sobrecaliente y se apague automáticamente.### 6.3 Cuando operas la cámara en el sitio para una reunión de video en vivo en 360°

- Cuando operes la cámara, asegúrate de caminar lentamente. Esto ayuda con la calidad del video y reduce cualquier posible tiempo de inactividad del video cuando la conexión de red de la cámara cambia entre puntos de acceso WiFi.

- Sostén la cámara frente a ti y por encima del nivel de los ojos. Esto permite que todos los participantes remotos vean la mayoría del área circundante.

- Para casos donde la cámara necesita permanecer estable, usa el trípode y extiende la cámara a la altura correcta, preferiblemente a nivel de los ojos.

- Siempre conecta la cámara a tu red WiFi local cuando sea posible. Para áreas sin acceso a WiFi, usa el punto de acceso proporcionado. El punto de acceso tiene una tarjeta SIM que se conectará a una red celular confiable cerca de ti. Siempre mantén el punto de acceso apagado cuando no esté en uso en interiores, de lo contrario la cámara 360° podría conectarse al punto de acceso, lo cual no deseamos en interiores. Cuando estés al aire libre, mantén el punto de acceso cerca de la cámara 360°.

- Cuando la velocidad de bits en cámara comienza a caer por debajo de 2 Mbps, camina más lentamente o detente completamente hasta que la señal se estabilice nuevamente. Esto generalmente sucede cuando cambias de un punto de acceso WiFi a otro.

- Si sabes que la conectividad y el video se interrumpirán cuando te muevas a una ubicación específica (Por ejemplo: moverte de un área de producción interior a un área al aire libre), avisa a los participantes remotos con anticipación.

- Si necesitas mostrar algo con alto detalle o texto pequeño, usa tu propio smartphone o el de un participante en el sitio para unirte a la reunión y presenta tu / su cámara trasera del teléfono.

- Si es posible, recomendamos que una persona adicional esté en el sitio para ayudar con el intercambio de cámara de smartphone descrito anteriormente, ya que a menudo resulta útil / necesario.

- Idealmente, los usuarios de smartphone en el sitio deben unirse a la reunión (1) en modo en el sitio y (2) en una red diferente a la que está usando la cámara para no reducir el ancho de banda de carga crucial de la cámara 360°.

- Todos los participantes en el sitio que se unan desde su smartphone deben estar silenciados, a menos que estén hablando activamente.