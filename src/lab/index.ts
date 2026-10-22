import type { SimConfig } from '../core/types';
import type { LabJSON } from './schema';
import { validateLab } from './schema';
import { compileLab } from './compile';

const lm = import.meta.glob('../../content/labs/*.json', { eager: true, import: 'default' }) as Record<string, LabJSON | LabJSON[]>;
const pk = import.meta.glob('../../content/packs/**/*.json', { eager: true, import: 'default' }) as Record<string, { labs?: LabJSON[] } | { labs?: LabJSON[] }[]>;
const todos: LabJSON[] = [...Object.values(lm).flatMap((x) => (Array.isArray(x) ? x : [x])), ...Object.values(pk).flatMap((x) => (Array.isArray(x) ? x : [x])).flatMap((x) => x.labs ?? [])];
export const LAB_WARNINGS: string[] = [];
export const LABS_JSON: LabJSON[] = todos.filter((j) => { const e = validateLab(j); if (e.length) { LAB_WARNINGS.push(...e); console.warn('[laboratorios]', e.join('; ')); return false; } return true; });
export const labsCompilados = (): SimConfig[] => LABS_JSON.map(compileLab);
export { compileLab, validateLab };
