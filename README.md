# feishu-tenant-api

[中文](./README.zh-CN.md)

Cross-workspace OpenClaw skill for accessing Feishu / Lark APIs with `tenant_access_token`.

## Overview

`feishu-tenant-api` is an OpenClaw skill for accessing Feishu / Lark APIs with `tenant_access_token`.

It is designed for cases where an agent needs to work with Feishu resources **outside a Feishu chat session**, such as:
- Telegram agents
- Discord agents
- cron jobs
- sub-agents
- other workspaces without Feishu MCP tool injection

Instead of relying on channel-bound user authorization, this skill uses **app identity** from `~/.openclaw/openclaw.json`.

## Included files

- `SKILL.md` — trigger rules and usage guidance
- `scripts/get_feishu_tenant_token.sh` — get `tenant_access_token`
- `scripts/bitable_records.py` — helper for Bitable `fields / list / create / update`
- `scripts/docx_create.py` — create Feishu docs via API
- `references/bitable.md` — Bitable API examples and notes
- `references/docs-drive.md` — Docs / Drive API notes
- `references/tools-template.md` — recommended `TOOLS.md` convention

## Requirements

- OpenClaw with Feishu credentials configured in:
  - `~/.openclaw/openclaw.json`
- Required Feishu app scopes granted in Open Platform
- Python 3
- Shell access

## Quick start

### Get tenant token

```bash
bash scripts/get_feishu_tenant_token.sh
```

### List Bitable records

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/bitable_records.py list <app_token> <table_id>
```

### Create a Feishu doc

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/docx_create.py "Weekly Note" <folder_token>
```

## Common permission issue

If the API returns error `99991672`, the app is missing required scopes.
Open the permission request link returned in the API response, grant the scopes, and retry.

## Recommended workspace convention

In each workspace, store resource metadata in `TOOLS.md`, for example:
- Bitable app token
- table ID
- doc token / folder token
- schema notes
- verified permissions date
