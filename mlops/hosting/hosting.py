from huggingface_hub import HfApi
import os
import time

api = HfApi(token=os.environ.get("HF_TOKEN"))

for attempt in range(5):
    try:
        api.upload_folder(
            folder_path="mlops/deployment",
            repo_id="jasreman8/Bank-Customer-Churn",
            repo_type="space",
            path_in_repo="",
        )
        print("Upload successful.")
        break
    except Exception as e:
        if "429" in str(e) and attempt < 4:
            wait = 60 * (attempt + 1)
            print(f"Rate limited. Retrying in {wait}s... (attempt {attempt+1}/5)")
            time.sleep(wait)
        else:
            raise
