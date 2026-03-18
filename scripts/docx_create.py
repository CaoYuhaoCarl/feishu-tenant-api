#!/usr/bin/env python3
import json
import os
import sys
import urllib.request


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def request(method, url, token, body=None):
    headers = {"Authorization": f"Bearer {token}"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    if len(sys.argv) < 2:
        die("Usage: docx_create.py <title> [folder_token]")

    token = os.environ.get("TENANT_TOKEN")
    if not token:
        die("TENANT_TOKEN env var is required")

    title = sys.argv[1]
    body = {"title": title}
    if len(sys.argv) >= 3 and sys.argv[2]:
        body["folder_token"] = sys.argv[2]

    url = "https://open.feishu.cn/open-apis/docx/v1/documents"
    print(json.dumps(request("POST", url, token, body), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
