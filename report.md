# pg_profile_lookup.ini Conflict Report

Commit: `f56312f86c7e4e10812ea9b83d2e394fd3cad9cf`
Rule: within the same platform, identical `(speed, cable_length)` must map to identical remaining tuple
Note: for symlinked files, each entry shows both original symlink link and resolved target link

## Conflicts by Platform

<details>
<summary><b>arista/x86_64-arista_7060x6_64pe_b</b> (3 conflicting speed/cable_length keys)</summary>

- speed=100000, cable_length=500m | 2 different lines | 2 total rows
  - `100000 500m 8636 0 1136396 0 3356` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-O128/pg_profile_lookup.ini:8` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-O128/pg_profile_lookup.ini#L8
  </details>

  - `100000 500m 8636 0 1136396 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-P32O64/pg_profile_lookup.ini:6` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-P32O64/pg_profile_lookup.ini#L6
  </details>


- speed=400000, cable_length=30m | 2 different lines | 2 total rows
  - `400000 30m 8636 0 425958 0 3356` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-O128/pg_profile_lookup.ini:4` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-O128/pg_profile_lookup.ini#L4
  </details>

  - `400000 30m 8636 0 425958 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-P32O64/pg_profile_lookup.ini:3` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-P32O64/pg_profile_lookup.ini#L3
  </details>


- speed=400000, cable_length=500m | 2 different lines | 2 total rows
  - `400000 500m 8636 0 1136396 0 3356` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-O128/pg_profile_lookup.ini:7` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-O128/pg_profile_lookup.ini#L7
  </details>

  - `400000 500m 8636 0 1136396 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-P32O64/pg_profile_lookup.ini:5` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7060x6_64pe_b/Arista-7060X6-64PE-B-P32O64/pg_profile_lookup.ini#L5
  </details>


</details>

<details>
<summary><b>arista/x86_64-arista_7260cx3_64</b> (6 conflicting speed/cable_length keys)</summary>

- speed=100000, cable_length=300m | 2 different lines | 6 total rows
  - `100000 300m 1248 1248 101088 0 2496` (5 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini:5` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L5
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini:5` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L5
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini:5` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L5
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini:5` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L5
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini:5` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L5
  </details>

  - `100000 300m 1248 1248 268736 0 2496` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini:8` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini#L8
  </details>


- speed=100000, cable_length=40m | 2 different lines | 6 total rows
  - `100000 40m 1248 1248 177632 0 2496` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini:6` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini#L6
  </details>

  - `100000 40m 1248 1248 59696 0 2496` (5 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini:4` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L4
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini:4` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L4
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini:4` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L4
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini:4` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L4
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini:4` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L4
  </details>


- speed=100000, cable_length=5m | 2 different lines | 6 total rows
  - `100000 5m 1248 1248 54080 0 2496` (5 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini:3` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L3
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini:3` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L3
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini:3` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L3
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini:3` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L3
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini:3` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L3
  </details>

  - `100000 5m 1248 1248 96928 0 2496` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini:4` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini#L4
  </details>


- speed=50000, cable_length=300m | 2 different lines | 6 total rows
  - `50000 300m 1248 1248 101088 0 2496` (5 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini:8` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L8
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini:8` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L8
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini:8` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L8
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini:8` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L8
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini:8` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L8
  </details>

  - `50000 300m 1248 1248 141856 0 2496` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini:7` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini#L7
  </details>


- speed=50000, cable_length=40m | 2 different lines | 6 total rows
  - `50000 40m 1248 1248 59696 0 2496` (5 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini:7` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L7
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini:7` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L7
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini:7` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L7
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini:7` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L7
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini:7` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L7
  </details>

  - `50000 40m 1248 1248 96096 0 2496` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini:5` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini#L5
  </details>


- speed=50000, cable_length=5m | 2 different lines | 6 total rows
  - `50000 5m 1248 1248 54080 0 2496` (5 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini:6` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L6
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini:6` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L6
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini:6` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D108C8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L6
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini:6` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D92C16/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L6
  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini:6` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-Q64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/common/profiles/th2/7260/BALANCED/pg_profile_lookup.ini#L6
  </details>

  - `50000 5m 1248 1248 56160 0 2496` (1 rows)
  <details>
  <summary>files</summary>

  - `device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini:3` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/arista/x86_64-arista_7260cx3_64/Arista-7260CX3-D96C16/pg_profile_lookup.ini#L3
  </details>


</details>

<details>
<summary><b>marvell/x86_64-marvell_dbmvtx9180-r0</b> (24 conflicting speed/cable_length keys)</summary>

- speed=100000, cable_length=100m | 2 different lines | 6 total rows
  - `100000 100m 1518 0 46496 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L17
  </details>

  - `100000 100m 1518 0 52224 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L29
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L29
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L29
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L29
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L29
  </details>


- speed=100000, cable_length=300m | 2 different lines | 6 total rows
  - `100000 300m 1518 0 72384 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L23
  </details>

  - `100000 300m 1518 0 77824 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L35
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L35
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L35
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L35
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L35
  </details>


- speed=100000, cable_length=40m | 2 different lines | 6 total rows
  - `100000 40m 1518 0 38816 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:11` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L11
  </details>

  - `100000 40m 1518 0 44544 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L23
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L23
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L23
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L23
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L23
  </details>


- speed=100000, cable_length=5m | 2 different lines | 6 total rows
  - `100000 5m 1518 0 34624 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:5` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L5
  </details>

  - `100000 5m 1518 0 40064 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L17
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L17
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L17
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L17
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L17
  </details>


- speed=200000, cable_length=100m | 2 different lines | 6 total rows
  - `200000 100m 1518 0 87168 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:18` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L18
  </details>

  - `200000 100m 1518 0 94464 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L30
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L30
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L30
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L30
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L30
  </details>


- speed=200000, cable_length=300m | 2 different lines | 6 total rows
  - `200000 300m 1518 0 138112 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L24
  </details>

  - `200000 300m 1518 0 145536 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L36
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L36
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L36
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L36
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L36
  </details>


- speed=200000, cable_length=40m | 2 different lines | 6 total rows
  - `200000 40m 1518 0 71904 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:12` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L12
  </details>

  - `200000 40m 1518 0 78848 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L24
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L24
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L24
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L24
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L24
  </details>


- speed=200000, cable_length=5m | 2 different lines | 6 total rows
  - `200000 5m 1518 0 62368 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:6` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L6
  </details>

  - `200000 5m 1518 0 70272 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:18` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L18
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:18` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L18
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:18` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L18
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:18` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L18
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:18` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L18
  </details>


- speed=25000, cable_length=100m | 2 different lines | 6 total rows
  - `25000 100m 1518 0 18848 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L15
  </details>

  - `25000 100m 1518 0 22016 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L27
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L27
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L27
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L27
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L27
  </details>


- speed=25000, cable_length=300m | 2 different lines | 6 total rows
  - `25000 300m 1518 0 25184 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L21
  </details>

  - `25000 300m 1518 0 29696 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L33
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L33
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L33
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L33
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L33
  </details>


- speed=25000, cable_length=40m | 2 different lines | 6 total rows
  - `25000 40m 1518 0 16928 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:9` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L9
  </details>

  - `25000 40m 1518 0 19840 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L21
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L21
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L21
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L21
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L21
  </details>


- speed=25000, cable_length=5m | 2 different lines | 6 total rows
  - `25000 5m 1518 0 15680 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:3` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L3
  </details>

  - `25000 5m 1518 0 18304 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L15
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L15
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L15
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L15
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L15
  </details>


- speed=400000, cable_length=100m | 2 different lines | 6 total rows
  - `400000 100m 1518 0 166688 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L19
  </details>

  - `400000 100m 1518 0 178560 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L31
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L31
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L31
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L31
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L31
  </details>


- speed=400000, cable_length=300m | 2 different lines | 6 total rows
  - `400000 300m 1518 0 268640 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L25
  </details>

  - `400000 300m 1518 0 280960 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L37
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L37
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L37
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L37
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L37
  </details>


- speed=400000, cable_length=40m | 2 different lines | 6 total rows
  - `400000 40m 1518 0 135520 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:13` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L13
  </details>

  - `400000 40m 1518 0 147072 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L25
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L25
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L25
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L25
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L25
  </details>


- speed=400000, cable_length=5m | 2 different lines | 6 total rows
  - `400000 5m 1518 0 117536 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:7` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L7
  </details>

  - `400000 5m 1518 0 129920 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L19
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L19
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L19
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L19
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L19
  </details>


- speed=50000, cable_length=100m | 2 different lines | 6 total rows
  - `50000 100m 1518 0 27264 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L16
  </details>

  - `50000 100m 1518 0 30080 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L28
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L28
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L28
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L28
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L28
  </details>


- speed=50000, cable_length=300m | 2 different lines | 6 total rows
  - `50000 300m 1518 0 40128 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L22
  </details>

  - `50000 300m 1518 0 43008 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L34
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L34
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L34
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L34
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L34
  </details>


- speed=50000, cable_length=40m | 2 different lines | 6 total rows
  - `50000 40m 1518 0 23392 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:10` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L10
  </details>

  - `50000 40m 1518 0 26240 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L22
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L22
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L22
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L22
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L22
  </details>


- speed=50000, cable_length=5m | 2 different lines | 6 total rows
  - `50000 5m 1518 0 21248 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:4` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L4
  </details>

  - `50000 5m 1518 0 24064 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L16
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L16
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L16
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L16
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L16
  </details>


- speed=800000, cable_length=100m | 2 different lines | 6 total rows
  - `800000 100m 1518 0 236688 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L20
  </details>

  - `800000 100m 1518 0 345984 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L32
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L32
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L32
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L32
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L32
  </details>


- speed=800000, cable_length=300m | 2 different lines | 6 total rows
  - `800000 300m 1518 0 468640 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L26
  </details>

  - `800000 300m 1518 0 550528 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L38
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L38
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L38
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L38
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L38
  </details>


- speed=800000, cable_length=40m | 2 different lines | 6 total rows
  - `800000 40m 1518 0 205520 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:14` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L14
  </details>

  - `800000 40m 1518 0 285312 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L26
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L26
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L26
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L26
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L26
  </details>


- speed=800000, cable_length=5m | 2 different lines | 6 total rows
  - `800000 5m 1518 0 197536 1 9408` (1 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini:8` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64x100G/pg_profile_lookup.ini#L8
  </details>

  - `800000 5m 1518 0 247424 1 13824` (5 rows)
  <details>
  <summary>files</summary>

  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G/pg_profile_lookup.ini#L20
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_128x400G_lab/pg_profile_lookup.ini#L20
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_256x200G/pg_profile_lookup.ini#L20
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_512x100G/pg_profile_lookup.ini#L20
  - `device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/marvell/x86_64-marvell_dbmvtx9180-r0/dbmvtx9180_64osfp_64x800G/pg_profile_lookup.ini#L20
  </details>


</details>

<details>
<summary><b>mellanox/x86_64-mlnx_msn2700-r0</b> (15 conflicting speed/cable_length keys)</summary>

- speed=10000, cable_length=300m | 2 different lines | 6 total rows
  - `10000 300m 19456 19456 27648 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L29
  </details>

  - `10000 300m 56320 19456 36864 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L29
  </details>


- speed=10000, cable_length=40m | 2 different lines | 6 total rows
  - `10000 40m 19456 19456 22528 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L24
  </details>

  - `10000 40m 49152 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L24
  </details>


- speed=10000, cable_length=5m | 2 different lines | 6 total rows
  - `10000 5m 19456 19456 22528 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L19
  </details>

  - `10000 5m 49152 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L19
  </details>


- speed=100000, cable_length=300m | 2 different lines | 6 total rows
  - `100000 300m 123904 19456 104448 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L33
  </details>

  - `100000 300m 19456 19456 78848 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L33
  </details>


- speed=100000, cable_length=40m | 2 different lines | 6 total rows
  - `100000 40m 19456 19456 29696 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L28
  </details>

  - `100000 40m 58368 19456 38912 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L28
  </details>


- speed=100000, cable_length=5m | 2 different lines | 6 total rows
  - `100000 5m 19456 19456 23552 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L23
  </details>

  - `100000 5m 50176 19456 30720 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L23
  </details>


- speed=25000, cable_length=300m | 2 different lines | 6 total rows
  - `25000 300m 19456 19456 36864 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L30
  </details>

  - `25000 300m 67584 19456 48128 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L30
  </details>


- speed=25000, cable_length=40m | 2 different lines | 6 total rows
  - `25000 40m 19456 19456 24576 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L25
  </details>

  - `25000 40m 51200 19456 31744 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L25
  </details>


- speed=25000, cable_length=5m | 2 different lines | 6 total rows
  - `25000 5m 19456 19456 22528 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L20
  </details>

  - `25000 5m 49152 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L20
  </details>


- speed=40000, cable_length=300m | 2 different lines | 6 total rows
  - `40000 300m 19456 19456 45056 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L31
  </details>

  - `40000 300m 78848 19456 59392 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L31
  </details>


- speed=40000, cable_length=40m | 2 different lines | 6 total rows
  - `40000 40m 19456 19456 25600 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L26
  </details>

  - `40000 40m 52224 19456 32768 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L26
  </details>


- speed=40000, cable_length=5m | 2 different lines | 6 total rows
  - `40000 5m 19456 19456 22528 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L21
  </details>

  - `40000 5m 49152 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L21
  </details>


- speed=50000, cable_length=300m | 2 different lines | 6 total rows
  - `50000 300m 19456 19456 50176 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L32
  </details>

  - `50000 300m 86016 19456 66560 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L32
  </details>


- speed=50000, cable_length=40m | 2 different lines | 6 total rows
  - `50000 40m 19456 19456 25600 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L27
  </details>

  - `50000 40m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L27
  </details>


- speed=50000, cable_length=5m | 2 different lines | 6 total rows
  - `50000 5m 19456 19456 22528 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-C28D8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D44C10/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D40C8S8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/Mellanox-SN2700-D48C8/pg_profile_lookup.ini#L22
  </details>

  - `50000 5m 49152 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn2700-r0/ACS-MSN2700/pg_profile_lookup.ini#L22
  </details>


</details>

<details>
<summary><b>mellanox/x86_64-mlnx_msn3800-r0</b> (15 conflicting speed/cable_length keys)</summary>

- speed=10000, cable_length=300m | 2 different lines | 7 total rows
  - `10000 300m 19456 19456 31744 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L29
  </details>

  - `10000 300m 63488 19456 44032 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L29
  </details>


- speed=10000, cable_length=40m | 2 different lines | 7 total rows
  - `10000 40m 19456 19456 26624 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L24
  </details>

  - `10000 40m 55296 19456 35840 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L24
  </details>


- speed=10000, cable_length=5m | 2 different lines | 7 total rows
  - `10000 5m 19456 19456 25600 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L19
  </details>

  - `10000 5m 54272 19456 34816 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L19
  </details>


- speed=100000, cable_length=300m | 2 different lines | 7 total rows
  - `100000 300m 159744 19456 140288 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L33
  </details>

  - `100000 300m 19456 19456 102400 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L33
  </details>


- speed=100000, cable_length=40m | 2 different lines | 7 total rows
  - `100000 40m 19456 19456 48128 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L28
  </details>

  - `100000 40m 86016 19456 66560 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L28
  </details>


- speed=100000, cable_length=5m | 2 different lines | 7 total rows
  - `100000 5m 19456 19456 40960 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L23
  </details>

  - `100000 5m 75776 19456 56320 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L23
  </details>


- speed=25000, cable_length=300m | 2 different lines | 7 total rows
  - `25000 300m 19456 19456 44032 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L30
  </details>

  - `25000 300m 78848 19456 59392 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L30
  </details>


- speed=25000, cable_length=40m | 2 different lines | 7 total rows
  - `25000 40m 19456 19456 30720 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L25
  </details>

  - `25000 40m 60416 19456 40960 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L25
  </details>


- speed=25000, cable_length=5m | 2 different lines | 7 total rows
  - `25000 5m 19456 19456 28672 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L20
  </details>

  - `25000 5m 58368 19456 38912 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L20
  </details>


- speed=40000, cable_length=300m | 2 different lines | 7 total rows
  - `40000 300m 19456 19456 55296 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L31
  </details>

  - `40000 300m 95232 19456 75776 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L31
  </details>


- speed=40000, cable_length=40m | 2 different lines | 7 total rows
  - `40000 40m 19456 19456 33792 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L26
  </details>

  - `40000 40m 65536 19456 46080 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L26
  </details>


- speed=40000, cable_length=5m | 2 different lines | 7 total rows
  - `40000 5m 19456 19456 30720 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L21
  </details>

  - `40000 5m 61440 19456 41984 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L21
  </details>


- speed=50000, cable_length=300m | 2 different lines | 7 total rows
  - `50000 300m 106496 19456 87040 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L32
  </details>

  - `50000 300m 19456 19456 63488 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L32
  </details>


- speed=50000, cable_length=40m | 2 different lines | 7 total rows
  - `50000 40m 19456 19456 36864 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L27
  </details>

  - `50000 40m 69632 19456 50176 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L27
  </details>


- speed=50000, cable_length=5m | 2 different lines | 7 total rows
  - `50000 5m 19456 19456 32768 0` (6 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D24C52/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C49S1/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D28C50/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/Mellanox-SN3800-D112C8/pg_profile_lookup.ini#L22
  </details>

  - `50000 5m 64512 19456 45056 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn3800-r0/ACS-MSN3800/pg_profile_lookup.ini#L22
  </details>


</details>

<details>
<summary><b>mellanox/x86_64-mlnx_msn4600c-r0</b> (20 conflicting speed/cable_length keys)</summary>

- speed=10000, cable_length=2000m | 2 different lines | 5 total rows
  - `10000 2000m 19456 19456 32768 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L34
  </details>

  - `10000 2000m 19456 19456 47104 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L40
  </details>


- speed=10000, cable_length=300m | 3 different lines | 6 total rows
  - `10000 300m 19456 19456 22528 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L35
  </details>

  - `10000 300m 19456 19456 30720 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L29
  </details>

  - `10000 300m 60416 19456 40960 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L33
  </details>


- speed=10000, cable_length=40m | 3 different lines | 6 total rows
  - `10000 40m 19456 19456 18432 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L30
  </details>

  - `10000 40m 19456 19456 25600 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L24
  </details>

  - `10000 40m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L26
  </details>


- speed=10000, cable_length=5m | 3 different lines | 6 total rows
  - `10000 5m 19456 19456 18432 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L25
  </details>

  - `10000 5m 19456 19456 24576 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L19
  </details>

  - `10000 5m 52224 19456 32768 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L19
  </details>


- speed=100000, cable_length=2000m | 2 different lines | 5 total rows
  - `100000 2000m 19456 19456 234496 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L38
  </details>

  - `100000 2000m 19456 19456 331776 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:44` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L44
  </details>


- speed=100000, cable_length=300m | 3 different lines | 6 total rows
  - `100000 300m 137216 19456 117760 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L37
  </details>

  - `100000 300m 19456 19456 120832 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L33
  </details>

  - `100000 300m 19456 19456 84992 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L39
  </details>


- speed=100000, cable_length=40m | 3 different lines | 6 total rows
  - `100000 40m 19456 19456 48128 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L34
  </details>

  - `100000 40m 19456 19456 66560 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L28
  </details>

  - `100000 40m 63488 19456 44032 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L30
  </details>


- speed=100000, cable_length=5m | 3 different lines | 6 total rows
  - `100000 5m 19456 19456 43008 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L29
  </details>

  - `100000 5m 19456 19456 59392 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L23
  </details>

  - `100000 5m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L23
  </details>


- speed=25000, cable_length=2000m | 2 different lines | 5 total rows
  - `25000 2000m 19456 19456 64512 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L35
  </details>

  - `25000 2000m 19456 19456 91136 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L41
  </details>


- speed=25000, cable_length=300m | 3 different lines | 6 total rows
  - `25000 300m 19456 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L36
  </details>

  - `25000 300m 19456 19456 41984 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L30
  </details>

  - `25000 300m 73728 19456 54272 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L34
  </details>


- speed=25000, cable_length=40m | 3 different lines | 6 total rows
  - `25000 40m 19456 19456 20480 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L31
  </details>

  - `25000 40m 19456 19456 28672 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L25
  </details>

  - `25000 40m 55296 19456 35840 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L27
  </details>


- speed=25000, cable_length=5m | 3 different lines | 6 total rows
  - `25000 5m 19456 19456 19456 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L26
  </details>

  - `25000 5m 19456 19456 26624 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L20
  </details>

  - `25000 5m 52224 19456 32768 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L20
  </details>


- speed=40000, cable_length=2000m | 2 different lines | 5 total rows
  - `40000 2000m 19456 19456 137216 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L42
  </details>

  - `40000 2000m 19456 19456 97280 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L36
  </details>


- speed=40000, cable_length=300m | 3 different lines | 6 total rows
  - `40000 300m 19456 19456 38912 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L37
  </details>

  - `40000 300m 19456 19456 54272 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L31
  </details>

  - `40000 300m 86016 19456 66560 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L35
  </details>


- speed=40000, cable_length=40m | 3 different lines | 6 total rows
  - `40000 40m 19456 19456 23552 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L32
  </details>

  - `40000 40m 19456 19456 33792 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L26
  </details>

  - `40000 40m 57344 19456 37888 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L28
  </details>


- speed=40000, cable_length=5m | 3 different lines | 6 total rows
  - `40000 5m 19456 19456 21504 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L27
  </details>

  - `40000 5m 19456 19456 30720 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L21
  </details>

  - `40000 5m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L21
  </details>


- speed=50000, cable_length=2000m | 2 different lines | 5 total rows
  - `50000 2000m 19456 19456 119808 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L37
  </details>

  - `50000 2000m 19456 19456 168960 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:43` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L43
  </details>


- speed=50000, cable_length=300m | 3 different lines | 6 total rows
  - `50000 300m 19456 19456 45056 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L38
  </details>

  - `50000 300m 19456 19456 63488 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L32
  </details>

  - `50000 300m 95232 19456 75776 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L36
  </details>


- speed=50000, cable_length=40m | 3 different lines | 6 total rows
  - `50000 40m 19456 19456 26624 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L33
  </details>

  - `50000 40m 19456 19456 36864 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L27
  </details>

  - `50000 40m 58368 19456 38912 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L29
  </details>


- speed=50000, cable_length=5m | 3 different lines | 6 total rows
  - `50000 5m 19456 19456 24576 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D24C52/pg_profile_lookup.ini#L28
  </details>

  - `50000 5m 19456 19456 33792 0` (4 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-C64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D100C12S2/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D48C40/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/Mellanox-SN4600C-D112C8/pg_profile_lookup.ini#L22
  </details>

  - `50000 5m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4600c-r0/ACS-MSN4600C/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L22
  </details>


</details>

<details>
<summary><b>mellanox/x86_64-mlnx_msn4700-r0</b> (32 conflicting speed/cable_length keys)</summary>

- speed=10000, cable_length=1500m | 2 different lines | 8 total rows
  - `10000 1500m 19456 19456 35840 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L40
  </details>

  - `10000 1500m 19456 19456 55296 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L40
  </details>


- speed=10000, cable_length=2000m | 2 different lines | 8 total rows
  - `10000 2000m 19456 19456 32768 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:45` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L45
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:45` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L45
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:45` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L45
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:45` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L45
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:45` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L45
  </details>

  - `10000 2000m 19456 19456 41984 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:47` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L47
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:47` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L47
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:47` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L47
  </details>


- speed=10000, cable_length=300m | 3 different lines | 9 total rows
  - `10000 300m 19456 19456 19456 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L33
  </details>

  - `10000 300m 19456 19456 30720 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L33
  </details>

  - `10000 300m 60416 19456 40960 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L33
  </details>


- speed=10000, cable_length=40m | 3 different lines | 9 total rows
  - `10000 40m 19456 19456 16384 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L26
  </details>

  - `10000 40m 19456 19456 25600 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L26
  </details>

  - `10000 40m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L26
  </details>


- speed=10000, cable_length=5m | 3 different lines | 9 total rows
  - `10000 5m 19456 19456 16384 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L19
  </details>

  - `10000 5m 19456 19456 24576 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L19
  </details>

  - `10000 5m 52224 19456 32768 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L19
  </details>


- speed=100000, cable_length=1500m | 2 different lines | 8 total rows
  - `100000 1500m 19456 19456 230400 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:44` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L44
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:44` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L44
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:44` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L44
  </details>

  - `100000 1500m 19456 19456 366592 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:44` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L44
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:44` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L44
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:44` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L44
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:44` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L44
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:44` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L44
  </details>


- speed=100000, cable_length=2000m | 2 different lines | 8 total rows
  - `100000 2000m 19456 19456 234496 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:49` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L49
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:49` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L49
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:49` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L49
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:49` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L49
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:49` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L49
  </details>

  - `100000 2000m 19456 19456 293888 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:51` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L51
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:51` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L51
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:51` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L51
  </details>


- speed=100000, cable_length=300m | 3 different lines | 9 total rows
  - `100000 300m 137216 19456 117760 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L37
  </details>

  - `100000 300m 19456 19456 120832 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L37
  </details>

  - `100000 300m 19456 19456 75776 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L37
  </details>


- speed=100000, cable_length=40m | 3 different lines | 9 total rows
  - `100000 40m 19456 19456 43008 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L30
  </details>

  - `100000 40m 19456 19456 66560 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L30
  </details>

  - `100000 40m 63488 19456 44032 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L30
  </details>


- speed=100000, cable_length=5m | 3 different lines | 9 total rows
  - `100000 5m 19456 19456 37888 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L23
  </details>

  - `100000 5m 19456 19456 59392 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L23
  </details>

  - `100000 5m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L23
  </details>


- speed=200000, cable_length=300m | 3 different lines | 9 total rows
  - `200000 300m 19456 19456 118784 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L38
  </details>

  - `200000 300m 19456 19456 188416 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L38
  </details>

  - `200000 300m 223232 19456 203776 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L38
  </details>


- speed=200000, cable_length=40m | 3 different lines | 9 total rows
  - `200000 40m 19456 19456 51200 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L31
  </details>

  - `200000 40m 19456 19456 80896 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L31
  </details>

  - `200000 40m 74752 19456 55296 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L31
  </details>


- speed=200000, cable_length=5m | 3 different lines | 9 total rows
  - `200000 5m 19456 19456 43008 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L24
  </details>

  - `200000 5m 19456 19456 66560 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L24
  </details>

  - `200000 5m 55296 19456 35840 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L24
  </details>


- speed=25000, cable_length=1500m | 2 different lines | 8 total rows
  - `25000 1500m 19456 19456 103424 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L41
  </details>

  - `25000 1500m 19456 19456 65536 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L41
  </details>


- speed=25000, cable_length=2000m | 2 different lines | 8 total rows
  - `25000 2000m 19456 19456 64512 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:46` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L46
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:46` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L46
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:46` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L46
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:46` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L46
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:46` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L46
  </details>

  - `25000 2000m 19456 19456 80896 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:48` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L48
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:48` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L48
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:48` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L48
  </details>


- speed=25000, cable_length=300m | 3 different lines | 9 total rows
  - `25000 300m 19456 19456 26624 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L34
  </details>

  - `25000 300m 19456 19456 41984 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L34
  </details>

  - `25000 300m 73728 19456 54272 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L34
  </details>


- speed=25000, cable_length=40m | 3 different lines | 9 total rows
  - `25000 40m 19456 19456 18432 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L27
  </details>

  - `25000 40m 19456 19456 28672 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L27
  </details>

  - `25000 40m 55296 19456 35840 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L27
  </details>


- speed=25000, cable_length=5m | 3 different lines | 9 total rows
  - `25000 5m 19456 19456 17408 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L20
  </details>

  - `25000 5m 19456 19456 26624 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L20
  </details>

  - `25000 5m 52224 19456 32768 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L20
  </details>


- speed=40000, cable_length=1500m | 2 different lines | 8 total rows
  - `40000 1500m 19456 19456 153600 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L42
  </details>

  - `40000 1500m 19456 19456 96256 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L42
  </details>


- speed=40000, cable_length=2000m | 2 different lines | 8 total rows
  - `40000 2000m 19456 19456 121856 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:49` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L49
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:49` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L49
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:49` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L49
  </details>

  - `40000 2000m 19456 19456 97280 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:47` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L47
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:47` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L47
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:47` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L47
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:47` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L47
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:47` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L47
  </details>


- speed=40000, cable_length=300m | 3 different lines | 9 total rows
  - `40000 300m 19456 19456 34816 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L35
  </details>

  - `40000 300m 19456 19456 54272 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L35
  </details>

  - `40000 300m 86016 19456 66560 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L35
  </details>


- speed=40000, cable_length=40m | 3 different lines | 9 total rows
  - `40000 40m 19456 19456 21504 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L28
  </details>

  - `40000 40m 19456 19456 33792 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L28
  </details>

  - `40000 40m 57344 19456 37888 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L28
  </details>


- speed=40000, cable_length=5m | 3 different lines | 9 total rows
  - `40000 5m 19456 19456 19456 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L21
  </details>

  - `40000 5m 19456 19456 30720 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L21
  </details>

  - `40000 5m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L21
  </details>


- speed=400000, cable_length=2000m | 2 different lines | 8 total rows
  - `400000 2000m 38912 38912 555008 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:53` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L53
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:53` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L53
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:53` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L53
  </details>

  - `400000 2000m 38912 38912 876544 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:50` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L50
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:50` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L50
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:50` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L50
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:50` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L50
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:50` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L50
  </details>


- speed=400000, cable_length=300m | 3 different lines | 9 total rows
  - `400000 300m 38912 38912 225280 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L39
  </details>

  - `400000 300m 38912 38912 358400 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L39
  </details>

  - `400000 300m 420864 37888 373760 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L39
  </details>


- speed=400000, cable_length=40m | 3 different lines | 9 total rows
  - `400000 40m 124928 37888 77824 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L32
  </details>

  - `400000 40m 38912 38912 144384 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L32
  </details>

  - `400000 40m 38912 38912 91136 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L32
  </details>


- speed=400000, cable_length=5m | 3 different lines | 9 total rows
  - `400000 5m 38912 38912 115712 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L25
  </details>

  - `400000 5m 38912 38912 73728 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L25
  </details>

  - `400000 5m 86016 37888 38912 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L25
  </details>


- speed=50000, cable_length=1500m | 2 different lines | 8 total rows
  - `50000 1500m 19456 19456 117760 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:43` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L43
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:43` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L43
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:43` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L43
  </details>

  - `50000 1500m 19456 19456 187392 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:43` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L43
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:43` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L43
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:43` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L43
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:43` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L43
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:43` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L43
  </details>


- speed=50000, cable_length=2000m | 2 different lines | 8 total rows
  - `50000 2000m 19456 19456 119808 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:48` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L48
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:48` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L48
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:48` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L48
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:48` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L48
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:48` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L48
  </details>

  - `50000 2000m 19456 19456 149504 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:50` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L50
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:50` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L50
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:50` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L50
  </details>


- speed=50000, cable_length=300m | 3 different lines | 9 total rows
  - `50000 300m 19456 19456 40960 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L36
  </details>

  - `50000 300m 19456 19456 63488 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L36
  </details>

  - `50000 300m 95232 19456 75776 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L36
  </details>


- speed=50000, cable_length=40m | 3 different lines | 9 total rows
  - `50000 40m 19456 19456 23552 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L29
  </details>

  - `50000 40m 19456 19456 36864 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L29
  </details>

  - `50000 40m 58368 19456 38912 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L29
  </details>


- speed=50000, cable_length=5m | 3 different lines | 9 total rows
  - `50000 5m 19456 19456 21504 0` (3 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V64/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8C48/pg_profile_lookup.ini#L22
  </details>

  - `50000 5m 19456 19456 33792 0` (5 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-A96C8V8/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O28/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-O8V48/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-V48C32/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/Mellanox-SN4700-C128/pg_profile_lookup.ini#L22
  </details>

  - `50000 5m 53248 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-mlnx_msn4700-r0/ACS-MSN4700/pg_profile_lookup.ini#L22
  </details>


</details>

<details>
<summary><b>mellanox/x86_64-nvidia_sn5600-r0</b> (32 conflicting speed/cable_length keys)</summary>

- speed=10000, cable_length=250m | 2 different lines | 2 total rows
  - `10000 250m 19456 19456 14336 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L36
  </details>

  - `10000 250m 43008 19456 23552 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L36
  </details>


- speed=10000, cable_length=300m | 3 different lines | 4 total rows
  - `10000 300m 19456 19456 23552 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:44` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L44
  </details>

  - `10000 300m 19456 19456 40960 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L35
  </details>

  - `10000 300m 75776 19456 56320 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:35` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L35
  </details>


- speed=10000, cable_length=40m | 3 different lines | 5 total rows
  - `10000 40m 19456 19456 20480 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L28
  </details>

  - `10000 40m 19456 19456 34816 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L27
  </details>

  - `10000 40m 65536 19456 46080 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:27` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L27
  </details>


- speed=10000, cable_length=5m | 3 different lines | 5 total rows
  - `10000 5m 19456 19456 20480 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L20
  </details>

  - `10000 5m 19456 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L19
  </details>

  - `10000 5m 64512 19456 45056 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:19` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L19
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:19` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L19
  </details>


- speed=100000, cable_length=250m | 2 different lines | 2 total rows
  - `100000 250m 19456 19456 68608 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L40
  </details>

  - `100000 250m 19456 19456 76800 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L40
  </details>


- speed=100000, cable_length=300m | 3 different lines | 4 total rows
  - `100000 300m 19456 19456 153600 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L39
  </details>

  - `100000 300m 19456 19456 83968 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:48` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L48
  </details>

  - `100000 300m 244736 19456 225280 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L39
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:39` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L39
  </details>


- speed=100000, cable_length=40m | 3 different lines | 5 total rows
  - `100000 40m 146432 19456 126976 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:31` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L31
  </details>

  - `100000 40m 19456 19456 49152 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L32
  </details>

  - `100000 40m 19456 19456 88064 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L31
  </details>


- speed=100000, cable_length=5m | 3 different lines | 5 total rows
  - `100000 5m 133120 19456 113664 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:23` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L23
  </details>

  - `100000 5m 19456 19456 44032 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L24
  </details>

  - `100000 5m 19456 19456 79872 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L23
  </details>


- speed=200000, cable_length=250m | 2 different lines | 2 total rows
  - `200000 250m 19456 19456 107520 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L41
  </details>

  - `200000 250m 19456 19456 116736 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L41
  </details>


- speed=200000, cable_length=300m | 3 different lines | 4 total rows
  - `200000 300m 19456 19456 130048 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:49` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L49
  </details>

  - `200000 300m 19456 19456 240640 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L40
  </details>

  - `200000 300m 374784 19456 355328 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:40` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L40
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:40` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L40
  </details>


- speed=200000, cable_length=40m | 3 different lines | 5 total rows
  - `200000 40m 177152 19456 157696 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L32
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:32` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L32
  </details>

  - `200000 40m 19456 19456 108544 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:32` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L32
  </details>

  - `200000 40m 19456 19456 60416 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L33
  </details>


- speed=200000, cable_length=5m | 3 different lines | 5 total rows
  - `200000 5m 150528 19456 131072 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L24
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:24` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L24
  </details>

  - `200000 5m 19456 19456 50176 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L25
  </details>

  - `200000 5m 19456 19456 91136 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:24` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L24
  </details>


- speed=25000, cable_length=250m | 2 different lines | 2 total rows
  - `25000 250m 19456 19456 20480 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L37
  </details>

  - `25000 250m 19456 19456 29696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L37
  </details>


- speed=25000, cable_length=300m | 3 different lines | 4 total rows
  - `25000 300m 19456 19456 30720 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:45` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L45
  </details>

  - `25000 300m 19456 19456 54272 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L36
  </details>

  - `25000 300m 96256 19456 76800 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:36` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L36
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:36` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L36
  </details>


- speed=25000, cable_length=40m | 3 different lines | 5 total rows
  - `25000 40m 19456 19456 22528 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L29
  </details>

  - `25000 40m 19456 19456 37888 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L28
  </details>

  - `25000 40m 71680 19456 52224 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:28` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L28
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:28` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L28
  </details>


- speed=25000, cable_length=5m | 3 different lines | 5 total rows
  - `25000 5m 19456 19456 21504 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L21
  </details>

  - `25000 5m 19456 19456 35840 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L20
  </details>

  - `25000 5m 67584 19456 48128 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L20
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:20` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L20
  </details>


- speed=40000, cable_length=250m | 2 different lines | 2 total rows
  - `40000 250m 19456 19456 28672 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L38
  </details>

  - `40000 250m 19456 19456 36864 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L38
  </details>


- speed=40000, cable_length=300m | 3 different lines | 4 total rows
  - `40000 300m 120832 19456 101376 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L37
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:37` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L37
  </details>

  - `40000 300m 19456 19456 39936 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:46` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L46
  </details>

  - `40000 300m 19456 19456 71680 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:37` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L37
  </details>


- speed=40000, cable_length=40m | 3 different lines | 5 total rows
  - `40000 40m 19456 19456 25600 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L30
  </details>

  - `40000 40m 19456 19456 45056 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L29
  </details>

  - `40000 40m 81920 19456 62464 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:29` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L29
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:29` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L29
  </details>


- speed=40000, cable_length=5m | 3 different lines | 5 total rows
  - `40000 5m 19456 19456 24576 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L22
  </details>

  - `40000 5m 19456 19456 41984 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L21
  </details>

  - `40000 5m 75776 19456 57344 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:21` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L21
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:21` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L21
  </details>


- speed=400000, cable_length=250m | 2 different lines | 2 total rows
  - `400000 250m 19456 19456 208896 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L42
  </details>

  - `400000 250m 19456 19456 217088 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L42
  </details>


- speed=400000, cable_length=300m | 3 different lines | 4 total rows
  - `400000 300m 19456 19456 243712 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:50` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L50
  </details>

  - `400000 300m 19456 19456 455680 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L41
  </details>

  - `400000 300m 697344 19456 677888 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:41` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L41
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:41` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L41
  </details>


- speed=400000, cable_length=40m | 3 different lines | 5 total rows
  - `400000 40m 19456 19456 104448 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L34
  </details>

  - `400000 40m 19456 19456 192512 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L33
  </details>

  - `400000 40m 303104 19456 283648 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:33` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L33
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:33` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L33
  </details>


- speed=400000, cable_length=5m | 3 different lines | 5 total rows
  - `400000 5m 19456 19456 157696 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L25
  </details>

  - `400000 5m 19456 19456 86016 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L26
  </details>

  - `400000 5m 250880 19456 231424 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:25` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L25
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:25` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L25
  </details>


- speed=50000, cable_length=250m | 2 different lines | 2 total rows
  - `50000 250m 19456 19456 33792 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L39
  </details>

  - `50000 250m 19456 19456 43008 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:39` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L39
  </details>


- speed=50000, cable_length=300m | 3 different lines | 4 total rows
  - `50000 300m 138240 19456 118784 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L38
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:38` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L38
  </details>

  - `50000 300m 19456 19456 46080 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:47` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L47
  </details>

  - `50000 300m 19456 19456 82944 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:38` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L38
  </details>


- speed=50000, cable_length=40m | 3 different lines | 5 total rows
  - `50000 40m 19456 19456 28672 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L31
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:31` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L31
  </details>

  - `50000 40m 19456 19456 50176 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L30
  </details>

  - `50000 40m 89088 19456 69632 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:30` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L30
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:30` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L30
  </details>


- speed=50000, cable_length=5m | 3 different lines | 5 total rows
  - `50000 5m 19456 19456 26624 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L23
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:23` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L23
  </details>

  - `50000 5m 19456 19456 46080 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L22
  </details>

  - `50000 5m 82944 19456 63488 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:22` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L22
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:22` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L22
  </details>


- speed=800000, cable_length=250m | 2 different lines | 2 total rows
  - `800000 250m 38912 38912 349184 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:43` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L43
  </details>

  - `800000 250m 38912 38912 357376 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:43` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L43
  </details>


- speed=800000, cable_length=300m | 3 different lines | 4 total rows
  - `800000 300m 1198080 38912 1150976 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L42
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:42` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L42
  </details>

  - `800000 300m 38912 38912 411648 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:51` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L51
  </details>

  - `800000 300m 38912 38912 771072 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:42` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L42
  </details>


- speed=800000, cable_length=40m | 3 different lines | 5 total rows
  - `800000 40m 38912 38912 132096 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L35
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:35` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L35
  </details>

  - `800000 40m 38912 38912 245760 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L34
  </details>

  - `800000 40m 410624 38912 362496 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:34` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L34
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:34` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L34
  </details>


- speed=800000, cable_length=5m | 3 different lines | 5 total rows
  - `800000 5m 304128 38912 257024 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L26
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini:26` → original symlink: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-O128/pg_profile_lookup.ini#L1 ; resolved target: https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/ACS-SN5600/pg_profile_lookup.ini#L26
  </details>

  - `800000 5m 38912 38912 175104 0` (1 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini:26` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-V256/pg_profile_lookup.ini#L26
  </details>

  - `800000 5m 38912 38912 95232 0` (2 rows)
  <details>
  <summary>files</summary>

  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C224O8/pg_profile_lookup.ini#L27
  - `device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini:27` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/mellanox/x86_64-nvidia_sn5600-r0/Mellanox-SN5600-C256S1/pg_profile_lookup.ini#L27
  </details>


</details>

<details>
<summary><b>nexthop/x86_64-nexthop_5010-r0</b> (6 conflicting speed/cable_length keys)</summary>

- speed=100000, cable_length=300m | 2 different lines | 3 total rows
  - `100000 300m 0 0 96000 -6 363506` (2 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini:4` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini#L4
  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini:4` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini#L4
  </details>

  - `100000 300m 18796 0 612140 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini:8` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini#L8
  </details>


- speed=400000, cable_length=120000m | 2 different lines | 3 total rows
  - `400000 120000m 0 0 82837504 -6 1454025` (2 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini:10` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini#L10
  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini:10` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini#L10
  </details>

  - `400000 120000m 18796 0 612140 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini:17` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini#L17
  </details>


- speed=400000, cable_length=2000m | 2 different lines | 3 total rows
  - `400000 2000m 0 0 1384000 -6 1454025` (2 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini:9` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini#L9
  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini:9` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini#L9
  </details>

  - `400000 2000m 18796 0 612140 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini:16` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini#L16
  </details>


- speed=400000, cable_length=300m | 2 different lines | 3 total rows
  - `400000 300m 0 0 296000 -6 1454025` (2 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini:8` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini#L8
  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini:8` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini#L8
  </details>

  - `400000 300m 18796 0 612140 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini:15` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini#L15
  </details>


- speed=400000, cable_length=50m | 2 different lines | 3 total rows
  - `400000 50m 0 0 136000 -6 1454025` (2 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini:7` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini#L7
  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini:7` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini#L7
  </details>

  - `400000 50m 18796 0 612140 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini:14` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini#L14
  </details>


- speed=800000, cable_length=300m | 2 different lines | 3 total rows
  - `800000 300m 0 0 564000 -6 1454025` (2 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini:12` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/BALANCED/pg_profile_lookup.ini#L12
  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini:12` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O64/pg_profile_lookup.ini#L12
  </details>

  - `800000 300m 18796 0 612140 0 3556` (1 rows)
  <details>
  <summary>files</summary>

  - `device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini:20` → https://github.com/Bojun-Feng/sonic-buildimage/blob/f56312f86c7e4e10812ea9b83d2e394fd3cad9cf/device/nexthop/x86_64-nexthop_5010-r0/NH-5010-F-O32-C32/BALANCED/pg_profile_lookup.ini#L20
  </details>


</details>
