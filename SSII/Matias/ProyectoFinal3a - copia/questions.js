/**
 * questions.js — Banco de Preguntas
 * 
 * Contiene todas las preguntas del test organizadas por categorías.
 * Solo exporta datos, no contiene lógica.
 * 
 * Categorías: windows, linux, hardware, redes, contenedores
 */

const CATEGORIES = [
    { id: 'windows',       name: 'Comandos Windows', icon: '🪟', description: 'CMD, PowerShell y gestión del sistema' },
    { id: 'linux',         name: 'Comandos Linux',   icon: '🐧', description: 'Terminal, permisos y paquetes' },
    { id: 'hardware',      name: 'Hardware',          icon: '🖥️', description: 'Componentes y arquitectura' },
    { id: 'redes',         name: 'Redes IP',          icon: '🌐', description: 'Direccionamiento y protocolos' },
    { id: 'contenedores',  name: 'Contenedores',      icon: '🐳', description: 'Docker, imágenes y volúmenes' }
];

const QUESTIONS = [
    // ==================== COMANDOS WINDOWS ====================
    {
        id: 1,
        category: 'windows',
        question: '¿Qué comando muestra la configuración IP en Windows?',
        options: ['ipconfig', 'ifconfig', 'ip addr', 'netstat'],
        correct: 0
    },
    {
        id: 2,
        category: 'windows',
        question: '¿Qué comando se usa para listar archivos y carpetas en CMD?',
        options: ['ls', 'list', 'dir', 'show'],
        correct: 2
    },
    {
        id: 3,
        category: 'windows',
        question: '¿Cuál es el comando para hacer ping a una dirección en Windows?',
        options: ['trace', 'ping', 'connect', 'reach'],
        correct: 1
    },
    {
        id: 4,
        category: 'windows',
        question: '¿Qué comando copia archivos y directorios de forma recursiva en CMD?',
        options: ['copy', 'cp', 'xcopy', 'move'],
        correct: 2
    },
    {
        id: 5,
        category: 'windows',
        question: '¿Qué comando muestra los procesos en ejecución en CMD?',
        options: ['ps', 'top', 'tasklist', 'proclist'],
        correct: 2
    },

    // ==================== COMANDOS LINUX ====================
    {
        id: 6,
        category: 'linux',
        question: '¿Qué comando cambia los permisos de un archivo en Linux?',
        options: ['chown', 'chmod', 'chperm', 'perm'],
        correct: 1
    },
    {
        id: 7,
        category: 'linux',
        question: '¿Qué comando muestra el contenido de un archivo en Linux?',
        options: ['show', 'display', 'cat', 'read'],
        correct: 2
    },
    {
        id: 8,
        category: 'linux',
        question: '¿Qué comando se usa para instalar paquetes en distribuciones basadas en Debian?',
        options: ['yum install', 'pacman -S', 'apt install', 'rpm -i'],
        correct: 2
    },
    {
        id: 9,
        category: 'linux',
        question: '¿Qué comando muestra el espacio en disco usado por directorios?',
        options: ['df', 'du', 'disk', 'space'],
        correct: 1
    },
    {
        id: 10,
        category: 'linux',
        question: '¿Qué comando busca archivos en el sistema de archivos de Linux?',
        options: ['search', 'locate', 'find', 'grep'],
        correct: 2
    },

    // ==================== HARDWARE ====================
    {
        id: 11,
        category: 'hardware',
        question: '¿Qué componente es el "cerebro" del ordenador?',
        options: ['RAM', 'CPU', 'GPU', 'SSD'],
        correct: 1
    },
    {
        id: 12,
        category: 'hardware',
        question: '¿Qué tipo de memoria es volátil y se borra al apagar el equipo?',
        options: ['SSD', 'ROM', 'RAM', 'HDD'],
        correct: 2
    },
    {
        id: 13,
        category: 'hardware',
        question: '¿Cuál de estos es un dispositivo de almacenamiento no volátil?',
        options: ['RAM', 'Caché L1', 'Registro CPU', 'SSD'],
        correct: 3
    },
    {
        id: 14,
        category: 'hardware',
        question: '¿Qué componente conecta todos los elementos del ordenador entre sí?',
        options: ['Fuente de alimentación', 'Placa base', 'Disipador', 'Ventilador'],
        correct: 1
    },
    {
        id: 15,
        category: 'hardware',
        question: '¿Qué unidad se utiliza para medir la velocidad del procesador?',
        options: ['MB', 'GHz', 'TB', 'Mbps'],
        correct: 1
    },

    // ==================== REDES IP ====================
    {
        id: 16,
        category: 'redes',
        question: '¿Cuántos bits tiene una dirección IPv4?',
        options: ['16', '32', '64', '128'],
        correct: 1
    },
    {
        id: 17,
        category: 'redes',
        question: '¿Qué máscara de subred corresponde a un /24?',
        options: ['255.255.0.0', '255.255.255.0', '255.255.255.128', '255.0.0.0'],
        correct: 1
    },
    {
        id: 18,
        category: 'redes',
        question: '¿Qué protocolo se encarga de resolver nombres de dominio a direcciones IP?',
        options: ['DHCP', 'FTP', 'DNS', 'HTTP'],
        correct: 2
    },
    {
        id: 19,
        category: 'redes',
        question: '¿Cuál es la dirección IP de loopback?',
        options: ['192.168.1.1', '10.0.0.1', '127.0.0.1', '0.0.0.0'],
        correct: 2
    },
    {
        id: 20,
        category: 'redes',
        question: '¿Qué puerto usa por defecto el protocolo HTTP?',
        options: ['21', '443', '22', '80'],
        correct: 3
    },

    // ==================== CONTENEDORES ====================
    {
        id: 21,
        category: 'contenedores',
        question: '¿Qué comando descarga una imagen de Docker Hub?',
        options: ['docker get', 'docker download', 'docker pull', 'docker fetch'],
        correct: 2
    },
    {
        id: 22,
        category: 'contenedores',
        question: '¿Qué comando lista los contenedores en ejecución?',
        options: ['docker list', 'docker ps', 'docker running', 'docker show'],
        correct: 1
    },
    {
        id: 23,
        category: 'contenedores',
        question: '¿Qué archivo define la configuración de un contenedor Docker?',
        options: ['docker-config.yml', 'container.json', 'Dockerfile', 'docker-setup.xml'],
        correct: 2
    },
    {
        id: 24,
        category: 'contenedores',
        question: '¿Qué comando para y elimina todos los recursos definidos en docker-compose?',
        options: ['docker-compose stop', 'docker-compose down', 'docker-compose remove', 'docker-compose kill'],
        correct: 1
    },
    {
        id: 25,
        category: 'contenedores',
        question: '¿Qué flag se usa para ejecutar un contenedor en segundo plano (detached)?',
        options: ['-b', '-s', '-d', '-bg'],
        correct: 2
    }
];
