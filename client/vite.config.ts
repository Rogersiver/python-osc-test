import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: true,
    strictPort: true,
    hmr: false,
  },
  plugins: [react()],
});
