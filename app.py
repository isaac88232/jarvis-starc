import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- ⚙️ CONFIGURACIÓN ---
# Reemplaza los ceros por tu número real (ej: 593987654321)
MI_WHATSAPP = "56977524476" 

# --- 🌌 INTERFAZ JARVIS UNIVERSITARIA V3 ---
HTML_APP = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>JARVIS OS</title>
    <style>
        body { background: #000; color: #fff; font-family: sans-serif; margin: 0; height: 100vh; overflow: hidden; transition: 1s; }
        body.universitario { background: radial-gradient(circle, #2b2100 0%, #000 100%); }
        
        #jarvis-core { 
            position: fixed; top: 40%; left: 50%; transform: translate(-50%, -50%) scale(0); 
            width: 280px; height: 280px; border-radius: 50%; opacity: 0; transition: 0.6s;
            background: url('https://i.pinimg.com/originals/3e/2d/a2/3e2da29188e70a6c761b6e4e08282f1b.gif') center/cover;
            filter: drop-shadow(0 0 20px #00ffff); z-index: 10;
        }
        #jarvis-core.mostrar { transform: translate(-50%, -50%) scale(1); opacity: 1; }
        body.universitario #jarvis-core { filter: drop-shadow(0 0 20px #ffd700); }
        
        #chat { padding: 20px; height: 75vh; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; }
        .bubble { padding: 12px; border-radius: 18px; max-width: 80%; font-size: 15px; border: 1px solid #222; }
        .jarvis { color: #00ffcc; background: rgba(0,255,204,0.05); align-self: flex-start; }
        .u-log { color: #ffd700; background: rgba(255,215,0,0.05); align-self: flex-start; font-weight: bold; border-color: #665500; }
        .usuario { background: #111; align-self: flex-end; }
        
        /* BOTÓN WHATSAPP FLOTANTE */
        .wa-link { 
            position: fixed; top: 20px; right: 20px; background: #25d366; 
            color: white; width: 45px; height: 45px; border-radius: 50%; 
            display: flex; align-items: center; justify-content: center; 
            text-decoration: none; font-size: 22px; z-index: 100; box-shadow: 0 0 10px #25d366;
        }

        .console { position: fixed; bottom: 0; width: 100%; padding: 20px; background: #000; display: flex; gap: 10px; border-top: 1px solid #222; }
        input { flex: 1; background: #0a0a0a; border: 1px solid #333; color: #fff; padding: 15px; border-radius: 30px; outline: none; }
        .btn-send { background: #00ffcc; border: none; width: 50px; height: 50px; border-radius: 50%; cursor: pointer; }
    </style>
</head>
<body id="main">
    <a href="https://wa.me/{{ wa_num }}" class="wa-link" target="_blank">💬</a>

    <div id="jarvis-core"></div>
    <div id="chat">
        <div class="bubble jarvis">Sistemas en línea, Isaac Briones. Esperando comandos.</div>
    </div>
    <div class="console">
        <input type="text" id="in" placeholder="Comando..." onkeypress="if(event.key==='Enter') ejecutar()">
        <button class="btn-send" onclick="ejecutar()">▶</button>
    </div>
    <script>
        function ejecutar() {
            const i = document.getElementById('in');
            const c = document.getElementById('chat');
            const b = document.getElementById('main');
            const core = document.getElementById('jarvis-core');
            const val = i.value.toLowerCase();
            if(!val) return;
            
            c.innerHTML += `<div class="bubble usuario">${i.value}</div>`;
            
            if (val.includes("modo universitario")) {
                b.classList.add('universitario');
                core.classList.add('mostrar');
                setTimeout(() => { 
                    core.classList.remove('mostrar'); 
                    c.innerHTML += `<div class="bubble u-log">🏛️ ACCESO UNIVERSITARIO. Optimizando bases de datos para investigación.</div>`; 
                }, 3000);
            } else {
                c.innerHTML += `<div class="bubble jarvis">Procesando consulta en red...</div>`;
            }
            i.value = "";
            c.scrollTop = c.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    # Enviamos el número de WhatsApp a la interfaz
    return render_template_string(HTML_APP, wa_num=MI_WHATSAPP)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
