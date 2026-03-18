# Bitable via tenant_access_token

## Minimal workflow

1. Get tenant token
2. Read field schema first when writing structured data
3. Use the Bitable REST API directly

## Common endpoints

## Reusable helper

After exporting `TENANT_TOKEN`, use the bundled script:

```bash
python3 <skill-dir>/scripts/bitable_records.py fields <app_token> <table_id>
python3 <skill-dir>/scripts/bitable_records.py list <app_token> <table_id>
python3 <skill-dir>/scripts/bitable_records.py create <app_token> <table_id> '{"fields":{"标题":"测试"}}'
python3 <skill-dir>/scripts/bitable_records.py update <app_token> <table_id> <record_id> '{"fields":{"重要程度":"🟡 中"}}'
```


### List records

```bash
curl -s "https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${TABLE_ID}/records?page_size=100" \
  -H "Authorization: Bearer ${TENANT_TOKEN}"
```

### Create record

```bash
curl -s -X POST "https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${TABLE_ID}/records" \
  -H "Authorization: Bearer ${TENANT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "fields": {
      "标题": "BTC突破$75K",
      "日期": 1772121600000,
      "类型": "价格行情",
      "币种": ["BTC"],
      "核心内容": "现货ETF净流入走强，价格突破关键区间。",
      "Cipher 观点": "趋势仍偏强，但短线追高性价比一般，等回踩更优。",
      "重要程度": "🔴 高",
      "来源": {"text": "示例来源", "link": "https://example.com"}
    }
  }'
```

### Update record

```bash
curl -s -X PUT "https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${TABLE_ID}/records/${RECORD_ID}" \
  -H "Authorization: Bearer ${TENANT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"fields": {"重要程度": "🟡 中"}}'
```

## Field-format traps

Always check field types before large writes.

- 日期: millisecond timestamp
- 单选: string
- 多选: string array
- 超链接: `{ "text": "...", "link": "..." }`
- 人员: usually `[{"id":"ou_xxx"}]`
- 附件: uploaded file token objects, not external URLs

## Recommended schema-discovery step

```bash
curl -s "https://open.feishu.cn/open-apis/bitable/v1/apps/${APP_TOKEN}/tables/${TABLE_ID}/fields" \
  -H "Authorization: Bearer ${TENANT_TOKEN}"
```

## Typical permission scopes

At least one of these is usually required depending on endpoint:
- `bitable:app`
- `bitable:app:readonly`
- `base:record:retrieve`

If the API returns `99991672`, surface the permission-application URL from the response.
