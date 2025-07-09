from fastapi import APIRouter, Request, Header
import json
from ..utils.verify_signature import verify_signature, SECRET

router = APIRouter(prefix="/webhooks", tags=["webhooks"])

@router.post("/github")
async def github_webhook(
    request: Request,
    x_github_event: str | None = Header(None),
    x_hub_signature_256: str | None = Header(None),
):
    raw = await request.body()

    if verify_signature(raw, x_hub_signature_256):
        print("Signature verified")
    else:
        print("Invalid signature")

    payload = json.loads(raw)

    print(f"EVENT: {x_github_event}")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    return {"ok": True}
