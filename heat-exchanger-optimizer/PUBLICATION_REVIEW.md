# Publication review

## Included

Thermal calculations, multi-exchanger configuration models, predictive fouling and
cleaning-cost logic, frontend pages and charts, parameterised SQL adapters, generic
offline preparation/review/backtesting utilities, documentation and regression checks.

## Excluded or replaced

- Real environment files, fixed login credentials and database connection settings.
- Company spreadsheets, documents, raw/processed operating records and model outputs.
- Actual equipment identifiers, sensor tags, design settings, cleaning histories and costs.
- Company-specific export utilities, per-machine data-processing scripts and workbook-bound tests.
- Virtual environments, caches, editor/assistant histories, archives and local commands.

The example equipment, sensor values, economic assumptions and generated histories are
invented. SQL queries contain code and column contracts, not database records.
The original supplied directory was not edited.

## Checks completed

- Checked all publication files for private network addresses, credential/key patterns,
  company-specific references and personal email addresses: no matches found.
- Compared against 103 original credential/equipment-identifier candidates without printing
  their values: no matches found in the publication copy.
- Parsed all included Python source and checked JavaScript syntax: passed.
- Ran 14 numerical, synthetic-data, database-isolation and route-handler checks: passed.
- Checked staged Git content for whitespace errors and confirmed private runtime files are ignored.
- Started a fresh local Git history; no source-directory Git objects were imported.

An HTTP server integration attempt was blocked by this execution environment's local
networking behavior. HTTP/browser execution and optional SQL integration have not been
validated here. Generic offline utilities were checked for syntax, not backtested against
company data. These checks reduce disclosure risk and do not guarantee detection of every
possible sensitive detail. Future changes require another review.
