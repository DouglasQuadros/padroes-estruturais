O padrão Facade foi utilizado para simplificar a interação do cliente com um sistema complexo de gerenciamento de tarefas.
Em vez de interagir diretamente com múltiplos subsistemas (como Tarefa, ArmazenamentoTarefas e SistemaNotificacao), o usuário interage com uma única interface: a classe SistemaGerenciamentoTarefas.

 - Funcionalidades
Adicionar Tarefa: Permite adicionar uma nova tarefa ao sistema.
Concluir Tarefa: Permite marcar uma tarefa como concluída.
Listar Tarefas: Exibe todas as tarefas, mostrando se estão pendentes ou concluídas.
Notificações: O sistema envia uma notificação sempre que uma tarefa é concluída.

 - Estrutura do Código
Tarefa: Representa uma tarefa e inclui métodos para marcar como concluída.
ArmazenamentoTarefas: Gerencia o armazenamento e a listagem de tarefas.
SistemaNotificacao: Envia notificações quando uma tarefa é concluída.
SistemaGerenciamentoTarefas (Facade): Fornece uma interface simplificada para o cliente interagir com o sistema de gerenciamento de tarefas.
