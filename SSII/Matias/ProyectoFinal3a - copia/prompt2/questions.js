const questions = [
  {
    id: 1,
    category: "Comandos Windows",
    question: "¿Qué comando de Windows se usa para verificar la configuración IP?",
    options: ["ipconfig", "netstat", "ping", "tracert"],
    correctAnswer: "ipconfig"
  },
  {
    id: 2,
    category: "Comandos Windows",
    question: "¿Qué comando permite ver las conexiones de red activas?",
    options: ["netstat -a", "ipconfig", "nslookup", "route"],
    correctAnswer: "netstat -a"
  },
  {
    id: 3,
    category: "Comandos Windows",
    question: "¿Para qué sirve el comando 'ping'?",
    options: ["Verificar conectividad", "Configurar DNS", "Rastrear ruta", "Ver puertos"],
    correctAnswer: "Verificar conectividad"
  },
  {
    id: 4,
    category: "Comandos Windows",
    question: "¿Qué comando muestra las tareas en ejecución?",
    options: ["tasklist", "services.msc", "taskmgr", "process"],
    correctAnswer: "tasklist"
  },
  {
    id: 5,
    category: "Comandos Windows",
    question: "¿Cuál es el comando para formatear un disco en Windows?",
    options: ["format", "diskpart", "fdisk", "mkfs"],
    correctAnswer: "format"
  },
  {
    id: 6,
    category: "Comandos Linux",
    question: "¿Qué comando Linux muestra el contenido de un directorio?",
    options: ["ls", "dir", "cat", "pwd"],
    correctAnswer: "ls"
  },
  {
    id: 7,
    category: "Comandos Linux",
    question: "¿Para qué sirve el comando 'chmod'?",
    options: ["Cambiar permisos", "Cambiar propietario", "Copiar archivo", "Montar sistema"],
    correctAnswer: "Cambiar permisos"
  },
  {
    id: 8,
    category: "Comandos Linux",
    question: "¿Qué comando se usa para buscar archivos en Linux?",
    options: ["find", "search", "locate", "where"],
    correctAnswer: "find"
  },
  {
    id: 9,
    category: "Comandos Linux",
    question: "¿Cuál es el comando para mostrar el directorio actual?",
    options: ["pwd", "cd", "ls", "dir"],
    correctAnswer: "pwd"
  },
  {
    id: 10,
    category: "Comandos Linux",
    question: "¿Qué comando permite ver los procesos en ejecución?",
    options: ["ps", "top", "kill", "proc"],
    correctAnswer: "ps"
  },
  {
    id: 11,
    category: "Hardware",
    question: "¿Qué componente es considerado el 'cerebro' del computadora?",
    options: ["CPU", "RAM", "Disco duro", "GPU"],
    correctAnswer: "CPU"
  },
  {
    id: 12,
    category: "Hardware",
    question: "¿Qué tipo de memoria es volátil y se borra al apagar el equipo?",
    options: ["RAM", "ROM", "SSD", "HDD"],
    correctAnswer: "RAM"
  },
  {
    id: 13,
    category: "Hardware",
    question: "¿Qué siglas corresponden a la memoria de acceso aleatorio?",
    options: ["RAM", "ROM", "CPU", "GPU"],
    correctAnswer: "RAM"
  },
  {
    id: 14,
    category: "Hardware",
    question: "¿Qué dispositivo se usa para guardar datos de forma permanente?",
    options: ["Disco duro", "RAM", "Cache", "Registro"],
    correctAnswer: "Disco duro"
  },
  {
    id: 15,
    category: "Hardware",
    question: "¿Qué componente se encarga de procesar los gráficos?",
    options: ["GPU", "CPU", "RAM", "Placa base"],
    correctAnswer: "GPU"
  },
  {
    id: 16,
    category: "Redes IP",
    question: "¿Cuántos bits tiene una dirección IPv4?",
    options: ["32", "64", "128", "16"],
    correctAnswer: "32"
  },
  {
    id: 17,
    category: "Redes IP",
    question: "¿Qué servicio traduce nombres de dominio a direcciones IP?",
    options: ["DNS", "DHCP", "FTP", "HTTP"],
    correctAnswer: "DNS"
  },
  {
    id: 18,
    category: "Redes IP",
    question: "¿Qué protocolo se usa para asignar IPs automáticamente?",
    options: ["DHCP", "DNS", "HTTP", "SMTP"],
    correctAnswer: "DHCP"
  },
  {
    id: 19,
    category: "Redes IP",
    question: "¿Qué clase de IP va de 192.0.0.0 a 223.255.255.255?",
    options: ["Clase C", "Clase A", "Clase B", "Clase D"],
    correctAnswer: "Clase C"
  },
  {
    id: 20,
    category: "Redes IP",
    question: "¿Qué significa la máscara 255.255.255.0?",
    options: ["/24", "/16", "/8", "/32"],
    correctAnswer: "/24"
  },
  {
    id: 21,
    category: "Contenedores",
    question: "¿Qué tecnología de contenedores es la más utilizada?",
    options: ["Docker", "VMware", "VirtualBox", "Hyper-V"],
    correctAnswer: "Docker"
  },
  {
    id: 22,
    category: "Contenedores",
    question: "¿Qué comando de Docker crea y ejecuta un contenedor?",
    options: ["docker run", "docker create", "docker start", "docker new"],
    correctAnswer: "docker run"
  },
  {
    id: 23,
    category: "Contenedores",
    question: "¿Qué es un Dockerfile?",
    options: ["Archivo de configuración", "Una imagen", "Un volumen", "Una red"],
    correctAnswer: "Archivo de configuración"
  },
  {
    id: 24,
    category: "Contenedores",
    question: "¿Para qué sirve el comando 'docker-compose'?",
    options: ["Definir servicios múltiples", "Crear imágenes", "Eliminar contenedores", "Monitorear recursos"],
    correctAnswer: "Definir servicios múltiples"
  },
  {
    id: 25,
    category: "Contenedores",
    question: "¿Qué comando lista los contenedores en ejecución?",
    options: ["docker ps", "docker list", "docker containers", "docker show"],
    correctAnswer: "docker ps"
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = questions;
}