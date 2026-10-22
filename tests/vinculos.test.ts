import { describe, it, expect } from 'vitest';
import { normaliza, clave, conceptos } from '../src/ui/vinculos';

describe('vínculos entre datos', () => {
  it('la misma cantidad escrita distinto tiene la misma clave', () => {
    expect(clave('1.000')).toBe(clave('1000'));
    expect(clave('0,5')).toBe(clave('0.5'));
    expect(normaliza('4.000')).toBe('4000');
    expect(normaliza('9,8')).toBe('9.8');
  });
  it('plural y tilde no separan una palabra', () => {
    expect(clave('Corrientes')).toBe(clave('corriente'));
    expect(clave('Función')).toBe(clave('funcion'));
  });
  it('varias cantidades en una marca no se arrastran entre sí', () => {
    const g = conceptos([{ frag: '2, 3, 3, 4, 8', rol: 'dato' }] as never);
    expect(g.every((s) => s.ks.size === 1)).toBe(true);
    expect(g.some((s) => s.ks.has(clave('3')) && s.ks.has(clave('4')))).toBe(false);
  });
  it('una cantidad se enlaza con su palabra y su unidad nombrada', () => {
    const [taxi, ohm] = [conceptos([{ frag: '$4.000 de arranque', rol: 'dato' }] as never)[0], conceptos([{ frag: '12 V', rol: 'dato' }] as never)[0]];
    expect(taxi.ks.has(clave('4000')) && taxi.ks.has(clave('arranque'))).toBe(true);
    expect(ohm.ks.has(clave('12')) && ohm.ks.has(clave('voltios'))).toBe(true);
  });
  it('cada marca agrupa sus palabras de contenido y descarta las vacías', () => {
    const g = conceptos([{ frag: 'La corriente', rol: 'pide', nota: 'I en amperios' }] as never);
    expect(g[0].ks.has(clave('corriente'))).toBe(true);
    expect(g[0].ks.has(clave('amperios'))).toBe(true);
    expect(g[0].ks.has(clave('para'))).toBe(false);
  });
  it('«fichas» abarca las rojas y las azules aunque la segunda lo calle; «rojas» solo las suyas', () => {
    const enun = 'Una bolsa tiene 3 fichas rojas y 5 azules.';
    const g = conceptos([{ frag: '3 fichas rojas', rol: 'dato' }, { frag: '5 azules', rol: 'dato' }] as never, enun);
    expect(g[0].gen.has(clave('fichas'))).toBe(true);
    expect(g[1].gen.has(clave('fichas'))).toBe(true);
    expect(g[0].gen.has(clave('colores')) && g[1].gen.has(clave('colores'))).toBe(true);
    expect(g[1].ks.has(clave('fichas'))).toBe(false);
  });
  it('una unidad compartida abarca a todos los datos que la usan', () => {
    const g = conceptos([{ frag: 'f = 10 cm', rol: 'dato' }, { frag: '15 cm', rol: 'dato' }] as never, 'f = 10 cm y 15 cm');
    expect(g[0].gen.has(clave('centimetros'))).toBe(true);
    expect(g[1].gen.has(clave('centimetros'))).toBe(true);
  });
});
