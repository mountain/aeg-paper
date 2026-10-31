#!/usr/bin/env python3
"""Exact product-tunnel calibration for Paper I's handle propositions.

Direction: Mingli Yuan. Construction/checking/drafting: Codex (OpenAI).
Reuses V1 incidence and link routines; not an independently authored checker.
No AES realization or native Adva execution is claimed.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json

import verify_v1 as v1


def body_check(cubes, boundary_chi, body_chi, label):
    tets = v1.triangulate(cubes)
    faces = Counter(face for tet in tets for face in v1.simplex_faces(tet))
    v1.demand(all(n in (1, 2) for n in faces.values()), label + ':face-incidence')
    boundary_triangles = {face for face, n in faces.items() if n == 1}
    surface = v1.surface_check(boundary_triangles, boundary_chi, 0, label)
    boundary_vertices = set().union(*map(set, boundary_triangles))
    links = defaultdict(set)
    for tet in tets:
        for vertex in tet:
            links[vertex].add(tuple(v for v in tet if v != vertex))
    kinds = Counter()
    for vertex, link in sorted(links.items()):
        on_boundary = vertex in boundary_vertices
        v1.surface_check(link, 1 if on_boundary else 2, 1 if on_boundary else 0,
                         label + ':vertex-link:' + str(vertex))
        kinds['disk' if on_boundary else 'sphere'] += 1
    chain = {cell: 1 for cell in cubes}
    v1.demand(not v1.boundary(v1.boundary(chain)), label + ':boundary-square')
    counts = v1.cubical_counts(cubes)
    v1.demand(counts['chi'] == body_chi, label + ':body-chi')
    return {'cubical': counts, 'tetrahedra': len(tets),
            'boundary': surface, 'vertex_links': dict(sorted(kinds.items()))}


def filling(cubes, cycle):
    # For H_1 only the 2-skeleton is needed. This is a body computation,
    # despite the reused V1 helper's original side-surface field names.
    faces = {cell for cell in v1.closure(cubes) if cell[3].bit_count() == 2}
    result = v1.mod2_surface_filling(faces, cycle)
    return {'coefficient_field': 'F_2',
            'bounds_body_2chain': result['cycle_bounds_in_side_surface'],
            'body_first_betti_number': result['side_first_betti_number'],
            'boundary_matrix_rank': result['boundary_matrix_rank'],
            'augmented_rank': result['augmented_rank'],
            'face_boundary_positive_controls': len(faces)}


def integral(chain):
    """Exact integral of -y dz along oriented cubical edges."""
    total = Fraction(0)
    for cell, coefficient in chain.items():
        v1.demand(cell[3].bit_count() == 1, 'integral:not-edge')
        if cell[3] == 4:
            total -= coefficient * Fraction(cell[1])
    return total


def main():
    ball = set(v1.box(range(3), range(3), range(3)))
    pit = ball - {(0, 1, 1, 7)}
    tunnel = ball - {(x, 1, 1, 7) for x in range(3)}
    disk = {(1, y, z, 6): 1 for y in range(3) for z in range(3)}
    small = {(1, 1, 1, 6): 1}
    annulus = v1.add(disk, v1.scale(small, -1))
    outer, inner = v1.boundary(disk), v1.boundary(small)
    v1.demand(v1.boundary(annulus) == v1.add(outer, v1.scale(inner, -1)),
              'annulus:oriented-boundary')
    annulus_check = v1.surface_check(v1.triangulate(annulus), 0, 2, 'annulus')
    v1.demand(set(v1.closure(annulus)) <= v1.closure(tunnel), 'annulus:outside')
    v1.demand(set(outer) <= v1.closure(v1.boundary({c: 1 for c in tunnel})),
              'outer-circle:not-on-body-boundary')
    # I times a radial arc from the outer to the inner square is a disk.
    meridian_disk = {(x, 0, 1, 3): 1 for x in range(3)}
    v1.surface_check(v1.triangulate(meridian_disk), 1, 1, 'meridian-disk')
    meridian = v1.boundary(meridian_disk)
    v1.demand(set(meridian_disk) <= v1.closure(tunnel), 'meridian:outside')
    v1.demand(set(meridian) <= v1.closure(v1.boundary({c: 1 for c in tunnel})),
              'meridian:not-on-boundary')
    cases = {}
    for name, cubes, bchi, hchi in [('ball', ball, 2, 1),
                                    ('blind_pit', pit, 2, 1),
                                    ('through_tunnel', tunnel, 0, 0)]:
        cases[name] = body_check(cubes, bchi, hchi, name)
        cases[name]['outer_circle'] = filling(cubes, outer)
    v1.demand(cases['ball']['outer_circle']['bounds_body_2chain'], 'ball:filling')
    v1.demand(cases['blind_pit']['outer_circle']['bounds_body_2chain'], 'pit:filling')
    v1.demand(not cases['through_tunnel']['outer_circle']['bounds_body_2chain'],
              'tunnel:nonfilling')
    inner_result, meridian_result = filling(tunnel, inner), filling(tunnel, meridian)
    v1.demand(not inner_result['bounds_body_2chain'], 'tunnel:inner-nonfilling')
    v1.demand(meridian_result['bounds_body_2chain'], 'tunnel:meridian-filling')
    periods = {'outer': int(integral(outer)), 'inner': int(integral(inner)),
               'curvature_over_annulus': -sum(annulus.values())}
    v1.demand(periods['outer'] - periods['inner'] == periods['curvature_over_annulus'],
              'annulus:stokes-sign')
    controls = []

    def reject(name, action):
        try:
            action()
        except v1.Rejected:
            controls.append(name)
        else:
            raise RuntimeError('negative control accepted: ' + name)

    reject('blind_pit_claimed_to_add_handle',
           lambda: body_check(pit, 0, 0, 'bad-pit'))
    reject('through_tunnel_claimed_to_remain_ball',
           lambda: body_check(tunnel, 2, 1, 'bad-tunnel'))
    reject('old_disk_claimed_to_survive',
           lambda: v1.demand(set(disk) <= v1.closure(tunnel), 'missing-disk-face'))
    reject('outer_circle_claimed_to_bound',
           lambda: v1.demand(filling(tunnel, outer)['bounds_body_2chain'], 'nonfilling'))
    reject('wrong_inner_boundary_sign',
           lambda: v1.demand(v1.boundary(annulus) == v1.add(outer, inner), 'sign'))
    reject('zero_curvature_claimed_for_minus_y_dz',
           lambda: v1.demand(integral(outer) == integral(inner), 'curvature'))
    broken = dict(annulus)
    del broken[(1, 0, 0, 6)]
    reject('missing_annular_face',
           lambda: v1.demand(v1.boundary(broken) == v1.add(outer, v1.scale(inner, -1)),
                             'extra-boundary'))
    disconnected = {(0, 0, 0, 7), (1, 1, 1, 7)}
    reject('vertex_only_contact', lambda: body_check(disconnected, 2, 1, 'bad-link'))
    source = Path(__file__)
    report = {
        'schema': 1,
        'scope': 'Fixed product tunnel; same-author calibration, no AES or native Seal',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'v1_helper_sha256': hashlib.sha256(source.with_name('verify_v1.py').read_bytes()).hexdigest(),
        'construction': {'box': '[0,3]^3', 'blind_pit_removed_cube': [0, 1, 1],
                         'tunnel_removed_cubes': [[x, 1, 1] for x in range(3)],
                         'interface_plane': 'x=1', 'annulus_face_count': len(annulus)},
        'cases': cases, 'annulus': annulus_check, 'inner_circle': inner_result,
        'meridian_circle': meridian_result, 'minus_y_dz_periods': periods,
        'oriented_boundary_identity': 'boundary(A) = C - c',
        'negative_controls_rejected': controls,
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
