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
Avatour permite a los usuarios colaborar de dos formas principales:

- **Unirse a una reunión de Avatour (Colaboración Sincrónica):**  
  Puede recibir una **invitación de calendario** para unirse a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota al sitio en vivo** o revisar activos de forma sincrónica juntos.

- **Visitar un Espacio de Trabajo (Colaboración Asincrónica):**  
  También puede ser invitado como **colaborador a un Espacio de Trabajo** para revisar activos **de forma asincrónica** (según su propio horario).### 3.1 Cómo unirse a una reunión de Avatour y visitar un espacio de trabajo de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Cualquier dispositivo de "pantalla plana" con un navegador web {#any-flat-screen}
Puede unirse a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, teléfono inteligente o tableta** utilizando un navegador web.  

##### Unirse a una reunión de Avatour

> **Nota:** Unirse a una reunión de Avatour requiere que **otorgue permisos de micrófono**. Por favor, acepte cualquier solicitud de permiso de su navegador.

1. **Mediante invitación de calendario (recomendado):**  
   - Normalmente recibirá una **invitación de calendario** con un **enlace de acceso directo** (por ejemplo: `https://avatour.live/join?s=xxxxx`).  
   - Al hacer clic en el enlace, se completará automáticamente el **código de reunión de 5 caracteres** y lo llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que necesita **iniciar sesión para acceder a la reunión**.  
   - **Reuniones protegidas con contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debe ingresar para unirse.

2. **Mediante código de reunión:**  
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, vaya a [https://avatour.live/join](https://avatour.live/join), ingrese su **nombre** y el **código de reunión**, y únase a la reunión.  
   - Si la reunión está **protegida con contraseña**, ingrese la contraseña proporcionada por el anfitrión.  
   - Si la reunión requiere **autenticación**, deberá **iniciar sesión con su cuenta de Avatour** antes de unirse.

> **Consejo 1:** Si su cámara o micrófono no funciona, puede estar en uso por otra aplicación (por ejemplo Microsoft Teams o Zoom). Cierre cualquier aplicación que pueda estar usando su cámara o micrófono, luego salga y vuelva a unirse a la reunión de Avatour.  

> **Consejo 2:** Si aún no puede unirse a la reunión, ejecute esta prueba: [https://avatour.live/test](https://avatour.live/test).  
> La prueba puede identificar si su **firewall corporativo o red** está bloqueando el acceso, y proporcionará información para guiar las conversaciones con su equipo de TI.  

> **Consejo 3:** **No** use las aplicaciones de Avatour para iOS o Android para unirse a reuniones. Estas aplicaciones solo son necesarias cuando **transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar el software Avatour 360° directamente y requieren un teléfono inteligente para asistir.

##### Visitar un espacio de trabajo de Avatour (sin unirse a una reunión de Avatour)

Puede acceder a un espacio de trabajo de las siguientes maneras:

- **Espacio de trabajo público:**  
  Si el espacio de trabajo es público, se puede acceder directamente al enlace — no se requiere inicio de sesión.

- **Espacio de trabajo restringido:**  
  Si el espacio de trabajo está restringido, debe ser agregado como **colaborador** con permisos de **Editor** o **Visualizador**.

  1. Cuando sea agregado como colaborador, recibirá una **notificación por correo electrónico** con un enlace al espacio de trabajo.
  2. Haga clic en el enlace del correo electrónico para abrir el espacio de trabajo. Si aún no ha iniciado sesión, se le pedirá que **inicie sesión o complete el registro**.
  3. Una vez que haya iniciado sesión, el espacio de trabajo se abrirá automáticamente.

  Alternativamente, puede iniciar sesión en [https://avatour.live/login](https://avatour.live/login) y acceder al espacio de trabajo desde su **lista de espacios de trabajo**.

#### 3.1.2 Visor de realidad virtual {#vr-headset}
Puede unirse a una reunión y visitar un espacio de trabajo desde una variedad de visores compatibles de Meta y Pico. Para hacer esto: 

1. Instale nuestra aplicación Avatour desde su respectiva tienda de aplicaciones de RV: [Cómo instalar la aplicación Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Cargue nuestra aplicación e ingrese el código de reunión o seleccione un espacio de trabajo para unirse a una reunión. Para más información sobre cómo usar nuestra aplicación de RV, consulte nuestro artículo de la Base de conocimientos [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).### 3.2 Herramientas de colaboración para reuniones y espacios de trabajo {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (síncronas):** Colabora en tiempo real con otros participantes, incluyendo visitas en vivo al sitio o revisión conjunta de recursos grabados.  
2. **Espacios de trabajo (asíncronos):** Revisa e interactúa con los recursos según tu propio horario, 24/7.

Las **herramientas de colaboración son mayormente similares** entre reuniones y espacios de trabajo, con algunas diferencias debido al contexto síncrono vs asíncrono.

#### 3.2.1 Diseño de la interfaz

La interfaz de Avatour está organizada en tres áreas principales:

- **Panel izquierdo** – Recursos del espacio de trabajo y herramientas de apoyo  
- **Lienzo central** – Área de visualización principal para video en vivo o recursos  
- **Panel derecho** – Información contextual, como participantes, reuniones o chat  

La mayoría de las interacciones se inician desde el **menú inferior**.  
Al hacer clic en una opción del menú, se abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **lienzo central** permanece como el área de visualización principal.

---
#### 3.2.2 Ejemplo de vista de reunión

Aquí hay un ejemplo de una vista en una reunión de Avatour:

![Interfaz de reunión de Avatour con panel de recursos, lienzo en blanco y panel de participantes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Reunión de Avatour con panel de recursos (izquierda), lienzo (centro) y panel de participantes (derecha)*

---

#### 3.2.3 Ejemplo de vista del espacio de trabajo

Aquí hay un ejemplo de una vista del espacio de trabajo:

![Espacio de trabajo de Avatour con panel de recursos, lienzo en blanco y panel de reuniones](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Espacio de trabajo de Avatour con panel de recursos (izquierda), lienzo (centro) y panel de reuniones (derecha)*

---

#### 3.2.4 Descripción general del menú inferior

El menú inferior proporciona acceso a los controles principales de la interfaz y los paneles:

**Menú inferior de reunión**  

![Menú inferior de reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menú inferior de reunión de Avatour*

- **Recursos** – Revisa los archivos del espacio de trabajo, incluyendo videos grabados, imágenes, capturas y PDFs. 
- **Chat** – Envía mensajes a todos los participantes de la reunión.  
- **Cámara** – Activa o desactiva tu cámara web.  
- **Micrófono** – Activa o silencia tu micrófono.  
- **Presentar** – Presenta un recurso, escritorio o transmisión de cámara web (consulta la sección Presentar a continuación).  
- **Herramientas del anfitrión** (solo anfitriones):  
  - **Bloquear enfoque** – Bloquea la vista para todos los participantes.  
  - **Silenciar a todos** – Silencia a todos los participantes.  
- **Habilitar pantalla completa** – Pone la pestaña de la reunión en pantalla completa.  
- **Salir de la reunión** – Abandona la reunión.  
- **Iniciar grabación** – Usa este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones pueden grabarse automáticamente si **inicio automático de grabación** está habilitado en la configuración del espacio de trabajo. En ambos casos, las grabaciones se guardan en los recursos del espacio de trabajo.
- **Mapa** – Abre o cierra el panel del mapa para recursos con seguimiento GPS. Al hacer clic en una ubicación, salta al punto exacto en el video. El mapa se actualiza en vivo mientras se reproduce el video.
- **Participantes** – Abre o cierra el panel de participantes.  
- **Información de la reunión** – Visualiza el código de la reunión, el enlace de invitación y accede a tutoriales relacionados.  

![Información de reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panel lateral de información de reunión de Avatour*

- **Configuración** – Ajusta la configuración de idioma, audio y video. Para reuniones de video 360° en vivo, usa **Mostrar tasa de bits** para monitorear las estadísticas de conectividad.

> Consejo: Envía el enlace de la reunión o agrégalo a un elemento del calendario para invitar a los participantes.

---

##### Menú Presentar

La opción **Presentar** en el menú inferior de la reunión te permite compartir contenido con todos los participantes.

- **Cámara** – Comparte la cámara de tu smartphone/tablet. También se puede usar durante una reunión de video 360° en vivo para superponer una vista secundaria para primeros planos o detalles específicos. 
- **Escritorio** – Comparte la pantalla de tu escritorio con todos los participantes.  
- **Recurso** – Presenta un recurso del espacio de trabajo. Al seleccionar un recurso, se abre la **barra de herramientas del recurso**, que proporciona controles de reproducción y herramientas de colaboración específicas para el recurso que se está presentando.

##### Barra de herramientas del recurso (Reunión)

Al presentar un recurso en una reunión, la **barra de herramientas del recurso** aparece sobre el lienzo. Aquí están las herramientas y opciones de menú disponibles al <u>presentar un recurso en una reunión</u> - explicadas de izquierda a derecha.

![Menú de Avatour al presentar un recurso en una reunión](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour al presentar un recurso en una reunión*


- **Línea de tiempo del video / Barra de progreso** – Muestra el progreso del video con notas y temas clave extraídos del audio. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.   
- **Captura** – Captura una imagen 360° o 2D del recurso.  
- **Destacar** – Resalta un área específica para todos los participantes durante las sesiones en vivo.  
- **Mostrar/Ocultar punto de vista (POV)** – Muestra dónde está mirando cada participante en el video 360°.  
- **Notas** – Crea notas ancladas a momentos específicos en el recurso. Las notas pueden categorizarse (Observación, Problema, Acción, Recomendación), rastrearse por estado (Abierto → En progreso → Resuelto) y compartirse mediante enlaces directos.  

  ![Nota y filtro de notas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota y filtros de notas de Avatour*

  - **Notas por comando de voz** – Estos son marcadores de posición generados automáticamente cuando la grabación detecta menciones como "insertar nota", "tomar una nota" o "hacer una nota". Estas notas aparecen en la línea de tiempo y necesitan ser **posicionadas y finalizadas** por el usuario. 

  ![Notas de Avatour - Generadas por comando de voz](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por comando de voz*

- **Panel de notas y resumen** – Abre un panel lateral que muestra todas las notas, temas clave y un resumen ejecutivo del recurso. Al hacer clic en un elemento, te lleva a ese momento en el video.  

  ![Resumen ejecutivo del recurso de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen ejecutivo de Avatour al presentar un recurso en una reunión*

  ![Temas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Temas de Avatour al presentar un recurso en una reunión*

  Desde el **panel lateral**, puedes **imprimir un informe del recurso** o **descargarlo como TXT o CSV**. Los informes pueden incluir notas, temas generados por IA y transcripciones completas. También puedes **elegir qué elementos incluir** antes de exportar.  

  ![Menús de impresión de informe de recurso de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menús de impresión / descarga de informe de recurso de Avatour*  

  ![Selección de elementos del informe de recurso de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menú de selección de elementos del informe de recurso de Avatour*

- **Compartir enlace** – Comparte un enlace a una nota específica o escena en el recurso.  
- **Subtítulos (CC)** – Muestra la transcripción de texto en pantalla durante la reproducción del video.

##### Barra de herramientas del recurso (Espacio de trabajo)

Al revisar un recurso en un espacio de trabajo, la barra de herramientas es similar pero optimizada para uso individual:

![Menú de Avatour al presentar un recurso fuera de una reunión, por ejemplo, al visitar un espacio de trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menú de Avatour al presentar un recurso en un espacio de trabajo*

- **Línea de tiempo del video / Barra de progreso** – Muestra el progreso del video con notas y temas clave extraídos de la pista de audio. Haz clic en cualquier parte de la línea de tiempo para desplazarte por el video. Haz clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.  
- **Captura, Notas, Panel de notas y resumen, Compartir enlace, Subtítulos**  
- No disponible: **Destacar, POV** (estos requieren participantes en vivo)  
- Controles adicionales:
  - **Saltos de 10 segundos** – Avanza/retrocede  
  - **Velocidad de reproducción** – Ajusta la velocidad (0.5×–2×)  
  - **Recortar video** – Recorta el inicio o el final del recurso## 4. Para usuarios anfitriones y administradores - Consola web de Avatour {#for-host-and-admin-users-avatour-web-console}
Cuando inicies sesión en tu Cuenta de Usuario de Avatour, accederás a la **Consola Web**.### 4.1 Consola Web - Menú Principal General {#web-console-overview-main-menu}

En el lado izquierdo, verá los siguientes elementos del menú:

![Avatour Web Console - Main Menu](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Consola Web de Avatour - Menú Principal*

- **Espacios de trabajo** – Organice su contenido de manera eficiente. Cada espacio de trabajo contiene **Activos**, **Colaboradores**, **Reuniones** y **Configuración**.  
- **Activos** – Acceda y administre todos sus activos (videos, imágenes, PDFs). Los administradores pueden ver todos los activos de la cuenta, y los activos compartidos son visibles para todos los usuarios.  
- **Perfil** – Administre su idioma y contraseña.  
- **Analíticas** – Realice un seguimiento de la actividad de las sesiones, el uso del espacio de trabajo y las métricas de ROI.  
- **Configuración** *(Solo administrador)* – Configure los valores predeterminados del espacio de trabajo, reuniones y activos en toda la organización. Los administradores también pueden personalizar la marca (logo, colores, fondos).  
- **Cuenta** *(Solo administrador)* – Administre usuarios registrados y cámaras 360°.  
- **Inicio de sesión del dispositivo** – Ingrese el código que aparece en su cámara 360° para vincularla con su cuenta.  
- **Tutoriales** – Acceda a tutoriales guiados.  
- **Cerrar sesión** – Cierre sesión en la consola.

> Secciones como Perfil, Inicio de sesión del dispositivo, Tutoriales y Cerrar sesión son autoexplicativas y no tienen subsecciones detalladas.

---### 4.2 Consola Web - Detalles por Elemento del Menú (con imágenes) {#web-console-details-by-menu-item}

#### 4.2.1 Espacios de Trabajo

Los espacios de trabajo son unidades organizativas flexibles que le permiten gestionar activos, colaboradores y reuniones en un solo lugar. Puede crear un nuevo espacio de trabajo con el botón **Nuevo Espacio de Trabajo** en la esquina superior derecha.

![Consola Web de Avatour - Elemento del Menú Principal Espacios de Trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web de Avatour - Elemento del Menú Principal Espacios de Trabajo*

Haga clic en el icono de campana para ver un resumen de la actividad del espacio de trabajo durante los últimos 7 días.

![Consola Web de Avatour - Actividades Recientes del Espacio de Trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Actividades Recientes del Espacio de Trabajo*

Dentro de un espacio de trabajo:

![Espacio de Trabajo de Avatour con Panel de Activos, Lienzo en blanco y Panel de Reuniones](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espacio de Trabajo con Activos (izquierda), Lienzo (centro), Reuniones (derecha)*

- **Activos** – Gestione archivos asignados a este espacio de trabajo.  
- **Colaboradores** – 
  Controle el acceso a los espacios de trabajo mediante 
  - **Visualizador** – Puede ver activos. La invitación crea un usuario Invitado si es necesario.  
  - **Editor** – Control total del espacio de trabajo, mismos derechos que el Anfitrión. La invitación actualiza al usuario a Anfitrión si es necesario.  
> Múltiples usuarios pueden acceder a un espacio de trabajo simultáneamente sin una reunión. Los espacios de trabajo públicos y la configuración de acceso a reuniones proporcionan acceso alternativo.  
- **Informe** – Genere un informe usando una plantilla de lista de verificación en los activos seleccionados del espacio de trabajo.  

![Informe del Espacio de Trabajo y Selección de Activos de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe del Espacio de Trabajo y Selección de Activos*

- **Mapa** – Muestre ubicaciones de activos habilitados con GPS en un mapa.  
- **Reuniones** – Organice reuniones en el espacio de trabajo.  
- **Configuración** – Configure valores predeterminados del espacio de trabajo y las reuniones:

![Configuración de Avatour - Vista del Espacio de Trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Configuración del Espacio de Trabajo*

**Configuración del Espacio de Trabajo**

- **Plantilla de Informe** – Seleccione la plantilla de lista de verificación para informes de IA.  
- **Habilitar Notificaciones** – Correos electrónicos de resumen diario para cambios de estado de notas.  

![Notificaciones por Correo Electrónico - Ejemplo](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Ejemplo de Notificaciones por Correo Electrónico*

- **Espacio de Trabajo Público** – Cualquier persona con el enlace puede ver los activos directamente.

**Configuración de Reuniones**
  
* **Autenticación requerida** – Los participantes deben iniciar sesión.  
* **Permitir acceso de invitados** – Permitir que usuarios no registrados vean los activos.  
* **Inicio Automático de Grabación / Inicio Manual** – Elija si las reuniones se graban automáticamente o se inician manualmente.  
* **Requerir anfitrión** – El anfitrión debe admitir a los participantes; la reunión termina cuando el anfitrión se va.  
* **Permitir acceso de espectador** – Unirse sin micrófono ni cámara; comunicarse por chat.  
* **Reuniones protegidas con contraseña** – Requerir una contraseña para unirse.  
* **Mostrar Pregunta de Ahorro en Viajes** – Preguntar a los participantes si la reunión redujo los viajes.  

> Las configuraciones se pueden combinar (por ejemplo, sin requerir anfitrión pero protegida con contraseña).

---

#### 4.2.2 Activos

Gestione todos los videos 360°/2D, imágenes y PDFs. Cargue/descargue activos, asígnelos a espacios de trabajo, compártalos con otros usuarios, renómbrelos, imprima/descargue informes, active el desenfoque de rostros y la resumación por IA.

![Consola Web de Avatour - Elemento del Menú Principal Activos](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Elemento del Menú Principal Activos*

---

#### 4.2.3 Analíticas

Proporciona información sobre reuniones, uso de espacios de trabajo y métricas de ROI.

![Consola Web de Avatour - Elemento del Menú Principal Analíticas (1 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Resumen de Analíticas*

![Consola Web de Avatour - Elemento del Menú Principal Analíticas (2 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Actividad de Reuniones y Uso de Espacios de Trabajo*

![Consola Web de Avatour - Elemento del Menú Principal Analíticas (3 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de Licencias de Dispositivos y ROI*## 5. Onsite - How to Use the Avatour Turnkey Kit {#onsite-how-to-use-the-avatour-turnkey-kit}

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
