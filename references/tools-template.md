# TOOLS.md template for workspace-local Feishu resources

Copy this pattern into each workspace's `TOOLS.md`.

## Feishu cross-channel access

- **Auth mode:** tenant_access_token via `channels.feishu.appId` + `channels.feishu.appSecret` in `~/.openclaw/openclaw.json`
- **Token helper:** `~/.agents/skills/feishu-tenant-api/scripts/get_feishu_tenant_token.sh`
- **Bitable helper:** `~/.agents/skills/feishu-tenant-api/scripts/bitable_records.py`
- **Doc helper:** `~/.agents/skills/feishu-tenant-api/scripts/docx_create.py`
- **Scope rule:** if API returns permission denied / `99991672`, open the permission request link from the response and grant app scopes first

### Resource registry template

#### <Resource Name>
- **Type:** bitable | docx | drive folder | wiki | sheet
- **Link:** <human URL>
- **App token / file token:** <token>
- **Table ID:** <table id, if bitable>
- **Folder token:** <folder token, if relevant>
- **Key fields / schema notes:**
  - <field>: <type / constraints>
- **Known working operations:** read / create / update / list
- **Permissions confirmed:** <date>

### Example usage

```bash
export TENANT_TOKEN=$(bash ~/.agents/skills/feishu-tenant-api/scripts/get_feishu_tenant_token.sh)
python3 ~/.agents/skills/feishu-tenant-api/scripts/bitable_records.py list <app_token> <table_id>
python3 ~/.agents/skills/feishu-tenant-api/scripts/docx_create.py "Weekly Note" <folder_token>
```
