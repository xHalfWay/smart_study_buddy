// document.addEventListener('DOMContentLoaded', function() {
//     const chatForm = document.getElementById('chat-form');
//     const chatInput = document.getElementById('chat-input');
//     const chatBox = document.getElementById('chat-box');

//     chatForm.addEventListener('submit', function(event) {
//         event.preventDefault();
//         const userMessage = chatInput.value;

//         if (userMessage.trim() === '') {
//             return;
//         }

//         addMessage('user', userMessage);
//         chatInput.value = '';

//         fetch('/gigachat_interaction/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/x-www-form-urlencoded',
//                 'X-CSRFToken': getCookie('csrftoken') 
//             },
//             body: new URLSearchParams({
//                 'csrfmiddlewaretoken': getCookie('csrftoken'), 
//                 'message': userMessage
//             })
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.response) {
//                 addMessage('bot', data.response);
//             } else {
//                 addMessage('bot', 'Ошибка при получении ответа от сервера.');
//             }
//         })
//         .catch(error => {
//             console.error('Ошибка:', error);
//             addMessage('bot', 'Ошибка при получении ответа от сервера.');
//         });
//     });

//     function addMessage(sender, message) {
//         const messageElement = document.createElement('div');
//         messageElement.classList.add('message', sender);
//         messageElement.textContent = message;
//         chatBox.appendChild(messageElement);
//         chatBox.scrollTop = chatBox.scrollHeight;
//     }

//     function getCookie(name) {
//         let cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             const cookies = document.cookie.split(';');
//             for (let i = 0; i < cookies.length; i++) {
//                 const cookie = cookies[i].trim();
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
// });
