# Data integrity demo

A small, dependency-free Python validator. The sample data is synthetic.

```bash
python validate_data.py sample_data/source.csv sample_data/target.csv --key id
```

Expected output: 1 key missing in target (`4`), 1 missing in source (`6`), and 1 field mismatch (`amount` for key `2`), then `RESULT: FAIL` with exit code 1, so it can be wired into a pipeline.

Extend it to read from databases or APIs by replacing `load()`.
