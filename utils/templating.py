from jinja2 import Template

def render_template(obj, context):
    if isinstance(obj, dict):
        return {k: render_template(v, context) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [render_template(v, context) for v in obj]
    elif isinstance(obj, str):
        return Template(obj).render(**context)
    else:
        return obj

