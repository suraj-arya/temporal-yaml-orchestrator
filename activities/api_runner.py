import httpx
import json
from jsonpath_ng import parse as jp
from utils.templating import render_template
from temporalio import activity


@activity.defn
async def run_api_step(step: dict, context: dict):
    req = render_template(step["request"], context)
    method = req.get("method", "GET").upper()
    headers = req.get("headers", {})
    body = req.get("body", None)

    response = await httpx.AsyncClient().request(
        method, req["url"], headers=headers, json=body
    )
    data = response.json()
    print(f"data: {data}")

    result = {}
    for key, path in step.get("parse", {}).items():
        expr = jp(path)
        matches = expr.find(data)
        result[key] = matches[0].value if matches else None

    return result or data
