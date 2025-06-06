<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Dreier KI-Assistent</title>
    <style>
        body {
            background-color: #009A92;
            font-family: Arial, sans-serif;
            color: white;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: white;
            padding: 10px;
            text-align: center;
        }

        header img {
            height: 60px;
        }

        .container {
            max-width: 600px;
            margin: 40px auto;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
        }

        h1 {
            text-align: center;
            margin-bottom: 10px;
        }

        #chat-box {
            background: white;
            color: black;
            padding: 10px;
            height: 300px;
            overflow-y: auto;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
        }

        #robot {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 80px;
        }

        #robot-bubble {
            position: fixed;
            bottom: 110px;
            right: 120px;
            background-color: white;
            color: black;
            padding: 10px;
            border-radius: 10px;
            display: none;
            max-width: 200px;
        }
    </style>
</head>
<body>

<header>
    <img src="/static/dreier-logo.png" alt="Dreier Logo">
</header>

<div class="container">
    <h1>Willkommen beim Dreier-KI-Assistenten</h1>
    <p style="text-align:center;">Ich beantworte Ihre Fragen zur Firma Dreier – rund um die Uhr!</p>

    <div id="chat-box"></div>
    <input type="text" id="user-input" placeholder="Ihre Frage zur Firma Dreier..." onkeydown="if(event.key==='Enter') sendMessage()">
</div>

<div id="robot-bubble">Ich denke nach...</div>
<img id="robot" src="/static/roboter.png" alt="Roboter">

<script>
    async function sendMessage() {
        const input = document.getElementById("user-input");
        const chatBox = document.getElementById("chat-box");
        const bubble = document.getElementById("robot-bubble");
        const message = input.value;
        if (!message) return;

        chatBox.innerHTML += "<b>Sie:</b> " + message + "<br>";
        input.value = "";
        bubble.style.display = "block";

        const response = await fetch("/chat", {
            method: "POST",
            body: JSON.stringify({message}),
            headers: {"Content-Type": "application/json"}
        });

        const data = await response.json();
        chatBox.innerHTML += "<b>Assistent:</b> " + data.response + "<br>";
        bubble.style.display = "none";
        chatBox.scrollTop = chatBox.scrollHeight;
    }
</script>

</body>
</html>
