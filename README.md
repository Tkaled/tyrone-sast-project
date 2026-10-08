# Tyrone SAST Lab 🔎

Proyecto educativo para demostrar cómo integrar **SAST (Static Application Security Testing)** en un pipeline **CI/CD** utilizando **Semgrep**.

## Tecnologias

- Python
- Flask
- Git
- GitHub
- GitHub Actions
- Semgrep
- VS Code

## Estructura

```text
tyrone-sast-project/
├── app.py
├── requirements.txt
├── README.md
├── .github/
│   └── workflows/
│       └── sast.yml
└── tests/
    └── test_app.py
```

## Vulnerabilidades intencionales

El archivo `app.py` contiene dos vulnerabilidades creadas exclusivamente para el laboratorio:

1. **SQL Injection**
2. **Command Injection**

No deben utilizarse en aplicaciones reales.

## Ejecutar localmente

### 1. Crear entorno virtual

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar

```bash
python app.py
```

Abrir:

```text
http://127.0.0.1:5000
```

## Ejecutar las pruebas

```bash
pytest
```

## SAST con Semgrep

El workflow:

```text
.github/workflows/sast.yml
```

se ejecuta automáticamente cuando se hace `push` o se crea/actualiza un Pull Request.

Flujo:

```text
Desarrollador
     |
     v
 Git Push
     |
     v
GitHub Actions
     |
     v
  Semgrep
     |
     v
Analisis SAST
     |
  +--+----------------+
  |                   |
  v                   v
Hallazgos           Sin hallazgos
  |                   |
  v                   v
Revisar             Continuar
```

## Objetivo académico

El objetivo es demostrar que una herramienta SAST puede analizar el código durante el proceso de integración continua y detectar problemas de seguridad antes de que el software llegue a producción.

## Importante

Las vulnerabilidades de este proyecto son intencionales y están diseñadas para un entorno local de aprendizaje. No se deben copiar estas prácticas a sistemas reales.
