#!/usr/bin/env python3
import json
import os
import sys
import urllib.request

BASE = "https://open.feishu.cn/open-apis/bitable/v1"


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
    if len(sys.argv) < 4:
        die("Usage: bitable_records.py <list|create|update|fields> <app_token> <table_id> [record_id] [json_payload]")

    action = sys.argv[1]
    app_token = sys.argv[2]
    table_id = sys.argv[3]
    token = os.environ.get("TENANT_TOKEN")
    if not token:
        die("TENANT_TOKEN env var is required")

    if action == "list":
        url = f"{BASE}/apps/{app_token}/tables/{table_id}/records?page_size=100"
        print(json.dumps(request("GET", url, token), ensure_ascii=False, indent=2))
        return

    if action == "fields":
        url = f"{BASE}/apps/{app_token}/tables/{table_id}/fields"
        print(json.dumps(request("GET", url, token), ensure_ascii=False, indent=2))
        return

    if action == "create":
        if len(sys.argv) < 5:
            die("create requires json_payload")
        payload = json.loads(sys.argv[4])
        url = f"{BASE}/apps/{app_token}/tables/{table_id}/records"
        print(json.dumps(request("POST", url, token, payload), ensure_ascii=False, indent=2))
        return

    if action == "update":
        if len(sys.argv) < 6:
            die("update requires record_id and json_payload")
        record_id = sys.argv[4]
        payload = json.loads(sys.argv[5])
        url = f"{BASE}/apps/{app_token}/tables/{table_id}/records/{record_id}"
        print(json.dumps(request("PUT", url, token, payload), ensure_ascii=False, indent=2))
        return

    die(f"Unknown action: {action}")


if __name__ == "__main__":
    main()
