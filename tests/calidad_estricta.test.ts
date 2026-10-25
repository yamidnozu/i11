import { describe, it, expect } from 'vitest';
import { spawnSync } from 'node:child_process';

describe('revisor estricto de contenido', () => {
  const r = spawnSync('python3', ['tools/auditoria_estricta.py', '--max-fallas', '10'], { encoding: 'utf8' });
  const hay = !r.error;
  it.skipIf(!hay)('no hay preguntas con relleno, razones repetidas, letras contradictorias ni sesgo en el banco propio', () => {
    expect(r.stdout + r.stderr).toContain('con fallas: 0');
    expect(r.status).toBe(0);
  });
});
