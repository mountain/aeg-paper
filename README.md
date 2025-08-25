# aeg-paper

[![DOI](https://zenodo.org/badge/16938961.svg)](https://zenodo.org/badge/latestdoi/16938961)

This paper introduces a novel geometric framework for studying arithmetic expressions, 
establishing a rigorous connection between algebraic operations and hyperbolic geometry.
We formalize arithmetic expressions as syntactic structures and demonstrate how they can be embedded into continuous geometric spaces where addition and multiplication correspond to movements along orthogonal directions.
Central to our approach is a flow equation that governs how expression values propagate through this geometric space.
We construct the first kind arithmetic expression space $\mathfrak{E}_1$ on the upper half-plane with a hyperbolic metric,
where the assignment function satisfies the flow equation and serves as an eigenfunction of the Laplacian.
This construction reveals that arithmetic torsion—the non-commutativity of addition and multiplication—directly
corresponds to geometric area, analogous to how curvature measures deviation from flatness.
The paper establishes arithmetic expressions as geometric objects with intrinsic invariants,
opening new avenues for exploring the interplay between computation and geometry.


## Building the PDF

Ensure that `pdflatex` and `bibtex` are available. Then run:

```bash
./build.sh
```

### Building with Docker

If a TeX environment is not installed locally, use Docker:

```bash
docker build -t aeg-paper .
docker run --rm -v $(pwd):/work aeg-paper
```
