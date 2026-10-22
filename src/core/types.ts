import type { AreaId } from '../adaptive/areas';

export type ParamValue = number | boolean | string;
export type Params = Record<string, ParamValue>;
export type M = Record<string, number>;

export interface ParamDef {
  key: string;
  label: string;
  type: 'slider' | 'select' | 'toggle' | 'text' | 'custom';
  min?: number;
  max?: number;
  step?: number;
  default: ParamValue;
  unit?: string;
  options?: { v: number; l: string }[];
  hint?: string;
  build?: (c: { params: Params; set: (k: string, v: ParamValue) => void }) => HTMLElement;
}

export interface GraphDef { id: string; x: string; y: string; title: string }
export interface GoalCheck { measure: string; target: number; tol: number }
export interface Challenge { id: string; prompt: string; fixed?: Params; checks: GoalCheck[]; hint?: string }

/** Contrato de lógica: funciones puras, sin DOM, testeables. */
export interface SimLogic<S> {
  init(p: Params): S;
  step?(s: S, p: Params, dt: number): S;
  done?(s: S, p: Params): boolean;
  sample?(s: S): Record<string, number>;
  measures(traj: S[], p: Params): M;
}

export interface ViewCtx<S> {
  ctx: CanvasRenderingContext2D;
  w: number;
  h: number;
  state: S;
  traj: S[];
  p: Params;
  measures: M;
  time: number;
  pointer: { x: number; y: number } | null;
}

/** Un paso de una resolución: título, expresión (mini-TeX) y nota opcional (admite $tex$). */
export interface Step { t: string; tex: string; nota?: string }
export interface Formula { tex: string; nombre: string; vars: [string, string][] }
export interface Learn {
  resumen: string;
  objetivos: string[];
  idea: string[];
  analogia?: string;
  formulas: Formula[];
  ejemplos: { titulo: string; texto: string; pasos: string[] }[];
  errores: { mito: string; realidad: string }[];
  saber11: string;
}
export interface Preset { id: string; label: string; desc: string; params: Params }
export interface Experiment {
  id: string; titulo: string; setup: Params; cambio?: Params;
  pregunta: string; opciones: string[]; correcta: number; explicacion: string;
  /** Solo para pruebas: verifica numéricamente que la explicación es cierta. */
  check?: (antes: M, despues: M) => boolean;
}
export interface CompareRow { label: string; teoria: number; sim: number; nota?: string }

export interface Extra<S = any> {
  learn: Learn;
  presets?: Preset[];
  experiments?: Experiment[];
  solution?: (p: Params, m: M) => Step[];
  compare?: (p: Params, m: M) => CompareRow[];
  insight?: (p: Params, m: M) => string;
  paramHints?: Record<string, string>;
  paramOverrides?: Record<string, Partial<ParamDef>>;
  readouts?: string[];
  ambient?: boolean;
  size?: { width: number; height: number };
  view?: (v: ViewCtx<S>) => void;
}

export interface SimConfig<S = any> {
  id: string;
  title: string;
  area: AreaId;
  subarea?: string;
  competencia: string;
  evidencias: string[];
  nivel: number;
  tiempoMin: number;
  mode: 'dynamic' | 'static';
  params: ParamDef[];
  logic: SimLogic<S>;
  render: { width: number; height: number; view: (v: ViewCtx<S>) => void };
  graphs?: GraphDef[];
  measureLabels?: Record<string, string>;
  challenges: Challenge[];
  table?: (p: Params, traj: S[]) => { cols: string[]; rows: (number | string)[][] };
  describe?: (m: M, p: Params) => string;
  learn?: Learn;
  presets?: Preset[];
  experiments?: Experiment[];
  solution?: Extra['solution'];
  compare?: Extra['compare'];
  insight?: Extra['insight'];
  readouts?: string[];
  ambient?: boolean;
}
