import aiohttp
import json
from jsonpath_ng import parse as jp
from utils.templating import render_template
from temporalio import activity

# Mark imports as pass through to allow them in the workflow sandbox
activity.pass_through_imports = [
    "aiohttp",
    "json",
    "jsonpath_ng",
    "jinja2"
]

@activity.defn
async def run_api_step(step: dict, context: dict):
    activity.logger.info("Starting API step execution")
    req = render_template(step["request"], context)
    method = req.get("method", "GET").upper()
    headers = req.get("headers", {})
    body = req.get("body", None)
    activity.logger.debug("Request details - Method: %s, Headers: %s, Body: %s", method, headers, body)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=method,
                url=req["url"],
                headers=headers,
                json=body,
                timeout=aiohttp.ClientTimeout(total=30)
            ) as response:
                response.raise_for_status()
                data = await response.json()
                
                activity.logger.debug("Response data: %s", data)

                if data is None:
                    activity.logger.warning("Received empty response")
                    return {}

                result = {}
                for key, path in step.get("parse", {}).items():
                    try:
                        expr = jp(path)
                        matches = expr.find(data)
                        result[key] = matches[0].value if matches else None
                    except Exception as e:
                        activity.logger.error("Error parsing JSONPath %s: %s", path, str(e))
                        result[key] = None

                activity.logger.info("API step completed successfully")
                return result or data
    except Exception as e:
        activity.logger.error("Request failed: %s", str(e))
        raise
