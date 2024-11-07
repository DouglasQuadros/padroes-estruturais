Este projeto implementa um sistema de gerenciamento de tarefas usando o padrão de projeto Facade. O sistema permite adicionar tarefas, concluir tarefas e visualizar o status das tarefas de forma simples, com uma interface única fornecida pela classe SistemaGerenciamentoTarefas.
- Funcionalidades
Adicionar Tarefa: Permite adicionar uma nova tarefa ao sistema.
Concluir Tarefa: Permite marcar uma tarefa como concluída.
Listar Tarefas: Exibe todas as tarefas, mostrando se estão pendentes ou concluídas.
Notificações: O sistema envia uma notificação sempre que uma tarefa é concluída.

Estrutura do Código
Tarefa: Representa uma tarefa e inclui métodos para marcar como concluída.
ArmazenamentoTarefas: Gerencia o armazenamento e a listagem de tarefas.
SistemaNotificacao: Envia notificações quando uma tarefa é concluída.
SistemaGerenciamentoTarefas (Facade): Fornece uma interface simplificada para o cliente interagir com o sistema de gerenciamento de tarefas.
