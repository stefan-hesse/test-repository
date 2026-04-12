# Avatour User and Best Practices Guide

## 1. Para todos os usuários do Avatour {#for-all-avatour-users}

Se você é novo no Avatour, os recursos a seguir oferecem uma introdução útil à plataforma e aos seus recursos:

1. [Vídeo "Como funciona o Avatour"](https://avatour.com/how-it-works)  
Uma breve visão geral dos principais recursos do Avatour e de como a plataforma possibilita uma colaboração remota imersiva.
2. [Perguntas frequentes](https://avatour.com/faqs)  
Respostas às perguntas mais frequentes.
3. [Glossário](https://avatour.com/glossary)  
Definições dos principais termos e conceitos do Avatour usados com frequência.
4. Site  
Dê uma olhada especialmente nas [Funcionalidades do Avatour](https://avatour.com/features), juntamente com as seções dedicadas a Casos de Uso e Setores, para saber como o Avatour pode atender às suas necessidades específicas.

## 2. Tipos de usuários do Avatour  {#avatour-user-types}

### 2.1 Participantes da reunião (não é necessária conta)
Os usuários podem participar da reunião sem se cadastrar para uma conta Avatour.
Exceção: se o organizador tiver restringido a reunião a usuários cadastrados — por exemplo, para permitir que apenas funcionários internos participem por meio do Single Sign-On (SSO) —, o convite do calendário indicará que os participantes devem fazer login para se autenticar.

Os usuários acessam a reunião da seguinte forma:

- Recebem um convite de calendário do anfitrião.
- Usam o link da reunião no convite para participar.
- Digitam uma senha da reunião, caso o anfitrião tenha ativado uma.
- Os participantes podem participar sem uma conta Avatour, a menos que a reunião seja restrita e exija login para autenticação.

#### 2.1.1 Participante 

- Pode participar e interagir plenamente (webcam, microfone, chat e funcionalidade de apresentação).
- Máximo de 20 participantes interativos por reunião.

#### 2.1.2 Espectador

- Pode assistir à reunião e participar apenas por chat.
- Não pode compartilhar vídeo, usar microfone, fazer apresentações, reproduzir/pausar recursos ou capturar instantâneos.
- Máximo de 10 espectadores por reunião.
- Juntamente com os participantes, uma reunião pode acomodar até 30 participantes.

### 2.2 Usuários registrados

Os usuários registrados possuem uma conta no Avatour. As contas são criadas de uma das seguintes maneiras:

- **Convidado pelo administrador:** Durante a integração, o Avatour configura um **tenant dedicado** para a organização e cria uma ou mais **contas de administrador**. Os administradores podem então **convidar usuários** dentro da organização e atribuí-los a **grupos**, que definem sua função na plataforma (Convidado, Anfitrião ou Administrador). Os usuários convidados recebem um **link de cadastro** para concluir a configuração da conta e definir uma senha.  
- **Convidado pelo anfitrião:** Os anfitriões podem adicionar usuários como **colaboradores editores** a um Espaço de Trabalho. Isso consome uma **licença de Anfitrião** e garante que o usuário tenha acesso no nível de Anfitrião.  
- **Provisionamento automático de SSO (apenas nos planos Enterprise/Business):** As contas podem ser criadas automaticamente pelo IdP. Por padrão, as contas provisionadas por SSO são adicionadas ao **grupo de Convidados**, a menos que sejam substituídas por meio de **mapeamentos de grupos SAML**. Os administradores ainda podem convidar usuários e atribuir associação a grupos diretamente, mesmo quando o SSO está habilitado.

**Resumo:**  

Os usuários registrados e sua associação a grupos podem ser gerenciados de várias maneiras:

- **Gerenciamento por administrador:** Um administrador no console do Avatour pode criar usuários e atribuí-los a grupos, o que define sua função na plataforma (Convidado, Anfitrião ou Administrador).  
- **Provisionamento de SSO:** Para clientes dos planos Enterprise ou Business com SSO ativado, o IdP pode provisionar contas automaticamente e atribuir associação a grupos, o que define a função do usuário na plataforma.  
- **Usuários convidados pelo Anfitrião:** Os Anfitriões podem convidar outros usuários como colaboradores Editores para Espaços de Trabalho específicos. Atribuir a função de colaborador Editor consome uma licença de Anfitrião.

**Prática recomendada (clientes Enterprise):**  
Para organizações que esperam um grande número de usuários que precisam acessar o Avatour, recomenda-se **integrar o Single Sign-On (SSO)** e gerenciar usuários e associações a grupos a partir do **IdP**. Essa abordagem simplifica o provisionamento de contas, a atribuição de grupos e o gerenciamento de licenças, reduzindo a sobrecarga administrativa e garantindo um controle de acesso consistente.

#### 2.2.1 Usuários convidados

- Adicionados ao **grupo de convidados**.  
- Podem **visualizar ativos** nos espaços de trabalho onde foram adicionados como **colaboradores visualizadores**.  
- Não podem criar espaços de trabalho, hospedar reuniões ou fazer upload de conteúdo.  
- As contas de convidados provisionadas por SSO **são autenticadas via IdP**; não é necessária nenhuma senha gerenciada pelo Avatour.

---

#### 2.2.2 Usuários licenciados (acesso ao console web)

##### Usuários anfitriões (Grupo: Anfitrião)

- Pode criar/gerenciar Espaços de Trabalho, convidar colaboradores para um espaço de trabalho, **organizar reuniões ao vivo**, enviar **Capturas Rápidas**.  
- Tem acesso ao **Painel do Anfitrião** e ao **Aplicativo do Operador** em câmeras 360° compatíveis.  

##### Usuários Administradores (Grupo: Admin)

- Inclui todos os recursos do Anfitrião, além da administração completa da conta.

**Privilégios adicionais de administrador incluem:**

**Gerenciamento de contas**  

- Criar novos usuários e atribuí-los a grupos.
- Redefinir senhas quando gerenciadas pelo Avatour (não aplicável quando o SSO está habilitado). 
- Atualizar usuários convidados para Anfitriões.  
- Desativar usuários (as contas de administrador devem primeiro ser convertidas para Anfitrião antes da exclusão).  
- Transferir ativos de um usuário Anfitrião para outro durante a exclusão.

**Configurações**  

- Configurar **configurações de segurança para toda a organização** para ativos, espaços de trabalho e reuniões hospedadas na plataforma (por exemplo, se um Anfitrião deve estar presente para iniciar uma reunião, se os rostos devem ser desfocados em todos os vídeos enviados para a plataforma).  
- Ativar ou desativar **recursos de IA** ou **gravação**.  
- Aplicar a identidade visual da empresa de maneira consistente em toda a plataforma, caso um **domínio personalizado** esteja configurado.
  

**Ativos e Análises** 
 
- Visualizar todos os ativos enviados por qualquer usuário da organização.  
- Analisar o uso da plataforma em toda a organização.

---

#### 2.2.3 Permissões de colaborador do espaço de trabalho

As permissões do espaço de trabalho definem o que um usuário pode fazer **dentro de um espaço de trabalho específico**. Elas são distintas da associação a grupos no nível da plataforma (Convidado, Anfitrião, Administrador).

- **Colaborador Editor:** Usuários com essa permissão podem:
  - Gerenciar ativos (carregar, remover, desfocar rostos, gerar resumos)  
  - Gerenciar configurações de reunião (ativar/desativar gravação, permitir ou remover participantes)  
  - Agendar e hospedar reuniões ao vivo  
  - Gerar relatórios com base em modelos predefinidos  
  - Adicionar ou remover colaboradores do Espaço de Trabalho  

- **Colaborador visualizador:** Usuários com essa permissão têm acesso somente para leitura aos ativos do Espaço de Trabalho. Eles **não podem modificar ativos, gerenciar reuniões ou gerenciar colaboradores**, mas **podem criar notas nos ativos**. 
  
## 3. Para participantes de reuniões remotas e visitantes do espaço de trabalho {#for-remote-meeting-participants-and-workspace-visitors}

O Avatour permite que os usuários colaborem de duas maneiras principais:

- **Participar de uma reunião no Avatour (Colaboração Sincrônica):**  
  Você pode receber um **convite de calendário** para participar de uma reunião no Avatour. Durante a reunião, os participantes podem realizar uma **visita remota ao local em tempo real** ou analisar recursos em conjunto de forma sincrônica.

- **Visitar um Espaço de Trabalho (Colaboração Assíncrona):**  
  Você também pode ser convidado como **colaborador de um Espaço de Trabalho** para revisar ativos **de forma assíncrona** (conforme sua própria disponibilidade).

### 3.1 Como participar de uma reunião do Avatour e visitar um Espaço de Trabalho do Avatour {#how-to-join-an-avatour-meeting-and-visit-an-avatour-workspace}
#### 3.1.1 Qualquer dispositivo com "tela plana" e navegador da Web {#any-flat-screen}
Você pode participar de uma reunião do Avatour a partir de **qualquer computador desktop ou laptop, smartphone ou tablet** usando um navegador da web.  

##### Participando de uma reunião do Avatour

> **Observação:** Para participar de uma reunião do Avatour, é necessário **conceder permissões de microfone**. Aceite todas as solicitações de permissão do seu navegador.

1. **Por meio de convite de calendário (recomendado):** 
 - Normalmente, você receberá um **convite de calendário** com um **link de acesso direto** (por exemplo: `https://avatour.live/join?s=xxxxx`). 
 - Ao clicar no link, o **código da reunião de 5 caracteres** será preenchido automaticamente e você será direcionado para a reunião.
   - **Autenticação necessária:** Algumas reuniões são restritas a usuários registrados. Nesse caso, o convite indicará que você precisa **fazer login para acessar a reunião**. 
 - **Reuniões protegidas por senha:** Algumas reuniões podem exigir uma senha. Nesse caso, o convite incluirá a senha que você deve inserir para participar.

2. **Por meio do código da reunião:**  
   - Se o anfitrião compartilhar um **código de reunião de 5 caracteres** separadamente, acesse [https://avatour.live/join](https://avatour.live/join), insira seu **nome** e o **código de reunião** e participe da reunião. 
 - Se a reunião for **protegida por senha**, insira a senha fornecida pelo anfitrião.  
   - Se a reunião exigir **autenticação**, você precisará **fazer login com sua conta do Avatour** antes de participar.

> **Dica 1:** Se sua câmera ou microfone não funcionar, pode ser que estejam sendo usados por outro aplicativo (por exemplo, Microsoft Teams ou Zoom). Feche todos os aplicativos que possam estar usando sua câmera ou microfone e, em seguida, saia e volte a participar da reunião do Avatour.  

> **Dica 2:** Se você ainda não conseguir participar da reunião, execute este teste: [https://avatour.live/test](https://avatour.live/test).  
> O teste pode identificar se o **firewall ou a rede corporativa** está bloqueando o acesso e fornecerá informações para orientar as discussões com sua equipe de TI.  

> **Dica 3:** **Não** use os aplicativos Avatour para iOS ou Android para participar de reuniões. Esses aplicativos são necessários apenas ao **transmitir uma reunião ao vivo a partir de uma câmera Insta360**, já que essas câmeras não podem executar o software Avatour 360° diretamente e precisam de um smartphone para auxiliar.

##### Acessando um Espaço de Trabalho Avatour (sem participar de uma Reunião Avatour)

Você pode acessar um Espaço de Trabalho das seguintes maneiras:

- **Espaço de Trabalho Público:**  
  Se o Espaço de Trabalho for público, o link pode ser acessado diretamente — sem necessidade de login.

- **Espaço de Trabalho Restrito:**  
  Se o Espaço de Trabalho for restrito, você deve ser adicionado como **colaborador** com permissões de **Editor** ou **Visualizador**.

  1. Quando você for adicionado como colaborador, receberá uma **notificação por e-mail** com um link para o Espaço de Trabalho.
  2. Clique no link do e-mail para abrir o Espaço de Trabalho. Se você ainda não estiver conectado, será solicitado que **faça login ou conclua o cadastro**.
  3. Após o login, o Espaço de Trabalho será aberto automaticamente.

  Como alternativa, você pode fazer login em [https://avatour.live/login](https://avatour.live/login) e acessar o Espaço de Trabalho a partir da sua **lista de Espaços de Trabalho**.

#### 3.1.2 Óculos de RV {#vr-headset}
Você pode participar de uma reunião e visitar um Espaço de Trabalho usando uma variedade de óculos compatíveis da Meta e da Pico. Para fazer isso: 

1. Instale nosso aplicativo Avatour a partir da loja de aplicativos de RV de sua preferência: [Como instalar o aplicativo Avatour VR](https://avatour.com/support/which-vr-headsets-can-i-use-with-avatour)
2. Abra nosso aplicativo e insira o código da reunião ou selecione um Espaço de Trabalho para participar de uma reunião. Para obter mais informações sobre como usar nosso aplicativo de RV, consulte nosso artigo da Base de Conhecimento [aqui](https://avatour.com/support/what-features-are-available-to-vr-guests).

### 3.2 Ferramentas de colaboração para reuniões e espaços de trabalho {#meeting-tools}

O Avatour permite a colaboração em dois contextos principais:

1. **Reuniões (sincrônicas):** Colabore em tempo real com outros participantes, incluindo visitas ao local ao vivo ou revisão conjunta de recursos gravados.  
2. **Espaços de Trabalho (assincrônicos):** Revise e interaja com recursos de acordo com sua própria programação, 24 horas por dia, 7 dias por semana.

As **ferramentas de colaboração são em grande parte semelhantes** entre reuniões e espaços de trabalho, com algumas diferenças devido ao contexto síncrono versus assíncrono.

#### 3.2.1 Layout da interface

A interface do Avatour está organizada em torno de três áreas principais:

- **Painel esquerdo** – Recursos do espaço de trabalho e ferramentas de apoio  
- **Área central** – Área principal de visualização para vídeo ao vivo ou recursos  
- **Painel direito** – Informações contextuais, como participantes, reuniões ou chat  

A maioria das interações é iniciada a partir do **menu inferior**.  
Clicar em uma opção do menu abre um **painel lateral** no lado esquerdo ou direito da tela, enquanto a **área central** permanece como a área de visualização principal.

---
#### 3.2.2 Exemplo de visualização de reunião

Aqui está um exemplo de visualização em uma reunião do Avatour:

![Interface do usuário da Reunião Avatour com Painel de Recursos, tela em branco e Painel de Participantes](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-assets-blank-participants_pugprq.png)  
*Reunião Avatour com Painel de Recursos (esquerda), tela (centro) e Painel de Participantes (direita)*

---

#### 3.2.3 Exemplo de visualização da área de trabalho

Aqui está um exemplo de visualização da área de trabalho:

![Área de trabalho do Avatour com painel de recursos, tela em branco e painel de reuniões](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png)  
*Área de Trabalho do Avatour com Painel de Recursos (à esquerda), Tela (ao centro) e Painel de Reuniões (à direita)*

---

#### 3.2.4 Visão geral do menu inferior

O menu inferior fornece acesso aos principais controles e painéis da interface:

**Menu inferior da reunião**  

![Menu inferior da reunião do Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-bottom-menu_bflaor.png)  
*Menu inferior da reunião do Avatour*

- **Recursos** – Visualize os arquivos da área de trabalho, incluindo vídeos gravados, imagens, capturas de tela e PDFs. 
- **Chat** – Envie mensagens a todos os participantes da reunião.  
- **Câmera** – Ligue ou desligue sua webcam.  
- **Microfone** – Silencie ou reative o seu microfone.  
- **Apresentar** – Apresente um recurso, a área de trabalho ou a imagem da webcam (consulte a seção Apresentar abaixo).  
- **Ferramentas do Anfitrião** (somente para anfitriões):  
  - **Bloquear Foco** – Bloqueia a visualização para todos os participantes.  
  - **Silenciar Todos** – Silencia todos os participantes.  
- **Ativar Tela Cheia** – Coloca a aba da reunião em tela cheia.  
- **Sair da Reunião** – Sai da reunião.  
- **Iniciar gravação** – Use este botão para iniciar e parar a gravação manualmente durante uma reunião. Alternativamente, as reuniões podem ser gravadas automaticamente se a opção **iniciar gravação automaticamente** estiver ativada nas configurações do espaço de trabalho. Em ambos os casos, as gravações são salvas nos recursos do espaço de trabalho.
- **Mapa** – Abra ou feche o painel do mapa para recursos com trilha de GPS. Clicar em um local leva ao ponto exato no vídeo. O mapa é atualizado em tempo real à medida que o vídeo é reproduzido.
- **Participantes** – Abra ou feche o painel de participantes.  
- **Informações da Reunião** – Visualize o código da reunião, o link de convite e acesse tutoriais relacionados.  

![Informações da Reunião do Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-meeting-info-side-pane_nx7dp4.png)  
*Painel lateral de informações da reunião do Avatour*

- **Configurações** – Ajuste as configurações de idioma, áudio e vídeo. Para reuniões com vídeo 360° ao vivo, use **Mostrar taxa de bits** para monitorar as estatísticas de conectividade.

> Dica: envie o link da reunião ou adicione-o a um item do calendário para convidar participantes.

---

##### Menu Apresentar

A opção **Apresentar** no menu inferior da reunião permite que você compartilhe conteúdo com todos os participantes.

- **Câmera** – Compartilhe a câmera do seu smartphone/tablet. Isso também pode ser usado durante uma reunião de vídeo ao vivo em 360° para sobrepor uma visualização secundária para close-ups ou detalhes específicos. 
- **Área de trabalho** – Compartilhe a tela da sua área de trabalho com todos os participantes.  
- **Recurso** – Apresente um recurso da área de trabalho. Ao selecionar um recurso, a **Barra de ferramentas de recursos** é aberta, oferecendo controles de reprodução e ferramentas de colaboração específicas para o recurso que está sendo apresentado.

##### Barra de ferramentas de recursos (Reunião)

Ao apresentar um recurso em uma reunião, a **Barra de ferramentas de recursos** aparece acima da tela. Aqui estão as ferramentas e os itens de menu disponíveis ao <u>apresentar um recurso em uma reunião</u> – explicados da esquerda para a direita.

![Menu do Avatour ao apresentar um recurso em uma reunião](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting_oflsr5.png) *Menu do Avatour ao apresentar um recurso em uma reunião*


- **Linha do tempo do vídeo / Barra de progresso** – Mostra o progresso do vídeo com notas e tópicos principais extraídos do áudio. Clique em uma nota ou tópico para pular para aquele momento e abrir a nota. Inclui controles de **Reproduzir / Pausar**.   
- **Instantâneo** – Capture uma imagem em 360° ou 2D do recurso.  
- **Destaque** – Destaque uma área específica para todos os participantes durante sessões ao vivo.  
- **Mostrar/ocultar ponto de vista (POV)** – Exibe para onde cada participante está olhando no vídeo em 360°.  
- **Notas** – Crie notas vinculadas a momentos específicos no recurso. As notas podem ser categorizadas (Observação, Problema, Ação, Recomendação), rastreadas por status (Aberto → Em andamento → Resolvido) e compartilhadas por meio de links diretos.  

  ![Nota do Avatour e Filtro de Notas](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-note-and-filters_g181oc.png) *Nota do Avatour e Filtros de Notas*

  - **Notas de comando de voz** – São marcadores de posição gerados automaticamente quando a gravação detecta menções como “inserir nota”, “fazer uma nota” ou “anotar”. Essas notas aparecem na linha do tempo e precisam ser **posicionadas e finalizadas** pelo usuário. 

  ![Notas do Avatour - Geradas por comando de voz](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-notes-voice-command-generated_ic5cu4.png) *Notas do Avatour - Geradas por comando de voz*

- **Painel de Notas e Resumo** – Abre um painel lateral que exibe todas as notas, tópicos principais e um resumo executivo do ativo. Clicar em um item leva você para aquele momento no vídeo.  

  ![Resumo executivo do ativo no Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-exec-summary_cqpqbs.png) *Resumo executivo do Avatour durante a apresentação de um ativo em uma reunião*

  ![Tópicos do Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-meeting-showing-topics_duuq1a.png) *Tópicos do Avatour durante a apresentação de um recurso em uma reunião*

  No **Painel Lateral**, você pode **imprimir um relatório de ativos** ou **baixá-lo como TXT ou CSV**. Os relatórios podem incluir notas, tópicos gerados por IA e transcrições completas. Você também pode **escolher quais elementos incluir** antes de exportar.  

  ![Menus de impressão do relatório de ativos do Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-print-menus_kn0syn.png)  
  *Menus de impressão/download do relatório de ativos do Avatour*  

  ![Seleção de elementos do relatório de ativos do Avatour](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-report-element-selection_ud8c5k.png)  
  *Menu de seleção de elementos do relatório de ativos do Avatour*

- **Compartilhar link** – Compartilhe um link para uma nota ou cena específica no recurso.  
- **Legendas ocultas (CC)** – Exiba a transcrição do texto na tela durante a reprodução do vídeo.

##### Barra de ferramentas do recurso (Área de trabalho)

Ao revisar um recurso em uma área de trabalho, a barra de ferramentas é semelhante, mas otimizada para uso individual:

![Menu do Avatour ao apresentar um recurso fora de uma reunião, por exemplo, ao visitar uma área de trabalho](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-present-asset-menu-workspace_iri8gc.png) *Menu do Avatour ao apresentar um recurso em uma área de trabalho*

- **Linha do tempo do vídeo / Barra de progresso** – Mostra o progresso do vídeo com notas e tópicos principais extraídos da trilha de áudio. Clique em qualquer lugar da linha do tempo para avançar ou retroceder no vídeo. Clique em uma nota ou tópico para saltar para aquele momento e abrir a nota. Inclui controles de **Reproduzir / Pausar**.  
- **Instantâneo, Notas, Painel de Notas e Resumo, Compartilhar Link, Legendas**  
- Indisponível: **Spotlight, POV** (estes requerem participantes ao vivo)  
- Controles adicionais:
  - **Passos de 10 segundos** – Pular para frente/para trás  
  - **Velocidade de reprodução** – Ajustar velocidade (0,5×–2×)  
  - **Cortar vídeo** – Cortar o início ou o fim do recurso


## 4. Para usuários anfitriões e administradores - Console da Web do Avatour {#for-host-and-admin-users-avatour-web-console}

Ao fazer login na sua conta de usuário do Avatour, você acessará o **Console da Web**.  

### 4.1 Console da Web - Visão geral do menu principal {#web-console-overview-main-menu}

No lado esquerdo, você verá os seguintes itens de menu:

![Console Web do Avatour - Menu Principal](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu_qwpthq.png) *Console Web do Avatour - Menu Principal*

- **Espaços de trabalho** – Organize seu conteúdo com eficiência. Cada espaço de trabalho contém **Recursos**, **Colaboradores**, **Reuniões** e **Configurações**.  
- **Recursos** – Acesse e gerencie todos os seus recursos (vídeos, imagens, PDFs). Os administradores podem visualizar todos os recursos da conta, e os recursos compartilhados ficam visíveis para todos os usuários.  
- **Perfil** – Gerencie seu idioma e senha.  
- **Análises** – Acompanhe a atividade das sessões, o uso do espaço de trabalho e as métricas de ROI.  
- **Configurações** *(Somente para administradores)* – Configure os padrões do espaço de trabalho, das reuniões e dos ativos em toda a organização. Os administradores também podem personalizar a identidade visual (logotipo, cores, planos de fundo).  
- **Conta** *(Somente para administradores)* – Gerencie usuários registrados e câmeras 360°.  
- **Login do dispositivo** – Digite o código exibido na sua câmera 360° para emparelhá-la com sua conta.  
- **Tutoriais** – Acesse tutoriais guiados.  
- **Sair** – Saia do console.

> Seções como Perfil, Login do dispositivo, Tutoriais e Sair são autoexplicativas e não possuem subseções detalhadas.

---

### 4.2 Console da Web - Detalhes por item do menu (com imagens) {#web-console-details-by-menu-item}

#### 4.2.1 Espaços de trabalho

Os espaços de trabalho são unidades organizacionais flexíveis que permitem gerenciar ativos, colaboradores e reuniões em um único lugar. Você pode criar um novo espaço de trabalho com o botão **Novo espaço de trabalho** no canto superior direito.

![Console Web do Avatour - Item do menu principal Espaços de trabalho](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspaces_hnhkjj.png) *Console Web do Avatour - Item do menu principal Espaços de trabalho*

Clique no ícone de sino para ver um resumo das atividades do espaço de trabalho nos últimos 7 dias.

![Console Web do Avatour - Atividades recentes do espaço de trabalho](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-workspace-recent-activities_gby1ws.png) *Atividades recentes do espaço de trabalho*

Dentro de um espaço de trabalho:

![Espaço de trabalho do Avatour com painel de ativos, tela em branco e painel de reuniões](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-assets-blank-meetings_qeumpl.png) *Espaço de trabalho com ativos (esquerda), tela (centro), reuniões (direita)*

- **Recursos** – Gerencie os arquivos alocados a este espaço de trabalho.  
- **Colaboradores** – 
  Controle o acesso aos espaços de trabalho por meio de 
  - **Visualizador** – Pode visualizar recursos. O convite cria um usuário Convidado, se necessário.  
  - **Editor** – Controle total do espaço de trabalho, com os mesmos direitos que o Anfitrião. O convite eleva o usuário à função de Anfitrião, se necessário.  
> Vários usuários podem acessar um espaço de trabalho simultaneamente sem uma reunião. Os espaços de trabalho públicos e as configurações de acesso às reuniões oferecem alternativas de acesso.  
- **Relatório** – Gere um relatório usando um modelo de lista de verificação nos ativos selecionados do espaço de trabalho.  

![Relatório do Espaço de Trabalho Avatour e Seleção de Ativos](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-asset-selection-and-workspace-report_itjt8f.png) *Relatório do Espaço de Trabalho e Seleção de Ativos*

- **Mapa** – Exibe localizações de ativos com GPS em um mapa.  
- **Reuniões** – Organize reuniões no espaço de trabalho.  
- **Configurações** – Configure as predefinições do espaço de trabalho e das reuniões:

![Configurações do Avatour - Visualização do Espaço de Trabalho](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-workspace-settings_llcei3.png) *Configurações do Espaço de Trabalho*

**Configurações do Espaço de Trabalho**

- **Modelo de Relatório** – Selecione o modelo de lista de verificação para relatórios de IA.  
- **Ativar Notificações** – E-mails diários com resumo das alterações no status das notas.  

![Notificações por e-mail - Exemplo](https://res.cloudinary.com/avatour/image/upload/c_crop,h_600,w_600,x_170,y_60/Screenshot_2026-03-05_140654_bjk0xk.png) *Exemplo de notificações por e-mail*

- **Espaço de trabalho público** – Qualquer pessoa com o link pode visualizar os recursos diretamente.

**Configurações da reunião**
  
* **Autenticação necessária** – Os participantes devem fazer login.  
* **Permitir acesso de convidados** – Permite que usuários não registrados visualizem os recursos.  
* **Gravação automática / Início manual** – Escolha se as reuniões serão gravadas automaticamente ou iniciadas manualmente.  
* **Exigir anfitrião** – O anfitrião deve admitir os participantes; a reunião termina quando o anfitrião sai.  
* **Permitir acesso de espectadores** – Participar sem microfone ou câmera; comunicar-se via chat.  
* **Reuniões protegidas por senha** – Exigir uma senha para participar.  
* **Mostrar pergunta sobre economia de deslocamento** – Perguntar aos participantes se a reunião reduziu o deslocamento.  

> As configurações podem ser combinadas (por exemplo, sem necessidade de anfitrião, mas protegidas por senha).

---

#### 4.2.2 Recursos

Gerencie todos os vídeos em 360°/2D, imagens e PDFs. Carregue/baixe recursos, aloque-os a espaços de trabalho, compartilhe com outros usuários, renomeie, imprima/baixe relatórios, ative o desfoque de rosto e a síntese por IA.

![Avatour Web Console - Item do menu principal Recursos](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-assets_ky5emz.png) *Item do menu principal Recursos*

---

#### 4.2.3 Análises

Fornece insights sobre reuniões, uso do espaço de trabalho e métricas de ROI.

![Avatour Web Console - Item do Menu Principal: Análises (1 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-1-of-3_ds3epe.png) *Visão geral das análises*

![Console Web do Avatour - Item do menu principal: Análises (2 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-2-of-3_vpcsme.png) *Atividade de reuniões e uso do espaço de trabalho*

![Avatour Web Console - Item do menu principal: Análises (3 de 3)](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-main-menu-analytics-3-of-3_hn2pmr.png) *Uso de licenças de dispositivos e ROI* 

## 5. No local - Como usar o kit pronto para uso da Avatour {#onsite-how-to-use-the-avatour-turnkey-kit}

### 5.1 Introdução
Aqui você encontrará um guia online muito completo para dar os primeiros passos com o Kit Avatour Turnkey: [Guia de Início Rápido – Kit Avatour Turnkey 3.1 (Configuração do Pilot PanoX V2)](https://avatour.com/quickstart-panox-v2)

E aqui está também a imagem com instruções que você encontrará dentro da tampa da maleta do kit 3.1.
![Imagem dentro da tampa da maleta do Kit Avatour](https://res.cloudinary.com/avatour/image/upload/v1775994773/avatour-turnkey-kit-3.1-inside-lid-picture_dq4ipl.png) *Imagem dentro da tampa da caixa do kit Avatour* 

Siga o guia e as instruções para desembalar, montar e ligar sua câmera.

---

### 5.2 Dicas úteis

#### Bateria externa – Reuniões mais longas e melhor desempenho térmico 

- **Se o seu kit incluir uma bateria Ulanzi:** Fixe-a entre a base do tripé e a haste extensível e, em seguida, conecte a bateria à câmera via USB-C.  

- **Se o seu kit incluir uma haste de bateria Telesin:** Monte a câmera diretamente na haste de bateria extensível Telesin e conecte-a via USB-C.  

Usando a bateria externa:

1. Aumenta a duração total da bateria de ~40 minutos (apenas com a bateria da câmera) para ~3 horas.  
2. Adiciona estabilidade à configuração da câmera.  
3. Ajuda a evitar um possível superaquecimento.  

> Recomendamos usar sempre a bateria externa desde o início, especialmente para reuniões ao vivo.

#### Considerações sobre áudio para reuniões ao vivo e gravações

- **Ambientes ruidosos:** 
  Use os fones de ouvido Shokz incluídos no seu kit para uma captura de áudio nítida.  
  - **Ligar/Desligar:** Mantenha pressionado o botão “+” por 3 segundos (LED azul = ligado, LED vermelho = desligado).  
  - **Modo de emparelhamento Bluetooth:** Com o fone de ouvido desligado, mantenha pressionado o botão “+” por 5 segundos (o LED pisca em azul/vermelho).  
  - **Volume:** Use os botões “+” e “-”.  

- **Ambientes mais silenciosos / vários participantes próximos à câmera:** 
  Use o alto-falante clipável NoxGear. Ele não tem a mesma alta fidelidade dos alto-falantes de conferência (por exemplo, Jabra Speak), mas é fácil de prender na camisa e capta vozes próximas com eficácia.  
  - **Ligar/Desligar:** Mantenha pressionado o botão Reproduzir/Pausar por 2 segundos.  
  - **Modo de emparelhamento Bluetooth:** Entra automaticamente no modo de emparelhamento ao ser ligado (o LED pisca em azul/vermelho; fica azul fixo quando emparelhado).  
  - **Volume:** Use os botões “+” e “-”.  

- **Usando seu próprio dispositivo:** Se preferir uma alternativa (por exemplo, um alto-falante de conferência ou fone de ouvido pessoal), você pode emparelhá-lo pela câmera: Configurações → Bluetooth.  

#### Conectividade, conectividade, conectividade
**Antes de começar:** Verifique a conexão com a internet via:

- **Wi-Fi local** (preferencial)
- **Rede móvel** (se estiver fora do alcance do Wi-Fi)

**Largura de banda recomendada:** 10 Mbps de upload/download para streaming completo em 360° (~5 Mbps). Largura de banda menor (1–2 Mbps) só funciona quando você estiver parado.

##### Teste de velocidade da rede
- **Teste em um único local:** Qualquer verificador de velocidade que você use normalmente (por exemplo, [Speedtest](https://www.speedtest.net)) para verificar a largura de banda de upload e download.   
- **Teste de caminhada pelo local:** Na câmera: Configurações → Rede → Teste de conexão. Caminhe por todo o espaço para confirmar a cobertura e a largura de banda.

##### Wi-Fi local
- Altamente recomendado para conexões estáveis.  
- Se o departamento de TI exigir uma lista de permissões, encontre o endereço MAC: Configurações → Sobre → Endereço Wi-Fi.

##### Rede móvel
**Opção A: Hotspot e SIM fornecidos no kit**  

- Conecte o hotspot GlocalMe ao stick de bateria Telesin (ímã).  
- Garante que não haja interferência e mantém a conexão se você se afastar da câmera.  
- Solução de problemas:
  - Confirme o SIM pré-instalado (não o Cloud SIM).  
  - Ative o 5G no Gerenciador de Cartão SIM.  
  - Verifique o APN correto para sua região ([Guia de configuração de APN](https://avatour.com/support/how-do-i-change-the-apn-on-my-glocalme-hotspot)).

**Opção B: Hotspot pessoal / SIM**
- Use seu próprio smartphone ou um hotspot dedicado.  

**Observação importante:**  
> Mantenha o hotspot desligado enquanto estiver conectado ao Wi-Fi; ative-o apenas quando estiver fora de alcance. O sistema operacional da câmera alterna dinamicamente entre redes Wi-Fi com base na intensidade do sinal e pode, inadvertidamente, mudar para o hotspot mesmo quando o Wi-Fi estiver disponível.

> As redes móveis podem limitar a largura de banda inesperadamente. Verifique com sua operadora os limites do plano de dados ou entre em contato com o suporte da Avatour se estiver usando nosso hotspot e SIM.

##### Situações de baixa largura de banda
- Grave vídeos do local com antecedência para reprodução posterior ([guia de gravação](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).  
- Compartilhe a transmissão da câmera de um smartphone para complementar áreas de baixa largura de banda (0,1–0,3 Mbps de upload).

##### Sem conectividade
- Apenas vídeos pré-gravados podem ser usados ([guia de gravação](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)).

#### Outros participantes no local – Práticas recomendadas

Quando vários participantes entram em uma reunião ao vivo do Avatour a partir do mesmo local da câmera 360°, o gerenciamento cuidadoso do **áudio e da largura de banda** é crucial:  

- Cada smartphone, tablet ou laptop conectado no local consome largura de banda da rede e pode afetar negativamente a transmissão da câmera 360°.  
- Vários microfones e alto-falantes no mesmo espaço podem causar **feedback de áudio**, tornando a experiência da reunião desagradável para todos os participantes.

#### Outros participantes no local – Melhores práticas

Quando vários participantes entram em uma reunião ao vivo do Avatour a partir do mesmo local da câmera 360°, o gerenciamento cuidadoso do **áudio e da largura de banda** é crucial:  

- Cada smartphone, tablet ou laptop conectado no local consome largura de banda da rede e pode afetar negativamente a transmissão da câmera 360°.  
- Vários microfones e alto-falantes no mesmo espaço podem causar **feedback de áudio**, tornando a experiência da reunião desagradável para todos os participantes.

Para lidar com esses desafios, siga estas **práticas recomendadas**:

- **Use fones de ouvido com ou sem fio:** de preferência com cancelamento de ruído para evitar eco e feedback.  
- **Modo no Local:** participe da reunião no modo no local quando estiver fisicamente presente perto da câmera 360°.  
  - Este modo é otimizado para uso no local: 
 - Silencia o microfone e o alto-falante do participante por padrão.  
    - **Não** transmite a imagem da câmera do participante. 
 - **Não** exibe a imagem da câmera 360° no navegador do participante. 
 - Economiza largura de banda da rede, garantindo que a câmera 360° tenha o máximo de upload disponível para a transmissão ao vivo.  
    - Útil quando um usuário deseja compartilhar detalhes específicos; você **pode compartilhar sua câmera** para visualizações direcionadas.  
- **Silenciar quando não estiver falando ativamente:** Evita feedback de áudio indesejado e distrações.  
- **Use uma rede separada, se possível:** Mantenha seu smartphone conectado a uma rede diferente da rede da câmera para reduzir interferências.  

Seguir essas diretrizes garante um tour ao vivo tranquilo e de alta qualidade tanto para participantes no local quanto para os remotos.

### 5.3 Aplicativo da Câmera Avatour

Aqui estão os menus (1) Nível Superior, (2) Configurações e (3) Configurações de Rede.

![Aplicativo Avatour 360° Camera - Três Menus](https://res.cloudinary.com/avatour/image/upload/avatour-screenshot-cam-app-3-menu-screens_nju8bt.png) *Aplicativo Avatour 360° Camera - 3 Menus*

**Captura Rápida** - Para gravação de vídeo 360° offline. - Para uma descrição detalhada, consulte [Como gravar e enviar vídeos 360° com o aplicativo Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app). Recomendamos usar um dispositivo de áudio externo (conectado via Bluetooth). Observação: você também pode gravar vídeos e tirar fotos 2D padrão — basta alternar entre os modos 360° e 2D no canto inferior direito da tela de captura rápida.

**Reunião ao Vivo** — Para videoconferências 360° ao vivo. Você verá seus espaços de trabalho e, ao clicar em um deles, iniciará a transmissão de vídeo ao vivo da câmera 360°. Antes de participar da reunião com sua câmera 360°, você precisa conectar um dispositivo de áudio via Bluetooth. Para uma descrição detalhada, consulte [Como iniciar uma reunião Live Capture com sua câmera Pilot?](https://avatour.com/support/how-to-start-a-live-capture-meeting-with-your-pilot-camera)

> Ao hospedar uma reunião Live Capture com sua câmera 360°, você terá à disposição ferramentas de reunião semelhantes às da experiência na web. Aqui está um link para o artigo da nossa Base de Conhecimento que explica essas ferramentas com mais detalhes: [Ferramentas do aplicativo do operador](https://avatour.com/support/what-avatour-app-tools-are-available-to-labpano-pilot-camera-operators)

**Galeria** - Encontre aqui todos os seus vídeos e fotos em 360° para enviar para o Avatour Web Console.

**Configurações** - Em Configurações, você tem as seguintes opções:

- **Rede**: Esta opção permite que você altere a rede Wi-Fi à qual a câmera está conectada ou execute um teste de conexão de rede para verificar a taxa de transferência de streaming
- **Captura ao Vivo**: Ajuste suas configurações de Captura ao Vivo de acordo com a largura de banda disponível, a sensibilidade de RV do convidado ou se as lentes de proteção da sua câmera estiverem instaladas:
  - **Taxa de Quadros** **Alvo**: Ajuste a taxa de quadros do seu vídeo de Captura ao Vivo entre 15 fps, 24 fps e 30 fps. Taxas de quadros mais altas produzem um vídeo mais suave, mas exigirão mais largura de banda de upload. Padrão: 15 fps
  - **Taxa de bits alvo**: Permite aumentar ou diminuir a taxa de bits máxima de streaming para sua Captura ao vivo. Você pode definir sua taxa de bits alvo entre 1 Mbps e 10 Mbps. Taxas de bits mais altas resultarão em maior resolução de vídeo, mas exigirão mais largura de banda de upload. Padrão: 5 Mbps
  - **Otimizar movimento**: Isso diminuirá a taxa de quadros do vídeo, gerando menos carga na largura de banda de upload da sua rede e aumentando sua taxa de bits de streaming. Além disso, essa opção ajuda a reduzir a sensação de enjoo para participantes de RV. Padrão: Desativado
  - **Lentes de proteção**: Isso afetará a forma como o vídeo em 360° é costurado, dependendo se lentes de proteção foram instaladas na sua câmera. Se você não tiver lentes de proteção, defina isso como “Não”. Se você recebeu um Kit 3.0, ele já vem com lentes de proteção pré-instaladas e você deve definir esta opção como “Sim”. Padrão: Sim

- **Captura Rápida**: Ajuste suas configurações de Captura Rápida de acordo com a taxa de quadros de vídeo de sua preferência, a largura de banda disponível para uploads de vídeos gravados ou se as lentes de proteção da sua câmera estiverem instaladas. A Captura Rápida tem uma resolução definida de 4K, o que geralmente oferece um bom equilíbrio entre qualidade de vídeo e tamanho do arquivo. (Para resoluções mais altas, você pode usar os aplicativos nativos da câmera, também no PanoX V2; para mais detalhes, consulte [Como gravar e enviar vídeos em 360° com o aplicativo Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)):
  - **Taxa de quadros alvo**: Ajuste a taxa de quadros para suas gravações de vídeo com Captura Rápida entre 15 fps, 24 fps e 30 fps. Taxas de quadros mais altas produzem um vídeo mais suave, mas aumentam o tamanho do arquivo de vídeo e o tempo de envio. Recomendado: 30 fps
  - **Taxa de bits alvo**: Defina a taxa de bits alvo para envios com Captura Rápida entre 5 Mbps e 20 Mbps. Taxas de bits mais baixas aumentam a velocidade de upload, mas diminuem a qualidade do vídeo. Recomendado: 20 Mbps
  - **Lentes de proteção**: *Consulte a seção Lentes de proteção para Captura ao vivo acima*

  > Consulte também nossa [Calculadora de tamanho de arquivo de vídeo Avatour 360°](https://avatour.com/file-size-calculator) para obter mais orientações sobre as configurações acima e os tamanhos dos arquivos de vídeo.

- **Sobre**: Visualize o número de série do dispositivo e a versão do software


**Conta** - Para fazer login com sua conta de host ou administrador do Avatour.

## 6. Recomendações sobre melhores práticas {#best-practice-advice}

### 6.1 Primeiras utilizações (informais) e familiarização

Para suas primeiras utilizações e para se familiarizar com o Avatour Web Console e o Avatour Turnkey Kit, recomendamos os seguintes passos:

1. Leve o kit para casa e experimente-o com a família e os amigos usando sua conexão de internet doméstica.
2. Leve o kit para o escritório e conecte-se à rede corporativa (podem surgir questões corporativas, como firewalls corporativos — mas você já sabe, desde a primeira etapa, que o Avatour está funcionando e que esse é um assunto a ser resolvido pela sua equipe de TI com a ajuda do Avatour).
3. Comece a usar o Avatour no local (fora do escritório) no local da reunião para o qual os participantes remotos normalmente precisariam se deslocar. Outras questões de conectividade podem surgir. O Avatour ajudará em cooperação com sua equipe de TI.
4. Comece a usar com participantes remotos internos e externos.

### 6.2 Antes de uma reunião ao vivo com vídeo em 360°

- Recomendamos fazer um tour em vídeo 360° gravado antes de qualquer tour ao vivo, se o tempo permitir, por três motivos: (1) Ter uma solução alternativa para o tour ao vivo, (2) ter algo para documentação e revisão posterior (além do tour ao vivo gravado) e (3) começar a criar uma biblioteca de vídeos 360° de todos os seus locais, o que pode ser útil para muitos casos de uso. 
- Todos os componentes do kit devem ser carregados por pelo menos 90 minutos antes da reunião ao vivo. De qualquer forma, recomendamos manter todos os dispositivos em carregamento contínuo quando não estiverem em uso. Assim, todos os dispositivos estarão sempre prontos, inclusive para reuniões ad hoc não planejadas.
- Tenha o kit totalmente montado (1. base do tripé + 2. bateria Ulanzi + 3. bastão extensível + 4. câmera 360°).

- Confirme se um Espaço de Trabalho foi criado para hospedar uma reunião ao vivo e inclua todos os recursos relevantes.

- Convide todos os participantes para a reunião através do seu Espaço de Trabalho. Isso cria um convite nos calendários de todos os participantes e inclui o link de convite para a reunião.

- Emparelhe e conecte à câmera os fones de ouvido ou alto-falantes Bluetooth que você planeja usar durante o tour.

- Todos os usuários de smartphones no local devem se conectar a uma rede diferente da rede da câmera. Isso reduzirá a carga na largura de banda da rede da câmera.

- Se você estiver sozinho como operador de câmera, leve um smartphone com você caso queira compartilhar a câmera do smartphone e mostrar detalhes finos.

- Confirme se a câmera 360 pode se conectar ao seu Wi-Fi local.

- Antes de uma reunião Avatour, planeje o trajeto que você seguirá pelas instalações. Faça uma reunião Avatour de teste com a câmera e verifique se todas as áreas têm taxas de bits acima de 1 Mbps de largura de banda. Isso pode ser visto na própria tela da câmera ou, como participante remoto, acessando Configurações e ativando Mostrar Taxa de Bits.

- Se você perceber que algumas áreas têm pouca ou nenhuma largura de banda, é melhor tirar fotos ou fazer uma gravação. Esses materiais podem então ser apresentados durante a reunião para que os participantes remotos possam analisá-los. Você pode seguir o guia aqui que explica nosso Quick Capture para gravar e enviar vídeos/imagens: [Como gravar e enviar vídeos 360 com o aplicativo Avatour?](https://avatour.com/support/how-do-you-record-and-upload-360-videos-with-the-avatour-app)

- Se houver participantes remotos na reunião que nunca tenham usado o Avatour antes, forneça a eles um breve resumo da plataforma, suas funcionalidades (vídeo 360 ao vivo, recursos, instantâneos, anotações, destaque) e as ferramentas da reunião.

- Você pode iniciar em outra solução de videoconferência (por exemplo, Teams, Zoom, Google Meet), mas antes de mudar para o Avatour, feche completamente o outro aplicativo de videoconferência. Em alguns casos, esses outros aplicativos priorizam o microfone/alto-falantes/webcam do seu dispositivo, fazendo com que eles sejam desativados para o Avatour. Além disso, NÃO execute o Avatour E outra videoconferência ao mesmo tempo, pois isso reduzirá a largura de banda disponível.

- Se você planeja usar a câmera 360° em um ambiente com temperatura elevada, é recomendável usar o módulo de resfriamento (somente Pilot Pano). Isso ajudará a reduzir as chances de a câmera superaquecer e desligar automaticamente.

### 6.3 Ao operar a câmera no local para uma reunião ao vivo com vídeo 360°

- Ao operar a câmera, certifique-se de **andar devagar** e **parar com frequência para apoiar a câmera no tripé**. Isso ajuda (1) na qualidade do vídeo, pois você produz menos dados de vídeo ao não mover a câmera desnecessariamente, e (2) reduz qualquer possível interrupção do vídeo quando a conexão de rede da câmera alterna entre pontos de acesso Wi-Fi.

- Segure a câmera à sua frente e acima do nível dos olhos. Isso permite que todos os participantes remotos vejam a maior parte da área ao seu redor.

- Nos casos em que a câmera precise permanecer estável, use o tripé e ajuste a câmera à altura correta, de preferência ao nível dos olhos.

- Sempre que possível, conecte a câmera à sua rede Wi-Fi local. Em áreas sem acesso Wi-Fi, use o hotspot fornecido. O hotspot possui um cartão SIM que se conectará a uma rede de celular confiável próxima a você. Mantenha o hotspot sempre desligado quando não estiver em uso em ambientes internos, pois, caso contrário, a câmera 360° poderá se conectar ao hotspot, o que não é desejável em ambientes internos. Quando estiver ao ar livre, mantenha o hotspot próximo à câmera 360°.

- Quando a taxa de bits da câmera começar a cair abaixo de 2 Mbps, ande mais devagar ou pare completamente até que o sinal se estabilize novamente. Isso geralmente acontece quando você muda de um ponto de acesso Wi-Fi para outro. 

- Se você souber que a conectividade e o vídeo vão cair ao se deslocar para um local específico (Exemplo: ao sair de uma área de produção interna para uma área externa), avise os participantes remotos com antecedência.

- Se precisar mostrar algo com alto nível de detalhes ou letras pequenas, use seu próprio smartphone ou o de um participante no local para participar da reunião e apresentar a câmera (traseira) do seu/dele.

- Se possível, recomendamos que haja uma pessoa adicional no local para ajudar com o compartilhamento da câmera do smartphone descrito acima, pois isso costuma ser útil/necessário.

- O ideal é que os usuários de smartphones no local participem da reunião (1) no modo local e (2) em uma rede diferente daquela que a câmera está usando, para não ocupar largura de banda de upload crucial da câmera 360°.

- Todos os participantes no local que estiverem participando por meio de seus smartphones devem ter o áudio silenciado, a menos que estejam falando ativamente.
