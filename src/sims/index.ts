import { register, listSims } from '../core/registry';
import { projectileSim } from './projectile';
import { muaSim } from './mrua';
import { ohmSim } from './ohm';
import { lensSim } from './lens';
import { gasSim } from './gases';
import { functionsSim } from './functions';
import { balanceSim } from './balance';
import { punnettSim } from './punnett';
import { lotkaSim } from './lotka';
import { probabilitySim } from './probability';
import { statsSim } from './stats';
import { enrich } from '../core/enrich';
import { labsCompilados } from '../lab';
import { projectileExtra } from '../learn/projectile';
import { muaExtra } from '../learn/mrua';
import { ohmExtra } from '../learn/ohm';
import { lensExtra } from '../learn/lens';
import { gasExtra } from '../learn/gases';
import { functionsExtra } from '../learn/functions';
import { balanceExtra } from '../learn/balance';
import { punnettExtra } from '../learn/punnett';
import { lotkaExtra } from '../learn/lotka';
import { probabilityExtra } from '../learn/probability';
import { statsExtra } from '../learn/stats';


const BASE_SIMS = [
  enrich(projectileSim, projectileExtra), enrich(muaSim, muaExtra), enrich(ohmSim, ohmExtra), enrich(lensSim, lensExtra),
  enrich(gasSim, gasExtra), enrich(functionsSim, functionsExtra), enrich(balanceSim, balanceExtra), enrich(punnettSim, punnettExtra),
  enrich(lotkaSim, lotkaExtra), enrich(probabilitySim, probabilityExtra), enrich(statsSim, statsExtra),
];

/** Un laboratorio en content/labs/ con el mismo id reemplaza al hecho en código; los ids nuevos se agregan. */
const JSON_LABS = labsCompilados();
export const ALL_SIMS = [...BASE_SIMS.map((b) => JSON_LABS.find((j) => j.id === b.id) ?? b), ...JSON_LABS.filter((j) => !BASE_SIMS.some((b) => b.id === j.id))];
export const BASE_CODIGO = BASE_SIMS;

let done = false;
export function registerAll() {
  if (done) return listSims();
  ALL_SIMS.forEach((s) => register(s as any));
  done = true;
  return listSims();
}
