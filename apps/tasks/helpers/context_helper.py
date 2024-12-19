def get_task_filter_context() -> dict:
    """
    Retorna um dicionário com as chaves e valores dos status de tarefas.
    """
    return {
        '': 'Todos',
        'backlog': 'Backlog',
        'todo': 'À fazer',
        'development': 'Em desenvolvimento',
        'done': 'Finalizado',
    }
