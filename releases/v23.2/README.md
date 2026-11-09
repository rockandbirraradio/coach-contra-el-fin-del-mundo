# Respaldo completo — El Coach contra el Fin del Mundo V23.2

**20 misiones, beta de estabilización.** No es una APK ni una edición certificada para Google Play.

Archivo final recuperable: `Coach_20_Misiones_V23_2_Estabilizacion.html` (4.700.641 bytes).

SHA-256 esperado: `4cfbb274eda0a4d71da456b924b56354579299ee2252fbb521f5cd8671bd3a4e`.

Las 14 partes en `parts/` contienen todos los bytes del HTML, sin modificar. Para reconstruir: desde la raíz del repositorio ejecutar `python3 releases/v23.2/restore.py`. La utilidad une las partes en orden, verifica el tamaño y SHA-256, y escribe el HTML en `releases/v23.2/`.

La rama `main` se mantiene intacta. La automatización incluida intenta reconstruir el HTML completo en esta misma rama al recibir el respaldo; si Actions no tiene permisos, la recuperación manual sigue funcionando.

**No borres las partes** aunque se genere el HTML completo: constituyen el respaldo recuperable.
