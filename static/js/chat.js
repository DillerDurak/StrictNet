let code = document.querySelector('#chat_code').textContent
let chat = document.querySelector('.chat')
let chatForm = document.querySelector('.chat_form')
let userImg = document.querySelector('#user_img').src
let userSource = document.querySelector('.profile_username').textContent
let userTarget = document.querySelector('#target_name').textContent

var connectionString = 'ws://' + window.location.host + '/ws/messages/' + code + '/';
const gameSocket = new WebSocket(connectionString);


window.addEventListener('load', ()=>{
    window.location.href = '#form'
})


gameSocket.onopen = function open(){
    console.log('WebSockets connection created.');
}

chatForm.addEventListener('submit', ()=>{
    let message = document.querySelector('#form').value
    console.log(message)
    let data = {
        'message': message,
        'source': userSource,
        'target': userTarget,
    }

    document.querySelector('#form').value = ''
    gameSocket.send(JSON.stringify(data))
    fetch('http://' + window.location.host + '/api/add_message/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
    }})
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => console.log('error: ', error))

})
    


gameSocket.onclose = function (e) {
    console.log('Socket is closed. Reconnect will be attempted in 1 second.', e.reason);
    setTimeout(function () {
        connect();
    }, 1000);
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');


gameSocket.onmessage = function (e){
    let data = JSON.parse(e.data);
    data = data["payload"];
    let message = data['message']
    let username = data['username']
    let target



    // chat.innerHTML += `
    // <div class="message_container">
    //     <img src="${img}" class="message_img" alt="">

    //     <div class="message_content">
    //         <p class="sourceId">${username} <span>{{m.createdAt|date:"j N G:i:s"}}
    //             <!-- {%ifchanged%}
    //                 {{m.updatedAt|date:"N j G i s"}} (updated)
    //             {%endifchanged%} -->
    //         </span></p>
    //         <div class="message">{{m.message}}</div>
    //     </div>
    
    // </div>
    // `
}
