async function getStreamResponse() {
    const question = document.getElementById('question');
    let responseField = document.getElementById('question-response');
    responseField.innerHTML = 'Pensando...';
    const url = "/chat/";
    let data = new FormData();
    data.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);
    data.append('question', question.value);

    question.value = '';
    const response = await fetch(url, {
        method: 'POST',
        body: data,
        credentials: 'same-origin'
    });
    responseField.innerHTML = '';

    const reader = response.body.getReader();
    while (true) {
        const { done, value } = await reader.read();

        if (done) {
            break;
        }

        const decodedValue = new TextDecoder("utf-8").decode(value);
        responseField.innerHTML += decodedValue;
    }
}
