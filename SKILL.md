---
name: feishu-tenant-api
description: Access Feishu/Lark APIs from any channel or workspace using tenant_access_token (app identity) instead of channel-bound user auth. Use when a non-Feishu agent (Telegram, Discord, local, cron, sub-agent, ACP session) needs to read or write Feishu Bitable, Docs, Drive, or other OpenAPI resources created in Feishu. Especially useful for cross-workspace reuse where the Feishu plugin tools are unavailable but app_id/app_secret are configured in openclaw.json.
---

# Feishu Tenant API

Use this skill when the current agent cannot rely on Feishu-session-only auth or MCP tools, but the machine already has Feishu app credentials in `~/.openclaw/openclaw.json`.

## Core pattern

1. Read `appId` and `appSecret` from `~/.openclaw/openclaw.json`
2. Exchange them for a `tenant_access_token`
3. Call the target Feishu OpenAPI endpoint with `Authorization: Bearer <token>`
4. Store stable resource IDs (`app_token`, `table_id`, `document_id`, folder tokens) in the workspace's `TOOLS.md` or another workspace-local config file

## When this is better than user auth

Prefer tenant token when:
- The task must work from Telegram / Discord / cron / sub-agents / other workspaces
- You want stable machine-level access without 2-hour user token expiry
- The Feishu app already has the required scopes

Do **not** assume tenant token can do everything. Some APIs require user identity or user-granted scopes. If tenant-token calls fail with permission errors, check app scopes first.

## Read only what you need

- For Bitable specifics, read `references/bitable.md`
- For Docs/Drive specifics, read `references/docs-drive.md`
- For workspace-local config conventions, read `references/tools-template.md`
- For reusable helpers, use:
  - `scripts/get_feishu_tenant_token.sh`
  - `scripts/bitable_records.py`
  - `scripts/docx_create.py`

## Fast path

Run the helper script to get a token:

```bash
bash <skill-dir>/scripts/get_feishu_tenant_token.sh
```

Then call APIs like:

```bash
curl -s "https://open.feishu.cn/open-apis/bitable/v1/apps/$APP_TOKEN/tables/$TABLE_ID/records?page_size=100" \
  -H "Authorization: Bearer $TENANT_TOKEN"
```

## Required checks

Before saying access is broken, verify all three:

1. `channels.feishu.appId` and `channels.feishu.appSecret` exist in `~/.openclaw/openclaw.json`
2. The Feishu app has the required scopes in Open Platform
3. The target resource ID is correct and accessible to the app

## Common failure mode

Error `99991672` means missing app scope. The response usually includes a direct permission-application link. Surface that link to the user and retry after they confirm permissions were granted.

## Workspace convention

For reusable setups, record the following in each workspace that uses the resource:
- resource name
- direct link
- app/document/app tokens
- table IDs if applicable
- field schema notes if using Bitable
- confirmed permission status and date

## Keep it lean

Do not build a full SDK unless the workflow truly needs it. For most tasks, one token request + one API request is enough.
