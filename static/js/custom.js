async function getStreamResponse(url, saveUrl) {
    const question = document.getElementById('question');
    let responseField = document.getElementById('question-response');
    responseField.innerHTML = 'Pensando...';
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
            data.append('response', responseField.innerHTML);
            await fetch(saveUrl, {
                method: 'POST',
                body: data,
                credentials: 'same-origin'
            })
            break;
        }
        const decodedValue = new TextDecoder("utf-8").decode(value);
        responseField.innerHTML += decodedValue;
    }
}