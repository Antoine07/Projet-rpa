import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Permet les connexions externes
    port: 5174,      // Port à exposer
    strictPort: true, // Évite de changer de port automatiquement
    watch: {
      usePolling: true // Pour que Docker détecte les changements de fichiers
    }
  }
})