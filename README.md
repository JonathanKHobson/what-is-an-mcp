# MCP explainer migration pilot

Local candidate for the existing [MCP explainer](https://jonathankhobson.github.io/what-is-an-mcp/). This branch is prepared for review. It is not a registered, saved or deployed ChatGPT Site.

## Edit and check

Edit `index.html` and `assets/`. Run `python3 scripts/build.py` from this repository, then `python3 -m http.server 58431 --bind 127.0.0.1 --directory dist`. Open `http://127.0.0.1:58431/`. Stop the server when finished. The build uses Python's standard library, performs no network access and replaces only this checkout's ignored `dist/` directory.

Keep the existing downloadable skill, ZIP and infographic bytes unchanged. The source and public site share commit `d1f316dd5cd3d0a140edffd08c1b9ec457ea85c4` as the migration baseline. Shared Compass assets are pinned in `vendor/`; their exact source URLs and hashes are in `vendor/provenance.json`. The builder changes self-links and active-navigation detection for root hosting. Outgoing links to other products keep their current destinations.

The visual correction groups the two introduction paragraphs that overlapped in the live desktop layout. A second scoped repair returns keyboard focus to Menu when Escape closes its links. The existing identity, copy, illustrations, download filenames and section IDs remain. The preserved source includes its original typography and punctuation.

## Publishing boundary

`.openai/hosting.json` declares static `dist/` with no invented Site ID. Registration, a Sites source push, saved version, deployment and any GitHub push need the Phase 2 approval recorded outside this public candidate. After approval, use the installed Sites workflow, persist the returned project ID, rebuild and record the source commit, package hash, saved version and deployment ID together. The Sites helper can commit and push; it is not a harmless local packaging command.

Retain the old Pages site and download URLs during the pilot. The build also serves `/what-is-an-mcp/` and its original download/image paths as compatibility aliases on the future host. Add the exact canonical URL after host approval. Do not implement redirects before the destination is deployed and checked. No database, uploaded files, credentials or server behavior are needed by this pilot.

## Rights and ownership

This is an unchanged-content migration of Kyle Hobson's existing public guide. Its current footer identifies code as AGPL-3.0-only and docs, prompts, skills and methodology as CC BY-SA 4.0, with names and official brand assets reserved. Those existing statements are preserved, not expanded to undocumented third-party rights. [Existing license and attribution page](https://jonathankhobson.github.io/compass-suite/license/). Do not treat the included brand marks as a general redistribution license. Before public source packaging, verify individual image and download notices and add the applicable full license texts.
