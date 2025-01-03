async function getStreamResponse(url, saveUrl) {
    const question = document.getElementById('question');
    const messageLogs = document.getElementById('message-logs');

    // Adiciona a pergunta ao histórico de mensagens
    const userMessage = document.createElement('div');
    userMessage.className = 'message message-user my-2 py-2';
    userMessage.textContent = question.value;
    messageLogs.appendChild(userMessage);

    // Cria um placeholder para a resposta do assistente
    const assistantMessage = document.createElement('div');
    assistantMessage.className = 'message message-assistant my-2 py-2';
    assistantMessage.textContent = 'Pensando...';
    messageLogs.appendChild(assistantMessage);

    // Scrolla para o final das mensagens
    messageLogs.scrollTop = messageLogs.scrollHeight;

    let data = new FormData();
    data.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);
    data.append('question', question.value);

    question.value = ''; // Limpa o campo de entrada

    const response = await fetch(url, {
        method: 'POST',
        body: data,
        credentials: 'same-origin'
    });

    const reader = response.body.getReader();
    assistantMessage.textContent = ''; // Limpa o placeholder antes de começar o streaming

    while (true) {
        const { done, value } = await reader.read();
        if (done) {
            data.append('response', assistantMessage.textContent);
            await fetch(saveUrl, {
                method: 'POST',
                body: data,
                credentials: 'same-origin'
            });
            break;
        }
        const decodedValue = new TextDecoder("utf-8").decode(value);
        assistantMessage.textContent += decodedValue;

        // Scrolla para o final enquanto o conteúdo é atualizado
        messageLogs.scrollTop = messageLogs.scrollHeight;
    }
}

document.getElementById('question').addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) { // Verifica se Enter foi pressionado sem Shift
        event.preventDefault(); // Impede a quebra de linha padrão
        const sendButton = document.querySelector('.btn-primary');
        sendButton.click(); // Simula o clique no botão Enviar
    }
});

function scrollToBottom() {
    const messageLogs = document.getElementById('message-logs');
    messageLogs.scrollTop = messageLogs.scrollHeight;
}

window.onload = scrollToBottom;
