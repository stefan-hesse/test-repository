# Avatour User and Best Practices Guide

## 1. Para Todos los Usuarios de Avatour {#for-all-avatour-users}

Si es nuevo en Avatour, los siguientes recursos proporcionan una introducción útil a la plataforma y sus capacidades:

1. [Video Cómo Funciona Avatour](https://avatour.com/how-it-works)  
Una breve descripción general de las principales características de Avatour y cómo la plataforma permite la colaboración remota inmersiva.
2. [Preguntas Frecuentes](https://avatour.com/faqs)  
Respuestas a preguntas frecuentes.
3. [Glosario](https://avatour.com/glossary)  
Definiciones de términos y conceptos clave de Avatour utilizados frecuentemente.
4. Sitio Web  
Eche un vistazo especialmente a la página de [Características de Avatour](https://avatour.com/features) junto con las secciones dedicadas a Casos de Uso e Industrias para aprender cómo Avatour puede apoyar sus necesidades específicas.

## 2. Tipos de usuarios de Avatour  {#avatour-user-types}

### 2.1 Asistentes a Reuniones (No se requiere cuenta)
Los usuarios pueden unirse a la reunión sin registrarse para obtener una cuenta de Avatour.
Excepción: Si el anfitrión ha restringido la reunión a usuarios registrados — por ejemplo, para permitir que solo empleados internos se unan mediante Inicio de Sesión Único (SSO) — la invitación del calendario indicará que los participantes deben iniciar sesión para autenticarse.

Los usuarios acceden a la reunión de la siguiente manera:

- Reciben una invitación de calendario del anfitrión.
- Usan el enlace de la reunión en la invitación para unirse.
- Ingresan una contraseña de reunión si el anfitrión ha habilitado una.
- Los participantes pueden unirse sin una cuenta de Avatour a menos que la reunión esté restringida y requiera inicio de sesión para autenticarse.

#### 2.1.1 Participante 

- Puede unirse e interactuar completamente (cámara web, micrófono, chat y funcionalidad de Presentar).
- Máximo de 20 participantes interactivos por reunión.

#### 2.1.2 Espectador

- Puede ver la reunión y participar únicamente a través del chat.
- No puede compartir video, usar micrófono, presentar, reproducir/pausar Activos ni capturar Instantáneas.
- Máximo de 10 Espectadores por reunión.
- Junto con los Participantes, una reunión puede albergar hasta 30 asistentes.

### 2.2 Usuarios Registrados

Los Usuarios Registrados tienen una cuenta de Avatour. Las cuentas se crean de una de las siguientes maneras:

- **Invitado por Admin:** Durante la incorporación, Avatour configura un **tenant dedicado** para la organización y crea una o más **cuentas de Admin**. Los Admins pueden entonces **invitar usuarios** dentro de la organización y asignarlos a **grupos**, que definen su rol en la plataforma (Invitado, Anfitrión o Admin). Los usuarios invitados reciben un **enlace de registro** para completar la configuración de la cuenta y establecer una contraseña.  
- **Invitado por Anfitrión:** Los Anfitriones pueden agregar usuarios como **colaboradores Editores** a un Espacio de Trabajo. Esto consume una **licencia de Anfitrión** y asegura que el usuario tenga acceso de nivel Anfitrión.  
- **Aprovisionamiento automático SSO (solo nivel Enterprise/Business):** Las cuentas pueden ser creadas automáticamente por el IdP. Por defecto, las cuentas aprovisionadas por SSO se agregan al **grupo de Invitados**, a menos que se sobrescriba mediante **mapeos de grupos SAML**. Los Admins aún pueden invitar usuarios y asignar membresía de grupo directamente incluso cuando SSO está habilitado.

**Resumen:**  

Los usuarios registrados y su membresía de grupo pueden gestionarse de múltiples maneras:

- **Gestión por Admin:** Un Admin en la consola de Avatour puede crear usuarios y asignarlos a grupos, que definen su rol en la plataforma (Invitado, Anfitrión o Admin).  
- **Aprovisionamiento SSO:** Para clientes de nivel Enterprise o Business con SSO habilitado, el IdP puede aprovisionar automáticamente cuentas y asignar membresía de grupo, lo que define el rol del usuario en la plataforma.  
- **Usuarios invitados por Anfitrión:** Los Anfitriones pueden invitar a otros usuarios como colaboradores Editores a Espacios de Trabajo específicos. Asignar el rol de colaborador Editor consume una licencia de Anfitrión.

**Mejor Práctica Recomendada (Clientes Enterprise):**  
Para organizaciones que esperan un gran número de usuarios que necesitan acceso a Avatour, se recomienda **integrar Inicio de Sesión Único (SSO)** y gestionar usuarios y membresías de grupo desde el **IdP**. Este enfoque optimiza el aprovisionamiento de cuentas, la asignación de grupos y la gestión de licencias, reduciendo la carga administrativa y asegurando un control de acceso consistente.

#### 2.2.1 Usuarios Invitados

- Agregados al **grupo de Invitados**.  
- Pueden **ver Activos** dentro de Espacios de Trabajo donde han sido agregados como **colaboradores Visualizadores**.  
- No pueden crear espacios de trabajo, organizar reuniones ni subir contenido.  
- Las cuentas de Invitados aprovisionadas por SSO **se autentican a través del IdP**; no se requiere contraseña gestionada por Avatour.

---

#### 2.2.2 Usuarios con Licencia (Acceso a la Consola Web)

##### Usuarios Anfitriones (Grupo: Anfitrión)

- Pueden crear/gestionar Espacios de Trabajo, invitar colaboradores a un espacio de trabajo, **organizar reuniones en vivo**, subir **Capturas Rápidas**.  
- Tienen acceso al **Panel de Anfitrión** y a la **App de Operador** en cámaras 360° compatibles.  

##### Usuarios Admin (Grupo: Admin)

- Incluye todas las capacidades de Anfitrión más administración completa de la cuenta.

**Los privilegios adicionales de Admin incluyen:**

**Gestión de Cuentas**  

- Crear nuevos usuarios y asignarlos a grupos.
- Restablecer contraseñas cuando son gestionadas por Avatour (no aplicable cuando SSO está habilitado). 
- Actualizar usuarios Invitados a Anfitrión.  
- Desactivar usuarios (las cuentas de Admin deben convertirse primero a Anfitrión antes de la eliminación).  
- Transferir activos de un usuario Anfitrión a otro durante la eliminación.

**Configuración**  

- Configurar **ajustes de seguridad a nivel de organización** para activos, espacios de trabajo y reuniones organizadas en la plataforma (por ejemplo, si un Anfitrión debe estar presente para iniciar una reunión, si los rostros deben difuminarse en todos los videos subidos a la plataforma).  
- Habilitar o deshabilitar **funciones de IA** o **grabación**.  
- Aplicar marca de la empresa consistentemente en toda la plataforma si se ha configurado un **dominio personalizado**.
  

**Activos y Analíticas** 
 
- Ver todos los Activos subidos por cualquier usuario en la organización.  
- Revisar el uso de la plataforma en toda la organización.

---

#### 2.2.3 Permisos de Colaborador de Espacio de Trabajo

Los permisos de Espacio de Trabajo definen lo que un usuario puede hacer **dentro de un Espacio de Trabajo específico**. Estos son separados de la membresía de grupo a nivel de plataforma (Invitado, Anfitrión, Admin).

- **Colaborador Editor:** Los usuarios con este permiso pueden:
  - Gestionar Activos (subir, eliminar, difuminar rostros, generar resúmenes)  
  - Gestionar configuración de reuniones (habilitar/deshabilitar grabación, permitir o eliminar participantes)  
  - Programar y organizar reuniones en vivo  
  - Generar informes basados en plantillas predefinidas  
  - Agregar o eliminar colaboradores del Espacio de Trabajo  

- **Colaborador Visualizador:** Los usuarios con este permiso tienen acceso de solo lectura a los Activos del Espacio de Trabajo. **No pueden modificar Activos, gestionar reuniones ni gestionar colaboradores**, pero **pueden crear Notas en los Activos**. 
  
## 3. Para Participantes de Reuniones Remotas y Visitantes del Espacio de Trabajo {#for-remote-meeting-participants-and-workspace-visitors}
<section>

Avatour permite a los usuarios colaborar de dos formas principales:

- **Unirse a una reunión de Avatour (Colaboración Sincrónica):**  
  Puede recibir una **invitación de calendario** para unirse a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota en vivo al sitio** o revisar recursos de forma sincrónica juntos.

- **Visitar un Espacio de Trabajo (Colaboración Asincrónica):**  
  También puede ser invitado como **colaborador a un Espacio de Trabajo** para revisar recursos de forma **asincrónica** (según su propio horario).

### 3.1 Cómo Unirse a una Reunión de Avatour y Visitar un Espacio de Trabajo de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Cualquier Dispositivo de "Pantalla Plana" con Navegador Web {#any-flat-screen}
Puede unirse a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, teléfono inteligente o tableta** usando un navegador web.  

##### Unirse a una Reunión de Avatour

> **Nota:** Unirse a una reunión de Avatour requiere que **conceda permisos de micrófono**. Por favor, acepte cualquier solicitud de permiso de su navegador.

1. **A través de invitación de calendario (recomendado):**  
   - Normalmente recibirá una **invitación de calendario** con un **enlace directo para unirse** (por ejemplo: `https://avatour.live/join?s=xxxxx`).  
   - Al hacer clic en el enlace, se completará automáticamente el **código de reunión de 5 caracteres** y lo llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que necesita **iniciar sesión para acceder a la reunión**.  
   - **Reuniones protegidas con contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debe ingresar para unirse.

2. **A través de código de reunión:**  
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, vaya a [https://avatour.live/join](https://avatour.live/join), ingrese su **nombre** y el **código de reunión**, y únase a la reunión.  
   - Si la reunión está **protegida con contraseña**, ingrese la contraseña proporcionada por el anfitrión.  
   - Si la reunión requiere **autenticación**, necesitará **iniciar sesión con su cuenta de Avatour** antes de unirse.

> **Consejo 1:** Si su cámara o micrófono no funcionan, pueden estar en uso por otra aplicación (por ejemplo, Microsoft Teams o Zoom). Cierre cualquier aplicación que pueda estar usando su cámara o micrófono, luego salga y vuelva a unirse a la reunión de Avatour.  

> **Consejo 2:** Si aún no puede unirse a la reunión, ejecute esta prueba: [https://avatour.live/test](https://avatour.live/test).  
> La prueba puede identificar si su **firewall corporativo o red** está bloqueando el acceso, y proporcionará información para guiar las conversaciones con su equipo de TI.  

> **Consejo 3:** **No** use las aplicaciones de Avatour para iOS o Android para unirse a reuniones. Estas aplicaciones solo son necesarias cuando se **transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar el software Avatour 360° directamente y requieren un teléfono inteligente para asistir.

##### Visitar un Espacio de Trabajo de Avatour (sin unirse a una Reunión de Avatour)

Puede acceder a un Espacio de Trabajo de las siguientes maneras:

- **Espacio de Trabajo Público:**  
  Si el Espacio de Trabajo es público, el enlace se puede acceder directamente—no se requiere inicio de sesión.

- **Espacio de Trabajo Restringido:**  
  Si el Espacio de Trabajo está restringido, debe ser agregado como **colaborador** con permisos de **Editor** o **Visualizador**.

  1. Cuando sea agregado como colaborador, recibirá una **notificación por correo electrónico** con un enlace al Espacio de Trabajo.
  2. Haga clic en el enlace del correo electrónico para abrir el Espacio de Trabajo. Si no ha iniciado sesión, se le pedirá que **inicie sesión o complete el registro**.
  3. Una vez que haya iniciado sesión, el Espacio de Trabajo se abrirá automáticamente.

  Alternativamente, puede iniciar sesión en [https://avatour.live/login](https://avatour.live/login) y acceder al Espacio de Trabajo desde su **lista de Espacios de Trabajo**.

#### 3.1.2 Visor de Realidad Virtual {#vr-headset}
Puede unirse a una reunión y visitar un espacio de trabajo desde una variedad de visores Meta y Pico compatibles. Para hacer esto: 

1. Instale nuestra aplicación Avatour desde la tienda de aplicaciones de su visor de RV respectivo: [Cómo instalar la aplicación Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Cargue nuestra aplicación e ingrese el código de reunión o seleccione un Espacio de Trabajo para unirse a una reunión. Para más información sobre cómo usar nuestra aplicación de RV, consulte nuestro artículo de la Base de Conocimientos [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Herramientas de Colaboración para Reuniones y Espacios de Trabajo {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (sincrónicas):** Colabore en tiempo real con otros participantes, incluyendo visitas en vivo al sitio o revisión de recursos grabados juntos.  
2. **Espacios de Trabajo (asincrónicos):** Revise e interactúe con recursos según su propio horario, 24/7.

Las **herramientas de colaboración son mayormente similares** entre reuniones y espacios de trabajo, con algunas diferencias debido al contexto sincrónico vs asincrónico.

#### 3.2.1 Disposición de la Interfaz

La interfaz de Avatour está organizada alrededor de tres áreas principales:

- **Panel izquierdo** – Recursos del espacio de trabajo y herramientas de apoyo  
- **Lienzo central** – Área de visualización principal para video en vivo o recursos  
- **Panel derecho** – Información contextual, como participantes, reuniones o chat  

La mayoría de las interacciones se inician desde el **menú inferior**.  
Al hacer clic en una opción del menú se abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **lienzo central** permanece como el área de visualización principal.

---
#### 3.2.2 Ejemplo de Vista de Reunión

Aquí hay un ejemplo de una vista en una Reunión de Avatour:

![Interfaz de Reunión Avatour con Panel de Recursos, Lienzo en blanco y Panel de Participantes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Reunión de Avatour con Panel de Recursos (izquierda), Lienzo (centro) y Panel de Participantes (derecha)*

---

#### 3.2.3 Ejemplo de Vista de Espacio de Trabajo

Aquí hay un ejemplo de una vista de Espacio de Trabajo:

![Espacio de Trabajo Avatour con Panel de Recursos, Lienzo en blanco y Panel de Reuniones](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espacio de Trabajo de Avatour con Panel de Recursos (izquierda), Lienzo (centro) y Panel de Reuniones (derecha)*

---

#### 3.2.4 Descripción General del Menú Inferior

El menú inferior proporciona acceso a los controles principales de la interfaz y paneles:

**Menú Inferior de Reunión**  

![Menú Inferior de Reunión Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menú Inferior de Reunión Avatour*

- **Recursos** – Revise archivos del espacio de trabajo, incluyendo videos grabados, imágenes, capturas y PDFs. 
- **Chat** – Envíe mensajes a todos los participantes de la reunión.  
- **Cámara** – Encienda o apague su cámara web.  
- **Micrófono** – Active o desactive su audio.  
- **Presentar** – Presente un recurso, escritorio o transmisión de cámara web (vea la sección Presentar a continuación).  
- **Herramientas de Anfitrión** (solo anfitriones):  
  - **Bloquear Enfoque** – Bloquee la vista para todos los participantes.  
  - **Silenciar a Todos** – Silencie a todos los participantes.  
- **Habilitar Pantalla Completa** – Ponga la pestaña de la reunión en pantalla completa.  
- **Salir de la Reunión** – Abandone la reunión.  
- **Iniciar Grabación** – Use este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones pueden grabarse automáticamente si **inicio automático de grabación** está habilitado en la configuración del espacio de trabajo. En ambos casos, las grabaciones se guardan en los recursos del espacio de trabajo.
- **Mapa** – Abra o cierre el panel del mapa para recursos con seguimiento GPS. Al hacer clic en una ubicación, salta al punto exacto en el video. El mapa se actualiza en vivo mientras se reproduce el video.
- **Participantes** – Abra o cierre el panel de participantes.  
- **Información de la Reunión** – Vea el código de la reunión, enlace de invitación y acceda a tutoriales relacionados.  

![Información de Reunión Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panel Lateral de Información de Reunión Avatour*

- **Configuración** – Ajuste la configuración de idioma, audio y video. Para reuniones de video 360° en vivo, use **Mostrar Tasa de Bits** para monitorear estadísticas de conectividad.

> Consejo: Envíe el enlace de la reunión o agréguelo a un elemento de calendario para invitar participantes.

---

##### Menú Presentar

La opción **Presentar** en el menú inferior de la reunión le permite compartir contenido con todos los participantes.

- **Cámara** – Comparta la cámara de su teléfono inteligente/tableta. Esto también se puede usar durante una reunión de video 360° en vivo para superponer una vista secundaria para primeros planos o detalles específicos. 
- **Escritorio** – Comparta la pantalla de su escritorio con todos los participantes.  
- **Recurso** – Presente un recurso del espacio de trabajo. Al seleccionar un recurso se abre la **Barra de herramientas del Recurso**, que proporciona controles de reproducción y herramientas de colaboración específicas para el recurso que se está presentando.

##### Barra de Herramientas del Recurso (Reunión)

Cuando presenta un recurso en una reunión, la **Barra de Herramientas del Recurso** aparece sobre el lienzo. Aquí están las herramientas y elementos del menú disponibles cuando <u>presenta un Recurso en una Reunión</u> - explicados de izquierda a derecha.

![Menú de Avatour al Presentar un Recurso en una Reunión](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour al presentar un Recurso en una Reunión*


- **Línea de Tiempo del Video / Barra de Progreso** – Muestra el progreso del video con notas y temas clave extraídos del audio. Haga clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.   
- **Captura** – Capture una imagen 360° o 2D del recurso.  
- **Foco** – Resalte un área específica para todos los participantes durante sesiones en vivo.  
- **Mostrar/Ocultar Punto de Vista (POV)** – Muestre dónde está mirando cada participante en el video 360°.  
- **Notas** – Cree notas ancladas a momentos específicos en el recurso. Las notas pueden categorizarse (Observación, Problema, Acción, Recomendación), rastrearse por estado (Abierto → En Progreso → Resuelto) y compartirse a través de enlaces directos.  

  ![Nota y Filtro de Notas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota y Filtros de Notas de Avatour*

  - **Notas por Comando de Voz** – Estos son marcadores de posición generados automáticamente cuando la grabación detecta menciones como "insertar nota", "tomar una nota" o "hacer una nota". Estas notas aparecen en la línea de tiempo y necesitan ser **posicionadas y finalizadas** por el usuario. 

  ![Notas de Avatour - Generadas por Comando de Voz](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por Comando de Voz*

- **Panel de Notas y Resumen** – Abre un panel lateral que muestra todas las notas, temas clave y un resumen ejecutivo del recurso. Al hacer clic en un elemento, lo lleva a ese momento en el video.  

  ![Resumen Ejecutivo de Recurso Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen Ejecutivo de Avatour al presentar un Recurso en una Reunión*

  ![Temas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Temas de Avatour al presentar un Recurso en una Reunión*

  Desde## 4. Para usuarios anfitriones y administradores - Consola web de Avatour {#for-host-and-admin-users-avatour-web-console}

Cuando inicias sesión en tu Cuenta de Usuario de Avatour, accederás a la **Consola Web**.  

### 4.1 Consola Web - Descripción General del Menú Principal {#web-console-overview-main-menu}

En el lado izquierdo, verás los siguientes elementos del menú:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Consola Web de Avatour - Menú Principal*

- **Espacios de Trabajo** – Organiza tu contenido de manera eficiente. Cada espacio de trabajo contiene **Recursos**, **Colaboradores**, **Reuniones** y **Configuración**.  
- **Recursos** – Accede y gestiona todos tus recursos (videos, imágenes, PDFs). Los administradores pueden ver todos los recursos de la cuenta, y los recursos compartidos son visibles para todos los usuarios.  
- **Perfil** – Gestiona tu idioma y contraseña.  
- **Analíticas** – Rastrea la actividad de sesiones, uso de espacios de trabajo y métricas de ROI.  
- **Configuración** *(Solo administrador)* – Configura los valores predeterminados de espacios de trabajo, reuniones y recursos en toda la organización. Los administradores también pueden personalizar la marca (logo, colores, fondos).  
- **Cuenta** *(Solo administrador)* – Gestiona usuarios registrados y cámaras 360°.  
- **Inicio de Sesión de Dispositivo** – Ingresa el código mostrado en tu cámara 360° para vincularla con tu cuenta.  
- **Tutoriales** – Accede a tutoriales guiados.  
- **Cerrar sesión** – Cierra sesión en la consola.

> Secciones como Perfil, Inicio de Sesión de Dispositivo, Tutoriales y Cerrar sesión son autoexplicativas y no tienen subsecciones detalladas.

---

### 4.2 Consola Web - Detalles por Elemento del Menú (con imágenes) {#web-console-details-by-menu-item}

#### 4.2.1 Espacios de Trabajo

Los espacios de trabajo son unidades organizativas flexibles que te permiten gestionar recursos, colaboradores y reuniones en un solo lugar. Puedes crear un nuevo espacio de trabajo con el botón **Nuevo Espacio de Trabajo** en la esquina superior derecha.

![Avatour Web Console - Main Menu Item Workspaces](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web de Avatour - Elemento del Menú Principal Espacios de Trabajo*

Haz clic en el icono de campana para ver un resumen de la actividad del espacio de trabajo en los últimos 7 días.

![Avatour Web Console - Workspace Recent Activities](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Actividades Recientes del Espacio de Trabajo*

Dentro de un espacio de trabajo:

![Avatour Workspace with Assets Panel, blank Canvas and Meetings Panel](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espacio de Trabajo con Recursos (izquierda), Lienzo (centro), Reuniones (derecha)*

- **Recursos** – Gestiona archivos asignados a este espacio de trabajo.  
- **Colaboradores** – 
  Controla el acceso a los espacios de trabajo mediante 
  - **Visualizador** – Puede ver recursos. La invitación crea un usuario Invitado si es necesario.  
  - **Editor** – Control total del espacio de trabajo, mismos derechos que el Anfitrión. La invitación actualiza al usuario a Anfitrión si es necesario.  
> Múltiples usuarios pueden acceder a un espacio de trabajo simultáneamente sin una reunión. Los espacios de trabajo públicos y la configuración de acceso a reuniones proporcionan acceso alternativo.  
- **Informe** – Genera un informe usando una plantilla de lista de verificación sobre los recursos seleccionados del espacio de trabajo.  

![Avatour Workspace Report and Asset Selection](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe del Espacio de Trabajo y Selección de Recursos*

- **Mapa** – Muestra ubicaciones de recursos con GPS en un mapa.  
- **Reuniones** – Organiza reuniones en el espacio de trabajo.  
- **Configuración** – Configura los valores predeterminados del espacio de trabajo y reuniones:

![Avatour Settings - Workspace View](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Configuración del Espacio de Trabajo*

**Configuración del Espacio de Trabajo**

- **Plantilla de Informe** – Selecciona la plantilla de lista de verificación para informes de IA.  
- **Habilitar Notificaciones** – Correos de resumen diario para cambios de estado de notas.  

![Email Notifications - Example](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Ejemplo de Notificaciones por Correo Electrónico*

- **Espacio de Trabajo Público** – Cualquier persona con el enlace puede ver los recursos directamente.

**Configuración de Reuniones**
  
* **Autenticación requerida** – Los participantes deben iniciar sesión.  
* **Permitir acceso de invitados** – Permitir que usuarios no registrados vean recursos.  
* **Inicio Automático de Grabación / Inicio Manual** – Elige si las reuniones se graban automáticamente o se inician manualmente.  
* **Requiere anfitrión** – El anfitrión debe admitir participantes; la reunión termina cuando el anfitrión se va.  
* **Permitir acceso de espectador** – Unirse sin micrófono o cámara; comunicarse vía chat.  
* **Reuniones protegidas con contraseña** – Requiere una contraseña para unirse.  
* **Mostrar Pregunta de Ahorro de Viaje** – Preguntar a los participantes si la reunión redujo los viajes.  

> Las configuraciones se pueden combinar (ej., sin anfitrión requerido pero protegido con contraseña).

---

#### 4.2.2 Recursos

Gestiona todos los videos 360°/2D, imágenes y PDFs. Carga/descarga recursos, asígnalos a espacios de trabajo, compártelos con otros usuarios, renómbralos, imprime/descarga informes, activa el desenfoque facial y la resumención con IA.

![Avatour Web Console - Main Menu Item Assets](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Elemento del Menú Principal Recursos*

---

#### 4.2.3 Analíticas

Proporciona información sobre reuniones, uso de espacios de trabajo y métricas de ROI.

![Avatour Web Console - Main Menu Item Analytics (1 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Descripción General de Analíticas*

![Avatour Web Console - Main Menu Item Analytics (2 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Actividad de Reuniones y Uso de Espacios de Trabajo*

![Avatour Web Console - Main Menu Item Analytics (3 of 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de Licencias de Dispositivos y ROI* 

## 6. Consejos de Mejores Prácticas {#best-practice-advice}

### 6.1 Primeros Usos (informales) y Familiarización

Para sus primeros usos y familiarizarse con la Consola Web de Avatour y el Kit Llave en Mano de Avatour, recomendamos los siguientes pasos:

1. Lleve el kit a casa y practique con familiares y amigos usando su conexión de internet doméstica.
2. Lleve el kit a la oficina y conéctese a una red corporativa (pueden surgir problemas corporativos, por ejemplo, firewalls corporativos - pero usted sabe por el paso uno que Avatour funciona y este es un tema a resolver por su equipo de TI con la ayuda de Avatour).
3. Comience a usar Avatour en sitio (fuera de su oficina) en el lugar de reunión al cual los participantes remotos normalmente necesitarían viajar. Pueden surgir más temas de conectividad. Avatour ayudará en cooperación con su equipo de TI.
4. Comience a usar con participantes remotos internos y externos.

### 6.2 Antes de una Reunión en Vivo con Video 360°

- Recomendamos hacer un recorrido en video 360° grabado antes de cualquier recorrido en vivo si el tiempo lo permite, por tres razones: (1) Tener una solución de respaldo para el recorrido en vivo, (2) tener algo para documentación y revisión posterior (además del recorrido en vivo grabado) y (3) comenzar a crear una biblioteca de videos 360° de todos sus sitios, lo cual puede ser útil para muchos casos de uso.
- Todos los componentes del kit cargados durante al menos 90 minutos antes de la reunión en vivo. De todos modos, recomendamos tener todos los dispositivos en carga continua cuando no estén en uso. De esta manera, todos los dispositivos siempre estarán listos, también para reuniones ad hoc no planificadas.
- Tenga el kit completamente ensamblado (1. base del trípode + 2. batería Ulanzi + 3. palo extensible + 4. cámara 360°).

- Confirme que se ha creado un Espacio de Trabajo para alojar una reunión en vivo e incluya todos los Recursos relevantes.

- Invite a todos los participantes a la reunión a través de su Espacio de Trabajo. Esto crea una invitación en los calendarios de todos los participantes e incluye el enlace de invitación a la reunión.

- Empareje y conecte sus auriculares bluetooth o altavoz que planea usar para su recorrido a la cámara.

- Todos los usuarios de smartphones en sitio deben conectarse desde una red diferente a la red de la cámara. Esto reducirá la carga en el ancho de banda de la red de la cámara.

- Si está solo como operador de cámara, lleve un smartphone con usted en caso de que quiera compartir la cámara del smartphone y mostrar detalles finos.

- Confirme que la cámara 360 puede conectarse a su WiFi local.

- Antes de una reunión de Avatour, planifique la ruta que tomará a través de las instalaciones. Haga una reunión de prueba de Avatour con la cámara y verifique que todas las áreas tengan tasas de bits superiores a 1 Mbps de ancho de banda. Esto se puede ver en la pantalla de la cámara misma, o como participante remoto yendo a Configuración y activando Mostrar Tasa de Bits.

- Si nota que algunas áreas tienen poco o ningún ancho de banda, es mejor tomar imágenes o una grabación. Estas pueden luego presentarse durante la reunión para que los participantes remotos las revisen. Puede seguir la guía aquí que explica nuestra Captura Rápida para grabar y subir videos/imágenes: [¿Cómo grabar y subir videos 360 con la App de Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si tiene participantes remotos uniéndose a la reunión que no han usado Avatour antes, proporcióneles un breve resumen de la plataforma, su funcionalidad (video en vivo 360, recursos, capturas, anotaciones, destacado) y las herramientas de la reunión.

- Puede comenzar en otra solución de videoconferencia (por ejemplo, Teams, Zoom, Google Meet) pero antes de pasar a Avatour, cierre completamente la otra aplicación de videoconferencia. En algunos casos, estas otras aplicaciones priorizarán el micrófono/altavoces/cámara web de su dispositivo, causando que se deshabiliten para Avatour. Además, NO ejecute Avatour Y otra videoconferencia al mismo tiempo ya que esto reducirá el ancho de banda disponible.

- Si planea usar la cámara 360 en un entorno de alta temperatura, se recomienda usar el módulo de enfriamiento (solo Pilot Pano). Esto ayudará a reducir las posibilidades de que la cámara se sobrecaliente y se apague automáticamente.

### 6.3 Al Operar la Cámara en Sitio para una Reunión en Vivo con Video 360°

- Al operar la cámara, asegúrese de caminar lentamente. Esto ayuda con la calidad del video y reduce cualquier posible tiempo de inactividad del video cuando la conexión de red de la cámara cambia entre puntos de acceso WiFi.

- Sostenga la cámara frente a usted y por encima del nivel de los ojos. Esto permite que todos los participantes remotos vean la mayor parte de su área circundante.

- Para casos donde la cámara necesita permanecer estable, use el soporte del trípode y extienda la cámara a la altura correcta, preferiblemente al nivel de los ojos.

- Siempre conecte la cámara a su red WiFi local cuando sea posible. Para áreas sin acceso WiFi, use el hotspot proporcionado. El hotspot tiene una tarjeta SIM que se conectará a una red celular confiable cerca de usted. Siempre mantenga el hotspot apagado cuando no esté en uso en interiores, ya que de lo contrario la cámara 360° podría conectarse al hotspot, lo cual no queremos en interiores. Cuando esté en exteriores, mantenga el hotspot cerca de la cámara 360°.

- Cuando la tasa de bits en la cámara comience a caer por debajo de 2 Mbps, camine más lento o deténgase completamente hasta que la señal se estabilice nuevamente. Esto generalmente sucede cuando cambia de un Punto de Acceso WiFi a otro.

- Si sabe que la conectividad y el video se perderán al moverse a una ubicación específica (Ejemplo: moverse de un área de producción interior a un área exterior), avise a los participantes remotos con anticipación.

- Si necesita mostrar algo en alto detalle o escritura pequeña, use su propio smartphone o el de un participante en sitio para unirse a la reunión y presentar la cámara (trasera) de su teléfono / el de ellos.

- Si es posible, recomendamos que una persona adicional esté en sitio para ayudar con el compartir cámara del smartphone descrito anteriormente, ya que esto a menudo resulta ser útil / necesario.

- Idealmente, los usuarios de smartphones en sitio deben unirse a la reunión (1) en modo en sitio y (2) en una red diferente de la que usa la cámara para no quitar ancho de banda de subida crucial de la cámara 360°.

- Todos los participantes en sitio que se unan desde su smartphone deben estar silenciados, a menos que estén hablando activamente.
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
