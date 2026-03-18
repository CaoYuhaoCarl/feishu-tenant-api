# feishu-tenant-api

Cross-workspace OpenClaw skill for accessing Feishu / Lark APIs with `tenant_access_token`.

用于在 **非飞书渠道**（Telegram / Discord / cron / sub-agent / 其他 workspace）里，直接访问飞书 / Lark API 的 OpenClaw Skill。

---

## English

### What this is

`feishu-tenant-api` is an OpenClaw skill that lets agents access Feishu / Lark APIs using **app identity** (`tenant_access_token`) instead of channel-bound user authorization.

This is useful when:
- the current agent is not running inside a Feishu chat
- Feishu plugin MCP tools are unavailable in the current workspace/session
- you want stable machine-level access for Bitable, Docs, Drive, etc.

### What it includes

- `SKILL.md` — trigger rules and usage guidance
- `scripts/get_feishu_tenant_token.sh` — get `tenant_access_token` from `~/.openclaw/openclaw.json`
- `scripts/bitable_records.py` — Bitable helper for `fields / list / create / update`
- `scripts/docx_create.py` — create Feishu docs via API
- `references/bitable.md` — Bitable API notes and examples
- `references/docs-drive.md` — Docs / Drive notes and examples
- `references/tools-template.md` — recommended `TOOLS.md` convention for each workspace

### Requirements

- OpenClaw configured with Feishu channel credentials in:
  - `~/.openclaw/openclaw.json`
- Feishu app scopes granted in Open Platform
- Python 3 and shell access

### Quick start

#### 1. Get a tenant token

```bash
bash scripts/get_feishu_tenant_token.sh
```

#### 2. List Bitable records

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/bitable_records.py list <app_token> <table_id>
```

#### 3. Create a Feishu doc

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/docx_create.py "Weekly Note" <folder_token>
```

### Common permission issue

If Feishu returns error `99991672`, the app is missing required scopes.
Open the permission request link returned by the API response, grant the scopes, then retry.

### Recommended use

In each workspace, store resource IDs in `TOOLS.md`, for example:
- Bitable app token
- table ID
- doc token / folder token
- schema notes
- verified permissions date

---

## 中文

### 这是什么

`feishu-tenant-api` 是一个 OpenClaw Skill，用来让 agent 在 **不依赖飞书会话授权** 的情况下，直接用 **应用身份**（`tenant_access_token`）访问飞书 / Lark API。

适用场景：
- 当前 agent 不在飞书聊天里运行
- 当前 workspace / session 拿不到飞书插件注入的 MCP 工具
- 想稳定访问多维表格、云文档、云盘等资源

### 包含内容

- `SKILL.md` — Skill 触发条件与使用说明
- `scripts/get_feishu_tenant_token.sh` — 从 `~/.openclaw/openclaw.json` 获取 `tenant_access_token`
- `scripts/bitable_records.py` — 多维表格辅助脚本，支持 `fields / list / create / update`
- `scripts/docx_create.py` — 通过 API 创建飞书文档
- `references/bitable.md` — 多维表格 API 示例与注意事项
- `references/docs-drive.md` — 云文档 / 云盘相关说明
- `references/tools-template.md` — 推荐的 workspace `TOOLS.md` 约定模板

### 依赖要求

- OpenClaw 已配置飞书渠道凭证，位置：
  - `~/.openclaw/openclaw.json`
- 飞书开放平台里已开通对应应用权限
- 本机可用 Python 3 和 shell

### 快速开始

#### 1. 获取 tenant token

```bash
bash scripts/get_feishu_tenant_token.sh
```

#### 2. 查询多维表格记录

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/bitable_records.py list <app_token> <table_id>
```

#### 3. 创建飞书文档

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/docx_create.py "周报" <folder_token>
```

### 常见权限问题

如果飞书接口返回 `99991672`，说明应用权限没开全。
直接打开 API 返回里的权限申请链接，补齐权限后再重试。

### 推荐做法

在每个 workspace 的 `TOOLS.md` 里登记资源信息，例如：
- 多维表格 app token
- table ID
- 文档 token / folder token
- 字段结构说明
- 权限验证日期

---

## Repo

GitHub: <https://github.com/CaoYuhaoCarl/feishu-tenant-api>
