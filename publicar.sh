#!/usr/bin/env bash
set -e

# Mensaje de commit (si no se especifica, usa uno por defecto con la fecha y hora)
MENSAJE=${1:-"Actualización del sitio web $(date '+%Y-%m-%d %H:%M')"}

echo "🔨 1. Compilando el sitio con Quarto..."
quarto render

echo "📦 2. Preparando archivos para Git..."
git add .

echo "💾 3. Creando commit: '$MENSAJE'..."
git commit -m "$MENSAJE"

echo "🚀 4. Subiendo a GitHub Pages..."
git push

echo "✅ ¡Listo! En menos de 1 minuto tus cambios estarán en vivo en:"
echo "👉 https://djguerrero23.github.io/Portafolio-Ingenieria-Electrica/"
