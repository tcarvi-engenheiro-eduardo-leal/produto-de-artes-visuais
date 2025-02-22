# Coding
- https://en.algorithmica.org/hpc/cpu-cache/aos-soa/
- Use:
    - Structure of arrays (SoA) is a layout separating elements of a record (or 'struct' in the C programming language) into one parallel array per field.[1] The motivation is easier manipulation with packed SIMD instructions in most instruction set architectures, since a single SIMD register can load homogeneous data, possibly transferred by a wide internal datapath (e.g. 128-bit). If only a specific part of the record is needed, only those parts need to be iterated over, allowing more data to fit onto a single cache line. The downside is requiring more cache ways when traversing data, and inefficient indexed addressing.
    - For example, to store N points in 3D space using a structure of arrays:
    ```python
    struct pointlist3D {
        float x[N];
        float y[N];
        float z[N];
    };
    struct pointlist3D points;
    float get_point_x(int i) { return points.x[i]; }
- 