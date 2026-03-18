# feishu-tenant-api

[English](#english) | [中文](#中文)

---

## English

### Overview

`feishu-tenant-api` is an OpenClaw skill for accessing Feishu / Lark APIs with `tenant_access_token`.

It is designed for cases where an agent needs to work with Feishu resources **outside a Feishu chat session**, such as:
- Telegram agents
- Discord agents
- cron jobs
- sub-agents
- other workspaces without Feishu MCP tool injection

Instead of relying on channel-bound user authorization, this skill uses **app identity** from `~/.openclaw/openclaw.json`.

### Included files

- `SKILL.md` — trigger rules and usage guidance
- `scripts/get_feishu_tenant_token.sh` — get `tenant_access_token`
- `scripts/bitable_records.py` — helper for Bitable `fields / list / create / update`
- `scripts/docx_create.py` — create Feishu docs via API
- `references/bitable.md` — Bitable API examples and notes
- `references/docs-drive.md` — Docs / Drive API notes
- `references/tools-template.md` — recommended `TOOLS.md` convention

### Requirements

- OpenClaw with Feishu credentials configured in:
  - `~/.openclaw/openclaw.json`
- Required Feishu app scopes granted in Open Platform
- Python 3
- Shell access

### Quick start

#### Get tenant token

```bash
bash scripts/get_feishu_tenant_token.sh
```

#### List Bitable records

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/bitable_records.py list <app_token> <table_id>
```

#### Create a Feishu doc

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/docx_create.py "Weekly Note" <folder_token>
```

### Common permission issue

If the API returns error `99991672`, the app is missing required scopes.
Open the permission request link returned in the API response, grant the scopes, and retry.

### Recommended workspace convention

In each workspace, store resource metadata in `TOOLS.md`, for example:
- Bitable app token
- table ID
- doc token / folder token
- schema notes
- verified permissions date

---

## 中文

### 简介

`feishu-tenant-api` 是一个 OpenClaw Skill，用来通过 `tenant_access_token` 访问飞书 / Lark API。

它适用于 agent **不在飞书聊天上下文里运行** 的场景，比如：
- Telegram agent
- Discord agent
- cron 定时任务
- sub-agent
- 没有飞书 MCP 工具注入的其他 workspace

这个 Skill 不依赖用户会话授权，而是直接使用 `~/.openclaw/openclaw.json` 中配置的**应用身份**。

### 包含文件

- `SKILL.md` — Skill 触发条件与使用说明
- `scripts/get_feishu_tenant_token.sh` — 获取 `tenant_access_token`
- `scripts/bitable_records.py` — 多维表格辅助脚本，支持 `fields / list / create / update`
- `scripts/docx_create.py` — 通过 API 创建飞书文档
- `references/bitable.md` — 多维表格 API 示例与注意事项
- `references/docs-drive.md` — 云文档 / 云盘 API 说明
- `references/tools-template.md` — 推荐的 `TOOLS.md` 配置约定

### 依赖要求

- OpenClaw 已配置飞书凭证，位置：
  - `~/.openclaw/openclaw.json`
- 飞书开放平台中已开通所需应用权限
- Python 3
- shell 环境

### 快速开始

#### 获取 tenant token

```bash
bash scripts/get_feishu_tenant_token.sh
```

#### 查询多维表格记录

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/bitable_records.py list <app_token> <table_id>
```

#### 创建飞书文档

```bash
export TENANT_TOKEN=$(bash scripts/get_feishu_tenant_token.sh)
python3 scripts/docx_create.py "周报" <folder_token>
```

### 常见权限问题

如果接口返回 `99991672`，说明应用权限没有开全。
打开 API 返回中的权限申请链接，补齐权限后再重试。

### 推荐的 workspace 约定

建议在每个 workspace 的 `TOOLS.md` 中登记资源信息，例如：
- 多维表格 app token
- table ID
- 文档 token / folder token
- 字段结构说明
- 权限验证日期
