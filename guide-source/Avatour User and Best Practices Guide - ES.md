# Avatour User and Best Practices Guide

## 1. Para Todos los Usuarios de Avatour {#for-all-avatour-users}

Si eres nuevo en Avatour, los siguientes recursos proporcionan una introducción útil a la plataforma y sus capacidades:

1. [Video Cómo Funciona Avatour](https://avatour.com/how-it-works)  
Una breve descripción general de las principales características de Avatour y cómo la plataforma permite la colaboración remota inmersiva.
2. [Preguntas Frecuentes](https://avatour.com/faqs)  
Respuestas a preguntas frecuentes en diversas áreas.
3. [Glosario](https://avatour.com/glossary)  
Definiciones de términos y conceptos clave de Avatour.
4. Sitio Web  
Echa un vistazo especialmente a la página de [Características de Avatour](https://avatour.com/features) junto con las secciones dedicadas de Casos de Uso e Industrias para conocer cómo Avatour puede apoyar tus necesidades específicas.## 2. Tipos de Usuarios de Avatour  {#avatour-user-types}

### 2.1 Asistentes a Reuniones (No se requiere cuenta)
Los usuarios pueden unirse a la reunión sin registrarse para obtener una cuenta de Avatour.
Excepción: Si el anfitrión ha restringido la reunión a usuarios registrados — por ejemplo, para permitir que solo los empleados internos se unan mediante Inicio de Sesión Único (SSO) — la invitación del calendario indicará que los participantes deben iniciar sesión para autenticarse.

Los usuarios acceden a la reunión de la siguiente manera:

- Reciben una invitación de calendario del anfitrión.
- Usan el enlace de la reunión en la invitación para unirse.
- Ingresan una contraseña de reunión si el anfitrión ha habilitado una.
- Los participantes pueden unirse sin una cuenta de Avatour a menos que la reunión esté restringida y requiera iniciar sesión para autenticarse.

#### 2.1.1 Participante 

- Puede unirse e interactuar completamente (cámara web, micrófono, chat y funcionalidad de Presentar).
- Máximo de 20 participantes interactivos por reunión.

#### 2.1.2 Espectador

- Puede ver la reunión y participar solo a través del chat.
- No puede compartir video, usar micrófono, presentar, reproducir/pausar Recursos ni capturar Instantáneas.
- Máximo de 10 Espectadores por reunión.
- Junto con los Participantes, una reunión puede alojar hasta 30 asistentes.

### 2.2 Usuarios Registrados

Los Usuarios Registrados tienen una cuenta de Avatour. Las cuentas se crean de una de las siguientes maneras:

- **Invitado por Admin:** Durante la incorporación, Avatour configura un **tenant dedicado** para la organización y crea una o más **cuentas de Admin**. Los Admins pueden entonces **invitar usuarios** dentro de la organización y asignarlos a **grupos**, que definen su rol en la plataforma (Invitado, Anfitrión o Admin). Los usuarios invitados reciben un **enlace de registro** para completar la configuración de la cuenta y establecer una contraseña.  
- **Invitado por Anfitrión:** Los Anfitriones pueden agregar usuarios como **colaboradores Editores** a un Espacio de Trabajo. Esto consume una **licencia de Anfitrión** y asegura que el usuario tenga acceso de nivel Anfitrión.  
- **Auto-aprovisionamiento SSO (solo nivel Enterprise/Business):** Las cuentas pueden ser creadas automáticamente por el IdP. Por defecto, las cuentas aprovisionadas por SSO se agregan al **grupo de Invitados**, a menos que se anule mediante **mapeos de grupos SAML**. Los Admins aún pueden invitar usuarios y asignar membresía de grupo directamente incluso cuando SSO está habilitado.

**Resumen:**  

Los usuarios registrados y su membresía de grupo pueden ser gestionados de múltiples maneras:

- **Gestión por Admin:** Un Admin en la consola de Avatour puede crear usuarios y asignarlos a grupos, que definen su rol en la plataforma (Invitado, Anfitrión o Admin).  
- **Aprovisionamiento SSO:** Para clientes de nivel Enterprise o Business con SSO habilitado, el IdP puede aprovisionar automáticamente cuentas y asignar membresía de grupo, lo que define el rol del usuario en la plataforma.  
- **Usuarios invitados por Anfitrión:** Los Anfitriones pueden invitar a otros usuarios como colaboradores Editores a Espacios de Trabajo específicos. Asignar el rol de colaborador Editor consume una licencia de Anfitrión.

**Mejor Práctica Recomendada (Clientes Enterprise):**  
Para organizaciones que esperan un gran número de usuarios que necesitan acceso a Avatour, se recomienda **integrar Inicio de Sesión Único (SSO)** y gestionar usuarios y membresías de grupo desde el **IdP**. Este enfoque agiliza el aprovisionamiento de cuentas, la asignación de grupos y la gestión de licencias, reduciendo la carga administrativa y asegurando un control de acceso consistente.

#### 2.2.1 Usuarios Invitados

- Agregados al **grupo de Invitados**.  
- Pueden **ver Recursos** dentro de los Espacios de Trabajo donde han sido agregados como **colaboradores Visualizadores**.  
- No pueden crear espacios de trabajo, organizar reuniones ni subir contenido.  
- Las cuentas de Invitados aprovisionadas por SSO **se autentican a través del IdP**; no se requiere contraseña gestionada por Avatour.

---

#### 2.2.2 Usuarios con Licencia (Acceso a la Consola Web)

##### Usuarios Anfitrión (Grupo: Anfitrión)

- Pueden crear/gestionar Espacios de Trabajo, invitar colaboradores a un espacio de trabajo, **organizar reuniones en vivo**, subir **Capturas Rápidas**.  
- Tienen acceso al **Panel de Anfitrión** y a la **App de Operador** en cámaras 360° compatibles.  

##### Usuarios Admin (Grupo: Admin)

- Incluye todas las capacidades de Anfitrión más la administración completa de la cuenta.

**Los privilegios adicionales de Admin incluyen:**

**Gestión de Cuentas**  

- Crear nuevos usuarios y asignarlos a grupos.
- Restablecer contraseñas cuando son gestionadas por Avatour (no aplicable cuando SSO está habilitado). 
- Actualizar usuarios Invitados a Anfitrión.  
- Desactivar usuarios (las cuentas de Admin deben convertirse primero a Anfitrión antes de la eliminación).  
- Transferir recursos de un usuario Anfitrión a otro durante la eliminación.

**Configuración**  

- Configurar **ajustes de seguridad a nivel organizacional** para recursos, espacios de trabajo y reuniones alojadas en la plataforma (por ejemplo, si un Anfitrión debe estar presente para iniciar una reunión, si los rostros deben difuminarse en todos los videos subidos a la plataforma).  
- Habilitar o deshabilitar **funciones de IA** o **grabación**.  
- Aplicar la marca de la empresa de manera consistente en toda la plataforma si se configura un **dominio personalizado**.
  

**Recursos y Analíticas** 
 
- Ver todos los Recursos subidos por cualquier usuario en la organización.  
- Revisar el uso de la plataforma en toda la organización.

---

#### 2.2.3 Permisos de Colaborador de Espacio de Trabajo

Los permisos de espacio de trabajo definen lo que un usuario puede hacer **dentro de un Espacio de Trabajo específico**. Estos son separados de la membresía de grupo a nivel de plataforma (Invitado, Anfitrión, Admin).

- **Colaborador Editor:** Los usuarios con este permiso pueden:
  - Gestionar Recursos (subir, eliminar, difuminar rostros, generar resúmenes)  
  - Gestionar configuración de reuniones (habilitar/deshabilitar grabación, permitir o eliminar participantes)  
  - Programar y organizar reuniones en vivo  
  - Generar informes basados en plantillas predefinidas  
  - Agregar o eliminar colaboradores del Espacio de Trabajo  

- **Colaborador Visualizador:** Los usuarios con este permiso tienen acceso de solo lectura a los Recursos del Espacio de Trabajo. **No pueden modificar Recursos, gestionar reuniones ni gestionar colaboradores**, pero **pueden crear Notas en los Recursos**.## 3. Para Participantes de Reuniones Remotas y Visitantes del Espacio de Trabajo {#for-remote-meeting-participants-and-workspace-visitors}

Avatour permite a los usuarios colaborar de dos formas principales:

- **Unirse a una reunión en vivo:**  
  Puede recibir una **invitación de calendario** para unirse a una reunión de Avatour. Durante la reunión, los participantes pueden realizar una **visita remota en vivo al sitio** o revisar activos de forma sincrónica juntos.

- **Visitar un Espacio de Trabajo:**  
  También puede ser invitado como **colaborador a un Espacio de Trabajo** para revisar activos **de forma asíncrona** (según su propio horario).

### 3.1 Cómo Unirse a una Reunión de Avatour y Visitar un Espacio de Trabajo de Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Cualquier Dispositivo de "Pantalla Plana" con un Navegador Web {#any-flat-screen}
Puede unirse a una reunión de Avatour desde **cualquier computadora de escritorio o portátil, teléfono inteligente o tableta** usando un navegador web.  

##### Unirse a una Reunión

> **Nota:** Unirse a una reunión de Avatour requiere que **otorgue permisos de micrófono**. Por favor, acepte cualquier solicitud de permiso de su navegador.

1. **Mediante invitación de calendario (recomendado):**  
   - Normalmente recibirá una **invitación de calendario** con un **enlace directo para unirse** (por ejemplo: `https://avatour.live/join?s=xxxxx`).  
   - Al hacer clic en el enlace se completará automáticamente el **código de reunión de 5 caracteres** y lo llevará a la reunión.
   - **Autenticación requerida:** Algunas reuniones están restringidas a usuarios registrados. En este caso, la invitación indicará que necesita **iniciar sesión para acceder a la reunión**.  
   - **Reuniones protegidas con contraseña:** Algunas reuniones pueden requerir una contraseña. En ese caso, la invitación incluirá la contraseña que debe ingresar para unirse.

2. **Mediante código de reunión:**  
   - Si el anfitrión comparte un **código de reunión de 5 caracteres** por separado, vaya a [https://avatour.live/join](https://avatour.live/join), ingrese su **nombre** y el **código de reunión**, y únase a la reunión.  
   - Si la reunión está **protegida con contraseña**, ingrese la contraseña proporcionada por el anfitrión.  
   - Si la reunión requiere **autenticación**, necesitará **iniciar sesión con su cuenta de Avatour** antes de unirse.

> **Consejo 1:** Si su cámara o micrófono no funciona, puede estar en uso por otra aplicación (por ejemplo, Microsoft Teams o Zoom). Cierre cualquier aplicación que pueda estar usando su cámara o micrófono, luego salga y vuelva a unirse a la reunión de Avatour.  

> **Consejo 2:** Si aún no puede unirse a la reunión, ejecute esta prueba: [https://avatour.live/test](https://avatour.live/test).  
> La prueba puede identificar si su **firewall corporativo o red** está bloqueando el acceso, y proporcionará información para guiar las discusiones con su equipo de TI.  

> **Consejo 3:** **No** use las aplicaciones de Avatour para iOS o Android para unirse a reuniones. Estas aplicaciones solo son necesarias cuando **transmite una reunión en vivo desde una cámara Insta360**, ya que esas cámaras no pueden ejecutar el software de Avatour 360° directamente y requieren un teléfono inteligente para asistir.

##### Visitar un Espacio de Trabajo Sin Unirse a una Reunión

Puede acceder a un Espacio de Trabajo sin unirse a una reunión en vivo de las siguientes maneras:

- **Espacio de Trabajo Público:**  
  Si el Espacio de Trabajo es público, el enlace se puede acceder directamente—no se requiere inicio de sesión.

- **Espacio de Trabajo Restringido:**  
  Si el Espacio de Trabajo está restringido, debe ser agregado como **colaborador** con permisos de **Editor** o **Visualizador**.

  1. Cuando sea agregado como colaborador, recibirá una **notificación por correo electrónico** con un enlace al Espacio de Trabajo.
  2. Haga clic en el enlace del correo electrónico para abrir el Espacio de Trabajo. Si aún no ha iniciado sesión, se le pedirá que **inicie sesión o complete el registro**.
  3. Una vez que haya iniciado sesión, el Espacio de Trabajo se abrirá automáticamente.

  Alternativamente, puede iniciar sesión en  
  https://avatour.live/login  
  y acceder al Espacio de Trabajo desde su **lista de Espacios de Trabajo**.

#### 3.1.2 Visor de Realidad Virtual {#vr-headset}
Puede unirse a una reunión y visitar un espacio de trabajo desde una variedad de visores compatibles de Meta y Pico. Para hacer esto: 

1. Instale nuestra aplicación Avatour desde su respectiva tienda de aplicaciones de RV: [Cómo instalar la aplicación Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Cargue nuestra aplicación e ingrese el código de reunión o seleccione un Espacio de Trabajo para unirse a una reunión. Para más información sobre cómo usar nuestra aplicación de RV, consulte nuestro artículo de la Base de Conocimientos [aquí](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Herramientas de Colaboración para Reuniones y Espacios de Trabajo {#meeting-tools}

Avatour permite la colaboración en dos contextos principales:

1. **Reuniones (sincrónicas):** Colabore en tiempo real con otros participantes, incluyendo visitas en vivo al sitio o revisando activos grabados juntos.  
2. **Espacios de Trabajo (asíncronos):** Revise e interactúe con activos según su propio horario, 24/7.

Las **herramientas de colaboración son mayormente similares** entre reuniones y espacios de trabajo, con algunas diferencias debido al contexto sincrónico vs asíncrono.

#### 3.2.1 Diseño de la Interfaz

La interfaz de Avatour está organizada alrededor de tres áreas principales:

- **Panel izquierdo** – Activos del espacio de trabajo y herramientas de apoyo  
- **Lienzo central** – Área principal de visualización para video en vivo o activos  
- **Panel derecho** – Información contextual, como participantes, reuniones o chat  

La mayoría de las interacciones se inician desde el **menú inferior**.  
Al hacer clic en una opción del menú se abre un **panel lateral** en el lado izquierdo o derecho de la pantalla, mientras que el **lienzo central** permanece como el área principal de visualización.

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

#### 3.2.4 Resumen del Menú Inferior

El menú inferior proporciona acceso a los controles principales de la interfaz y paneles:

**Menú Inferior de Reunión**  

![Menú Inferior de Reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menú Inferior de Reunión de Avatour*

- **Activos** – Revise archivos del espacio de trabajo, incluyendo videos grabados, imágenes, capturas y PDFs. 
- **Chat** – Envíe mensajes a todos los participantes de la reunión.  
- **Cámara** – Encienda o apague su cámara web.  
- **Micrófono** – Silencie o active su micrófono.  
- **Presentar** – Presente un activo, escritorio o transmisión de cámara web (vea la sección Presentar a continuación).  
- **Herramientas del Anfitrión** (solo anfitriones):  
  - **Bloquear Enfoque** – Bloquee la vista para todos los participantes.  
  - **Silenciar a Todos** – Silencie a todos los participantes.  
- **Habilitar Pantalla Completa** – Ponga la pestaña de la reunión en pantalla completa.  
- **Salir de la Reunión** – Abandone la reunión.  
- **Iniciar Grabación** – Use este botón para iniciar y detener la grabación manualmente durante una reunión. Alternativamente, las reuniones pueden grabarse automáticamente si **el inicio automático de grabación** está habilitado en la configuración del espacio de trabajo. En ambos casos, las grabaciones se guardan en los activos del espacio de trabajo.
- **Mapa** – Abra o cierre el panel del mapa para activos con seguimiento GPS. Al hacer clic en una ubicación salta al punto exacto en el video. El mapa se actualiza en vivo mientras se reproduce el video.
- **Participantes** – Abra o cierre el panel de participantes.  
- **Información de la Reunión** – Vea el código de reunión, enlace de invitación y acceda a tutoriales relacionados.  

![Información de Reunión de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Panel Lateral de Información de Reunión de Avatour*

- **Configuración** – Ajuste el idioma, audio y configuración de video. Para reuniones de video 360° en vivo, use **Mostrar Tasa de Bits** para monitorear estadísticas de conectividad.

> Consejo: Envíe el enlace de la reunión o agréguelo a un elemento del calendario para invitar participantes.

---

##### Menú Presentar

La opción **Presentar** en el menú inferior de la reunión le permite compartir contenido con todos los participantes.

- **Cámara** – Comparta la cámara de su teléfono inteligente/tableta. Esto también se puede usar durante una reunión de video 360° en vivo para superponer una vista secundaria para primeros planos o detalles específicos. 
- **Escritorio** – Comparta la pantalla de su escritorio con todos los participantes.  
- **Activo** – Presente un activo del espacio de trabajo. Al seleccionar un activo se abre la **Barra de herramientas del activo**, que proporciona controles de reproducción y herramientas de colaboración específicas para el activo que se está presentando.

##### Barra de Herramientas del Activo (Reunión)

Al presentar un activo en una reunión, la **Barra de Herramientas del Activo** aparece sobre el lienzo. Aquí están las herramientas y elementos del menú disponibles cuando <u>presenta un Activo en una Reunión</u> - explicados de izquierda a derecha.

![Menú de Avatour mientras Presenta un Activo en una Reunión](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menú de Avatour cuando presenta un Activo en una Reunión*


- **Línea de Tiempo del Video / Barra de Progreso** – Muestra el progreso del video con notas y temas clave extraídos del audio. Haga clic en una nota o tema para saltar a ese momento y abrir la nota. Incluye controles de **Reproducir / Pausar**.   
- **Captura** – Capture una imagen 360° o 2D del activo.  
- **Destacar** – Resalte un área específica para todos los participantes durante sesiones en vivo.  
- **Mostrar/Ocultar Punto de Vista (POV)** – Muestre dónde está mirando cada participante en el video 360°.  
- **Notas** – Cree notas ancladas a momentos específicos en el activo. Las notas pueden categorizarse (Observación, Problema, Acción, Recomendación), rastrearse por estado (Abierto → En Progreso → Resuelto) y compartirse mediante enlaces directos.  

  ![Nota y Filtro de Notas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota y Filtros de Notas de Avatour*

  - **Notas por Comando de Voz** – Estos son marcadores de posición generados automáticamente cuando la grabación detecta menciones como "insertar nota", "tomar una nota" o "hacer una nota". Estas notas aparecen en la línea de tiempo y necesitan ser **posicionadas y finalizadas** por el usuario. 

  ![Notas de Avatour - Generadas por Comando de Voz](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas de Avatour - Generadas por Comando de Voz*

- **Panel de Notas y Resumen** – Abre un panel lateral que muestra todas las notas, temas clave y un resumen ejecutivo del activo. Al hacer clic en un elemento salta a ese momento en el video.  

  ![Resumen Ejecutivo de Activo de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumen Ejecutivo de Avatour mientras presenta un Activo en una Reunión*

  ![Temas de Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *## 4. Para Usuarios Anfitrión y Administrador - Consola Web de Avatour {#for-host-and-admin-users-avatour-web-console}

Cuando inicie sesión en su Cuenta de Usuario de Avatour, accederá a la **Consola Web**.  

### 4.1 Consola Web - Menú Principal General {#web-console-overview-main-menu}

En el lado izquierdo, verá los siguientes elementos del menú:

![Consola Web de Avatour - Menú Principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Consola Web de Avatour - Menú Principal*

- **Espacios de Trabajo** – Organice su contenido de manera eficiente. Cada espacio de trabajo contiene **Activos**, **Colaboradores**, **Reuniones** y **Configuración**.  
- **Activos** – Acceda y gestione todos sus activos (videos, imágenes, PDFs). Los administradores pueden ver todos los activos de la cuenta, y los activos compartidos son visibles para todos los usuarios.  
- **Perfil** – Gestione su idioma y contraseña.  
- **Analíticas** – Realice seguimiento de la actividad de sesiones, uso de espacios de trabajo y métricas de ROI.  
- **Configuración** *(Solo administrador)* – Configure los valores predeterminados de espacios de trabajo, reuniones y activos en toda la organización. Los administradores también pueden personalizar la marca (logo, colores, fondos).  
- **Cuenta** *(Solo administrador)* – Gestione usuarios registrados y cámaras 360°.  
- **Inicio de Sesión de Dispositivo** – Ingrese el código mostrado en su cámara 360° para vincularla con su cuenta.  
- **Tutoriales** – Acceda a tutoriales guiados.  
- **Cerrar sesión** – Salga de la consola.

> Secciones como Perfil, Inicio de Sesión de Dispositivo, Tutoriales y Cerrar sesión son autoexplicativas y no tienen subsecciones detalladas.

---

### 4.2 Consola Web - Detalles por Elemento del Menú (con imágenes) {#web-console-details-by-menu-item}

#### 4.2.1 Espacios de Trabajo

Los espacios de trabajo son unidades organizativas flexibles que le permiten gestionar activos, colaboradores y reuniones en un solo lugar. Puede crear un nuevo espacio de trabajo con el botón **Nuevo Espacio de Trabajo** en la esquina superior derecha.

![Consola Web de Avatour - Elemento del Menú Principal Espacios de Trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Consola Web de Avatour - Elemento del Menú Principal Espacios de Trabajo*

Haga clic en el icono de campana para ver un resumen de la actividad del espacio de trabajo en los últimos 7 días.

![Consola Web de Avatour - Actividades Recientes del Espacio de Trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Actividades Recientes del Espacio de Trabajo*

Dentro de un espacio de trabajo:

![Espacio de Trabajo de Avatour con Panel de Activos, Lienzo en blanco y Panel de Reuniones](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espacio de Trabajo con Activos (izquierda), Lienzo (centro), Reuniones (derecha)*

- **Activos** – Gestione archivos asignados a este espacio de trabajo.  
- **Colaboradores** – 
  Controle el acceso a los espacios de trabajo mediante 
  - **Visualizador** – Puede ver activos. La invitación crea un usuario Invitado si es necesario.  
  - **Editor** – Control total del espacio de trabajo, mismos derechos que el Anfitrión. La invitación actualiza al usuario a Anfitrión si es necesario.  
> Múltiples usuarios pueden acceder a un espacio de trabajo simultáneamente sin una reunión. Los espacios de trabajo públicos y la configuración de acceso a reuniones proporcionan acceso alternativo.  
- **Informe** – Genere un informe usando una plantilla de lista de verificación sobre los activos seleccionados del espacio de trabajo.  

![Informe de Espacio de Trabajo de Avatour y Selección de Activos](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Informe de Espacio de Trabajo y Selección de Activos*

- **Mapa** – Muestre ubicaciones de activos habilitados con GPS en un mapa.  
- **Reuniones** – Organice reuniones en el espacio de trabajo.  
- **Configuración** – Configure los valores predeterminados del espacio de trabajo y reuniones:

![Configuración de Avatour - Vista del Espacio de Trabajo](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Configuración del Espacio de Trabajo*

**Configuración del Espacio de Trabajo**

- **Plantilla de Informe** – Seleccione la plantilla de lista de verificación para informes de IA.  
- **Habilitar Notificaciones** – Correos electrónicos de resumen diario para cambios de estado de notas.  

![Notificaciones por Correo Electrónico - Ejemplo](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Ejemplo de Notificaciones por Correo Electrónico*

- **Espacio de Trabajo Público** – Cualquier persona con el enlace puede ver los activos directamente.

**Configuración de Reuniones**
  
* **Autenticación requerida** – Los participantes deben iniciar sesión.  
* **Permitir acceso de invitados** – Permitir que usuarios no registrados vean activos.  
* **Inicio Automático de Grabación / Inicio Manual** – Elija si las reuniones se graban automáticamente o se inician manualmente.  
* **Requerir anfitrión** – El anfitrión debe admitir participantes; la reunión termina cuando el anfitrión se va.  
* **Permitir acceso de espectador** – Unirse sin micrófono o cámara; comunicarse por chat.  
* **Reuniones protegidas con contraseña** – Requerir una contraseña para unirse.  
* **Mostrar Pregunta de Ahorro de Viaje** – Preguntar a los participantes si la reunión redujo los viajes.  

> Las configuraciones se pueden combinar (ej., sin anfitrión requerido pero protegido con contraseña).

---

#### 4.2.2 Activos

Gestione todos los videos 360°/2D, imágenes y PDFs. Cargue/descargue activos, asigne a espacios de trabajo, comparta con otros usuarios, renombre, imprima/descargue informes, active el desenfoque de rostros y la resumización con IA.

![Consola Web de Avatour - Elemento del Menú Principal Activos](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Elemento del Menú Principal Activos*

---

#### 4.2.3 Analíticas

Proporciona información sobre reuniones, uso de espacios de trabajo y métricas de ROI.

![Consola Web de Avatour - Elemento del Menú Principal Analíticas (1 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Resumen de Analíticas*

![Consola Web de Avatour - Elemento del Menú Principal Analíticas (2 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Actividad de Reuniones y Uso de Espacios de Trabajo*

![Consola Web de Avatour - Elemento del Menú Principal Analíticas (3 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de Licencias de Dispositivos y ROI*## 5. En el sitio - Cómo usar el Kit Llave en Mano de Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Primeros pasos
[Guía de inicio rápido – Kit Llave en Mano de Avatour 3.1 (configuración Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

Siga la guía para desempacar, ensamblar y encender su cámara.

---

### 5.2 Consejos útiles

#### Batería externa – Reuniones en vivo más largas y mejor gestión térmica 

- **Si su kit incluye una batería Ulanzi:** Fíjela entre la base del trípode y el palo extensible, luego conecte la batería a la cámara mediante USB-C.  

- **Si su kit incluye un palo con batería Telesin:** Monte la cámara directamente en el palo extensible con batería Telesin y conéctela mediante USB-C.  

Usar la batería externa:

1. Extiende la duración total de la batería de ~40 minutos (solo batería de la cámara) a ~3 horas.  
2. Añade estabilidad a la configuración de la cámara.  
3. Ayuda a prevenir el posible sobrecalentamiento.  

> Recomendamos usar siempre la batería externa desde el principio, especialmente para reuniones en vivo.

#### Consideraciones de audio para reuniones en vivo y grabaciones

- **Entornos ruidosos:** 
  Use los auriculares Shokz incluidos en su kit para una captura de audio clara.  
  - **Encender/Apagar:** Mantenga presionado el botón "+" durante 3 segundos (LED azul = encendido, LED rojo = apagado).  
  - **Modo de emparejamiento Bluetooth:** Con los auriculares apagados, mantenga presionado el botón "+" durante 5 segundos (el LED parpadea azul/rojo).  
  - **Volumen:** Use los botones "+" y "-".  

- **Entornos más silenciosos / múltiples participantes cerca de la cámara:** 
  Use el altavoz de clip NoxGear. No es de tan alta fidelidad como los altavoces de conferencia (por ejemplo, Jabra Speak), pero es fácil de sujetar a su camisa y captura eficazmente las voces cercanas.  
  - **Encender/Apagar:** Mantenga presionado el botón Reproducir/Pausar durante 2 segundos.  
  - **Modo de emparejamiento Bluetooth:** Entra automáticamente en modo de emparejamiento al encenderse (el LED parpadea azul/rojo; azul fijo cuando está emparejado).  
  - **Volumen:** Use los botones "+" y "-".  

- **Usar su propio dispositivo:** Si prefiere una alternativa (por ejemplo, un altavoz de conferencia o auriculares personales), puede emparejarlo a través de la cámara: Configuración → Bluetooth.  

#### Conectividad, conectividad, conectividad
**Antes de comenzar:** Asegure la conexión a internet mediante:

- **WiFi local** (preferido)
- **Red móvil** (si está fuera del alcance del WiFi)

**Ancho de banda recomendado:** 10 Mbps de subida/bajada para transmisión completa en 360° (~5 Mbps). Un ancho de banda menor (1–2 Mbps) solo funciona estando quieto.

##### Probar velocidad de red
- **Prueba de ubicación única:** Cualquier medidor de velocidad que use normalmente (por ejemplo, [Speedtest](https://www.speedtest.net)) para verificar el ancho de banda de subida.   
- **Prueba caminando por el sitio:** Desde la cámara: Configuración → Red → Prueba de conexión. Camine por todo el espacio para confirmar cobertura y ancho de banda.

##### WiFi local
- Altamente recomendado para conexiones estables.  
- Si TI requiere lista blanca, encuentre la dirección MAC: Configuración → Acerca de → Dirección WiFi.

##### Red móvil
**Opción A: Hotspot y SIM proporcionados en el kit**  

- Fije el hotspot GlocalMe al palo con batería Telesin (imán).  
- Asegura que no haya interferencia y mantiene la conexión si se aleja de la cámara.  
- Solución de problemas:
  - Confirme que la SIM esté preinstalada (no Cloud SIM).  
  - Habilite 5G en el Administrador de tarjetas SIM.  
  - Verifique el APN correcto para su región ([guía de configuración de APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opción B: Hotspot personal / SIM**
- Use su propio smartphone o hotspot dedicado.  

**Nota importante:**  
> Mantenga el hotspot apagado mientras está conectado a WiFi; actívelo solo cuando esté fuera del alcance. El sistema operativo de la cámara cambia dinámicamente entre redes WiFi según la intensidad de la señal y puede cambiar inadvertidamente al hotspot incluso cuando el WiFi está disponible.

> Las redes móviles pueden limitar el ancho de banda inesperadamente. Consulte con su operador sobre los límites de su plan de datos, o contacte al soporte de Avatour si usa nuestro hotspot y SIM.

##### Situaciones de bajo ancho de banda
- Grabe previamente videos de ubicación para reproducción posterior ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Comparta una transmisión de cámara de smartphone para complementar áreas de bajo ancho de banda (0.1–0.3 Mbps de subida).

##### Sin conectividad
- Solo se puede usar video pregrabado ([guía de grabación](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Otros participantes en el sitio – Mejores prácticas

Cuando múltiples participantes se unen a una reunión en vivo de Avatour desde la misma ubicación que la cámara 360°, la gestión cuidadosa del **audio y el ancho de banda** es crucial:  

- Cada smartphone, tablet o laptop conectado en el sitio consume ancho de banda de red y puede impactar negativamente la transmisión de la cámara 360°.  
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo desagradable la experiencia de la reunión para todos los participantes.

#### Otros participantes en el sitio – Mejores prácticas

Cuando múltiples participantes se unen a una reunión en vivo de Avatour desde la misma ubicación que la cámara 360°, la gestión cuidadosa del **audio y el ancho de banda** es crucial:  

- Cada smartphone, tablet o laptop conectado en el sitio consume ancho de banda de red y puede impactar negativamente la transmisión de la cámara 360°.  
- Múltiples micrófonos y altavoces en el mismo espacio pueden causar **retroalimentación de audio**, haciendo desagradable la experiencia de la reunión para todos los participantes.

Para abordar estos desafíos, siga estas **mejores prácticas**:

- **Use auriculares con cable o inalámbricos:** Preferiblemente con cancelación de ruido para prevenir eco y retroalimentación.  
- **Modo en el sitio:** Únase a la reunión en modo En el sitio cuando esté físicamente presente cerca de la cámara 360°.  
  - Este modo está optimizado para uso en el sitio:  
    - Silencia el micrófono y altavoz del participante por defecto.  
    - **No** envía la transmisión de la cámara del participante.  
    - **No** muestra la transmisión de la cámara 360° en el navegador del participante.  
    - Conserva el ancho de banda de red, asegurando que la cámara 360° tenga la máxima subida disponible para la transmisión en vivo.  
    - Útil cuando un usuario quiere compartir detalles específicos; **puede compartir su cámara** para vistas específicas.  
- **Silenciar cuando no esté hablando activamente:** Previene retroalimentación de audio no deseada y distracciones.  
- **Use una red separada si es posible:** Conecte su smartphone a una red diferente a la de la cámara para reducir interferencias.  

Seguir estas pautas asegura un tour en vivo fluido y de alta calidad tanto para participantes en el sitio como remotos.

### 5.3 Aplicación de cámara Avatour

Aquí están (1) el Nivel superior, (2) Configuración y (3) los menús de Configuración de red.

![Aplicación de cámara 360° Avatour - Tres menús](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Aplicación de cámara 360° Avatour - 3 menús*

**Captura rápida** - Para grabación de video 360° sin conexión. - Para una descripción detallada vea [¿Cómo grabar y subir videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Recomendamos usar un dispositivo de audio externo (conectado vía bluetooth). Nota: También puede hacer videos e imágenes 2D estándar - simplemente cambie el modo entre 360° y 2D en la esquina inferior derecha una vez en la pantalla de CR.

**Reunión en vivo** - Para videoconferencias en vivo 360°. Verá sus espacios de trabajo y al hacer clic en uno iniciará la transmisión de video en vivo desde la cámara 360°. Antes de poder unirse a la reunión con su cámara 360° necesita conectar un dispositivo de audio vía bluetooth. Para una descripción detallada vea [¿Cómo iniciar una reunión de Captura en vivo con su cámara Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Al organizar una reunión de Captura en vivo con su cámara 360, tendrá herramientas de reunión similares disponibles que reflejan la experiencia web. Aquí hay un enlace a nuestro artículo de la Base de conocimientos que explica estas herramientas con más detalle: [Herramientas de la aplicación del operador](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galería** - Encuentre aquí todos sus videos e imágenes 360° para subir a la Consola web de Avatour.

**Configuración** - Dentro de Configuración, tiene las siguientes opciones:

- **Red**: Esta opción le permite cambiar a qué red WiFi está conectada la cámara o ejecutar una prueba de conexión de red para ver su rendimiento de transmisión
- **Captura en vivo**: Ajuste la configuración de Captura en vivo dependiendo del ancho de banda disponible, la sensibilidad a RV de los invitados, o si las lentes protectoras de su cámara están instaladas:
  - **Tasa de fotogramas objetivo**: Ajuste la tasa de fotogramas para su video de Captura en vivo entre 15 fps, 24 fps y 30 fps. Tasas de fotogramas más altas producen un video más fluido, pero requerirán más ancho de banda de subida. Predeterminado: 15 fps
  - **Tasa de bits objetivo**: Le permite aumentar o disminuir la tasa de bits máxima de transmisión para su Captura en vivo. Puede establecer su tasa de bits objetivo entre 1 Mbps y 10 Mbps. Tasas de bits más altas resultarán en mayor resolución de video, pero requerirán más ancho de banda de subida. Predeterminado: 5 Mbps
  - **Optimizar movimiento**: Esto disminuirá la tasa de fotogramas del video, generando menos carga en el ancho de banda de subida de su red, y aumentará su tasa de bits de transmisión. Además, esta opción ayuda a reducir el mareo por movimiento para participantes de RV. Predeterminado: Desactivado
  - **Lentes protectoras**: Esto afectará cómo se une el video 360° dependiendo de si las lentes protectoras han sido instaladas en su cámara. Si no tiene lentes protectoras, configure esto en "No". Si recibió un Kit 3.0, tiene lentes protectoras preinstaladas y debe configurar esto en "Sí". Predeterminado: Sí

- **Captura rápida**: Ajuste la configuración de Captura rápida dependiendo de su tasa de fotogramas de video preferida, ancho de banda disponible para subidas de video grabado, o si las lentes protectoras de su cámara están instaladas. Captura rápida tiene una resolución establecida de 4k que generalmente logra un buen equilibrio entre calidad de video y tamaño de archivo. (Para resoluciones más altas puede usar las aplicaciones nativas de la cámara, también en la PanoX V2, para detalles vea [¿Cómo grabar y subir videos 360 con la aplicación Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Tasa de fotogramas objetivo**: Ajuste la tasa de fotogramas para sus grabaciones de video de Captura rápida entre 15 fps, 24 fps y 30 fps. Tasas de fotogramas más altas producen un video más fluido, pero aumentarán el tamaño del archivo de video y el tiempo de subida. Recomendado: 30 fps
  - **Tasa de bits objetivo**: Establezca la tasa de bits objetivo para subidas de Captura rápida entre 5 Mbps y 20 Mbps. Tasas de bits más bajas aumentan las velocidades de subida, pero disminuirán la calidad del video. Recomendado: 20 Mbps
  - **Lentes protectoras**: *Vea la sección de Lentes protectoras para Captura en vivo arriba*
- **Acerca de**: Vea el número de serie del dispositivo y la versión del software

**Cuenta** - Para iniciar sesión con su cuenta de anfitrión o administrador de Avatour.## 6. Consejos de Mejores Prácticas {#best-practice-advice}

### 6.1 Primeros Usos (Informales) y Familiarización

Para sus primeros usos y familiarización con la Consola Web de Avatour y el Kit Llave en Mano de Avatour, recomendamos los siguientes pasos:

1. Lleve el kit a casa y pruébelo con familiares y amigos usando su conexión de internet doméstica.
2. Lleve el kit a la oficina y conéctelo a una red corporativa (pueden surgir problemas corporativos, por ejemplo, firewalls corporativos - pero usted sabe por el paso uno que Avatour funciona y este es un tema a resolver por su equipo de TI con la ayuda de Avatour).
3. Comience a usar Avatour en sitio (fuera de su oficina) en el lugar de reunión al que normalmente los participantes remotos necesitarían viajar. Pueden surgir más temas de conectividad. Avatour ayudará en cooperación con su equipo de TI.
4. Comience a usar con participantes remotos internos y externos.

### 6.2 Antes de una Reunión en Vivo con Video 360°

- Recomendamos hacer un recorrido en video 360° grabado antes de cualquier recorrido en vivo si el tiempo lo permite por tres razones: (1) Tener una solución de respaldo para el recorrido en vivo, (2) tener algo para documentación y revisión posterior (además del recorrido en vivo grabado) y (3) comenzar a crear una biblioteca de videos 360° de todos sus sitios que puede ser útil para muchos casos de uso.
- Todos los componentes del kit cargados durante al menos 90 minutos antes de la reunión en vivo. De todos modos, recomendamos tener todos los dispositivos en carga continua cuando no estén en uso. De esta manera, todos los dispositivos siempre estarán listos, también para reuniones ad hoc no planificadas.
- Tenga el kit completamente ensamblado (1. base del trípode + 2. batería Ulanzi + 3. palo extensible + 4. cámara 360°).

- Confirme que se ha creado un Espacio de Trabajo para alojar una reunión en vivo e incluya todos los Activos relevantes.

- Invite a todos los participantes a la reunión a través de su Espacio de Trabajo. Esto crea una invitación en los calendarios de todos los participantes e incluye el enlace de invitación a la reunión.

- Empareje y conecte sus auriculares o altavoz bluetooth que planea usar para su recorrido a la cámara.

- Todos los usuarios de smartphones en sitio deben conectarse desde una red diferente a la red de la cámara. Esto reducirá la carga en el ancho de banda de la red de la cámara.

- Si está solo como operador de cámara, lleve un smartphone consigo en caso de que quiera compartir la cámara del smartphone y mostrar detalles finos.

- Confirme que la cámara 360 puede conectarse a su WiFi local.

- Antes de una reunión de Avatour, planifique la ruta que tomará a través de las instalaciones. Haga una reunión de prueba de Avatour con la cámara y verifique que todas las áreas tengan tasas de bits superiores a 1 Mbps de ancho de banda. Esto se puede ver en la pantalla de la cámara misma, o como participante remoto yendo a Configuración y activando Mostrar Tasa de Bits.

- Si nota que algunas áreas tienen poco o ningún ancho de banda, es mejor tomar imágenes o una grabación. Estas pueden luego presentarse durante la reunión para que los participantes remotos las revisen. Puede seguir la guía aquí que explica nuestra Captura Rápida para grabar y subir videos/imágenes: [How do you record and upload 360 videos with the Avatour App?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Si tiene participantes remotos que se unen a la reunión y no han usado Avatour antes, proporcióneles un breve resumen de la plataforma, su funcionalidad (video en vivo 360, activos, capturas, anotaciones, destacar) y las herramientas de reunión.

- Puede comenzar en otra solución de videoconferencia (por ejemplo, Teams, Zoom, Google Meet) pero antes de pasar a Avatour, cierre completamente la otra aplicación de videoconferencia. En algunos casos, estas otras aplicaciones priorizarán el micrófono/altavoces/cámara web de su dispositivo, causando que se deshabiliten para Avatour. Además, NO ejecute Avatour Y otra videoconferencia al mismo tiempo ya que esto reducirá el ancho de banda disponible.

- Si planea usar la cámara 360 en un entorno de alta temperatura, se recomienda usar el módulo de enfriamiento (solo Pilot Pano). Esto ayudará a reducir las posibilidades de que la cámara se sobrecaliente y se apague automáticamente.

### 6.3 Al Operar la Cámara en Sitio para una Reunión en Vivo con Video 360°

- Al operar la cámara, asegúrese de caminar lentamente. Esto ayuda con la calidad del video y reduce cualquier posible tiempo de inactividad del video cuando la conexión de red de la cámara cambia entre puntos de acceso WiFi.

- Sostenga la cámara frente a usted y por encima del nivel de los ojos. Esto permite que todos los participantes remotos vean la mayoría de su área circundante.

- Para instancias donde la cámara necesita permanecer estable, use el soporte del trípode y extienda la cámara a la altura correcta, preferiblemente al nivel de los ojos.

- Siempre conecte la cámara a su red WiFi local cuando sea posible. Para áreas sin acceso WiFi, use el hotspot proporcionado. El hotspot tiene una tarjeta SIM que se conectará a una red celular confiable cerca de usted. Siempre mantenga el hotspot apagado cuando no esté en uso en interiores, ya que de lo contrario la cámara 360° podría conectarse al hotspot, lo cual no queremos en interiores. Cuando esté en exteriores, mantenga el hotspot cerca de la cámara 360°.

- Cuando la tasa de bits en la cámara comience a caer por debajo de 2 Mbps, camine más lento o deténgase completamente hasta que la señal se estabilice nuevamente. Esto generalmente sucede cuando cambia de un Punto de Acceso WiFi a otro.

- Si sabe que la conectividad y el video se caerán al moverse a una ubicación específica (Ejemplo: moverse de un área de producción interior a un área exterior), avise a los participantes remotos con anticipación.

- Si necesita mostrar algo con alto detalle o escritura pequeña, use su propio smartphone o el de un participante en sitio para unirse a la reunión y presentar la cámara (trasera) de su teléfono / el de ellos.

- Si es posible, recomendamos que una persona adicional esté en sitio para ayudar con el compartir cámara del smartphone descrito anteriormente, ya que esto a menudo resulta ser útil / necesario.

- Idealmente, los usuarios de smartphones en sitio deben unirse a la reunión (1) en modo en sitio y (2) en una red diferente de la que usa la cámara para no quitar ancho de banda de subida crucial de la cámara 360°.

- Todos los participantes en sitio que se unan desde su smartphone deben estar silenciados, a menos que estén hablando activamente.