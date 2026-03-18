#!/usr/bin/env bash
set -euo pipefail

CONFIG="${1:-$HOME/.openclaw/openclaw.json}"

APP_ID=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["channels"]["feishu"]["appId"])' "$CONFIG")
APP_SECRET=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["channels"]["feishu"]["appSecret"])' "$CONFIG")

RESP=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d "{\"app_id\":\"${APP_ID}\",\"app_secret\":\"${APP_SECRET}\"}")

python3 -c 'import json,sys; resp=json.loads(sys.argv[1]); code=resp.get("code",0); exit(print(resp["tenant_access_token"]) is None) if code==0 else (_ for _ in ()).throw(SystemExit(json.dumps(resp, ensure_ascii=False)))' "$RESP"
