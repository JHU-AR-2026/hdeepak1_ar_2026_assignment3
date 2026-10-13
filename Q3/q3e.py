import numpy as np

def project_point(point, W, H, n, f, fx, fy, ox, oy):
    # OpenGL projection matrix derived from camera intrinsics
    P = np.array([
        [2 * fx / W, 0, 1 - 2 * ox / W, 0],
        [0, 2 * fy / H, 1 - 2 * oy / H, 0],
        [0, 0, -(f + n) / (f - n), -(2 * f * n) / (f - n)],
        [0, 0, -1, 0]
    ], dtype=float)

    # Convert camera-space point to homogeneous coordinates
    Pc = np.array([
        point[0],
        point[1],
        point[2],
        1.0
    ])

    # Camera coordinates -> clip coordinates
    clip = P @ Pc

    # Perspective divide: clip -> NDC
    ndc = clip[:3] / clip[3]

    # NDC -> pixel coordinates
    u = 0.5 * (ndc[0] + 1.0) * W
    v = 0.5 * (ndc[1] + 1.0) * H

    return P, clip, ndc, (u, v)


# Values from Q3
W = 800
H = 600
n = 0.2
f = 20.0

fx = 800
fy = 800
ox = 400
oy = 400

point = (0.3, -0.15, -6.0)


P, clip, ndc, pixel = project_point(
    point,
    W, H,
    n, f,
    fx, fy,
    ox, oy
)


print("Projection matrix:")
print(P)

print("\nClip-space coordinates:")
print(clip)

print("\nNDC coordinates:")
print(ndc)

print("\nPixel coordinates:")
print(pixel)