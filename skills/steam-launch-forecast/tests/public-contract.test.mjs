import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const root = new URL('..', import.meta.url);
const read = (path) => readFile(new URL(path, root), 'utf8');

test('skill requires a forecast mode and a knowledge cutoff', async () => {
  const skill = await read('SKILL.md');

  assert.match(skill, /Forecast mode:/);
  assert.match(skill, /Knowledge cutoff:/);
  assert.match(skill, /blind_prelaunch/);
  assert.match(skill, /post_launch_nowcast/);
  assert.match(skill, /unbiased/i);
});

test('public calibration contract protects timing, evidence, and metric definitions', async () => {
  const contract = await read('references/calibration-contract.md');

  assert.match(contract, /issued_at/);
  assert.match(contract, /knowledge_cutoff_at/);
  assert.match(contract, /date-only/);
  assert.match(contract, /IANA time zone/);
  assert.match(contract, /verified/);
  assert.match(contract, /provisional/);
  assert.match(contract, /disputed/);
  assert.match(contract, /not.*cohort conversion/i);
  assert.match(contract, /WAPE/);
  assert.match(contract, /provisional.*not generalizable/i);
});

test('public test prompts cover leakage and published-data boundaries', async () => {
  const prompts = await read('examples/test-prompts.md');
  const readme = await read('README.md');

  assert.match(prompts, /same day/i);
  assert.match(prompts, /released game/i);
  assert.match(readme, /private calibration/i);
  assert.match(readme, /calibration-contract\.md/);
});
