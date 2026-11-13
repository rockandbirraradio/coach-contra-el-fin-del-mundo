# El Coach contra el Fin del Mundo — Android V24.0 RC1

Estado: **candidata funcional aprobada en Samsung; respaldo de los binarios Android pendiente de carga**.

La rama se creó desde `backup/v23.1-beta-20-misiones`, conservando el HTML completo de las 20 misiones V23.2 y su reconstrucción documentada. **La rama main no se modificó.**

## Identidad de la candidata aprobada

- Paquete: `com.rockandbirra.coach`
- `versionCode`: `240`
- `versionName`: `24.0-beta`
- Tipo: **APK debug** (NO subir a Google Play como edición de publicación)
- Nombre de respaldo local: `EL_COACH_V24_0_RC1_20_MISIONES.apk`
- SHA-256 de la APK aprobada (copia validada en Windows): `B75E5B2C0F53D164D7371744056B4A8217EF47FFD0FA35C1789E2A662CA8693A`
- SHA-256 del HTML V23.2: `4cfbb274eda0a4d71da456b924b56354579299ee2252fbb521f5cd8671bd3a4e`
- QA reportado por el propietario: instalación como actualización de V16.4, SAVE conservado, controles, audio, modo avión, icono y final misión 20 aprobados.

## Archivos necesarios para completar respaldo Android (TODAVÍA NO CARGADOS)

1. Copia limpia del proyecto `RockAndBirra_Android_V24_0_20_MISIONES`, excluyendo `.gradle/`, `.idea/`, `build/`, `app/build/`, `local.properties`, `*.keystore`, `*.jks`, `*.key`, contraseñas, tokens y cualquier secreto.
2. APK RC1 exacta, identificada por el SHA-256 indicado arriba. Subir como artefacto de GitHub Releases o a una ubicación privada si se desea evitar distribuir APK debug públicamente.
3. Registrar pruebas de reconstrucción, checksum y compilación limpia en otro equipo.

## Reglas de congelación

- No cambiar 20 misiones, controles, SAVE, radio, sonidos, icono oficial ni archivos aprobados.
- Mantener `main`, proyecto original V15.1 y APK instalada intactos.
- No usar el almacén `debug.keystore` para publicación.
- Para Play Store, generar AAB de **release** con una clave de carga privada custodiada por el propietario, configurar Play App Signing y cumplir requisitos vigentes de target API, ficha y pruebas.
- No afirmar que el código Android completo o la APK ya están respaldados en GitHub hasta verificar su carga y SHA.

## Plan de acción

1. Completar respaldo seguro del proyecto Android y binario RC1.
2. Conservar una segunda copia externa del APK y verificar SHA-256.
3. Preparar compilación de lanzamiento (AAB) en un clon separado, sin afectar RC1.
