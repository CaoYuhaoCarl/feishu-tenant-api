# Docs and Drive via tenant_access_token

Use tenant token for machine-level access to Feishu Docs/Drive resources when app scopes are sufficient.

## Common endpoints

## Reusable helper

After exporting `TENANT_TOKEN`, create a doc with:

```bash
python3 <skill-dir>/scripts/docx_create.py "新建文档标题" <folder_token>
```


### Get document raw content

For newer docs APIs, endpoint choice varies by doc type. Start from Drive metadata when unsure.

### Get file metadata

```bash
curl -s "https://open.feishu.cn/open-apis/drive/v1/files/${FILE_TOKEN}" \
  -H "Authorization: Bearer ${TENANT_TOKEN}"
```

### List folder contents

```bash
curl -s "https://open.feishu.cn/open-apis/drive/v1/files?folder_token=${FOLDER_TOKEN}&page_size=50" \
  -H "Authorization: Bearer ${TENANT_TOKEN}"
```

### Create a doc

```bash
curl -s -X POST "https://open.feishu.cn/open-apis/docx/v1/documents" \
  -H "Authorization: Bearer ${TENANT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"title":"新建文档标题","folder_token":"YOUR_FOLDER_TOKEN"}'
```

## Notes

- Feishu has multiple document families (`docs`, `docx`, sheets, wiki). Confirm the resource type before choosing the endpoint.
- Some content-editing flows are block-based rather than raw markdown/text replacement.
- If a dedicated Feishu doc skill/tool is available in-channel, prefer that for rich doc editing. Use tenant-token REST calls as the cross-channel fallback.

## Typical scopes

Depending on action, you may need app scopes like:
- `drive:drive`
- `drive:drive:readonly`
- `docx:document`
- `docx:document:readonly`

If you get an access-denied response, extract the permission request link and send it to the user.
