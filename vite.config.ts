import { defineConfig, loadEnv } from 'vite';
import { copyFileSync, existsSync, mkdirSync, readdirSync } from 'node:fs';
import { resolve } from 'node:path';

function gateIcfesAssets(include: boolean) {
  let root = process.cwd();
  let outDir = resolve(root, 'dist');
  return {
    name: 'icfes-asset-gate',
    apply: 'build' as const,
    configResolved(config: { root: string; build: { outDir: string } }) {
      root = config.root;
      outDir = resolve(root, config.build.outDir);
    },
    closeBundle() {
      if (!include) return;
      const source = resolve(root, 'content/icfes');
      if (!existsSync(source)) return;
      for (const prefix of readdirSync(source, { withFileTypes: true }).filter(x => x.isDirectory())) {
        const imageDir = resolve(source, prefix.name, 'imagenes');
        if (!existsSync(imageDir)) continue;
        const target = resolve(outDir, 'icfes', prefix.name);
        mkdirSync(target, { recursive: true });
        for (const file of readdirSync(imageDir, { withFileTypes: true }).filter(x => x.isFile())) {
          copyFileSync(resolve(imageDir, file.name), resolve(target, file.name));
        }
      }
    },
  };
}

/** Contenido oficial del Icfes (content/icfes/): solo entra al build si VITE_ICFES=1. Sin permiso escrito del Icfes, la versión publicada no lo incluye. */
export default defineConfig(({ mode }) => {
  const env = { ...loadEnv(mode, process.cwd(), 'VITE_'), ...process.env };
  const incluir = env.VITE_ICFES === '1';
  return {
    plugins: [
      { name: 'icfes-gate', enforce: 'pre' as const, load(id: string) { if (!incluir && /[\\/]content[\\/]icfes[\\/].*\.json$/.test(id)) return '[]'; return null; } },
      gateIcfesAssets(incluir),
    ],
    build: { target: 'es2020', sourcemap: false, chunkSizeWarningLimit: 300 },
    test: { environment: 'node', include: ['tests/**/*.test.ts'] },
  };
});
