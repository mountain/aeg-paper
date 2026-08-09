# Legacy root manuscript

This directory archives the monolithic AEG manuscript that immediately preceded
the four-paper restructuring.

- Entry point: `aeg-paper.tex`
- Build command: `./build.sh`
- Section sources: `sections/sec01.tex`--`sections/sec12.tex`
- Historical source revision: `095ae4b28cb645ea43e18aa2560d227830cc3a14`
  (`paper: add ACS torsion and contact curvature`, 2026-08-06)

The entry point was recovered verbatim from that revision. The section files are
the corresponding tracked legacy sources; only an archival provenance comment was
added to each file. Their mathematical content is unchanged. This bundle is retained
for provenance and is not an authoritative source for Papers I--IV.

The mathematical content remains archival and non-authoritative. The entry point's
resource paths have been adjusted so that it can be compiled in this directory while
continuing to use the repository-level bibliography and images and the archived
LaTeX styles. The build writes `aeg-paper.pdf` and the usual LaTeX auxiliary files
to this directory.
