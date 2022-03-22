# beoneapi

Contains the python library for connecting with the bifrost database. Used by bifrost and beone dashboards.

## Installation

```bash
pip install beoneapi
```

## Usage

```python
import beoneapi
# Call this once before making any other calls.
beoneapi.add_URI("mongodb://user:pass@hostname:27017/dbname")

beoneapi.get_run_list()

```

Or with multiple databases:

```python
import beoneapi

beoneapi.add_URI("mongodb://user:pass@hostname:27017/dbname", "db1")
beoneapi.add_URI("mongodb://user:pass@hostname:27017/dbname", "db2")

beoneapi.get_run_list(connection_name="db1")

beoneapi.get_run_list(connection_name="db2")
```
