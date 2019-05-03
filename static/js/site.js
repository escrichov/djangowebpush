const pushForm = document.getElementById('send-push_form');
const errorMsg = document.querySelector('.error');

pushForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    const input = this[0];
    const textarea = this[1];
    const button = this[2];
    errorMsg.innerText = '';

    const head = input.value;
    const body = textarea.value;

    if (head && body) {
        button.innerText = 'Sending...';
        button.disabled = true;

        const res = await fetch('/send_push_form', {
            method: 'POST',
            body: JSON.stringify({head, body}),
            headers: {
                'content-type': 'application/json'
            }
        });
        if (res.status === 200) {
            console.log("Notification sended correctly!");
            button.innerText = 'Send another 😃!';
            button.disabled = false;
            input.value = '';
            textarea.value = '';
        } else {
            var error_message = "Unknown Error";
            try {
                const message = await res.json();
                error_message = message['message'];
            } catch (error) {
                console.log(error);
            }
            errorMsg.innerText = error_message;
            button.innerText = 'Something broke 😢..  Try again?';
            button.disabled = false;
        }
    }
    else {
        let error;
        if (!head || !body){
            error = 'Please ensure you complete the form🙏🏾'
        }
        errorMsg.innerText = error;
    }
});