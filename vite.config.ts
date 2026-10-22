import { defineConfig, loadEnv } from 'vite';

/** Contenido oficial del Icfes (content/icfes/): solo entra al build si VITE_ICFES=1. Sin permiso escrito del Icfes, la versión publicada no lo incluye. */
export default defineConfig(({ mode }) => {
  const env = { ...loadEnv(mode, process.cwd(), 'VITE_'), ...process.env };
  const incluir = env.VITE_ICFES === '1';
  return {
    plugins: [{ name: 'icfes-gate', enforce: 'pre' as const, load(id: string) { if (!incluir && /[\\/]content[\\/]icfes[\\/].*\.json$/.test(id)) return '[]'; return null; } }],
    build: { target: 'es2020', sourcemap: false, chunkSizeWarningLimit: 300 },
    test: { environment: 'node', include: ['tests/**/*.test.ts'] },
  };
});
