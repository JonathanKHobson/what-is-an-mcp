# Project map

- `index.html`: authored guide, section IDs, download links and copy interaction.
- `assets/network.css`: existing published style snapshot. `assets/migration-fixes.css`: scoped repair for the overlapping introductory paragraphs.
- `downloads/`, `mcp-infographic/`: preserved public artifacts, not regenerated here.
- `vendor/compass-suite/`: five pinned public shell dependencies, provenance in `vendor/provenance.json`.
- `scripts/build.py`: deterministic, offline static projection into ignored `dist/`, including root self-links and compatibility paths.
- `.openai/hosting.json`: local static configuration. Add a real project ID only through approved registration.

Python standard library is the only build dependency. No secrets, environment variables, database migrations or runtime storage are required. README.md owns the local run and publishing boundary. The external Phase 2 record owns approval, evidence and rollback; do not copy private ecosystem records into this repository.
