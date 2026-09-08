#!/usr/bin/env node
/*
 * Regenerate `<program>.blocks` from `<program>.ts` using MakeCode's *real*
 * pxt decompiler, run locally (no browser).
 *
 * Why this exists
 * ---------------
 * An anonymous MakeCode share only opens on the **Blocks** tab if its
 * `main.blocks` file contains real block XML. An empty placeholder gives a
 * Blocks tab you must click — it still lands on JavaScript. MakeCode only
 * decompiles TypeScript -> blocks inside its editor, so this script drives the
 * same decompiler headlessly via the `makecode` (mkc) toolchain and writes the
 * XML next to each `main.ts`. scripts/publish_makecode.py then ships it.
 *
 * Setup / usage
 * -------------
 *   npm i makecode          # or run once via: npx -y makecode --help
 *   node scripts/decompile_blocks.js <code-dir> [<code-dir> ...]
 *
 * Each <code-dir> is a lesson's `code/` folder; every `*.ts` in it is
 * decompiled to a sibling `*.blocks`. With no args it does nothing (be
 * explicit about which lessons to (re)bake). Re-run whenever a `main.ts`
 * changes, then run publish_makecode.py to mint fresh shares.
 *
 * All programs here use the default core/radio/microphone deps; if a lesson
 * adds a `deps.txt`, extend PXT_JSON below before baking it.
 */
const fs = require("fs");
const os = require("os");
const path = require("path");

// Resolve the mkc modules whether installed locally or via the npx cache.
function loadMkc() {
  const tries = [];
  const req = (m) => { try { return require(m); } catch (e) { tries.push(m); return null; } };
  let host = req("makecode-core/built/host");
  let nodeHost = req("makecode/built/nodeHost");
  let mkc = req("makecode-core/built/mkc");
  if (host && nodeHost && mkc) return { host, nodeHost, mkc };
  console.error(
    "Could not resolve the 'makecode' toolchain. Install it first:\n" +
    "  npm i makecode\n" +
    "or run this script from a directory where 'npx -y makecode' has been run."
  );
  process.exit(2);
}

const TARGET_WEBSITE = "https://makecode.microbit.org/";
const DEPS = { core: "*", radio: "*", microphone: "*" };

async function main() {
  const dirs = process.argv.slice(2);
  if (dirs.length === 0) {
    console.error("usage: node scripts/decompile_blocks.js <code-dir> [<code-dir> ...]");
    process.exit(1);
  }
  const { host, nodeHost, mkc } = loadMkc();
  host.setHost(nodeHost.createNodeHost());
  mkc.setLogging({ log: () => {}, error: (m) => console.error("[mkc] " + m), debug: () => {} });

  // A throwaway mkc project the decompiler compiles against; main.ts is swapped
  // per program. node_modules is linked so requires resolve inside the temp dir.
  const work = fs.mkdtempSync(path.join(os.tmpdir(), "mkc-decompile-"));
  fs.writeFileSync(path.join(work, "mkc.json"),
    JSON.stringify({ targetWebsite: TARGET_WEBSITE, links: {} }, null, 2));
  fs.writeFileSync(path.join(work, "pxt.json"), JSON.stringify({
    name: "decompile-work", dependencies: DEPS,
    files: ["main.ts"], preferredEditor: "tsprj",
  }, null, 4));
  fs.writeFileSync(path.join(work, "main.ts"), "");
  try {
    const resolved = path.dirname(require.resolve("makecode-core/built/mkc"));
    fs.symlinkSync(path.resolve(resolved, "../../.."), path.join(work, "node_modules"), "dir");
  } catch (e) { /* modules already resolvable from cwd */ }

  const prj = new mkc.Project(work);
  await prj.loadEditorAsync();

  let ok = 0, fail = 0;
  for (const dir of dirs) {
    const tsFiles = fs.readdirSync(dir).filter((f) => f.endsWith(".ts")).sort();
    for (const ts of tsFiles) {
      const name = ts.replace(/\.ts$/, "");
      fs.writeFileSync(path.join(work, "main.ts"), fs.readFileSync(path.join(dir, ts)));
      prj.mainPkg = null; prj.lastPxtJson = null;
      await prj.loadPkgAsync();
      const opts = await prj.service.getOptionsAsync(prj.mainPkg);
      opts.ast = true;
      const res = await prj.service.languageService.performOperationAsync(
        "decompile", { options: opts, fileName: "main.ts" });
      const blocks = res && res.outfiles && res.outfiles["main.blocks"];
      if (blocks && blocks.includes("<block ")) {
        fs.writeFileSync(path.join(dir, `${name}.blocks`), blocks);
        console.log(`OK   ${dir}/${name}.blocks (${blocks.length} bytes)`);
        ok++;
      } else {
        const why = (res && (res.errorMessage || JSON.stringify(res.diagnostics))) || "empty";
        console.error(`FAIL ${dir}/${name}: ${String(why).slice(0, 200)}`);
        fail++;
      }
    }
  }
  if (prj.service.languageService.dispose) prj.service.languageService.dispose();
  console.log(`\ndone: ${ok} decompiled, ${fail} failed`);
  process.exit(fail ? 1 : 0);
}

main().catch((e) => { console.error("FATAL", (e && (e.stack || e.message)) || e); process.exit(1); });
