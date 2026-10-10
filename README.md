# What is an MCP?

A plain-language guide to Model Context Protocol, with an installation-review skill and illustrated explanations.

- [Read the guide](https://what-is-an-mcp.jkylehobson.chatgpt.site/).
- [Existing GitHub Pages address](https://jonathankhobson.github.io/what-is-an-mcp/) remains available, including its original downloads and section links.
- [Download the safety skill](https://what-is-an-mcp.jkylehobson.chatgpt.site/downloads/safe-install-review.skill).

## Edit and check

This repository owns the guide's source. The Sites managed repository is a publication mirror. Edit `index.html` and `assets/`; `docs/project-map.md` describes the other files.

Run `python3 scripts/build.py` from this repository, then `python3 -m http.server 58431 --bind 127.0.0.1 --directory dist`. Open `http://127.0.0.1:58431/` and stop the server when finished. The build uses Python's standard library, performs no network access and replaces only this checkout's ignored `dist/` directory.

Keep the existing skill, ZIP and infographic bytes unchanged. The migration baseline is commit `d1f316dd5cd3d0a140edffd08c1b9ec457ea85c4`. Shared Compass assets are pinned in `vendor/`; their source revisions and hashes are in `vendor/provenance.json`. The builder adapts self-links and active navigation for root hosting. Links to other products retain their current destinations.

## Publish and verify

`.openai/hosting.json` identifies the Site and static `dist/` output. Use the installed Sites source workflow to build, push the reviewed source and package it, then save and deploy that exact commit and archive. Preserve the Site's public audience. A source push alone does not confirm a successful deployment.

Keep GitHub `main` and the Sites source mirror at the same reviewed revision. Check both remote heads before publishing and reconcile any independent hosted-editor changes. Record the source commit, archive hash, saved version and deployment ID in the maintainer's release record. Verify the live guide, mobile navigation, copy control, canonical URL and download bytes after deployment.

The build also serves `/what-is-an-mcp/` and its original download/image paths as compatibility aliases. GitHub Pages remains available as a fallback; no old download URL redirects to HTML. There is no database, secret, authentication integration or runtime storage to migrate. Revert the affected source commit and deploy the corresponding previous artifact to roll back an update.

## Preserved content and rights

The migration preserves the guide, visual identity, illustrations, section IDs and downloads. It repairs overlapping introductory paragraphs and restores keyboard focus to Menu when Escape closes its links.

The existing footer identifies code as AGPL-3.0-only and docs, prompts, skills and methodology as CC BY-SA 4.0; names and official brand assets remain reserved. These statements are preserved without expanding third-party rights. See the [existing license and attribution page](https://jonathankhobson.github.io/compass-suite/license/) and `vendor/provenance.json`. Brand marks are included to present this guide, not licensed for unrelated reuse.
